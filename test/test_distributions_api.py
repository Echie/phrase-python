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
from Phrase.api.distributions_api import DistributionsApi  # noqa: E501
from Phrase.rest import ApiException


class TestDistributionsApi(unittest.TestCase):
    """DistributionsApi unit test stubs"""

    def setUp(self):
        self.api = Phrase.api.distributions_api.DistributionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_distribution_create(self):
        """Test case for distribution_create

        Create a distribution  # noqa: E501
        """
        pass

    def test_distribution_delete(self):
        """Test case for distribution_delete

        Delete a distribution  # noqa: E501
        """
        pass

    def test_distribution_show(self):
        """Test case for distribution_show

        Get a single distribution  # noqa: E501
        """
        pass

    def test_distribution_update(self):
        """Test case for distribution_update

        Update a distribution  # noqa: E501
        """
        pass

    def test_distributions_list(self):
        """Test case for distributions_list

        List distributions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
