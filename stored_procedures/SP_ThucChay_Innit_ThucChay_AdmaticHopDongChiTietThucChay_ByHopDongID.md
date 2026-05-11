# Stored Procedure: `ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay_ByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-15 18:00:25.063000
- **Ngày sửa cuối**: 2018-10-22 17:04:14.247000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongFK` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay_ByHopDongID] 1007564,  '2018-10-22'
*/

CREATE  PROCEDURE [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay_ByHopDongID] 
	@HopDongFK INT,
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

	UPDATE dbo.AdmaticThuTuChayHopDongChiTiet
	SET ThanhTien = hdct.ThanhTien
	FROM dbo.AdmaticThuTuChayHopDongChiTiet at
	INNER JOIN dbo.HopDongChiTiet hdct ON at.HopDongFK = hdct.HopDongFK
	AND hdct.HopDongChiTietID = at.HopDongChiTietID

	--CAP NHAT TRANG THAI THUC CHAY VA THANH TIEN THUC CHAY
	INSERT INTO #AdmaticHopDongChiTietThucChay
	    ( HopDongChitietID ,
	        DoanhSoThucChay ,
			DoanhSoThucChayKhuyenMai,
	        ThucChayDenNgay,
			SoLuongThucChay,
			SoLuongthucChayKhuyenMai
	    )
	SELECT DISTINCT A.HopDongChiTietREF,
                    A.ThanhTienThucChay,
                    A.ThucChayKhuyenMai,
                    A.ThucChayDenNgay,
                    A.SoluongThucChay,
                    A.SoLuongThucChayKM FROM
	(
		SELECT tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay
		, SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)ThucChayKhuyenMai
		, MAX(tcdt.NgayThucHien)ThucChayDenNgay 
		, SUM(tcdt.SoLuongThucChay + ISNULL(tcdt.SoLuongThayDoi,0)) AS SoluongThucChay
		, SUM(ISNULL(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0)) AS SoLuongThucChayKM
		FROM dbo.ThucChayDaTinh tcdt
		WHERE tcdt.DmHinhThucQuangCao = 42
		AND NOT (tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18) --LOAI MUA NGOAI
		AND tcdt.HopDongChiTietREF <> 0
		AND tcdt.HopDongID = @HopDongFK
		AND tcdt.NgayThucHien <= @NgayThucHien
		--AND tcdt.HopDongChiTietREF NOT IN (SELECT  DISTINCT hopdongchitietID FROM AdmaticThuTuChayHopDongChiTiet WHERE trangthaithucchay = 3)
		GROUP BY tcdt.HopDongChiTietReF
		UNION ALL
		SELECT tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay
		, SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)ThucChayKhuyenMai
		, MAX(tcdt.NgayThucHien)ThucChayDenNgay 
		, SUM(tcdt.SoLuongThucChay + ISNULL(tcdt.SoLuongThayDoi,0)) AS SoluongThucChay
		, SUM(ISNULL(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0)) AS SoLuongThucChayKM
		FROM dbo.ThucChayDaTinhAdmarket tcdt
		WHERE tcdt.DmHinhThucQuangCao = 42
		AND NOT (tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18) --LOAI MUA NGOAI
		AND tcdt.HopDongChiTietREF <> 0
		AND tcdt.HopDongID = @HopDongFK
		AND tcdt.NgayThucHien <= @NgayThucHien
		--AND tcdt.HopDongChiTietREF NOT IN (SELECT  DISTINCT hopdongchitietID FROM AdmaticThuTuChayHopDongChiTiet WHERE trangthaithucchay = 3)
		GROUP BY tcdt.HopDongChiTietReF
	)A
	SELECT DISTINCT * FROM #AdmaticHopDongChiTietThucChay

	--Update tien thuc chay
	UPDATE dbo.AdmaticThuTuChayHopDongChiTiet
	SET ThanhtienThucChay = hdct.DoanhSoThucChay,
	ThucChayDenNgay = hdct.ThucChayDenNgay,
	SoluongThucChay = (
						CASE WHEN (ChietKhau = 100) AND (UPPER(DonViTinh) = 'CPM') THEN hdct.SoLuongthucChayKhuyenMai/1000
							 WHEN (ChietKhau <> 100 OR ChietKhau = 0) AND (UPPER(DonViTinh) = 'CPM') THEN hdct.SoLuongThucChay/1000
							 WHEN (ChietKhau = 100) AND (UPPER(DonViTinh) = 'CPC') THEN hdct.SoLuongthucChayKhuyenMai
							 WHEN (ChietKhau <> 100 OR ChietKhau = 0) AND (UPPER(DonViTinh) = 'CPC') THEN hdct.SoLuongThucChay
							 WHEN (ChietKhau = 100) AND (UPPER(DonViTinh) = 'TRUE VIEW') THEN hdct.SoLuongthucChayKhuyenMai
							 WHEN (ChietKhau <> 100 OR ChietKhau = 0) AND (UPPER(DonViTinh) = 'TRUE VIEW') THEN hdct.SoLuongThucChay
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
