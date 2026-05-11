# Stored Procedure: `ThucChayAdmarketSaleHopDong_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:25.730000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.373000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-06
-- Description:	<Description,,>
-- =============================================
-- exec ThucChayAdmarketSaleHopDong_Insert '2013-09-01'
CREATE PROCEDURE [dbo].[ThucChayAdmarketSaleHopDong_Insert] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	INSERT INTO ThucChayAdmarketSaleHopDong
	
    SELECT 
		dbo.ThucChay_Admarket_FormatSoHopDong(A.[Contract]),
		B.NgayKyHopDong,B.NgayDanhSoHopDong,
		B.SysNhanVienREF,B.TenDangNhap,B.TenNhanVien,
		B.DmPhongBanREF,B.TenPhongBan,
		B.DmBoPhanREF,B.TenBoPhan,
		B.DmNhomLamViecREF,B.TenNhom,
		B.DmDiaDiemLamViecREF,B.TenDiaDiemLamViec,
		A.DmSanPhamREF, A.TenSanPham, 
		'Click',
		SUM(CAST(A.Click AS BIGINT)) AS TongClick,
		SUM(CAST(A.[View] AS BIGINT)) AS TongView,
		SUM(A.[Money]) AS ThanhTienThucChay,
		0 AS ThanhTienKhuyenMai,
		A.NgayThucHien,
		'nhatmq', GETDATE(),'nhatmq', GETDATE()
	FROM ThucChayAdmarketHopDong A
		LEFT JOIN HopDong B ON dbo.ThucChay_Admarket_FormatSoHopDong(A.[Contract]) = B.SoHopDong
	WHERE 1=1 
		AND CONVERT(Date,A.NgayThucHien) <= @NgayThucHien
    GROUP BY
		A.[Contract],
		A.DmSanPhamREF, A.TenSanPham, 
		--B.SoHopDong, 
		B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien,B.SoHopDong,B.NgayKyHopDong,B.NgayDanhSoHopDong,
		B.SysNhanVienREF,B.TenDangNhap,B.TenNhanVien,
		B.DmPhongBanREF,B.TenPhongBan,
		B.DmBoPhanREF,B.TenBoPhan,
		B.DmNhomLamViecREF,B.TenNhom,
		B.DmDiaDiemLamViecREF,B.TenDiaDiemLamViec,
		A.DmSanPhamREF, A.TenSanPham,A.NgayThucHien
	;

	--INSERT INTO ThucChayAdmarketSaleHopDong(
	--	SysNhanVienREF,TenNhanVien,
	--	DmSanPhamREF,TenSanPham,
	--	DonViTinh,
	--	TongClick, TongView,
	--	TongTienThucChay, TongTienKhuyenMai,
	--	NgayThucHien,
	--	CreatedBy, CreatedAt,
	--	LastModifiedBy, LastModifiedAt
	--)	
	--SELECT
	--	dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone) AS SysNhanVienREF,
	--	ISNULL((SELECT HoVaTen FROM dbo.GetNhanVienInfoByNhanVienID(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),@NgayThucHien)),A.FullName) AS TenNhanVien,
		
	--	A.DmSanPhamREF,
	--	A.TenSanPham,
	--	'Click',
	--	(SUM(A.TTC) -
	--	(SELECT TongClick 
	--	FROM dbo.ThucChayAdmarketGetGiaTriCoHopDongByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.DmSanPhamREF,CONVERT(Date,A.CreateDate))
	--	))AS TongClick,
		
	--	(SUM(A.TTV) -
	--	(SELECT TongView 
	--	FROM dbo.ThucChayAdmarketGetGiaTriCoHopDongByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.DmSanPhamREF,CONVERT(Date,A.CreateDate))
	--	))AS TongView,
		
	--	(SUM(A.[Money]) -
	--	(SELECT TongTienThucChay 
	--	FROM dbo.ThucChayAdmarketGetGiaTriCoHopDongByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.DmSanPhamREF,CONVERT(Date,A.CreateDate))
	--	))AS TongTienThucChay,
		
	--	(SUM(CONVERT(float,A.Promotion)) -
	--	(SELECT TongTienKhuyenMai 
	--	FROM dbo.ThucChayAdmarketGetGiaTriCoHopDongByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.DmSanPhamREF,CONVERT(Date,A.CreateDate))
	--	))AS TongTienKhuyenMai,
		
	--	A.CreateDate,
	--	'nhatmq',GETDATE(),'nhatmq',GETDATE()
	--FROM ThucChayAdmarket A
	--WHERE
	--	CONVERT(Date,A.CreateDate) = @NgayThucHien
	--GROUP BY
	--	A.FullName, A.Email, A.Phone, A.DmSanPhamREF, A.CreateDate, A.DmSanPhamREF, A.TenSanPham
END

```
