# Stored Procedure: `ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-02 10:48:02.577000
- **Ngày sửa cuối**: 2018-05-07 09:47:45.667000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham_ByHopDong]  '2018-04-30', 501853
CREATE  PROCEDURE [dbo].[ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham_ByHopDong] 
	@NgayThucHien DATETIME,
	@HopDongREF INT
AS
BEGIN
	DECLARE @HopDongChiTietID INT, @DmNhanHangREF NVARCHAR(100), @DmNhanHangREF_Odl NVARCHAR(200), @DmSanPhamREF INT, @HopDongID INT
	DECLARE Cursor_NhanHangHDCT CURSOR FOR

		SELECT HopDongChiTietID, DanhSachNhanHangREF, DmSanPhamREF, HopDongFK
		FROM dbo.HopDongChiTiet
		WHERE DmLoaiREF = 42
		AND NOT (DmLoaiREF = 13 OR DmLoaiBannerREF = 18)
		AND HopDongFK = @HopDongREF
		AND DeletedStatus = 0

	OPEN Cursor_NhanHangHDCT
	FETCH NEXT FROM Cursor_NhanHangHDCT INTO @HopDongChiTietID , @DmNhanHangREF , @DmSanPhamREF , @HopDongID
	WHILE @@FETCH_STATUS =0
	BEGIN
		--CHECK THAY DOI NHAN HANG HOPDONGCHITIET
		PRINT 'Thong tin hopdongchitiet thay doi'
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
				--PRINT 'HopDong thay doi' + @DmNhanHangREF + ': nhan cu' + @DmNhanHangREF_Odl
				--SELECT  @HopDongID
				--SELECT  @DmSanPhamREF
				--SELECT  @DmBannerREF
				--SELECT  @DmNhanHangREF
				--SELECT  @DmNhanHangREF_Odl
				--SELECT @NgayThucHien
						
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
