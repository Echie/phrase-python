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


class LocaleStatistics(object):
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
        'keys_total_count': 'int',
        'keys_untranslated_count': 'int',
        'words_total_count': 'int',
        'translations_completed_count': 'int',
        'translations_unverified_count': 'int',
        'unverified_words_count': 'int',
        'missing_words_count': 'int'
    }

    attribute_map = {
        'keys_total_count': 'keys_total_count',
        'keys_untranslated_count': 'keys_untranslated_count',
        'words_total_count': 'words_total_count',
        'translations_completed_count': 'translations_completed_count',
        'translations_unverified_count': 'translations_unverified_count',
        'unverified_words_count': 'unverified_words_count',
        'missing_words_count': 'missing_words_count'
    }

    def __init__(self, keys_total_count=None, keys_untranslated_count=None, words_total_count=None, translations_completed_count=None, translations_unverified_count=None, unverified_words_count=None, missing_words_count=None, local_vars_configuration=None):  # noqa: E501
        """LocaleStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keys_total_count = None
        self._keys_untranslated_count = None
        self._words_total_count = None
        self._translations_completed_count = None
        self._translations_unverified_count = None
        self._unverified_words_count = None
        self._missing_words_count = None
        self.discriminator = None

        if keys_total_count is not None:
            self.keys_total_count = keys_total_count
        if keys_untranslated_count is not None:
            self.keys_untranslated_count = keys_untranslated_count
        if words_total_count is not None:
            self.words_total_count = words_total_count
        if translations_completed_count is not None:
            self.translations_completed_count = translations_completed_count
        if translations_unverified_count is not None:
            self.translations_unverified_count = translations_unverified_count
        if unverified_words_count is not None:
            self.unverified_words_count = unverified_words_count
        if missing_words_count is not None:
            self.missing_words_count = missing_words_count

    @property
    def keys_total_count(self):
        """Gets the keys_total_count of this LocaleStatistics.  # noqa: E501


        :return: The keys_total_count of this LocaleStatistics.  # noqa: E501
        :rtype: int
        """
        return self._keys_total_count

    @keys_total_count.setter
    def keys_total_count(self, keys_total_count):
        """Sets the keys_total_count of this LocaleStatistics.


        :param keys_total_count: The keys_total_count of this LocaleStatistics.  # noqa: E501
        :type: int
        """

        self._keys_total_count = keys_total_count

    @property
    def keys_untranslated_count(self):
        """Gets the keys_untranslated_count of this LocaleStatistics.  # noqa: E501


        :return: The keys_untranslated_count of this LocaleStatistics.  # noqa: E501
        :rtype: int
        """
        return self._keys_untranslated_count

    @keys_untranslated_count.setter
    def keys_untranslated_count(self, keys_untranslated_count):
        """Sets the keys_untranslated_count of this LocaleStatistics.


        :param keys_untranslated_count: The keys_untranslated_count of this LocaleStatistics.  # noqa: E501
        :type: int
        """

        self._keys_untranslated_count = keys_untranslated_count

    @property
    def words_total_count(self):
        """Gets the words_total_count of this LocaleStatistics.  # noqa: E501


        :return: The words_total_count of this LocaleStatistics.  # noqa: E501
        :rtype: int
        """
        return self._words_total_count

    @words_total_count.setter
    def words_total_count(self, words_total_count):
        """Sets the words_total_count of this LocaleStatistics.


        :param words_total_count: The words_total_count of this LocaleStatistics.  # noqa: E501
        :type: int
        """

        self._words_total_count = words_total_count

    @property
    def translations_completed_count(self):
        """Gets the translations_completed_count of this LocaleStatistics.  # noqa: E501


        :return: The translations_completed_count of this LocaleStatistics.  # noqa: E501
        :rtype: int
        """
        return self._translations_completed_count

    @translations_completed_count.setter
    def translations_completed_count(self, translations_completed_count):
        """Sets the translations_completed_count of this LocaleStatistics.


        :param translations_completed_count: The translations_completed_count of this LocaleStatistics.  # noqa: E501
        :type: int
        """

        self._translations_completed_count = translations_completed_count

    @property
    def translations_unverified_count(self):
        """Gets the translations_unverified_count of this LocaleStatistics.  # noqa: E501


        :return: The translations_unverified_count of this LocaleStatistics.  # noqa: E501
        :rtype: int
        """
        return self._translations_unverified_count

    @translations_unverified_count.setter
    def translations_unverified_count(self, translations_unverified_count):
        """Sets the translations_unverified_count of this LocaleStatistics.


        :param translations_unverified_count: The translations_unverified_count of this LocaleStatistics.  # noqa: E501
        :type: int
        """

        self._translations_unverified_count = translations_unverified_count

    @property
    def unverified_words_count(self):
        """Gets the unverified_words_count of this LocaleStatistics.  # noqa: E501


        :return: The unverified_words_count of this LocaleStatistics.  # noqa: E501
        :rtype: int
        """
        return self._unverified_words_count

    @unverified_words_count.setter
    def unverified_words_count(self, unverified_words_count):
        """Sets the unverified_words_count of this LocaleStatistics.


        :param unverified_words_count: The unverified_words_count of this LocaleStatistics.  # noqa: E501
        :type: int
        """

        self._unverified_words_count = unverified_words_count

    @property
    def missing_words_count(self):
        """Gets the missing_words_count of this LocaleStatistics.  # noqa: E501


        :return: The missing_words_count of this LocaleStatistics.  # noqa: E501
        :rtype: int
        """
        return self._missing_words_count

    @missing_words_count.setter
    def missing_words_count(self, missing_words_count):
        """Sets the missing_words_count of this LocaleStatistics.


        :param missing_words_count: The missing_words_count of this LocaleStatistics.  # noqa: E501
        :type: int
        """

        self._missing_words_count = missing_words_count

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
        if not isinstance(other, LocaleStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocaleStatistics):
            return True

        return self.to_dict() != other.to_dict()
