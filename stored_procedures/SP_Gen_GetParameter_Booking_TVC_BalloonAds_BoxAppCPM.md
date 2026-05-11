# Stored Procedure: `Gen_GetParameter_Booking_TVC_BalloonAds_BoxAppCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 10:00:54.640000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.167000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_GetParameter_Booking_TVC_BalloonAds_BoxAppCPM] 	
As 	
Begin 	
Select 	
(Select Isnull(Max([LastModifiedAt]),'2014-01-01') from [dbo].[Booking] Where 1=1  and ((HinhThucSP =2 and MaSanPham=8) OR (HinhThucSP =2 and MaSanPham=9))  and DeletedStatus <> 1) As 'pthoigianthuchien'	
End

```
