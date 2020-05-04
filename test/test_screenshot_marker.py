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
from Phrase.models.screenshot_marker import ScreenshotMarker  # noqa: E501
from Phrase.rest import ApiException

class TestScreenshotMarker(unittest.TestCase):
    """ScreenshotMarker unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScreenshotMarker
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Phrase.models.screenshot_marker.ScreenshotMarker()  # noqa: E501
        if include_optional :
            return ScreenshotMarker(
                id = '0', 
                presentation = '0', 
                presentation_type = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                translation_key = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"home.index.headline","description":"My description for this key...","name_hash":"1b31d2580ce324f246f66b3be00ed399","plural":false,"tags":["awesome-feature","needs-proofreading"],"data_type":"string","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}
            )
        else :
            return ScreenshotMarker(
        )

    def testScreenshotMarker(self):
        """Test ScreenshotMarker"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
