# Stored Procedure: `ThucChayDaTinh_GG_FB_UpdateGiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:25.930000
- **Ngày sửa cuối**: 2015-05-05 18:14:59.743000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-24
-- Description:	<Description,,>
-- =============================================
/*

	EXEC dbo.ThucChayDaTinh_GG_FB_UpdateGiaTriThayDoi '2014-12-30'

 */
CREATE PROCEDURE [dbo].[ThucChayDaTinh_GG_FB_UpdateGiaTriThayDoi] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE	@HopDongREF INT,
			@SoHopDong NVARCHAR(50),
			@HopDongChiTietID INT,
			@DonViTinh			NVARCHAR(50),
			@account			NVARCHAR(50),
			@DotChayHopDong		NVARCHAR(200)
			
	DECLARE @SoLuongDotChayHD INT,
			@ThanhTienHDCT FLOAT, 
			@DmSanPhamREF	INT,
			@TenSanPham		NVARCHAR(50)
			
	DECLARE 
			@count_HDCT INT, 
			@SoLuongThucChayBF INT
			
	DECLARE @SoLuongCurrent	INT,
			@DonGiaCurrent	INT,
			@ChietKhauCurrent	INT,
			@ThanhTienCurrent	FLOAT,
			@DeltaValue			FLOAT,
			@GiaTriThayDoiByWebsite	FLOAT,
			@GiaTriThayDoi		FLOAT = 0,
			@SoLuongThayDoi		BIGINT,
			@DonViTinhCurrent	NVARCHAR(50)
	
	DECLARE @SoLuongOld	INT,
			@DonGiaOld	INT,
			@ChietKhauOld	INT,
			@ThanhTienOld	FLOAT,
			@DonGiaTheoDonViTinh FLOAT	
	
	DECLARE @NgayThayDoiMax	DATETIME,
			@HopDongThayDoiREFMax INT	
	
	DECLARE @Count INT,
			@ThucChayTheoSite FLOAT,
			@Tyle				FLOAT,
			@TongTienThucChay	FLOAT,
			@TongSoLuongThucChay BIGINT
		
	DECLARE @NoiDungLog			NVARCHAR(MAX),
			@GhiChu				NVARCHAR(MAX)
			
	DECLARE @GiaTriHopDong		FLOAT,
			@GiaTriThucChay	FLOAT
		
	DECLARE @MaHopDongId				INT,
			@TenMaHopDong			NVARCHAR(50)	
			
	DECLARE @DmWebsiteREF	INT,
			@TenWebsite		NVARCHAR(50),
			@GiaTriThayDoiChiPhi	FLOAT,
			@ThucChayChiPhi			FLOAT,
			@GiaTriPhanBoChiPhi		FLOAT,
			@phanBoChiPhiId	INT,
			@sanPhamChiPhiId	NVARCHAR(50),
			@tenSanPhamChiPhi NVARCHAR(50),
			@donViTinhChiPhi	NVARCHAR(50),
			@thanhTienPhanBoChiPhi	FLOAT
			
	DECLARE @websiteIdThucChay INT = 0,
			@tenWebsiteThucChay nvarchar(50) = '',
			@type				nvarchar(50) = ''
				

	PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
	SET @count_HDCT = 0
	SET @SoLuongThucChayBF = 0
	
	
	DECLARE Record_Cursor_UpDate CURSOR FOR 
    
	SELECT 
		T1.HopDongID, T1.SoHopDong, T1.HopDongChiTietID, T1.DmSanPhamREF, T1.TenSanPham, T1.DonViTinh,
		T1.DmMaHopDongREF, T1.TenMaHopDong, T1.HopDongThayDoiID,
		T1.ThanhTien
		,T2.ThanhTienThucChay
	FROM
	(
		SELECT
			A.HopDongID, A.SoHopDong, B.HopDongChiTietID, B.DmSanPhamREF, B.TenSanPham, B.DonViTinh,
			A.DmMaHopDongREF, A.TenMaHopDong,
			(SELECT MAX(hdtd.HopDongThayDoiID) FROM HopDongThayDoi hdtd WHERE hdtd.HopDongFK = A.HopDongID) HopDongThayDoiID,
			--B.TK_AdMarket,	
			B.ThanhTien
		FROM HopDong A
			INNER JOIN HopDongChiTiet B ON B.HopDongFK = A.HopDongID
		WHERE 1=1
			AND A.TrangThaiHopDong <> 3
			AND B.DmSanPhamREF IN (306,423,535)
			AND B.DmWebsiteREF IN (285, 307)
			--AND A.SoHopDong = 'QC1631014'			
	)T1	INNER JOIN	
	(	
		SELECT
			C.HopDongID, C.SoHopDong, C.HopDongChiTietREF, C.DmSanPhamREF, C.TenSanPham,
			SUM(C.ThanhTienSauTrietKhauThucChay + C.GiaTriThayDoi) ThanhTienThucChay
		FROM ThucChayDaTinh C
		WHERE 1 = 1
			AND C.TrangThaiHopDong <> 3
			AND C.DmSanPhamREF IN (306,423,535)
			AND C.DmWebsiteREF IN (466, 426)
			AND C.NgayThucHien <= @NgayThucHien
		GROUP BY
			C.HopDongID, C.SoHopDong, C.HopDongChiTietREF, C.DmSanPhamREF, C.TenSanPham
	)T2 ON T2.HopDongChiTietREF = T1.HopDongChiTietID
	WHERE 1=1
		AND T1.ThanhTien < ROUND(T2.ThanhTienThucChay,0)
	
	OPEN Record_Cursor_UpDate

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_UpDate INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham, @DonViTinh, 
										@MaHopDongId, @TenMaHopDong, @HopDongThayDoiREFMax,
										@ThanhTienCurrent, @TongTienThucChay
		
	WHILE @@FETCH_STATUS = 0
		BEGIN
			SELECT @account = TK_Admarket
			FROM HopDongChiTiet AS hdct
			WHERE hdct.HopDongChiTietID = @HopDongChiTietID
			
			IF @DmSanPhamREF = 423
			BEGIN
				SET @DmWebsiteREF = 285;
				SET @websiteIdThucChay = 466;	
				SET @TenWebsite = 'Google';
				SET @tenWebsiteThucChay = 'google.com.vn';
			END
			ELSE
			BEGIN
				SET @DmWebsiteREF = 307;	
				SET @websiteIdThucChay = 426;
				SET @TenWebsite = 'Facebook';
				SET @tenWebsiteThucChay = 'facebook.com';
			END						
			
			PRINT '1: Update gia tri thay doi';
			PRINT '@SoHopDong: ' + CONVERT(NVARCHAR(50), @SoHopDong);
			PRINT '@HopDongREF: ' + CONVERT(NVARCHAR(50), @HopDongREF);
			PRINT '@HopDongThayDoiREFMax: ' + CONVERT(NVARCHAR(50), @HopDongThayDoiREFMax);
			
			SELECT @ThanhTienCurrent = A.ThanhTien,
				@DonViTinhCurrent = A.DonViTinh,
				@account = A.TK_AdMarket,
				@SoLuongCurrent = dbo.ThucChay_GetQuantityThucChay(A.DmSanPhamREF,A.SoLuong,A.DonViTinh)
			FROM HopDongChiTiet A
			WHERE A.HopDongChiTietID = @HopDongChiTietID;
			
			SELECT @ThanhTienOld = A.ThanhTien
			FROM HopDongChiTietThayDoi A			
			WHERE A.HopDongThayDoiREF = @HopDongThayDoiREFMax
				AND A.HopDongChiTietREF = @HopDongChiTietID
				
			PRINT '@ThanhTienCurrent: ' + CONVERT(NVARCHAR(50), @ThanhTienCurrent);
			PRINT '@ThanhTienOld: ' + CONVERT(NVARCHAR(50), @ThanhTienOld);
			
			IF @ThanhTienCurrent <> @ThanhTienOld
			BEGIN
				PRINT 'Hop dong thay doi gia tri'
				PRINT '@DonViTinhCurrent: ' + CONVERT(NVARCHAR(50), @DonViTinhCurrent);
				
				IF @DonViTinhCurrent = N'Gói'
				BEGIN
					PRINT 'GOI'	
					PRINT '@TongTienThucChay: ' + CONVERT(NVARCHAR(50), @TongTienThucChay);
					--XAC DINH PHAN BO NAY DANG CHAY THEO DANG NAO
					PRINT 'Hop dong dieu chinh giam tien'
					SET @GiaTriThayDoi = (@ThanhTienCurrent - @TongTienThucChay);
						
					SELECT TOP 1 @DotChayHopDong = isnull(tcdt.DotChayHopDong,''), @DonGiaTheoDonViTinh = isnull(tcdt.DonGiaTheoDonVi,0)*(100 -isnull(tcdt.ChietKhau,0))/100
					FROM ThucChayDaTinh tcdt
					WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
					ORDER BY tcdt.NgayThucHien DESC
					-- XAC DINH DON GIA
					IF(@DotChayHopDong = 'click' OR @DotChayHopDong = 'page_like')
					BEGIN
						SET @type = @DotChayHopDong
						IF(@DonGiaTheoDonViTinh <>0) 
							SET @SoLuongThayDoi = @GiaTriThayDoi/@DonGiaTheoDonViTinh;
						ELSE
							SET @SoLuongThayDoi = 0;
					END
					ELSE
						BEGIN
							SET @type = 'phi_quan_ly'
							SET @SoLuongThayDoi = 0;
						END
					BEGIN
						SET @GhiChu = N'Update_GTTD, Hop dong thay doi gia tri'
						EXEC dbo.ThucChayDaTinh_GG_FB_InsertGiaTriThayDoi
							@NgayThucHien			= @NgayThucHien,
							@SoHopDong				= @SoHopDong,				
							@PhanBoID				= @HopDongChiTietID,
							@DmSanPhamREF			= @DmSanPhamREF,
							@TenSanPham				= @TenSanPham,							
							@DmWebsiteREF			= @websiteIdThucChay,
							@TenWebsite				= @tenWebsiteThucChay,
							@TongViewThucChay		= 0,
							@TongClickThucChay		= 0,
							@SoLuongThucChay		= @SoLuongThayDoi,
							@ThanhTienThucChay		= @GiaTriThayDoi,
							@SoLuongThucChayKM		= 0,
							@ThanhTienThucChayKM	= 0,
							@DonViTinhSanPham		= 0,
							@GhiChu					= @GhiChu,
							@Type					= @type
							
						-- In sert log gia tri thay doi
						EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
							@HopDongREF
							,@SoHopDong
							,@HopDongChiTietID
							,@DmSanPhamREF
							,0 --@DmWebsiteREF
							,@NgayThucHien
							,@GiaTriThayDoi
							,@DonGiaCurrent
							,@SoLuongCurrent
							,@DonGiaOld
							,@SoLuongOld
							,@NoiDungLog
							,'HopDongChiTiet_Google_Facebook'
							,@GhiChu	
							
						-- Update gia tri online
						INSERT ThucChayGoogleFacebookOnline
						SELECT
							@DmSanPhamREF AS DmSanPhamREF
							,@TenSanPham as TenSanPham
							,@account as TaiKhoan
							,0 as SoNgayChay
							,@SoLuongThayDoi*(-1) as Click
							,@GiaTriThayDoi*(-1) as	ThanhTien
							,@type as Type
							,NEWID() as	ThucChayGoogleFacebookID
							,@NgayThucHien as NgayThucHien
							,GETDATE() as CreatedAt
							,'asd' as CreatedBy
							,GETDATE() as LastModifiedAt
							,'asd' as LastModifiedBy
							,0 as RecordStatus
							,0 as DeletedStatus													
							
					END
				END
				ELSE IF (@DonViTinhCurrent = 'CPC' OR @DonViTinhCurrent = 'CLICK' OR @DonViTinhCurrent = 'LIKE')
				BEGIN
					SET @type = 'click';
					
					SELECT 
						--@TongTienThucChay = ISNULL(SUM(ISNULL(A.ThanhTienSauTrietKhauThucChay,0) + ISNULL(A.GiaTriThayDoi,0)),0),
						@TongSoLuongThucChay = ISNULL(SUM(ISNULL(A.SoLuongThucChay,0) + ISNULL(A.SoLuongThayDoi,0)),0)
					FROM ThucChayDaTinh A
					WHERE 1=1
						AND A.HopDongChiTietREF = @HopDongChiTietID
						AND A.TrangThaiHopDong <> 3
						AND A.DmSanPhamREF = @DmSanPhamREF
						AND A.NgayThucHien <= @NgayThucHien
						AND A.DmWebsiteREF = @websiteIdThucChay
						AND A.DonViTinh = @DonViTinhCurrent
						
					PRINT '@TongSoLuongThucChay: ' + CONVERT(NVARCHAR(50), @TongSoLuongThucChay);
					PRINT '@TongTienThucChay: ' + CONVERT(NVARCHAR(50), @TongTienThucChay);
					
					IF @TongSoLuongThucChay > @SoLuongCurrent
					BEGIN
						PRINT 'Hop dong thay doi giam '
						SET @SoLuongThayDoi = (@SoLuongCurrent - @TongSoLuongThucChay);
						SET @GiaTriThayDoi = (@ThanhTienCurrent - @TongTienThucChay);						
						
						SET @GhiChu = N'Update_GTTD, Hop dong thay doi gia tri'
						EXEC dbo.ThucChayDaTinh_GG_FB_InsertGiaTriThayDoi
							@NgayThucHien			= @NgayThucHien,
							@SoHopDong				= @SoHopDong,				
							@PhanBoID				= @HopDongChiTietID,
							@DmSanPhamREF			= @DmSanPhamREF,
							@TenSanPham				= @TenSanPham,							
							@DmWebsiteREF			= @websiteIdThucChay,
							@TenWebsite				= @tenWebsiteThucChay,
							@TongViewThucChay		= 0,
							@TongClickThucChay		= 0,
							@SoLuongThucChay		= @SoLuongThayDoi,
							@ThanhTienThucChay		= @GiaTriThayDoi,
							@SoLuongThucChayKM		= 0,
							@ThanhTienThucChayKM	= 0,
							@DonViTinhSanPham		= 0,
							@GhiChu					= @GhiChu,
							@Type					= @type
							
						-- In sert log gia tri thay doi
						EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
							@HopDongREF
							,@SoHopDong
							,@HopDongChiTietID
							,@DmSanPhamREF
							,0 --@DmWebsiteREF
							,@NgayThucHien
							,@GiaTriThayDoi
							,@DonGiaCurrent
							,@SoLuongCurrent
							,@DonGiaOld
							,@SoLuongOld
							,@NoiDungLog
							,'HopDongChiTiet_Google_Facebook'
							,@GhiChu	
							
						-- Update gia tri online
						INSERT ThucChayGoogleFacebookOnline
						SELECT
							@DmSanPhamREF AS DmSanPhamREF
							,@TenSanPham as TenSanPham
							,@account as TaiKhoan
							,0 as SoNgayChay
							,@SoLuongThayDoi*(-1) as Click
							,@GiaTriThayDoi*(-1) as	ThanhTien
							,'chi_phi' as Type
							,NEWID() as	ThucChayGoogleFacebookID
							,@NgayThucHien as NgayThucHien
							,GETDATE() as CreatedAt
							,'asd' as CreatedBy
							,GETDATE() as LastModifiedAt
							,'asd' as LastModifiedBy
							,0 as RecordStatus
							,0 as DeletedStatus
					END
				END
				ELSE IF (@DonViTinhCurrent = N'Ngày' OR @DonViTinhCurrent = N'Tuần' OR @DonViTinhCurrent = N'Tháng' OR @DonViTinhCurrent = N'Năm')
				BEGIN
					SELECT @TongTienThucChay = ISNULL(SUM(ISNULL(A.ThanhTienSauTrietKhauThucChay,0) + ISNULL(A.GiaTriThayDoi,0)),0),
						@TongSoLuongThucChay = ISNULL(SUM(ISNULL(A.SoLuongThucChay,0) + ISNULL(A.SoLuongThayDoi,0)),0)
					FROM ThucChayDaTinh A
					WHERE 1=1
						AND A.HopDongChiTietREF = @HopDongChiTietID
						AND A.TrangThaiHopDong <> 3
						AND A.DmSanPhamREF = @DmSanPhamREF
						AND A.NgayThucHien <= @NgayThucHien
						AND A.DonViTinh = @DonViTinhCurrent
						
					PRINT '@TongSoLuongThucChay: ' + CONVERT(NVARCHAR(50), @TongSoLuongThucChay);
					PRINT '@TongTienThucChay: ' + CONVERT(NVARCHAR(50), @TongTienThucChay);
					
					SELECT @TongTienThucChay = ISNULL(SUM(ISNULL(A.ThanhTienSauTrietKhauThucChay,0) + ISNULL(A.GiaTriThayDoi,0)),0),
						@TongSoLuongThucChay = ISNULL(SUM(ISNULL(A.SoLuongThucChay,0) + ISNULL(A.SoLuongThayDoi,0)),0)
					FROM ThucChayDaTinh A
					WHERE 1=1
						AND A.HopDongChiTietREF = @HopDongChiTietID
						AND A.TrangThaiHopDong <> 3
						AND A.DmSanPhamREF = @DmSanPhamREF
						AND A.NgayThucHien <= @NgayThucHien
						AND A.DonViTinh = @DonViTinhCurrent
						
					PRINT '@TongSoLuongThucChay: ' + CONVERT(NVARCHAR(50), @TongSoLuongThucChay);
					PRINT '@TongTienThucChay: ' + CONVERT(NVARCHAR(50), @TongTienThucChay);
					
					IF @TongSoLuongThucChay > @SoLuongCurrent
					BEGIN
						PRINT 'Hop dong thay doi giam '
						SET @SoLuongThayDoi = (@SoLuongCurrent - @TongSoLuongThucChay);
						SET @GiaTriThayDoi = (@ThanhTienCurrent - @TongTienThucChay);
						SET @type = 'thoi_gian'
						
						SET @GhiChu = N'Update_GTTD, Hop dong thay doi gia tri'
						EXEC dbo.ThucChayDaTinh_GG_FB_InsertGiaTriThayDoi
							@NgayThucHien			= @NgayThucHien,
							@SoHopDong				= @SoHopDong,				
							@PhanBoID				= @HopDongChiTietID,
							@DmSanPhamREF			= @DmSanPhamREF,
							@TenSanPham				= @TenSanPham,							
							@DmWebsiteREF			= @websiteIdThucChay,
							@TenWebsite				= @tenWebsiteThucChay,
							@TongViewThucChay		= 0,
							@TongClickThucChay		= 0,
							@SoLuongThucChay		= @SoLuongThayDoi,
							@ThanhTienThucChay		= @GiaTriThayDoi,
							@SoLuongThucChayKM		= 0,
							@ThanhTienThucChayKM	= 0,
							@DonViTinhSanPham		= 0,
							@GhiChu					= @GhiChu,
							@Type					= @type
							
						-- In sert log gia tri thay doi
						EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
							@HopDongREF
							,@SoHopDong
							,@HopDongChiTietID
							,@DmSanPhamREF
							,0 --@DmWebsiteREF
							,@NgayThucHien
							,@GiaTriThayDoi
							,@DonGiaCurrent
							,@SoLuongCurrent
							,@DonGiaOld
							,@SoLuongOld
							,@NoiDungLog
							,'HopDongChiTiet_Google_Facebook'
							,@GhiChu	
							
						-- Update gia tri online
						INSERT ThucChayGoogleFacebookOnline
						SELECT
							@DmSanPhamREF AS DmSanPhamREF
							,@TenSanPham as TenSanPham
							,@account as TaiKhoan
							,0 as SoNgayChay
							,@SoLuongThayDoi*(-1) as Click
							,@GiaTriThayDoi*(-1) as	ThanhTien
							,'chi_phi' as Type
							,NEWID() as	ThucChayGoogleFacebookID
							,@NgayThucHien as NgayThucHien
							,GETDATE() as CreatedAt
							,'asd' as CreatedBy
							,GETDATE() as LastModifiedAt
							,'asd' as LastModifiedBy
							,0 as RecordStatus
							,0 as DeletedStatus
					END
				END	
			END

			
			FETCH NEXT FROM Record_Cursor_UpDate INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham, @DonViTinh, 
												@MaHopDongId, @TenMaHopDong, @HopDongThayDoiREFMax,
												@ThanhTienCurrent, @TongTienThucChay
		END
	CLOSE Record_Cursor_UpDate
	DEALLOCATE Record_Cursor_UpDate
	
	
	
	---- Check xem co hop dong huy hay khong	
	
	DECLARE @HopDongHuyId				INT,
			@SoHopDongHuy				NVARCHAR(50),
			@PhanBoHuyId				INT,
			@SanPhamHuyId				INT,
			@TenSanPhamHuy				NVARCHAR(50),
			@SoLuongThayDoiThucChay		BIGINT,
			@ThanhTienThayDoiThucChay	FLOAT,
			@DonViTinhHuy				NVARCHAR(50),
			@MaHopDongHuyId				INT,
			@TenMaHopDongHuy			NVARCHAR(50),
			@TongSoLuongHuy				INT = 0
	
	DECLARE hd_cursor CURSOR FOR --GG011214
	
	SELECT 
		T1.HopDongID, T1.SoHopDong, T1.HopDongChiTietID, T1.DmSanPhamREF, T1.TenSanPham, 
		T1.DmMaHopDongREF, T1.TenMaHopDong, 
		T1.ThanhTien
		,T2.ThanhTienThucChay, T2.TongSoLuongHuy,
		T2.DmWebsiteREF, T2.TenWebsite
	FROM
	(
		SELECT
			A.HopDongID, A.SoHopDong, B.HopDongChiTietID, B.DmSanPhamREF, B.TenSanPham,
			A.DmMaHopDongREF, A.TenMaHopDong,			
			--B.TK_AdMarket,	
			B.ThanhTien
		FROM HopDong A
			INNER JOIN HopDongChiTiet B ON B.HopDongFK = A.HopDongID
		WHERE 1=1
			AND A.TrangThaiHopDong = 3
			AND B.DmSanPhamREF IN (306,423,535)
			AND B.DmWebsiteREF IN (285, 307)
			--AND A.SoHopDong = 'GG011214'			
	)T1	INNER JOIN	
	(	
		SELECT
			C.HopDongID, C.SoHopDong, C.HopDongChiTietREF, C.DmSanPhamREF, C.TenSanPham,
			C.DmWebsiteREF, C.TenWebsite,
			SUM(C.ThanhTienSauTrietKhauThucChay + C.GiaTriThayDoi) ThanhTienThucChay,
			SUM(C.SoLuongThucChay + C.SoLuongThayDoi) TongSoLuongHuy
		FROM ThucChayDaTinh C
		WHERE 1 = 1
			AND C.TrangThaiHopDong <> 3
			AND C.DmSanPhamREF IN (306,423,535)
			AND C.DmWebsiteREF IN (466, 426)
			AND C.NgayThucHien <= @NgayThucHien
		GROUP BY
			C.HopDongID, C.SoHopDong, C.HopDongChiTietREF, C.DmSanPhamREF, C.TenSanPham,
			C.DmWebsiteREF, C.TenWebsite
	)T2 ON T2.HopDongChiTietREF = T1.HopDongChiTietID
	WHERE 1=1
		AND T2.ThanhTienThucChay > 0
	
	OPEN hd_cursor
	FETCH NEXT FROM hd_cursor INTO @HopDongHuyId, @SoHopDongHuy, @PhanBoHuyId, @SanPhamHuyId, @TenSanPhamHuy, @MaHopDongHuyId, @TenMaHopDongHuy,
									@ThanhTienCurrent, @TongTienThucChay, @TongSoLuongHuy, @WebsiteIdThucChay, @TenWebsiteThucChay
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT '2: Update gia tri thay doi by hop dong huy';
		
		SELECT @account = TK_Admarket
		FROM HopDongChiTiet AS hdct
		WHERE hdct.HopDongChiTietID = @PhanBoHuyId
	
		SET @ThanhTienThayDoiThucChay = ((-1)*@TongTienThucChay);
		SET @SoLuongThayDoiThucChay = ((-1)*@TongSoLuongHuy);
		
		PRINT '@ThanhTienThayDoiThucChay: ' + cast(@ThanhTienThayDoiThucChay as nvarchar(50))
		
		SET @type = ''
		SET @GhiChu = 'HUY_HOPDONG'
		
		-- Insert gia tri thay doi
		EXEC dbo.ThucChayDaTinh_GG_FB_InsertGiaTriThayDoi
			@NgayThucHien			= @NgayThucHien,
			@SoHopDong				= @SoHopDongHuy,				
			@PhanBoID				= @PhanBoHuyId,
			@DmSanPhamREF			= @SanPhamHuyId,
			@TenSanPham				= @TenSanPhamHuy,							
			@DmWebsiteREF			= @websiteIdThucChay,
			@TenWebsite				= @tenWebsiteThucChay,
			@TongViewThucChay		= 0,
			@TongClickThucChay		= 0,
			@SoLuongThucChay		= @SoLuongThayDoiThucChay,
			@ThanhTienThucChay		= @ThanhTienThayDoiThucChay,
			@SoLuongThucChayKM		= 0,
			@ThanhTienThucChayKM	= 0,
			@DonViTinhSanPham		= 0,
			@GhiChu					= @GhiChu,
			@Type					= @type
			
		-- Insert Log gia tri thay doi
		PRINT 'Log: ' + @NoiDungLog;
		EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
			@HopDongHuyId
			,@SoHopDongHuy
			,@PhanBoHuyId
			,@DmSanPhamREF
			,0
			,@NgayThucHien
			,@ThanhTienThayDoiThucChay
			,0
			,0
			,0
			,0
			,'Update Gia tri thay doi cho hop dong Huy'
			,'HopDongChiTiet_Admarket_HopDongHuy'
			,''							
					
		FETCH NEXT FROM hd_cursor INTO @HopDongHuyId, @SoHopDongHuy, @PhanBoHuyId, @SanPhamHuyId, @TenSanPhamHuy, @MaHopDongHuyId, @TenMaHopDongHuy,
										@ThanhTienCurrent, @TongTienThucChay, @TongSoLuongHuy, @WebsiteIdThucChay, @TenWebsiteThucChay
	END
	
	CLOSE hd_cursor;
	DEALLOCATE hd_cursor; 
		
	SELECT 2
END


```
