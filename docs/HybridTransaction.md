# HybridTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**date** | **date** |  | 
**amount** | **int** | The transaction amount in milliunits format | 
**cleared** | **str** | The cleared status of the transaction | 
**approved** | **bool** | Whether or not the transaction is approved | 
**account_id** | **str** |  | 
**deleted** | **bool** | Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests. | 
**type** | **str** | Whether the hybrid transaction represents a regular transaction or a subtransaction | 
**account_name** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


