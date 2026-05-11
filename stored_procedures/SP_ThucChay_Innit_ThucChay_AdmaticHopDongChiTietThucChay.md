# Stored Procedure: `ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-09 16:37:38.293000
- **Ngày sửa cuối**: 2018-12-10 12:03:34.660000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay] '2018-06-17'
CREATE  PROCEDURE [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay] 
	@NgayThucHien DATETIME
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
	SELECT tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay
	, SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)ThucChayKhuyenMai
	, MAX(tcdt.NgayThucHien)ThucChayDenNgay 
	, SUM(tcdt.SoLuongThucChay + ISNULL(tcdt.SoLuongThayDoi,0))
	, SUM(ISNULL(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0))
	FROM dbo.ThucChayDaTinh tcdt
	WHERE tcdt.DmHinhThucQuangCao = 42
	AND NOT (tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18) --LOAI MUA NGOAI
	AND tcdt.HopDongChiTietREF <> 0
	AND tcdt.NgayThucHien <= @NgayThucHien
	--AND tcdt.HopDongChiTietREF NOT IN 
	--(
	--	SELECT  DISTINCT hopdongchitietID FROM AdmaticThuTuChayHopDongChiTiet 
	--	WHERE ThanhTien >  ISNULL(ThanhtienThucChay,0)
	--)
	GROUP BY tcdt.HopDongChiTietReF
	--UNION ALL
	--SELECT tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay
	--, SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)ThucChayKhuyenMai
	--, MAX(tcdt.NgayThucHien)ThucChayDenNgay 
	--, SUM(tcdt.SoLuongThucChay + ISNULL(tcdt.SoLuongThayDoi,0))
	--, SUM(ISNULL(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0))
	--FROM dbo.ThucChayDaTinhAdmarket tcdt
	--WHERE tcdt.DmHinhThucQuangCao = 42
	--AND NOT (tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18) --LOAI MUA NGOAI
	--AND tcdt.HopDongChiTietREF <> 0
	--AND tcdt.NgayThucHien <= @NgayThucHien
	----AND tcdt.HopDongChiTietREF NOT IN 
	----(
	----		SELECT  DISTINCT hopdongchitietID FROM AdmaticThuTuChayHopDongChiTiet 
	----		WHERE ThanhTien > ISNULL(ThanhtienThucChay,0)
	----)
	--GROUP BY tcdt.HopDongChiTietReF

	--Update tien thuc chay
	UPDATE dbo.AdmaticThuTuChayHopDongChiTiet
	SET ThanhtienThucChay = hdct.DoanhSoThucChay,
	ThucChayDenNgay = hdct.ThucChayDenNgay,
	SoluongThucChay = (
						CASE WHEN (ChietKhau = 100) AND (UPPER(DonViTinh) = 'CPM') THEN hdct.SoLuongthucChayKhuyenMai/1000
							 WHEN (ChietKhau <> 100 OR ChietKhau = 0) AND (UPPER(DonViTinh) = 'CPM') THEN hdct.SoLuongThucChay/1000
							 WHEN (ChietKhau = 100) AND (UPPER(DonViTinh) = 'CPC') THEN hdct.SoLuongthucChayKhuyenMai
							 WHEN (ChietKhau <> 100 OR ChietKhau = 0) AND (UPPER(DonViTinh) = 'CPC') THEN hdct.SoLuongThucChay
							 WHEN (ChietKhau = 100) AND (UPPER(DonViTinh) = 'True View') THEN hdct.SoLuongthucChayKhuyenMai
							 WHEN (ChietKhau <> 100 OR ChietKhau = 0) AND (UPPER(DonViTinh) = 'True View') THEN hdct.SoLuongThucChay
						ELSE 0
						END
					  ),
	Trangthaithucchay = (CASE WHEN thanhtien <= hdct.DoanhSoThucChay AND (chietkhau <> 100 OR ChietKhau = 0)THEN 3
								WHEN thanhtien > hdct.DoanhSoThucChay AND (chietkhau <> 100 OR ChietKhau = 0) AND hdct.DoanhSoThucChay <> 0 THEN 2
								WHEN (chietkhau = 100) AND (hdct.DoanhSoThucChayKhuyenMai >= DonGia*SoLuong) THEN 3
								WHEN (chietkhau = 100) AND (hdct.DoanhSoThucChayKhuyenMai < DonGia*SoLuong) AND (hdct.DoanhSoThucChayKhuyenMai <> 0) THEN 2
								WHEN (chietkhau = 100) AND (hdct.DoanhSoThucChayKhuyenMai = 0) THEN 1
								WHEN (chietkhau <> 100 OR ChietKhau = 0) AND (hdct.DoanhSoThucChay = 0) THEN 1
								ELSE 0
							END
							)
	FROM (
		SELECT tt.HopDongChiTietID ,
	        ISNULL(hdct.DoanhSoThucChay,0)DoanhSoThucChay ,
			ISNULL(hdct.DoanhSoThucChayKhuyenMai,0)DoanhSoThucChayKhuyenMai,
	        hdct.ThucChayDenNgay,
			ISNULL(hdct.SoLuongThucChay,0)SoLuongThucChay,
			ISNULL(hdct.SoLuongthucChayKhuyenMai,0)SoLuongthucChayKhuyenMai 
			FROM dbo.AdmaticThuTuChayHopDongChiTiet tt 
		LEFT JOIN #AdmaticHopDongChiTietThucChay hdct ON tt.HopDongChiTietID = hdct.HopDongChitietID
	) hdct
	WHERE hdct.HopDongChitietID = AdmaticThuTuChayHopDongChiTiet.HopDongChiTietID
	--AND AdmaticThuTuChayHopDongChiTiet.Trangthaithucchay <> 3
	--Update trang thai thuc chay
	
END

```
