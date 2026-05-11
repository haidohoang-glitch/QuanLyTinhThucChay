# Stored Procedure: `Gen_GetParameter_HopDongChiTietLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:33:52.240000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.170000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_HopDongChiTietLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[HopDongChiTietLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
