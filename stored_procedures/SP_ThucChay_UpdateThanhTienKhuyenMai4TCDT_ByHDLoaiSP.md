# Stored Procedure: `ThucChay_UpdateThanhTienKhuyenMai4TCDT_ByHDLoaiSP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-26 10:03:19.360000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.507000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_UpdateThanhTienKhuyenMai4TCDT_ByHDLoaiSP] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
	, @SoHopDong NVARCHAR(50)
	, @TypeProduct INT
	, @DmWebsiteREF INT
AS
BEGIN
	DECLARE @v_count INT
	DECLARE @v_tongviewthucchay BIGINT, @v_tongviewphanbo BIGINT, @v_viewthucchay BIGINT
	DECLARE @v_dongia FLOAT
	--KIEM TRA HD CO TON TAI PHAN BO KHUYEN MAI ?
	SET @v_count =
	(
		SELECT COUNT(hdct.HopDongChiTietID) FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.SoHopDong = @SoHopDong
		AND hdct.DmSanPhamREF = dbo.[GetProductIDByTypeProduct](@TypeProduct)
		AND hdct.IsKhuyenMai = 1
	)
	--HD TON TAI PHAN BO KHUYEN MAI
	IF(@v_count >0)
		BEGIN
			--LAY DON GIA CUA PHAN BO KHUYEN MAI
			SET @v_dongia =
			(
				SELECT max(ISNULL(hdct.DonGia,0))/1000 FROM HopDong hd
				INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				WHERE hd.SoHopDong = @SoHopDong
				AND hdct.DmSanPhamREF = dbo.[GetProductIDByTypeProduct](@TypeProduct)
				AND hdct.IsKhuyenMai = 1	
			)
			SET @v_dongia = ISNULL(@v_dongia,0)
			--LAY TONG VIEW THUC CHAY CUA HOP DONG TU THUCCHAY (NGAYTHUCCHAY<= NGAYTHUCHIEN)
			SET @v_tongviewthucchay =
			(
				SELECT SUM(ISNULL(tc.SoLuongThucChay,0)) FROM ThucChayDaTinh tc
				WHERE UPPER(LTRIM(RTRIM(tc.SoHopDong))) = @SoHopDong
				AND tc.DmSanPhamREF = dbo.[GetProductIDByTypeProduct](@TypeProduct)
				AND Convert(date,tc.NgayThucHien) <= @NgayThucHien
			)
			SET @v_tongviewthucchay = ISNULL(@v_tongviewthucchay,0)
			--LAY TONG VIEW CUA CAC PHAN BO KHONG PHAI LA KHUYEN MAI
			SET @v_tongviewphanbo = 
			(
				SELECT SUM(ISNULL(hdct.SoLuong,0))*1000 FROM HopDong hd
				INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				WHERE hd.SoHopDong = @SoHopDong
				AND hdct.DmSanPhamREF = dbo.[GetProductIDByTypeProduct](@TypeProduct)
				AND hdct.IsKhuyenMai = 0	
			)
			SET @v_tongviewphanbo = ISNULL(@v_tongviewphanbo,0)
			--LAY TONG VIEW THUC CHAY NGAY THUC HIEN CUA SP HD THEO WEBSITE
			SET @v_viewthucchay =
					(
						SELECT MAX(ISNULL(tc.TongViewThucChay,0)) FROM ThucChay tc
						WHERE tc.SoHopDong = @SoHopDong
						AND tc.TypeProduct = @TypeProduct
						AND tc.DmWebsiteREF = @DmWebsiteREF
						AND Convert(DATE,tc.NgayThucHien) = @NgayThucHien	
					)
			SET @v_viewthucchay = ISNULL(@v_viewthucchay,0)		
			--NEU CHUA PHAT SINH VIEW CHO PHAN BO KHUYEN MAI
			IF(@v_tongviewphanbo >= @v_tongviewthucchay + @v_viewthucchay)
				BEGIN
					--Chua phat sinh khuyen mai, Update gia tri KM  = 0
					UPDATE ThucChayDaTinh
					SET
						ThanhTienKM = 0
					WHERE SoHopDong = @SoHopDong
					AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
					AND DmSanPhamREF = dbo.[GetProductIDByTypeProduct](@TypeProduct)
					AND DmWebsiteREF = @DmWebsiteREF
				END
			ELSE
				--PHAT SINH VIEW CHO PHAN BO KHUYEN MAI
				BEGIN
					
					IF((@v_tongviewthucchay > @v_tongviewphanbo) AND ((@v_tongviewthucchay - @v_viewthucchay)<= @v_tongviewphanbo))
						BEGIN
							--@v_viewthucchay
							UPDATE ThucChayDaTinh
							SET
								ThanhTienKM = @v_dongia*(@v_tongviewthucchay- @v_tongviewphanbo)
							WHERE SoHopDong = @SoHopDong
							AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
							AND DmSanPhamREF = dbo.[GetProductIDByTypeProduct](@TypeProduct)
							AND DmWebsiteREF = @DmWebsiteREF
							--PRINT 'phat sinh view TH1 :' + CONVERT(NVARCHAR(100),(@v_dongia*@v_viewthucchay))
						END
					IF((@v_tongviewthucchay > @v_tongviewphanbo) AND ((@v_tongviewthucchay - @v_viewthucchay)>= @v_tongviewphanbo))
						BEGIN
							--@v_tongviewthucchay - @v_tongviewphanbo	
							UPDATE ThucChayDaTinh
							SET
								ThanhTienKM = @v_dongia*@v_viewthucchay
							WHERE SoHopDong = @SoHopDong
							AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
							AND DmSanPhamREF = dbo.[GetProductIDByTypeProduct](@TypeProduct)
							AND DmWebsiteREF = @DmWebsiteREF
							--PRINT 'phat sinh view TH2 :' + CONVERT(NVARCHAR(100),@v_dongia*((@v_tongviewthucchay + @v_viewthucchay) - @v_tongviewphanbo))
						END
				END
		END
	--HD KHONG TON TAI PHAN BO KHUYEN MAI	
	ELSE
		BEGIN
			UPDATE ThucChayDaTinh
			SET
				ThanhTienKM = 0
			WHERE SoHopDong = @SoHopDong
			AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
			AND DmSanPhamREF = dbo.[GetProductIDByTypeProduct](@TypeProduct)
			AND DmWebsiteREF = @DmWebsiteREF
		END
   --PRINT @NgayThucHien
   --PRINT @SoHopDong
   --PRINT @TypeProduct
   --PRINT @DmWebsiteREF
   --PRINT @v_tongviewthucchay
   --PRINT @v_tongviewphanbo
   --PRINT @v_viewthucchay
   --PRINT @v_dongia
   
END

--EXEC [dbo].[ThucChay_UpdateThanhTienKhuyenMai4TCDT_ByHDLoaiSP] '2013-01-1','QC1030313', 8, 341

```
