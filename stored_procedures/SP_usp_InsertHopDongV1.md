# Stored Procedure: `usp_InsertHopDongV1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-04 17:26:21.933000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.800000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |
| `@TenMaHopDong` | `nvarchar(100)` | No |
| `@So` | `nvarchar(100)` | No |
| `@Thang` | `int(4)` | No |
| `@Nam` | `int(4)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@NhanHopDong` | `nvarchar(2000)` | No |
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
| `@NganhHang` | `nvarchar(2000)` | No |
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
| `@TenDiaDiemLamViec` | `nvarchar(500)` | No |
| `@ChuyenTrang` | `int(4)` | No |
| `@IsUuDai` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertHopDongV1](
    @HopDongID                   INT,
    @DmMaHopDongREF              INT,
    @TenMaHopDong                NVARCHAR(50),
    @So                          NVARCHAR(50),
    @Thang                       INT,
    @Nam                         INT,
    @NgayKyHopDong               DATETIME,
    @NhanHopDong                 NVARCHAR(1000),
    @GiaTriHopDong               FLOAT,
    @SoHopDong                   NVARCHAR(50),
    @NgayChuyenHopDongChoKeToan  DATETIME,
    @GhiChu                      NVARCHAR(300),
    @NgayNhanHopDongBanCung      DATETIME,
    @DmKhachHangREF              INT,
    @TenKhachHang                NVARCHAR(255),
    @SysNhanVienREF              INT,
    @TenDangNhap                 NVARCHAR(25),
    @TenNhanVien                 NVARCHAR(100),
    @NgayDanhSoHopDong           DATETIME,
    @NganhHang                   NVARCHAR(1000),
    @DmNhomREF                   INT,
    @TrangThaiHopDong            INT,
    @IsBanCung                   INT,
    @CongNo                      FLOAT,
    @GhiChuHopDong               NVARCHAR(4000),
    @NgayNhanBanFax              DATETIME,
    @LyDoHuyHopDong              NVARCHAR(4000),
    @DangSuDung                  INT,
    @IsGiayPhep                  INT,
    @DmPhongBanREF               INT,
    @TenPhongBan                 NVARCHAR(50),
    @DmBoPhanREF                 INT,
    @TenBoPhan                   NVARCHAR(50),
    @DmNhomLamViecREF            INT,
    @TenNhom                     NVARCHAR(50),
    @DmDiaDiemLamViecREF         INT,
    @TenDiaDiemLamViec           NVARCHAR(250),
    @ChuyenTrang                 INT,
    @IsUuDai                     INT,
    @CreatedBy                   NVARCHAR(50),
    @CreatedAt                   DATETIME,
    @LastModifiedBy              NVARCHAR(50),
    @LastModifiedAt              DATETIME,
    @DeletedStatus               INT,
    @PrintStatus                 INT,
    @RecordStatus                INT
)
AS
	SET NOCOUNT ON
	
	IF (
	       EXISTS(
	           SELECT *
	           FROM   HopDong
	           WHERE  [HopDongID] = @HopDongID
	       )
	   )
	BEGIN
	    UPDATE [dbo].[HopDong]
	    SET    [DmMaHopDongREF]              = @DmMaHopDongREF,
	           [TenMaHopDong]                = @TenMaHopDong,
	           [So]                          = @So,
	           [Thang]                       = @Thang,
	           [Nam]                         = @Nam,
	           [NgayKyHopDong]               = @NgayKyHopDong,
	           [NhanHopDong]                 = @NhanHopDong,
	           [GiaTriHopDong]               = @GiaTriHopDong,
	           [SoHopDong]                   = @SoHopDong,
	           [NgayChuyenHopDongChoKeToan]  = @NgayChuyenHopDongChoKeToan,
	           [GhiChu]                      = @GhiChu,
	           [NgayNhanHopDongBanCung]      = @NgayNhanHopDongBanCung,
	           [DmKhachHangREF]              = @DmKhachHangREF,
	           [TenKhachHang]                = @TenKhachHang,
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
	           [LastModifiedBy]              = @LastModifiedBy,
	           [LastModifiedAt]              = @LastModifiedAt,
	           [DeletedStatus]               = @DeletedStatus,
	           [PrintStatus]                 = @PrintStatus,
	           [RecordStatus]                = @RecordStatus
	    WHERE  [HopDongID]                   = @HopDongID
	END
	ELSE
	BEGIN
	    INSERT INTO 
	           [dbo].[HopDong]
	      (
	        [HopDongID],
	        [DmMaHopDongREF],
	        [TenMaHopDong],
	        [So],
	        [Thang],
	        [Nam],
	        [NgayKyHopDong],
	        [NhanHopDong],
	        [GiaTriHopDong],
	        [SoHopDong],
	        [NgayChuyenHopDongChoKeToan],
	        [GhiChu],
	        [NgayNhanHopDongBanCung],
	        [DmKhachHangREF],
	        [TenKhachHang],
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
	        [RecordStatus]
	      )
	    VALUES
	      (
	        @HopDongID,
	        @DmMaHopDongREF,
	        @TenMaHopDong,
	        @So,
	        @Thang,
	        @Nam,
	        @NgayKyHopDong,
	        @NhanHopDong,
	        @GiaTriHopDong,
	        @SoHopDong,
	        @NgayChuyenHopDongChoKeToan,
	        @GhiChu,
	        @NgayNhanHopDongBanCung,
	        @DmKhachHangREF,
	        @TenKhachHang,
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
	        @RecordStatus
	      )
	END

```
