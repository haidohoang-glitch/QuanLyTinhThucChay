# Stored Procedure: `ThucChay_CheckHopDongXoaPhanBo_CPDKhongDotChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-01 14:37:39.950000
- **Ngày sửa cuối**: 2024-08-21 16:12:00.290000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoLuongHT` | `int(4)` | No |
| `@ThanhTienHDCT` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongXoaPhanBo_CPDKhongDotChay] 

	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@SoLuongHT INT,
	@ThanhTienHDCT FLOAT
AS
BEGIN
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500)
	DECLARE @TenWebste NVARCHAR(100), @TenChuyenMuc NVARCHAR(100), @TenBanner NVARCHAR(100), @GiaTriThayDoi FLOAT
	DECLARE @Soluong INT , @DonGia INT	, @CountHDTD INT, @DmSanPhamREF INT, @DmWebsiteREF INT
	DECLARE @GiaTriThucChayDatinh FLOAT, @SoLuongThucchayDatinh FLOAT, @GiatriKMDatinh FLOAT, @SoluongKMDatinh FLOAT
	
	--1. Lấy thông tin phân bổ
	SELECT TOP 1 
			@TenWebste = hdcttd.TenWebsite, @TenChuyenMuc = hdcttd.TenChuyenMuc
			,@TenBanner = hdcttd.TenViTri, @Soluong = hdcttd.SoLuong, @DonGia = hdcttd.DonGia
			, @DmSanPhamREF = hdcttd.DmSanPhamREF, @DmWebsiteREF = hdcttd.DmWebsiteREF
	FROM HopDongThayDoi hdtd
	INNER JOIN HopDongChiTietThayDoi hdcttd 
	ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
	WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
		AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
	ORDER BY hdcttd.HopDongChiTietThayDoiID 
	
	SET @TenWebste = ISNULL(@TenWebste,'')
	SET @TenChuyenMuc = ISNULL(@TenChuyenMuc, '')
	SET @TenBanner = ISNULL(@TenBanner,'')
	SET @Soluong = ISNULL(@Soluong, 0)
	SET @DonGia = ISNULL(@DonGia, 0)
	SET @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
	SET @DmWebsiteREF = ISNULL(@DmWebsiteREF,0)
		
	SET @CONTENT_LOG = @CONTENT_LOG + N'[ThucChay_CheckHopDongXoaPhanBo_CPDKhongDotChay], ' + N'Phân bổ :' + @TenWebste + '->' + @TenChuyenMuc + '->' + @TenBanner
		
	--2. Xác định số lượng, giá trị thay đổi do xóa phân bổ
	SELECT @SoLuongThucchayDatinh = SUM(ISNULL(tcdt.SoLuongThucChay,0)) + SUM(ISNULL(tcdt.SoLuongThayDoi,0))  ,
			@GiaTriThucChayDatinh = SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)) + SUM(ISNULL(tcdt.GiaTriThayDoi,0)) ,
			@SoluongKMDatinh = SUM(ISNULL(tcdt.SoLuongThucChayKM,0)) + SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) ,
			@GiatriKMDatinh = SUM(ISNULL(tcdt.ThanhTienKM,0)) + SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien 
			AND tcdt.HopDongChiTietREF= @HopDongChiTietID

	--3. Đối trừ thay đổi
	IF isnull(@GiatriKMDatinh, 0) <>0
	BEGIN
		SET @SoLuongThucchayDatinh = isnull(@SoLuongThucchayDatinh, 0)
		SET @GiaTriThucChayDatinh = isnull(@GiaTriThucChayDatinh, 0)
		SET @SoluongKMDatinh = isnull(@SoluongKMDatinh, 0)
		SET @GiatriKMDatinh = isnull(@GiatriKMDatinh, 0)

		EXEC [dbo].ThucChay_InsertKhuyenMaiThayDoi_CPDKhongDotChay 
				@HopDongChiTietID ,@NgaythucHien  ,
				0 , 
				0 , 
				0 , 
				0 	
	END
	ELSE
		IF isnull(@GiaTriThucChayDatinh, 0) <>0 
		BEGIN
			SET @CountHDTD = 
			(
				SELECT COUNT(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
				WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
				AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
			)
			set @GiaTriThayDoi= - @GiaTriThucChayDatinh

			IF(@CountHDTD >0)
			BEGIN
				UPDATE ThucChayDaTinh
				SET	GiaTriThayDoi = @GiaTriThayDoi
				, LastModifiedAt = GETDATE()
				, GhiChu = @CONTENT_LOG
				WHERE HopDongID = @HopDongREF
				AND HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien = @NgayThucHien 
			END
			ELSE
				BEGIN
					EXEC [dbo].[ThucChay_InsertThucTreoThayDoi_CPDKhongDotChay] @HopDongChiTietID,@NgaythucHien,@GiaTriThayDoi
				END			
		END
END

```
