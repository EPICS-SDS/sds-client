# MultiResponseDataset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**search_after** | **int** |  | [optional] 
**datasets** | [**List[Dataset]**](Dataset.md) |  | 

## Example

```python
from sds_client.models.multi_response_dataset import MultiResponseDataset

# TODO update the JSON string below
json = "{}"
# create an instance of MultiResponseDataset from a JSON string
multi_response_dataset_instance = MultiResponseDataset.from_json(json)
# print the JSON string representation of the object
print MultiResponseDataset.to_json()

# convert the object into a dict
multi_response_dataset_dict = multi_response_dataset_instance.to_dict()
# create an instance of MultiResponseDataset from a dict
multi_response_dataset_form_dict = multi_response_dataset.from_dict(multi_response_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


