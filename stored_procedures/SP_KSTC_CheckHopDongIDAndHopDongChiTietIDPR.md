# Stored Procedure: `KSTC_CheckHopDongIDAndHopDongChiTietIDPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-09 16:50:31.907000
- **Ngày sửa cuối**: 2014-12-09 16:50:31.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckHopDongIDAndHopDongChiTietIDPR 
	-- Add the parameters for the stored procedure here
	@HopDongID INT,
	@HopDongChiTietID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SELECT tchdctp.ThucChayHopDongChiTietPRID ID
 ,tchdctp.HopDongREF
 ,tchdctp.HopDongChiTietREF
 ,tchdctp.ThoiGianBatDau
 ,tchdctp.KhuyenMai
 ,tchdctp.GiaTien
 ,tchdctp.CreatedAt
 ,tchdctp.LastModifiedAt
 ,tchdctp.RecordStatus
 ,tchdctp.DeletedStatus
  FROM ThucChayHopDongChiTietPR tchdctp
 WHERE tchdctp.HopDongREF = @HopDongID
 AND tchdctp.HopDongChiTietREF = @HopDongChiTietID
 --AND tchdctp.DeletedStatus <> 1
 --AND tchdctp.RecordStatus = 0
 AND ThoiGianBatDau >= '2013-01-01'

 ------------List Data ThucChayDaTinh-------------------
 SELECT 
 tcdt.ThucChayDaTinhID,
 tcdt.SoHopDong, tcdt.HopDongChiTietREF
 , tcdt.TenHinhThucQuangCao
 , tcdt.DotChayBooking
 , tcdt.SoLuong
 , tcdt.DonGia
 , tcdt.SoLuongThucChay
 , tcdt.SoLuongThucChayKM
 , tcdt.ChietKhau
 , tcdt.ThanhTienSauTrietKhauThucChay
 , tcdt.ThanhTienKM
 , tcdt.GiaTriThayDoi
 , tcdt.NgayThucHien 
 ,tcdt.CreatedAt, tcdt.LastModifiedAt,tcdt.GhiChu
 FROM ThucChayDaTinh tcdt
 WHERE tcdt.DmSanPhamREF = 141
 AND tcdt.HopDongID = @HopDongID
 AND tcdt.HopDongChiTietREF = @HopDongChiTietID
 --AND '20408' IN (tcdt.DotChayBooking) 

 ORDER BY tcdt.NgayThucHien
 
 ----------------Get Thong Tin HopDong, HopDongChiTiet ----------------------
 SELECT hd.SoHopDong , hd.HopDongID, hdct.HopDongChiTietID, hdct.TenLoai
 ,hdct.TenSanPham
 , hdct.TenWebsite +','+ hdct.TenChuyenMuc+','+ hdct.TenViTri  AS Vitri
 , hdct.SoLuong
 , hdct.DonGia, hdct.ChietKhau, hdct.ThanhTien 
 , hd.LastModifiedAt, hd.TrangThaiHopDong
 FROM HopDong hd INNER JOIN  HopDongChiTiet hdct
 ON hd.HopDongID = hdct.HopDongFK
 WHERE hd.HopDongID = @HopDongID
 AND hdct.HopDongChiTietID = @HopDongChiTietID
 AND hd.TrangThaiHopDong <> 3
 AND hd.DeletedStatus <> 1
 AND hdct.DeletedStatus <> 1
 --AND hdct.DmSanPhamREF = 141
 
 ----------------Get Thong Tin HopDongThayDoi ----------------------------
 SELECT
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
 FROM HopDongThayDoi hdtd INNER JOIN HopDongChiTietThayDoi hdcttd
 ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
 WHERE
 hdcttd.HopDongFK = @HopDongID
 AND hdcttd.HopDongChiTietREF = @HopDongChiTietID
 ORDER BY hdtd.NgayThayDoi desc
 --Get Thong tin hopdong sua
 SELECT * FROM HopDongChiTietLog hdctl WHERE hdctl.HopDongChiTietREF = @HopDongChiTietID
 ----Check Toan bo hop dong --------------------------
