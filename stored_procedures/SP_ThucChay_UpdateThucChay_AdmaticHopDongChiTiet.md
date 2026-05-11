# Stored Procedure: `ThucChay_UpdateThucChay_AdmaticHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-28 15:10:19.190000
- **Ngày sửa cuối**: 2019-12-24 17:06:52.897000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
	'2018-06-29',528833
*/
CREATE  PROCEDURE [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
	@NgayThucHien DATETIME,
	@HopDongChiTietID INT
AS
BEGIN
	CREATE TABLE #AdmaticHopDongChiTietThucChay
	(
		HopDongChitietID INT,
		DoanhSoThucChay BIGINT,
		DoanhSoThucChayKhuyenMai BIGINT,
		ThucChayDenNgay DATETIME,
		SoLuongThucChay BIGINT,
		SoLuongthucChayKhuyenMai BIGINT

	)
	--CAP NHAT TRANG THAI THUC CHAY VA THANH TIEN THUC CHAY
	INSERT INTO #AdmaticHopDongChiTietThucChay
	    ( HopDongChitietID ,
	        DoanhSoThucChay ,
			DoanhSoThucChayKhuyenMai,
	        ThucChayDenNgay,
			SoLuongThucChay,
			SoLuongthucChayKhuyenMai
	    )
	SELECT tcdt.HopDongChiTietREF, ROUND((SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)),0) ThanhTienThucChay
	, ROUND((SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)),0)ThucChayKhuyenMai
	, MAX(tcdt.NgayThucHien)ThucChayDenNgay 
	, SUM(tcdt.SoLuongThucChay + ISNULL(tcdt.SoLuongThayDoi,0)) AS SoLuongThucChay
	, SUM(ISNULL(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0)) AS SoLuongThucChayKM
	FROM dbo.ThucChayDaTinh tcdt
	WHERE tcdt.DmHinhThucQuangCao = 42
	AND NOT (tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18) --LOAI MUA NGOAI
	AND tcdt.HopDongChiTietREF <> 0
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	AND tcdt.NgayThucHien <= @NgayThucHien
	GROUP BY tcdt.HopDongChiTietReF

	--Update tien thuc chay
	UPDATE ad
	SET ad.ThanhtienThucChay = hdct.DoanhSoThucChay,
	ad.ThucChayDenNgay = hdct.ThucChayDenNgay,
	ad.SoluongThucChay = (
						CASE WHEN (ad.ChietKhau = 100) AND (UPPER(ad.DonViTinh) = 'CPM') THEN hdct.SoLuongthucChayKhuyenMai/1000
							 WHEN (ad.ChietKhau <> 100 OR ad.ChietKhau = 0) AND (UPPER(ad.DonViTinh) = 'CPM') THEN hdct.SoLuongThucChay/1000
							 WHEN (ad.ChietKhau = 100) AND (UPPER(ad.DonViTinh) = 'CPC') THEN hdct.SoLuongthucChayKhuyenMai
							 WHEN (ad.ChietKhau <> 100 OR ad.ChietKhau = 0) AND (UPPER(ad.DonViTinh) = 'CPC') THEN hdct.SoLuongThucChay
							 WHEN (ad.ChietKhau = 100) AND (UPPER(ad.DonViTinh) = 'TRUE VIEW') THEN hdct.SoLuongthucChayKhuyenMai
							 WHEN (ad.ChietKhau <> 100 OR ad.ChietKhau = 0) AND (UPPER(ad.DonViTinh) = 'TRUE VIEW') THEN hdct.SoLuongThucChay
						ELSE 0
						END
					  ),
	ad.Trangthaithucchay = (CASE WHEN ad.thanhtien <= hdct.DoanhSoThucChay AND (ad.chietkhau <> 100 OR ad.ChietKhau = 0)THEN 3
								WHEN ad.thanhtien > hdct.DoanhSoThucChay AND (ad.chietkhau <> 100 OR ad.ChietKhau = 0) AND hdct.DoanhSoThucChay <> 0 THEN 2
								WHEN (ad.chietkhau = 100) AND (hdct.DoanhSoThucChayKhuyenMai >= ad.DonGia*ad.SoLuong) THEN 3
								WHEN (ad.chietkhau = 100) AND (hdct.DoanhSoThucChayKhuyenMai < ad.DonGia*ad.SoLuong) THEN 2
								WHEN (ad.chietkhau = 100) AND (hdct.DoanhSoThucChayKhuyenMai = 0) THEN 1
								WHEN (ad.chietkhau <> 100 OR ad.ChietKhau = 0) AND (hdct.DoanhSoThucChay = 0) THEN 1
								ELSE 0
							END
							)
	FROM dbo.AdmaticThuTuChayHopDongChiTiet ad INNER JOIN #AdmaticHopDongChiTietThucChay hdct
	on hdct.HopDongChitietID = ad.HopDongChiTietID
	--AND AdmaticThuTuChayHopDongChiTiet.Trangthaithucchay <> 3
	--Update trang thai thuc chay
	
END

```
