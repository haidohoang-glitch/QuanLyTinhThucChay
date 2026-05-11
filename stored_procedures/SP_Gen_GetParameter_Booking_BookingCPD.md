# Stored Procedure: `Gen_GetParameter_Booking_BookingCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 10:00:42.377000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.600000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_Booking_BookingCPD] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2014-01-01') from [dbo].[Booking] Where 1=1  and MaSanPham = 1 and HinhThucSP = 1 and DeletedStatus <> 1) As 'pthoigianthuchien'	
End

```
