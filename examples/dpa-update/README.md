# Dynamic Products Update

## What's this example about?

[Facebook dynamic product ads](https://developers.facebook.com/docs/marketing-api/dynamic-product-ads/)
helps you promote relevant products to shoppers browsing your product catalog on
your website or mobile app.

This example shows how to update specific products in a catalog by changing
their price or putting them out of stock.

This example has 3 parts:
- An XML product feed
- A script that reads this feed and randomly updates the price of some products
- A script that uses Ads API to update product prices in a product catalog

## Pre-requisites
- A [Business Manager](https://business.facebook.com)
- A product catalog based on the XML feed provided
- The standard pre-requisites for other usage examples from Python Ads SDK

## How to run
1. Make sure product feed has been created and products are loaded
2. Edit `dpa_update.py` and put your catalog ID in `catalog_id` variable
3. `python stock_update.py feed-dpa.xml 3` will choose three products to update.
Pipe its output into `dpa_update.py`. That is:
`python stock_update.py feed-dpa.xml 3 | python dpa_update.py`
4. Check updated prices on your catalog
