# Changelog

All notable changes to this project will be documented in this file.


## Unreleased

## v3.3.0
### Changed
- Graph API call upgrade to [v3.3](https://developers.facebook.com/docs/graph-api/changelog/version3.3)
### Deprecated
- `parent_id` in `AbstractCrudObject`.
- Function `remote_create`, `remote_read`, `remote_update` and `remote_delete` for `AbstractCrudObject`. Check out our [recommended way](https://github.com/facebook/facebook-python-business-sdk#exploring-the-graph) to make API call with python SDK.
