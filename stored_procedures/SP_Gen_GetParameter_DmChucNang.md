# Stored Procedure: `Gen_GetParameter_DmChucNang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:15.857000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.073000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmChucNang] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmChucNang] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
