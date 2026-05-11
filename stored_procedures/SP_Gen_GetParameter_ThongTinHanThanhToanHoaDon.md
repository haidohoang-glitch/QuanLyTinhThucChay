# Stored Procedure: `Gen_GetParameter_ThongTinHanThanhToanHoaDon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:23:46.623000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.340000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThongTinHanThanhToanHoaDon] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2010-01-01') from [dbo].[ThongTinHanThanhToanHoaDon] Where 1=1  and DeletedStatus <> 1) As 'NgaySua'	
End

```
