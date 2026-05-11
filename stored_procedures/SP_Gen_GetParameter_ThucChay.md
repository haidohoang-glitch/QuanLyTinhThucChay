# Stored Procedure: `Gen_GetParameter_ThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-22 11:29:08.617000
- **Ngày sửa cuối**: 2017-05-22 11:29:08.617000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChay] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChay] Where 1=1   and DeletedStatus <> 1) As 'dtStart'
End

```
