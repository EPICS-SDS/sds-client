# sds_client.EventsApi

All URIs are relative to *https://sds-retriever.cyolo.ess.eu/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_aggregated_datasets_by_event_events_post**](EventsApi.md#query_aggregated_datasets_by_event_events_post) | **POST** /events | Query Aggregated Datasets By Event


# **query_aggregated_datasets_by_event_events_post**
> object query_aggregated_datasets_by_event_events_post(start=start, end=end, sds_event_cycle_id_start=sds_event_cycle_id_start, sds_event_cycle_id_end=sds_event_cycle_id_end, size=size, sort=sort, collector_id_list=collector_id_list)

Query Aggregated Datasets By Event

Search for datasets in the index.
- **collector_id** (List[str], optional): list of collector IDs to
  consider for the search
- **start** (int, optional): UTC timestamp for interval start
- **end** (int, optional): UTC timestamp for interval end
- **sds_event_cycle_id_start** (int, optional): SDS event cycle ID for interval start
- **sds_event_cycle_id_end** (int, optional): SDS event cycle ID for interval end
- **size** (int, optional): number of events to return. Defaults to 10.
- **sort** (SortOrder, optional): to sort results in ascending or descending order in time (descending by default)

To search for a set of PVs, first one needs to search for collectors
containing those PVs and then search by collector IDs.

### Example

```python
import time
import os
import sds_client
from sds_client.models.collector_id_list import CollectorIdList
from sds_client.models.sort_order import SortOrder
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
    api_instance = sds_client.EventsApi(api_client)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    sds_event_cycle_id_start = 56 # int |  (optional)
    sds_event_cycle_id_end = 56 # int |  (optional)
    size = 10 # int |  (optional) (default to 10)
    sort = sds_client.SortOrder() # SortOrder |  (optional)
    collector_id_list = sds_client.CollectorIdList() # CollectorIdList |  (optional)

    try:
        # Query Aggregated Datasets By Event
        api_response = api_instance.query_aggregated_datasets_by_event_events_post(start=start, end=end, sds_event_cycle_id_start=sds_event_cycle_id_start, sds_event_cycle_id_end=sds_event_cycle_id_end, size=size, sort=sort, collector_id_list=collector_id_list)
        print("The response of EventsApi->query_aggregated_datasets_by_event_events_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->query_aggregated_datasets_by_event_events_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **sds_event_cycle_id_start** | **int**|  | [optional] 
 **sds_event_cycle_id_end** | **int**|  | [optional] 
 **size** | **int**|  | [optional] [default to 10]
 **sort** | [**SortOrder**](.md)|  | [optional] 
 **collector_id_list** | [**CollectorIdList**](CollectorIdList.md)|  | [optional] 

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

