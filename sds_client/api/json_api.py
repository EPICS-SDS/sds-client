# coding: utf-8

"""
    SDS Client Service API

     This API can be used for: - get collectors configuration by query or by ID - get datasets by a search query or by ID - get files by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query - get data as json by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query 

    The version of the OpenAPI document: 0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from datetime import datetime

from pydantic import StrictInt, StrictStr, conlist

from typing import Any, Optional

from sds_client.models.datase_definition import DataseDefinition

from sds_client.api_client import ApiClient
from sds_client.api_response import ApiResponse
from sds_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class JsonApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_json_by_dataset_id_json_dataset_id_get(self, id : Any, pvs : Optional[conlist(StrictStr)] = None, **kwargs) -> object:  # noqa: E501
        """Get Json By Dataset Id  # noqa: E501

        Get the dataset with the given `id` as json - **pvs** (List[str], optional): list of PVs to return  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_json_by_dataset_id_json_dataset_id_get(id, pvs, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: object
        :param pvs:
        :type pvs: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_json_by_dataset_id_json_dataset_id_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_json_by_dataset_id_json_dataset_id_get_with_http_info(id, pvs, **kwargs)  # noqa: E501

    @validate_arguments
    def get_json_by_dataset_id_json_dataset_id_get_with_http_info(self, id : Any, pvs : Optional[conlist(StrictStr)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Json By Dataset Id  # noqa: E501

        Get the dataset with the given `id` as json - **pvs** (List[str], optional): list of PVs to return  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_json_by_dataset_id_json_dataset_id_get_with_http_info(id, pvs, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: object
        :param pvs:
        :type pvs: List[str]
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'pvs'
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
                    " to method get_json_by_dataset_id_json_dataset_id_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id'] is not None:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('pvs') is not None:  # noqa: E501
            _query_params.append(('pvs', _params['pvs']))
            _collection_formats['pvs'] = 'multi'

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
            '200': "object",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/json/dataset/{id}', 'GET',
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
    def get_json_by_dataset_query_json_query_get(self, collector_id : Optional[conlist(StrictStr)] = None, start : Optional[datetime] = None, end : Optional[datetime] = None, sds_event_pulse_id_start : Optional[StrictInt] = None, sds_event_pulse_id_end : Optional[StrictInt] = None, include_pvs : Optional[conlist(StrictStr)] = None, **kwargs) -> object:  # noqa: E501
        """Get Json By Dataset Query  # noqa: E501

        Search for datasets in the index and returns a json with all hits. - **collector_id** (List[str], optional): list of collector IDs to   consider for the search - **start** (int, optional): UTC timestamp for interval start - **end** (int, optional): UTC timestamp for interval end - **sds_event_pulse_id_start** (int, optional): SDS event pulse ID for interval start - **sds_event_pulse_id_end** (int, optional): SDS event pulse ID for interval end - **search_after** (int, optional): to scroll over a large number of hits - **include_pvs** (List[str], optional): list of PVs to return  To search for a set of PVs, first one needs to search for collectors containing those PVs and then search by collector IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_json_by_dataset_query_json_query_get(collector_id, start, end, sds_event_pulse_id_start, sds_event_pulse_id_end, include_pvs, async_req=True)
        >>> result = thread.get()

        :param collector_id:
        :type collector_id: List[str]
        :param start:
        :type start: datetime
        :param end:
        :type end: datetime
        :param sds_event_pulse_id_start:
        :type sds_event_pulse_id_start: int
        :param sds_event_pulse_id_end:
        :type sds_event_pulse_id_end: int
        :param include_pvs:
        :type include_pvs: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_json_by_dataset_query_json_query_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_json_by_dataset_query_json_query_get_with_http_info(collector_id, start, end, sds_event_pulse_id_start, sds_event_pulse_id_end, include_pvs, **kwargs)  # noqa: E501

    @validate_arguments
    def get_json_by_dataset_query_json_query_get_with_http_info(self, collector_id : Optional[conlist(StrictStr)] = None, start : Optional[datetime] = None, end : Optional[datetime] = None, sds_event_pulse_id_start : Optional[StrictInt] = None, sds_event_pulse_id_end : Optional[StrictInt] = None, include_pvs : Optional[conlist(StrictStr)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Json By Dataset Query  # noqa: E501

        Search for datasets in the index and returns a json with all hits. - **collector_id** (List[str], optional): list of collector IDs to   consider for the search - **start** (int, optional): UTC timestamp for interval start - **end** (int, optional): UTC timestamp for interval end - **sds_event_pulse_id_start** (int, optional): SDS event pulse ID for interval start - **sds_event_pulse_id_end** (int, optional): SDS event pulse ID for interval end - **search_after** (int, optional): to scroll over a large number of hits - **include_pvs** (List[str], optional): list of PVs to return  To search for a set of PVs, first one needs to search for collectors containing those PVs and then search by collector IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_json_by_dataset_query_json_query_get_with_http_info(collector_id, start, end, sds_event_pulse_id_start, sds_event_pulse_id_end, include_pvs, async_req=True)
        >>> result = thread.get()

        :param collector_id:
        :type collector_id: List[str]
        :param start:
        :type start: datetime
        :param end:
        :type end: datetime
        :param sds_event_pulse_id_start:
        :type sds_event_pulse_id_start: int
        :param sds_event_pulse_id_end:
        :type sds_event_pulse_id_end: int
        :param include_pvs:
        :type include_pvs: List[str]
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'collector_id',
            'start',
            'end',
            'sds_event_pulse_id_start',
            'sds_event_pulse_id_end',
            'include_pvs'
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
                    " to method get_json_by_dataset_query_json_query_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('collector_id') is not None:  # noqa: E501
            _query_params.append(('collector_id', _params['collector_id']))
            _collection_formats['collector_id'] = 'multi'

        if _params.get('start') is not None:  # noqa: E501
            if isinstance(_params['start'], datetime):
                _query_params.append(('start', _params['start'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('start', _params['start']))

        if _params.get('end') is not None:  # noqa: E501
            if isinstance(_params['end'], datetime):
                _query_params.append(('end', _params['end'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('end', _params['end']))

        if _params.get('sds_event_pulse_id_start') is not None:  # noqa: E501
            _query_params.append(('sds_event_pulse_id_start', _params['sds_event_pulse_id_start']))

        if _params.get('sds_event_pulse_id_end') is not None:  # noqa: E501
            _query_params.append(('sds_event_pulse_id_end', _params['sds_event_pulse_id_end']))

        if _params.get('include_pvs') is not None:  # noqa: E501
            _query_params.append(('include_pvs', _params['include_pvs']))
            _collection_formats['include_pvs'] = 'multi'

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
            '200': "object",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/json/query', 'GET',
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
    def get_json_by_path_json_get(self, path : StrictStr, pvs : Optional[conlist(StrictStr)] = None, **kwargs) -> object:  # noqa: E501
        """Get Json By Path  # noqa: E501

        Get a json representation of a file from the storage - **path** (str, required): file path - **pvs** (List[str], optional): list of PVs to return  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_json_by_path_json_get(path, pvs, async_req=True)
        >>> result = thread.get()

        :param path: (required)
        :type path: str
        :param pvs:
        :type pvs: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_json_by_path_json_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_json_by_path_json_get_with_http_info(path, pvs, **kwargs)  # noqa: E501

    @validate_arguments
    def get_json_by_path_json_get_with_http_info(self, path : StrictStr, pvs : Optional[conlist(StrictStr)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Json By Path  # noqa: E501

        Get a json representation of a file from the storage - **path** (str, required): file path - **pvs** (List[str], optional): list of PVs to return  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_json_by_path_json_get_with_http_info(path, pvs, async_req=True)
        >>> result = thread.get()

        :param path: (required)
        :type path: str
        :param pvs:
        :type pvs: List[str]
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'path',
            'pvs'
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
                    " to method get_json_by_path_json_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('path') is not None:  # noqa: E501
            _query_params.append(('path', _params['path']))

        if _params.get('pvs') is not None:  # noqa: E501
            _query_params.append(('pvs', _params['pvs']))
            _collection_formats['pvs'] = 'multi'

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
            '200': "object",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/json', 'GET',
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
    def get_json_with_multiple_datasets_json_datasets_post(self, datase_definition : conlist(DataseDefinition), include_pvs : Optional[conlist(StrictStr)] = None, **kwargs) -> object:  # noqa: E501
        """Get Json With Multiple Datasets  # noqa: E501

        Get a Json containing the requested datasets. - **datasets** (List[Dataset], required): list of datasets to download - **include_pvs** (List[str], optional): list of PVs to return  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_json_with_multiple_datasets_json_datasets_post(datase_definition, include_pvs, async_req=True)
        >>> result = thread.get()

        :param datase_definition: (required)
        :type datase_definition: List[DataseDefinition]
        :param include_pvs:
        :type include_pvs: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_json_with_multiple_datasets_json_datasets_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_json_with_multiple_datasets_json_datasets_post_with_http_info(datase_definition, include_pvs, **kwargs)  # noqa: E501

    @validate_arguments
    def get_json_with_multiple_datasets_json_datasets_post_with_http_info(self, datase_definition : conlist(DataseDefinition), include_pvs : Optional[conlist(StrictStr)] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Json With Multiple Datasets  # noqa: E501

        Get a Json containing the requested datasets. - **datasets** (List[Dataset], required): list of datasets to download - **include_pvs** (List[str], optional): list of PVs to return  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_json_with_multiple_datasets_json_datasets_post_with_http_info(datase_definition, include_pvs, async_req=True)
        >>> result = thread.get()

        :param datase_definition: (required)
        :type datase_definition: List[DataseDefinition]
        :param include_pvs:
        :type include_pvs: List[str]
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'datase_definition',
            'include_pvs'
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
                    " to method get_json_with_multiple_datasets_json_datasets_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('include_pvs') is not None:  # noqa: E501
            _query_params.append(('include_pvs', _params['include_pvs']))
            _collection_formats['include_pvs'] = 'multi'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['datase_definition'] is not None:
            _body_params = _params['datase_definition']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "object",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/json/datasets', 'POST',
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
