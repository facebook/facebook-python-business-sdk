
===============================
Facebook Ads API SDK for Python
===============================

facebookads provides an interface between your python application and Facebook's
Ads API.


1. Install
==========

Via pip::

    pip install facebookads

Downloaded package::

    python setup.py install


2. Your Facebook App
====================

To get started with the sdk you must have a Facebook app registered at
https://developers.facebook.com/. In addition, your app must be approved for
Ads API usage and have all migrations enabled. Learn more about the Ads API at
https://developers.facebook.com/docs/ads-api.

To get started with the examples provided in the examples/ folder, you need:

- an app id
- app secret
- an access token

.. note:: The access token must be from the app above.

It is expected that an app in production will build its own infrastructure to
interact with a user to generate an access token and choose an account to
manage. To learn more about access tokens go to
https://developers.facebook.com/docs/reference/ads-api/overview/.

Authentication
--------------

Import the sdk::

    import facebookads

Assuming you have a user with an access token, set up a ``FacebookSession``::

    from facebookads.session import FacebookSession
    session = FacebookSession(<app_id>, <app_secret>, <access_token>)

Set up an ``FacebookAdsApi`` instance using this session::

    from facebookads.api import FacebookAdsApi
    api = FacebookAdsApi(session)

If you do not want to specify the api instance when instantiating graph objects,
you can set an api instance as the default api instance through which objects
will interface::

    FacebookAdsApi.set_default_api(api)


3. CRUD design
==============

The SDK implements a CRUD (create, read, update, delete) design. Objects
relevant to exploring the graph are located in the objects module of the
facebookads package.

All objects on the graph are instances of ``AbstractObject``. Some objects can
be directly queried and thus are instances of ``AbstractCrudObject`` (a subclass
of ``AbstractObject``). Both these abstract classes are located in
facebookads.objects.

AbstractCrudObject can have all or some of the following methods:

- remote_create
- remote_read
- remote_update
- remote_delete

For example, AdCampaign has all these methods but AdAccount does not. Read the
Ads API documentation for more information about how different ad objects are
used.

Let's get all the ad accounts for the user with the given access token. Notice
we will not specify a keyword argument ``api=api`` when instantiating the
``AdUser`` object because we've above set the default api. Also notice that
we wrap the return value of ``get_ad_accounts`` with ``list()`` because
``get_ad_accounts`` returns an ``EdgeIterator`` and we want to get the full
list right away instead of having the iterator lazily loading accounts as we
iterate through it::

    import facebookads.objects as objects

    me = objects.AdUser(fbid='me')
    my_accounts = list(me.get_ad_accounts())

We shall work with the following account, assuming the user chose the first one.
You probably also only have one ad account::

    my_account = my_accounts[0]

.. note:: If you want to work with an account for which you already know its
   id, you can directly instantiate an AdAccount object by giving it an fbid
   parameter (e.g. ``fbid='act_xyz'``). The user must have permission to use the
   account, of course.


3. Create
=========

Let's create an AdCampaign. We can go to
https://developers.facebook.com/docs/reference/ads-api/adcampaign to make sure
we are following the creation requirements::

    campaign = my_account.child(objects.AdCampaign)
    campaign[objects.AdCampaign.Field.name] = "FooBar Campain"
    campaign[objects.AdCampaign.Field.status] = objects.AdCampaign.Status.paused
    campaign.remote_create()


4. Read
=======

We can also read properties of an object from the api assuming that the object
is already created and has a node path. Accessing properties of an object is
simple since AbstractObjects implement the collections.MutableMapping. You can
access them just like accessing a key of a dictionary::
    
    my_account.remote_read(fields=[objects.AdAccount.Field.amount_spent])
    print("Amount spent by account %s: %s" % (
        my_account.get_id(),
        my_account[objects.AdAccount.Field.amount_spent],
    )


5. Update
=========

To update an object, we can modify its properties and then call the
``remote_update`` method to sync the object with the server::
    
    # Correcting typo "Campain" -> "Campaign"
    campaign[objects.AdCampaign.Field.name] = "FooBar Campaign"
    campaign.remote_update()


6. Delete
=========

We decide we don't want this campaign anymore::

    campaign.remote_delete()


7. Parameters and File Attachments
==================================

All CRUD calls support a ``params`` keyword argument which takes a dictionary
mapping paramater names to values in case advanced modification is required.

``remote_create`` and ``remote_update`` support a ``files`` keyword argument
which takes a dictionary mapping file reference names to binary opened file
objects.

``remote_read`` supports a ``fields`` keyworkd argument which is a convenient
way of specifying the 'fields' parameter. ``fields`` takes a list of fields
which should be read during the call.


8. Exploring Edges
==================

You can explore the edge of an object by instantiating an ``EdgeIterator`` (
available in facebookads.objects). In addition, there are also methods you may
find in the class and method documentation which are a convenient way to
get these iterators. For example, above we iterated over all the accounts
associated with a user by calling the ``get_ad_accounts`` method on the
``AdUser``.


9. Batch Calls
==============

It is efficient to group together large numbers of calls into one http request.
The SDK makes this process simple. You can group together calls into an instance
of ``FacebookAdsApiBatch`` (available in facebookads.api). To easily get one
for your api instance::

    my_api_batch = api.new_batch()

Calls can be added to the batch instead of being executed immediately::

    campaign.delete(batch=my_api_batch)

Once you're finished adding calls to the batch, you can send off the request::

    my_api_batch.execute()

Please follow batch call guidelines in the Ads API documentation. There are
optimal numbers of calls per batch. In addition, you may need to watch out that
for rate limiting as a batch call simply improves network performance and each
call does count individually towards rate limiting.


10. Exceptions
==============

See ``facebookads.exceptions`` for a list of exceptions which may be thrown by
the SDK.


11. Tests
=========

You may run the tests on your own account by executing the following, making
sure to fill in your own app and account information::

    python -m facebookads.test.tests app_id app_secret access_token account_id

Or::

    python3 -m facebookads.test.tests app_id app_secret access_token account_id


12. Examples
============

Examples of usage are located in the examples/ folder.
