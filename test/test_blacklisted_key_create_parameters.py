# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import Phrase
from Phrase.models.blacklisted_key_create_parameters import BlacklistedKeyCreateParameters  # noqa: E501
from Phrase.rest import ApiException

class TestBlacklistedKeyCreateParameters(unittest.TestCase):
    """BlacklistedKeyCreateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BlacklistedKeyCreateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Phrase.models.blacklisted_key_create_parameters.BlacklistedKeyCreateParameters()  # noqa: E501
        if include_optional :
            return BlacklistedKeyCreateParameters(
                name = 'date.formats.*'
            )
        else :
            return BlacklistedKeyCreateParameters(
        )

    def testBlacklistedKeyCreateParameters(self):
        """Test BlacklistedKeyCreateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
