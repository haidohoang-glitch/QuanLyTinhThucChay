# Stored Procedure: `Gen_GetParameter_QuyenChucNangNhomQuyenLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:29.203000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.370000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_QuyenChucNangNhomQuyenLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([ThoiGianLog]),'2010-01-01') from [dbo].[QuyenChucNangNhomQuyenLog] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
