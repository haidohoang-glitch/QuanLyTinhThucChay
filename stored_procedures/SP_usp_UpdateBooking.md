# Stored Procedure: `usp_UpdateBooking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-25 18:11:19.510000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.010000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@BookingID` | `int(4)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@Status` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@SoLuong` | `float(8)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `nvarchar(800)` | No |
| `@HinhThucSP` | `int(4)` | No |
| `@TenHinhSanPham` | `nvarchar(100)` | No |
| `@MaSanPham` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   ceo
-- Stored Procedure Name: [dbo].[usp_UpdateBooking]
-- Create Date: 25 Tháng Sáu 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateBooking]
	@BookingID int,
	@NgayBatDau datetime,
	@NgayKetThuc datetime,
	@Status int,
	@SoHopDong nvarchar(50),
	@SoLuong float,
	@TenWebsite nvarchar(100),
	@DmWebsiteREF nvarchar(400),
	@HinhThucSP int,
	@TenHinhSanPham nvarchar(50),
	@MaSanPham int,
	@TenSanPham nvarchar(100),
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT 
AS

SET NOCOUNT ON

UPDATE [dbo].[Booking] SET
	[NgayBatDau] = @NgayBatDau,
	[NgayKetThuc] = @NgayKetThuc,
	[Status] = @Status,
	[SoHopDong] = @SoHopDong,
	[SoLuong] = @SoLuong,
	[TenWebsite] = @TenWebsite,
	[DmWebsiteREF] = @DmWebsiteREF,
	[HinhThucSP] = @HinhThucSP,
	[TenHinhSanPham] = @TenHinhSanPham,
	[MaSanPham] = @MaSanPham,
	[TenSanPham] = @TenSanPham,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	DeletedStatus = @DeletedStatus,
	PrintStatus = @PrintStatus,
	RecordStatus = @RecordStatus
WHERE
	[BookingID] = @BookingID

--endregion

```
