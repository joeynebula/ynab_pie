# swagger_client.MonthsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_budget_month**](MonthsApi.md#get_budget_month) | **GET** /budgets/{budget_id}/months/{month} | Single budget month
[**get_budget_months**](MonthsApi.md#get_budget_months) | **GET** /budgets/{budget_id}/months | List budget months


# **get_budget_month**
> MonthDetailResponse get_budget_month(budget_id, month)

Single budget month

Returns a single budget month

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MonthsApi(swagger_client.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The ID of the Budget.  \"last-used\" can also be used to specify the last used budget.
month = '2013-10-20' # date | The Budget Month in ISO format (e.g. 2016-12-01).    \"current\" can also be used to specify the current calendar month (UTC).

try:
    # Single budget month
    api_response = api_instance.get_budget_month(budget_id, month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonthsApi->get_budget_month: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**str**](.md)| The ID of the Budget.  \&quot;last-used\&quot; can also be used to specify the last used budget. | 
 **month** | **date**| The Budget Month in ISO format (e.g. 2016-12-01).    \&quot;current\&quot; can also be used to specify the current calendar month (UTC). | 

### Return type

[**MonthDetailResponse**](MonthDetailResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_months**
> MonthSummariesResponse get_budget_months(budget_id)

List budget months

Returns all budget months

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MonthsApi(swagger_client.ApiClient(configuration))
budget_id = 'budget_id_example' # str | The ID of the Budget.  \"last-used\" can also be used to specify the last used budget.

try:
    # List budget months
    api_response = api_instance.get_budget_months(budget_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonthsApi->get_budget_months: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**str**](.md)| The ID of the Budget.  \&quot;last-used\&quot; can also be used to specify the last used budget. | 

### Return type

[**MonthSummariesResponse**](MonthSummariesResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

