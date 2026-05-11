# Stored Procedure: `Gen_GetParameter_DiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-15 16:35:20.393000
- **Ngày sửa cuối**: 2015-04-15 16:35:20.393000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_DiaChi] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DiaChi] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End
```
