# Stored Procedure: `ThucChay_UpdateGiaTriThayDoi_HDHuy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 10:29:42.597000
- **Ngày sửa cuối**: 2017-01-20 10:38:23.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayCheckHuy` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoi_HDHuy] '2014-08-15'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoi_HDHuy] 
-- Add the parameters for the stored procedure here
	--@HopDongREF INT,
	--@SoHopDong NVARCHAR(50),
	@NgayCheckHuy DATETIME,
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @HopDongREF INT,
			@SoHopDong NVARCHAR(50),
			@DmSanPhamREF INT
		
	DECLARE @HopDongChiTietID INT,
	        @HopDongChiTietThayDoiGia INT,
	        @HopDongChiTietThayDoiCK INT
	
	DECLARE @DotChayHopDongChiTietThayDoi INT,
	        @SoLuongHD INT,
	        @SoLuongHDBF INT
	
	DECLARE @SoNgayDotChayThayDoi INT,
	        @DmWebsiteREF INT,
	        @TenWebsite NVARCHAR(100),
	        @SoLuongHT INT,
	        @TiLeThuChaySite FLOAT
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX),
	        @NGUON_LOG NVARCHAR(500),
	        @CONTENT_DETAIL_LOG NVARCHAR(MAX)
	
	DECLARE @CountHDTD INT,
	        @GiaTriThayDoi FLOAT,
	        @SoLuongThucChayByWebiste INT,
	        @TongSLThucChayByWebsite BIGINT,
	        @GiaTriThayDoi_HDTD_SL FLOAT
	
	DECLARE @DonGiaLienKeTruoc FLOAT,
	        @SoLuongThucChay FLOAT
	
	DECLARE @DonGiaHienTai    FLOAT,
	        @TenSanPham       NVARCHAR(50),
	        @NgayThayDoiLast  DATETIME
	
	SET @SoNgayDotChayThayDoi = 0
	SET @SoLuongThucChayByWebiste = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @DotChayHopDongChiTietThayDoi = 0
	SET @HopDongChiTietThayDoiGia = 0
	SET @HopDongChiTietThayDoiCK = 0
	SET @SoLuongHD = 0
	SET @SoLuongHDBF = 0
	SET @TiLeThuChaySite = 0
	SET @TongSLThucChayByWebsite = 0
	SET @GiaTriThayDoi_HDTD_SL = 0
	PRINT @SoHopDong
	PRINT @DmSanPhamREF

	DELETE FROM ThucChayDaTinh
	WHERE NgayThucHien = @NgayThucHien
	AND DotChayHopDong = 'HDHUY'
	AND DmSanPhamREF NOT IN (423,141)

	DECLARE Record_Cursor_TCDT1 CURSOR  FOR
		SELECT * FROM
		(
		SELECT tcdt.DmWebsiteREF, tcdt.TenWebsite, tcdt.HopDongChiTietREF,tcdt.HopDongID,tcdt.SoHopDong, tcdt.DmSanPhamREF
		, tcdt.TenSanPham, 
		 - SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)thanhtienthucchay,
		 - SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) SoLuongThucChaytheowebsite
		FROM ThucChayDaTinh tcdt
		INNER JOIN HopDong hd ON hd.HopDongID = tcdt.HopDongID
		WHERE 1=1
		AND hd.TrangThaiHopDong = 3
		AND tcdt.TrangThaiHopDong <> 3
		AND CONVERT(DATE,hd.LastModifiedAt) = CONVERT(DATE,@NgayCheckHuy)
		AND tcdt.DmSanPhamREF NOT IN (423,141)
		GROUP BY tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF
		, tcdt.TenSanPham, tcdt.DmWebsiteREF, tcdt.TenWebsite
		)tcdt
		WHERE tcdt.thanhtienthucchay <> 0
		ORDER BY tcdt.HopDongID, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF

	OPEN Record_Cursor_TCDT1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_TCDT1 INTO @DmWebsiteREF, @TenWebsite,@HopDongChiTietID, @HopDongREF, @SoHopDong, @DmSanPhamREF, @TenSanPham, @GiaTriThayDoi, @SoLuongThucChayByWebiste
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    SET @CONTENT_LOG = N'Hợp đồng ' + @SoHopDong + N' hủy ngày ' + CONVERT(NVARCHAR(50),@NgayThucHien) + ' ,Website :' + @TenWebsite
	    --GHI LOG VIEC THAY DOI
	        INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
	          (
	            [ThuChay_LogNNTinhGiaTriThayDoiID],
	            [HopDongREF],
	            [SoHopDong],
	            [HopDongChiTietREF],
	            [DmSanPhamREF],
	            [DmWebsiteREF],
	            [NgayThucHien],
	            [GiaTriThayDoi],
	            [GiaSauCK1],
	            [Soluong1],
	            [GiaSauCK2],
	            [Soluong2],
	            [NoiDungLog],
	            [NguonLog],
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
	            NEWID(),
	            @HopDongREF,
	            @SoHopDong,
	            @HopDongChiTietID,
	            @DmSanPhamREF,
	            @DmWebsiteREF,
	            @NgayThucHien,
	            @GiaTriThayDoi,
	            @DonGiaHienTai,
	            @SoLuongHT,
	            @DonGiaLienKeTruoc,
	            @SoLuongHT,
	            @CONTENT_LOG,
	            @NGUON_LOG,
	            'CPM',
	            'ThucChay',
	            GETDATE(),
	            'ThucChay',
	            GETDATE(),
	            0,
	            0,
	            0
	          )
	      PRINT 'So hop dong: ' + @SoHopDong
	        IF(@HopDongChiTietID <> 0)
	        BEGIN
	        	PRINT 'ThucTreo: '
				--EXEC  ThucChay_InsertThucTreoThayDoiSP_CPM_HDHuy @HopDongChiTietID, @DmSanPhamREF,@TenSanPham, @NgayThucHien, @GiaTriThayDoi,@DmWebsiteREF, @TenWebsite, @SoLuongThucChayByWebiste
				EXEC  [dbo].[ThucChay_InsertThucChayDaTinh_DoiTruGiam_CPM_HDHuy] @HopDongChiTietID, @DmSanPhamREF,@TenSanPham, @NgayThucHien, @GiaTriThayDoi,@DmWebsiteREF, @TenWebsite, @SoLuongThucChayByWebiste
				
	        END
			ELSE
				BEGIN
					PRINT 'SanPham: '
					--EXEC  ThucChay_InsertThucTreoThayDoiPPSP_CPM_KiemToan @HopDongChiTietID, @DmSanPhamREF,@TenSanPham, @NgayThucHien, @GiaTriThayDoi,@DmWebsiteREF, @TenWebsite, @SoLuongThucChayByWebiste	
					EXEC  ThucChay_InsertThucTreoThayDoiPPSP_CPM_HDHuy @HopDongREF, @DmSanPhamREF, @TenSanPham, @NgayThucHien, @GiaTriThayDoi,@DmWebsiteREF, @TenWebsite, @SoLuongThucChayByWebiste	
				END
					
	    FETCH NEXT FROM Record_Cursor_TCDT1 INTO @DmWebsiteREF, @TenWebsite,@HopDongChiTietID, @HopDongREF, @SoHopDong, @DmSanPhamREF, @TenSanPham, @GiaTriThayDoi, @SoLuongThucChayByWebiste
	END
	CLOSE Record_Cursor_TCDT1
	DEALLOCATE Record_Cursor_TCDT1
	SELECT 1
END

```
