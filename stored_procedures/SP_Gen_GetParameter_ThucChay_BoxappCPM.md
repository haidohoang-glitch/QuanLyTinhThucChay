# Stored Procedure: `Gen_GetParameter_ThucChay_BoxappCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:52:10.730000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.620000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChay_BoxappCPM] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = 9 and DeletedStatus <> 1) As 'dtStart',	
(Select 9) As '_typeproduct'	
End

```
