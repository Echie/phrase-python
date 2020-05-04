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
from Phrase.models.locale_statistics import LocaleStatistics  # noqa: E501
from Phrase.rest import ApiException

class TestLocaleStatistics(unittest.TestCase):
    """LocaleStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocaleStatistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Phrase.models.locale_statistics.LocaleStatistics()  # noqa: E501
        if include_optional :
            return LocaleStatistics(
                keys_total_count = 56, 
                keys_untranslated_count = 56, 
                words_total_count = 56, 
                translations_completed_count = 56, 
                translations_unverified_count = 56, 
                unverified_words_count = 56, 
                missing_words_count = 56
            )
        else :
            return LocaleStatistics(
        )

    def testLocaleStatistics(self):
        """Test LocaleStatistics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
