# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:25:38.367000
- **Ngày sửa cuối**: 2017-05-13 08:13:49.847000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `bigint(8)` | No |
| `@HopDongREF` | `bigint(8)` | No |
| `@HopDongChiTietREF` | `bigint(8)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@TenChuyenMuc` | `nvarchar(400)` | No |
| `@TieuDiem` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(400)` | No |
| `@KhuyenMai` | `int(4)` | No |
| `@GiaTien` | `bigint(8)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@Link` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@TenHinhThucQuangCao` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(400)` | No |
| `@ThucChayHopDongChiTietPrREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmDonViTinhREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPR]
	@ThucChayHopDongChiTietPRID BIGINT ,
	@HopDongREF BIGINT ,
	@HopDongChiTietREF BIGINT ,
	@DmWebsiteREF INT ,
	@TenWebsite NVARCHAR(200) ,
	@DmChuyenMucREF INT ,
	@TenChuyenMuc NVARCHAR(200) ,
	@TieuDiem INT ,
	@DmNhanHangREF INT ,
	@NhanHang NVARCHAR(200) ,
	@KhuyenMai INT ,
	@GiaTien BIGINT ,
	@ThoiGianBatDau DATETIME ,
	@Link NVARCHAR(200) ,
	@GhiChu NVARCHAR(200) ,
	@DmHinhThucQuangCaoREF INT ,
	@TenHinhThucQuangCao NVARCHAR(200) ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT,
	@SoLuong INT,
	@ChietKhau FLOAT,
	@DmViTriREF INT,
	@TenViTri NVARCHAR(200),
	@ThucChayHopDongChiTietPrREF INT,
	@DmSanPhamREF INT,
	@DmDonViTinhREF INT
AS
BEGIN
	DECLARE @v_DmSanPhamREF INT, @v_DmHinhThucQuangCaoREF INT, @v_TenHinhThucQuangCao NVARCHAR(300)
	SET @v_DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
	SET @v_DmHinhThucQuangCaoREF = ISNULL(@DmHinhThucQuangCaoREF,0)
	SET @v_TenHinhThucQuangCao = ISNULL(@TenHinhThucQuangCao,'')
	

	SET @NhanHang = ISNULL(@NhanHang,'')
	SET @NhanHang = REPLACE(@NhanHang, '''''','''')
	--IF(@ThucChayHopDongChiTietPrREF <> 0)
	--BEGIN
	--	SELECT @v_DmHinhThucQuangCaoREF = tchdctp.DmHinhThucQuangCaoREF
	--	, @v_TenHinhThucQuangCao = tchdctp.TenHinhThucQuangCao
	--	, @v_DmSanPhamREF = tchdctp.DmSanPhamREF 
	--	FROM ThucChayHopDongChiTietPR tchdctp
	--	WHERE tchdctp.ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPrREF
	--	AND tchdctp.ThucChayHopDongChiTietPrREF = 0
		
	--	SET @v_DmSanPhamREF = ISNULL(@v_DmSanPhamREF,@DmSanPhamREF)
	--	SET @v_DmHinhThucQuangCaoREF = ISNULL(@v_DmHinhThucQuangCaoREF,@DmHinhThucQuangCaoREF)
	--END
	
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [ThucChayHopDongChiTietPR]
	           WHERE  [ThucChayHopDongChiTietPRID] = @ThucChayHopDongChiTietPRID
	       )
	   )
	    UPDATE [dbo].[ThucChayHopDongChiTietPR]
	    SET    [HopDongREF]                  = @HopDongREF,
	           [HopDongChiTietREF]           = @HopDongChiTietREF,
	           [DmWebsiteREF]                = @DmWebsiteREF,
	           [TenWebsite]                  = @TenWebsite,
	           [DmChuyenMucREF]              = @DmChuyenMucREF,
	           [TenChuyenMuc]                = @TenChuyenMuc,
	           [TieuDiem]                    = @TieuDiem,
	           [DmNhanHangREF]               = @DmNhanHangREF,
	           [NhanHang]                    = @NhanHang,
	           [KhuyenMai]                   = @KhuyenMai,
	           [GiaTien]                     = @GiaTien,
	           [ThoiGianBatDau]              = @ThoiGianBatDau,
	           [Link]                        = @Link,
	           [GhiChu]                      = @GhiChu,
	           [DmHinhThucQuangCaoREF]       = @v_DmHinhThucQuangCaoREF,
	           [TenHinhThucQuangCao]         = @v_TenHinhThucQuangCao,
	           [CreatedBy]                   = @CreatedBy,
	           [CreatedAt]                   = @CreatedAt,
	           [LastModifiedBy]              = @LastModifiedBy,
	           [LastModifiedAt]              = @LastModifiedAt,
	           [PrintStatus]                 = @PrintStatus,
	           [SoLuong]					 = @SoLuong,
	           [ChietKhau]					 = @ChietKhau,
	           [DmViTriREF]					 = @DmViTriREF,
	           [TenViTri]					 = @TenViTri,
	           [ThucChayHopDongChiTietPrREF] = @ThucChayHopDongChiTietPrREF,
	           [DmSanPhamREF]				 = @v_DmSanPhamREF,
	           [DmDonViTinhREF]				= @DmDonViTinhREF
	    WHERE  [ThucChayHopDongChiTietPRID]  = @ThucChayHopDongChiTietPRID
	ELSE
	    INSERT INTO [dbo].[ThucChayHopDongChiTietPR]
	      (
	        [ThucChayHopDongChiTietPRID],
	        [HopDongREF],
	        [HopDongChiTietREF],
	        [DmWebsiteREF],
	        [TenWebsite],
	        [DmChuyenMucREF],
	        [TenChuyenMuc],
	        [TieuDiem],
	        [DmNhanHangREF],
	        [NhanHang],
	        [KhuyenMai],
	        [GiaTien],
	        [ThoiGianBatDau],
	        [Link],
	        [GhiChu],
	        [DmHinhThucQuangCaoREF],
	        [TenHinhThucQuangCao],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
	        [SoLuong],
	        [ChietKhau],
            [DmViTriREF],
            [TenViTri],
            [ThucChayHopDongChiTietPrREF],
            [DmSanPhamREF],
			[DmDonViTinhREF]
	      )
	    VALUES
	      (
	        @ThucChayHopDongChiTietPRID,
	        @HopDongREF,
	        @HopDongChiTietREF,
	        @DmWebsiteREF,
	        @TenWebsite,
	        @DmChuyenMucREF,
	        @TenChuyenMuc,
	        @TieuDiem,
	        @DmNhanHangREF,
	        @NhanHang,
	        @KhuyenMai,
	        @GiaTien,
	        @ThoiGianBatDau,
	        @Link,
	        @GhiChu,
	        @v_DmHinhThucQuangCaoREF,
	        @v_TenHinhThucQuangCao,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus,
	        @SoLuong,
	        @ChietKhau,
	        @DmViTriREF,
	        @TenViTri,
	        @ThucChayHopDongChiTietPrREF,
	        @v_DmSanPhamREF,
			@DmDonViTinhREF
	      )
END
	
```
