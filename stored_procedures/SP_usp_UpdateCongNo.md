# Stored Procedure: `usp_UpdateCongNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:01.940000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.007000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@CongNoID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHoaDon` | `int(4)` | No |
| `@NgayXuat` | `datetime(8)` | No |
| `@GiaTri` | `float(8)` | No |
| `@GiaTriThanhToan` | `float(8)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@HanThanhToanID` | `int(4)` | No |
| `@NgayTraHoaDon` | `datetime(8)` | No |
| `@IsSoPhieuThu` | `int(4)` | No |
| `@SoHoaDonGiamTru` | `int(4)` | No |
| `@SoBangThongKe` | `int(4)` | No |
| `@NgayChuyenChoKeToan` | `datetime(8)` | No |
| `@Sign` | `int(4)` | No |
| `@PhieuThuLinkNapTien` | `nvarchar(100)` | No |
| `@TaiKhoanKhachHangREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateCongNo]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateCongNo]
	@CongNoID int,
	@HopDongREF int,
	@SoHoaDon int,
	@NgayXuat datetime,
	@GiaTri float,
	@GiaTriThanhToan float,
	@NgayThanhToan datetime,
	@HanThanhToanID int,
	@NgayTraHoaDon datetime,
	@IsSoPhieuThu int,
	@SoHoaDonGiamTru int,
	@SoBangThongKe int,
	@NgayChuyenChoKeToan datetime,
	@Sign int,
	@PhieuThuLinkNapTien nvarchar(50),
	@TaiKhoanKhachHangREF int,
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[CongNo] SET
	[HopDongREF] = @HopDongREF,
	[SoHoaDon] = @SoHoaDon,
	[NgayXuat] = @NgayXuat,
	[GiaTri] = @GiaTri,
	[GiaTriThanhToan] = @GiaTriThanhToan,
	[NgayThanhToan] = @NgayThanhToan,
	[HanThanhToanID] = @HanThanhToanID,
	[NgayTraHoaDon] = @NgayTraHoaDon,
	[IsSoPhieuThu] = @IsSoPhieuThu,
	[SoHoaDonGiamTru] = @SoHoaDonGiamTru,
	[SoBangThongKe] = @SoBangThongKe,
	[NgayChuyenChoKeToan] = @NgayChuyenChoKeToan,
	[Sign] = @Sign,
	[PhieuThuLinkNapTien] = @PhieuThuLinkNapTien,
	[TaiKhoanKhachHangREF] = @TaiKhoanKhachHangREF,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[CongNoID] = @CongNoID

--endregion

```