DECLARE @ThanhTienHD FLOAT, @ThanhTienTT FLOAT, @ThanhTienTC FLOAT, @ChietKhau INT, @ThanhTienKMTC FLOAT, @ThanhTienTTKM FLOAT, @IsKhuyenMai INT
SET @ChietKhau = (SELECT hdct.ChietKhau
					 FROM HopDongChiTiet hdct 
					 WHERE hdct.DeletedStatus <> 1 AND hdct.DmSanPhamREF = 141
					 AND hdct.HopDongFK = @HopDongID
					 AND hdct.HopDongChiTietID = @HopDongChiTietID
)
SET @IsKhuyenMai = (SELECT hdct.IsKhuyenMai
					 FROM HopDongChiTiet hdct 
					 WHERE hdct.DeletedStatus <> 1 AND hdct.DmSanPhamREF = 141
					 AND hdct.HopDongFK = @HopDongID
					 AND hdct.HopDongChiTietID = @HopDongChiTietID
					 )
SET @ThanhTienHD = (SELECT 
                    SUM(hdct.ThanhTien)
					 FROM HopDongChiTiet hdct 
					 WHERE hdct.DeletedStatus <> 1 AND hdct.DmSanPhamREF = 141
					 AND hdct.HopDongFK = @HopDongID
					 AND hdct.HopDongChiTietID = @HopDongChiTietID
					 )
SET @ThanhTienTT =  (SELECT 
					 SUM(ttpr.GiaTien) AS tttt
					 FROM ThucChayHopDongChiTietPR ttpr
					 WHERE ttpr.RecordStatus = 1 AND 
					 ttpr.deletedstatus <> 1	
					 --AND ttpr.KhuyenMai = 0
					 AND ttpr.HopDongREF = @HopDongID
					 AND ttpr.HopDongChiTietREF = @HopDongChiTietID
					 AND ttpr.ThoiGianBatDau >='2013-01-01'
)

SET @ThanhTienTT = @ThanhTienTT * (100-@ChietKhau)/100

SET @ThanhTienTTKM = (SELECT 
					 SUM(ttpr.GiaTien) AS tttt
					 FROM ThucChayHopDongChiTietPR ttpr
					 WHERE ttpr.RecordStatus = 1 AND ttpr.deletedstatus <> 1						 
					 AND ttpr.HopDongREF = @HopDongID
					 AND ttpr.HopDongChiTietREF = @HopDongChiTietID
					 AND ttpr.ThoiGianBatDau >='2013-01-01'
)
IF (@ChietKhau = 100 OR @isKhuyenMai = 1) 
	SET @ThanhTienTTKM = @ThanhTienTTKM
ELSE SET @ThanhTienTTKM = 0

SET @ThanhTienTC = (SELECT
					 SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS tttc
					 FROM ThucChayDaTinh tcdt
					 WHERE tcdt.DmSanPhamREF in (141 ,245,250) 	
					  AND tcdt.HopDongID = @HopDongID
					 AND tcdt.HopDongChiTietREF = @HopDongChiTietID
)

SET @ThanhTienKMTC = (SELECT
					 SUM(tcdt.ThanhTienKM) TTKM
					 FROM ThucChayDaTinh tcdt
					 WHERE tcdt.DmSanPhamREF = 141  	
					  AND tcdt.HopDongID = @HopDongID
					 AND tcdt.HopDongChiTietREF = @HopDongChiTietID
)

SELECT @ThanhTienHD [HD], @ThanhTienTT  TT, @ThanhTienTC TC,  @ThanhTienKMTC KMTC, @ThanhTienTTKM TTKM,
(@ThanhTienTT  - @ThanhTienTC) lechTTTC,
(@ThanhTienHD  - @ThanhTienTC) lechHDTC,
(@ThanhTienTTKM - @ThanhTienKMTC) lechTTKM
END

```
