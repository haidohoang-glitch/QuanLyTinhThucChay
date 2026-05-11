# Stored Procedure: `Gen_GetParameter_ThucChay_BoxappCPDByContract`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-01 17:04:51.933000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.627000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_ThucChay_BoxappCPDByContract] 	
As 	
Begin 	
Select 	
(Select Dateadd(day,1,Isnull(Max([NgayThucHien]),'2013-12-31')) from [dbo].[ThucChay] Where 1=1  and typeproduct = -2 and DeletedStatus <> 1) As 'dtStart',	
(Select -2) As '_typeproduct'	
End

```
