# Stored Procedure: `KSTC_GoogleFacebook_chiphiquanly`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:24.250000
- **Ngày sửa cuối**: 2015-04-08 10:00:24.250000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@TaiKhoan` | `nvarchar(100)` | No |
| `@TienThucChay` | `int(4)` | No |
| `@Type` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KSTC_GoogleFacebook_chiphiquanly] 
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF INT, 
	@TenSanPham NVARCHAR(50), 
	@TaiKhoan NVARCHAR(50), 
	@TienThucChay INT, 
	@Type NVARCHAR(50), 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @TienOnline FLOAT, @TienThucChayDaTinh FLOAT, @GhiChu NVARCHAR(200)
	--Loai cam ket chi phi khong co truong hop khuyen mai	
	--kiem tra so tong (TCDT + vi online = TC)
	--1.Tien online
	set @TienOnline  = ISNULL((select SUM(ThanhTien) from ThucChayGoogleFacebookOnline 
						WHERE DmSanPhamREF = @DmSanPhamREF
						AND TaiKhoan = @TaiKhoan
						AND [Type] = @Type
						AND NgayThucHien = @NgayThucHien),0)
     --2.Tien thuc chay da tinh
     set @TienThucChayDaTinh = ISNULL((SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
            FROM ThucChayDaTinh tcdt 
     WHERE tcdt.NgayThucHien = @NgayThucHien
     AND tcdt.HopDongChiTietREF IN (					
				     SELECT HopDongChiTietID FROM HopDongChiTiet hdct 
					 WHERE hdct.DeletedStatus <> 1	
					 AND hdct.HopDongFK IN (SELECT HopDongID FROM HopDong WHERE TrangThaiHopDong <> 3)
					 AND hdct.DmSanPhamREF = @DmSanPhamREF
					 AND hdct.DonViTinh IN (N'Gói',N'đ/v')							
							 
					 UNION ALL
					 
					 SELECT HopDongChiTietID FROM HopDongChiTiet hdct 
					 WHERE hdct.DeletedStatus <> 1	
					 AND hdct.DmWebsiteREF IN (285,307)					 
					 AND hdct.HopDongFK IN (SELECT HopDongID FROM HopDong WHERE TrangThaiHopDong <> 3)
					 AND @TaiKhoan IN (SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(hdct.TK_Admarket,',')))
					 AND hdct.HopDongFK IN (SELECT HopDongFK FROM HopDongChiTiet hdct 
							 WHERE hdct.DmSanPhamREF = @DmSanPhamREF
							 AND hdct.DonViTinh IN (N'Gói',N'đ/v')
							 AND hdct.DeletedStatus <> 1)
					 )				
	),0)
	IF @TienThucChay <> (@TienOnline + @TienThucChayDaTinh)
		set @GhiChu = 'So tien tong sai'
	ELSE
		set @GhiChu = 'So tien tong dung:' 
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
