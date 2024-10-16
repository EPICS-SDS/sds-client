# BeamInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**state** | **str** |  | 
**present** | **str** |  | 
**len** | **float** |  | 
**energy** | **float** |  | 
**dest** | **str** |  | 
**curr** | **float** |  | 

## Example

```python
from sds_client.models.beam_info import BeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BeamInfo from a JSON string
beam_info_instance = BeamInfo.from_json(json)
# print the JSON string representation of the object
print BeamInfo.to_json()

# convert the object into a dict
beam_info_dict = beam_info_instance.to_dict()
# create an instance of BeamInfo from a dict
beam_info_form_dict = beam_info.from_dict(beam_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


