# Stored Procedure: `ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-04-27 16:24:10.370000
- **Ngày sửa cuối**: 2024-09-25 15:21:32.737000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham]  '2017-08-04'
CREATE  PROCEDURE [dbo].[ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongChiTietID INT, @DmNhanHangREF NVARCHAR(100), @DmNhanHangREF_Odl NVARCHAR(200), @DmSanPhamREF INT, @HopDongID INT
	, @NgayDanhSoGioiHan DATETIME = DATEADD(Y,-3,GETDATE())
	DECLARE Cursor_NhanHangHDCT CURSOR FOR

		SELECT hdct.HopDongChiTietID, hdct.DanhSachNhanHangREF, hdct.DmSanPhamREF, hdct.HopDongFK
		FROM dbo.HopDongChiTiet hdct
		INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan AND hd.DeletedStatus = 0) hd
		ON HD.HopDongID = hdct.HopDongFK
		WHERE hdct.DmLoaiREF = 42
		AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821,342,585,5056)
		AND NOT(hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
		AND CONVERT(DATE,hdct.LastModifiedAt) = @NgayThucHien
		AND hdct.DeletedStatus = 0

	OPEN Cursor_NhanHangHDCT
	FETCH NEXT FROM Cursor_NhanHangHDCT INTO @HopDongChiTietID , @DmNhanHangREF , @DmSanPhamREF , @HopDongID
	WHILE @@FETCH_STATUS =0
	BEGIN
		--CHECK THAY DOI NHAN HANG THAY DOI
		PRINT 'Thong tin treo thay doi'
		IF(EXISTS(SELECT TOP (1) HopDongChiTietREF FROM dbo.ThucChayDaTinh
			WHERE DmSanPhamREF = @DmSanPhamREF
			AND HopDongID = @HopDongID
			AND DmHinhThucQuangCao = 42
			AND HopDongChiTietREF = @HopDongChiTietID
			AND NhanHang <> @DmNhanHangREF
			AND NgayThucHien < @NgayThucHien
			ORDER BY NgayThucHien DESC
		))
		BEGIN
		    SET @DmNhanHangREF_Odl = (SELECT TOP (1) NhanHang 
				FROM dbo.ThucChayDaTinh
				WHERE DmSanPhamREF = @DmSanPhamREF
				AND DmHinhThucQuangCao = 42
				AND HopDongChiTietREF = @HopDongChiTietID
				AND NhanHang <> @DmNhanHangREF
				AND NgayThucHien < @NgayThucHien
				ORDER BY NgayThucHien DESC
			)
			IF(@DmNhanHangREF <> @DmNhanHangREF_Odl)
			BEGIN
			    --THUC HIEN DOI TRU VOI THONG TIN NHAN HANG MOI
				EXEC [dbo].[ThucChay_Insert_GTTD_GiamTang_NhanHang_ThucChayDaTinh_Admatic] 
							@HopDongID = @HopDongID, 
							@DmSanPhamREF = @DmSanPhamREF,
							@HopDongChiTietID = @HopDongChiTietID,
							@NhanHangNew = @DmNhanHangREF,
							@NhanHangOld = @DmNhanHangREF_Odl,
							@NgayThucHien = @NgayThucHien
			END
		END
		

	FETCH NEXT FROM Cursor_NhanHangHDCT INTO @HopDongChiTietID , @DmNhanHangREF , @DmSanPhamREF , @HopDongID
	END
	CLOSE Cursor_NhanHangHDCT;
	DEALLOCATE Cursor_NhanHangHDCT;

END


```
