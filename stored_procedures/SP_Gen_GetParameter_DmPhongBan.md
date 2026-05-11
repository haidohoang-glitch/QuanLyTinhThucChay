# Stored Procedure: `Gen_GetParameter_DmPhongBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:35:59.093000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.560000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_DmPhongBan] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[DmPhongBan] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
