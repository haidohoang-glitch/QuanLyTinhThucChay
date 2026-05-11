# Stored Procedure: `Gen_GetParameter_KhachhangThongTinTaiKhoan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-26 16:39:37.050000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.917000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_KhachhangThongTinTaiKhoan] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[KhachhangThongTinTaiKhoan] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
