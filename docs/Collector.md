# Collector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**event_code** | **int** |  | 
**pvs** | **List[str]** |  | 
**parent_path** | **str** |  | [optional] [default to '/']
**collector_id** | **str** |  | [optional] 
**version** | **int** |  | [optional] [default to 1]
**created** | **datetime** |  | 

## Example

```python
from sds_client.models.collector import Collector

# TODO update the JSON string below
json = "{}"
# create an instance of Collector from a JSON string
collector_instance = Collector.from_json(json)
# print the JSON string representation of the object
print Collector.to_json()

# convert the object into a dict
collector_dict = collector_instance.to_dict()
# create an instance of Collector from a dict
collector_from_dict = Collector.from_dict(collector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


