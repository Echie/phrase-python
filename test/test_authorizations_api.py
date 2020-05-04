# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import Phrase
from Phrase.api.authorizations_api import AuthorizationsApi  # noqa: E501
from Phrase.rest import ApiException


class TestAuthorizationsApi(unittest.TestCase):
    """AuthorizationsApi unit test stubs"""

    def setUp(self):
        self.api = Phrase.api.authorizations_api.AuthorizationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authorization_create(self):
        """Test case for authorization_create

        Create an authorization  # noqa: E501
        """
        pass

    def test_authorization_delete(self):
        """Test case for authorization_delete

        Delete an authorization  # noqa: E501
        """
        pass

    def test_authorization_show(self):
        """Test case for authorization_show

        Get a single authorization  # noqa: E501
        """
        pass

    def test_authorization_update(self):
        """Test case for authorization_update

        Update an authorization  # noqa: E501
        """
        pass

    def test_authorizations_list(self):
        """Test case for authorizations_list

        List authorizations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
