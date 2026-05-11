# Stored Procedure: `Gen_GetParameter_ThucChay_ContentNetworkSponsorship`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-16 16:38:31.427000
- **Ngày sửa cuối**: 2017-05-16 16:38:31.427000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThucChay_ContentNetworkSponsorship] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2016-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = 17 and DeletedStatus <> 1) As 'dtStart',	
(Select 17) As '_typeproduct'	
End
```
