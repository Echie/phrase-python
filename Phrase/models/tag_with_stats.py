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


class TagWithStats(object):
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
        'name': 'str',
        'keys_count': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'statistics': 'list[TagWithStats1Statistics1]'
    }

    attribute_map = {
        'name': 'name',
        'keys_count': 'keys_count',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'statistics': 'statistics'
    }

    def __init__(self, name=None, keys_count=None, created_at=None, updated_at=None, statistics=None, local_vars_configuration=None):  # noqa: E501
        """TagWithStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._keys_count = None
        self._created_at = None
        self._updated_at = None
        self._statistics = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if keys_count is not None:
            self.keys_count = keys_count
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if statistics is not None:
            self.statistics = statistics

    @property
    def name(self):
        """Gets the name of this TagWithStats.  # noqa: E501


        :return: The name of this TagWithStats.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TagWithStats.


        :param name: The name of this TagWithStats.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def keys_count(self):
        """Gets the keys_count of this TagWithStats.  # noqa: E501


        :return: The keys_count of this TagWithStats.  # noqa: E501
        :rtype: int
        """
        return self._keys_count

    @keys_count.setter
    def keys_count(self, keys_count):
        """Sets the keys_count of this TagWithStats.


        :param keys_count: The keys_count of this TagWithStats.  # noqa: E501
        :type: int
        """

        self._keys_count = keys_count

    @property
    def created_at(self):
        """Gets the created_at of this TagWithStats.  # noqa: E501


        :return: The created_at of this TagWithStats.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TagWithStats.


        :param created_at: The created_at of this TagWithStats.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TagWithStats.  # noqa: E501


        :return: The updated_at of this TagWithStats.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TagWithStats.


        :param updated_at: The updated_at of this TagWithStats.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def statistics(self):
        """Gets the statistics of this TagWithStats.  # noqa: E501


        :return: The statistics of this TagWithStats.  # noqa: E501
        :rtype: list[TagWithStats1Statistics1]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this TagWithStats.


        :param statistics: The statistics of this TagWithStats.  # noqa: E501
        :type: list[TagWithStats1Statistics1]
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
        if not isinstance(other, TagWithStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagWithStats):
            return True

        return self.to_dict() != other.to_dict()
