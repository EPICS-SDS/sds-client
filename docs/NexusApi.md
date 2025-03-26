# sds_client.NexusApi

All URIs are relative to *https://sds-retriever.cyolo.ess.eu/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nexus_by_dataset_id_nexus_dataset_id_get**](NexusApi.md#get_nexus_by_dataset_id_nexus_dataset_id_get) | **GET** /nexus/dataset/{id} | Get Nexus By Dataset Id
[**get_nexus_by_dataset_query_nexus_query_post**](NexusApi.md#get_nexus_by_dataset_query_nexus_query_post) | **POST** /nexus/query | Get Nexus By Dataset Query
[**get_nexus_by_path_nexus_get**](NexusApi.md#get_nexus_by_path_nexus_get) | **GET** /nexus/ | Get Nexus By Path
[**get_nexus_with_multiple_datasets_nexus_datasets_post**](NexusApi.md#get_nexus_with_multiple_datasets_nexus_datasets_post) | **POST** /nexus/datasets | Get Nexus With Multiple Datasets


# **get_nexus_by_dataset_id_nexus_dataset_id_get**
> get_nexus_by_dataset_id_nexus_dataset_id_get(id)

Get Nexus By Dataset Id

Get the NeXus file containing the dataset with the given `id`

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
    api_instance = sds_client.NexusApi(api_client)
    id = None # object | 

    try:
        # Get Nexus By Dataset Id
        api_instance.get_nexus_by_dataset_id_nexus_dataset_id_get(id)
    except Exception as e:
        print("Exception when calling NexusApi->get_nexus_by_dataset_id_nexus_dataset_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

void (empty response body)

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

# **get_nexus_by_dataset_query_nexus_query_post**
> get_nexus_by_dataset_query_nexus_query_post(start=start, end=end, sds_event_cycle_id_start=sds_event_cycle_id_start, sds_event_cycle_id_end=sds_event_cycle_id_end, size=size, include_pvs=include_pvs, collector_id_list=collector_id_list)

Get Nexus By Dataset Query

Search for datasets in the index and returns a file containing all hits.
- **collector_id** (List[str], optional): list of collector IDs to
  consider for the search
- **start** (int, optional): UTC timestamp for interval start
- **end** (int, optional): UTC timestamp for interval end
- **sds_event_cycle_id_start** (int, optional): SDS event cycle ID for interval start
- **sds_event_cycle_id_end** (int, optional): SDS event cycle ID for interval end
- **size** (int, optional): Limit the number of results. If used alone, it will return the latest *size* datasets
- **search_after** (int, optional): to scroll over a large number of hits
- **include_pvs** (List[str], optional): list of PVs to return

To search for a set of PVs, first one needs to search for collectors
containing those PVs and then search by collector IDs.

### Example

```python
import time
import os
import sds_client
from sds_client.models.collector_id_list import CollectorIdList
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
    api_instance = sds_client.NexusApi(api_client)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    sds_event_cycle_id_start = 56 # int |  (optional)
    sds_event_cycle_id_end = 56 # int |  (optional)
    size = 56 # int |  (optional)
    include_pvs = ['include_pvs_example'] # List[str] |  (optional)
    collector_id_list = sds_client.CollectorIdList() # CollectorIdList |  (optional)

    try:
        # Get Nexus By Dataset Query
        api_instance.get_nexus_by_dataset_query_nexus_query_post(start=start, end=end, sds_event_cycle_id_start=sds_event_cycle_id_start, sds_event_cycle_id_end=sds_event_cycle_id_end, size=size, include_pvs=include_pvs, collector_id_list=collector_id_list)
    except Exception as e:
        print("Exception when calling NexusApi->get_nexus_by_dataset_query_nexus_query_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **sds_event_cycle_id_start** | **int**|  | [optional] 
 **sds_event_cycle_id_end** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **include_pvs** | [**List[str]**](str.md)|  | [optional] 
 **collector_id_list** | [**CollectorIdList**](CollectorIdList.md)|  | [optional] 

### Return type

void (empty response body)

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

# **get_nexus_by_path_nexus_get**
> get_nexus_by_path_nexus_get(path)

Get Nexus By Path

Get a NeXus file from the storage
- **path** (str, required): file path

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
    api_instance = sds_client.NexusApi(api_client)
    path = 'path_example' # str | 

    try:
        # Get Nexus By Path
        api_instance.get_nexus_by_path_nexus_get(path)
    except Exception as e:
        print("Exception when calling NexusApi->get_nexus_by_path_nexus_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

void (empty response body)

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

# **get_nexus_with_multiple_datasets_nexus_datasets_post**
> get_nexus_with_multiple_datasets_nexus_datasets_post(datase_definition, include_pvs=include_pvs)

Get Nexus With Multiple Datasets

Get a set of NeXus files containing the requested datasets, one file per collector (zipped if needed).
- **datasets** (List[Dataset], required): list of datasets to download
- **include_pvs** (List[str], optional): list of PVs to return

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
    api_instance = sds_client.NexusApi(api_client)
    datase_definition = [sds_client.DataseDefinition()] # List[DataseDefinition] | 
    include_pvs = ['include_pvs_example'] # List[str] |  (optional)

    try:
        # Get Nexus With Multiple Datasets
        api_instance.get_nexus_with_multiple_datasets_nexus_datasets_post(datase_definition, include_pvs=include_pvs)
    except Exception as e:
        print("Exception when calling NexusApi->get_nexus_with_multiple_datasets_nexus_datasets_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datase_definition** | [**List[DataseDefinition]**](DataseDefinition.md)|  | 
 **include_pvs** | [**List[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

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

