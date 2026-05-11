# Stored Procedure: `Gen_InsertOrUpdate_HopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:36:33.413000
- **Ngày sửa cuối**: 2017-03-11 10:45:44.850000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `bigint(8)` | No |
| `@DmMaHopDongREF` | `bigint(8)` | No |
| `@TenMaHopDong` | `nvarchar(400)` | No |
| `@SO` | `nvarchar(400)` | No |
| `@Thang` | `nvarchar(400)` | No |
| `@Nam` | `nvarchar(400)` | No |
| `@NgayKyHopDong` | `nvarchar(400)` | No |
| `@NhanHopDong` | `nvarchar(400)` | No |
| `@GiaTriHopDong` | `float(8)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@ThucHienDenNgayThucChay` | `datetime(8)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@ThucHienDenNgayHoaDon` | `datetime(8)` | No |
| `@ThanhTienHoaDon` | `bigint(8)` | No |
| `@ThucHienDenNgayCongNo` | `datetime(8)` | No |
| `@ThanhTienThanhToan` | `bigint(8)` | No |
| `@ThanhTienCongNo` | `float(8)` | No |
| `@NgayChuyenHopDongChoKeToan` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@NgayNhanHopDongBanCung` | `datetime(8)` | No |
| `@DmKhachHangREF` | `bigint(8)` | No |
| `@TenKhachHang` | `nvarchar(400)` | No |
| `@DmHinhThucKhachHangREF` | `int(4)` | No |
| `@TenHinhThucKhachHang` | `nvarchar(200)` | No |
| `@DmLoaiKhachHangREF` | `int(4)` | No |
| `@TenLoaiKhachHang` | `nvarchar(200)` | No |
| `@SysNhanVienREF` | `bigint(8)` | No |
| `@TenDangNhap` | `nvarchar(400)` | No |
| `@TenNhanVien` | `nvarchar(400)` | No |
| `@NgayDanhSoHopDong` | `datetime(8)` | No |
| `@NganhHang` | `nvarchar(400)` | No |
| `@DmNhomREF` | `bigint(8)` | No |
| `@TrangThaiHopDong` | `int(4)` | No |
| `@IsBanCung` | `int(4)` | No |
| `@CongNo` | `float(8)` | No |
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
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@NgayHuyHopDong` | `datetime(8)` | No |
| `@NguoiHuyHopDong` | `nvarchar(200)` | No |
| `@IsCalcVoucher` | `int(4)` | No |
| `@GiaTriDatCoc` | `bigint(8)` | No |
| `@NgayDatCoc` | `datetime(8)` | No |
| `@NgayGiaHanDatCoc` | `datetime(8)` | No |
| `@TenNhanGoc` | `nvarchar(400)` | No |
| `@DmNhanGocREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDong]
	@HopDongID BIGINT ,
	@DmMaHopDongREF BIGINT ,
	@TenMaHopDong NVARCHAR(200) ,
	@SO NVARCHAR(200) ,
	@Thang NVARCHAR(200) ,
	@Nam NVARCHAR(200) ,
	@NgayKyHopDong NVARCHAR(200) ,
	@NhanHopDong NVARCHAR(200) ,
	@GiaTriHopDong FLOAT ,
	@SoHopDong NVARCHAR(200) ,
	@ThucHienDenNgayThucChay DATETIME ,
	@ThanhTienThucChay FLOAT ,
	@ThucHienDenNgayHoaDon DATETIME ,
	@ThanhTienHoaDon BIGINT ,
	@ThucHienDenNgayCongNo DATETIME ,
	@ThanhTienThanhToan BIGINT ,
	@ThanhTienCongNo FLOAT ,
	@NgayChuyenHopDongChoKeToan DATETIME ,
	@GhiChu NVARCHAR(200) ,
	@NgayNhanHopDongBanCung DATETIME ,
	@DmKhachHangREF BIGINT ,
	@TenKhachHang NVARCHAR(200) ,
	@DmHinhThucKhachHangREF INT,
	@TenHinhThucKhachHang NVARCHAR(100),
	@DmLoaiKhachHangREF INT,
	@TenLoaiKhachHang NVARCHAR(100),
	@SysNhanVienREF BIGINT ,
	@TenDangNhap NVARCHAR(200) ,
	@TenNhanVien NVARCHAR(200) ,
	@NgayDanhSoHopDong DATETIME ,
	@NganhHang NVARCHAR(200) ,
	@DmNhomREF BIGINT ,
	@TrangThaiHopDong INT ,
	@IsBanCung INT ,
	@CongNo FLOAT ,
	@GhiChuHopDong NVARCHAR(200) ,
	@NgayNhanBanFax DATETIME ,
	@LyDoHuyHopDong NVARCHAR(200) ,
	@DangSuDung INT ,
	@IsGiayPhep INT ,
	@DmPhongBanREF BIGINT ,
	@TenPhongBan NVARCHAR(200) ,
	@DmBoPhanREF BIGINT ,
	@TenBoPhan NVARCHAR(200) ,
	@DmNhomLamViecREF BIGINT ,
	@TenNhom NVARCHAR(200) ,
	@DmDiaDiemLamViecREF BIGINT ,
	@TenDiaDiemLamViec NVARCHAR(200) ,
	@ChuyenTrang INT ,
	@IsUuDai INT ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT,
	@NgayHuyHopDong DATETIME,
	@NguoiHuyHopDong NVARCHAR(100),
	@IsCalcVoucher INT,
	@GiaTriDatCoc BIGINT,
	@NgayDatCoc DATETIME,
	@NgayGiaHanDatCoc DATETIME,
	@TenNhanGoc NVARCHAR(200),
	@DmNhanGocREF INT
	
AS
BEGIN
	SET @NhanHopDong = [dbo].[ReplaceNhanHangDoubleNhay](@NhanHopDong)
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [HopDong]
	           WHERE  [HopDongID] = @HopDongID
	       )
	   )
	    UPDATE [dbo].[HopDong]
	    SET    [DmMaHopDongREF]              = @DmMaHopDongREF,
	           [TenMaHopDong]                = @TenMaHopDong,
	           [SO]                          = @SO,
	           [Thang]                       = @Thang,
	           [Nam]                         = @Nam,
	           [NgayKyHopDong]               = @NgayKyHopDong,
	           [NhanHopDong]                 = @NhanHopDong,
	           [GiaTriHopDong]               = @GiaTriHopDong,
	           [SoHopDong]                   = @SoHopDong,
	           [ThucHienDenNgayThucChay]     = @ThucHienDenNgayThucChay,
	           [ThanhTienThucChay]           = @ThanhTienThucChay,
	           [ThucHienDenNgayHoaDon]       = @ThucHienDenNgayHoaDon,
	           [ThanhTienHoaDon]             = @ThanhTienHoaDon,
	           [ThucHienDenNgayCongNo]       = @ThucHienDenNgayCongNo,
	           [ThanhTienThanhToan]          = @ThanhTienThanhToan,
	           [ThanhTienCongNo]             = @ThanhTienCongNo,
	           [NgayChuyenHopDongChoKeToan]  = @NgayChuyenHopDongChoKeToan,
	           [GhiChu]                      = @GhiChu,
	           [NgayNhanHopDongBanCung]      = @NgayNhanHopDongBanCung,
	           [DmKhachHangREF]              = @DmKhachHangREF,
	           [TenKhachHang]                = @TenKhachHang,
	           [DmHinhThucKhachHangREF]		 = @DmHinhThucKhachHangREF,
	           [TenHinhThucKhachHang]		 = @TenHinhThucKhachHang,
	           [DmLoaiKhachHangREF]			 = @DmLoaiKhachHangREF,
	           [TenLoaiKhachHang]			 = @TenLoaiKhachHang,
	           [SysNhanVienREF]              = @SysNhanVienREF,
	           [TenDangNhap]                 = @TenDangNhap,
	           [TenNhanVien]                 = @TenNhanVien,
	           [NgayDanhSoHopDong]           = @NgayDanhSoHopDong,
	           [NganhHang]                   = @NganhHang,
	           [DmNhomREF]                   = @DmNhomREF,
	           [TrangThaiHopDong]            = @TrangThaiHopDong,
	           [IsBanCung]                   = @IsBanCung,
	           [CongNo]                      = @CongNo,
	           [GhiChuHopDong]               = @GhiChuHopDong,
	           [NgayNhanBanFax]              = @NgayNhanBanFax,
	           [LyDoHuyHopDong]              = @LyDoHuyHopDong,
	           [DangSuDung]                  = @DangSuDung,
	           [IsGiayPhep]                  = @IsGiayPhep,
	           [DmPhongBanREF]               = @DmPhongBanREF,
	           [TenPhongBan]                 = @TenPhongBan,
	           [DmBoPhanREF]                 = @DmBoPhanREF,
	           [TenBoPhan]                   = @TenBoPhan,
	           [DmNhomLamViecREF]            = @DmNhomLamViecREF,
	           [TenNhom]                     = @TenNhom,
	           [DmDiaDiemLamViecREF]         = @DmDiaDiemLamViecREF,
	           [TenDiaDiemLamViec]           = @TenDiaDiemLamViec,
	           [ChuyenTrang]                 = @ChuyenTrang,
	           [IsUuDai]                     = @IsUuDai,
	           [CreatedBy]                   = @CreatedBy,
	           [CreatedAt]                   = @CreatedAt,
	           [LastModifiedBy]              = @LastModifiedBy,
	           [LastModifiedAt]              = @LastModifiedAt,
	           [DeletedStatus]               = @DeletedStatus,
	           [PrintStatus]                 = @PrintStatus,
	           [RecordStatus]                = @RecordStatus,
	           [NgayHuyHopDong]				 = @NgayHuyHopDong,
	           [NguoiHuyHopDong]			 = @NguoiHuyHopDong,
	           [IsCalcVoucher]				 = @IsCalcVoucher,
	           [GiaTriDatCoc]				 = @GiaTriDatCoc,
	           [NgayDatCoc]					 = @NgayDatCoc,
	           [NgayGiaHanDatCoc]			 = @NgayGiaHanDatCoc,
			   [TenNhanGoc]					 = @TenNhanGoc,
			   [DmNhanGocREF]				 = @DmNhanGocREF
	    WHERE  [HopDongID]                   = @HopDongID
	ELSE
	    INSERT INTO [dbo].[HopDong]
	      (
	        [HopDongID],
	        [DmMaHopDongREF],
	        [TenMaHopDong],
	        [SO],
	        [Thang],
	        [Nam],
	        [NgayKyHopDong],
	        [NhanHopDong],
	        [GiaTriHopDong],
	        [SoHopDong],
	        [ThucHienDenNgayThucChay],
	        [ThanhTienThucChay],
	        [ThucHienDenNgayHoaDon],
	        [ThanhTienHoaDon],
	        [ThucHienDenNgayCongNo],
	        [ThanhTienThanhToan],
	        [ThanhTienCongNo],
	        [NgayChuyenHopDongChoKeToan],
	        [GhiChu],
	        [NgayNhanHopDongBanCung],
	        [DmKhachHangREF],
	        [TenKhachHang],
	        [DmHinhThucKhachHangREF],
	        [TenHinhThucKhachHang],
	        [DmLoaiKhachHangREF],
	        [TenLoaiKhachHang],
	        [SysNhanVienREF],
	        [TenDangNhap],
	        [TenNhanVien],
	        [NgayDanhSoHopDong],
	        [NganhHang],
	        [DmNhomREF],
	        [TrangThaiHopDong],
	        [IsBanCung],
	        [CongNo],
	        [GhiChuHopDong],
	        [NgayNhanBanFax],
	        [LyDoHuyHopDong],
	        [DangSuDung],
	        [IsGiayPhep],
	        [DmPhongBanREF],
	        [TenPhongBan],
	        [DmBoPhanREF],
	        [TenBoPhan],
	        [DmNhomLamViecREF],
	        [TenNhom],
	        [DmDiaDiemLamViecREF],
	        [TenDiaDiemLamViec],
	        [ChuyenTrang],
	        [IsUuDai],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
	        [NgayHuyHopDong],
	        [NguoiHuyHopDong],
	        [IsCalcVoucher],
	        [GiaTriDatCoc],
	        [NgayDatCoc],
	        [NgayGiaHanDatCoc],
			[TenNhanGoc],
			[DmNhanGocREF]
	      )
	    VALUES
	      (
	        @HopDongID,
	        @DmMaHopDongREF,
	        @TenMaHopDong,
	        @SO,
	        @Thang,
	        @Nam,
	        @NgayKyHopDong,
	        @NhanHopDong,
	        @GiaTriHopDong,
	        @SoHopDong,
	        @ThucHienDenNgayThucChay,
	        @ThanhTienThucChay,
	        @ThucHienDenNgayHoaDon,
	        @ThanhTienHoaDon,
	        @ThucHienDenNgayCongNo,
	        @ThanhTienThanhToan,
	        @ThanhTienCongNo,
	        @NgayChuyenHopDongChoKeToan,
	        @GhiChu,
	        @NgayNhanHopDongBanCung,
	        @DmKhachHangREF,
	        @TenKhachHang,
	        @DmHinhThucKhachHangREF,
	        @TenHinhThucKhachHang,
	        @DmLoaiKhachHangREF,
	        @TenLoaiKhachHang,
	        @SysNhanVienREF,
	        @TenDangNhap,
	        @TenNhanVien,
	        @NgayDanhSoHopDong,
	        @NganhHang,
	        @DmNhomREF,
	        @TrangThaiHopDong,
	        @IsBanCung,
	        @CongNo,
	        @GhiChuHopDong,
	        @NgayNhanBanFax,
	        @LyDoHuyHopDong,
	        @DangSuDung,
	        @IsGiayPhep,
	        @DmPhongBanREF,
	        @TenPhongBan,
	        @DmBoPhanREF,
	        @TenBoPhan,
	        @DmNhomLamViecREF,
	        @TenNhom,
	        @DmDiaDiemLamViecREF,
	        @TenDiaDiemLamViec,
	        @ChuyenTrang,
	        @IsUuDai,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus,
	        @NgayHuyHopDong,
	        @NguoiHuyHopDong,
	        @IsCalcVoucher,
	        @GiaTriDatCoc,
	        @NgayDatCoc,
	        @NgayGiaHanDatCoc,
			@TenNhanGoc,
			@DmNhanGocREF
	      )
END
```
