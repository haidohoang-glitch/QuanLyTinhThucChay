# Stored Procedure: `Gen_GetParameter_ThucChayDaTinh_BrandPage_UV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-08-31 17:10:33.037000
- **Ngày sửa cuối**: 2015-09-05 10:55:05.487000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [Gen_GetParameter_ThucChayDaTinh_BrandPage_UV]
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChayDaTinh_BrandPage_UV] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChayCPR] Where 1=1 ) As 'dtStart',
(SELECT 16) as '_typeproduct'	
End

```
