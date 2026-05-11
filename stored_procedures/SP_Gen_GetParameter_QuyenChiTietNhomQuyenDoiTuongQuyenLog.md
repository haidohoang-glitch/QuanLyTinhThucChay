# Stored Procedure: `Gen_GetParameter_QuyenChiTietNhomQuyenDoiTuongQuyenLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:31.193000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.453000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_QuyenChiTietNhomQuyenDoiTuongQuyenLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[QuyenChiTietNhomQuyenDoiTuongQuyenLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
