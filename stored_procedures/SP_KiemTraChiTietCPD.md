# Stored Procedure: `KiemTraChiTietCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-14 16:56:02.947000
- **Ngày sửa cuối**: 2017-02-14 16:56:02.947000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE KiemTraChiTietCPD 
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

--------------------XỬ LÝ DỮ LIỆU PHÁT SINH----------------------------------------
-----------------------hd co dot chay----------------------
--EXEC ThucChay_InsertThucChayDaTinh_CPDBySoHopDongDotChay   '2017-01-11','2017-01-11', 'NB0090117', 140
--EXEC ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDByHopDongChiTiet '2017-02-13', 500152, 500434
----------------------Tinh thuc chay khong dot chay ----------------------
--EXEC ThucChay_InsertThucChayDaTinh_CPD_KhongDotChayBySoHopDong  '2016-11-19','2016-11-20','QC2071116'
--exec ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChayBySHD 45125, 'QC2930816',101018, '2016-12-26'
----------------------TMDT -----------------------------------------------
--EXEC ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_TMDTByHopDongChiTiet 26468, 'PC060614',99147, '2016-08-17'

-------Update nhan hang tcdt theo dung thực treo-------------------------------------------------------
--sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_Manual  @NgayThucHien DATETIME,@HopDongID INT,@PhanBoID INT,@NhanHangOld NVARCHAR(50)
--sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_Manual '2017-01-12' ,500140 ,500338 ,'139913'

SELECT

hd.HopDongID, hd.TenKhachHang
, hd.SoHopDong
, hdct.HopDongChiTietID, NhanHang, DanhSachNhanHangREF
, hdct.DmSanPhamREF
, hdct.TenSanPham
, hdct.TenLoai
, hdct.TenWebsite
, hdct.DonGia
, hdct.ChietKhau
, hdct.ThanhTien
, hdct.ThanhtienThucChay
, ROUND(hdct.ThanhTien - hdct.ThanhtienThucChay,0) [ThanhTienHD - TTTC]
FROM HopDong hd INNER JOIN HopDongChiTiet hdct
ON hd.HopDongID = hdct.HopDongFK
WHERE 1=1
--AND hd.HopDongID = 29714
and hd.SoHopDong = @SoHopDong
--AND hdct.HopDongChiTietID = @HopDongChiTietID
--AND hdct.TenWebsite LIKE N'Vneconomy'
--AND hdct.HopDongChiTietID = 49135
AND hdct.DeletedStatus = 0
--AND hd.TrangThaiHopDong <> 3
AND hdct.DmSanPhamREF IN (140,228,549,564,385)

--SELECT * FROM ThucChay_LogNNTinhGiaTriThayDoi tclngttd 
--WHERE tclngttd.HopDongREF = (SELECT hd.HopDongID FROM HopDong hd WHERE hd.SoHopDong = @SoHopDong)
--,AND tclngttd.HopDongChiTietREF = @HopDongChiTietID
--SELECT * FROM HopDongChiTietLog hdctl WHERE hdctl.HopDongChiTietREF = @HopDongChiTietID
--SELECT * FROM HopDongLog hdl WHERE hdl.HopDongID =  (SELECT hd.HopDongID FROM HopDong hd WHERE hd.SoHopDong = @SoHopDong)
SELECT 'HDThayDoi'[HDThayDoi],
 hdtd.HopDongThayDoiID
, hdtd.HopDongFK
, hdcttd.HopDongChiTietREF
, hdtd.NgayThayDoi
, hdcttd.SoLuong
, hdcttd.DonViTinh
, hdcttd.DonGia
, hdcttd.ChietKhau
, hdcttd.ThanhTien
, hdtd.GiaTriHopDong  
, hdcttd.LastModifiedBy
FROM HopDongThayDoi hdtd INNER JOIN HopDongChiTietThayDoi hdcttd
ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
WHERE 
--CONVERT(date, hdtd.NgayThayDoi) BETWEEN '2013-11-09' AND '2013-11-17' 
hdcttd.HopDongFK = (SELECT hd.HopDongID
                      FROM HopDong hd WHERE hd.SoHopDong = @SoHopDong)
AND hdcttd.HopDongChiTietREF = @HopDongChiTietID

SELECT 'ThongTinHD' [ThongTinHD], hd.TrangThaiHopDong,DotChayHopDongChiTietID, hd.SoHopDong, hdct.HopDongChiTietID, hd.TenNhanVien,SysNhanVienREF

