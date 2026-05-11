# Stored Procedure: `usp_InsertBooking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-25 18:11:19.410000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.227000

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
| `@DonViTinh` | `int(4)` | No |
| `@SoLuongTheoDV` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   ceo
-- Stored Procedure Name: [dbo].[usp_InsertBooking]
-- Create Date: 25 Tháng Sáu 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertBooking]
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
	@RecordStatus INT,
	@DonViTinh INT,
	@SoLuongTheoDV INT
AS

SET NOCOUNT ON
IF(EXISTS(SELECT * FROM dbo.Booking WHERE BookingID = @BookingID AND HinhThucSP = @HinhThucSP AND MaSanPham = @MaSanPham)) 
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
	RecordStatus = @RecordStatus,
	DonViTinh = @DonViTinh,
	SoLuongTheoDV = @SoLuongTheoDV
WHERE
	[BookingID] = @BookingID AND HinhThucSP = @HinhThucSP AND MaSanPham = @MaSanPham
ELSE

INSERT INTO [dbo].[Booking] (
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
	[LastModifiedAt],
	DeletedStatus,
	PrintStatus,
	RecordStatus,
	DonViTinh,
	SoLuongTheoDV
) VALUES (
	@BookingID,
	@NgayBatDau,
	@NgayKetThuc,
	@Status,
	@SoHopDong,
	@SoLuong,
	@TenWebsite,
	@DmWebsiteREF,
	@HinhThucSP,
	@TenHinhSanPham,
	@MaSanPham,
	@TenSanPham,
	@CreatedBy,
	@CreatedAt,
	@LastModifiedBy,
	@LastModifiedAt,
	@DeletedStatus,
	@PrintStatus,
	@RecordStatus,
	@DonViTinh,
	@SoLuongTheoDV
)

--endregion

```
