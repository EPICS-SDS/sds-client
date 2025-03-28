# coding: utf-8

"""
    SDS Client Service API

     This API can be used for: - get collectors configuration by query or by ID - get datasets by a search query or by ID - get files by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query - get data as json by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query 

    The version of the OpenAPI document: 0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sds_client.models.dataset import Dataset  # noqa: E501

class TestDataset(unittest.TestCase):
    """Dataset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dataset:
        """Test Dataset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dataset`
        """
        model = Dataset()  # noqa: E501
        if include_optional:
            return Dataset(
                collector_id = '',
                sds_event_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sds_cycle_start_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sds_event_cycle_id = 56,
                path = '/directory/file.h5',
                beam_info = sds_client.models.beam_info.Beam Info(),
                id = ''
            )
        else:
            return Dataset(
                collector_id = '',
                sds_event_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sds_cycle_start_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sds_event_cycle_id = 56,
                path = '/directory/file.h5',
                beam_info = sds_client.models.beam_info.Beam Info(),
                id = '',
        )
        """

    def testDataset(self):
        """Test Dataset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
