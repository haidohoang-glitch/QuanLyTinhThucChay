# Stored Procedure: `Gen_GetParameter_ThucChay_BannerCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:54:08.020000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.640000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChay_BannerCPD] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = 1 and DeletedStatus <> 1) As 'dtStart',	
(Select 1) As '_typeproduct'	
End

```
