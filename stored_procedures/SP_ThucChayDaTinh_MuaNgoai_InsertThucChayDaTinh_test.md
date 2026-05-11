# Stored Procedure: `ThucChayDaTinh_MuaNgoai_InsertThucChayDaTinh_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-08 15:55:55.680000
- **Ngày sửa cuối**: 2017-11-08 15:55:55.680000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |
| `@phanBoId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-12
-- Description:	Tinh thuc chay mua ngoai theo ngay thuc hien
-- =============================================
/*
	EXEC [ThucChayDaTinh_MuaNgoai_InsertThucChayDaTinh] '2016-11-24', 98488
*/

CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayDaTinh_test] 
	-- Add the parameters for the stored procedure here
	@ngayThucHien	DATETIME,
	@phanBoId		INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @soLuongThucChay		INT		= 0,
			@thanhTienThucChay		FLOAT	= 0,
			@chietKhauHopDong		INT		= 0,
			@chietKhauMuaNgoai		INT		= 0,
			@thucChayTruocChietKhau	FLOAT	= 0,
			@soLuongThayDoi			INT		= 0,
			@giaTriThayDoi			FLOAT	= 0,
			@soLuongKhuyenMai		INT		= 0,
			@thanhTienKhuyenMai		FLOAT	= 0,
			@soLuongKMThayDoi		INT		= 0,
			@giaTriKMThayDoi		FLOAT	= 0,
			@isKhuyenMai			INT		= 0,
			@donViTinh				NVARCHAR(50),
			@donViTinhThucChay		NVARCHAR(50),
			@ghiChu					NVARCHAR(512) = N'MuaNgoai',
			@giaTriPhanBo			FLOAT	= 0,
			@soLuongPhanBo			INT		= 0
			
	DECLARE @soLuongThucChayTichLuy	INT		= 0,
			@thanhTienThucChayTichLuy	FLOAT	= 0,
			@soLuongKMTichLuy			INT = 0,
			@thanhTienKMTichLuy			FLOAT = 0,
			@soLuongThucChayCurrent		INT = 0,
			@thanhTienThucChayCurrent	FLOAT = 0,
			@deltaValueSoLuong			INT		= 0,
			@deltaValueThucChay			FLOAT	= 0,
			@ThuChayDenNgay				DATETIME,
			@ThanhTienBan				FLOAT,
			@SoluongHDCT				INT=0,
			@DonGiaHDCT					FLOAT=0,
			@IsMuaNgoaiChot				INT=0
	
	SET @IsMuaNgoaiChot=
	(
		SELECT COUNT(CONTRACT_DETAIL_ID) FROM ThucChayMuaNgoaiChot
		WHERE CONTRACT_DETAIL_ID = @phanBoId
		AND DELETED_STATUS = 0
	)
			
	SET @ThuChayDenNgay = 
	(
		--SELECT hdct.ThucChayDenNgay FROM HopDongChiTiet hdct
		--WHERE hdct.HopDongChiTietID = @phanBoId	
		SELECT hdct.NgaySuaThucChay FROM dbo.ThucChayMuaNgoai_HopDongChiTiet hdct
		WHERE hdct.HopDongChiTietREF = @phanBoId	
	)
	IF EXISTS(SELECT A.HopDongChiTietREF 
				FROM ThucChayDaTinh A 
				WHERE A.HopDongChiTietREF = @phanBoId
					--AND A.DotChayHopDong = N'MuaNgoai'
					AND (A.DmHinhThucQuangCao = 13 OR A.DmLoaiBannerREF = 18)
					AND A.NgayThucHien <= @ngayThucHien)
	BEGIN
		PRINT 'Da ton tai!';
		SELECT 
			@soLuongThucChayTichLuy = SUM(A.SoLuongThucChay + A.SoLuongThayDoi),
			@thanhTienThucChayTichLuy = SUM(A.ThanhTienSauTrietKhauThucChay + A.GiaTriThayDoi),
			@thucChayTruocChietKhau = SUM(A.ThanhTienThucChayTruocTrietKhau),
			@soLuongKMTichLuy = SUM(A.SoLuongThucChayKM + A.SoLuongKMThayDoi),
			@thanhTienKMTichLuy = SUM(A.ThanhTienKM + A.GiaTriKMThayDoi)
		FROM ThucChayDaTinh A
		WHERE A.HopDongChiTietREF = @phanBoId
		GROUP BY A.IsKhuyenMai
		
		SELECT
			@soLuongThucChayCurrent = ISNULL(dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh(hdct.SoluongThucChay,hdct.DonViTinhThucChayMuaNgoai),0),
			@thanhTienThucChayCurrent = TC.ThanhTienThucChayMuaNgoaiTruocCK,
			@isKhuyenMai = hdct.IsKhuyenMai,
			@chietKhauHopDong = TC.ChietKhauMuaNgoai,
			@donViTinh = hdct.DonViTinh,
			@ThanhTienBan = hdct.ThanhTien,
			@SoluongHDCT = hdct.SoLuong,
			@DonGiaHDCT = hdct.DonGia,
			@donViTinhThucChay = dbo.FormatDonViTinh(hdct.DonViTinhThucChayMuaNgoai)
		FROM HopDongChiTiet hdct
			INNER JOIN dbo.ThucChayMuaNgoai_HopDongChiTiet TC ON hdct.HopDongChiTietID = TC.HopDongChiTietREF
		WHERE HopDongChiTietID = @phanBoId

		--NEU DA CHOT MUA NGOAI THI ThanhTienThucChayMuaNgoaiTruocCK = @SoluongHDCT*@DonGiaHDCT
		IF(@IsMuaNgoaiChot <> 0)
			SET @thanhTienThucChayCurrent = @DonGiaHDCT*@SoluongHDCT

		SET @thucChayTruocChietKhau = @thanhTienThucChayCurrent - @thucChayTruocChietKhau 
		IF @isKhuyenMai = 0--NEU KHONG PHAI LA PHAN BO KHUYEN MAI
		BEGIN
			--Quy doi @thanhTienThucChayCurrent thanh sau chiet khau HD
			--CHECK THANH TIEN THUC CHAY CO VUOT GIA TRI BAN
			--PRINT 'khong la khuyen mai'
			SET @thanhTienThucChayCurrent = @thanhTienThucChayCurrent*(100-@chietKhauHopDong)/100
			--PRINT CONVERT(NVARCHAR(200),@ThanhTienBan)
			--PRINT CONVERT(NVARCHAR(200),@thanhTienThucChayTichLuy)
			--PRINT CONVERT(NVARCHAR(200),@thanhTienThucChayCurrent)

			-- rem fix bug ngay 27/09/2017
			--IF((@ThanhTienBan >= @thanhTienThucChayTichLuy) AND (@ThanhTienBan >= @thanhTienThucChayCurrent))
			BEGIN

				SET @deltaValueThucChay = (@thanhTienThucChayCurrent - @thanhTienThucChayTichLuy);
				SET @deltaValueSoLuong = (@soLuongThucChayCurrent - @soLuongThucChayTichLuy);
				IF(@ThanhTienBan < @thanhTienThucChayTichLuy + @deltaValueThucChay)
				BEGIN
					SET @deltaValueThucChay = @ThanhTienBan - @thanhTienThucChayTichLuy
				END

				--PRINT 'thucchay 1:'	+ CONVERT(NVARCHAR(200),@deltaValueThucChay)

				IF(@deltaValueThucChay <> 0)
				BEGIN
					IF (Convert(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay)) 
					BEGIN
						SET @thanhTienThucChay = @deltaValueThucChay
						SET @soLuongThucChay = @deltaValueSoLuong
					END
					ELSE
					BEGIN
						SET @giaTriThayDoi = @deltaValueThucChay
						SET @soLuongThayDoi = @deltaValueSoLuong
					END
				END	
			END
			
		END
		ELSE--PHAN BO KHUYEN MAI
		BEGIN
			----CHECK XEM THANH TIEN KHUYEN MAI DA VUOT GIA TRI TINH CHUA
			IF((@SoluongHDCT * @DonGiaHDCT) < @thanhTienKMTichLuy)
			BEGIN
				SET @deltaValueThucChay = (@thanhTienThucChayCurrent - @thanhTienKMTichLuy)
				IF(@deltaValueThucChay <>0)
				BEGIN
					IF (Convert(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay)) 
					BEGIN
						SET @thanhTienKhuyenMai = @deltaValueThucChay
					END
					ELSE
					BEGIN
						SET @giaTriKMThayDoi = @deltaValueThucChay
					END
				
					SET @deltaValueSoLuong = (@soLuongThucChayCurrent - @soLuongThucChayTichLuy);
				
					IF (Convert(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay)) 
					BEGIN
						SET @soLuongKhuyenMai = @deltaValueSoLuong;
					END
					ELSE
					BEGIN
						SET @soLuongKMThayDoi = @deltaValueSoLuong;				
					END	
				END
			END
			 
		END
	END
	ELSE
	BEGIN
		PRINT 'Chua ton tai!';
		
		SELECT 
			@soLuongThucChay = ISNULL(dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh(A.SoluongThucChay,A.DonViTinhThucChayMuaNgoai),0),
			@chietKhauHopDong = A.ChietKhau,
			@chietKhauMuaNgoai = TC.ChietKhauMuaNgoai,
			@thucChayTruocChietKhau = TC.ThanhTienThucChayMuaNgoaiTruocCK,
			@donViTinh = A.DonViTinh,
			@ThanhTienBan = A.ThanhTien,
			@DonGiaHDCT = A.DonGia,
			@SoluongHDCT = A.SoLuong,
			@donViTinhThucChay = dbo.FormatDonViTinh(A.DonViTinhThucChayMuaNgoai),
			@isKhuyenMai = A.IsKhuyenMai
		FROM HopDongChiTiet A
				INNER JOIN dbo.ThucChayMuaNgoai_HopDongChiTiet TC ON A.HopDongChiTietID = TC.HopDongChiTietREF
		WHERE 1=1
			AND A.HopDongChiTietID = @phanBoId;

			--NEU DA CHOT MUA NGOAI THI ThanhTienThucChayMuaNgoaiTruocCK = @SoluongHDCT*@DonGiaHDCT
			IF(@IsMuaNgoaiChot <> 0)
			BEGIN
				SET @thanhTienThucChayCurrent = @SoluongHDCT*@DonGiaHDCT
				SET @soLuongThucChayCurrent = @SoluongHDCT;
				SET @thucChayTruocChietKhau = @thanhTienThucChayCurrent;
			END
		IF(	@thucChayTruocChietKhau <> 0)
		BEGIN
			IF @isKhuyenMai = 0--NEU KHONG PHAI LA PHAN BO KHUYEN MAI
			BEGIN
				
				--IF(@ThanhTienBan<= (@thucChayTruocChietKhau*(100-@chietKhauHopDong)/100))
				--BEGIN
				--	SET @deltaValueSoLuong = @soLuongThucChayCurrent 
				--	IF(CONVERT(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay))
				--	BEGIN
				--		SET @thanhTienThucChay = @thucChayTruocChietKhau*(100-@chietKhauHopDong)/100
				--		SET @soLuongThucChay = 	@deltaValueSoLuong			
				--	END 
					
				--	ELSE				
				--		BEGIN
				--			SET @giaTriThayDoi = @thucChayTruocChietKhau*(100-@chietKhauHopDong)/100
				--			SET @soLuongThayDoi = 	@deltaValueSoLuong
				--		END
				--END
				--ELSE
				--	BEGIN
				--		SET @deltaValueSoLuong = @soLuongThucChayCurrent 
				--		IF(CONVERT(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay))
				--		BEGIN
				--			SET @thanhTienThucChay = @ThanhTienBan
				--			SET @soLuongThucChay = 	@deltaValueSoLuong			
				--		END 
					
				--		ELSE				
				--			BEGIN
				--				SET @giaTriThayDoi = @ThanhTienBan
				--				SET @soLuongThayDoi = 	@deltaValueSoLuong
				--			END
				--	END
				

				IF(@ThanhTienBan<= (@thucChayTruocChietKhau*(100-@chietKhauHopDong)/100))
				BEGIN
					SET @deltaValueSoLuong = @soLuongThucChayCurrent 
					IF(CONVERT(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay))
					BEGIN
						SET @thanhTienThucChay = @ThanhTienBan
						SET @soLuongThucChay = 	@deltaValueSoLuong	
						
					END 
					ELSE				
						BEGIN
							SET @giaTriThayDoi = @ThanhTienBan
							SET @soLuongThayDoi = 	@deltaValueSoLuong
						END
				END
				ELSE
					BEGIN
						SET @deltaValueSoLuong = @soLuongThucChayCurrent 
						IF(CONVERT(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay))
						BEGIN
							SET @thanhTienThucChay = @thucChayTruocChietKhau*(100-@chietKhauHopDong)/100
							SET @soLuongThucChay = 	@deltaValueSoLuong			
						END 
					
						ELSE				
							BEGIN
								SET @giaTriThayDoi = @thucChayTruocChietKhau*(100-@chietKhauHopDong)/100
								SET @soLuongThayDoi = 	@deltaValueSoLuong
								
							END
					END
					
			END
			ELSE--NEU LA PHAN BO KHUYEN MAI
			BEGIN
				IF(Convert(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay))
				BEGIN
					SET @soLuongKhuyenMai = @soLuongThucChay
					SET @soLuongThucChay = 0
					SET @thanhTienKhuyenMai = @thucChayTruocChietKhau	
				END
				ELSE
					BEGIN
						SET @soLuongKMThayDoi = @soLuongThucChay
						SET @soLuongThucChay = 0
						SET @giaTriKMThayDoi = @thucChayTruocChietKhau
					END
			END	
		END
	END
	
	PRINT '@soLuongThucChayCurrent: ' + CONVERT(NVARCHAR(50), @soLuongThucChayCurrent);
	
	PRINT 'SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @soLuongThucChay);
	PRINT '@chietKhauMuaNgoai: ' + CONVERT(NVARCHAR(50), @chietKhauMuaNgoai);
	PRINT '@thucChayTruocChietKhau: ' + CONVERT(NVARCHAR(50), @thucChayTruocChietKhau);
	PRINT '@thanhTienThucChay: ' + CONVERT(NVARCHAR(50), @thanhTienThucChay);
	PRINT '@donViTinh: ' + @donViTinh;
	
	IF (@thanhTienThucChay <> 0 OR @thanhTienKhuyenMai <> 0 OR @soLuongThucChay <> 0 OR @soLuongKhuyenMai <> 0 
		OR @giaTriThayDoi <> 0 OR @giaTriKMThayDoi <> 0 OR @soLuongThayDoi <> 0 OR @soLuongKMThayDoi <> 0)
	BEGIN
		PRINT 'Insert'
		EXEC dbo.ThucChayDaTinhMuaNgoai_InsertByPhanBoId_test
		@ngayThucHien						= @ngayThucHien,
		@phanBoId							= @phanBoId,
		@soLuongThucChay					= @soLuongThucChay,
		@thanhTienThucChayMuaNgoaiTruocCK	= @thucChayTruocChietKhau,
		@thanhTienThucChay					= @thanhTienThucChay,
		@soLuongThayDoi						= @soLuongThayDoi,
		@giaTriThayDoi						= @giaTriThayDoi,
		@soLuongKhuyenMai					= @soLuongKhuyenMai,
		@thanhTienKhuyenMai					= @thanhTienKhuyenMai,
		@soLuongKMThayDoi					= @soLuongKMThayDoi,
		@giaTriKMThayDoi					= @giaTriKMThayDoi,
		@donViTinhThucChay					= @donViTinhThucChay,
		@ghiChu								= @ghiChu
		
	END
	ELSE
	BEGIN
		PRINT 'Not Insert'
	END
	
    --SELECT 1;
END

```
