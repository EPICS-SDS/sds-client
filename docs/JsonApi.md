# sds_client.JsonApi

All URIs are relative to *https://sds-retriever.cyolo.ess.eu/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_json_by_dataset_id_json_dataset_id_get**](JsonApi.md#get_json_by_dataset_id_json_dataset_id_get) | **GET** /json/dataset/{id} | Get Json By Dataset Id
[**get_json_by_dataset_query_json_query_get**](JsonApi.md#get_json_by_dataset_query_json_query_get) | **GET** /json/query | Get Json By Dataset Query
[**get_json_by_path_json_get**](JsonApi.md#get_json_by_path_json_get) | **GET** /json | Get Json By Path
[**get_json_with_multiple_datasets_json_datasets_post**](JsonApi.md#get_json_with_multiple_datasets_json_datasets_post) | **POST** /json/datasets | Get Json With Multiple Datasets


# **get_json_by_dataset_id_json_dataset_id_get**
> object get_json_by_dataset_id_json_dataset_id_get(id, pvs=pvs)

Get Json By Dataset Id

Get the dataset with the given `id` as json - **pvs** (List[str], optional): list of PVs to return

### Example

```python
import time
import os
import sds_client
from sds_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sds-retriever.cyolo.ess.eu/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sds_client.Configuration(
    host = "https://sds-retriever.cyolo.ess.eu/api"
)


# Enter a context with an instance of the API client
with sds_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sds_client.JsonApi(api_client)
    id = None # object | 
    pvs = ['pvs_example'] # List[str] |  (optional)

    try:
        # Get Json By Dataset Id
        api_response = api_instance.get_json_by_dataset_id_json_dataset_id_get(id, pvs=pvs)
        print("The response of JsonApi->get_json_by_dataset_id_json_dataset_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JsonApi->get_json_by_dataset_id_json_dataset_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **pvs** | [**List[str]**](str.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_by_dataset_query_json_query_get**
> object get_json_by_dataset_query_json_query_get(collector_id=collector_id, start=start, end=end, sds_event_pulse_id_start=sds_event_pulse_id_start, sds_event_pulse_id_end=sds_event_pulse_id_end, include_pvs=include_pvs)

Get Json By Dataset Query

Search for datasets in the index and returns a json with all hits. - **collector_id** (List[str], optional): list of collector IDs to   consider for the search - **start** (int, optional): UTC timestamp for interval start - **end** (int, optional): UTC timestamp for interval end - **sds_event_pulse_id_start** (int, optional): SDS event pulse ID for interval start - **sds_event_pulse_id_end** (int, optional): SDS event pulse ID for interval end - **search_after** (int, optional): to scroll over a large number of hits - **include_pvs** (List[str], optional): list of PVs to return  To search for a set of PVs, first one needs to search for collectors containing those PVs and then search by collector IDs.

### Example

```python
import time
import os
import sds_client
from sds_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sds-retriever.cyolo.ess.eu/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sds_client.Configuration(
    host = "https://sds-retriever.cyolo.ess.eu/api"
)


# Enter a context with an instance of the API client
with sds_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sds_client.JsonApi(api_client)
    collector_id = ['collector_id_example'] # List[str] |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    sds_event_pulse_id_start = 56 # int |  (optional)
    sds_event_pulse_id_end = 56 # int |  (optional)
    include_pvs = ['include_pvs_example'] # List[str] |  (optional)

    try:
        # Get Json By Dataset Query
        api_response = api_instance.get_json_by_dataset_query_json_query_get(collector_id=collector_id, start=start, end=end, sds_event_pulse_id_start=sds_event_pulse_id_start, sds_event_pulse_id_end=sds_event_pulse_id_end, include_pvs=include_pvs)
        print("The response of JsonApi->get_json_by_dataset_query_json_query_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JsonApi->get_json_by_dataset_query_json_query_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | [**List[str]**](str.md)|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **sds_event_pulse_id_start** | **int**|  | [optional] 
 **sds_event_pulse_id_end** | **int**|  | [optional] 
 **include_pvs** | [**List[str]**](str.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_by_path_json_get**
> object get_json_by_path_json_get(path, pvs=pvs)

Get Json By Path

Get a json representation of a file from the storage - **path** (str, required): file path - **pvs** (List[str], optional): list of PVs to return

### Example

```python
import time
import os
import sds_client
from sds_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sds-retriever.cyolo.ess.eu/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sds_client.Configuration(
    host = "https://sds-retriever.cyolo.ess.eu/api"
)


# Enter a context with an instance of the API client
with sds_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sds_client.JsonApi(api_client)
    path = 'path_example' # str | 
    pvs = ['pvs_example'] # List[str] |  (optional)

    try:
        # Get Json By Path
        api_response = api_instance.get_json_by_path_json_get(path, pvs=pvs)
        print("The response of JsonApi->get_json_by_path_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JsonApi->get_json_by_path_json_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **pvs** | [**List[str]**](str.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_with_multiple_datasets_json_datasets_post**
> object get_json_with_multiple_datasets_json_datasets_post(datase_definition, include_pvs=include_pvs)

Get Json With Multiple Datasets

Get a Json containing the requested datasets. - **datasets** (List[Dataset], required): list of datasets to download - **include_pvs** (List[str], optional): list of PVs to return

### Example

```python
import time
import os
import sds_client
from sds_client.models.datase_definition import DataseDefinition
from sds_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sds-retriever.cyolo.ess.eu/api
# See configuration.py for a list of all supported configuration parameters.
configuration = sds_client.Configuration(
    host = "https://sds-retriever.cyolo.ess.eu/api"
)


# Enter a context with an instance of the API client
with sds_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sds_client.JsonApi(api_client)
    datase_definition = [sds_client.DataseDefinition()] # List[DataseDefinition] | 
    include_pvs = ['include_pvs_example'] # List[str] |  (optional)

    try:
        # Get Json With Multiple Datasets
        api_response = api_instance.get_json_with_multiple_datasets_json_datasets_post(datase_definition, include_pvs=include_pvs)
        print("The response of JsonApi->get_json_with_multiple_datasets_json_datasets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JsonApi->get_json_with_multiple_datasets_json_datasets_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datase_definition** | [**List[DataseDefinition]**](DataseDefinition.md)|  | 
 **include_pvs** | [**List[str]**](str.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

