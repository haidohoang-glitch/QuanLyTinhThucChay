# Stored Procedure: `Gen_GetParameter_DmNhom`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:36:04.693000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.670000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmNhom] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmNhom] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
