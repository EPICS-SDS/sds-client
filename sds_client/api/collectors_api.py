# coding: utf-8

"""
    SDS Client Service API

     This API can be used for: - get collectors configuration by query or by ID - get datasets by a search query or by ID - get files by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query - get data as json by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query 

    The version of the OpenAPI document: 0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictInt, StrictStr, conlist

from typing import Any, Optional

from sds_client.models.multi_response_collector import MultiResponseCollector
from sds_client.models.sort_order import SortOrder

from sds_client.api_client import ApiClient
from sds_client.api_response import ApiResponse
from sds_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CollectorsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_collector_collectors_collector_id_get(self, collector_id : Any, **kwargs) -> MultiResponseCollector:  # noqa: E501
        """Get Collector  # noqa: E501

        Return the collector with the given `collector_id`, as a list with all the versions available.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_collector_collectors_collector_id_get(collector_id, async_req=True)
        >>> result = thread.get()

        :param collector_id: (required)
        :type collector_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MultiResponseCollector
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_collector_collectors_collector_id_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_collector_collectors_collector_id_get_with_http_info(collector_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_collector_collectors_collector_id_get_with_http_info(self, collector_id : Any, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Collector  # noqa: E501

        Return the collector with the given `collector_id`, as a list with all the versions available.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_collector_collectors_collector_id_get_with_http_info(collector_id, async_req=True)
        >>> result = thread.get()

        :param collector_id: (required)
        :type collector_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MultiResponseCollector, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'collector_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_collector_collectors_collector_id_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['collector_id'] is not None:
            _path_params['collector_id'] = _params['collector_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "MultiResponseCollector",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/collectors/{collector_id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def query_collectors_collectors_get(self, name : Optional[StrictStr] = None, parent_path : Optional[StrictStr] = None, event_code : Optional[StrictInt] = None, pv : Optional[conlist(StrictStr)] = None, sort : Optional[SortOrder] = None, latest_version_only : Annotated[Optional[StrictBool], Field(description="Return only the latest version of each collector")] = None, search_after : Optional[StrictInt] = None, **kwargs) -> MultiResponseCollector:  # noqa: E501
        """Query Collectors  # noqa: E501

        Search for collectors that contain **at least** the PVs given as a parameter. The collector can contain more PVs than the ones defined, it does not need to be a perfect match. All the parameters can contain wildcards, including PV names.  Arguments: - **name** (str, optional): name of the collector - **parent_path** (str, optional): parent_path of the collector - **event_code** (int, optional): event code - **pv** (List[str], optional): list of PVs  Returns: a list of dataset descriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_collectors_collectors_get(name, parent_path, event_code, pv, sort, latest_version_only, search_after, async_req=True)
        >>> result = thread.get()

        :param name:
        :type name: str
        :param parent_path:
        :type parent_path: str
        :param event_code:
        :type event_code: int
        :param pv:
        :type pv: List[str]
        :param sort:
        :type sort: SortOrder
        :param latest_version_only: Return only the latest version of each collector
        :type latest_version_only: bool
        :param search_after:
        :type search_after: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MultiResponseCollector
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the query_collectors_collectors_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.query_collectors_collectors_get_with_http_info(name, parent_path, event_code, pv, sort, latest_version_only, search_after, **kwargs)  # noqa: E501

    @validate_arguments
    def query_collectors_collectors_get_with_http_info(self, name : Optional[StrictStr] = None, parent_path : Optional[StrictStr] = None, event_code : Optional[StrictInt] = None, pv : Optional[conlist(StrictStr)] = None, sort : Optional[SortOrder] = None, latest_version_only : Annotated[Optional[StrictBool], Field(description="Return only the latest version of each collector")] = None, search_after : Optional[StrictInt] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Query Collectors  # noqa: E501

        Search for collectors that contain **at least** the PVs given as a parameter. The collector can contain more PVs than the ones defined, it does not need to be a perfect match. All the parameters can contain wildcards, including PV names.  Arguments: - **name** (str, optional): name of the collector - **parent_path** (str, optional): parent_path of the collector - **event_code** (int, optional): event code - **pv** (List[str], optional): list of PVs  Returns: a list of dataset descriptions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_collectors_collectors_get_with_http_info(name, parent_path, event_code, pv, sort, latest_version_only, search_after, async_req=True)
        >>> result = thread.get()

        :param name:
        :type name: str
        :param parent_path:
        :type parent_path: str
        :param event_code:
        :type event_code: int
        :param pv:
        :type pv: List[str]
        :param sort:
        :type sort: SortOrder
        :param latest_version_only: Return only the latest version of each collector
        :type latest_version_only: bool
        :param search_after:
        :type search_after: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MultiResponseCollector, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'name',
            'parent_path',
            'event_code',
            'pv',
            'sort',
            'latest_version_only',
            'search_after'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_collectors_collectors_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('name') is not None:  # noqa: E501
            _query_params.append(('name', _params['name']))

        if _params.get('parent_path') is not None:  # noqa: E501
            _query_params.append(('parent_path', _params['parent_path']))

        if _params.get('event_code') is not None:  # noqa: E501
            _query_params.append(('event_code', _params['event_code']))

        if _params.get('pv') is not None:  # noqa: E501
            _query_params.append(('pv', _params['pv']))
            _collection_formats['pv'] = 'multi'

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort'].value))

        if _params.get('latest_version_only') is not None:  # noqa: E501
            _query_params.append(('latest_version_only', _params['latest_version_only']))

        if _params.get('search_after') is not None:  # noqa: E501
            _query_params.append(('search_after', _params['search_after']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "MultiResponseCollector",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/collectors', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
