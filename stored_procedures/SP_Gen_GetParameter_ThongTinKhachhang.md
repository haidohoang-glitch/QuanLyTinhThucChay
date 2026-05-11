# Stored Procedure: `Gen_GetParameter_ThongTinKhachhang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-16 15:42:59.333000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.260000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThongTinKhachhang] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinKhachhang] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
