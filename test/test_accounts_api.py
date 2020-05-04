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
from Phrase.api.accounts_api import AccountsApi  # noqa: E501
from Phrase.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = Phrase.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_show(self):
        """Test case for account_show

        Get a single account  # noqa: E501
        """
        pass

    def test_accounts_list(self):
        """Test case for accounts_list

        List accounts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
