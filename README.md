# sds-client

This API can be used for:
- get collectors configuration by query or by ID
- get datasets by a search query or by ID
- get files by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query
- get data as json by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.3
- Package version: 1.0.0
- Generator version: 7.13.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sds_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sds_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = sds_client.CollectorsApi(api_client)
    collector_id = None # object | 

    try:
        # Get Collector
        api_response = api_instance.get_collector_collectors_collector_id_get(collector_id)
        print("The response of CollectorsApi->get_collector_collectors_collector_id_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectorsApi->get_collector_collectors_collector_id_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://sds-retriever.cyolo.ess.eu/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CollectorsApi* | [**get_collector_collectors_collector_id_get**](docs/CollectorsApi.md#get_collector_collectors_collector_id_get) | **GET** /collectors/{collector_id} | Get Collector
*CollectorsApi* | [**query_collectors_collectors_get**](docs/CollectorsApi.md#query_collectors_collectors_get) | **GET** /collectors | Query Collectors
*DatasetsApi* | [**get_dataset_datasets_id_get**](docs/DatasetsApi.md#get_dataset_datasets_id_get) | **GET** /datasets/{id} | Get Dataset
*DatasetsApi* | [**query_datasets_datasets_post**](docs/DatasetsApi.md#query_datasets_datasets_post) | **POST** /datasets | Query Datasets
*EventsApi* | [**query_aggregated_datasets_by_event_events_post**](docs/EventsApi.md#query_aggregated_datasets_by_event_events_post) | **POST** /events | Query Aggregated Datasets By Event
*JsonApi* | [**get_json_by_dataset_id_json_dataset_id_get**](docs/JsonApi.md#get_json_by_dataset_id_json_dataset_id_get) | **GET** /json/dataset/{id} | Get Json By Dataset Id
*JsonApi* | [**get_json_by_dataset_query_json_query_post**](docs/JsonApi.md#get_json_by_dataset_query_json_query_post) | **POST** /json/query | Get Json By Dataset Query
*JsonApi* | [**get_json_by_path_json_get**](docs/JsonApi.md#get_json_by_path_json_get) | **GET** /json | Get Json By Path
*JsonApi* | [**get_json_with_multiple_datasets_json_datasets_post**](docs/JsonApi.md#get_json_with_multiple_datasets_json_datasets_post) | **POST** /json/datasets | Get Json With Multiple Datasets
*NexusApi* | [**get_nexus_by_dataset_id_nexus_dataset_id_get**](docs/NexusApi.md#get_nexus_by_dataset_id_nexus_dataset_id_get) | **GET** /nexus/dataset/{id} | Get Nexus By Dataset Id
*NexusApi* | [**get_nexus_by_dataset_query_nexus_query_post**](docs/NexusApi.md#get_nexus_by_dataset_query_nexus_query_post) | **POST** /nexus/query | Get Nexus By Dataset Query
*NexusApi* | [**get_nexus_by_path_nexus_get**](docs/NexusApi.md#get_nexus_by_path_nexus_get) | **GET** /nexus/ | Get Nexus By Path
*NexusApi* | [**get_nexus_with_multiple_datasets_nexus_datasets_post**](docs/NexusApi.md#get_nexus_with_multiple_datasets_nexus_datasets_post) | **POST** /nexus/datasets | Get Nexus With Multiple Datasets


## Documentation For Models

 - [Collector](docs/Collector.md)
 - [CollectorIdList](docs/CollectorIdList.md)
 - [DataseDefinition](docs/DataseDefinition.md)
 - [Dataset](docs/Dataset.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [MultiResponseCollector](docs/MultiResponseCollector.md)
 - [MultiResponseDataset](docs/MultiResponseDataset.md)
 - [SortOrder](docs/SortOrder.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




