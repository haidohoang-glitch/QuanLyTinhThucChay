# Stored Procedure: `Gen_GetParameter_ThucChayDaTinh_SponsorPage_UV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-29 16:16:21.880000
- **Ngày sửa cuối**: 2017-08-29 16:16:21.880000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThucChayDaTinh_SponsorPage_UV] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2016-12-31')) from [dbo].[ThucChayCPR] Where 1=1 ) As 'dtStart',	
(Select Isnull(Max([TypeProduct]),0) + 1 from [dbo].[ThucChayCPR] Where 1=1 ) As '_typeproduct'	
End
```
