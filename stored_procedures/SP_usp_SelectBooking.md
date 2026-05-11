# Stored Procedure: `usp_SelectBooking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-25 18:11:19.607000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.237000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@BookingID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   ceo
-- Stored Procedure Name: [dbo].[usp_SelectBooking]
-- Create Date: 25 Tháng Sáu 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectBooking]
	@BookingID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[BookingID],
	[NgayBatDau],
	[NgayKetThuc],
	[Status],
	[SoHopDong],
	[SoLuong],
	[TenWebsite],
	[DmWebsiteREF],
	[HinhThucSP],
	[TenHinhSanPham],
	[MaSanPham],
	[TenSanPham],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt]
FROM
	[dbo].[Booking]
WHERE
		[BookingID] = @BookingID


--endregion

```
