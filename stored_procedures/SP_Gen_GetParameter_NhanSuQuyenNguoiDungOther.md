# Stored Procedure: `Gen_GetParameter_NhanSuQuyenNguoiDungOther`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-04-01 16:49:28.193000
- **Ngày sửa cuối**: 2016-04-01 16:49:28.193000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_NhanSuQuyenNguoiDungOther] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[NhanSuQuyenNguoiDungOther] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End
```
