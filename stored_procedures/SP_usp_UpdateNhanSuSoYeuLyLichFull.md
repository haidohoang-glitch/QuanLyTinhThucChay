# Stored Procedure: `usp_UpdateNhanSuSoYeuLyLichFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:29.993000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.590000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |
| `@MaNhanSu` | `nvarchar(100)` | No |
| `@HoVaTen` | `nvarchar(400)` | No |
| `@BiDanh` | `nvarchar(100)` | No |
| `@NgaySinh` | `datetime(8)` | No |
| `@NoiSinh` | `nvarchar(400)` | No |
| `@GioiTinh` | `int(4)` | No |
| `@SoCMT` | `nvarchar(100)` | No |
| `@CapTai` | `nvarchar(400)` | No |
| `@NgayCap` | `datetime(8)` | No |
| `@NguyenQuan` | `nvarchar(400)` | No |
| `@HoKhauThuongTru` | `nvarchar(400)` | No |
| `@NoiOHienNay` | `nvarchar(400)` | No |
| `@DanToc` | `nvarchar(100)` | No |
| `@TonGiao` | `nvarchar(100)` | No |
| `@TrinhDoVanHoa` | `nvarchar(100)` | No |
| `@NgoaiNgu` | `nvarchar(100)` | No |
| `@QuaTrinhBanThan` | `nvarchar(400)` | No |
| `@BanMem` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Email` | `nvarchar(100)` | No |
| `@DienThoai` | `nvarchar(100)` | No |
| `@DienThoai1` | `nvarchar(100)` | No |
| `@DienThoai2` | `nvarchar(2)` | No |
| `@Code` | `nvarchar(2)` | No |
| `@NgayNghiViec` | `datetime(8)` | No |
| `@NgayBatDauLamViec` | `datetime(8)` | No |
| `@ImageFIleName` | `nvarchar(2)` | No |
| `@ImageFIleNameEncode` | `nvarchar(2)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuSoYeuLyLichFull]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateNhanSuSoYeuLyLichFull]
	@NhanSuSoYeuLyLichID int,
	@MaNhanSu nvarchar(50),
	@HoVaTen nvarchar(200),
	@BiDanh nvarchar(50),
	@NgaySinh datetime,
	@NoiSinh nvarchar(200),
	@GioiTinh int,
	@SoCMT nvarchar(50),
	@CapTai nvarchar(200),
	@NgayCap datetime,
	@NguyenQuan nvarchar(200),
	@HoKhauThuongTru nvarchar(200),
	@NoiOHienNay nvarchar(200),
	@DanToc nvarchar(50),
	@TonGiao nvarchar(50),
	@TrinhDoVanHoa nvarchar(50),
	@NgoaiNgu nvarchar(50),
	@QuaTrinhBanThan nvarchar(200),
	@BanMem nvarchar(200),
	@GhiChu nvarchar(200),
	@Email nvarchar(50),
	@DienThoai nvarchar(50),
	@DienThoai1 nvarchar(50),
	@DienThoai2 nvarchar(1),
	@Code nvarchar(1),
	@NgayNghiViec datetime,
	@NgayBatDauLamViec datetime,
	@ImageFIleName nvarchar(1),
	@ImageFIleNameEncode nvarchar(1),
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[NhanSuSoYeuLyLichFull] SET
	[MaNhanSu] = @MaNhanSu,
	[HoVaTen] = @HoVaTen,
	[BiDanh] = @BiDanh,
	[NgaySinh] = @NgaySinh,
	[NoiSinh] = @NoiSinh,
	[GioiTinh] = @GioiTinh,
	[SoCMT] = @SoCMT,
	[CapTai] = @CapTai,
	[NgayCap] = @NgayCap,
	[NguyenQuan] = @NguyenQuan,
	[HoKhauThuongTru] = @HoKhauThuongTru,
	[NoiOHienNay] = @NoiOHienNay,
	[DanToc] = @DanToc,
	[TonGiao] = @TonGiao,
	[TrinhDoVanHoa] = @TrinhDoVanHoa,
	[NgoaiNgu] = @NgoaiNgu,
	[QuaTrinhBanThan] = @QuaTrinhBanThan,
	[BanMem] = @BanMem,
	[GhiChu] = @GhiChu,
	[Email] = @Email,
	[DienThoai] = @DienThoai,
	[DienThoai1] = @DienThoai1,
	[DienThoai2] = @DienThoai2,
	[Code] = @Code,
	[NgayNghiViec] = @NgayNghiViec,
	[NgayBatDauLamViec] = @NgayBatDauLamViec,
	[ImageFIleName] = @ImageFIleName,
	[ImageFIleNameEncode] = @ImageFIleNameEncode,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[NhanSuSoYeuLyLichID] = @NhanSuSoYeuLyLichID

--endregion

```
