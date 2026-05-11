# Stored Procedure: `Gen_GetParameter_QuyenChiTietNhomQuyenDoiTuongQuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:25.417000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.483000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_QuyenChiTietNhomQuyenDoiTuongQuyen] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[QuyenChiTietNhomQuyenDoiTuongQuyen] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
