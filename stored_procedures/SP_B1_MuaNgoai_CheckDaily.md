# Stored Procedure: `B1_MuaNgoai_CheckDaily`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-15 17:06:54.890000
- **Ngày sửa cuối**: 2017-02-15 17:06:54.890000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE B1_MuaNgoai_CheckDaily
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

   SELECT hd.SoHopDong,  hdct.HopDongChiTietID
  --, hdct.DmSanPhamREF
  --, hdct.ThanhTien, hdct.ChietKhau
  , hdct.ThanhTienThucChayMuaNgoaiTruocCK
  , (hdct.ThanhTienThucChayMuaNgoaiTruocCK * (100 - hdct.ChietKhau)/100) AS TienChay_HD 
 FROM HopDong hd FULL OUTER  JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK AND hd.TrangThaiHopDong <> 3 AND hdct.DeletedStatus= 0
  AND (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
  AND hdct.DeletedStatus = 0  
  
  WHERE hdct.DeletedStatus=0
  AND hdct.ThanhTienThucChayMuaNgoaiTruocCK <> 0 
   AND hd.NgayDanhSoHopDong >'2013-01-01'
ORDER BY hd.HopDongID, hdct.HopDongChiTietID
END

```
