# Stored Procedure: `Gen_GetParameter_ThucChay_BrandPage`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-08-31 17:01:30.983000
- **Ngày sửa cuối**: 2015-09-12 10:29:11.760000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[Gen_GetParameter_ThucChay_BrandPage] 
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChay_BrandPage] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2014-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = 16 and DeletedStatus <> 1) As 'dtStart',
(SELECT 16) as '_typeproduct'		
End
```
