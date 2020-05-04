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
from Phrase.models.styleguide_preview import StyleguidePreview  # noqa: E501
from Phrase.rest import ApiException

class TestStyleguidePreview(unittest.TestCase):
    """StyleguidePreview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StyleguidePreview
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Phrase.models.styleguide_preview.StyleguidePreview()  # noqa: E501
        if include_optional :
            return StyleguidePreview(
                id = '0', 
                title = '0'
            )
        else :
            return StyleguidePreview(
        )

    def testStyleguidePreview(self):
        """Test StyleguidePreview"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
