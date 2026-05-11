# Stored Procedure: `ThucChayDaTinhAdmarket_UpdateGiaTriThayDoiManualByContractNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-24 16:13:49.760000
- **Ngày sửa cuối**: 2015-04-09 11:50:16.037000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ContractNo` | `nvarchar(100)` | No |
| `@SanPhamID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-09-05
-- Description:	Update gia tri thay doi bang tay
-- =============================================
-- 
/*
	EXEC dbo.ThucChayDaTinhAdmarket_UpdateGiaTriThayDoiManualByContractNo 
		'2015-04-06', 
		'QC060115', 
		585
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_UpdateGiaTriThayDoiManualByContractNo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien		DATETIME,
	@ContractNo			NVARCHAR(50),
	@SanPhamID			INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @GiaTriHopDong	FLOAT = 0,
			@HopDongId		INT = 0,
			@ThanhTienThucChay FLOAT = 0,
			@Delta	FLOAT = 0,
			@DmViTriREF			INT,
			@TenViTri			NVARCHAR(50),
			
			@PhanBoId	INT,
			@TenSanPham		NVARCHAR(50),
			@ThanhTienPhanBo	FLOAT,
			@ThanhTienThucChayPhanBo	FLOAT,
			@GiaTriThayDoi	FLOAT,
			@DonViTinh		NVARCHAR(50)
			
	DECLARE @NoiDungLog			NVARCHAR(MAX),
			@GhiChu				NVARCHAR(MAX)
			
	DECLARE @MaHopDongId				INT,
			@TenMaHopDong			NVARCHAR(50),
			@account			NVARCHAR(50)
			
	DECLARE @Count INT,
			@ThucChayTheoSite FLOAT,
			@Tyle				FLOAT,
			@TongTienThucChay	FLOAT,
			@ThanhTienThucChayByViTri	FLOAT = 0,
			@TyLeByViTri			FLOAT = 0,
			@ThucChayAdXMobile	FLOAT = 0,
			@ThucChayAdxEcommerce FLOAT = 0,
			@ThucChayAdx		FLOAT = 0,
			@GiaTriThayDoiByViTri	FLOAT = 0
			
    SELECT 
		@GiaTriHopDong = ISNULL(SUM(ThanhTien),0)
		,@HopDongId = hd.HopDongID
		,@MaHopDongId = hd.DmMaHopDongREF
		,@TenMaHopDong = hd.TenMaHopDong
    FROM HopDong AS hd
		INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
    WHERE 1=1
		AND hd.SoHopDong = @ContractNo
		AND hdct.DmSanPhamREF = @SanPhamID
		AND hdct.DeletedStatus = 0
		AND hd.TrangThaiHopDong <> 3
		--AND hdct.IsKhuyenMai <> 1
    GROUP BY hd.HopDongID, hd.DmMaHopDongREF, hd.TenMaHopDong
		
	SELECT 
		@ThanhTienThucChay = SUM(ISNULL(A.ThanhTienSauTrietKhauThucChay,0) + ISNULL(A.GiaTriThayDoi,0))
	FROM ThucChayDaTinhAdmarket A
	WHERE 1=1
		AND A.TrangThaiHopDong <> 3
		AND A.SoHopDong = @ContractNo
		AND A.DmSanPhamREF = @SanPhamID;
		
	IF @ThanhTienThucChay > @GiaTriHopDong
	BEGIN
		SET @Delta = (@ThanhTienThucChay - @GiaTriHopDong);
	END
	
	IF @Delta > 0
	BEGIN
		DECLARE pb_cursor CURSOR FOR
		SELECT 
			hdct.HopDongChiTietID, hdct.TenSanPham, hdct.ThanhTien, hdct.DonViTinh, hdct.TK_AdMarket
		FROM HopDongChiTiet AS hdct
		WHERE hdct.HopDongFK = @HopDongId
			AND hdct.DeletedStatus = 0
			AND hdct.DmSanPhamREF = @SanPhamID
			AND hdct.IsKhuyenMai <> 1
		
		OPEN pb_cursor
		
		FETCH NEXT FROM pb_cursor INTO @PhanBoId, @TenSanPham, @ThanhTienPhanBo, @DonViTinh, @account
		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			SELECT @ThanhTienThucChayPhanBo = ISNULL(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi),0)
			FROM ThucChayDaTinhAdmarket AS tcdta
			WHERE tcdta.TrangThaiHopDong <> 3
				AND tcdta.HopDongChiTietREF = @PhanBoId
				AND tcdta.DmSanPhamREF = @SanPhamID;
				
			IF @ThanhTienThucChayPhanBo > @ThanhTienPhanBo
			BEGIN
				SET @GiaTriThayDoi = (@ThanhTienPhanBo - @ThanhTienThucChayPhanBo);
				SET @NoiDungLog = N'Hợp đồng thay đổi giá trị';
				SET @GhiChu = N'Hợp đồng thay đổi giá trị';
				
				PRINT '@GiaTriThayDoi: ' + CONVERT(NVARCHAR(50), @GiaTriThayDoi);
				
				IF @DonViTinh = 'CPC'
					SET @DonViTinh = 'CLICK'
				ELSE IF @DonViTinh = 'CPM'
					SET @DonViTinh = 'VIEW'
				ELSE 
					SET @DonViTinh = 'CLICK'
				
				--PRINT 'Log: ' + @NoiDungLog;
				EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
					@HopDongID
					,@ContractNo
					,@PhanBoId
					,@SanPhamID
					,0 --@DmWebsiteREF
					,@NgayThucHien
					,0
					,0
					,0
					,0
					,0
					,@NoiDungLog
					,'HopDongChiTiet_Admarket_SSV'
					,@GhiChu
						
				DECLARE vitri_cursor CURSOR FOR
				SELECT DmViTriREF, TenViTri, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
				FROM ThucChayDaTinhAdmarket tcdt
				WHERE HopDongChiTietREF = @PhanBoId
					AND tcdt.DmSanPhamREF = @SanPhamID
					AND tcdt.NgayThucHien BETWEEN '2014-01-01' AND @NgayThucHien 
				GROUP BY
					DmViTriREF, TenViTri
				
				OPEN vitri_cursor
				
				FETCH NEXT FROM vitri_cursor INTO @DmViTriREF, @TenViTri, @ThanhTienThucChayByViTri
				WHILE @@FETCH_STATUS = 0
				BEGIN
					SET @TyLeByViTri = (@ThanhTienThucChayByViTri/@ThanhTienThucChayPhanBo)
					SET @GiaTriThayDoiByViTri = (@TyLeByViTri*@GiaTriThayDoi)
					
					IF @GiaTriThayDoiByViTri <> 0
					BEGIN
						--Insert gia tri thay doi
						EXEC dbo.ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi
							@NgayThucHien				= @NgayThucHien
							,@HopDongId					= @HopDongId
							,@SoHopDong					= @ContractNo
							,@PhanBoId					= @PhanBoId
							,@SanPhamId					= @SanPhamID
							,@TenSanPham				= @TenSanPham
							,@DonViTinh					= @DonViTinh
							,@SoLuongThayDoiThucChay	= 0
							,@ThanhTienThayDoiThucChay	= @GiaTriThayDoiByViTri
							,@SoLuongThayDoiKhuyenMai	= 0
							,@ThanhTienThayDoiKhuyenMai	= 0
							,@GhiChu					= 'UPDATE_GTTD'
							,@DmViTriREF				= @DmViTriREF
							,@TenViTri					= @TenViTri
							
						-- Insert thuc chay online
						SET @GiaTriThayDoiByViTri = (@GiaTriThayDoiByViTri*(-1))
						
						SET @GhiChu = ('UPDATE_GTTD_' + @ContractNo)
						-- Insert bu gia tri cho doi tuong khong co so hop dong
						EXEC dbo.ThucChayDaTinhAdmarket_InsertNoContractByProduct
							@DmSanPhamREF			= @SanPhamID
							,@TenSanPham			= @TenSanPham
							,@DonViTinh				= @DonViTinh
							,@DmWebsiteREF			= 0
							,@TenWebsite			= ''
							,@NgayThucHien			= @NgayThucHien
							,@SoLuongThucChay		= 0
							,@SoLuongThhucChayKM	= 0
							,@ThanhTienThucChay		= 0
							,@ThanhTienThucChayKM	= 0
							,@DmMaHopDongREF		= @MaHopDongId
							,@TenMaHopDong			= @TenMaHopDong
							,@GhiChu				= @GhiChu
							,@GiaTriThayDoi			= @GiaTriThayDoiByViTri
							,@SoLuongThayDoi		= 0
							,@DmViTriREF			= @DmViTriREF
							,@TenViTri				= @TenViTri
							
						INSERT INTO ThucChayAdmarketOnline
						SELECT 
							NEWID()
							,@SanPhamID
							,@TenSanPham -- AdX  CPC Admarket
							,@account
							,0 -- TotalViewOnline
							,0 -- TotalClickOnline
							,0 -- SoLuongThucChayOnline
							,@DonViTinh
							,@GiaTriThayDoiByViTri -- Tien online
							,0	-- KM online
							,@NgayThucHien
							,0 --IsNoiBo
							,'Vuot_Gia_Tri_Hop_Dong'
							,0
							,GETDATE()
							,'asd'
							,GETDATE()
							,'asd'
							,@DmViTriREF
							,@TenViTri
					END
					
					FETCH NEXT FROM vitri_cursor INTO @DmViTriREF, @TenViTri, @ThanhTienThucChayByViTri
				END
				
				CLOSE vitri_cursor
				DEALLOCATE vitri_cursor

				SET @GiaTriThayDoi = 0	
			END
			
			FETCH NEXT FROM pb_cursor INTO @PhanBoId, @TenSanPham, @ThanhTienPhanBo, @DonViTinh, @account
		END
		
		CLOSE pb_cursor
		DEALLOCATE pb_cursor;	
		
	END
	
	-- Insert data no contract
    EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract @NgayThucHien;		
    
	SELECT 2
END

```
