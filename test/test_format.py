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
from Phrase.models.format import Format  # noqa: E501
from Phrase.rest import ApiException

class TestFormat(unittest.TestCase):
    """Format unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Format
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Phrase.models.format.Format()  # noqa: E501
        if include_optional :
            return Format(
                name = '0', 
                api_name = '0', 
                description = '0', 
                extension = '0', 
                default_encoding = '0', 
                importable = True, 
                exportable = True, 
                default_file = '0', 
                renders_default_locale = True, 
                includes_locale_information = True
            )
        else :
            return Format(
        )

    def testFormat(self):
        """Test Format"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
