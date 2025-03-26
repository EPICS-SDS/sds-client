# coding: utf-8

"""
    SDS Client Service API

     This API can be used for: - get collectors configuration by query or by ID - get datasets by a search query or by ID - get files by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query - get data as json by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query 

    The version of the OpenAPI document: 0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sds_client.api.events_api import EventsApi  # noqa: E501


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EventsApi()

    def tearDown(self) -> None:
        self.api.api_client.close()

    def test_query_aggregated_datasets_by_event_events_post(self) -> None:
        """Test case for query_aggregated_datasets_by_event_events_post

        Query Aggregated Datasets By Event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
