# Stored Procedure: `Gen_GetParameter_ThucChay_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:50.763000
- **Ngày sửa cuối**: 2017-09-11 15:02:50.780000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChay_Mobile] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2016-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = 10 and DeletedStatus <> 1) As 'dtStart',	
(Select 10) As '_typeproduct'	
End

```
