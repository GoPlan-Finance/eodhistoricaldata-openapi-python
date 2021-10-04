# openapi_client.AssetsApi

All URIs are relative to *https://eodhistoricaldata.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_fundamentals_general_section**](AssetsApi.md#asset_fundamentals_general_section) | **GET** /fundamentals/{ticker}?fmt&#x3D;json&amp;filter&#x3D;General | Get Asset fundamentals
[**real_time_quote**](AssetsApi.md#real_time_quote) | **GET** /real-time/{ticker}?fmt&#x3D;json | Get Asset fundamentals
[**search_asset**](AssetsApi.md#search_asset) | **GET** /search/{query} | Search symbols


# **asset_fundamentals_general_section**
> AssetFundamentalsSectionGeneral asset_fundamentals_general_section(ticker)

Get Asset fundamentals

### Example

* Api Key Authentication (api_token):
```python
import time
import openapi_client
from openapi_client.api import assets_api
from openapi_client.model.asset_fundamentals_section_general import AssetFundamentalsSectionGeneral
from pprint import pprint
# Defining the host is optional and defaults to https://eodhistoricaldata.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://eodhistoricaldata.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    ticker = "ticker_example" # str | Asset Ticker

    # example passing only required values which don't have defaults set
    try:
        # Get Asset fundamentals
        api_response = api_instance.asset_fundamentals_general_section(ticker)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AssetsApi->asset_fundamentals_general_section: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Asset Ticker |

### Return type

[**AssetFundamentalsSectionGeneral**](AssetFundamentalsSectionGeneral.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **real_time_quote**
> [AssetQuote] real_time_quote(ticker)

Get Asset fundamentals

### Example

* Api Key Authentication (api_token):
```python
import time
import openapi_client
from openapi_client.api import assets_api
from openapi_client.model.asset_quote import AssetQuote
from pprint import pprint
# Defining the host is optional and defaults to https://eodhistoricaldata.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://eodhistoricaldata.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    ticker = "ticker_example" # str | Asset Ticker
    s = "AAPL.US,GOOG.US" # str | Extra tickers to fetch separated by a \",\" (Max recommended by EOD is 15-20 tickers) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Asset fundamentals
        api_response = api_instance.real_time_quote(ticker)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AssetsApi->real_time_quote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Asset fundamentals
        api_response = api_instance.real_time_quote(ticker, s=s)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AssetsApi->real_time_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Asset Ticker |
 **s** | **str**| Extra tickers to fetch separated by a \&quot;,\&quot; (Max recommended by EOD is 15-20 tickers) | [optional]

### Return type

[**[AssetQuote]**](AssetQuote.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_asset**
> [SymbolSearch] search_asset(query)

Search symbols

### Example

* Api Key Authentication (api_token):
```python
import time
import openapi_client
from openapi_client.api import assets_api
from openapi_client.model.symbol_search import SymbolSearch
from pprint import pprint
# Defining the host is optional and defaults to https://eodhistoricaldata.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://eodhistoricaldata.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = assets_api.AssetsApi(api_client)
    query = "query_example" # str | Name of ticker or search string

    # example passing only required values which don't have defaults set
    try:
        # Search symbols
        api_response = api_instance.search_asset(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AssetsApi->search_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Name of ticker or search string |

### Return type

[**[SymbolSearch]**](SymbolSearch.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

