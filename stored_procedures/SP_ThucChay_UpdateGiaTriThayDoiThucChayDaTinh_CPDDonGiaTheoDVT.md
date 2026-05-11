# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDonGiaTheoDVT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:24.777000
- **Ngày sửa cuối**: 2024-08-21 16:02:44.867000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHIen` | `datetime(8)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDDonGiaTheoDVT] 
	@NgayThucHIen DATETIME
AS
BEGIN
	DECLARE	@HopDongREF INT, @HopDongChiTietID INT , @SoHopDong NVARCHAR(50), @NgayThucHienBF DATETIME
	DECLARE @SoLuongDotChayHD INT, @ThanhTienHDCT FLOAT
	, @NgayDanhSo_GioiHan DATETIME = '2018-01-01'

	SET @NgayThucHienBF = DATEADD(DAY,-1,@NgayThucHIen)
	
	--1. Xác định danh mục phân bổ thay đổi thông tin đơn giá
	DECLARE Record_Cursor CURSOR FOR 
		
		SELECT a.HopDongID,
			   a.SoHopDong,
			   a.HopDongChiTietREF,
			   b.SoLuongDotChayHD,
			   b.ThanhTien
		FROM   (
		--**TRANGTT COMMENT 2024-08-21 XEM LAI DIEU KIEN THEO @NgayThucHienBF, VA CACH THUC CHECK THAY DOI 
				   SELECT DISTINCT tcdt.HopDongChiTietREF,
						  tcdt.SoHopDong,
						  tcdt.HopDongID,
						  tcdt.DonGiaTheoDonVi,
						  tcdt.NgayThucHien
				   FROM   ThucChayDaTinh tcdt
				   WHERE  tcdt.DmSanPhamREF IN (140, 228, 564, 549,5082)
						  AND tcdt.NgayThucHien = @NgayThucHienBF
						  AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1 --Ðon v? c?a hình th?c CPD
						  AND tcdt.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan
						  AND tcdt.DotChayHopDong <> N'CPD_KhongDotChay'
			   )a
			   INNER JOIN (
						SELECT DISTINCT tcdt.HopDongChiTietREF,
							   tcdt.SoHopDong,
							   tcdt.HopDongID,
							   tcdt.DonGiaTheoDonVi,
							   tcdt.SoLuongDotChayHD,
							   tcdt.ThanhTien,
							   tcdt.NgayThucHien
						FROM   ThucChayDaTinh tcdt
						WHERE  tcdt.DmSanPhamREF IN (140, 228, 564, 549,5082)
							   AND tcdt.NgayThucHien = @NgayThucHIen
							   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1  --Ðon v? c?a hình th?c CPD
							   AND tcdt.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan
							   AND tcdt.DotChayHopDong <> N'CPD_KhongDotChay'
					)b
					ON  a.HopDongChiTietREF = b.HopDongChiTietREF
					AND a.HopDongID = b.HopDongID
		WHERE a.DonGiaTheoDonVi <> b.DonGiaTheoDonVi            
	
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
END

```
