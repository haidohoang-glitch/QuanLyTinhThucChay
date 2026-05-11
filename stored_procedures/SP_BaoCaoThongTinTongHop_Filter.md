# Stored Procedure: `BaoCaoThongTinTongHop_Filter`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-16 16:51:06.020000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.903000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FilterName` | `nvarchar(256)` | No |
| `@FilterValue` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SONVM>
-- Create date: <16/12/2013>
-- Description:	<Điều kiện tìm kiếm của Báo cáo Thông tin Tổng hơp>
-- =============================================
--[BaoCaoThongTinTongHop_Filter] 'ContractNo', 'BT'
--[BaoCaoThongTinTongHop_Filter] 'Customer', 'af'
--[BaoCaoThongTinTongHop_Filter] 'Staff', ''
--[BaoCaoThongTinTongHop_Filter] 'ProductType', ''
--[BaoCaoThongTinTongHop_Filter] 'Product', ''
--[BaoCaoThongTinTongHop_Filter] 'TagWebsite', '240, 339'
--[BaoCaoThongTinTongHop_Filter] 'HaveATagWebsite', ''
--[BaoCaoThongTinTongHop_Filter] 'WebsiteAll', ''
--[BaoCaoThongTinTongHop_Filter] 'WebsiteByTag', '475, 476, 477'
--[BaoCaoThongTinTongHop_Filter] 'Label', N'ô tô'
--[BaoCaoThongTinTongHop_Filter] 'Industry', ''

CREATE PROCEDURE [dbo].[BaoCaoThongTinTongHop_Filter] 
	@FilterName  NVARCHAR(128),
	@FilterValue NVARCHAR(4000)
AS
BEGIN	
	DECLARE @Sql NVARCHAR(MAX)		
	DECLARE @Count INT
	SET @Count = 10
	
	SET @Sql = 'DECLARE @TypeId INT '
	
	SET @Sql += (		
		SELECT CASE(@FilterName)			
			-- Số hợp đồng --
			WHEN 'ContractNo' THEN			
			'SELECT TOP ' + CONVERT(NVARCHAR(4), @Count) + ' * FROM (SELECT DISTINCT(HopDongID) Id, SoHopDong AS [Text], @TypeId AS TypeId FROM HopDong
			 WHERE DeletedStatus = 0 AND SoHopDong <> '''' AND SoHopDong LIKE N''%' + @FilterValue + '%'') AS T'     	

			-- Khách hàng --
			WHEN 'Customer' THEN
			'SELECT TOP ' + CONVERT(NVARCHAR(4), @Count) + ' * FROM (SELECT DISTINCT(DmKhachHangREF) AS Id, TenKhachHang AS [Text], @TypeId AS TypeId FROM HopDong
			 WHERE DeletedStatus = 0 AND TenKhachHang <> '''' AND TenKhachHang LIKE N''%' + @FilterValue + '%'') AS T'

			-- Nhân viên --
			WHEN 'Staff' THEN
			'SELECT DISTINCT(TenDangNhap) AS Id, TenNhanVien AS [Text], @TypeId AS TypeId FROM HopDong hd
			 WHERE DeletedStatus = 0 AND TenDangNhap <> '''' AND TenNhanVien LIKE N''%' + @FilterValue + '%'' ORDER BY hd.TenDangNhap'

			-- Hình thức quảng cáo --
			WHEN 'ProductType' THEN
			'SELECT DmLoaiSanPhamID AS Id, TenLoaiSanPham AS [Text], @TypeId AS TypeId FROM DmLoaiSanPham WHERE DeletedStatus = 0 ORDER BY TenLoaiSanPham'

			-- Sản phẩm --
			WHEN 'ProductAll' THEN
			'SELECT DmSanPhamID AS Id, TenSanPham AS [Text], @TypeId AS TypeId FROM DmSanPham WHERE DeletedStatus = 0 ORDER BY TenSanPham'
			
			WHEN 'ProductByType' THEN
			'SELECT dsp.DmSanPhamID AS Id, dsp.TenSanPham AS [Text], @TypeId AS TypeId FROM DmLoaiSanPhamDetail dmlspd
			INNER JOIN DmSanPham dsp ON dsp.DmSanPhamID = dmlspd.dmsanphamFK
			WHERE dmlspd.DmLoaiSanPhamFK IN ('+ @FilterValue +')'

			-- Nhóm Website -- 						
			WHEN 'TagWebsite' THEN
			'SELECT DISTINCT(TagId) AS Id, Tag AS [Text], @TypeId AS TypeId FROM TyLePhanBoWebsite WHERE DmSanPhamREF IN ('+ @FilterValue +') ORDER BY Tag'
			--WHEN 'HaveATagWebsite' THEN
			--'SELECT DISTINCT(DmSanPhamREF) AS Id, TenSanPham AS [Text] FROM TyLePhanBoWebsite'			
			
			-- Website --
			WHEN 'WebsiteAll' THEN			
			'SELECT dw.DmWebsiteID AS Id, dw.TenWebsite AS [Text], @TypeId AS TypeId FROM DmWebsite dw ORDER BY dw.TenWebsite'
			
			WHEN 'WebsiteByTag' THEN			
			'SELECT DISTINCT(dw.DmWebsiteID) AS Id, dw.TenWebsite AS [Text], @TypeId AS TypeId FROM DmWebsite dw
			 JOIN TyLePhanBoWebsite tlpbw
			 ON dw.WebsiteLink = tlpbw.Website
			 WHERE tlpbw.TagID IN (' + @FilterValue + ')			
			 ORDER BY dw.TenWebsite'
	
			-- Nhãn --
			WHEN 'Label' THEN			
			'SELECT TOP ' + CONVERT(NVARCHAR(4), @Count) + ' * FROM (SELECT DISTINCT(NhanHang) AS [Text], NhanHang AS Id, @TypeId AS TypeId FROM HopDongChiTiet
			 WHERE DeletedStatus = 0 AND NhanHang <> '''' AND NhanHang LIKE N''%' + @FilterValue + '%'') AS T'

			-- Ngành -- 
			WHEN 'Industry' THEN
			'SELECT TOP ' + CONVERT(NVARCHAR(4), @Count) + ' * FROM (SELECT DISTINCT(TenNhomNganh) AS [Text], TenNhomNganh AS Id, @TypeId AS TypeId FROM HopDongChiTiet
			 WHERE DeletedStatus = 0 AND TenNhomNganh <> '''' AND TenNhomNganh LIKE N''%' + @FilterValue + '%'') AS T'
		END
	)
	
	PRINT @Sql
	EXEC (@Sql) 			            	
END

```
