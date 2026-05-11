# Stored Procedure: `ThucChay_UpdateGiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-15 15:46:49.313000
- **Ngày sửa cuối**: 2015-06-05 01:13:33.220000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongid` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoi] '2015-05-16'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoi] 
-- Add the parameters for the stored procedure here
	@HopDongid INT,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT,
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @IsExistHDCT INT
			
		
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
	DECLARE @ThanhTienTC float	        
	
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
	SET @ThanhTienTC = 0
	SET @SoLuongThucChay = 0
	PRINT @SoHopDong
	PRINT @DmSanPhamREF
	
	DECLARE Record_Cursor_TCDT1 CURSOR  FOR
	--CAU LENH NAY SU DUNG CHO VIEC LAY DU LIEU DE UPDATE
		
		--	select DmWebsiteREF, TenWebsite, HopDOngChiTietREF
		--, HopDongID,SoHopDong, DmSanPhamREF, TenSanPham
		--,sum(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) thanhtienthucchay
		--,sum(SoLuongThucChay) soluongthucchay
		-- from ABM_Phuongtt.dbo.[ThucChayDaTinh]  
		-- where SoHopDong = 'NB100315'
		-- AND HopDongID = 33331
		-- --AND HopDongChiTietREF = 65515
		--AND DmSanPhamREF = 613
		----AND YEAR(NgayThucHien) = 2015
		----AND TrangThaiHopDong <> 3
		--Group by DmWebsiteREF, TenWebsite, HopDOngChiTietREF, HopDongID,SoHopDong, DmSanPhamREF, TenSanPham
		
		-- cau lenh update gia tri 31/12/2014
			    SELECT b.DmWebsiteREF,
	           b.TenWebsite,
	           b.HopDongChiTietREF,
	           b.HopDongID,
	           b.SoHopDong,
	           b.DmSanPhamREF,
	           b.TenSanPham,
	           (ISNULL(a.thanhtientc, 0) - ISNULL(b.thanhtientc, 0))
	           ThanhTienLech,
	           (
	               ISNULL(a.SoLuongThucChay, 0) - ISNULL(b.SoLuongThucChay, 0)
	           ) SoLuongLech
	    FROM   (
	               SELECT dwr.DmWebsiteReportingdbID DmWebsiteREF,
	                      tcdt.TenWebsite
	                      , tcdt.HopDongChiTietREF 
	                      ,
	                      tcdt.HopDongID,
	                      tcdt.SoHopDong,
	                      tcdt.DmSanPhamREF,
	                      tcdt.TenSanPham,
	                      SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) 
	                      thanhtientc,
	                      SUM(tcdt.SoLuongThucChay)SoLuongThucChay
	               FROM   ABM_Data_Release_Test.dbo.ThucChayDaTinh tcdt
	                      LEFT JOIN DmWebsiteReportingdb dwr
	                           ON  dwr.TenWebsite = tcdt.TenWebsite
	               WHERE  1 = 1
	                       AND (((tcdt.HopDongID = @HopDongId) AND (tcdt.DmSanPhamREF = @DmSanPhamREF)))
	                           AND tcdt.HopDongChiTietREF =@HopDongChiTietID
	               GROUP BY
	                      tcdt.HopDongID,
	                      tcdt.SoHopDong,
	                      tcdt.HopDongChiTietREF,
	                      tcdt.DmSanPhamREF,
	                      tcdt.TenSanPham,
	                      dwr.DmWebsiteReportingdbID,
	                      tcdt.TenWebsite
	           )a
	           right JOIN (
	                    SELECT tcdt.DmWebsiteREF,
	                           tcdt.TenWebsite,
	                           tcdt.HopDongID,
	                           tcdt.SoHopDong,
	                           tcdt.DmSanPhamREF,
	                           tcdt.TenSanPham
	                           	, tcdt.HopDongChiTietREF
	                           ,
	                           SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) 
	                           thanhtientc,
	                           SUM(tcdt.SoLuongThucChay)SoLuongThucChay
	                    FROM   ABM_Data_Release.dbo.ThucChayDaTinh tcdt
	                    WHERE  
	                            tcdt.TrangThaiHopDong <> 3
	                           AND tcdt.DmHinhThucQuangCao <> 13
	                            AND (((tcdt.HopDongID = @HopDongId) AND (tcdt.DmSanPhamREF = @DmSanPhamREF)))
	                           AND tcdt.HopDongChiTietREF =@HopDongChiTietID
	                    GROUP BY
	                           tcdt.HopDongID,
	                           tcdt.SoHopDong,
	                           tcdt.HopDongChiTietREF,
	                           tcdt.DmSanPhamREF,
	                           tcdt.TenSanPham,
	                           tcdt.DmWebsiteREF,
	                           tcdt.TenWebsite
	                )b
	                ON  a.HopDongID = b.HopDongID
	                AND a.hopdongchitietREF = B.HopDongChiTietREF
	                AND b.DmSanPhamREF = a.DmSanPhamREF
	                AND a.TenWebsite = b.TenWebsite
	              WHERE  1 = 1


	OPEN Record_Cursor_TCDT1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_TCDT1 INTO @DmWebsiteREF, @TenWebsite,@HopDongChiTietID
	, @HopDongid, @SoHopDong, @DmSanPhamREF, @TenSanPham, @GiaTriThayDoi, @SoLuongThucChayByWebiste
	
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
	            @HopDongid,
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
	          
	    
	        --HAM NAY SU DUNG CHO TRUONG HOP UPDATE LAI GIA TRI THAY DOI VOI HOPDONGCHITIET <> 0
			SET @IsExistHDCT =
			(
				SELECT COUNT(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct
				WHERE hdct.DeletedStatus = 0
				AND hdct.HopDongChiTietID = @HopDongChiTietID
			)
			IF(@IsExistHDCT >0)
			begin
				--select @ThanhTienTC = sum(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
				--, @SoLuongThucChay = sum(SoLuongThucChay) 
				-- from [ThucChayDaTinh]  
				-- where SoHopDong = 'NB100315'
				--and DmSanPhamREF = 613
				----AND YEAR(ngaythuchien) = 2015
				----AND HopDongChiTietREF = 65515
				--and HopDongID = @HopDongREF
				--and HopDongChiTietREF = @HopDongChiTietID
				--and DmWebsiteREF = @DmWebsiteREF
				
				--set @GiaTriThayDoi = @GiaTriThayDoi - ISNULL(@ThanhTienTC,0)
				--set @SoLuongThucChayByWebiste = @SoLuongThucChayByWebiste - ISNULL(@SoLuongThucChay,0)
				
				EXEC  ThucChay_InsertThucTreoThayDoiSP_CPM @HopDongChiTietID
				, @DmSanPhamREF,@TenSanPham, @NgayThucHien, @GiaTriThayDoi,@DmWebsiteREF, @TenWebsite, @SoLuongThucChayByWebiste
			end			
			ELSE
				EXEC  ThucChay_InsertThucChayDaTinh_CPM_PboXoa @HopDongChiTietID, @DmSanPhamREF,@TenSanPham, @NgayThucHien, @GiaTriThayDoi,@DmWebsiteREF, @TenWebsite, @SoLuongThucChayByWebiste				
	    FETCH NEXT FROM Record_Cursor_TCDT1 INTO @DmWebsiteREF, @TenWebsite,@HopDongChiTietID, @HopDongid, @SoHopDong, @DmSanPhamREF, @TenSanPham, @GiaTriThayDoi, @SoLuongThucChayByWebiste
	END
	CLOSE Record_Cursor_TCDT1
	DEALLOCATE Record_Cursor_TCDT1
	SELECT 1
END

```
