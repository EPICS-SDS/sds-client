# Dataset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collector_id** | **str** |  | 
**sds_event_timestamp** | **datetime** |  | 
**sds_cycle_start_timestamp** | **datetime** |  | 
**sds_event_cycle_id** | **int** |  | 
**path** | **str** |  | 
**beam_info** | **object** |  | 
**id** | **str** |  | 

## Example

```python
from sds_client.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print Dataset.to_json()

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_from_dict = Dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


