# DataseDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collector_id** | **str** |  | 
**sds_event_timestamp** | **datetime** |  | 
**sds_event_pulse_id** | **int** |  | 
**path** | **str** |  | 

## Example

```python
from sds_client.models.datase_definition import DataseDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of DataseDefinition from a JSON string
datase_definition_instance = DataseDefinition.from_json(json)
# print the JSON string representation of the object
print DataseDefinition.to_json()

# convert the object into a dict
datase_definition_dict = datase_definition_instance.to_dict()
# create an instance of DataseDefinition from a dict
datase_definition_form_dict = datase_definition.from_dict(datase_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


