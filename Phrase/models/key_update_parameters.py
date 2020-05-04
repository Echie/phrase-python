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


class KeyUpdateParameters(object):
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
        'name': 'str',
        'description': 'str',
        'plural': 'bool',
        'name_plural': 'str',
        'data_type': 'str',
        'tags': 'str',
        'max_characters_allowed': 'int',
        'screenshot': 'file',
        'remove_screenshot': 'bool',
        'unformatted': 'bool',
        'xml_space_preserve': 'bool',
        'original_file': 'str',
        'localized_format_string': 'str',
        'localized_format_key': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'name': 'name',
        'description': 'description',
        'plural': 'plural',
        'name_plural': 'name_plural',
        'data_type': 'data_type',
        'tags': 'tags',
        'max_characters_allowed': 'max_characters_allowed',
        'screenshot': 'screenshot',
        'remove_screenshot': 'remove_screenshot',
        'unformatted': 'unformatted',
        'xml_space_preserve': 'xml_space_preserve',
        'original_file': 'original_file',
        'localized_format_string': 'localized_format_string',
        'localized_format_key': 'localized_format_key'
    }

    def __init__(self, branch=None, name=None, description=None, plural=None, name_plural=None, data_type=None, tags=None, max_characters_allowed=None, screenshot=None, remove_screenshot=None, unformatted=None, xml_space_preserve=None, original_file=None, localized_format_string=None, localized_format_key=None, local_vars_configuration=None):  # noqa: E501
        """KeyUpdateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch = None
        self._name = None
        self._description = None
        self._plural = None
        self._name_plural = None
        self._data_type = None
        self._tags = None
        self._max_characters_allowed = None
        self._screenshot = None
        self._remove_screenshot = None
        self._unformatted = None
        self._xml_space_preserve = None
        self._original_file = None
        self._localized_format_string = None
        self._localized_format_key = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if plural is not None:
            self.plural = plural
        if name_plural is not None:
            self.name_plural = name_plural
        if data_type is not None:
            self.data_type = data_type
        if tags is not None:
            self.tags = tags
        if max_characters_allowed is not None:
            self.max_characters_allowed = max_characters_allowed
        if screenshot is not None:
            self.screenshot = screenshot
        if remove_screenshot is not None:
            self.remove_screenshot = remove_screenshot
        if unformatted is not None:
            self.unformatted = unformatted
        if xml_space_preserve is not None:
            self.xml_space_preserve = xml_space_preserve
        if original_file is not None:
            self.original_file = original_file
        if localized_format_string is not None:
            self.localized_format_string = localized_format_string
        if localized_format_key is not None:
            self.localized_format_key = localized_format_key

    @property
    def branch(self):
        """Gets the branch of this KeyUpdateParameters.  # noqa: E501

        specify the branch to use  # noqa: E501

        :return: The branch of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this KeyUpdateParameters.

        specify the branch to use  # noqa: E501

        :param branch: The branch of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def name(self):
        """Gets the name of this KeyUpdateParameters.  # noqa: E501

        Key name  # noqa: E501

        :return: The name of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeyUpdateParameters.

        Key name  # noqa: E501

        :param name: The name of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this KeyUpdateParameters.  # noqa: E501

        Key description (usually includes contextual information for translators)  # noqa: E501

        :return: The description of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeyUpdateParameters.

        Key description (usually includes contextual information for translators)  # noqa: E501

        :param description: The description of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def plural(self):
        """Gets the plural of this KeyUpdateParameters.  # noqa: E501

        Indicates whether key supports pluralization  # noqa: E501

        :return: The plural of this KeyUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._plural

    @plural.setter
    def plural(self, plural):
        """Sets the plural of this KeyUpdateParameters.

        Indicates whether key supports pluralization  # noqa: E501

        :param plural: The plural of this KeyUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._plural = plural

    @property
    def name_plural(self):
        """Gets the name_plural of this KeyUpdateParameters.  # noqa: E501

        Plural name for the key (used in some file formats, e.g. Gettext)  # noqa: E501

        :return: The name_plural of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._name_plural

    @name_plural.setter
    def name_plural(self, name_plural):
        """Sets the name_plural of this KeyUpdateParameters.

        Plural name for the key (used in some file formats, e.g. Gettext)  # noqa: E501

        :param name_plural: The name_plural of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._name_plural = name_plural

    @property
    def data_type(self):
        """Gets the data_type of this KeyUpdateParameters.  # noqa: E501

        Type of the key. Can be one of the following: string, number, boolean, array, markdown.  # noqa: E501

        :return: The data_type of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this KeyUpdateParameters.

        Type of the key. Can be one of the following: string, number, boolean, array, markdown.  # noqa: E501

        :param data_type: The data_type of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def tags(self):
        """Gets the tags of this KeyUpdateParameters.  # noqa: E501

        List of tags separated by comma to be associated with the key.  # noqa: E501

        :return: The tags of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this KeyUpdateParameters.

        List of tags separated by comma to be associated with the key.  # noqa: E501

        :param tags: The tags of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def max_characters_allowed(self):
        """Gets the max_characters_allowed of this KeyUpdateParameters.  # noqa: E501

        Max. number of characters translations for this key can have.  # noqa: E501

        :return: The max_characters_allowed of this KeyUpdateParameters.  # noqa: E501
        :rtype: int
        """
        return self._max_characters_allowed

    @max_characters_allowed.setter
    def max_characters_allowed(self, max_characters_allowed):
        """Sets the max_characters_allowed of this KeyUpdateParameters.

        Max. number of characters translations for this key can have.  # noqa: E501

        :param max_characters_allowed: The max_characters_allowed of this KeyUpdateParameters.  # noqa: E501
        :type: int
        """

        self._max_characters_allowed = max_characters_allowed

    @property
    def screenshot(self):
        """Gets the screenshot of this KeyUpdateParameters.  # noqa: E501

        Screenshot/image for the key. This parameter is deprecated. Please use the Screenshots endpoint instead.  # noqa: E501

        :return: The screenshot of this KeyUpdateParameters.  # noqa: E501
        :rtype: file
        """
        return self._screenshot

    @screenshot.setter
    def screenshot(self, screenshot):
        """Sets the screenshot of this KeyUpdateParameters.

        Screenshot/image for the key. This parameter is deprecated. Please use the Screenshots endpoint instead.  # noqa: E501

        :param screenshot: The screenshot of this KeyUpdateParameters.  # noqa: E501
        :type: file
        """

        self._screenshot = screenshot

    @property
    def remove_screenshot(self):
        """Gets the remove_screenshot of this KeyUpdateParameters.  # noqa: E501

        Indicates whether the screenshot will be deleted. This parameter is deprecated. Please use the Screenshots endpoint instead.  # noqa: E501

        :return: The remove_screenshot of this KeyUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._remove_screenshot

    @remove_screenshot.setter
    def remove_screenshot(self, remove_screenshot):
        """Sets the remove_screenshot of this KeyUpdateParameters.

        Indicates whether the screenshot will be deleted. This parameter is deprecated. Please use the Screenshots endpoint instead.  # noqa: E501

        :param remove_screenshot: The remove_screenshot of this KeyUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._remove_screenshot = remove_screenshot

    @property
    def unformatted(self):
        """Gets the unformatted of this KeyUpdateParameters.  # noqa: E501

        Indicates whether the key should be exported as \"unformatted\". Supported by Android XML and other formats.  # noqa: E501

        :return: The unformatted of this KeyUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._unformatted

    @unformatted.setter
    def unformatted(self, unformatted):
        """Sets the unformatted of this KeyUpdateParameters.

        Indicates whether the key should be exported as \"unformatted\". Supported by Android XML and other formats.  # noqa: E501

        :param unformatted: The unformatted of this KeyUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._unformatted = unformatted

    @property
    def xml_space_preserve(self):
        """Gets the xml_space_preserve of this KeyUpdateParameters.  # noqa: E501

        Indicates whether the key should be exported with \"xml:space=preserve\". Supported by several XML-based formats.  # noqa: E501

        :return: The xml_space_preserve of this KeyUpdateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._xml_space_preserve

    @xml_space_preserve.setter
    def xml_space_preserve(self, xml_space_preserve):
        """Sets the xml_space_preserve of this KeyUpdateParameters.

        Indicates whether the key should be exported with \"xml:space=preserve\". Supported by several XML-based formats.  # noqa: E501

        :param xml_space_preserve: The xml_space_preserve of this KeyUpdateParameters.  # noqa: E501
        :type: bool
        """

        self._xml_space_preserve = xml_space_preserve

    @property
    def original_file(self):
        """Gets the original_file of this KeyUpdateParameters.  # noqa: E501

        Original file attribute. Used in some formats, e.g. XLIFF.  # noqa: E501

        :return: The original_file of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._original_file

    @original_file.setter
    def original_file(self, original_file):
        """Sets the original_file of this KeyUpdateParameters.

        Original file attribute. Used in some formats, e.g. XLIFF.  # noqa: E501

        :param original_file: The original_file of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._original_file = original_file

    @property
    def localized_format_string(self):
        """Gets the localized_format_string of this KeyUpdateParameters.  # noqa: E501

        NSStringLocalizedFormatKey attribute. Used in .stringsdict format.  # noqa: E501

        :return: The localized_format_string of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._localized_format_string

    @localized_format_string.setter
    def localized_format_string(self, localized_format_string):
        """Sets the localized_format_string of this KeyUpdateParameters.

        NSStringLocalizedFormatKey attribute. Used in .stringsdict format.  # noqa: E501

        :param localized_format_string: The localized_format_string of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._localized_format_string = localized_format_string

    @property
    def localized_format_key(self):
        """Gets the localized_format_key of this KeyUpdateParameters.  # noqa: E501

        NSStringLocalizedFormatKey attribute. Used in .stringsdict format.  # noqa: E501

        :return: The localized_format_key of this KeyUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._localized_format_key

    @localized_format_key.setter
    def localized_format_key(self, localized_format_key):
        """Sets the localized_format_key of this KeyUpdateParameters.

        NSStringLocalizedFormatKey attribute. Used in .stringsdict format.  # noqa: E501

        :param localized_format_key: The localized_format_key of this KeyUpdateParameters.  # noqa: E501
        :type: str
        """

        self._localized_format_key = localized_format_key

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
        if not isinstance(other, KeyUpdateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeyUpdateParameters):
            return True

        return self.to_dict() != other.to_dict()
