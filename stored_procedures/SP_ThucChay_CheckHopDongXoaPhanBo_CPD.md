# Stored Procedure: `ThucChay_CheckHopDongXoaPhanBo_CPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-02 13:02:52.103000
- **Ngày sửa cuối**: 2024-08-21 15:58:42.443000

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

CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongXoaPhanBo_CPD] 
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@SoLuongHT INT,
	@ThanhTienHDCT FLOAT
AS
BEGIN

	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500)
	DECLARE @TenWebste NVARCHAR(100), @TenChuyenMuc NVARCHAR(100), @TenBanner NVARCHAR(100), @GiaTriThayDoi FLOAT, @SoLuongThayDoi FLOAT
	DECLARE @Soluong INT , @DonGia INT	, @CountHDTD INT, @DmSanPhamREF INT, @DmWebsiteREF INT
	DECLARE @SoluongKMThayDoi FLOAT, @GiatriKMThayDoi FLOAT
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
		
	SET @CONTENT_LOG = @CONTENT_LOG + N'Phân bổ :' + @TenWebste + '->' + @TenChuyenMuc + '->' + @TenBanner
	SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi:' + 	CONVERT(NVARCHAR(30),@HopDongChiTietID)
	
	--2. Xác định số lượng, giá trị thay đổi do xóa phân bổ
	SELECT  @SoLuongThayDoi = SUM(ISNULL(tcdt.SoLuongThucChay,0)) + SUM(ISNULL(tcdt.SoLuongThayDoi,0))  ,
		    @GiaTriThayDoi = SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)) + SUM(ISNULL(tcdt.GiaTriThayDoi,0)) ,
			@SoluongKMThayDoi = SUM(ISNULL(tcdt.SoLuongThucChayKM,0)) + SUM(ISNULL(tcdt.SoLuongKMThayDoi,0)) ,
			@GiatriKMThayDoi = SUM(ISNULL(tcdt.ThanhTienKM,0)) + SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien 
	AND tcdt.HopDongChiTietREF= @HopDongChiTietID

	--3. Đối trừ thay đổi
	set @GiaTriThayDoi= ISNULL(@GiaTriThayDoi,0)
	set @SoLuongThayDoi= ISNULL(@SoLuongThayDoi,0)
	set @SoluongKMThayDoi= ISNULL(@SoluongKMThayDoi,0)
	set @GiatriKMThayDoi= ISNULL(@GiatriKMThayDoi,0)

	IF round(@GiaTriKMThayDoi, 2) <> 0
	BEGIN
		EXEC [dbo].ThucChay_InsertKhuyenMaiThayDoi_CPD 
				@HopDongChiTietID ,@NgaythucHien  ,
				0 , 
				0 , 
				0 , 
				0
	END
	ELSE
		IF (@GiaTriThayDoi <>0)
		BEGIN
			SET @CountHDTD = 
			(
				SELECT COUNT(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
				WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
				AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
			)
			set @GiaTriThayDoi= - @GiaTriThayDoi
			set @SoLuongThayDoi= - @SoLuongThayDoi

			IF(@CountHDTD >0)
			BEGIN
				
				UPDATE ThucChayDaTinh
				SET	GiaTriThayDoi = @GiaTriThayDoi
					, SoLuongThayDoi = @SoLuongThayDoi
				, LastModifiedAt = GETDATE()
				, ghichu = 'SP: ThucChay_CheckHopDongXoaPhanBo_CPD,' + @NGUON_LOG +', ' + @CONTENT_LOG
				WHERE HopDongID = @HopDongREF
				AND HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien = @NgayThucHien 
			END
			ELSE
				BEGIN
					EXEC [dbo].[ThucChay_InsertThucTreoThayDoi_CPD] @HopDongChiTietID,@NgaythucHien,@GiaTriThayDoi, @SoLuongThayDoi
				END			
		END
	
END

```
