# Stored Procedure: `usp_InsertKhachHangFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:28.400000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.127000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangID` | `int(4)` | No |
| `@MaKhachHang` | `nvarchar(100)` | No |
| `@TenKhachHang` | `nvarchar(100)` | No |
| `@TenVietTat` | `nvarchar(200)` | No |
| `@TenTiengAnh` | `nvarchar(200)` | No |
| `@IsDaiLy` | `int(4)` | No |
| `@TenChuDoanhNghiep` | `nvarchar(200)` | No |
| `@MaSoThue` | `nvarchar(100)` | No |
| `@MaSoDangKyKinhDoanh` | `nvarchar(100)` | No |
| `@SoCMND` | `nvarchar(100)` | No |
| `@NgayCap` | `datetime(8)` | No |
| `@NoiCap` | `nvarchar(400)` | No |
| `@NgayNhap` | `datetime(8)` | No |
| `@DiaChiTrenHopDong` | `nvarchar(400)` | No |
| `@ChiNhanh` | `int(4)` | No |
| `@ChiNhanh1` | `nvarchar(400)` | No |
| `@ChiNhanh2` | `nvarchar(400)` | No |
| `@Code` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@Loai` | `int(4)` | No |
| `@DienThoai` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |
| `@Email` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertKhachHangFull]
	@KhachHangID int,
	@MaKhachHang nvarchar(50),
	@TenKhachHang nvarchar(50),
	@TenVietTat nvarchar(100),
	@TenTiengAnh nvarchar(100),
	@IsDaiLy int,
	@TenChuDoanhNghiep nvarchar(100),
	@MaSoThue nvarchar(50),
	@MaSoDangKyKinhDoanh nvarchar(50),
	@SoCMND nvarchar(50),
	@NgayCap datetime,
	@NoiCap nvarchar(200),
	@NgayNhap datetime,
	@DiaChiTrenHopDong nvarchar(200),
	@ChiNhanh int,
	@ChiNhanh1 nvarchar(200),
	@ChiNhanh2 nvarchar(200),
	@Code int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int,
	@Loai int,
	@DienThoai nvarchar(50),
	@GhiChu nvarchar(500),
	@Email nvarchar(50)
AS

SET NOCOUNT ON
IF(EXISTS(SELECT * FROM KhachHangFull WHERE KhachHangID = @KhachHangID))
UPDATE [dbo].[KhachHangFull] SET
	[MaKhachHang] = @MaKhachHang,
	[TenKhachHang] = @TenKhachHang,
	[TenVietTat] = @TenVietTat,
	[TenTiengAnh] = @TenTiengAnh,
	[IsDaiLy] = @IsDaiLy,
	[TenChuDoanhNghiep] = @TenChuDoanhNghiep,
	[MaSoThue] = @MaSoThue,
	[MaSoDangKyKinhDoanh] = @MaSoDangKyKinhDoanh,
	[SoCMND] = @SoCMND,
	[NgayCap] = @NgayCap,
	[NoiCap] = @NoiCap,
	[NgayNhap] = @NgayNhap,
	[DiaChiTrenHopDong] = @DiaChiTrenHopDong,
	[ChiNhanh] = @ChiNhanh,
	[ChiNhanh1] = @ChiNhanh1,
	[ChiNhanh2] = @ChiNhanh2,
	[Code] = @Code,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus,
	Loai = @Loai ,
	DienThoai = @DienThoai ,
	GhiChu = @GhiChu ,
	Email = @Email 	
WHERE
	[KhachHangID] = @KhachHangID
else
INSERT INTO [dbo].[KhachHangFull] (
	[KhachHangID],
	[MaKhachHang],
	[TenKhachHang],
	[TenVietTat],
	[TenTiengAnh],
	[IsDaiLy],
	[TenChuDoanhNghiep],
	[MaSoThue],
	[MaSoDangKyKinhDoanh],
	[SoCMND],
	[NgayCap],
	[NoiCap],
	[NgayNhap],
	[DiaChiTrenHopDong],
	[ChiNhanh],
	[ChiNhanh1],
	[ChiNhanh2],
	[Code],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus],
	Loai  ,
	DienThoai ,
	GhiChu  ,
	Email 
) VALUES (
	@KhachHangID,
	@MaKhachHang,
	@TenKhachHang,
	@TenVietTat,
	@TenTiengAnh,
	@IsDaiLy,
	@TenChuDoanhNghiep,
	@MaSoThue,
	@MaSoDangKyKinhDoanh,
	@SoCMND,
	@NgayCap,
	@NoiCap,
	@NgayNhap,
	@DiaChiTrenHopDong,
	@ChiNhanh,
	@ChiNhanh1,
	@ChiNhanh2,
	@Code,
	@CreatedBy,
	@CreatedAt,
	@LastModifiedBy,
	@LastModifiedAt,
	@DeletedStatus,
	@PrintStatus,
	@RecordStatus,
	@Loai ,
	@DienThoai ,
	@GhiChu ,
	@Email 	
)

```
