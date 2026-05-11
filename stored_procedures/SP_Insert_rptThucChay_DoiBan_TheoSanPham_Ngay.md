# Stored Procedure: `Insert_rptThucChay_DoiBan_TheoSanPham_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-07 12:18:33.753000
- **Ngày sửa cuối**: 2015-03-07 12:18:33.753000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 03022014
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[Insert_rptThucChay_HopDong_Ngay]  '2013-01-01','2013-01-31'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_DoiBan_TheoSanPham_Ngay] 
	-- Add the parameters for the stored procedure here
    @FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE 
	FROM   rptThucChay_HopDong_Ngay
	WHERE  1 = 1
	       AND NgayThucHien BETWEEN @FromDate AND @ToDate
	
	WHILE @NgayThucHien <= @ToDate
		BEGIN
			 INSERT INTO rptThucChay_DoiBan_TheoSanPham_Ngay
			 SELECT 
				dstchdc.NgayThucHien,
				dstchdc.TenSanPham,
				dstchdc.DmSanPhamREF,
				dstchdc.TenPhongBan,
				dstchdc.PhongBanREF,
				dstchdc.TenBoPhan,
				dstchdc.BoPhanREF,
				dstchdc.TenNhom,
				dstchdc.NhomREF,
				'' DienGiai,
			    [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
                  dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	           SUM(dstchdc.ThucChayPhatSinhTrongKy)ThucChayPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
				  dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,	
			      @NgayThucHien,
			      1,0
				)+ SUM(dstchdc.ThucChayPhatSinhTrongKy)
				AS ThucChayPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
					dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,			
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)KhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
					dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,		
			      @NgayThucHien,
			      2,0
				) + SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)
	           AS KhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
				dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,		
			      @NgayThucHien,
			      3,0
				) AS NoiBoPhatSinhDauKy,
	           SUM(dstchdc.NoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
					dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,			
			      @NgayThucHien,
			      3,0
				) + SUM(dstchdc.NoiBoPhatSinhTrongKy)
				AS NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	          [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
					dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,			
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	           SUM(dstchdc.SoLuongPhatSinhTrongKy)SoLuongPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
					dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,	
			      @NgayThucHien,
			      1,1
				)+ SUM(dstchdc.SoLuongPhatSinhTrongKy)
				AS SoLuongPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
					dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,		
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)SoLuongKhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
					dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,			
			      @NgayThucHien,
			      2,1
				) + SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)
	           AS SoLuongKhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
					dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,		
			      @NgayThucHien,
			      3,1
				) AS SoLuongNoiBoPhatSinhDauKy,
	           SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBanTheoSanPham] 
				(
				  dstchdc.DmSanPhamREF,	
				  dstchdc.PhongBanREF,
	              dstchdc.BoPhanREF,
	              dstchdc.NhomREF,			
			      @NgayThucHien,
			      3,1
				) + SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)
				AS SoLuongNoiBoPhatSinhCuoiKy
			 FROM   DoanhSoThucChayHopDongTheoThoiGian dstchdc
			
			 WHERE dstchdc.NgayThucHien = @NgayThucHien
			 GROUP BY
			    dstchdc.NgayThucHien,
				dstchdc.TenSanPham,
				dstchdc.DmSanPhamREF,
				dstchdc.TenPhongBan,
				dstchdc.PhongBanREF,
				dstchdc.TenBoPhan,
				dstchdc.BoPhanREF,
				dstchdc.TenNhom,
				dstchdc.NhomREF
			SET @NgayThucHien = DATEADD(DAY, 1, @NgayThucHien)
		END
END

```
