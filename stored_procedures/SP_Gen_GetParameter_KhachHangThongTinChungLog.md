# Stored Procedure: `Gen_GetParameter_KhachHangThongTinChungLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-26 16:35:46.440000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.947000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_KhachHangThongTinChungLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[KhachHangThongTinChungLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
