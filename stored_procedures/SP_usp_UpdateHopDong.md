# Stored Procedure: `usp_UpdateHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:09:09.170000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.127000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |
| `@TenMaHopDong` | `nvarchar(100)` | No |
| `@So` | `int(4)` | No |
| `@Thang` | `int(4)` | No |
| `@Nam` | `int(4)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@NhanHopDong` | `datetime(8)` | No |
| `@GiaTriHopDong` | `float(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayChuyenHopDongChoKeToan` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(600)` | No |
| `@NgayNhanHopDongBanCung` | `datetime(8)` | No |
| `@DmKhachHangREF` | `int(4)` | No |
| `@TenKhachHang` | `nvarchar(510)` | No |
| `@SysNhanVienREF` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(50)` | No |
| `@TenNhanVien` | `nvarchar(200)` | No |
| `@NgayDanhSoHopDong` | `datetime(8)` | No |
| `@NganhHang` | `nvarchar(100)` | No |
| `@DmNhomREF` | `int(4)` | No |
| `@TrangThaiHopDong` | `int(4)` | No |
| `@IsBanCung` | `int(4)` | No |
| `@CongNo` | `float(8)` | No |
| `@GhiChuHopDong` | `nvarchar(8000)` | No |
| `@NgayNhanBanFax` | `datetime(8)` | No |
| `@LyDoHuyHopDong` | `nvarchar(8000)` | No |
| `@DangSuDung` | `int(4)` | No |
| `@IsGiayPhep` | `int(4)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@TenPhongBan` | `nvarchar(100)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@TenBoPhan` | `nvarchar(100)` | No |
| `@DmNhomLamViecREF` | `int(4)` | No |
| `@TenNhom` | `nvarchar(100)` | No |
| `@DmDiaDiemLamViecREF` | `int(4)` | No |
| `@TenDiaDiemLamViec` | `nvarchar(100)` | No |
| `@ChuyenTrang` | `int(4)` | No |
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
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_UpdateHopDong]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateHopDong]
	@HopDongID int,
	@DmMaHopDongREF int,
	@TenMaHopDong nvarchar(50),
	@So int,
	@Thang int,
	@Nam int,
	@NgayKyHopDong datetime,
	@NhanHopDong datetime,
	@GiaTriHopDong float,
	@SoHopDong nvarchar(50),
	@NgayChuyenHopDongChoKeToan datetime,
	@GhiChu nvarchar(300),
	@NgayNhanHopDongBanCung datetime,
	@DmKhachHangREF int,
	@TenKhachHang nvarchar(255),
	@SysNhanVienREF int,
	@TenDangNhap nvarchar(25),
	@TenNhanVien nvarchar(100),
	@NgayDanhSoHopDong datetime,
	@NganhHang nvarchar(50),
	@DmNhomREF int,
	@TrangThaiHopDong int,
	@IsBanCung int,
	@CongNo float,
	@GhiChuHopDong nvarchar(4000),
	@NgayNhanBanFax datetime,
	@LyDoHuyHopDong nvarchar(4000),
	@DangSuDung int,
	@IsGiayPhep int,
	@DmPhongBanREF int,
	@TenPhongBan nvarchar(50),
	@DmBoPhanREF int,
	@TenBoPhan nvarchar(50),
	@DmNhomLamViecREF int,
	@TenNhom nvarchar(50),
	@DmDiaDiemLamViecREF int,
	@TenDiaDiemLamViec nvarchar(50),
	@ChuyenTrang int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[HopDong] SET
	[DmMaHopDongREF] = @DmMaHopDongREF,
	[TenMaHopDong] = @TenMaHopDong,
	[So] = @So,
	[Thang] = @Thang,
	[Nam] = @Nam,
	[NgayKyHopDong] = @NgayKyHopDong,
	[NhanHopDong] = @NhanHopDong,
	[GiaTriHopDong] = @GiaTriHopDong,
	[SoHopDong] = @SoHopDong,
	[NgayChuyenHopDongChoKeToan] = @NgayChuyenHopDongChoKeToan,
	[GhiChu] = @GhiChu,
	[NgayNhanHopDongBanCung] = @NgayNhanHopDongBanCung,
	[DmKhachHangREF] = @DmKhachHangREF,
	[TenKhachHang] = @TenKhachHang,
	[SysNhanVienREF] = @SysNhanVienREF,
	[TenDangNhap] = @TenDangNhap,
	[TenNhanVien] = @TenNhanVien,
	[NgayDanhSoHopDong] = @NgayDanhSoHopDong,
	[NganhHang] = @NganhHang,
	[DmNhomREF] = @DmNhomREF,
	[TrangThaiHopDong] = @TrangThaiHopDong,
	[IsBanCung] = @IsBanCung,
	[CongNo] = @CongNo,
	[GhiChuHopDong] = @GhiChuHopDong,
	[NgayNhanBanFax] = @NgayNhanBanFax,
	[LyDoHuyHopDong] = @LyDoHuyHopDong,
	[DangSuDung] = @DangSuDung,
	[IsGiayPhep] = @IsGiayPhep,
	[DmPhongBanREF] = @DmPhongBanREF,
	[TenPhongBan] = @TenPhongBan,
	[DmBoPhanREF] = @DmBoPhanREF,
	[TenBoPhan] = @TenBoPhan,
	[DmNhomLamViecREF] = @DmNhomLamViecREF,
	[TenNhom] = @TenNhom,
	[DmDiaDiemLamViecREF] = @DmDiaDiemLamViecREF,
	[TenDiaDiemLamViec] = @TenDiaDiemLamViec,
	[ChuyenTrang] = @ChuyenTrang,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[HopDongID] = @HopDongID

```
