# Stored Procedure: `ThucChayDaTinhAdmarketSale_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:23.407000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.160000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-06
-- Description:	<Description,,>
-- =============================================
-- exec ThucChayDaTinhAdmarketSale_Insert '2014-04-22', '2014-04-22'
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarketSale_Insert] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	-- Xoa du lieu
	DELETE FROM ThucChayDaTinhAdmarketSale WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
	
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	
	WHILE (@NgayThucHien <= @EndDate)
    BEGIN
		INSERT INTO ThucChayDaTinhAdmarketSale(
			SoHopDong, NgayKyHopDong, NgayDanhSo,
			SysNhanVienREF, TenDangNhap, TenNhanVien,
			DmPhongBanREF, TenPhongBan,
			DmBoPhanREF, TenBoPhan,
			DmNhomLamViecREF, TenNhomLamVIec,
			DmDiaDiemLamViecREF, TenDiaDiemLamViec,
			DmSanPhamREF,TenSanPham,
			DonViTinh,
			TongClick, TongView,
			TongTienThucChay, TongTienKhuyenMai,
			NgayThucHien,
			CreatedBy, CreatedAt,
			LastModifiedBy, LastModifiedAt
		)	
		SELECT
			'-' SoHopDong,
			'1900-01-01' NgayKyHopDong, '1900-01-01' NgayDanhSo,
			dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone) AS SysNhanVienREF,
			ISNULL
			(
				(SELECT TOP 1 AdminPermisionHDCN.TenDangNhap FROM AdminPermisionHDCN where AdminPermisionHDCN.NhanSuSoYeuLyLichID = dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone)),
				'_blank_' + A.FullName
			) AS TenDangNhap,
			--ISNULL((SELECT TOP 1 HoVaTen FROM dbo.GetNhanVienInfoByNhanVienID(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate)),A.FullName) AS TenNhanVien,
			ISNULL((SELECT NS.HoVaTen FROM NhanSuSoYeuLyLichFull NS WHERE NS.NhanSuSoYeuLyLichID = dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone)),A.FullName) AS TenNhanVien,
			--(SELECT TOP 1 DmPhongBanREF FROM dbo.AdmarketGetQuaTrinhCongTacByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate,A.CreateDate)) AS DmPhongBanREF,
			--(SELECT TOP 1 TenPhongBan FROM dbo.AdmarketGetQuaTrinhCongTacByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate,A.CreateDate)) AS TenPhongBan,
			--(SELECT TOP 1 DmBoPhanREF FROM dbo.AdmarketGetQuaTrinhCongTacByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate,A.CreateDate)) AS DmBoPhanREF,
			--(SELECT TOP 1 TenBoPhanNghiepVu FROM dbo.AdmarketGetQuaTrinhCongTacByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate,A.CreateDate)) AS TenBoPhan,
			--(SELECT TOP 1 DmNhomLamViecREF FROM dbo.AdmarketGetQuaTrinhCongTacByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate,A.CreateDate)) AS DmNhomLamViecREF,
			--(SELECT TOP 1 TenNhomLamViec FROM dbo.AdmarketGetQuaTrinhCongTacByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate,A.CreateDate)) AS TenNhomLamViec,
			--(SELECT TOP 1 DmDiaDiemLamViecREF FROM dbo.AdmarketGetQuaTrinhCongTacByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate,A.CreateDate)) AS DmDiaDiemLamViecREF,
			--(SELECT TOP 1 TenDiaDiemLamViec FROM dbo.AdmarketGetQuaTrinhCongTacByNhanVien(dbo.ThucChayAdmarketGetNhanVienID(A.FullName,A.Email,A.Phone),A.CreateDate,A.CreateDate)) AS TenDiaDiemLamViec,
			0 DmPhongBanREF,
			'' TenPhongBan,
			0 DmBoPhanREF,
			'' TenBoPhan,
			0 DmNhomLamViecREF,
			'' TenNhomLamViec,
			0 DmDiaDiemLamViecREF,
			'' TenDiaDiemLamViec,
			A.DmSanPhamREF,
			A.TenSanPham,
			CASE WHEN A.DmSanPhamREF = 337 THEN 'View'
				ELSE 'Click'
			END DonViTinh,
			CAST(ISNULL(SUM(A.TTC),0) AS BIGINT) AS TongClick,
		
			CAST(ISNULL(SUM(A.TTV),0) AS BIGINT) AS TongView,
		
			SUM(ISNULL(A.[Money],0)/1.1) AS TongTienThucChay,
		
			ISNULL(SUM(CONVERT(float,A.Promotion)/1.1),0) AS TongTienKhuyenMai,
		
			@NgayThucHien,
			'nhatmq' CreatedBy,@NgayThucHien CreatedAt,'nhatmq' LastModifiedBy,@NgayThucHien LastModifiedAt
		FROM ThucChayAdmarket A
		WHERE
			A.CreateDate BETWEEN @StartDate AND @EndDate  --AND DmSanPhamREF = 299
		GROUP BY
			A.FullName, A.Email, A.Phone, A.DmSanPhamREF, A.CreateDate, A.DmSanPhamREF, A.TenSanPham
		ORDER BY 
			A.FullName, A.CreateDate;
			
		EXEC ThucChayDaTinhAdmarketSale_InsertByDay 144, 'CPC Admarket', 'Click', @NgayThucHien;
		
		EXEC ThucChayDaTinhAdmarketSale_InsertByDay 299, 'CPC Plus Admarket', 'Click', @NgayThucHien;
		
		EXEC ThucChayDaTinhAdmarketSale_InsertByDay 337, 'CPM Admarket', 'View', @NgayThucHien;
		
		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
	
	END
END

```
