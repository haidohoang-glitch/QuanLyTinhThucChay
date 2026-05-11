# Stored Procedure: `Gen_InsertOrUpdate_HopDongLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:14:20.507000
- **Ngày sửa cuối**: 2017-04-05 14:13:55.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongLogID` | `bigint(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmMaHopDongREF` | `bigint(8)` | No |
| `@TenMaHopDong` | `nvarchar(400)` | No |
| `@SO` | `nvarchar(400)` | No |
| `@Thang` | `nvarchar(400)` | No |
| `@Nam` | `nvarchar(400)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@NhanHopDong` | `nvarchar(400)` | No |
| `@GiaTriHopDong` | `float(8)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@ThucHienDenNgayThucChay` | `datetime(8)` | No |
| `@ThanhTienThucChay` | `bigint(8)` | No |
| `@ThucHienDenNgayHoaDon` | `datetime(8)` | No |
| `@ThanhTienHoaDon` | `bigint(8)` | No |
| `@ThucHienDenNgayCongNo` | `datetime(8)` | No |
| `@ThanhTienCongNo` | `bigint(8)` | No |
| `@NgayChuyenHopDongChoKeToan` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@NgayNhanHopDongBanCung` | `datetime(8)` | No |
| `@DmKhachHangREF` | `bigint(8)` | No |
| `@TenKhachHang` | `nvarchar(400)` | No |
| `@SysNhanVienREF` | `bigint(8)` | No |
| `@TenDangNhap` | `nvarchar(400)` | No |
| `@TenNhanVien` | `nvarchar(400)` | No |
| `@NgayDanhSoHopDong` | `datetime(8)` | No |
| `@NganhHang` | `nvarchar(400)` | No |
| `@DmNhomREF` | `bigint(8)` | No |
| `@TrangThaiHopDong` | `int(4)` | No |
| `@IsBanCung` | `int(4)` | No |
| `@CongNo` | `int(4)` | No |
| `@GhiChuHopDong` | `nvarchar(400)` | No |
| `@NgayNhanBanFax` | `datetime(8)` | No |
| `@LyDoHuyHopDong` | `nvarchar(400)` | No |
| `@DangSuDung` | `int(4)` | No |
| `@IsGiayPhep` | `int(4)` | No |
| `@DmPhongBanREF` | `bigint(8)` | No |
| `@TenPhongBan` | `nvarchar(400)` | No |
| `@DmBoPhanREF` | `bigint(8)` | No |
| `@TenBoPhan` | `nvarchar(400)` | No |
| `@DmNhomLamViecREF` | `bigint(8)` | No |
| `@TenNhom` | `nvarchar(400)` | No |
| `@DmDiaDiemLamViecREF` | `bigint(8)` | No |
| `@TenDiaDiemLamViec` | `nvarchar(400)` | No |
| `@ChuyenTrang` | `int(4)` | No |
| `@IsUuDai` | `int(4)` | No |
| `@ThoiGianLog` | `datetime(8)` | No |
| `@NguoiLog` | `nvarchar(400)` | No |
| `@LoaiLog` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongLog] 	
@HopDongLogID bigint ,	
@HopDongID int ,	
@DmMaHopDongREF bigint ,	
@TenMaHopDong nvarchar (200) ,	
@SO nvarchar (200) ,	
@Thang nvarchar (200) ,	
@Nam nvarchar (200) ,	
@NgayKyHopDong datetime ,	
@NhanHopDong nvarchar (200) ,	
@GiaTriHopDong float ,	
@SoHopDong nvarchar (200) ,	
@ThucHienDenNgayThucChay datetime ,	
@ThanhTienThucChay bigint ,	
@ThucHienDenNgayHoaDon datetime ,	
@ThanhTienHoaDon bigint ,	
@ThucHienDenNgayCongNo datetime ,	
@ThanhTienCongNo bigint ,	
@NgayChuyenHopDongChoKeToan datetime ,	
@GhiChu nvarchar (200) ,	
@NgayNhanHopDongBanCung datetime ,	
@DmKhachHangREF bigint ,	
@TenKhachHang nvarchar (200) ,	
@SysNhanVienREF bigint ,	
@TenDangNhap nvarchar (200) ,	
@TenNhanVien nvarchar (200) ,	
@NgayDanhSoHopDong datetime ,	
@NganhHang nvarchar (200) ,	
@DmNhomREF bigint ,	
@TrangThaiHopDong int ,	
@IsBanCung int ,	
@CongNo int ,	
@GhiChuHopDong nvarchar (200) ,	
@NgayNhanBanFax datetime ,	
@LyDoHuyHopDong nvarchar (200) ,	
@DangSuDung int ,	
@IsGiayPhep int ,	
@DmPhongBanREF bigint ,	
@TenPhongBan nvarchar (200) ,	
@DmBoPhanREF bigint ,	
@TenBoPhan nvarchar (200) ,	
@DmNhomLamViecREF bigint ,	
@TenNhom nvarchar (200) ,	
@DmDiaDiemLamViecREF bigint ,	
@TenDiaDiemLamViec nvarchar (200) ,	
@ChuyenTrang int ,	
@IsUuDai int ,	
@ThoiGianLog datetime ,	
@NguoiLog nvarchar (200) ,	
@LoaiLog int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
BEGIN
	PRINT 'KHONG SU DUNG NUA'
	--if(exists(select * from [HopDongLog] where [HopDongLogID] = @HopDongLogID))	
	--UPDATE [dbo].[HopDongLog] SET 	
	--[HopDongID] = @HopDongID,	
	--[DmMaHopDongREF] = @DmMaHopDongREF,	
	--[TenMaHopDong] = @TenMaHopDong,	
	--[SO] = @SO,	
	--[Thang] = @Thang,	
	--[Nam] = @Nam,	
	--[NgayKyHopDong] = @NgayKyHopDong,	
	--[NhanHopDong] = @NhanHopDong,	
	--[GiaTriHopDong] = @GiaTriHopDong,	
	--[SoHopDong] = @SoHopDong,	
	--[ThucHienDenNgayThucChay] = @ThucHienDenNgayThucChay,	
	--[ThanhTienThucChay] = @ThanhTienThucChay,	
	--[ThucHienDenNgayHoaDon] = @ThucHienDenNgayHoaDon,	
	--[ThanhTienHoaDon] = @ThanhTienHoaDon,	
	--[ThucHienDenNgayCongNo] = @ThucHienDenNgayCongNo,	
	--[ThanhTienCongNo] = @ThanhTienCongNo,	
	--[NgayChuyenHopDongChoKeToan] = @NgayChuyenHopDongChoKeToan,	
	--[GhiChu] = @GhiChu,	
	--[NgayNhanHopDongBanCung] = @NgayNhanHopDongBanCung,	
	--[DmKhachHangREF] = @DmKhachHangREF,	
	--[TenKhachHang] = @TenKhachHang,	
	--[SysNhanVienREF] = @SysNhanVienREF,	
	--[TenDangNhap] = @TenDangNhap,	
	--[TenNhanVien] = @TenNhanVien,	
	--[NgayDanhSoHopDong] = @NgayDanhSoHopDong,	
	--[NganhHang] = @NganhHang,	
	--[DmNhomREF] = @DmNhomREF,	
	--[TrangThaiHopDong] = @TrangThaiHopDong,	
	--[IsBanCung] = @IsBanCung,	
	--[CongNo] = @CongNo,	
	--[GhiChuHopDong] = @GhiChuHopDong,	
	--[NgayNhanBanFax] = @NgayNhanBanFax,	
	--[LyDoHuyHopDong] = @LyDoHuyHopDong,	
	--[DangSuDung] = @DangSuDung,	
	--[IsGiayPhep] = @IsGiayPhep,	
	--[DmPhongBanREF] = @DmPhongBanREF,	
	--[TenPhongBan] = @TenPhongBan,	
	--[DmBoPhanREF] = @DmBoPhanREF,	
	--[TenBoPhan] = @TenBoPhan,	
	--[DmNhomLamViecREF] = @DmNhomLamViecREF,	
	--[TenNhom] = @TenNhom,	
	--[DmDiaDiemLamViecREF] = @DmDiaDiemLamViecREF,	
	--[TenDiaDiemLamViec] = @TenDiaDiemLamViec,	
	--[ChuyenTrang] = @ChuyenTrang,	
	--[IsUuDai] = @IsUuDai,	
	--[ThoiGianLog] = @ThoiGianLog,	
	--[NguoiLog] = @NguoiLog,	
	--[LoaiLog] = @LoaiLog,	
	--[CreatedBy] = @CreatedBy,	
	--[CreatedAt] = @CreatedAt,	
	--[LastModifiedBy] = @LastModifiedBy,	
	--[LastModifiedAt] = @LastModifiedAt,	
	--[DeletedStatus] = @DeletedStatus,	
	--[PrintStatus] = @PrintStatus,	
	--[RecordStatus] = @RecordStatus where [HopDongLogID] = @HopDongLogID	
	--else 	
	--INSERT INTO [dbo].[HopDongLog] (	
	--[HopDongLogID],	
	--[HopDongID],	
	--[DmMaHopDongREF],	
	--[TenMaHopDong],	
	--[SO],	
	--[Thang],	
	--[Nam],	
	--[NgayKyHopDong],	
	--[NhanHopDong],	
	--[GiaTriHopDong],	
	--[SoHopDong],	
	--[ThucHienDenNgayThucChay],	
	--[ThanhTienThucChay],	
	--[ThucHienDenNgayHoaDon],	
	--[ThanhTienHoaDon],	
	--[ThucHienDenNgayCongNo],	
	--[ThanhTienCongNo],	
	--[NgayChuyenHopDongChoKeToan],	
	--[GhiChu],	
	--[NgayNhanHopDongBanCung],	
	--[DmKhachHangREF],	
	--[TenKhachHang],	
	--[SysNhanVienREF],	
	--[TenDangNhap],	
	--[TenNhanVien],	
	--[NgayDanhSoHopDong],	
	--[NganhHang],	
	--[DmNhomREF],	
	--[TrangThaiHopDong],	
	--[IsBanCung],	
	--[CongNo],	
	--[GhiChuHopDong],	
	--[NgayNhanBanFax],	
	--[LyDoHuyHopDong],	
	--[DangSuDung],	
	--[IsGiayPhep],	
	--[DmPhongBanREF],	
	--[TenPhongBan],	
	--[DmBoPhanREF],	
	--[TenBoPhan],	
	--[DmNhomLamViecREF],	
	--[TenNhom],	
	--[DmDiaDiemLamViecREF],	
	--[TenDiaDiemLamViec],	
	--[ChuyenTrang],	
	--[IsUuDai],	
	--[ThoiGianLog],	
	--[NguoiLog],	
	--[LoaiLog],	
	--[CreatedBy],	
	--[CreatedAt],	
	--[LastModifiedBy],	
	--[LastModifiedAt],	
	--[DeletedStatus],	
	--[PrintStatus],	
	--[RecordStatus])	
	--Values 	
	--(	
	--@HopDongLogID,	
	--@HopDongID,	
	--@DmMaHopDongREF,	
	--@TenMaHopDong,	
	--@SO,	
	--@Thang,	
	--@Nam,	
	--@NgayKyHopDong,	
	--@NhanHopDong,	
	--@GiaTriHopDong,	
	--@SoHopDong,	
	--@ThucHienDenNgayThucChay,	
	--@ThanhTienThucChay,	
	--@ThucHienDenNgayHoaDon,	
	--@ThanhTienHoaDon,	
	--@ThucHienDenNgayCongNo,	
	--@ThanhTienCongNo,	
	--@NgayChuyenHopDongChoKeToan,	
	--@GhiChu,	
	--@NgayNhanHopDongBanCung,	
	--@DmKhachHangREF,	
	--@TenKhachHang,	
	--@SysNhanVienREF,	
	--@TenDangNhap,	
	--@TenNhanVien,	
	--@NgayDanhSoHopDong,	
	--@NganhHang,	
	--@DmNhomREF,	
	--@TrangThaiHopDong,	
	--@IsBanCung,	
	--@CongNo,	
	--@GhiChuHopDong,	
	--@NgayNhanBanFax,	
	--@LyDoHuyHopDong,	
	--@DangSuDung,	
	--@IsGiayPhep,	
	--@DmPhongBanREF,	
	--@TenPhongBan,	
	--@DmBoPhanREF,	
	--@TenBoPhan,	
	--@DmNhomLamViecREF,	
	--@TenNhom,	
	--@DmDiaDiemLamViecREF,	
	--@TenDiaDiemLamViec,	
	--@ChuyenTrang,	
	--@IsUuDai,	
	--@ThoiGianLog,	
	--@NguoiLog,	
	--@LoaiLog,	
	--@CreatedBy,	
	--@CreatedAt,	
	--@LastModifiedBy,	
	--@LastModifiedAt,	
	--@DeletedStatus,	
	--@PrintStatus,	
	--@RecordStatus)
END
```
