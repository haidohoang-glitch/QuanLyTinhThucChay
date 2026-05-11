# Stored Procedure: `usp_InsertThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-09 11:13:12.260000
- **Ngày sửa cuối**: 2014-11-19 12:24:45.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(510)` | No |
| `@TenWebsite` | `nvarchar(510)` | No |
| `@ChuyenMuc` | `nvarchar(510)` | No |
| `@TieuDiem` | `int(4)` | No |
| `@KhuyenMai` | `int(4)` | No |
| `@GiaTien` | `int(4)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@Link` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[usp_InsertThucChayHopDongChiTietPR]
	@ThucChayHopDongChiTietPRID INT,
	@HopDongREF INT,
	@HopDongChiTietREF INT,
	@NhanHang NVARCHAR(255),
	@TenWebsite NVARCHAR(255),
	@ChuyenMuc NVARCHAR(255),
	@TieuDiem INT,
	@KhuyenMai INT,
	@GiaTien INT,
	@ThoiGianBatDau DATETIME,
	@Link NVARCHAR(200),
	@GhiChu NVARCHAR(255),
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModifiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT
AS
	SET NOCOUNT ON
	IF (
	       EXISTS(
	           SELECT [HopDongREF]
	           FROM   ThucChayHopDongChiTietPR
	           WHERE  [ThucChayHopDongChiTietPRID] = @ThucChayHopDongChiTietPRID
	       )
	   )
	    UPDATE [dbo].[ThucChayHopDongChiTietPR]
	    SET    [HopDongREF]                  = @HopDongREF,
	           [HopDongChiTietREF]           = @HopDongChiTietREF,
	           [NhanHang]                    = @NhanHang,
	           [TenWebsite]                  = @TenWebsite,
	           [ChuyenMuc]                   = @ChuyenMuc,
	           [TieuDiem]                    = @TieuDiem,
	           [KhuyenMai]                   = @KhuyenMai,
	           [GiaTien]                     = @GiaTien,
	           [ThoiGianBatDau]              = @ThoiGianBatDau,
	           [Link]                        = @Link,
	           [GhiChu]                      = @GhiChu,
	           [LastModifiedBy]              = @LastModifiedBy,
	           [LastModifiedAt]              = @LastModifiedAt,
	           [PrintStatus]                 = @PrintStatus
	    WHERE  [ThucChayHopDongChiTietPRID]  = @ThucChayHopDongChiTietPRID
	ELSE
	    INSERT INTO [dbo].[ThucChayHopDongChiTietPR]
	      (
	        [ThucChayHopDongChiTietPRID],
	        [HopDongREF],
	        [HopDongChiTietREF],
	        [NhanHang],
	        [TenWebsite],
	        [ChuyenMuc],
	        [TieuDiem],
	        [KhuyenMai],
	        [GiaTien],
	        [ThoiGianBatDau],
	        [Link],
	        [GhiChu],
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
	        @ThucChayHopDongChiTietPRID,
	        @HopDongREF,
	        @HopDongChiTietREF,
	        @NhanHang,
	        @TenWebsite,
	        @ChuyenMuc,
	        @TieuDiem,
	        @KhuyenMai,
	        @GiaTien,
	        @ThoiGianBatDau,
	        @Link,
	        @GhiChu,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )
	    

```
