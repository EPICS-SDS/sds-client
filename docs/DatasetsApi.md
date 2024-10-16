# sds_client.DatasetsApi

All URIs are relative to *https://sds-retriever.cyolo.ess.eu/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_datasets_id_get**](DatasetsApi.md#get_dataset_datasets_id_get) | **GET** /datasets/{id} | Get Dataset
[**query_datasets_datasets_get**](DatasetsApi.md#query_datasets_datasets_get) | **GET** /datasets | Query Datasets


# **get_dataset_datasets_id_get**
> Dataset get_dataset_datasets_id_get(id)

Get Dataset

Get the dataset metadata with the give `id`

### Example

```python
import time
import os
import sds_client
from sds_client.models.dataset import Dataset
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
    api_instance = sds_client.DatasetsApi(api_client)
    id = None # object | 

    try:
        # Get Dataset
        api_response = api_instance.get_dataset_datasets_id_get(id)
        print("The response of DatasetsApi->get_dataset_datasets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_dataset_datasets_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Dataset**](Dataset.md)

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

# **query_datasets_datasets_get**
> MultiResponseDataset query_datasets_datasets_get(collector_id=collector_id, start=start, end=end, sds_event_pulse_id_start=sds_event_pulse_id_start, sds_event_pulse_id_end=sds_event_pulse_id_end, sort=sort, search_after=search_after)

Query Datasets

Search for datasets in the index. - **collector_id** (List[str], optional): list of collector IDs to   consider for the search - **start** (int, optional): UTC timestamp for interval start - **end** (int, optional): UTC timestamp for interval end - **sds_event_pulse_id_start** (int, optional): SDS event pulse ID for interval start - **sds_event_pulse_id_end** (int, optional): SDS event pulse ID for interval end - **sort** (SortOrder, optional): to sort results in ascending or descending order in time - **search_after** (int, optional): to scroll over a large number of hits  To search for a set of PVs, first one needs to search for collectors containing those PVs and then search by collector IDs.

### Example

```python
import time
import os
import sds_client
from sds_client.models.multi_response_dataset import MultiResponseDataset
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
    api_instance = sds_client.DatasetsApi(api_client)
    collector_id = ['collector_id_example'] # List[str] |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    sds_event_pulse_id_start = 56 # int |  (optional)
    sds_event_pulse_id_end = 56 # int |  (optional)
    sort = sds_client.SortOrder() # SortOrder |  (optional)
    search_after = 56 # int |  (optional)

    try:
        # Query Datasets
        api_response = api_instance.query_datasets_datasets_get(collector_id=collector_id, start=start, end=end, sds_event_pulse_id_start=sds_event_pulse_id_start, sds_event_pulse_id_end=sds_event_pulse_id_end, sort=sort, search_after=search_after)
        print("The response of DatasetsApi->query_datasets_datasets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->query_datasets_datasets_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | [**List[str]**](str.md)|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **sds_event_pulse_id_start** | **int**|  | [optional] 
 **sds_event_pulse_id_end** | **int**|  | [optional] 
 **sort** | [**SortOrder**](.md)|  | [optional] 
 **search_after** | **int**|  | [optional] 

### Return type

[**MultiResponseDataset**](MultiResponseDataset.md)

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

