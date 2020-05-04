# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Phrase.configuration import Configuration


class TranslationDetails1(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'user': 'UserPreview',
        'word_count': 'int'
    }

    attribute_map = {
        'user': 'user',
        'word_count': 'word_count'
    }

    def __init__(self, user=None, word_count=None, local_vars_configuration=None):  # noqa: E501
        """TranslationDetails1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._word_count = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if word_count is not None:
            self.word_count = word_count

    @property
    def user(self):
        """Gets the user of this TranslationDetails1.  # noqa: E501


        :return: The user of this TranslationDetails1.  # noqa: E501
        :rtype: UserPreview
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TranslationDetails1.


        :param user: The user of this TranslationDetails1.  # noqa: E501
        :type: UserPreview
        """

        self._user = user

    @property
    def word_count(self):
        """Gets the word_count of this TranslationDetails1.  # noqa: E501


        :return: The word_count of this TranslationDetails1.  # noqa: E501
        :rtype: int
        """
        return self._word_count

    @word_count.setter
    def word_count(self, word_count):
        """Sets the word_count of this TranslationDetails1.


        :param word_count: The word_count of this TranslationDetails1.  # noqa: E501
        :type: int
        """

        self._word_count = word_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TranslationDetails1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationDetails1):
            return True

        return self.to_dict() != other.to_dict()
