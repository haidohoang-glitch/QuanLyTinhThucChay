# Stored Procedure: `Gen_GetParameter_NhanSuQuyenNguoiDungLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:37:35.700000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.740000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_NhanSuQuyenNguoiDungLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[NhanSuQuyenNguoiDungLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
