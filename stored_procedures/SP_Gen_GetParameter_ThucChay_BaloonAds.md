# Stored Procedure: `Gen_GetParameter_ThucChay_BaloonAds`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:52:40.913000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.643000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChay_BaloonAds] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = 5 and DeletedStatus <> 1) As 'dtStart',	
(Select 5) As '_typeproduct'	
End

```
