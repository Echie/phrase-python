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


class StyleguideCreateParameters(object):
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
        'title': 'str',
        'audience': 'str',
        'target_audience': 'str',
        'grammatical_person': 'str',
        'vocabulary_type': 'str',
        'business': 'str',
        'company_branding': 'str',
        'formatting': 'str',
        'glossary_terms': 'str',
        'grammar_consistency': 'str',
        'literal_translation': 'str',
        'overall_tone': 'str',
        'samples': 'str'
    }

    attribute_map = {
        'title': 'title',
        'audience': 'audience',
        'target_audience': 'target_audience',
        'grammatical_person': 'grammatical_person',
        'vocabulary_type': 'vocabulary_type',
        'business': 'business',
        'company_branding': 'company_branding',
        'formatting': 'formatting',
        'glossary_terms': 'glossary_terms',
        'grammar_consistency': 'grammar_consistency',
        'literal_translation': 'literal_translation',
        'overall_tone': 'overall_tone',
        'samples': 'samples'
    }

    def __init__(self, title=None, audience=None, target_audience=None, grammatical_person=None, vocabulary_type=None, business=None, company_branding=None, formatting=None, glossary_terms=None, grammar_consistency=None, literal_translation=None, overall_tone=None, samples=None, local_vars_configuration=None):  # noqa: E501
        """StyleguideCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._audience = None
        self._target_audience = None
        self._grammatical_person = None
        self._vocabulary_type = None
        self._business = None
        self._company_branding = None
        self._formatting = None
        self._glossary_terms = None
        self._grammar_consistency = None
        self._literal_translation = None
        self._overall_tone = None
        self._samples = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if audience is not None:
            self.audience = audience
        if target_audience is not None:
            self.target_audience = target_audience
        if grammatical_person is not None:
            self.grammatical_person = grammatical_person
        if vocabulary_type is not None:
            self.vocabulary_type = vocabulary_type
        if business is not None:
            self.business = business
        if company_branding is not None:
            self.company_branding = company_branding
        if formatting is not None:
            self.formatting = formatting
        if glossary_terms is not None:
            self.glossary_terms = glossary_terms
        if grammar_consistency is not None:
            self.grammar_consistency = grammar_consistency
        if literal_translation is not None:
            self.literal_translation = literal_translation
        if overall_tone is not None:
            self.overall_tone = overall_tone
        if samples is not None:
            self.samples = samples

    @property
    def title(self):
        """Gets the title of this StyleguideCreateParameters.  # noqa: E501

        Style guide title  # noqa: E501

        :return: The title of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this StyleguideCreateParameters.

        Style guide title  # noqa: E501

        :param title: The title of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def audience(self):
        """Gets the audience of this StyleguideCreateParameters.  # noqa: E501

        Audience description  # noqa: E501

        :return: The audience of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this StyleguideCreateParameters.

        Audience description  # noqa: E501

        :param audience: The audience of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._audience = audience

    @property
    def target_audience(self):
        """Gets the target_audience of this StyleguideCreateParameters.  # noqa: E501

        Can be one of: not_specified, children, teenager, young_adults, adults, old_adults.  # noqa: E501

        :return: The target_audience of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this StyleguideCreateParameters.

        Can be one of: not_specified, children, teenager, young_adults, adults, old_adults.  # noqa: E501

        :param target_audience: The target_audience of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._target_audience = target_audience

    @property
    def grammatical_person(self):
        """Gets the grammatical_person of this StyleguideCreateParameters.  # noqa: E501

        Can be one of: not_specified, first_person_singular, second_person_singular, third_person_singular_masculine, third_person_singular_feminine, third_person_singular_neuter, first_person_plural, second_person_plural, third_person_plural.  # noqa: E501

        :return: The grammatical_person of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._grammatical_person

    @grammatical_person.setter
    def grammatical_person(self, grammatical_person):
        """Sets the grammatical_person of this StyleguideCreateParameters.

        Can be one of: not_specified, first_person_singular, second_person_singular, third_person_singular_masculine, third_person_singular_feminine, third_person_singular_neuter, first_person_plural, second_person_plural, third_person_plural.  # noqa: E501

        :param grammatical_person: The grammatical_person of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._grammatical_person = grammatical_person

    @property
    def vocabulary_type(self):
        """Gets the vocabulary_type of this StyleguideCreateParameters.  # noqa: E501

        Can be one of: not_specified, popular, technical, fictional.  # noqa: E501

        :return: The vocabulary_type of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._vocabulary_type

    @vocabulary_type.setter
    def vocabulary_type(self, vocabulary_type):
        """Sets the vocabulary_type of this StyleguideCreateParameters.

        Can be one of: not_specified, popular, technical, fictional.  # noqa: E501

        :param vocabulary_type: The vocabulary_type of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._vocabulary_type = vocabulary_type

    @property
    def business(self):
        """Gets the business of this StyleguideCreateParameters.  # noqa: E501

        Description of the business  # noqa: E501

        :return: The business of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._business

    @business.setter
    def business(self, business):
        """Sets the business of this StyleguideCreateParameters.

        Description of the business  # noqa: E501

        :param business: The business of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._business = business

    @property
    def company_branding(self):
        """Gets the company_branding of this StyleguideCreateParameters.  # noqa: E501

        Company branding to remain consistent.  # noqa: E501

        :return: The company_branding of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._company_branding

    @company_branding.setter
    def company_branding(self, company_branding):
        """Sets the company_branding of this StyleguideCreateParameters.

        Company branding to remain consistent.  # noqa: E501

        :param company_branding: The company_branding of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._company_branding = company_branding

    @property
    def formatting(self):
        """Gets the formatting of this StyleguideCreateParameters.  # noqa: E501

        Formatting requirements and character limitations.  # noqa: E501

        :return: The formatting of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._formatting

    @formatting.setter
    def formatting(self, formatting):
        """Sets the formatting of this StyleguideCreateParameters.

        Formatting requirements and character limitations.  # noqa: E501

        :param formatting: The formatting of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._formatting = formatting

    @property
    def glossary_terms(self):
        """Gets the glossary_terms of this StyleguideCreateParameters.  # noqa: E501

        List of terms and/or phrases that need to be translated consistently.  # noqa: E501

        :return: The glossary_terms of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._glossary_terms

    @glossary_terms.setter
    def glossary_terms(self, glossary_terms):
        """Sets the glossary_terms of this StyleguideCreateParameters.

        List of terms and/or phrases that need to be translated consistently.  # noqa: E501

        :param glossary_terms: The glossary_terms of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._glossary_terms = glossary_terms

    @property
    def grammar_consistency(self):
        """Gets the grammar_consistency of this StyleguideCreateParameters.  # noqa: E501

        Formal or informal pronouns, consistent conjugation, grammatical gender  # noqa: E501

        :return: The grammar_consistency of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._grammar_consistency

    @grammar_consistency.setter
    def grammar_consistency(self, grammar_consistency):
        """Sets the grammar_consistency of this StyleguideCreateParameters.

        Formal or informal pronouns, consistent conjugation, grammatical gender  # noqa: E501

        :param grammar_consistency: The grammar_consistency of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._grammar_consistency = grammar_consistency

    @property
    def literal_translation(self):
        """Gets the literal_translation of this StyleguideCreateParameters.  # noqa: E501

        Can be one of: Cultural/Conversational, Literal, Neutral.  # noqa: E501

        :return: The literal_translation of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._literal_translation

    @literal_translation.setter
    def literal_translation(self, literal_translation):
        """Sets the literal_translation of this StyleguideCreateParameters.

        Can be one of: Cultural/Conversational, Literal, Neutral.  # noqa: E501

        :param literal_translation: The literal_translation of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._literal_translation = literal_translation

    @property
    def overall_tone(self):
        """Gets the overall_tone of this StyleguideCreateParameters.  # noqa: E501

        Tone requirement descriptions  # noqa: E501

        :return: The overall_tone of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._overall_tone

    @overall_tone.setter
    def overall_tone(self, overall_tone):
        """Sets the overall_tone of this StyleguideCreateParameters.

        Tone requirement descriptions  # noqa: E501

        :param overall_tone: The overall_tone of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._overall_tone = overall_tone

    @property
    def samples(self):
        """Gets the samples of this StyleguideCreateParameters.  # noqa: E501

        Provide links to sample product pages, FAQ pages, etc. to give the translator a point of reference. You can also provide past translations. Even snippets or short paragraphs are helpful for maintaining consistency.  # noqa: E501

        :return: The samples of this StyleguideCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this StyleguideCreateParameters.

        Provide links to sample product pages, FAQ pages, etc. to give the translator a point of reference. You can also provide past translations. Even snippets or short paragraphs are helpful for maintaining consistency.  # noqa: E501

        :param samples: The samples of this StyleguideCreateParameters.  # noqa: E501
        :type: str
        """

        self._samples = samples

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
        if not isinstance(other, StyleguideCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StyleguideCreateParameters):
            return True

        return self.to_dict() != other.to_dict()
