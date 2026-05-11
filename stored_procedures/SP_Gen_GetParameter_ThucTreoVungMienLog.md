# Stored Procedure: `Gen_GetParameter_ThucTreoVungMienLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:27:16.717000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.500000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucTreoVungMienLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThucTreoVungMienLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
