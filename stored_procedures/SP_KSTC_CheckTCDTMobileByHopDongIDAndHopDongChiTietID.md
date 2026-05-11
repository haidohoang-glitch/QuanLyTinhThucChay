# Stored Procedure: `KSTC_CheckTCDTMobileByHopDongIDAndHopDongChiTietID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-08 17:01:40.220000
- **Ngày sửa cuối**: 2014-12-08 17:01:40.220000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckTCDTMobileByHopDongIDAndHopDongChiTietID 
	-- Add the parameters for the stored procedure here
	@HopDongID INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN

SELECT deletedstatus,HopDongChiTietID, hdct.DonViTinh, hdct.DonGia, hdct.IsKhuyenMai,hdct.DeletedStatus, hdct.ThanhTien,hdct.ChietKhau,hdct.SoLuong,		
hdct.GiamGia,hdct.ThanhTien,		
dbo.GetSoHopDongByID(hdct.HopDongFK),hdct.HopDongFK		
           FROM HopDongChiTiet hdct WHERE hdct.HopDongFK = @HopDongID  		
           AND hdct.DmSanPhamREF = 342 AND hdct.HopDongFK NOT IN (SELECT HopDongID		
                                                                    FROM HopDong WHERE TrangThaiHopDong = 3)		
   		
SELECT * FROM HopDongChiTietLog hdctl WHERE hdctl.HopDongChiTietREF = @HopDongChiTietID		
SELECT * FROM HopDongChiTietThayDoi hdcttd WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID		
--Du lieu temp		
SELECT GiaTriHopDong FROM HopDong WHERE HopDongID = @HopDongID		
SELECT SUM(tcmt.TongViewThucChay)tv,SUM(tcmt.TongClickThucChay)tc,tcmt.ProductUnitName,tcmt.HopDongChiTietREF		
FROM ThucChay_MobileTemp tcmt WHERE tcmt.HopDongChiTietREF = @HopDongChiTietID		
AND tcmt.NgayThucHien <=@NgayThucHien 		
GROUP BY tcmt.ProductUnitName,tcmt.HopDongChiTietREF		
		
--Du lieu thuc chay
SELECT SUM(tcmt.TongViewThucChay)tv, SUM(tcmt.TongClickThucChay) tc,tcmt.ProductUnitName,tcmt.HopDongChiTietREF		
FROM ThucChay tcmt WHERE tcmt.HopDongChiTietREF = @HopDongChiTietID		
AND tcmt.NgayThucHien <=@NgayThucHien   		
AND tcmt.TypeProduct = 10		
GROUP BY tcmt.ProductUnitName,tcmt.HopDongChiTietREF		
          		
--Du lieu tcdt	
SELECT year(ngaythuchien),hopdongchitietref,tcdtm.DonViTinh,dongia,tcdtm.DonGiaTheoDonVi,ChietKhau,		
tcdtm.TenHinhThucQuangCao,		
SUM(tcdtm.TongViewThucChay)tv, SUM(tcdtm.TongClickThucChay)tc,SUM(tcdtm.SoLuongThayDoi) sltd,		
SUM(tcdtm.SoLuongThucChayKM + tcdtm.SoLuongKMThayDoi)slkm,		
SUM(tcdtm.SoLuongThucChay)sltc,SUM(tcdtm.SoLuongThucChayLechTreoHa)sllth,		
SUM(tcdtm.ThanhTienSauTrietKhauThucChay+tcdtm.GiaTriThayDoi)tt, SUM(tcdtm.ThanhTienLechTreoHa)lth	,SUM(tcdtm.ThanhTienKM + tcdtm.GiaTriKMThayDoi) ttkm	
  FROM ThucChayDaTinh tcdtm WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID		
  AND tcdtm.NgayThucHien <=@NgayThucHien		
GROUP BY tcdtm.DonViTinh,tcdtm.DonGia, tcdtm.DonGiaTheoDonVi,YEAR(tcdtm.NgayThucHien),ChietKhau,tcdtm.HopDongChiTietREF,tcdtm.TenHinhThucQuangCao		
--Du lieu tcdt mobile
SELECT year(ngaythuchien),hopdongchitietref,tcdtm.DonViTinh,dongia,tcdtm.DonGiaTheoDonVi,ChietKhau,		
SUM(tcdtm.TongViewThucChay)tv, SUM(tcdtm.TongClickThucChay)tc,		
SUM(tcdtm.SoLuongThucChayKM)slkm,		
SUM(tcdtm.SoLuongThucChay)sltc,SUM(tcdtm.SoLuongThucChayLechTreoHa)sllth,		
SUM(tcdtm.ThanhTienSauTrietKhauThucChay+tcdtm.GiaTriThayDoi)tt, SUM(tcdtm.ThanhTienLechTreoHa)lth	,SUM(tcdtm.ThanhTienKM) ttkm	
  FROM ThucChayDaTinhMobile tcdtm WHERE tcdtm.HopDongChiTietREF = @HopDongChiTietID		
  AND tcdtm.NgayThucHien <=@NgayThucHien		
GROUP BY tcdtm.DonViTinh,tcdtm.DonGia, tcdtm.DonGiaTheoDonVi,YEAR(tcdtm.NgayThucHien),ChietKhau,tcdtm.HopDongChiTietREF		

END

```
