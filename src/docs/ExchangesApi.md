# openapi_client.ExchangesApi

All URIs are relative to *https://eodhistoricaldata.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_echanges**](ExchangesApi.md#list_echanges) | **GET** /exchanges-list | Search symbols
[**list_symbols**](ExchangesApi.md#list_symbols) | **GET** /exchange-symbol-list/{exchangeCode}?fmt&#x3D;json | Search symbols


# **list_echanges**
> [Exchange] list_echanges()

Search symbols

### Example

* Api Key Authentication (api_token):
```python
import time
import openapi_client
from openapi_client.api import exchanges_api
from openapi_client.model.exchange import Exchange
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
    api_instance = exchanges_api.ExchangesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Search symbols
        api_response = api_instance.list_echanges()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExchangesApi->list_echanges: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Exchange]**](Exchange.md)

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

# **list_symbols**
> [Symbol] list_symbols(exchange_code)

Search symbols

### Example

* Api Key Authentication (api_token):
```python
import time
import openapi_client
from openapi_client.api import exchanges_api
from openapi_client.model.symbol import Symbol
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
    api_instance = exchanges_api.ExchangesApi(api_client)
    exchange_code = "exchangeCode_example" # str | ExchangeCode

    # example passing only required values which don't have defaults set
    try:
        # Search symbols
        api_response = api_instance.list_symbols(exchange_code)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ExchangesApi->list_symbols: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_code** | **str**| ExchangeCode |

### Return type

[**[Symbol]**](Symbol.md)

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

