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
from Phrase.models.job_locale_complete_parameters import JobLocaleCompleteParameters  # noqa: E501
from Phrase.rest import ApiException

class TestJobLocaleCompleteParameters(unittest.TestCase):
    """JobLocaleCompleteParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobLocaleCompleteParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Phrase.models.job_locale_complete_parameters.JobLocaleCompleteParameters()  # noqa: E501
        if include_optional :
            return JobLocaleCompleteParameters(
                branch = 'my-feature-branch'
            )
        else :
            return JobLocaleCompleteParameters(
        )

    def testJobLocaleCompleteParameters(self):
        """Test JobLocaleCompleteParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