, hdct.NhanHang , DanhSachNhanHangREF
, hdct.TenLoai
, hdct.DmSanPhamREF
, hdct.TenSanPham, hdct.DmWebsiteREF
, hdct.TenWebsite + ', ' + ISNULL(hdct.TenChuyenMuc, '') +', '+ ISNULL(hdct.TenViTri, '') AS Vitri
, hdct.SoLuong
, hdct.DonViTinh, DonViTinhREF
, SUM(DATEDIFF(DAY, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc)+1) AS SoLuongDC
, hdct.DonGia
, hdct.ChietKhau
, hdct.ThanhTien
, hdct.IsKhuyenMai
, hd.CreatedBy
, dchdct.BookingREF
, CONVERT(DATE,dchdct.ThoiGianBatDau)ThoiGianBatDau, CONVERT(DATE,dchdct.ThoiGianKetThuc)ThoiGianKetThuc
, hdct.LastModifiedAt LastModifiedAtpb
, hd.LastModifiedAt
, hdct.GhiChu
, hdct.DeletedStatus, hdct.DmBannerREF, hdct.DmLoaiBannerREF, hdct.LastModifiedBy
FROM   HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
LEFT JOIN DotChayHopDongChiTiet dchdct ON( hdct.HopDongChiTietID = dchdct.HopDongChiTietREF AND dchdct.DeletedStatus <> 1)
WHERE  hd.SoHopDong = @SoHopDong
AND hdct.HopDongChiTietID = @HopDongChiTietID
AND hd.TrangThaiHopDong <> 3
--AND hdct.DeletedStatus = 0
GROUP BY  hd.TrangThaiHopDong,DanhSachNhanHangREF,DotChayHopDongChiTietID,SysNhanVienREF,
hd.SoHopDong, hdct.HopDongChiTietID, hd.TenNhanVien
, hdct.NhanHang 
, hdct.DmSanPhamREF
, hdct.TenSanPham, hdct.DmWebsiteREF
, hdct.TenWebsite , hdct.TenChuyenMuc, hdct.TenViTri
, hdct.SoLuong
, hdct.DonViTinh, DonViTinhREF
, hdct.ChietKhau
, hdct.ThanhTien
, hd.CreatedBy
, hdct.IsKhuyenMai
, dchdct.BookingREF
, dchdct.ThoiGianBatDau,dchdct.ThoiGianKetThuc
, hdct.DonGia
, hdct.LastModifiedAt
, hd.LastModifiedAt
, hdct.TenLoai
, hdct.GhiChu
, hdct.DeletedStatus, hdct.DmBannerREF, hdct.DmLoaiBannerREF, hdct.LastModifiedBy
ORDER BY dchdct.ThoiGianBatDau
----------------------
----------------------------------------------
SELECT tchdct.ThucChayHopDongChiTietID,tchdct.HopDongREF, tchdct.HopDongChiTietREF, NhanHang, DmNhanHangREF
, CONVERT(DATE,tchdct.ThoiGianBatDau)ThoiGianBatDau, CONVERT(DATE,tchdct.ThoiGianKetThuc) ThoiGianKetThuc
, DATEDIFF(DAY,tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc)+1 AS SoLuongTreo
, tchdct.BookingREF, tchdct.DmBannerREF
, tchdct.CreatedAt, tchdct.LastModifiedAt 
, tchdct.DeletedStatus,tchdct.CreatedBy,tchdct.LastModifiedBy
FROM ThucChayHopDongChiTiet tchdct 
WHERE tchdct.HopDongChiTietREF = @HopDongChiTietID
AND tchdct.DeletedStatus <> 1


SELECT tcdt.TenKhachHang,
tcdt.ThucChayDaTinhID, tcdt.SoHopDong , TenDangNhap, TenNhanVien
, tcdt.HopDongChiTietREF, NhanHang, GhiChu
, tcdt.TenSanPham
       , tcdt.SoLuong
       , tcdt.TenWebsite, tcdt.DmWebsiteREF
       , CASE WHEN tcdt.IsKhuyenMai = 0 THEN tcdt.SoLuongThucChay ELSE tcdt.SoLuongThucChayKM END SoLuongChay 
       , tcdt.SoLuongThayDoi
       , tcdt.SoLuongKMThayDoi
       , tcdt.DonViTinh
       , tcdt.DmSanPhamREF 
       , tcdt.ChietKhau   
       , tcdt.SoLuongDotChayHD
       , tcdt.SoLuongDotChayBooking
       , tcdt.DonGiaTheoDonVi      
       , tcdt.ThanhTienThucChayTruocTrietKhau
       , tcdt.ThanhTienSauTrietKhauThucChay
       , tcdt.ThanhTienKM, tcdt.GiaTriKMThayDoi
       , tcdt.GiaTriThayDoi
       , tcdt.NgayThucHien
       , tcdt.DotChayHopDong
       , tcdt.DotChayBooking  
       , tcdt.TrangThaiHopDong
       , tcdt.LastModifiedAt
       , tcdt.CreatedAt, tcdt.DotChayHopDong
       , tcdt.TrangThaiHopDong
 --, tcdt.SoLuongThayDoi              
FROM   ThucChayDaTinh tcdt
WHERE 1=1  
	--tcdt.SoHopDong = @SoHopDong
       AND tcdt.HopDongChiTietREF = @HopDongChiTietID
       --AND CONVERT(date, tcdt.NgayThucHien) BETWEEN '2013-08-26' AND '2013-12-31'  
       --AND tcdt.DmWebsiteREF = 137
ORDER BY tcdt.NgayThucHien


SELECT tcdt.TenKhachHang, tcdt.SoHopDong, tcdt.HopDongID, tcdt.HopDongChiTietREF, DmSanPhamREF, tcdt.NhanHang
, SUM(tcdt.ThanhTienSauTrietKhauThucChay) AS TienThucChay
, ROUND(sum(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) AS tttc_final
, SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SL
, SUM(tcdt.SoLuongThucChayKM) AS slKM
, ROUND(SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi),0) AS ttkm
, SUM(tcdt.GiaTriThayDoi) AS gttd
FROM   ThucChayDaTinh tcdt
WHERE  1=1

       AND tcdt.HopDongChiTietREF = @HopDongChiTietID

GROUP BY tcdt.TenKhachHang, tcdt.SoHopDong,tcdt.HopDongID, tcdt.HopDongChiTietREF, DmSanPhamREF, tcdt.NhanHang

END

```
