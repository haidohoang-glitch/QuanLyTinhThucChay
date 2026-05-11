# Stored Procedure: `Gen_GetParameter_KhachHangNguoiLienHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 14:35:09.593000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.020000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_KhachHangNguoiLienHe] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[KhachHangNguoiLienHe] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
