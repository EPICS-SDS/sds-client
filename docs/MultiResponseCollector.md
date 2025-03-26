# MultiResponseCollector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**search_after** | **int** |  | 
**collectors** | [**List[Collector]**](Collector.md) |  | 

## Example

```python
from sds_client.models.multi_response_collector import MultiResponseCollector

# TODO update the JSON string below
json = "{}"
# create an instance of MultiResponseCollector from a JSON string
multi_response_collector_instance = MultiResponseCollector.from_json(json)
# print the JSON string representation of the object
print MultiResponseCollector.to_json()

# convert the object into a dict
multi_response_collector_dict = multi_response_collector_instance.to_dict()
# create an instance of MultiResponseCollector from a dict
multi_response_collector_from_dict = MultiResponseCollector.from_dict(multi_response_collector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


