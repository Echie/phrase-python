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


class TagWithStats1Statistics1(object):
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
        'locale': 'LocalePreview',
        'statistics': 'TagWithStats1Statistics'
    }

    attribute_map = {
        'locale': 'locale',
        'statistics': 'statistics'
    }

    def __init__(self, locale=None, statistics=None, local_vars_configuration=None):  # noqa: E501
        """TagWithStats1Statistics1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._locale = None
        self._statistics = None
        self.discriminator = None

        if locale is not None:
            self.locale = locale
        if statistics is not None:
            self.statistics = statistics

    @property
    def locale(self):
        """Gets the locale of this TagWithStats1Statistics1.  # noqa: E501


        :return: The locale of this TagWithStats1Statistics1.  # noqa: E501
        :rtype: LocalePreview
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this TagWithStats1Statistics1.


        :param locale: The locale of this TagWithStats1Statistics1.  # noqa: E501
        :type: LocalePreview
        """

        self._locale = locale

    @property
    def statistics(self):
        """Gets the statistics of this TagWithStats1Statistics1.  # noqa: E501


        :return: The statistics of this TagWithStats1Statistics1.  # noqa: E501
        :rtype: TagWithStats1Statistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this TagWithStats1Statistics1.


        :param statistics: The statistics of this TagWithStats1Statistics1.  # noqa: E501
        :type: TagWithStats1Statistics
        """

        self._statistics = statistics

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
        if not isinstance(other, TagWithStats1Statistics1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagWithStats1Statistics1):
            return True

        return self.to_dict() != other.to_dict()
