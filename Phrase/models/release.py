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


class Release(object):
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
        'id': 'str',
        'version': 'int',
        'app_min_version': 'str',
        'app_max_version': 'str',
        'description': 'str',
        'platforms': 'list[str]',
        'environments': 'list[str]',
        'locales': 'list[LocalePreview]',
        'project': 'ProjectShort',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'app_min_version': 'app_min_version',
        'app_max_version': 'app_max_version',
        'description': 'description',
        'platforms': 'platforms',
        'environments': 'environments',
        'locales': 'locales',
        'project': 'project',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, version=None, app_min_version=None, app_max_version=None, description=None, platforms=None, environments=None, locales=None, project=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Release - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._version = None
        self._app_min_version = None
        self._app_max_version = None
        self._description = None
        self._platforms = None
        self._environments = None
        self._locales = None
        self._project = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if app_min_version is not None:
            self.app_min_version = app_min_version
        if app_max_version is not None:
            self.app_max_version = app_max_version
        if description is not None:
            self.description = description
        if platforms is not None:
            self.platforms = platforms
        if environments is not None:
            self.environments = environments
        if locales is not None:
            self.locales = locales
        if project is not None:
            self.project = project
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Release.  # noqa: E501


        :return: The id of this Release.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Release.


        :param id: The id of this Release.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this Release.  # noqa: E501


        :return: The version of this Release.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Release.


        :param version: The version of this Release.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def app_min_version(self):
        """Gets the app_min_version of this Release.  # noqa: E501


        :return: The app_min_version of this Release.  # noqa: E501
        :rtype: str
        """
        return self._app_min_version

    @app_min_version.setter
    def app_min_version(self, app_min_version):
        """Sets the app_min_version of this Release.


        :param app_min_version: The app_min_version of this Release.  # noqa: E501
        :type: str
        """

        self._app_min_version = app_min_version

    @property
    def app_max_version(self):
        """Gets the app_max_version of this Release.  # noqa: E501


        :return: The app_max_version of this Release.  # noqa: E501
        :rtype: str
        """
        return self._app_max_version

    @app_max_version.setter
    def app_max_version(self, app_max_version):
        """Sets the app_max_version of this Release.


        :param app_max_version: The app_max_version of this Release.  # noqa: E501
        :type: str
        """

        self._app_max_version = app_max_version

    @property
    def description(self):
        """Gets the description of this Release.  # noqa: E501


        :return: The description of this Release.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Release.


        :param description: The description of this Release.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def platforms(self):
        """Gets the platforms of this Release.  # noqa: E501


        :return: The platforms of this Release.  # noqa: E501
        :rtype: list[str]
        """
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        """Sets the platforms of this Release.


        :param platforms: The platforms of this Release.  # noqa: E501
        :type: list[str]
        """

        self._platforms = platforms

    @property
    def environments(self):
        """Gets the environments of this Release.  # noqa: E501


        :return: The environments of this Release.  # noqa: E501
        :rtype: list[str]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this Release.


        :param environments: The environments of this Release.  # noqa: E501
        :type: list[str]
        """

        self._environments = environments

    @property
    def locales(self):
        """Gets the locales of this Release.  # noqa: E501


        :return: The locales of this Release.  # noqa: E501
        :rtype: list[LocalePreview]
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        """Sets the locales of this Release.


        :param locales: The locales of this Release.  # noqa: E501
        :type: list[LocalePreview]
        """

        self._locales = locales

    @property
    def project(self):
        """Gets the project of this Release.  # noqa: E501


        :return: The project of this Release.  # noqa: E501
        :rtype: ProjectShort
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Release.


        :param project: The project of this Release.  # noqa: E501
        :type: ProjectShort
        """

        self._project = project

    @property
    def created_at(self):
        """Gets the created_at of this Release.  # noqa: E501


        :return: The created_at of this Release.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Release.


        :param created_at: The created_at of this Release.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Release.  # noqa: E501


        :return: The updated_at of this Release.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Release.


        :param updated_at: The updated_at of this Release.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Release):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Release):
            return True

        return self.to_dict() != other.to_dict()
