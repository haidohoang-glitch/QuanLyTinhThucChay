# Stored Procedure: `Gen_GetParameter_ThucChayDaTinh_ThucChay_DonViTinh_TrueView`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-19 15:49:17.080000
- **Ngày sửa cuối**: 2017-05-19 15:49:17.080000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThucChayDaTinh_ThucChay_DonViTinh_TrueView] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2016-12-31')) from [dbo].[ThucChayTrueView] Where 1=1 ) As 'dtStart'	
End
```
