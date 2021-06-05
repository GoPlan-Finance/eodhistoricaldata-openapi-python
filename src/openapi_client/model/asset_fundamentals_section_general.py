"""
    EOD Historical Data API

    EOD Historical Data API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sam@sddproductions.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.asset_fundamentals_section_general_address_data import AssetFundamentalsSectionGeneralAddressData
    globals()['AssetFundamentalsSectionGeneralAddressData'] = AssetFundamentalsSectionGeneralAddressData


class AssetFundamentalsSectionGeneral(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'code': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'exchange': (str,),  # noqa: E501
            'currency_code': (str,),  # noqa: E501
            'currency_name': (str,),  # noqa: E501
            'currency_symbol': (str,),  # noqa: E501
            'country_name': (str,),  # noqa: E501
            'country_iso': (str,),  # noqa: E501
            'isin': (str,),  # noqa: E501
            'cusip': (str,),  # noqa: E501
            'cik': (str,),  # noqa: E501
            'employer_id_number': (str,),  # noqa: E501
            'fiscal_year_end': (str,),  # noqa: E501
            'ipo_date': (date,),  # noqa: E501
            'international_domestic': (str,),  # noqa: E501
            'sector': (str,),  # noqa: E501
            'industry': (str,),  # noqa: E501
            'gic_sector': (str,),  # noqa: E501
            'gic_group': (str,),  # noqa: E501
            'gic_industry': (str,),  # noqa: E501
            'gic_sub_industry': (str,),  # noqa: E501
            'home_category': (str,),  # noqa: E501
            'is_delisted': (bool,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'address': (str,),  # noqa: E501
            'address_data': (AssetFundamentalsSectionGeneralAddressData,),  # noqa: E501
            'listings': ([object],),  # noqa: E501
            'officers': ([object],),  # noqa: E501
            'phone': (str,),  # noqa: E501
            'web_url': (str,),  # noqa: E501
            'logo_url': (str,),  # noqa: E501
            'full_time_employees': (float,),  # noqa: E501
            'updated_at': (date,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'code': 'Code',  # noqa: E501
        'type': 'Type',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'exchange': 'Exchange',  # noqa: E501
        'currency_code': 'CurrencyCode',  # noqa: E501
        'currency_name': 'CurrencyName',  # noqa: E501
        'currency_symbol': 'CurrencySymbol',  # noqa: E501
        'country_name': 'CountryName',  # noqa: E501
        'country_iso': 'CountryISO',  # noqa: E501
        'isin': 'ISIN',  # noqa: E501
        'cusip': 'CUSIP',  # noqa: E501
        'cik': 'CIK',  # noqa: E501
        'employer_id_number': 'EmployerIdNumber',  # noqa: E501
        'fiscal_year_end': 'FiscalYearEnd',  # noqa: E501
        'ipo_date': 'IPODate',  # noqa: E501
        'international_domestic': 'InternationalDomestic',  # noqa: E501
        'sector': 'Sector',  # noqa: E501
        'industry': 'Industry',  # noqa: E501
        'gic_sector': 'GicSector',  # noqa: E501
        'gic_group': 'GicGroup',  # noqa: E501
        'gic_industry': 'GicIndustry',  # noqa: E501
        'gic_sub_industry': 'GicSubIndustry',  # noqa: E501
        'home_category': 'HomeCategory',  # noqa: E501
        'is_delisted': 'IsDelisted',  # noqa: E501
        'description': 'Description',  # noqa: E501
        'address': 'Address',  # noqa: E501
        'address_data': 'AddressData',  # noqa: E501
        'listings': 'Listings',  # noqa: E501
        'officers': 'Officers',  # noqa: E501
        'phone': 'Phone',  # noqa: E501
        'web_url': 'WebURL',  # noqa: E501
        'logo_url': 'LogoURL',  # noqa: E501
        'full_time_employees': 'FullTimeEmployees',  # noqa: E501
        'updated_at': 'UpdatedAt',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, code, type, name, exchange, *args, **kwargs):  # noqa: E501
        """AssetFundamentalsSectionGeneral - a model defined in OpenAPI

        Args:
            code (str):
            type (str):
            name (str):
            exchange (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            currency_code (str): [optional]  # noqa: E501
            currency_name (str): [optional]  # noqa: E501
            currency_symbol (str): [optional]  # noqa: E501
            country_name (str): [optional]  # noqa: E501
            country_iso (str): [optional]  # noqa: E501
            isin (str): [optional]  # noqa: E501
            cusip (str): [optional]  # noqa: E501
            cik (str): [optional]  # noqa: E501
            employer_id_number (str): [optional]  # noqa: E501
            fiscal_year_end (str): [optional]  # noqa: E501
            ipo_date (date): [optional]  # noqa: E501
            international_domestic (str): [optional]  # noqa: E501
            sector (str): [optional]  # noqa: E501
            industry (str): [optional]  # noqa: E501
            gic_sector (str): [optional]  # noqa: E501
            gic_group (str): [optional]  # noqa: E501
            gic_industry (str): [optional]  # noqa: E501
            gic_sub_industry (str): [optional]  # noqa: E501
            home_category (str): [optional]  # noqa: E501
            is_delisted (bool): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            address (str): [optional]  # noqa: E501
            address_data (AssetFundamentalsSectionGeneralAddressData): [optional]  # noqa: E501
            listings ([object]): [optional]  # noqa: E501
            officers ([object]): [optional]  # noqa: E501
            phone (str): [optional]  # noqa: E501
            web_url (str): [optional]  # noqa: E501
            logo_url (str): [optional]  # noqa: E501
            full_time_employees (float): [optional]  # noqa: E501
            updated_at (date): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.code = code
        self.type = type
        self.name = name
        self.exchange = exchange
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)