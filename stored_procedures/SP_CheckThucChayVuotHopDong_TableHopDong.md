# Stored Procedure: `CheckThucChayVuotHopDong_TableHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-08 14:37:27.273000
- **Ngày sửa cuối**: 2021-11-03 15:19:28.960000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[CheckThucChayVuotHopDong_TableHopDong] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
Delete from KS_ThucChay_HopDong

/*CREATE TABLE KS_ThucChay_HopDong
(
SoHopDong NVARCHAR(50),
Nam INT,
TrangThaiHopDong INT,
HopDongID INT,
HopDongChiTietID INT,
DmLoaiREF INT,
DmLoaiBannerREF INT,
DmSanPhamREF INT,
SoLuong FLOAT,
DonViTinh NVARCHAR(10),
ChietKhau FLOAT,
ThanhTien FLOAT,
ThanhTienKhuyenMai FLOAT,
TK_AdMarket NVARCHAR(50),
LastModifiedAt Datetime)

*/
-------------------Insert dữ liệu--------------------
INSERT INTO KS_ThucChay_HopDong
SELECT SoHopDong,
Nam,
hd.TrangThaiHopDong,
HopDongID,
HopDongChiTietID,
hdct.DmLoaiREF,
DmLoaiBannerREF ,
DmSanPhamREF ,
SoLuong,
DonViTinh,
ChietKhau,
(CASE WHEN hd.TrangThaiHopDong = 3 THEN 0 
WHEN hdct.DeletedStatus = 1 THEN 0
ELSE ThanhTien END )ThanhTien,
(CASE WHEN hdct.ChietKhau =100 THEN hdct.SoLuong*hdct.DonGia
WHEN hdct.IsKhuyenMai = 1 THEN hdct.SoLuong*hdct.DonGia
ELSE 0 END ) ThanhTienKhuyenMai,
hdct.TK_AdMarket,
hdct.LastModifiedAt

 FROM HopDong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
 WHERE hd.Nam >=2015
END

```
