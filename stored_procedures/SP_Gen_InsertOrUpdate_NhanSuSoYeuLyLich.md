# Stored Procedure: `Gen_InsertOrUpdate_NhanSuSoYeuLyLich`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:36:13.683000
- **Ngày sửa cuối**: 2015-10-27 15:26:36.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichID` | `bigint(8)` | No |
| `@MaNhanSu` | `nvarchar(400)` | No |
| `@HoVaTen` | `nvarchar(400)` | No |
| `@BiDanh` | `nvarchar(400)` | No |
| `@NgaySinh` | `datetime(8)` | No |
| `@NoiSinh` | `nvarchar(400)` | No |
| `@GioiTinh` | `int(4)` | No |
| `@SoCMTND` | `nvarchar(400)` | No |
| `@NoiCap` | `nvarchar(400)` | No |
| `@NgayCap` | `datetime(8)` | No |
| `@HoKhauThuongTru` | `nvarchar(400)` | No |
| `@DiaChiThuongTru` | `nvarchar(400)` | No |
| `@DiaChiLienHe` | `nvarchar(400)` | No |
| `@DanToc` | `nvarchar(400)` | No |
| `@TonGiao` | `nvarchar(400)` | No |
| `@TrinhDoVanHoa` | `nvarchar(400)` | No |
| `@TrinhDoNgoaiNgu` | `nvarchar(400)` | No |
| `@QuaTrinhBanThan` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Email` | `nvarchar(400)` | No |
| `@EmailCaNhan` | `nvarchar(400)` | No |
| `@Mobile` | `nvarchar(400)` | No |
| `@DienThoai1` | `nvarchar(400)` | No |
| `@DienThoai2` | `nvarchar(400)` | No |
| `@Code` | `bigint(8)` | No |
| `@NgayBatDauLamViec` | `datetime(8)` | No |
| `@NgayNghiViec` | `datetime(8)` | No |
| `@ImageFIleName` | `nvarchar(400)` | No |
| `@ImageFIleNameEncode` | `nvarchar(400)` | No |
| `@MaSoThue` | `nvarchar(400)` | No |
| `@IsNhanSuYN` | `int(4)` | No |
| `@BanMem` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuSoYeuLyLich]
	@NhanSuSoYeuLyLichID BIGINT ,
	@MaNhanSu NVARCHAR(200) ,
	@HoVaTen NVARCHAR(200) ,
	@BiDanh NVARCHAR(200) ,
	@NgaySinh DATETIME ,
	@NoiSinh NVARCHAR(200) ,
	@GioiTinh INT ,
	@SoCMTND NVARCHAR(200) ,
	@NoiCap NVARCHAR(200) ,
	@NgayCap DATETIME ,
	@HoKhauThuongTru NVARCHAR(200) ,
	@DiaChiThuongTru NVARCHAR(200) ,
	@DiaChiLienHe NVARCHAR(200) ,
	@DanToc NVARCHAR(200) ,
	@TonGiao NVARCHAR(200) ,
	@TrinhDoVanHoa NVARCHAR(200) ,
	@TrinhDoNgoaiNgu NVARCHAR(200) ,
	@QuaTrinhBanThan NVARCHAR(200) ,
	@GhiChu NVARCHAR(200) ,
	@Email NVARCHAR(200) ,
	@EmailCaNhan NVARCHAR(200) ,
	@Mobile NVARCHAR(200) ,
	@DienThoai1 NVARCHAR(200) ,
	@DienThoai2 NVARCHAR(200) ,
	@Code BIGINT ,
	@NgayBatDauLamViec DATETIME ,
	@NgayNghiViec DATETIME ,
	@ImageFIleName NVARCHAR(200) ,
	@ImageFIleNameEncode NVARCHAR(200) ,
	@MaSoThue NVARCHAR(200) ,
	@IsNhanSuYN INT ,
	@BanMem NVARCHAR(200) ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT
