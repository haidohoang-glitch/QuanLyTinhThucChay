# Stored Procedure: `Gen_GetParameter_AdminPermisionHDCN`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 10:00:56.417000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.603000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_AdminPermisionHDCN] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[AdminPermisionHDCN] Where 1=1  and DeletedStatus <> 1) As 'dtStart'	
End

```
