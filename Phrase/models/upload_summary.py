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


class UploadSummary(object):
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
        'locales_created': 'int',
        'translation_keys_created': 'int',
        'translation_keys_updated': 'int',
        'translation_keys_unmentioned': 'int',
        'translations_created': 'int',
        'translations_updated': 'int',
        'tags_created': 'int',
        'translation_keys_ignored': 'int'
    }

    attribute_map = {
        'locales_created': 'locales_created',
        'translation_keys_created': 'translation_keys_created',
        'translation_keys_updated': 'translation_keys_updated',
        'translation_keys_unmentioned': 'translation_keys_unmentioned',
        'translations_created': 'translations_created',
        'translations_updated': 'translations_updated',
        'tags_created': 'tags_created',
        'translation_keys_ignored': 'translation_keys_ignored'
    }

    def __init__(self, locales_created=None, translation_keys_created=None, translation_keys_updated=None, translation_keys_unmentioned=None, translations_created=None, translations_updated=None, tags_created=None, translation_keys_ignored=None, local_vars_configuration=None):  # noqa: E501
        """UploadSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._locales_created = None
        self._translation_keys_created = None
        self._translation_keys_updated = None
        self._translation_keys_unmentioned = None
        self._translations_created = None
        self._translations_updated = None
        self._tags_created = None
        self._translation_keys_ignored = None
        self.discriminator = None

        if locales_created is not None:
            self.locales_created = locales_created
        if translation_keys_created is not None:
            self.translation_keys_created = translation_keys_created
        if translation_keys_updated is not None:
            self.translation_keys_updated = translation_keys_updated
        if translation_keys_unmentioned is not None:
            self.translation_keys_unmentioned = translation_keys_unmentioned
        if translations_created is not None:
            self.translations_created = translations_created
        if translations_updated is not None:
            self.translations_updated = translations_updated
        if tags_created is not None:
            self.tags_created = tags_created
        if translation_keys_ignored is not None:
            self.translation_keys_ignored = translation_keys_ignored

    @property
    def locales_created(self):
        """Gets the locales_created of this UploadSummary.  # noqa: E501


        :return: The locales_created of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._locales_created

    @locales_created.setter
    def locales_created(self, locales_created):
        """Sets the locales_created of this UploadSummary.


        :param locales_created: The locales_created of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._locales_created = locales_created

    @property
    def translation_keys_created(self):
        """Gets the translation_keys_created of this UploadSummary.  # noqa: E501


        :return: The translation_keys_created of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._translation_keys_created

    @translation_keys_created.setter
    def translation_keys_created(self, translation_keys_created):
        """Sets the translation_keys_created of this UploadSummary.


        :param translation_keys_created: The translation_keys_created of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._translation_keys_created = translation_keys_created

    @property
    def translation_keys_updated(self):
        """Gets the translation_keys_updated of this UploadSummary.  # noqa: E501


        :return: The translation_keys_updated of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._translation_keys_updated

    @translation_keys_updated.setter
    def translation_keys_updated(self, translation_keys_updated):
        """Sets the translation_keys_updated of this UploadSummary.


        :param translation_keys_updated: The translation_keys_updated of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._translation_keys_updated = translation_keys_updated

    @property
    def translation_keys_unmentioned(self):
        """Gets the translation_keys_unmentioned of this UploadSummary.  # noqa: E501


        :return: The translation_keys_unmentioned of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._translation_keys_unmentioned

    @translation_keys_unmentioned.setter
    def translation_keys_unmentioned(self, translation_keys_unmentioned):
        """Sets the translation_keys_unmentioned of this UploadSummary.


        :param translation_keys_unmentioned: The translation_keys_unmentioned of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._translation_keys_unmentioned = translation_keys_unmentioned

    @property
    def translations_created(self):
        """Gets the translations_created of this UploadSummary.  # noqa: E501


        :return: The translations_created of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._translations_created

    @translations_created.setter
    def translations_created(self, translations_created):
        """Sets the translations_created of this UploadSummary.


        :param translations_created: The translations_created of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._translations_created = translations_created

    @property
    def translations_updated(self):
        """Gets the translations_updated of this UploadSummary.  # noqa: E501


        :return: The translations_updated of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._translations_updated

    @translations_updated.setter
    def translations_updated(self, translations_updated):
        """Sets the translations_updated of this UploadSummary.


        :param translations_updated: The translations_updated of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._translations_updated = translations_updated

    @property
    def tags_created(self):
        """Gets the tags_created of this UploadSummary.  # noqa: E501


        :return: The tags_created of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._tags_created

    @tags_created.setter
    def tags_created(self, tags_created):
        """Sets the tags_created of this UploadSummary.


        :param tags_created: The tags_created of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._tags_created = tags_created

    @property
    def translation_keys_ignored(self):
        """Gets the translation_keys_ignored of this UploadSummary.  # noqa: E501


        :return: The translation_keys_ignored of this UploadSummary.  # noqa: E501
        :rtype: int
        """
        return self._translation_keys_ignored

    @translation_keys_ignored.setter
    def translation_keys_ignored(self, translation_keys_ignored):
        """Sets the translation_keys_ignored of this UploadSummary.


        :param translation_keys_ignored: The translation_keys_ignored of this UploadSummary.  # noqa: E501
        :type: int
        """

        self._translation_keys_ignored = translation_keys_ignored

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
        if not isinstance(other, UploadSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UploadSummary):
            return True

        return self.to_dict() != other.to_dict()
