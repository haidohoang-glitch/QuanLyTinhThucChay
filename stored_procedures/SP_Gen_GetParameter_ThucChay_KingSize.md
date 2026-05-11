# Stored Procedure: `Gen_GetParameter_ThucChay_KingSize`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-03 10:52:18.270000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.607000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChay_KingSize] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = 14 and DeletedStatus <> 1) As 'dtStart',	
(Select 14) As '_typeproduct'	
End

```
