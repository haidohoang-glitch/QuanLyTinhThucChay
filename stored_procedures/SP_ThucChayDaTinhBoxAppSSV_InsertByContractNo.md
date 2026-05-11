# Stored Procedure: `ThucChayDaTinhBoxAppSSV_InsertByContractNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:28:00.100000
- **Ngày sửa cuối**: 2016-03-17 09:28:00.100000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCao` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-24
-- Description:	Phan bo thuc chay BoxappSSV theo hop dong
-- =============================================
--
-- EXEC dbo.ThucChayDaTinhBoxAppSSV_InsertByContractNo '2014-11-12','QC2851014', 26, 370,'Box App', 182,'suckhoedoisong.vn'

CREATE PROCEDURE [dbo].[ThucChayDaTinhBoxAppSSV_InsertByContractNo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien		DATETIME,
	@SoHopDong			NVARCHAR(50),
	@DmHinhThucQuangCao	INT,
	@DmSanPhamREF		INT,
	@TenSanPham			NVARCHAR(50),
	@DmWebsiteREF		INT,
	@TenWebsite			NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	PRINT 'WebsiteID: ' + CONVERT(NVARCHAR(50), @DmWebsiteREF);
	
	DECLARE @TenBannerList	NVARCHAR(MAX);
	SET @TenBannerList = '''300x250'',''300x385'''
	
	DECLARE @SoLuongHopDong		INT = 0,
			@ThanhTienHopDong	FLOAT = 0,
			@SoLuongHopDongKM	INT = 0,
			@ThanhTienHopDongKM	FLOAT = 0,
			@DonViTinhPhanBo	NVARCHAR(50),
			@PhanBoID			INT,
			@HopDongID			INT,
			@SoLuongPhanBo		INT,
			@ThanhTienPhanBo	FLOAT,
			@SoLuongPhanBoKM	INT,
			@ThanhTienPhanBoKM	FLOAT
			
	DECLARE @SoLuongThucChayHopDong		INT = 0,
			@ThanhTienThucChayHopDong	FLOAT = 0,
			@SoLuongThucChayHopDongKM	INT = 0,
			@ThanhTienThucChayHopDongKM	FLOAT = 0
			
	DECLARE	@TongSoLuongThucChayTichLuy		INT = 0,
			@TongThanhTienThucChayTichLuy	FLOAT = 0,
			@TongSoLuongThucChayKMTichLuy	INT = 0,
			@TongThanhTienThucChayKMTichLuy	FLOAT = 0,
			@TongSoLuongThucChayTichLuyTheoPhanBo INT = 0,
			@TongThanhTienThucChayTichLuyTheoPhanBo FLOAT = 0,
			@TongSoLuongThucChayKMTichLuyTheoPhanBo	INT = 0,
			@TongThanhTienThucChayKMTichLuyTheoPhanBo	FLOAT = 0
			
	DECLARE @TongSoLuongThucChaySanPham INT = 0,
			@SoLuongThucChaySanPham		INT = 0,
			@ThanhTienThucChaySanPham	FLOAT = 0,
			@SoLuongThucChaySanPhamKM	INT = 0,
			@ThanhTienThucChaySanPhamKM FLOAT = 0,
			@TyLeThucChay				FLOAT = 0,
			@TyLeKhuyenMai				FLOAT = 0,
			@TongViewThucChay			INT,
			@TongClickThucChay			INT,
			@TypeInsert					INT,
			@IsPPSanPham				INT
			
	DECLARE @SoLuongThucChay		INT = 0,
			@ThanhTienThucChay		FLOAT = 0,
			@SoLuongThucChayKM		INT = 0,
			@ThanhTienThucChayKM	FLOAT = 0,
			@SoLuongLechTreoHa		INT = 0,
			@ThanhTienLechTreoHa	FLOAT = 0
			
	-- Select So luong, Thanh tien thuc chay tu he thong san pham
	SELECT 
		@TongSoLuongThucChaySanPham		= ISNULL(SUM(A.SoLuongThucChay),0),
		@ThanhTienThucChaySanPham	= ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay),0),
		@SoLuongThucChaySanPhamKM   = ISNULL(SUM(A.SoLuongThucChayKM),0),
		@ThanhTienThucChaySanPhamKM = ISNULL(SUM(A.ThanhTienKM),0),
		@TongClickThucChay			= ISNULL(SUM(A.TongClickThucChay),0),
		@TongViewThucChay			= ISNULL(SUM(A.TongViewThucChay),0)
	FROM ThucChayDaTinhBoxAppSSV A
	WHERE
		A.NgayThucHien				= @NgayThucHien
		AND A.DmSanPhamREF			= @DmSanPhamREF
		AND A.DmHinhThucQuangCao	= @DmHinhThucQuangCao
		AND A.DmWebsiteREF			= @DmWebsiteREF
		AND A.SoHopDong				= @SoHopDong

	PRINT 'SoHopDong: ' + @SoHopDong;
	PRINT '@ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
	PRINT '@ThanhTienThucChaySanPhamKM: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPhamKM);
	
	-- truong hop co so luong nhung khong co tien thi se insert so luong vao bang online
	IF(@ThanhTienThucChaySanPham = 0
		AND @ThanhTienThucChaySanPhamKM = 0
		AND @SoLuongThucChaySanPham = 0
		AND @SoLuongThucChaySanPhamKM = 0)
	BEGIN
		INSERT INTO ThucChayBoxAppSSVOnline
		SELECT 
			NEWID()
			,@SoHopDong
			,@DmSanPhamREF
			,@TenSanPham
			,@DmWebsiteREF
			,@TenWebsite
			,'View' DonViTinh
			,@TongSoLuongThucChaySanPham SoLuongThucChay
			,0 ThanhTienThucChay
			,0 SoLuongKhuyenMai
			,0 ThanhTienKhuyenMai
			,@NgayThucHien
			,'' GhiChu
			,GETDATE() CreatedAt
			,'asd' CreatedBy
			,GETDATE() LastModifiedAt
			,'asd' LastModifiedBy
			,1 RecordStatus
	END

	IF (@ThanhTienThucChaySanPham > 0 OR @ThanhTienThucChaySanPhamKM > 0)
	BEGIN
		SET @TyLeThucChay = (@ThanhTienThucChaySanPham/(@ThanhTienThucChaySanPham + @ThanhTienThucChaySanPhamKM))
		SET @TyLeKhuyenMai = (@ThanhTienThucChaySanPhamKM/(@ThanhTienThucChaySanPham + @ThanhTienThucChaySanPhamKM))
	END
	ELSE
	BEGIN
		SET @TyLeThucChay = 0;
		SET @TyLeKhuyenMai = 0;
	END

	SET @SoLuongThucChaySanPham = ROUND(@TyLeThucChay*@TongSoLuongThucChaySanPham,0);
	SET @SoLuongThucChaySanPhamKM = ROUND(@TyLeKhuyenMai*@TongSoLuongThucChaySanPham,0);

	PRINT '@@TongSoLuongThucChaySanPham: ' + CONVERT(NVARCHAR(50), @TongSoLuongThucChaySanPham);
		
	PRINT '@SoLuongThucChaySanPham: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySanPham);	
	PRINT '@SoLuongThucChaySanPhamKM: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySanPhamKM);	
	
	IF (@ThanhTienThucChaySanPham > 0 OR @SoLuongThucChaySanPham > 0)
	BEGIN
		-- Seelct SoLuong, ThanhTien  theo hop dong
		SELECT 
			@SoLuongHopDong = ISNULL(SUM(hdct.SoLuong*1000),0),
			@ThanhTienHopDong = ISNULL(SUM(hdct.ThanhTien),0)
		FROM HopDong AS hd
			INNER JOIN HopDongChiTiet AS hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE
			hd.SoHopDong = @SoHopDong
			AND hd.TrangThaiHopDong <> 3
			AND hdct.DmSanPhamREF = @DmSanPhamREF
			AND (hdct.DmLoaiREF = @DmHinhThucQuangCao
					OR hdct.TenViTri IN ('300x250','300x385'))
			AND hdct.DeletedStatus = 0
			AND hdct.IsKhuyenMai <> 1
			AND hdct.DmLoaiREF <> 13 -- Mua Ngoai
			
		PRINT '@SoLuongHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongHopDong);
		PRINT '@ThanhTienHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienHopDong);
		
		IF EXISTS(
					SELECT HopDongChiTietREF 
					FROM ThucChayDaTinh AS tcdt 
					WHERE tcdt.SoHopDong = @SoHopDong AND tcdt.HopDongChiTietREF = 0
					UNION ALL
					SELECT HopDongChiTietREF 
					FROM ThucChayDaTinhAdmarket AS tcdtadk 
					WHERE tcdtadk.SoHopDong = @SoHopDong AND tcdtadk.HopDongChiTietREF = 0
				  )
			SET @IsPPSanPham = 1;
		ELSE
			SET @IsPPSanPham = 0;
			
		PRINT '@IsPPSanPham: ' + CONVERT(NVARCHAR(50), @IsPPSanPham);
					
		DECLARE tc_cursor CURSOR FOR
		SELECT hd.HopDongID, hdct.HopDongChiTietID, 
			CASE hdct.DonViTinhREF
				WHEN 1 THEN hdct.SoLuong*1000 -- 1 CPM = 1000 View
				ELSE hdct.SoLuong
			END AS SoLuong, 
			hdct.DonViTinh, hdct.ThanhTien
		FROM HopDong AS hd
			INNER JOIN HopDongChiTiet AS hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE
			hd.SoHopDong = @SoHopDong
			AND hdct.DmSanPhamREF = @DmSanPhamREF
			AND (hdct.DmLoaiREF = @DmHinhThucQuangCao
					OR hdct.TenViTri IN ('300x250','300x385'))
			AND hdct.DeletedStatus = 0
			AND hdct.IsKhuyenMai <> 1	
			AND hdct.DmLoaiREF <> 13		
		OPEN tc_cursor
	
		FETCH NEXT FROM tc_cursor INTO @HopDongID, @PhanBoID, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienPhanBo 
		WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT 'SoLuongThucChaySanPham: ' + CONVERT(NVARCHAR(50),@SoLuongThucChaySanPham);
			PRINT 'ThanhTienThucCHaySanPham: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChaySanPham);
			
			PRINT 'PhanBoID: ' + CONVERT(NVARCHAR(50),@PhanBoID);
			PRINT '@SoLuongPhanBo: ' + CONVERT(NVARCHAR(50),@SoLuongPhanBo);
			IF (@IsPPSanPham = 1) -- PP San pham
			BEGIN
				PRINT 'PP SanPham: 1';
				-- Select SoLuong, ThanhTien thuc chay tich luy theo hop dong
				SELECT 
					@TongSoLuongThucChayTichLuy = SUM(C.SoLuongThucChay),				
					@TongThanhTienThucChayTichLuy = SUM(C.ThanhTienThucChaySauTrietKhau)				
				FROM
				(	
					SELECT 
						ISNULL(SUM(A.SoLuongThucChay),0) AS SoLuongThucChay,
						ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay + A.GiaTriThayDoi),0) AS ThanhTienThucChaySauTrietKhau
					FROM ThucChayDaTinh A
					WHERE 
						A.DmSanPhamREF = @DmSanPhamREF
						AND (A.DmHinhThucQuangCao = @DmHinhThucQuangCao
								OR A.TenViTri IN ('300x250','300x385'))
						AND A.HopDongID = @HopDongID
						AND A.SoHopDong = @SoHopDong
						AND A.NgayThucHien <= @NgayThucHien
						AND A.DmHinhThucQuangCao <> 13
					UNION ALL
					SELECT 
						ISNULL(SUM(B.SoLuongThucChay),0) AS SoLuongThucChay,
						ISNULL(SUM(B.ThanhTienSauTrietKhauThucChay + B.GiaTriThayDoi),0) AS ThanhTienThucChaySauTrietKhau
					FROM ThucChayDaTinhAdmarket B
					WHERE 
						B.DmSanPhamREF = @DmSanPhamREF
						AND (B.DmHinhThucQuangCao = @DmHinhThucQuangCao
								OR B.TenViTri IN ('300x250','300x385'))
						AND B.HopDongID = @HopDongID
						AND B.SoHopDong = @SoHopDong
						AND B.NgayThucHien <= @NgayThucHien
						AND B.DmHinhThucQuangCao <> 13
				)C
					
				PRINT '@TongSoLuongThucChayTichLuy: ' + CONVERT(NVARCHAR(50), @TongSoLuongThucChayTichLuy);
				PRINT '@TongThanhTienThucChayTichLuy: ' + CONVERT(NVARCHAR(50), @TongThanhTienThucChayTichLuy);
				
				IF @TongThanhTienThucChayTichLuy < @ThanhTienHopDong
				BEGIN
					-- Select so luong, thanh tien thuc chay tich luy theo phan bo
					IF EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinh WHERE HopDongChiTietREF = @PhanBoID)
					BEGIN
						SELECT 
							@TongSoLuongThucChayTichLuyTheoPhanBo = SUM(tcdt.SoLuongThucChay),
							@TongThanhTienThucChayTichLuyTheoPhanBo = SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0))
						FROM ThucChayDaTinh AS tcdt
						WHERE HopDongChiTietREF = @PhanBoID
							AND DmHinhThucQuangCao <> 13
					END
					
					PRINT '@TongSoLuongThucChayTichLuyTheoPhanBo: ' + CONVERT(NVARCHAR(50), @TongSoLuongThucChayTichLuyTheoPhanBo);
					PRINT '@TongThanhTienThucChayTichLuyTheoPhanBo: ' + CONVERT(NVARCHAR(50), @TongThanhTienThucChayTichLuyTheoPhanBo);
					
					-- check Thanh tien thuc chay tich luy theo hop dong so voi thanh tien tren hop dong
					IF (@TongThanhTienThucChayTichLuy + @ThanhTienThucChaySanPham) > @ThanhTienHopDong
					BEGIN
						SET @ThanhTienThucChay = (@ThanhTienHopDong -  @TongThanhTienThucChayTichLuy);
					END
					ELSE
					BEGIN
						SET @ThanhTienThucChay = @ThanhTienThucChaySanPham;
					END
					
					-- check thanh tien thuc chay tich luy theo phan bo hop dong va gia tri phan bo hop dong
					IF @TongThanhTienThucChayTichLuyTheoPhanBo < @ThanhTienPhanBo
					BEGIN
						IF @TongThanhTienThucChayTichLuyTheoPhanBo + @ThanhTienThucChay > @ThanhTienPhanBo
						BEGIN
							SET @ThanhTienThucChay = (@ThanhTienPhanBo - @TongThanhTienThucChayTichLuyTheoPhanBo)
						END						
					END 
					ELSE
						SET @ThanhTienThucChay = 0;
					
					-- check so luong da vuot so luong tren hop dong nhung tien thi chua vuot
					IF @ThanhTienThucChay > 0 AND @TongSoLuongThucChayTichLuy < @SoLuongHopDong
					BEGIN
						IF @TongSoLuongThucChayTichLuy + @SoLuongThucChaySanPham > @SoLuongHopDong
						BEGIN
							SET @SoLuongThucChay = @SoLuongHopDong - @TongSoLuongThucChayTichLuy
							PRINT 'SL 111';
						END
						ELSE
						BEGIN
							SET @SoLuongThucChay = @SoLuongThucChaySanPham
							PRINT 'SL 222';
						END	
						
						PRINT '@SoLuongPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBo);
						PRINT '@SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay);
						IF @TongSoLuongThucChayTichLuyTheoPhanBo < @SoLuongPhanBo
						BEGIN
							IF @TongSoLuongThucChayTichLuyTheoPhanBo + @SoLuongThucChay > @SoLuongPhanBo
							BEGIN
								SET @SoLuongThucChay = (@SoLuongPhanBo - @TongSoLuongThucChayTichLuyTheoPhanBo);
							END
							ELSE
							BEGIN
								SET @SoLuongThucChay = @SoLuongThucChay;
							END
						END
					END
					ELSE
					BEGIN
						SET @SoLuongThucChay = 0;
						SET @SoLuongLechTreoHa = @SoLuongThucChaySanPham;
						
						SET @SoLuongThucChaySanPham = 0;
					END
				END
				PRINT '@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay);
				PRINT '@SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay);
				
				IF (@ThanhTienThucChay > 0 OR @SoLuongThucChay > 0)
				BEGIN
					EXEC dbo.ThucChayDaTinhBoxAppSSV_InsertByPhanBoID
						@NgayThucHien
						,@SoHopDong
						,@PhanBoID
						,@DmSanPhamREF
						,@TenSanPham
						,@DmWebsiteREF
						,@TenWebsite
						,@TongViewThucChay
						,@TongClickThucChay
						,@SoLuongThucChay
						,@ThanhTienThucChay
						,@SoLuongThucChayKM
						,@ThanhTienThucChayKM
						,@SoLuongLechTreoHa
						,@ThanhTienLechTreoHa
						,@TypeInsert;
						
					SET @ThanhTienThucChaySanPham = @ThanhTienThucChaySanPham - @ThanhTienThucChay;
					SET @SoLuongThucChaySanPham   = @SoLuongThucChaySanPham - @SoLuongThucChay;
				END
			END
			ELSE
			BEGIN
				-- Select so luong, thanh tien thuc chay tich luy theo phan bo
				PRINT '@PhanBoID: ' + CONVERT(NVARCHAR(50),@PhanBoID);
				IF EXISTS(
							SELECT HopDongChiTietREF FROM ThucChayDaTinh A WHERE A.HopDongChiTietREF = @PhanBoID
							UNION ALL
							SELECT HopDongChiTietREF FROM ThucChayDaTinhAdmarket B WHERE B.HopDongChiTietREF = @PhanBoID
						 )
				BEGIN
					PRINT '@PhanBoID1: ' + CONVERT(NVARCHAR(50),@PhanBoID);
					SELECT 
						@TongSoLuongThucChayTichLuyTheoPhanBo = SUM(C.SoLuongThucChay),
						@TongThanhTienThucChayTichLuyTheoPhanBo = SUM(C.ThanhTienSauTrietKhauThucChay)
					FROM 
					(
						SELECT 
							ISNULL(SUM(A.SoLuongThucChay),0) AS SoLuongThucChay,
							ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay + A.GiaTriThayDoi),0) ThanhTienSauTrietKhauThucChay
						FROM ThucChayDaTinh A
						WHERE A.HopDongChiTietREF = @PhanBoID
						UNION ALL
						SELECT 
							ISNULL(SUM(B.SoLuongThucChay),0) AS SoLuongThucChay,
							ISNULL(SUM(B.ThanhTienSauTrietKhauThucChay + B.GiaTriThayDoi),0) ThanhTienSauTrietKhauThucChay
						FROM ThucChayDaTinhAdmarket B
						WHERE B.HopDongChiTietREF = @PhanBoID
					)C
				END
				ELSE
				BEGIN
					SET @TongSoLuongThucChayTichLuyTheoPhanBo = 0;
					SET @TongThanhTienThucChayTichLuyTheoPhanBo = 0;
				END

				PRINT '@TongSoLuongThucChayTichLuyTheoPhanBo: ' + CONVERT(NVARCHAR(50), @TongSoLuongThucChayTichLuyTheoPhanBo);
				PRINT '@TongThanhTienThucChayTichLuyTheoPhanBo: ' + CONVERT(NVARCHAR(50), @TongThanhTienThucChayTichLuyTheoPhanBo);
				
				/*
				 * check thanh tien thuc chay theo phan bo da vuot qua gia tri phan bo hay chua
				 */ 
				IF (@TongThanhTienThucChayTichLuyTheoPhanBo < @ThanhTienPhanBo OR @TongSoLuongThucChayTichLuyTheoPhanBo < @SoLuongPhanBo)
				BEGIN
					IF @TongThanhTienThucChayTichLuyTheoPhanBo + @ThanhTienThucChaySanPham > @ThanhTienPhanBo
					BEGIN
						SET @ThanhTienThucChay = (@ThanhTienPhanBo - @TongThanhTienThucChayTichLuyTheoPhanBo);
					END
					ELSE
					BEGIN
						SET @ThanhTienThucChay = @ThanhTienThucChaySanPham;
					END
					
					IF (@TongSoLuongThucChayTichLuyTheoPhanBo < @SoLuongPhanBo)
					BEGIN
						IF @TongSoLuongThucChayTichLuyTheoPhanBo + @SoLuongThucChaySanPham > @SoLuongPhanBo
						BEGIN
							SET @SoLuongThucChay = (@SoLuongPhanBo - @TongSoLuongThucChayTichLuyTheoPhanBo);
						END
						ELSE
						BEGIN
							SET @SoLuongThucChay = @SoLuongThucChaySanPham;
						END
					END
					--ELSE
					--BEGIN
					--	SET @SoLuongLechTreoHa = @SoLuongThucChaySanPham;
						
					--	SET @SoLuongThucChaySanPham = 0;
					--END
					
					PRINT '@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay);
					PRINT '@SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay);
					
					IF (@ThanhTienThucChay > 0 OR @SoLuongThucChay > 0) 
					BEGIN
						EXEC dbo.ThucChayDaTinhBoxAppSSV_InsertByPhanBoID
						@NgayThucHien
						,@SoHopDong
						,@PhanBoID
						,@DmSanPhamREF
						,@TenSanPham
						,@DmWebsiteREF
						,@TenWebsite
						,@TongViewThucChay
						,@TongClickThucChay
						,@SoLuongThucChay
						,@ThanhTienThucChay
						,@SoLuongThucChayKM
						,@ThanhTienThucChayKM
						,@SoLuongLechTreoHa
						,@ThanhTienLechTreoHa
						,@TypeInsert;
					END
				END
			END	
			
			SET @ThanhTienThucChaySanPham = (@ThanhTienThucChaySanPham - @ThanhTienThucChay);
			SET @SoLuongThucChaySanPham = (@SoLuongThucChaySanPham - @SoLuongThucChay)
			
			PRINT '@ThanhTienThucChaySanPhamConDu1: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
			PRINT '@SoLuongThucChaySanPhamConDu1: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySanPham);
											
			FETCH NEXT FROM tc_cursor INTO @HopDongID, @PhanBoID, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienPhanBo
		END
		CLOSE tc_cursor;
		DEALLOCATE tc_cursor;
		
		PRINT '@ThanhTienThucChaySanPhamConDu: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
		PRINT '@HopDongID: ' + CONVERT(NVARCHAR(50), @HopDongID);
		
		-- Neu du lieu thuc chay van con thi insert vao gia tri online
		IF (@ThanhTienThucChaySanPham > 0 OR @SoLuongThucChaySanPham > 0)
		BEGIN
			INSERT INTO ThucChayBoxAppSSVOnline
			SELECT 
				NEWID()
				,@SoHopDong
				,@DmSanPhamREF
				,@TenSanPham
				,@DmWebsiteREF
				,@TenWebsite
				,'View' DonViTinh
				,@SoLuongThucChaySanPham SoLuongThucChay
				,@ThanhTienThucChaySanPham ThanhTienThucChay
				,0 SoLuongKhuyenMai
				,0 ThanhTienKhuyenMai
				,@NgayThucHien
				,'' GhiChu
				,GETDATE() CreatedAt
				,'asd' CreatedBy
				,GETDATE() LastModifiedAt
				,'asd' LastModifiedBy
				,1 RecordStatus
			
			SET @ThanhTienThucChaySanPham = 0;
			SET @SoLuongThucChaySanPham = 0;
		END
	END
	
	PRINT '@@SoLuongThucChaySanPhamKM: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySanPhamKM);
	PRINT '@@ThanhTienThucChaySanPhamKM: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPhamKM);
	-- Thuc chay khuyen mai
	IF (@ThanhTienThucChaySanPhamKM > 0 OR @SoLuongThucChaySanPhamKM > 0)
	BEGIN
		-- Check hop dong co phan bo khuyen mai hay ko?
		IF EXISTS(SELECT HopDongChiTietID
		          FROM HopDongChiTiet hdct
					INNER JOIN HopDong AS hd ON hd.HopDongID = hdct.HopDongFK 
		          WHERE hd.SoHopDong = @SoHopDong AND IsKhuyenMai = 1  
						AND hd.TrangThaiHopDong <> 3 AND hdct.DeletedStatus = 0
						AND hdct.DmLoaiREF <> 13)
		BEGIN
			PRINT 'Co Khuyen Mai';
			DECLARE km_cursor CURSOR FOR
			SELECT hd.HopDongID, hdct.HopDongChiTietID, 
				CASE hdct.DonViTinhREF
					WHEN 1 THEN hdct.SoLuong*1000 -- 1 CPM = 1000 View
					ELSE hdct.SoLuong
				END AS SoLuong, 
				hdct.DonViTinh, 
				(hdct.SoLuong*hdct.DonGia) ThanhTienKM				
			FROM HopDong AS hd
				INNER JOIN HopDongChiTiet AS hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE
				hd.SoHopDong = @SoHopDong
				AND hdct.DmSanPhamREF = @DmSanPhamREF
				AND (hdct.DmLoaiREF = @DmHinhThucQuangCao
						OR hdct.TenViTri IN ('300x250','300x385'))
				AND hdct.DeletedStatus = 0
				AND hdct.IsKhuyenMai = 1	
				AND hdct.DmLoaiREF <> 13		
			OPEN km_cursor
		
			FETCH NEXT FROM km_cursor INTO @HopDongID, @PhanBoID, @SoLuongPhanBoKM, @DonViTinhPhanBo, @ThanhTienPhanBoKM 
			WHILE @@FETCH_STATUS = 0
			BEGIN
				PRINT '@HopDongID: ' + CAST(@HopDongID AS NVARCHAR(50));
				PRINT '@IsPPSanPham111: ' + CONVERT(NVARCHAR(50), @IsPPSanPham);
				IF @IsPPSanPham = 1
				BEGIN
					PRINT 'PP San Pham 111111';
					-- Seelct SoLuongKM, ThanhTienKM  theo hop dong
					SELECT 
						@SoLuongHopDongKM = ISNULL(SUM(hdct.SoLuong*1000),0),
						@ThanhTienHopDongKM = ISNULL(SUM(hdct.SoLuong*hdct.DonGia),0)
					FROM HopDong AS hd
						INNER JOIN HopDongChiTiet AS hdct ON hd.HopDongID = hdct.HopDongFK
					WHERE
						hd.SoHopDong = @SoHopDong
						AND hd.TrangThaiHopDong <> 3
						AND hdct.DmSanPhamREF = @DmSanPhamREF
						AND (hdct.DmLoaiREF = @DmHinhThucQuangCao
								OR hdct.TenViTri IN ('300x250','300x385'))
						AND hdct.DeletedStatus = 0
						AND hdct.IsKhuyenMai = 1
						AND hdct.DmLoaiREF <> 13
						
					-- select Soluong, ThanhTien thuc chay KM tich luy 
					IF EXISTS(	
								SELECT SoHopDong
								FROM ThucChayDaTinh AS tcdt
								WHERE 
									DmSanPhamREF = @DmSanPhamREF
									AND (DmHinhThucQuangCao = @DmHinhThucQuangCao
											OR tcdt.TenViTri IN ('300x250','300x385'))
									AND SoHopDong = @SoHopDong
									AND tcdt.NgayThucHien <= @NgayThucHien
									AND DmHinhThucQuangCao <> 13
								UNION ALL
								SELECT SoHopDong
								FROM ThucChayDaTinhAdmarket B
								WHERE 
									B.DmSanPhamREF = @DmSanPhamREF
									AND (B.DmHinhThucQuangCao = @DmHinhThucQuangCao
											OR B.TenViTri IN ('300x250','300x385'))
									AND B.SoHopDong = @SoHopDong
									AND B.NgayThucHien <= @NgayThucHien
									AND B.DmHinhThucQuangCao <> 13
							  )
					BEGIN
						SELECT 
							@TongSoLuongThucChayKMTichLuy = SUM(C.SoLuongThucChayKM),
							@TongThanhTienThucChayKMTichLuy = SUM(C.ThanhTienKM)
						FROM
						(
							SELECT 
								ISNULL(SUM(A.SoLuongThucChayKM),0) AS SoLuongThucChayKM,
								ISNULL(SUM(A.ThanhTienKM),0) AS ThanhTienKM
							FROM ThucChayDaTinh A
							WHERE
								A.DmSanPhamREF = @DmSanPhamREF
								AND (A.DmHinhThucQuangCao = @DmHinhThucQuangCao
										OR A.TenViTri IN ('300x250','300x385'))
								AND A.SoHopDong = @SoHopDong
								AND A.NgayThucHien <= @NgayThucHien
								AND A.DmHinhThucQuangCao <> 13
							UNION ALL
							SELECT 
								ISNULL(SUM(B.SoLuongThucChayKM),0) AS SoLuongThucChayKM,
								ISNULL(SUM(B.ThanhTienKM),0) AS ThanhTienKM
							FROM ThucChayDaTinhAdmarket B
							WHERE
								B.DmSanPhamREF = @DmSanPhamREF
								AND (B.DmHinhThucQuangCao = @DmHinhThucQuangCao
										OR B.TenViTri IN ('300x250','300x385'))
								AND B.SoHopDong = @SoHopDong
								AND B.NgayThucHien <= @NgayThucHien
								AND B.DmHinhThucQuangCao <> 13
						)C
					END
							
					IF @TongThanhTienThucChayKMTichLuy < @ThanhTienHopDongKM
					BEGIN
						IF @TongThanhTienThucChayKMTichLuy + @ThanhTienThucChaySanPhamKM > @ThanhTienHopDongKM
						BEGIN
							SET @ThanhTienThucChayKM = (@ThanhTienHopDongKM - @TongThanhTienThucChayKMTichLuy);
						END
						ELSE
						BEGIN
							SET @ThanhTienThucChayKM = @ThanhTienThucChaySanPhamKM;
						END
						
						IF EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinh AS tcdt WHERE ThanhTienKM > 0 AND HopDongChiTietREF = @PhanBoID)
						BEGIN
							-- Select tong soluong, thanhtien thuc chay khuyen mai tich luy theo phan bo id
							SELECT 
								@TongSoLuongThucChayKMTichLuyTheoPhanBo = SUM(tcdt.SoLuongThucChayKM),
								@TongThanhTienThucChayKMTichLuyTheoPhanBo = SUM(tcdt.ThanhTienKM)
							FROM ThucChayDaTinh AS tcdt
							WHERE tcdt.HopDongChiTietREF = @PhanBoID
								AND tcdt.TrangThaiHopDong <> 3
								AND ThanhTienKM > 0
								AND tcdt.DmHinhThucQuangCao <> 13
							
							IF @TongThanhTienThucChayKMTichLuyTheoPhanBo < @SoLuongPhanBoKM		
							BEGIN
								IF @TongThanhTienThucChayKMTichLuyTheoPhanBo + @ThanhTienThucChayKM > @SoLuongPhanBoKM
								BEGIN
									SET @ThanhTienThucChayKM = (@SoLuongPhanBoKM - @TongThanhTienThucChayKMTichLuyTheoPhanBo);
								END
							END	
							ELSE
								SET @ThanhTienThucChayKM = 0;					
							
						END
						IF @ThanhTienThucChayKM > 0 AND @TongSoLuongThucChayKMTichLuy < @SoLuongHopDongKM
						BEGIN
							IF @TongSoLuongThucChayKMTichLuy + @SoLuongThucChaySanPhamKM > @SoLuongHopDongKM
							BEGIN
								SET @SoLuongThucChayKM = (@SoLuongHopDongKM - @TongSoLuongThucChayKMTichLuy);
							END
							ELSE
							BEGIN
								SET @SoLuongThucChayKM = @SoLuongThucChaySanPhamKM;
							END
							
							SET @SoLuongThucChaySanPhamKM = @SoLuongThucChaySanPhamKM - @SoLuongThucChayKM;
						END
						ELSE
						BEGIN
							SET @SoLuongThucChayKM = 0;
							SET @SoLuongLechTreoHa = @SoLuongThucChaySanPhamKM;
							
							SET @SoLuongThucChaySanPhamKM = 0;
						END
						
						IF (@ThanhTienThucChayKM > 0 OR @SoLuongThucChayKM > 0)
						BEGIN
							SET @SoLuongThucChay = 0;
							SET @ThanhTienThucChay = 0;

							PRINT '@@SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay);
							PRINT '@@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay);

							EXEC dbo.ThucChayDaTinhBoxAppSSV_InsertByPhanBoID
								@NgayThucHien
								,@SoHopDong
								,@PhanBoID
								,@DmSanPhamREF
								,@TenSanPham
								,@DmWebsiteREF
								,@TenWebsite
								,@TongViewThucChay
								,@TongClickThucChay
								,@SoLuongThucChay
								,@ThanhTienThucChay
								,@SoLuongThucChayKM
								,@ThanhTienThucChayKM
								,@SoLuongLechTreoHa
								,@ThanhTienLechTreoHa
								,@TypeInsert;
								
								SET @ThanhTienThucChaySanPhamKM = (@ThanhTienThucChaySanPhamKM - @ThanhTienThucChayKM);
						END
						
					END
					
				END
				ELSE
				BEGIN
					PRINT 'PP San Pham 00000';
					PRINT 'PhanBoID: ' + CAST(@PhanBoID AS NVARCHAR(50));
					-- Select so luong km, thanh tien km thuc chay tich luy theo phan bo
					IF EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinh WHERE HopDongChiTietREF = @PhanBoID)
					BEGIN
						SELECT 
							@TongSoLuongThucChayKMTichLuyTheoPhanBo = SUM(C.SoLuongThucChayKM),
							@TongThanhTienThucChayKMTichLuyTheoPhanBo = SUM(C.ThanhTienKM)
						FROM 
						(
							SELECT 
								SUM(A.SoLuongThucChayKM) AS SoLuongThucChayKM,
								SUM(A.ThanhTienKM) AS ThanhTienKM
							FROM ThucChayDaTinh A
							WHERE A.HopDongChiTietREF = @PhanBoID
							UNION ALL
							SELECT 
								SUM(B.SoLuongThucChayKM) AS SoLuongThucChayKM,
								SUM(B.ThanhTienKM) AS ThanhTienKM
							FROM ThucChayDaTinhAdmarket B
							WHERE B.HopDongChiTietREF = @PhanBoID
						)C
					END
					ELSE
					BEGIN
						SET @TongSoLuongThucChayKMTichLuyTheoPhanBo = 0;
						SET	@TongThanhTienThucChayKMTichLuyTheoPhanBo = 0;
					END
					
					PRINT '@TongSoLuongThucChayKMTichLuyTheoPhanBo: ' + CONVERT(NVARCHAR(50), @TongSoLuongThucChayKMTichLuyTheoPhanBo);
					PRINT '@TongThanhTienThucChayKMTichLuyTheoPhanBo: ' + CONVERT(NVARCHAR(50), @TongThanhTienThucChayKMTichLuyTheoPhanBo);
					
					-- select soluong km, thanh tien km theo phan bo hop dong
					SELECT  @SoLuongPhanBoKM = CASE WHEN DonViTinh = 'CPM' THEN ISNULL(Soluong*1000,0) ELSE ISNULL(SoLuong,0) END,
							@ThanhTienPhanBoKM = ISNULL((SoLuong*DonGia),0)
					FROM HopDongChiTiet
					WHERE HopDongChiTietID = @PhanBoID
					
					PRINT '@SoLuongPhanBoKM: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBoKM);
					PRINT '@ThanhTienPhanBoKM: ' + CONVERT(NVARCHAR(50), @ThanhTienPhanBoKM);
					PRINT '@ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
					
					-- check thanh tien thuc chay theo phan bo da vuot qua gia tri phan bo hay chua
					IF @TongThanhTienThucChayKMTichLuyTheoPhanBo < @ThanhTienPhanBoKM
					BEGIN
						IF @TongThanhTienThucChayKMTichLuyTheoPhanBo + @ThanhTienThucChaySanPhamKM > @ThanhTienPhanBoKM
						BEGIN
							PRINT '1***'
							SET @ThanhTienThucChayKM = (@ThanhTienPhanBoKM - @TongThanhTienThucChayKMTichLuyTheoPhanBo);
						END
						ELSE
						BEGIN
							PRINT '2***'
							SET @ThanhTienThucChayKM = @ThanhTienThucChaySanPhamKM;
						END
						
						IF @TongSoLuongThucChayKMTichLuyTheoPhanBo < @SoLuongPhanBoKM
						BEGIN
							IF @TongSoLuongThucChayKMTichLuyTheoPhanBo + @SoLuongThucChaySanPhamKM > @SoLuongPhanBoKM
							BEGIN
								PRINT 'SL 1***'
								SET @SoLuongThucChayKM = (@SoLuongPhanBoKM - @TongSoLuongThucChayKMTichLuyTheoPhanBo);
							END
							ELSE
							BEGIN
								PRINT 'SL 2***'
								SET @SoLuongThucChayKM = @SoLuongThucChaySanPhamKM;
							END
							
							SET @SoLuongThucChaySanPhamKM = (@SoLuongThucChaySanPhamKM - @SoLuongThucChayKM)
						END
						--ELSE
						--BEGIN
						--	SET @SoLuongLechTreoHa = @SoLuongThucChaySanPhamKM;
							
						--	SET @SoLuongThucChaySanPhamKM = 0;
						--END

						IF (@ThanhTienThucChayKM > 0 OR @SoLuongThucChayKM > 0)
						BEGIN
							SET @SoLuongThucChay = 0;
							SET @ThanhTienThucChay = 0;

							PRINT '@@@SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay);
							PRINT '@@@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay);

							EXEC dbo.ThucChayDaTinhBoxAppSSV_InsertByPhanBoID
							@NgayThucHien
							,@SoHopDong
							,@PhanBoID
							,@DmSanPhamREF
							,@TenSanPham
							,@DmWebsiteREF
							,@TenWebsite
							,@TongViewThucChay
							,@TongClickThucChay
							,@SoLuongThucChay
							,@ThanhTienThucChay
							,@SoLuongThucChayKM
							,@ThanhTienThucChayKM
							,@SoLuongLechTreoHa
							,@ThanhTienLechTreoHa
							,@TypeInsert;
							
							SET @ThanhTienThucChaySanPhamKM = (@ThanhTienThucChaySanPhamKM - @ThanhTienThucChayKM);
							
						END
					END
				END	
				FETCH NEXT FROM km_cursor INTO @HopDongID, @PhanBoID, @SoLuongPhanBoKM, @DonViTinhPhanBo, @ThanhTienPhanBoKM
			END
			
			CLOSE km_cursor;
			DEALLOCATE km_cursor;
		END
	END
	
	PRINT '@@SoLuongThucChaySanPhamKM: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySanPhamKM);
	PRINT '@@ThanhTienThucChaySanPhamKM: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPhamKM);
	-- Neu tien KM, so luong KM van con du thi se insert vao bang luu du lieu online
	IF (@ThanhTienThucChaySanPhamKM > 0 OR @SoLuongThucChaySanPhamKM > 0)
	BEGIN
		PRINT 'Insert Online';
		
		INSERT INTO ThucChayBoxAppSSVOnline
		SELECT 
			NEWID()
			,@SoHopDong
			,@DmSanPhamREF
			,@TenSanPham
			,@DmWebsiteREF
			,@TenWebsite
			,'View' DonViTinh
			,0 SoLuongThucChay
			,0 ThanhTienThucChay
			,@SoLuongThucChaySanPhamKM SoLuongKhuyenMai
			,@ThanhTienThucChaySanPhamKM ThanhTienKhuyenMai
			,@NgayThucHien
			,'' GhiChu
			,GETDATE() CreatedAt
			,'asd' CreatedBy
			,GETDATE() LastModifiedAt
			,'asd' LastModifiedBy
			,1 RecordStatus
		
		SET @ThanhTienThucChaySanPhamKM = 0;
		SET @SoLuongThucChaySanPhamKM = 0;
	END
	
END
/****** Object:  StoredProcedure [dbo].[ThucChay_CheckHopDongCoThayDoi_TMDT]    Script Date: 10/24/2014 10:07:18 ******/
SET ANSI_NULLS ON

```
