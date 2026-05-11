# Stored Procedure: `Gen_GetParameter_ThucChay_Sponsor`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-07 09:43:12.763000
- **Ngày sửa cuối**: 2017-06-07 09:43:12.763000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_GetParameter_ThucChay_Sponsor] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2016-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = 18 and DeletedStatus <> 1) As 'dtStart',	
(Select 18) As '_typeproduct'	
End
```
