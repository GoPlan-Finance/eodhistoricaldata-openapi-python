"""
    EOD Historical Data API

    EOD Historical Data API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sam@sddproductions.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.asset_fundamentals_section_general import AssetFundamentalsSectionGeneral
from openapi_client.model.symbol_search import SymbolSearch


class AssetsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __asset_fundamentals_general_section(
            self,
            ticker,
            **kwargs
        ):
            """Get Asset fundamentals  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.asset_fundamentals_general_section(ticker, async_req=True)
            >>> result = thread.get()

            Args:
                ticker (str): Asset Ticker

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AssetFundamentalsSectionGeneral
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['ticker'] = \
                ticker
            return self.call_with_http_info(**kwargs)

        self.asset_fundamentals_general_section = _Endpoint(
            settings={
                'response_type': (AssetFundamentalsSectionGeneral,),
                'auth': [
                    'api_token'
                ],
                'endpoint_path': '/fundamentals/{ticker}?fmt=json&filter=General',
                'operation_id': 'asset_fundamentals_general_section',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ticker',
                ],
                'required': [
                    'ticker',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ticker':
                        (str,),
                },
                'attribute_map': {
                    'ticker': 'ticker',
                },
                'location_map': {
                    'ticker': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__asset_fundamentals_general_section
        )

        def __search_asset(
            self,
            query,
            **kwargs
        ):
            """Search symbols  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.search_asset(query, async_req=True)
            >>> result = thread.get()

            Args:
                query (str): Name of ticker or search string

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [SymbolSearch]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['query'] = \
                query
            return self.call_with_http_info(**kwargs)

        self.search_asset = _Endpoint(
            settings={
                'response_type': ([SymbolSearch],),
                'auth': [
                    'api_token'
                ],
                'endpoint_path': '/search/{query}',
                'operation_id': 'search_asset',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'query',
                ],
                'required': [
                    'query',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'query':
                        (str,),
                },
                'attribute_map': {
                    'query': 'query',
                },
                'location_map': {
                    'query': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__search_asset
        )