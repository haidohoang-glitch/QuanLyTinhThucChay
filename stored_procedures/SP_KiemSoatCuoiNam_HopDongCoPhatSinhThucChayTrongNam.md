# Stored Procedure: `KiemSoatCuoiNam_HopDongCoPhatSinhThucChayTrongNam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-28 16:39:07.440000
- **Ngày sửa cuối**: 2016-11-28 16:39:26.577000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE KiemSoatCuoiNam_HopDongCoPhatSinhThucChayTrongNam
	
AS
BEGIN
		----DANH SACH HOP DONG CO PHAT SINH THUC CHAY 2016, CHAY XONG
--1.  LIET KE DOANH SACH HOP DONG CO PHAT SINH THUC CHAY 2016
--2. TINH TONG DOANH SO THUC CHAY CUA CAC HOP DONG NAY (Tru Dang Tin, Tuyen bai, Adpage)

------*******LAM BUOC 1*****----------
CREATE TABLE #HopDong( HopDongID INT)

INSERT #HopDong
        ( HopDongID )
SELECT  HopDongID

FROM dbo.ThucChayDaTinh 
WHERE HopDongID <> 0
AND HopDongChiTietREF <> 0
AND YEAR(NgayThucHien) = 2016
GROUP BY HopDongID
UNION ALL
SELECT HopDongID
FROM dbo.ThucChayDaTinhAdmarket
WHERE HopDongID <> 0
AND HopDongChiTietREF <> 0
AND YEAR(NgayThucHien) = 2016
GROUP BY HopDongID
------*******LAM BUOC 2*****----------

SELECT A.*, hdct.thanhtien, tcdt2016.ThanhTienThucChay  ThanhTienThucChay2016 FROM
(
	SELECT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF
	, tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.DmLoaiBannerREF
	, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay
	, SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) KhuyenMai
	FROM dbo.ThucChayDaTinh tcdt
	WHERE 1=1
	AND (tcdt.DmSanPhamREF NOT IN (299,337,299,144,585,628) AND NOT(tcdt.DmSanPhamREF = 375 
	AND year(tcdt.NgayThucHien) = 2013))
	AND tcdt.DmSanPhamREF NOT IN (141,637,305)
	AND tcdt.HopDongID IN (SELECT HopDongID FROM #HopDong)
	AND tcdt.HopDongChiTietREF <> 0
	GROUP BY tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF
	, tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.DmLoaiBannerREF
	UNION ALL
	SELECT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF
	, tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.DmLoaiBannerREF
	, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay
	, SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) KhuyenMai
	FROM dbo.ThucChayDaTinhAdmarket tcdt
	WHERE  1=1
	AND tcdt.HopDongChiTietREF <>0
	AND tcdt.HopDongID IN (SELECT HopDongID FROM #HopDong)
	GROUP BY tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF
	, tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.DmLoaiBannerREF
)A
INNER JOIN
(
	SELECT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF
	, tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.DmLoaiBannerREF
	, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay
	, SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) KhuyenMai
	FROM dbo.ThucChayDaTinh tcdt
	WHERE 1=1
	AND (tcdt.DmSanPhamREF NOT IN (299,337,299,144,585,628) AND NOT(tcdt.DmSanPhamREF = 375 
	AND year(tcdt.NgayThucHien) = 2013))
	AND tcdt.DmSanPhamREF NOT IN (141,637,305)
	AND tcdt.HopDongID IN (SELECT HopDongID FROM #HopDong)
	AND tcdt.HopDongChiTietREF <> 0
	AND YEAR(tcdt.NgayThucHien) = 2016
	GROUP BY tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF
	, tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.DmLoaiBannerREF
	UNION ALL
	SELECT tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF
	, tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.DmLoaiBannerREF
	, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay
	, SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) KhuyenMai
	FROM dbo.ThucChayDaTinhAdmarket tcdt
	WHERE  1=1
	AND tcdt.HopDongChiTietREF <>0
	AND tcdt.HopDongID IN (SELECT HopDongID FROM #HopDong)
	AND YEAR(tcdt.NgayThucHien) = 2016
	GROUP BY tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF
	, tcdt.DmHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.DmLoaiBannerREF
)tcdt2016 ON tcdt2016.HopDongChiTietREF = A.HopDongChiTietREF
AND tcdt2016.DmHinhThucQuangCao = A.DmHinhThucQuangCao AND  tcdt2016.DmSanPhamREF = A.DmSanPhamREF
INNER JOIN HopDongChitiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID

ORDER BY A.SoHopDong, A.HopDongChiTietREF

DROP TABLE #HopDong


END

```
