# Stored Procedure: `Gen_GetParameter_ThucChayDaTinh_TVC_CPV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-06 16:31:03.907000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.733000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChayDaTinh_TVC_CPV] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChayCPV] Where 1=1 ) As '_ngaythuchien'	
End

```
