# Stored Procedure: `Gen_GetParameter_NhanSuThongTinNhanSuThayThe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:37:33.623000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.607000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_NhanSuThongTinNhanSuThayThe] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[NhanSuThongTinNhanSuThayThe] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
