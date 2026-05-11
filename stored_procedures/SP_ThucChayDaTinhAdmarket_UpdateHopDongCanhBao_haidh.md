# Stored Procedure: `ThucChayDaTinhAdmarket_UpdateHopDongCanhBao_haidh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:03.373000
- **Ngày sửa cuối**: 2015-06-19 18:00:16.100000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-03-21
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.ThucChayDaTinhAdmarket_UpdateHopDongCanhBao '2015-01-01'
* */
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_UpdateHopDongCanhBao_haidh]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @hopDongID	INT,
			@soHopDong	NVARCHAR(50),
			@phanBoId	INT,
			@account	NVARCHAR(50),
			@sanPhamID	INT,
			@tenSanPham	NVARCHAR(50),
			@tenMaHopDong	NVARCHAR(50),
			@isNoiBo		INT
			
	DECLARE @soLuongThucChay	INT,
			@thanhTienThucChay	FLOAT,
			@soLuongThayDoi		INT,
			@giaTriThayDoi		FLOAT,
			@dmViTriREF			INT,
			@tenViTri			NVARCHAR(50)
			
	DECLARE @minNgayTienVe		DATETIME,
			@LastDateCharge		DATETIME,
			@maxNgayCanhBao		DATETIME,
			@ghiChu				NVARCHAR(50)

    DECLARE hd_cursor CURSOR FOR
    SELECT DISTINCT
		HopDongID, SoHopDong, HopDongChiTietID, TK_Admarket, DmViTriREF, TenViTri, DmSanPhamREF, TenSanPham,
		LEFT(SoHopDong,2) TenMaHopDong
    FROM HopDongAdmarketCanhBao
    WHERE 1=1
		AND RecordStatus = 0
		AND NgayThucHien <= @NgayThucHien
		
	OPEN hd_cursor
	
	FETCH NEXT FROM hd_cursor INTO @hopDongID, @soHopDong, @phanBoId, @account, @dmViTriREF, @tenViTri, @sanPhamID, @tenSanPham, @tenMaHopDong
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @hopDongID, @soHopDong, @phanBoId
		
		IF (@tenMaHopDong = 'NB' OR @tenMaHopDong = 'SH')
			SET @isNoiBo = 1;
		ELSE
			SET @isNoiBo = 0;
		
		--XAC DINH NGAY NAP TIEN CUOI CUNG CUA TAI KHOAN
		SELECT @LastDateCharge = MAX(d.LastDateRecharge) 
		FROM dbo.AdmarketUserLastRecharge d
		WHERE  d.UserName = @account
		AND CONVERT(DATE,LastDateRecharge) <=@NgayThucHien
		--AND d.Code LIKE 'cpc'--TABLE NAY PHAI CHO THEM DmSanPhamREF
		 	
		-- select max ngay canh bao
		SELECT 
			@maxNgayCanhBao = MAX(NgayThucHien)
		FROM HopDongAdmarketCanhBao AS hdacb
		WHERE 1=1
			AND hdacb.HopDongID = @hopDongID
			AND hdacb.RecordStatus = 0
			AND hdacb.NgayThucHien <= @NgayThucHien
			
		IF @LastDateCharge >= @maxNgayCanhBao
		BEGIN
			-- Update status trong bang canh bao
			UPDATE HopDongAdmarketCanhBao
			SET RecordStatus = 1 --Update ve tinh trang khong con canh bao
			WHERE 1=1
				AND HopDongID = @hopDongID
				AND HopDongChiTietID = @phanBoId
				
				AND RecordStatus = 0
		END
		ELSE
		BEGIN
			SELECT 1
			--NEU QUA SO NGAY CHO PHEP CHAY THAU CHI THI PHAI UPDATE LAI GIA TRI THAY DOI CHO CAC HD DA CHAY
			--IF(@NgayThucHien = DATEADD(DAY,[dbo].[fn_GetSoNgayDuocPhepChayThauChi](),@maxNgayCanhBao))
			--BEGIN
			--	SELECT 
			--		@soLuongThucChay = ISNULL(SUM(tcdta.SoLuongThucChay + tcdta.SoLuongThayDoi), 0),
			--		@thanhTienThucChay = ISNULL(SUM(tcdta.ThanhTienSauTrietKhauThucChay + tcdta.GiaTriThayDoi), 0)
			--	FROM ThucChayDaTinhAdmarket AS tcdta
			--	WHERE 1=1
			--		AND tcdta.HopDongID = @hopDongID
			--		AND tcdta.HopDongChiTietREF = @phanBoId
			--		AND tcdta.TrangThaiHopDong <> 3
			--		AND tcdta.NgayThucHien <= @NgayThucHien
			--		AND tcdta.DmViTriREF = @dmViTriREF
					
			--	SET @soLuongThayDoi = ((-1)*@soLuongThucChay);
			--	SET @giaTriThayDoi = ((-1)*@thanhTienThucChay);
				
			--	SET @ghiChu = N'UPDATE_GTTD_TAM_TINH_THUC_CHAY';
				
			--	--Insert gia tri thay doi
			--	EXEC dbo.ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi
			--		@NgayThucHien				= @NgayThucHien
			--		,@HopDongId					= @HopDongID
			--		,@SoHopDong					= @SoHopDong
			--		,@PhanBoId					= @phanBoId
			--		,@SanPhamId					= @sanPhamID
			--		,@TenSanPham				= @tenSanPham
			--		,@DonViTinh					= 'CLICK'
			--		,@SoLuongThayDoiThucChay	= @soLuongThayDoi
			--		,@ThanhTienThayDoiThucChay	= @giaTriThayDoi
			--		,@SoLuongThayDoiKhuyenMai	= 0
			--		,@ThanhTienThayDoiKhuyenMai	= 0
			--		,@GhiChu					= @ghiChu
			--		,@DmViTriREF				= @DmViTriREF
			--		,@TenViTri					= @TenViTri
					
			--	-- Insert log gia tri thay doi
			--	EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
			--		@HopDongID
			--		,@SoHopDong
			--		,@phanBoId
			--		,@sanphamID
			--		,0 --@DmWebsiteREF
			--		,@NgayThucHien
			--		,@giaTriThayDoi
			--		,0
			--		,0
			--		,0
			--		,0
			--		,@ghiChu
			--		,'HopDongChiTiet_Admarket_SSV'
			--		,@GhiChu
					
			--	-- Insert gia tri vao bang Online
			--	INSERT INTO ThucChayAdmarketOnline
			--	SELECT 
			--		NEWID()
			--		,@sanPhamID
			--		,@tenSanPham -- AdX  CPC Admarket
			--		,@account
			--		,0 -- TotalViewOnline
			--		,0 -- TotalClickOnline
			--		,0 -- SoLuongThucChayOnline
			--		,'CLICK'
			--		,@thanhTienThucChay -- Tien online
			--		,0	-- KM online
			--		,@NgayThucHien
			--		,@isNoiBo --IsNoiBo
			--		,@ghiChu
			--		,0
			--		,GETDATE()
			--		,'asd'
			--		,GETDATE()
			--		,'asd'
			--		,@dmViTriREF
			--		,@tenViTri
			--END
		END
		FETCH NEXT FROM hd_cursor INTO @hopDongID, @soHopDong, @phanBoId, @account, @dmViTriREF, @tenViTri, @sanPhamID, @tenSanPham, @tenMaHopDong
	END
	
	CLOSE hd_cursor
	DEALLOCATE hd_cursor
END

```
