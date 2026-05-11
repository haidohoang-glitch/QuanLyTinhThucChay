# Stored Procedure: `Gen_GetParameter_HopDongLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:14:20.790000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.080000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_HopDongLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[HopDongLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
