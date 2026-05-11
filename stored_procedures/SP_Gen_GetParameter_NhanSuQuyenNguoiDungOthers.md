# Stored Procedure: `Gen_GetParameter_NhanSuQuyenNguoiDungOthers`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-12-11 15:52:06.950000
- **Ngày sửa cuối**: 2015-12-11 15:52:06.950000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_NhanSuQuyenNguoiDungOthers] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[NhanSuQuyenNguoiDungOthers] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End
```
