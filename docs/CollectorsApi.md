# sds_client.CollectorsApi

All URIs are relative to *https://sds-retriever.cyolo.ess.eu/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_collector_collectors_id_get**](CollectorsApi.md#get_collector_collectors_id_get) | **GET** /collectors/{id} | Get Collector
[**query_collectors_collectors_get**](CollectorsApi.md#query_collectors_collectors_get) | **GET** /collectors | Query Collectors


# **get_collector_collectors_id_get**
> Collector get_collector_collectors_id_get(id)

Get Collector

Return the collector with the given `id`

### Example

```python
import time
import os
import sds_client
from sds_client.models.collector import Collector
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
    api_instance = sds_client.CollectorsApi(api_client)
    id = None # object | 

    try:
        # Get Collector
        api_response = api_instance.get_collector_collectors_id_get(id)
        print("The response of CollectorsApi->get_collector_collectors_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectorsApi->get_collector_collectors_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Collector**](Collector.md)

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

# **query_collectors_collectors_get**
> MultiResponseCollector query_collectors_collectors_get(name=name, event_name=event_name, event_code=event_code, pv=pv, sort=sort, search_after=search_after)

Query Collectors

Search for collectors that contain **at least** the PVs given as a parameter. The collector can contain more PVs than the ones defined, it does not need to be a perfect match. All the parameters can contain wildcards, including PV names.  Arguments: - **name** (str, optional): name of the collector - **event_name** (str, optional): name of the event - **event_code** (int, optional): event code - **pv** (List[str], optional): list of PVs  Returns: a list of dataset descriptions

### Example

```python
import time
import os
import sds_client
from sds_client.models.multi_response_collector import MultiResponseCollector
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
    api_instance = sds_client.CollectorsApi(api_client)
    name = 'name_example' # str |  (optional)
    event_name = 'event_name_example' # str |  (optional)
    event_code = 56 # int |  (optional)
    pv = ['pv_example'] # List[str] |  (optional)
    sort = sds_client.SortOrder() # SortOrder |  (optional)
    search_after = 56 # int |  (optional)

    try:
        # Query Collectors
        api_response = api_instance.query_collectors_collectors_get(name=name, event_name=event_name, event_code=event_code, pv=pv, sort=sort, search_after=search_after)
        print("The response of CollectorsApi->query_collectors_collectors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectorsApi->query_collectors_collectors_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **event_name** | **str**|  | [optional] 
 **event_code** | **int**|  | [optional] 
 **pv** | [**List[str]**](str.md)|  | [optional] 
 **sort** | [**SortOrder**](.md)|  | [optional] 
 **search_after** | **int**|  | [optional] 

### Return type

[**MultiResponseCollector**](MultiResponseCollector.md)

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

