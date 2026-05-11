# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTietPRLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:26:38.110000
- **Ngày sửa cuối**: 2016-11-09 15:21:03.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRLogID` | `bigint(8)` | No |
| `@ThucChayHopDongChiTietPRREF` | `int(4)` | No |
| `@HopDongREF` | `bigint(8)` | No |
| `@HopDongChiTietREF` | `bigint(8)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@TenChuyenMuc` | `nvarchar(400)` | No |
| `@TieuDiem` | `int(4)` | No |
| `@DmNhanHangREF` | `nvarchar(400)` | No |
| `@NhanHang` | `nvarchar(400)` | No |
| `@KhuyenMai` | `int(4)` | No |
| `@GiaTien` | `bigint(8)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@Link` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@TenHinhThucQuangCao` | `nvarchar(400)` | No |
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
| `@SoLuong` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPRLog]
	@ThucChayHopDongChiTietPRLogID BIGINT ,
	@ThucChayHopDongChiTietPRREF INT ,
	@HopDongREF BIGINT ,
	@HopDongChiTietREF BIGINT ,
	@DmWebsiteREF INT ,
	@TenWebsite NVARCHAR(200) ,
	@DmChuyenMucREF INT ,
	@TenChuyenMuc NVARCHAR(200) ,
	@TieuDiem INT ,
	@DmNhanHangREF NVARCHAR(200) ,
	@NhanHang NVARCHAR(200) ,
	@KhuyenMai INT ,
	@GiaTien BIGINT ,
	@ThoiGianBatDau DATETIME ,
	@Link NVARCHAR(200) ,
	@GhiChu NVARCHAR(200) ,
	@DmHinhThucQuangCaoREF INT ,
	@TenHinhThucQuangCao NVARCHAR(200) ,
	@ThoiGianLog DATETIME ,
	@NguoiLog NVARCHAR(200) ,
	@LoaiLog INT ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT,
	@SoLuong INT
AS
BEGIN
	
	SET @NhanHang = ISNULL(@NhanHang,'')
	SET @NhanHang = REPLACE(@NhanHang, '''''','''')

	IF (
	       EXISTS(
	           SELECT *
	           FROM   [ThucChayHopDongChiTietPRLog]
	           WHERE  [ThucChayHopDongChiTietPRLogID] = @ThucChayHopDongChiTietPRLogID
	       )
	)
	BEGIN
		UPDATE [dbo].[ThucChayHopDongChiTietPRLog]
	    SET    [ThucChayHopDongChiTietPRREF]    = @ThucChayHopDongChiTietPRREF,
	           [HopDongREF]                     = @HopDongREF,
	           [HopDongChiTietREF]              = @HopDongChiTietREF,
	           [DmWebsiteREF]                   = @DmWebsiteREF,
	           [TenWebsite]                     = @TenWebsite,
	           [DmChuyenMucREF]                 = @DmChuyenMucREF,
	           [TenChuyenMuc]                   = @TenChuyenMuc,
	           [TieuDiem]                       = @TieuDiem,
	           [DmNhanHangREF]                  = @DmNhanHangREF,
	           [NhanHang]                       = @NhanHang,
	           [KhuyenMai]                      = @KhuyenMai,
	           [GiaTien]                        = @GiaTien,
	           [ThoiGianBatDau]                 = @ThoiGianBatDau,
	           [Link]                           = @Link,
	           [GhiChu]                         = @ThucChayHopDongChiTietPRREF ,--@GhiChu,
	           [DmHinhThucQuangCaoREF]          = @DmHinhThucQuangCaoREF,
	           [TenHinhThucQuangCao]            = @TenHinhThucQuangCao,
	           [ThoiGianLog]                    = @ThoiGianLog,
	           [NguoiLog]                       = @NguoiLog,
	           [LoaiLog]                        = @LoaiLog,
	           [CreatedBy]                      = @CreatedBy,
	           [CreatedAt]                      = @CreatedAt,
	           [LastModifiedBy]                 = @LastModifiedBy,
	           [LastModifiedAt]                 = @LastModifiedAt,
	           [DeletedStatus]                  = @DeletedStatus,
	           [PrintStatus]                    = @PrintStatus,
	           [RecordStatus]                   = @RecordStatus,
	           [SoLuong]						= @SoLuong
	    WHERE  [ThucChayHopDongChiTietPRLogID]  = @ThucChayHopDongChiTietPRLogID
	END
	    
	ELSE
		BEGIN
			INSERT INTO [dbo].[ThucChayHopDongChiTietPRLog]
	      (
	        [ThucChayHopDongChiTietPRLogID],
	        [ThucChayHopDongChiTietPRREF],
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
	        [ThoiGianLog],
	        [NguoiLog],
	        [LoaiLog],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
	        [SoLuong]
	      )
	    VALUES
	      (
	        @ThucChayHopDongChiTietPRLogID,
	        @ThucChayHopDongChiTietPRREF,
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
	        @DmHinhThucQuangCaoREF,
	        @TenHinhThucQuangCao,
	        @ThoiGianLog,
	        @NguoiLog,
	        @LoaiLog,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus,
	        @SoLuong
	      )
	      
		END
	    
	      IF(@LoaiLog = 3)
	      BEGIN
	      	UPDATE ThucChayHopDongChiTietPR
	      	SET
	      		LastModifiedBy = @LastModifiedBy,
	      		LastModifiedAt = @ThoiGianLog,
	      		DeletedStatus = 1
	      	WHERE ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRREF
	      END
END
	

```
