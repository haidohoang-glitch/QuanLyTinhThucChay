# Stored Procedure: `ThucChayKiemTra_AdX`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-26 16:15:18.737000
- **Ngày sửa cuối**: 2014-12-12 11:28:36.760000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

-- EXC [dbo].[ThucChayKiemTra_AdX] '2014-11-19'

CREATE PROCEDURE [dbo].[ThucChayKiemTra_AdX]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DateTime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
SELECT T1.*, T2.username, T2.TongClickThucChay, T2.TongViewThucChay, T2.SoLuongThucChay, T2.ThanhTienSauTrietKhauThucChay, T2.ThanhTienKM,  
T2.SoLuongThucChayOnline, T2.TienThucChayOnline, T2.TienKhuyenMaiOnline, T2.TongTien
,(T1.ttc- T2.SoLuongThucChay - T2.SoLuongThucChayOnline) Lech_SoLuong
,(T1.ThanhTienThucChay - T2.ThanhTienSauTrietKhauThucChay-T2.TienThucChayOnline) Lech_Tien_thucchay
,(T1.ThanhTienKM-T2.ThanhTienKM-T2.TienKhuyenMaiOnline) Lech_tienKM
,(T1.TongTien - T2.TongTien) Lech_TongTien
FROM
(
 SELECT 
  T.DmSanPhamREF, T.TenSanPham,
  T.username,T.ttc, T.ttv,
  SUM(T.ThanhTienThucChay) AS ThanhTienThucChay,
  SUM(T.ThanhTienKM) AS ThanhTienKM,
  SUM(T.ThanhTienThucChay + T.ThanhTienKM) AS TongTien
 FROM
 (
  SELECT distinct 
   A.DmSanPhamREF, A.TenSanPham, A.username,A.ttv, A.ttc,
    A.ttc as SoLuong,
   CASE A.IsNoiBo
    WHEN 1 THEN (A.[money] + A.pro)/1.1
    ELSE A.[money]/1.1
   END ThanhTienThucChay,
   CASE A.IsNoiBo
    WHEN 1 THEN 0
    ELSE A.pro/1.1
   END ThanhTienKM
  FROM ThucChayAdXforUsers A
   INNER JOIN HopDongChiTiet B ON B.TK_AdMarket = A.username AND A.DmSanPhamREF = B.DmSanPhamREF
   INNER JOIN HopDong hd ON B.hopdongFK=hd.HopDongID
  WHERE 1=1
   AND A.NgayThucHien =@NgayThucHien
   AND B.DmSanPhamREF =585
   AND (A.[money] <>0 OR A.pro <>0)
   AND B.TK_AdMarket <> '' AND convert(date,B.CreatedAt) >= '2013-01-01' AND convert(date,B.CreatedAt) <= @NgayThucHien
   AND B.DeletedStatus <> 1 AND hd.TrangThaiHopDong <> 3
 )T
 GROUP BY T.DmSanPhamREF, T.TenSanPham , T.username, T.ttv, T.ttc
)T1 LEFT JOIN 
(
 SELECT T.username, T.DmSanPhamREF, 
  SUM(ISNULL(T.TongClickThucChay,0)) TongClickThucChay,
  SUM(ISNULL(T.TongViewThucChay,0)) TongViewThucChay,
  SUM(ISNULL(T.SoLuongThucChay,0)) SoLuongThucChay,
  SUM(ISNULL(T.SoLuongThucChayKM,0)) SoLuongThucChayKM,
  SUM(T.ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
  SUM(T.ThanhTienKM) AS ThanhTienKM, 
  SUM(ISNULL(T.SoLuongThucChayOnline,0)) SoLuongThucChayOnline, 
  SUM(T.TienThucChayOnline) AS TienThucChayOnline,
  SUM(T.TienKhuyenMaiOnline) AS TienKhuyenMaiOnline,
  SUM(T.ThanhTienSauTrietKhauThucChay + T.ThanhTienKM + T.TienThucChayOnline + T.TienKhuyenMaiOnline) TongTien
 FROM
 (

  SELECT 
   A.DmSanPhamREF, A.TenSanPham,
   A.username,
   ISNULL(SUM(A.TongClickThucChay),0) TongClickThucChay, 
   ISNULL(SUM(A.TongViewThucChay),0) TongViewThucChay, 
   ISNULL(SUM(A.SoLuongThucChay),0) SoLuongThucChay, 
   ISNULL(SUM(A.SoLuongThucChayKM),0) SoLuongThucChayKM, 
   ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay),0) ThanhTienSauTrietKhauThucChay,
   ISNULL(SUM(A.ThanhTienKM),0) AS ThanhTienKM,
   ISNULL(SUM(A.SoLuongThucChayOnline),0) AS SoLuongThucChayOnline,
   ISNULL(SUM(A.TienThucChayOnline),0) AS TienThucChayOnline,
   ISNULL(SUM(A.TienKhuyenMaiOnline),0) AS TienKhuyenMaiOnline
  FROM 
  (
  SELECT 
   tcdta.DmSanPhamREF, tcdta.TenSanPham, 
   (SELECT hdct.TK_AdMarket
      FROM HopDongChiTiet AS hdct WHERE hdct.HopDongChiTietID = tcdta.HopDongChiTietREF) username,
   tcdta.TongClickThucChay, 
   tcdta.TongViewThucChay, 
   tcdta.SoLuongThucChay, 
   tcdta.SoLuongThucChayKM, 
   tcdta.ThanhTienSauTrietKhauThucChay,
   tcdta.ThanhTienKM,
   0 SoLuongThucChayOnline,
   0 TienThucChayOnline,
   0 TienKhuyenMaiOnline
  FROM ThucChayDaTinhAdmarket tcdta
  WHERE tcdta.NgayThucHien = @NgayThucHien
   AND tcdta.DmSanPhamREF = 585
   AND tcdta.DotChayHopDong <> 'Adx_Chay_Lai_Du_Lieu'
   AND tcdta.DotChayHopDong <> 'Admarket_Chay_Lai_Du_Lieu'
   AND tcdta.DotChayHopDong <> 'ThucChay_Admarket_Chay_Lai_Du_Lieu_Online'
   
  UNION ALL
  
  SELECT 
  tcao.DmSanPhamREF, 
  tcao.TenSanPham, 
  tcao.TaiKhoan,
  tcao.TotalClick, 
  tcao.TotalView, 
  0 SoLuongThucChay,
  0 SoLuongKM,
  0 SoLuongThucChay,
  0 TienKhuyenMai,
  tcao.SoLuong SoLuongThucChayOnline, 
  tcao.TienThucChay TienThucChayOnline, 
  tcao.TienKhuyenMai TienKhuyenMaiOnline
  FROM ThucChayAdmarketOnline tcao
  WHERE 1=1 --AND tcao.RecordStatus=0
  AND tcao.NgayThucHien= @NgayThucHien
  AND tcao.DmSanPhamREF=585
  AND tcao.GhiChu <> 'Tinh_Lai'
  ) A
  GROUP BY
   A.DmSanPhamREF, A.TenSanPham, A.username
 )T
 GROUP BY T.username, T.DmSanPhamREF
)T2 ON T1.username = T2.username AND T1.DmSanPhamREF = T2.DmSanPhamREF 
WHERE T1.ttc <> (T2.SoLuongThucChay + T2.SoLuongThucChayOnline)
OR T1.ThanhTienThucChay <> (T2.ThanhTienSauTrietKhauThucChay+T2.TienThucChayOnline)
OR T1.ThanhTienKM <> (T2.ThanhTienKM+T2.TienKhuyenMaiOnline)
OR T1.TongTien <> T2.TongTien
ORDER BY T1.TongTien DESC
END

```
