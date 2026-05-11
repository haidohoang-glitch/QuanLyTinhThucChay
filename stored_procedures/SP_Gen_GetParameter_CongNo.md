# Stored Procedure: `Gen_GetParameter_CongNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 10:00:59.850000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.137000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_CongNo] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[CongNo] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
