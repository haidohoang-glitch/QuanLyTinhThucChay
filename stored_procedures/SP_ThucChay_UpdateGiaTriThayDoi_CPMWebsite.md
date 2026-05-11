# Stored Procedure: `ThucChay_UpdateGiaTriThayDoi_CPMWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-06 11:42:54.990000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.943000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoi_CPMWebsite] '2014-06-05'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoi_CPMWebsite] 
-- Add the parameters for the stored procedure here
	--@HopDongREF INT,
	--@SoHopDong NVARCHAR(50),
	--@DmSanPhamREF INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @HopDongREF INT,
			@SoHopDong NVARCHAR(50),
			@DmSanPhamREF INT
		
	DECLARE @ChietKhauBF FLOAT,@HopDongChiTietID INT,
	        @ChietKhau FLOAT,
	        @DonGiaBF FLOAT,
	        @DonGia FLOAT,
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
	
	DECLARE Record_Cursor_TCDT1 CURSOR  FOR


			SELECT a.DmWebsiteREF,a.TenWebsite,0 HopdongchitietID, a.HopDongID, a.SoHopDong,a.DmSanPhamREF, a.TenSanPham
			, ((a.SoLuongThucChay * (b.DonGia*(100-b.ChietKhau)/100)) -a.thanhtien) thanhtienlech  
			  FROM
			(
			SELECT tcdt.SoHopDong, tcdt.HopDongID, tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmWebsiteREF, tcdt.TenWebsite
			,SUM(tcdt.SoLuongThucChay)SoLuongThucChay
			,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) thanhtien
			  FROM ThucChayDaTinh tcdt
			WHERE tcdt.HopDongID in
			(22943,
			24028,
			20701,
			17633,
			22425,
			22622,
			21482,
			24044,
			21691)
			AND tcdt.DmSanPhamREF = 339
			AND tcdt.DonViTinh = 'CLICK'
			GROUP BY tcdt.SoHopDong, tcdt.HopDongID,tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmWebsiteREF, tcdt.TenWebsite
			)A
			INNER JOIN 
			(
				SELECT hd.HopDongID, hdct.DonGia, hdct.ChietKhau
				  FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				WHERE hd.HopDongID IN  (22943,
										24028,
										20701,
										17633,
										22425,
										22622,
										21482,
										24044,
										21691)
										AND hdct.DmSanPhamREF = 339
										
			)B ON A.HopDongID = b.HopDongID
			WHERE a.SoLuongThucChay >0

	
	OPEN Record_Cursor_TCDT1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_TCDT1 INTO @DmWebsiteREF, @TenWebsite,@HopDongChiTietID, @HopDongREF, @SoHopDong, @DmSanPhamREF, @TenSanPham, @GiaTriThayDoi
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT 'vao roi'
	    SET @CONTENT_DETAIL_LOG = N'Giá trị thay đổi:' + CONVERT(NVARCHAR(30), CONVERT(BIGINT, @GiaTriThayDoi))
	        + '; Website:' + @TenWebsite
	    
	    PRINT @CONTENT_DETAIL_LOG
	    	    
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
	        --EXEC ThucChay_InsertThucTreoThayDoi_CPM @HopDongChiTietID,
	        --         @NgayThucHien,
	        --         @GiaTriThayDoi,
	        --         @DmWebsiteREF,
	        --         @TenWebsite
	        --//Update khi HopDongChiTietID = 0
	        EXEC [ThucChay_InsertThucTreoThayDoiPPSP_CPM] @HopDongREF, @DmSanPhamREF,@TenSanPham, @NgayThucHien, @GiaTriThayDoi,@DmWebsiteREF, @TenWebsite
	        --//Update khi HopDongChiTietID !=0
	        --EXEC  ThucChay_InsertThucTreoThayDoiSP_CPM @HopDongChiTietID, @DmSanPhamREF,@TenSanPham, @NgayThucHien, @GiaTriThayDoi,@DmWebsiteREF, @TenWebsite
	    FETCH NEXT FROM Record_Cursor_TCDT1 INTO @DmWebsiteREF, @TenWebsite,@HopDongChiTietID, @HopDongREF, @SoHopDong, @DmSanPhamREF, @TenSanPham, @GiaTriThayDoi
	END
	CLOSE Record_Cursor_TCDT1
	DEALLOCATE Record_Cursor_TCDT1
	SELECT 1
END

```
