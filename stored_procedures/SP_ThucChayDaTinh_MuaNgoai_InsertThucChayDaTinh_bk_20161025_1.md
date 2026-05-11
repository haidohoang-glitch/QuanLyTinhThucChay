# Stored Procedure: `ThucChayDaTinh_MuaNgoai_InsertThucChayDaTinh_bk_20161025_1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-25 11:10:40.023000
- **Ngày sửa cuối**: 2016-10-25 11:10:43.960000

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
	EXEC [ThucChayDaTinh_MuaNgoai_InsertThucChayDaTinh] '2015-04-06', 66834
*/

CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayDaTinh_bk_20161025_1] 
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
			@ThanhTienBan				INT
			
			
	SET @ThuChayDenNgay =
	(
		SELECT hdct.ThucChayDenNgay FROM HopDongChiTiet hdct
		WHERE hdct.HopDongChiTietID = @phanBoId	
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
			@thanhTienThucChayCurrent = hdct.ThanhTienThucChayMuaNgoaiTruocCK,
			@isKhuyenMai = hdct.IsKhuyenMai,
			@chietKhauHopDong = hdct.ChietKhau,
			@donViTinh = hdct.DonViTinh,
			@donViTinhThucChay = dbo.FormatDonViTinh(hdct.DonViTinhThucChayMuaNgoai)
		FROM HopDongChiTiet hdct
		WHERE HopDongChiTietID = @phanBoId
		
		SET @thucChayTruocChietKhau = @thanhTienThucChayCurrent - @thucChayTruocChietKhau 
		IF @isKhuyenMai = 0--NEU KHONG PHAI LA PHAN BO KHUYEN MAI
		BEGIN
			--Quy doi @thanhTienThucChayCurrent thanh sau chiet khau HD
			SET @thanhTienThucChayCurrent = @thanhTienThucChayCurrent*(100-@chietKhauHopDong)/100
			
			SET @deltaValueThucChay = (@thanhTienThucChayCurrent - @thanhTienThucChayTichLuy);
			SET @deltaValueSoLuong = (@soLuongThucChayCurrent - @soLuongThucChayTichLuy);
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
		ELSE--PHAN BO KHUYEN MAI
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
	ELSE
	BEGIN
		PRINT 'Chua ton tai!';
		
		SELECT 
			@soLuongThucChay = ISNULL(dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh(A.SoluongThucChay,A.DonViTinhThucChayMuaNgoai),0),
			@chietKhauHopDong = A.ChietKhau,
			@chietKhauMuaNgoai = A.ChietKhauMuaNgoai,
			@thucChayTruocChietKhau = A.ThanhTienThucChayMuaNgoaiTruocCK,
			@donViTinh = A.DonViTinh,
			@donViTinhThucChay = dbo.FormatDonViTinh(A.DonViTinhThucChayMuaNgoai),
			@isKhuyenMai = A.IsKhuyenMai
		FROM HopDongChiTiet A
		WHERE 1=1
			AND A.HopDongChiTietID = @phanBoId;
		IF(	@thucChayTruocChietKhau <> 0)
		BEGIN
			IF @isKhuyenMai = 0--NEU KHONG PHAI LA PHAN BO KHUYEN MAI
			BEGIN
				SET @deltaValueSoLuong = @soLuongThucChayCurrent 
				IF(Convert(date,@ngayThucHien) = Convert(date,@ThuChayDenNgay))
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
		EXEC dbo.ThucChayDaTinhMuaNgoai_InsertByPhanBoId
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
