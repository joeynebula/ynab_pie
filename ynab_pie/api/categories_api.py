# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ynab_pie.api_client import ApiClient


class CategoriesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_categories(self, budget_id, **kwargs):  # noqa: E501
        """List categories  # noqa: E501

        Returns all categories grouped by category group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.get_categories(budget_id, async_=True)
        >>> result = thread.get()

        :param async bool
        :param str budget_id: The ID of the Budget.  \"last-used\" can also be used to specify the last used budget. (required)
        :return: CategoriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_categories_with_http_info(budget_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_categories_with_http_info(budget_id, **kwargs)  # noqa: E501
            return data

    def get_categories_with_http_info(self, budget_id, **kwargs):  # noqa: E501
        """List categories  # noqa: E501

        Returns all categories grouped by category group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.get_categories_with_http_info(budget_id, async_=True)
        >>> result = thread.get()

        :param async bool
        :param str budget_id: The ID of the Budget.  \"last-used\" can also be used to specify the last used budget. (required)
        :return: CategoriesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_categories" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if ('budget_id' not in params or
                params['budget_id'] is None):
            raise ValueError("Missing the required parameter `budget_id` when calling `get_categories`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CategoriesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_category_by_id(self, budget_id, category_id, **kwargs):  # noqa: E501
        """Single category  # noqa: E501

        Returns a single category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.get_category_by_id(budget_id, category_id, async_=True)
        >>> result = thread.get()

        :param async bool
        :param str budget_id: The ID of the Budget.  \"last-used\" can also be used to specify the last used budget. (required)
        :param str category_id: The ID of the Category. (required)
        :return: CategoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_category_by_id_with_http_info(budget_id, category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_category_by_id_with_http_info(budget_id, category_id, **kwargs)  # noqa: E501
            return data

    def get_category_by_id_with_http_info(self, budget_id, category_id, **kwargs):  # noqa: E501
        """Single category  # noqa: E501

        Returns a single category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.get_category_by_id_with_http_info(budget_id, category_id, async_=True)
        >>> result = thread.get()

        :param async bool
        :param str budget_id: The ID of the Budget.  \"last-used\" can also be used to specify the last used budget. (required)
        :param str category_id: The ID of the Category. (required)
        :return: CategoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id', 'category_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_category_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if ('budget_id' not in params or
                params['budget_id'] is None):
            raise ValueError("Missing the required parameter `budget_id` when calling `get_category_by_id`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_category_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/categories/{category_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CategoryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
