# Stored Procedure: `Gen_GetParameter_ThucChayDaTinh_KingSize_UV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-08-28 10:53:31.400000
- **Ngày sửa cuối**: 2016-09-16 17:25:31.193000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChayDaTinh_KingSize_UV] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2015-12-31')) from [dbo].[ThucChayCPR] Where 1=1 ) As 'dtStart',	
(SELECT 14) as '_typeproduct'	
End
```
