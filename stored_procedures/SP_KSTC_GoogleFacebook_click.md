# Stored Procedure: `KSTC_GoogleFacebook_click`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:24.040000
- **Ngày sửa cuối**: 2015-04-08 10:00:24.040000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@TaiKhoan` | `nvarchar(100)` | No |
| `@SoClick` | `int(4)` | No |
| `@Type` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [KSTC_GoogleFacebook_click] 423,'Google Ads','Nha Hang Cong Vien Nho',879,'click','2014-12-20'
CREATE PROCEDURE [dbo].[KSTC_GoogleFacebook_click]  
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF INT, 
	@TenSanPham NVARCHAR(50), 
	@TaiKhoan NVARCHAR(50), 
	@SoClick INT, 
	@Type NVARCHAR(50), 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @SoClickOnline FLOAT, @SoClickThucChayDaTinh FLOAT, @GhiChu NVARCHAR(200)
	--Loai cam ket click co truong hop khuyen mai	
	--Hop dong co dvt CPV duoc nhom theo loai click, du lieu thuc chay duoc dua vao cot click
	--kiem tra so tong (TCDT + vi online = TC)
	--1.So click chay online
	SET @SoClickOnline =0 
	SET @SoClickThucChayDaTinh = 0
	set @SoClickOnline  = ISNULL((select SUM(Click) from ThucChayGoogleFacebookOnline 
						WHERE DmSanPhamREF = @DmSanPhamREF
						AND TaiKhoan = @TaiKhoan
						AND [Type] = @Type
						AND NgayThucHien = @NgayThucHien),0)
	
     --2.So click chay da tinh
     set @SoClickThucChayDaTinh = ISNULL((SELECT SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi + tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi)
            FROM ThucChayDaTinh tcdt 
     WHERE tcdt.NgayThucHien = @NgayThucHien
     AND tcdt.HopDongChiTietREF IN (					
				     SELECT HopDongChiTietID FROM HopDongChiTiet hdct 
					 WHERE hdct.DeletedStatus <> 1	
					 AND hdct.HopDongFK IN (SELECT HopDongID FROM HopDong WHERE TrangThaiHopDong <> 3)
					 AND hdct.HopDongFK IN (SELECT HopDongFK FROM HopDongChiTiet hdct 
							 WHERE hdct.DmSanPhamREF = @DmSanPhamREF
							 AND @TaiKhoan IN (SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(hdct.TK_Admarket,','))) 
							 AND hdct.DonViTinh IN ('CPC','CPV')
							 AND hdct.DeletedStatus <> 1)	
					 )	
	AND tcdt.DonViTinh IN ('CPC','CPV')			
	),0)
	
	IF @SoClick <> (@SoClickOnline + @SoClickThucChayDaTinh)
		SET @GhiChu = 'So click tong sai'
	ELSE
		SET @GhiChu = 'So click tong dung'
		Insert into #temp 
		SELECT 
		@DmSanPhamREF, 
		@TenSanPham , 
		@TaiKhoan, 
		@Type, 
		@NgayThucHien,
		@GhiChu 
	
END

```
