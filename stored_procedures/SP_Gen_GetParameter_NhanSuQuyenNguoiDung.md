# Stored Procedure: `Gen_GetParameter_NhanSuQuyenNguoiDung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:36:06.330000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.777000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_NhanSuQuyenNguoiDung] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[NhanSuQuyenNguoiDung] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
