# Stored Procedure: `Gen_GetParameter_HopDongHanThanhToanLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-24 09:55:14.780000
- **Ngày sửa cuối**: 2016-03-24 09:55:14.780000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_HopDongHanThanhToanLog] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LogTime]),'2010-01-01') from [dbo].[HopDongHanThanhToanLog] Where 1=1 ) As 'NgaySua'	
End
```