AS
BEGIN
		
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [NhanSuSoYeuLyLich]
	           WHERE  [NhanSuSoYeuLyLichID] = @NhanSuSoYeuLyLichID
	       )
	   )
	    UPDATE [dbo].[NhanSuSoYeuLyLich]
	    SET    [MaNhanSu]             = @MaNhanSu,
	           [HoVaTen]              = @HoVaTen,
	           [BiDanh]               = @BiDanh,
	           [NgaySinh]             = @NgaySinh,
	           [NoiSinh]              = @NoiSinh,
	           [GioiTinh]             = @GioiTinh,
	           [SoCMTND]              = @SoCMTND,
	           [NoiCap]               = @NoiCap,
	           [NgayCap]              = @NgayCap,
	           [HoKhauThuongTru]      = @HoKhauThuongTru,
	           [DiaChiThuongTru]      = @DiaChiThuongTru,
	           [DiaChiLienHe]         = @DiaChiLienHe,
	           [DanToc]               = @DanToc,
	           [TonGiao]              = @TonGiao,
	           [TrinhDoVanHoa]        = @TrinhDoVanHoa,
	           [TrinhDoNgoaiNgu]      = @TrinhDoNgoaiNgu,
	           [QuaTrinhBanThan]      = @QuaTrinhBanThan,
	           [GhiChu]               = @GhiChu,
	           [Email]                = @Email,
	           [EmailCaNhan]          = @EmailCaNhan,
	           [Mobile]               = @Mobile,
	           [DienThoai1]           = @DienThoai1,
	           [DienThoai2]           = @DienThoai2,
	           [Code]                 = @Code,
	           [NgayBatDauLamViec]    = @NgayBatDauLamViec,
	           [NgayNghiViec]         = @NgayNghiViec,
	           [ImageFIleName]        = @ImageFIleName,
	           [ImageFIleNameEncode]  = @ImageFIleNameEncode,
	           [MaSoThue]             = @MaSoThue,
	           [IsNhanSuYN]           = @IsNhanSuYN,
	           [BanMem]               = @BanMem,
	           [CreatedBy]            = @CreatedBy,
	           [CreatedAt]            = @CreatedAt,
	           [LastModifiedBy]       = @LastModifiedBy,
	           [LastModifiedAt]       = @LastModifiedAt,
	           [DeletedStatus]        = @DeletedStatus,
	           [PrintStatus]          = @PrintStatus,
	           [RecordStatus]         = @RecordStatus
	    WHERE  [NhanSuSoYeuLyLichID]  = @NhanSuSoYeuLyLichID
	ELSE
	    INSERT INTO [dbo].[NhanSuSoYeuLyLich]
	      (
	        [NhanSuSoYeuLyLichID],
	        [MaNhanSu],
	        [HoVaTen],
	        [BiDanh],
	        [NgaySinh],
	        [NoiSinh],
	        [GioiTinh],
	        [SoCMTND],
	        [NoiCap],
	        [NgayCap],
	        [HoKhauThuongTru],
	        [DiaChiThuongTru],
	        [DiaChiLienHe],
	        [DanToc],
	        [TonGiao],
	        [TrinhDoVanHoa],
	        [TrinhDoNgoaiNgu],
	        [QuaTrinhBanThan],
	        [GhiChu],
	        [Email],
	        [EmailCaNhan],
	        [Mobile],
	        [DienThoai1],
	        [DienThoai2],
	        [Code],
	        [NgayBatDauLamViec],
	        [NgayNghiViec],
	        [ImageFIleName],
	        [ImageFIleNameEncode],
	        [MaSoThue],
	        [IsNhanSuYN],
	        [BanMem],
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
	        @NhanSuSoYeuLyLichID,
	        @MaNhanSu,
	        @HoVaTen,
	        @BiDanh,
	        @NgaySinh,
	        @NoiSinh,
	        @GioiTinh,
	        @SoCMTND,
	        @NoiCap,
	        @NgayCap,
	        @HoKhauThuongTru,
	        @DiaChiThuongTru,
	        @DiaChiLienHe,
	        @DanToc,
	        @TonGiao,
	        @TrinhDoVanHoa,
	        @TrinhDoNgoaiNgu,
	        @QuaTrinhBanThan,
	        @GhiChu,
	        @Email,
	        @EmailCaNhan,
	        @Mobile,
	        @DienThoai1,
	        @DienThoai2,
	        @Code,
	        @NgayBatDauLamViec,
	        @NgayNghiViec,
	        @ImageFIleName,
	        @ImageFIleNameEncode,
	        @MaSoThue,
	        @IsNhanSuYN,
	        @BanMem,
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
