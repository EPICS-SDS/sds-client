# coding: utf-8

"""
    SDS Client Service API

     This API can be used for: - get collectors configuration by query or by ID - get datasets by a search query or by ID - get files by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query - get data as json by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query 

    The version of the OpenAPI document: 0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sds_client.models.beam_info import BeamInfo  # noqa: E501

class TestBeamInfo(unittest.TestCase):
    """BeamInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BeamInfo:
        """Test BeamInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BeamInfo`
        """
        model = BeamInfo()  # noqa: E501
        if include_optional:
            return BeamInfo(
                mode = '',
                state = '',
                present = '',
                len = 1.337,
                energy = 1.337,
                dest = '',
                curr = 1.337
            )
        else:
            return BeamInfo(
                mode = '',
                state = '',
                present = '',
                len = 1.337,
                energy = 1.337,
                dest = '',
                curr = 1.337,
        )
        """

    def testBeamInfo(self):
        """Test BeamInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
