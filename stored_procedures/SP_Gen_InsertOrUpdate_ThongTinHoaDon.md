# Stored Procedure: `Gen_InsertOrUpdate_ThongTinHoaDon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:18:29.800000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.807000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinHoaDonID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHoaDon` | `nvarchar(400)` | No |
| `@NgayXuatHoaDon` | `datetime(8)` | No |
| `@GiaTri` | `float(8)` | No |
| `@NgayTraHoaDon` | `datetime(8)` | No |
| `@SoBangThongKe` | `nvarchar(400)` | No |
| `@TaiKhoanKhachHang` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinHoaDon]
	@ThongTinHoaDonID INT ,
	@HopDongREF INT ,
	@SoHoaDon NVARCHAR(200) ,
	@NgayXuatHoaDon DATETIME ,
	@GiaTri FLOAT ,
	@NgayTraHoaDon DATETIME ,
	@SoBangThongKe NVARCHAR(200) ,
	@TaiKhoanKhachHang NVARCHAR(200) ,
	@GhiChu NVARCHAR(200) ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@RecordStatus INT ,
	@PrintStatus INT
AS
BEGIN
	DECLARE @TongGiaTriHD FLOAT, @NgayXuatHoaDonMax DATETIME
	DECLARE @GiaTriHDConLai FLOAT, @GiaTriThanhToan FLOAT, @IsExistRecord INT
	DECLARE @GiaTriHoaDonThanhToan FLOAT, @HopDongHanThanhToanID INT
	
	SET @TongGiaTriHD = 0
	SET @IsExistRecord = 0
	SET @GiaTriThanhToan = 0
	SET @GiaTriHDConLai = @GiaTri
	SET @NgayXuatHoaDonMax = '2010-01-01'
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [ThongTinHoaDon]
	           WHERE  [ThongTinHoaDonID] = @ThongTinHoaDonID
	       )
	   )
	    UPDATE [dbo].[ThongTinHoaDon]
	    SET    [HopDongREF]         = @HopDongREF,
	           [SoHoaDon]           = @SoHoaDon,
	           [NgayXuatHoaDon]     = @NgayXuatHoaDon,
	           [GiaTri]             = @GiaTri,
	           [NgayTraHoaDon]      = @NgayTraHoaDon,
	           [SoBangThongKe]      = @SoBangThongKe,
	           [TaiKhoanKhachHang]  = @TaiKhoanKhachHang,
	           [GhiChu]             = @GhiChu,
	           [CreatedBy]          = @CreatedBy,
	           [CreatedAt]          = @CreatedAt,
	           [LastModifiedBy]     = @LastModifiedBy,
	           [LastModifiedAt]     = @LastModifiedAt,
	           [DeletedStatus]      = @DeletedStatus,
	           [RecordStatus]       = @RecordStatus,
	           [PrintStatus]        = @PrintStatus
	    WHERE  [ThongTinHoaDonID]   = @ThongTinHoaDonID
	ELSE
	    INSERT INTO [dbo].[ThongTinHoaDon]
	      (
	        [ThongTinHoaDonID],
	        [HopDongREF],
	        [SoHoaDon],
	        [NgayXuatHoaDon],
	        [GiaTri],
	        [NgayTraHoaDon],
	        [SoBangThongKe],
	        [TaiKhoanKhachHang],
	        [GhiChu],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [RecordStatus],
	        [PrintStatus]
	      )
	    VALUES
	      (
	        @ThongTinHoaDonID,
	        @HopDongREF,
	        @SoHoaDon,
	        @NgayXuatHoaDon,
	        @GiaTri,
	        @NgayTraHoaDon,
	        @SoBangThongKe,
	        @TaiKhoanKhachHang,
	        @GhiChu,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @RecordStatus,
	        @PrintStatus
	      )
	      --1. UPDATE THONG TIN HOA DON CHO HopDong
	      SELECT @TongGiaTriHD = SUM(ISNULL(tthd.GiaTri,0)), @NgayXuatHoaDonMax = MAX(tthd.NgayXuatHoaDon)  
	      FROM ThongTinHoaDon tthd
	      WHERE tthd.HopDongREF = @HopDongREF  AND tthd.DeletedStatus = 0
	      
	      UPDATE HopDong
	      SET
	      	ThucHienDenNgayHoaDon = @NgayXuatHoaDonMax,
	      	ThanhTienHoaDon = @TongGiaTriHD
	      WHERE	HopDongID = @HopDongREF
		        
END

```
