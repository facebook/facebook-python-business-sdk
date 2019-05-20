# Changelog

All notable changes to this project will be documented in this file.


## Unreleased

## v3.3.3
### Fix
[PR542](https://github.com/facebook/facebook-python-business-sdk/pull/542)
[PR541](https://github.com/facebook/facebook-python-business-sdk/pull/541/)

## v3.3.2
### Changed
- Remove list of API call from Business SDK, any [these APIs](https://developers.facebook.com/docs/graph-api/changelog/4-30-2019-endpoint-deprecations) included in Business SDK will be deprecated.   

## v3.3.0
### Changed
- Graph API call upgrade to [v3.3](https://developers.facebook.com/docs/graph-api/changelog/version3.3)
### Deprecated
- `parent_id` in `AbstractCrudObject`.
- Function `remote_create`, `remote_read`, `remote_update` and `remote_delete` for `AbstractCrudObject`. Check out our [recommended way](https://github.com/facebook/facebook-python-business-sdk#exploring-the-graph) to make API call with python SDK.
