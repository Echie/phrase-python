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


class TranslationsUnverifyParameters(object):
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
        'branch': 'str',
        'q': 'str',
        'sort': 'str',
        'order': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'q': 'q',
        'sort': 'sort',
        'order': 'order'
    }

    def __init__(self, branch=None, q=None, sort=None, order=None, local_vars_configuration=None):  # noqa: E501
        """TranslationsUnverifyParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch = None
        self._q = None
        self._sort = None
        self._order = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if q is not None:
            self.q = q
        if sort is not None:
            self.sort = sort
        if order is not None:
            self.order = order

    @property
    def branch(self):
        """Gets the branch of this TranslationsUnverifyParameters.  # noqa: E501

        specify the branch to use  # noqa: E501

        :return: The branch of this TranslationsUnverifyParameters.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this TranslationsUnverifyParameters.

        specify the branch to use  # noqa: E501

        :param branch: The branch of this TranslationsUnverifyParameters.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def q(self):
        """Gets the q of this TranslationsUnverifyParameters.  # noqa: E501

        q_description_placeholder  # noqa: E501

        :return: The q of this TranslationsUnverifyParameters.  # noqa: E501
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """Sets the q of this TranslationsUnverifyParameters.

        q_description_placeholder  # noqa: E501

        :param q: The q of this TranslationsUnverifyParameters.  # noqa: E501
        :type: str
        """

        self._q = q

    @property
    def sort(self):
        """Gets the sort of this TranslationsUnverifyParameters.  # noqa: E501

        Sort criteria. Can be one of: key_name, created_at, updated_at.  # noqa: E501

        :return: The sort of this TranslationsUnverifyParameters.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this TranslationsUnverifyParameters.

        Sort criteria. Can be one of: key_name, created_at, updated_at.  # noqa: E501

        :param sort: The sort of this TranslationsUnverifyParameters.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def order(self):
        """Gets the order of this TranslationsUnverifyParameters.  # noqa: E501

        Order direction. Can be one of: asc, desc.  # noqa: E501

        :return: The order of this TranslationsUnverifyParameters.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this TranslationsUnverifyParameters.

        Order direction. Can be one of: asc, desc.  # noqa: E501

        :param order: The order of this TranslationsUnverifyParameters.  # noqa: E501
        :type: str
        """

        self._order = order

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
        if not isinstance(other, TranslationsUnverifyParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationsUnverifyParameters):
            return True

        return self.to_dict() != other.to_dict()
