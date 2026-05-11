# Stored Procedure: `ThucChay_EXEC_ThucChay_ThanhTien_Admatic_ByBanner_SoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-07-01 16:37:31.687000
- **Ngày sửa cuối**: 2022-07-01 16:38:29.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_EXEC_ThucChay_ThanhTien_Admatic_ByBanner_SoHopDong] 'QC2600622'
SELECT CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
*/

CREATE PROCEDURE [dbo].[ThucChay_EXEC_ThucChay_ThanhTien_Admatic_ByBanner_SoHopDong]
	@pSoHopDong NVARCHAR(100)
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
		  AND SOHOPDONG = @pSoHopDong
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
