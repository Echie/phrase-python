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
from Phrase.models.bitbucket_sync import BitbucketSync  # noqa: E501
from Phrase.rest import ApiException

class TestBitbucketSync(unittest.TestCase):
    """BitbucketSync unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BitbucketSync
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Phrase.models.bitbucket_sync.BitbucketSync()  # noqa: E501
        if include_optional :
            return BitbucketSync(
                id = '0', 
                repository_name = '0', 
                last_export_to_bitbucket_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_import_from_bitbucket_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                valid_phraseapp_yaml = True, 
                phraseapp_projects = [
                    {"id":"abcd1234cdef1234abcd1234cdef1234","name":"My Android Project","main_format":"xml","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}
                    ]
            )
        else :
            return BitbucketSync(
        )

    def testBitbucketSync(self):
        """Test BitbucketSync"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
