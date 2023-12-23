# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

## v17.0.0


### Added
- `advanced_measurement_table` field to Event for Conversion API

## v11.0.0


### Changed
- Graph API call upgrade to [v11.0]https://developers.facebook.com/docs/graph-api/changelog/version11.0

## v10.0.1

### Added
- Support for sending multiple values for certain UserData parameters to Conversions API.

## v10.0.0

### Changed
- Graph API call upgrade to [v10.0](https://developers.facebook.com/docs/graph-api/changelog/version10.0)
## v9.0.1


### Added
- `action_source` field to Event for Conversions API.

### Fixed
- Enum compatibility for Python 2.7

## v9.0.0

### Changed
- Graph API call upgrade to [v9.0](https://developers.facebook.com/docs/graph-api/changelog/version9.0)

## v8.0.5

### Added
- `delivery_category` field to Content for Conversions API.

### Added
- Added HttpServiceInterface to enable the default request object to be overridden by a user-defined HTTP Request Service object. Available for Conversions API create event requests.
- Added batching to Conversions API. Create batched event requests by using BatchProcessor.

## v8.0.3
### Added
- Added partner_agent field to Conversions API EventRequest and EventRequestAsync.
- Added async support to Conversions API - Create event request promises by using EventRequestAsync.
- `lead_id` field to the Conversions API `user_data` section.

## v8.0.0

### Changed
- Graph API call upgrade to [v8.0](https://developers.facebook.com/docs/graph-api/changelog/version8.0)

### Fixed
- Fixed `delivery_category` field being mandatory in custom_data section for Conversions API.

## v7.0.4
### Added
- `delivery_category` field in custom_data section for Conversions API(formerly Serverside API).

## v7.0.3
### Added
- Added support for data processing options in Serverside API. For more details see : https://developers.facebook.com/docs/marketing-apis/data-processing-options

## v7.0.1
### Fixed
- Adding Python 2.7 compatibility for ServerSide API

## v7.0.0
### Changed
- Graph API call upgrade to [v7.0](https://developers.facebook.com/docs/graph-api/changelog/version7.0)

## v6.0.0
### Changed
- Graph API call upgrade to [v6.0](https://developers.facebook.com/docs/graph-api/changelog/version6.0)

## v5.0.3
### Changed
 - Strongly typed Server-Side API support for python (https://developers.facebook.com/docs/marketing-api/facebook-pixel/server-side-api)
### Fix
  - Pull request 554 (`get_insights_async()`) resolved

## v5.0.1

### Added
  - Added `CrashRepoter`, more context available [here](https://developers.facebook.com/docs/business-sdk/guides/crash-reports)

## v5.0.0
### Changed
- Graph API call upgrade to [v5.0](https://developers.facebook.com/docs/graph-api/changelog/version5.0)

## v4.0.6

### Fixed
 - Add back `source` param in `adaccount.create_ad_video`.

## v4.0.0
### Changed
- Graph API call upgrade to [v4.0](https://developers.facebook.com/docs/graph-api/changelog/version4.0)

## v3.3.5
### Fix
[PR543](https://github.com/facebook/facebook-python-business-sdk/pull/543)

## v3.3.4

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

