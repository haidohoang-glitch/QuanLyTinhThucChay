# Stored Procedure: `KSTC_CheckHopDongIDAndHopDongChiTietIDCPK`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-09 17:04:02.517000
- **Ngày sửa cuối**: 2014-12-09 17:04:02.517000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckHopDongIDAndHopDongChiTietIDCPK 
	-- Add the parameters for the stored procedure here
	@HopDongID INT, 
	@HopDongChiTietID INT, 
	@DmSanPhamREF INT
AS
BEGIN
	SELECT tchdctp.ThucChayHopDongChiTietID
	,tchdctp.DeletedStatus
	,tchdctp.HopDongREF
	,tchdctp.HopDongChiTietREF
	,tchdctp.ThoiGianBatDau
	,tchdctp.CreatedAt
	,tchdctp.LastModifiedAt
	,tchdctp.RecordStatus
	 FROM ThucChayHopDongChiTiet tchdctp
	LEFT JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctp.HopDongChiTietREF     
	WHERE tchdctp.HopDongREF = @HopDongID AND
	 tchdctp.HopDongChiTietREF = @HopDongChiTietID
	AND hdct.DmSanPhamREF = @DmSanPhamREF
	--AND tchdctp.DeletedStatus <> 1
	--AND tchdctp.RecordStatus =1
	--AND tchdctp.ThoiGianBatDau >= '2013-01-01'

	SELECT tcdt.NgayThucHien, tcdt.GiaTriThayDoi, GhiChu, tcdt.HopDongChiTietREF
	  FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongChiTietREF = 0 AND tcdt.HopDongID = @HopDongID
	AND tcdt.DmSanPhamREF = @DmSanPhamREF
	------------List Data ThucChayDaTinh-------------------
	SELECT 
	tcdt.ThucChayDaTinhID,
	tcdt.SoHopDong
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
	,tcdt.CreatedAt, tcdt.LastModifiedAt, tcdt.SoLuongThucChayLechTreoHa, tcdt.ThanhTienLechTreoHa
	FROM ThucChayDaTinh tcdt
	WHERE tcdt.DmSanPhamREF = @DmSanPhamREF
	AND tcdt.HopDongID = @HopDongID
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	--AND '20408' IN (tcdt.DotChayBooking) 
	ORDER BY tcdt.NgayThucHien

	----------------Get Thong Tin HopDong, HopDongChiTiet ----------------------
	SELECT hd.SoHopDong , hd.HopDongID, hdct.HopDongChiTietID,hdct.donvitinh,hdct.Ghichu
	,hdct.DmSanPhamREF
	,hdct.TenSanPham
	, hdct.TenWebsite +','+ hdct.TenChuyenMuc+','+ hdct.TenViTri  AS Vitri
	, hdct.SoLuong
	, hdct.DonGia, hdct.ChietKhau, hdct.ThanhTien 
	, hd.LastModifiedAt, hdct.DmWebsiteREF

	FROM HopDong hd INNER JOIN  HopDongChiTiet hdct
	ON hd.HopDongID = hdct.HopDongFK
	WHERE hd.HopDongID = @HopDongID
	AND hdct.HopDongChiTietID = @HopDongChiTietID
	AND hdct.DmSanPhamREF IN (@DmSanPhamREF,306,423)
	AND hd.TrangThaiHopDong <> 3
	AND hd.DeletedStatus <> 1
	AND hdct.DeletedStatus <> 1

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
	AND hdcttd.DmSanPhamREF = @DmSanPhamREF
	ORDER BY hdtd.NgayThayDoi desc
	----Check Toan bo hop dong --------------------------
	 ----Check Toan bo hop dong --------------------------
	DECLARE @ThanhTienHD FLOAT, @SoLuongTT INT, @ThanhTienTC FLOAT, 
	@ChietKhau INT, @ThanhTienTT FLOAT, @DonGia FLOAT, @IsKhuyenMai INT, 
	@ThanhTienTTKM FLOAT, @ThanhTienTCKM FLOAT

	SET @ChietKhau = (SELECT hdct.ChietKhau
						 FROM HopDongChiTiet hdct 
						 WHERE hdct.DeletedStatus <> 1 AND hdct.DmSanPhamREF = @DmSanPhamREF
						 AND hdct.HopDongFK = @HopDongID
						 AND hdct.HopDongChiTietID = @HopDongChiTietID
	)
	SET @IsKhuyenMai = (SELECT hdct.IsKhuyenMai
						 FROM HopDongChiTiet hdct 
						 WHERE hdct.DeletedStatus <> 1 AND hdct.DmSanPhamREF = @DmSanPhamREF
						 AND hdct.HopDongFK = @HopDongID
						 AND hdct.HopDongChiTietID = @HopDongChiTietID
	)

	SET @DonGia = (SELECT DonGia FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	AND hdct.DeletedStatus <> 1)
	SET @ThanhTienHD = (SELECT 
						SUM(hdct.ThanhTien)
						 FROM HopDongChiTiet hdct 
						 WHERE hdct.DeletedStatus <> 1 AND hdct.DmSanPhamREF = @DmSanPhamREF
						 AND hdct.HopDongFK = @HopDongID
						 AND hdct.HopDongChiTietID = @HopDongChiTietID
						 )
	SET @SoLuongTT =  ISNULL((SELECT 
						 count(tt.ThucChayHopDongChiTietID) AS tt
						 FROM ThucChayHopDongChiTiet tt
						 INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tt.HopDongChiTietREF
						 WHERE  tt.deletedstatus = 0	
						 AND hdct.DeletedStatus <> 1					
						 AND tt.HopDongREF = @HopDongID
						 AND tt.HopDongChiTietREF = @HopDongChiTietID
						 AND hdct.DmSanPhamREF = @DmSanPhamREF
						 AND tt.RecordStatus = 1
						 
	),0)



	IF (@ChietKhau = 100 OR @IsKhuyenMai = 1)
		SET @ThanhTienTTKM = @SoLuongTT * @DonGia
	ELSE SET @ThanhTienTTKM = 0

	SET @ThanhTienTT = @SoLuongTT * @DonGia* (100-@ChietKhau)/100

	SET @ThanhTienTC = ISNULL((SELECT
						 SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS tttc
						 FROM ThucChayDaTinh tcdt
						 WHERE tcdt.DmSanPhamREF = @DmSanPhamREF  	
						  AND tcdt.HopDongID = @HopDongID
						 AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	),0)
	SET @ThanhTienTCKM = ISNULL((SELECT
						 SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS tttc
						 FROM ThucChayDaTinh tcdt
						 WHERE tcdt.DmSanPhamREF = @DmSanPhamREF  	
						  AND tcdt.HopDongID = @HopDongID
						 AND tcdt.HopDongChiTietREF = @HopDongChiTietID),0)

	SELECT @ThanhTienHD [HD], @ThanhTienTT  TT, @ThanhTienTC TC, 
	(@ThanhTienTT  - @ThanhTienTC) lechTTTC,
	(@ThanhTienHD  - @ThanhTienTC) lechHDTC,
	@ThanhTienTTKM TTKM, @ThanhTienTCKM TCKM,
	(@ThanhTienTTKM - @ThanhTienTCKM) lechKM
END

```
