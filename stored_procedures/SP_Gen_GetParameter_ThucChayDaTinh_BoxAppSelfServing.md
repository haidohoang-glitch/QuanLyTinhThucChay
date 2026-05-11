# Stored Procedure: `Gen_GetParameter_ThucChayDaTinh_BoxAppSelfServing`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 14:16:13.170000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.777000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChayDaTinh_BoxAppSelfServing] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChayDaTinhBoxAppSSV] Where 1=1 ) As 'dtStart'	
End

```
