# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDotChayTD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:24.690000
- **Ngày sửa cuối**: 2024-08-21 16:04:00.657000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHIen` | `datetime(8)` | No |

## Definition (Source Code)

```sql


CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDotChayTD] 
	@NgayThucHIen DATETIME
AS
BEGIN
	DECLARE	@HopDongREF INT, @HopDongChiTietID INT , @SoHopDong NVARCHAR(50), @NgayThucHienBF DATETIME
	DECLARE @SoLuongDotChayHD INT, @ThanhTienHDCT FLOAT
	, @NgayDanhSo_GioiHan DATETIME = '2018-01-01'

	SET @NgayThucHienBF = DATEADD(DAY,-1,@NgayThucHIen)

	--1. Xác định danh mục phân bổ thay đổi thông tin thực treo
	DECLARE Record_Cursor CURSOR FOR 
		
		SELECT DISTINCT A.* FROM 
		(
			SELECT DISTINCT hdct.HopDongFK , hd.SoHopDong, tchdct.HopDongChiTietREF, hdct.SoLuong, hdct.ThanhTien 
			FROM ThucChayHopDongChiTiet tchdct
			INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
			INNER JOIN hopdong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE 1 = 1
			AND hdct.DeletedStatus = 0
			AND hd.TrangThaiHopDong <> 3
			AND hdct.DmLoaiREF <> 13 
			AND hdct.DmSanPhamREF IN (140,228,564,549,5082) 
			AND convert(date,tchdct.LastModifiedAt) = @NgayThucHIen
			AND hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1 
			AND EXISTS (SELECT TOP (1) dc.HopDongChiTietREF from dbo.DotChayHopDongchitiet dc WHERE dc.HopDongChiTietREF = hdct.HopDongChiTietID)--Check CPD dotchay 02/12/2022

			UNION

			SELECT distinct hdtd.HopDongFK, hdtd.SoHopDong, dchdcttd.HopDongChiTietREF,hdct.SoLuong, hdct.ThanhTien
			FROM
			  (	SELECT distinct hdtd.*, hd.SoHopDong from (SELECT * FROM HopDongThayDoi hdtd WHERE 1=1 AND convert(date,hdtd.NgayThayDoi) = @NgayThucHIen)hdtd
				INNER JOIN (SELECT hd.SoHopDong, hd.HopDongID, hd.NgayDanhSoHopDong FROM HopDong hd WHERE hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan)hd 
				ON hd.HopDongID = hdtd.HopDongFK
			  ) hdtd
			INNER JOIN (SELECT * FROM HopDongChiTiet hdct 
				WHERE 1=1 AND hdct.DmSanPhamREF IN (140,228,564,549,5082)
				AND hdct.DeletedStatus = 0
				AND EXISTS (SELECT TOP (1) dc.HopDongChiTietREF from dbo.DotChayHopDongchitiet dc WHERE dc.HopDongChiTietREF = hdct.HopDongChiTietID)--Check CPD dotchay 02/12/2022
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 1
			)hdct ON hdct.HopDongFK = hdtd.HopDongFK
			INNER JOIN DotChayHopDongChiTietThayDoi dchdcttd ON hdct.HopDongChiTietID = dchdcttd.HopDongChiTietREF
			WHERE 1=1
		)A 

	OPEN Record_Cursor

	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
	
	--2. Đối trừ
	WHILE @@FETCH_STATUS = 0
		BEGIN
			EXEC ThucChay_CheckHopDongCoThayDoi_CPDDotChay @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien ,@SoLuongDotChayHD ,@ThanhTienHDCT
		FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
		END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	SELECT 2
END



```
