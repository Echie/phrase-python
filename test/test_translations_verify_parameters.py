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
from Phrase.models.translations_verify_parameters import TranslationsVerifyParameters  # noqa: E501
from Phrase.rest import ApiException

class TestTranslationsVerifyParameters(unittest.TestCase):
    """TranslationsVerifyParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TranslationsVerifyParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Phrase.models.translations_verify_parameters.TranslationsVerifyParameters()  # noqa: E501
        if include_optional :
            return TranslationsVerifyParameters(
                branch = 'my-feature-branch', 
                q = 'PhraseApp*%20unverified:true%20tags:feature,center', 
                sort = 'updated_at', 
                order = 'desc'
            )
        else :
            return TranslationsVerifyParameters(
        )

    def testTranslationsVerifyParameters(self):
        """Test TranslationsVerifyParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
