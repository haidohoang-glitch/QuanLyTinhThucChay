# Stored Procedure: `ThucChay_EXEC_ThucChay_ThanhTien_Admatic_ByBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-27 09:57:00.753000
- **Ngày sửa cuối**: 2024-12-16 16:04:05.307000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_EXEC_ThucChay_ThanhTien_Admatic_ByBanner]

SELECT CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
*/

CREATE PROCEDURE [dbo].[ThucChay_EXEC_ThucChay_ThanhTien_Admatic_ByBanner]
AS
BEGIN
	DECLARE @SoHopDong NVARCHAR(50), @DmSanPhamREF INT, @DmBannerREF INT,@NgayThucHien DATETIME
	SET @NgayThucHien = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))

	--CAP NHAP THONG TIN BANNER DEN NGAY
	EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_ThanhTien_Admatic] @NgayThucHien = @NgayThucHien

	DECLARE Record_Cursor_Banner CURSOR FOR 
		SELECT DISTINCT [SOHOPDONG]
			  ,[DMSANPHAMREF]
			  ,[DMBANNERREF]
		  FROM [dbo].[INFOBANNER_BRANDING_THANHTIEN_ADMATIC]
		  WHERE [DELETEDSTATUS] = 0
		  AND ISNULL([TrangThaiTinh],0) = 0 --TRANG THAI = 0 DANG CHAY , 1 DA DUNG CHAY
		  AND Createdat > DATEADD(yyyy,-1,GETDATE()) --Banner tao trong 1 nam so voi ngay hien tai
		  AND NOT ( Createdat <= DATEADD(d,-30,GETDATE()) 
		  AND NgayThucHienMax = '1900-01-01 00:00:00.000' ) --Banner tao ma sau 1 thang ko co thuc chay
		  AND (NgayThucHienMax = '1900-01-01 00:00:00.000' OR NgayThucHienMax >= DATEADD(mm,-2,GETDATE())) ---
		OPEN Record_Cursor_Banner

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor_Banner into @SoHopDong, @DmSanPhamREF, @DmBannerREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--print @DmBannerREF
				--print @SoHopDong
				--print @DmSanPhamREF
				EXEC [dbo].[ThucChay_TinhGiaTriThucChay_ThucChay_ThanhTien_Admatic_ByBanner]
				@SoHopDong = @SoHopDong,
				@DmSanPhamREF = @DmSanPhamREF,
				@DmBannerREF = @DmBannerREF
			FETCH NEXT FROM Record_Cursor_Banner into @SoHopDong, @DmSanPhamREF, @DmBannerREF
			END

		CLOSE Record_Cursor_Banner
		DEALLOCATE Record_Cursor_Banner
END

```
