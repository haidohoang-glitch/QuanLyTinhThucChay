# Stored Procedure: `KiemTra_DauVao_DangTin_ChietKhauThucTreoKhacHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-18 10:20:10.627000
- **Ngày sửa cuối**: 2016-11-24 17:57:50.973000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KiemTra_DauVao_DangTin_ChietKhauThucTreoKhacHD]
	-- Add the parameters for the stored procedure here
	--Check chiết khấu thực treo có khác với hd không


AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT A.*, B.* FROM 
(
SELECT hd.SoHopDong, hd.HopDongID, hdct.DmSanPhamREF,  hdct.ChietKhau ChietKhauHD,
 SUM(hdct.ThanhTien)ThanhTien, SUM(hdct.ThanhtienThucChay)ThanhtienThucChay,(SUM(hdct.ThanhTien)- SUM(hdct.ThanhtienThucChay))lech
FROM dbo.HopDong hd INNER JOIN hopdongchitiet hdct
ON hd.HopDongID = hdct.HopDongFK
WHERE hdct.DmSanPhamREF IN (141,305,637)
AND hdct.DeletedStatus = 0
AND hd.Nam>=2014 AND hdct.ChietKhau <> 100
AND HopDongID IN (SELECT HopDongREF FROM dbo.ThucChayHopDongChiTietPR WHERE LastModifiedAt >='2016-01-01' AND ThoiGianBatDau>='2013-01-01'
AND DeletedStatus = 0 )
AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
--AND hd.HopDongID = 46926


AND hd.TrangThaiHopDong <> 3
GROUP BY hd.SoHopDong, hd.HopDongID, hdct.DmSanPhamREF,  hdct.ChietKhau

)A
FULL OUTER JOIN 
(
SELECT DISTINCT dbo.GetSoHopDongByID(HopDongREF) SoHopDongTT, HopDongREF, DmSanPhamREF, ChietKhau ChietKhauTT 
FROM dbo.ThucChayHopDongChiTietPR WHERE LastModifiedAt >='2016-01-01'AND ThoiGianBatDau>='2013-01-01'
AND DeletedStatus = 0 AND ChietKhau<> 100
AND RIGHT(dbo.GetSoHopDongByID(HopDongREF),2)>='14'
AND HopDongREF NOT IN (SELECT HopDongID FROM hopdong WHERE TrangThaiHopDong = 3)
--AND HopDongREF = 46926


AND DmHinhThucQuangCaoREF <> 13
)B
ON A.HopDongID =B.HopDongREF
AND B.DmSanPhamREF =B.DmSanPhamREF
and  A.ChietKhauHD= B.ChietKhauTT
and  ISNULL(A.ChietKhauHD,0)= ISNULL(B.ChietKhauTT,0)
WHERE ISNULL(A.ChietKhauHD,0)<> ISNULL(B.ChietKhauTT,0)
-- or A.ChietKhauHD IS NULL or B.ChietKhauTT IS null



END




```
