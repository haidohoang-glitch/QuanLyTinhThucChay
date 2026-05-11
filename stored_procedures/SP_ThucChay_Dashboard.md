# Stored Procedure: `ThucChay_Dashboard`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-14 13:08:24.517000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.913000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `nvarchar(400)` | No |
| `@ToDate` | `nvarchar(400)` | No |
| `@LoaiBaoCao` | `int(4)` | No |
| `@DonViThoiGian` | `int(4)` | No |
| `@ListSanPhamID` | `nvarchar(4000)` | No |
| `@ListWebsiteID` | `nvarchar(4000)` | No |
| `@ListSoHopDong` | `nvarchar(4000)` | No |
| `@ListPhongID` | `nvarchar(4000)` | No |
| `@ListBoPhanID` | `nvarchar(4000)` | No |
| `@ListNhomID` | `nvarchar(4000)` | No |
| `@ListUserName` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_Dashboard]
	@FromDate nvarchar(200), 
	@ToDate nvarchar(200),
	@LoaiBaoCao int, -- 1: San pham; 2: Website; 3: Hop dong; 4: Doi ban; 5: Phong ban; 6: Bo phan; 7: Nhan vien
	@DonViThoiGian int,
	@ListSanPhamID nvarchar(2000),
	@ListWebsiteID nvarchar(2000),
	@ListSoHopDong nvarchar(2000),
	@ListPhongID nvarchar(2000),
	@ListBoPhanID nvarchar(2000),
	@ListNhomID nvarchar(2000),
	@ListUserName nvarchar(2000)
AS
BEGIN
	--CASE @LoaiBaoCao
	--	WHEN 1 THEN
	--		EXEC dbo.ThucChay_DashboardSanPham
	--			@ListSanPhamID,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	--	WHEN 2 THEN
	--		EXEC dbo.ThucChay_DashboardSanPham
	--			@ListWebsiteID,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	--	WHEN 3 THEN
	--		EXEC dbo.ThucChay_DashboardSanPham
	--			@ListSoHopDong,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	--	WHEN 4 THEN
	--		EXEC dbo.ThucChay_DashboardSanPham
	--			@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	--END;
	IF @LoaiBaoCao = 1 
		EXEC dbo.ThucChay_DashboardSanPham
			@FromDate,@ToDate,@ListSanPhamID,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	ELSE IF @LoaiBaoCao = 2 
		EXEC dbo.ThucChay_DashboardWebsite
			@FromDate,@ToDate,@ListWebsiteID,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	ELSE IF @LoaiBaoCao = 3 
		EXEC dbo.ThucChay_DashboardHopDong
			@FromDate,@ToDate,@ListSoHopDong,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	ELSE IF @LoaiBaoCao = 4
		EXEC dbo.ThucChay_DashboardDoiBan
			@FromDate,@ToDate,@ListSanPhamID,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	ELSE IF @LoaiBaoCao = 5
		EXEC dbo.ThucChay_DashboardPhongBan
			@FromDate,@ToDate,@ListSanPhamID,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	ELSE IF @LoaiBaoCao = 6
		EXEC dbo.ThucChay_DashboardBoPhan
			@FromDate,@ToDate,@ListSanPhamID,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
	ELSE IF @LoaiBaoCao = 7
		EXEC dbo.ThucChay_DashboardNhanVien
			@FromDate,@ToDate,@ListSanPhamID,@ListPhongID,@ListBoPhanID,@ListNhomID,@ListUserName,@DonViThoiGian
END

```
