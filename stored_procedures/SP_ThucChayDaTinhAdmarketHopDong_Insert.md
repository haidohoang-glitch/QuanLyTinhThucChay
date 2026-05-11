# Stored Procedure: `ThucChayDaTinhAdmarketHopDong_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:30:37.313000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.030000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-25
-- Description:	<Description,,>
-- =============================================
-- EXEC ThucChayDaTinhAdmarketHopDong_Insert '2014-04-20','2014-04-20'
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarketHopDong_Insert] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	-- Xoa duu lieu
	DELETE FROM ThucChayDaTinhAdmarketHopDong WHERE NgayThucHien BETWEEN @StartDate AND @EndDate

	DECLARE @NgayThucHien DATETIME;
	
	SET @NgayThucHien = @StartDate;

	WHILE (@NgayThucHien <= @EndDate)
	BEGIN 

		INSERT INTO ThucChayDaTinhAdmarketHopDong
        (
           	[SoHopDong]
           ,[NgayKyHopDong]
           ,[NgayDanhSo]
           ,[SysNhanVienREF]
           ,[TenDangNhap]
           ,[TenNhanVien]
           ,[DmPhongBanREF]
           ,[TenPhongBan]
           ,[DmBoPhanREF]
           ,[TenBoPhan]
           ,[DmNhomLamViecREF]
           ,[TenNhomLamViec]
           ,[DmDiaDiemLamViecREF]
           ,[TenDiaDiemLamViec]
           ,[DmHinhThucQuangCao]
           ,[TenHinhThucQuangCao]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[DonViTinh]
           ,[TongClick]
           ,[TongView]
           ,[TongTienThucChay]
           ,[TongTienKhuyenMai]
           ,[NgayThucHien]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
        )
	
		SELECT 
			dbo.ThucChay_Admarket_FormatSoHopDong(A.[Contract]),
			B.NgayKyHopDong,
			B.NgayDanhSoHopDong,
			B.SysNhanVienREF,B.TenDangNhap,B.TenNhanVien,
			B.DmPhongBanREF,B.TenPhongBan,
			B.DmBoPhanREF,B.TenBoPhan,
			B.DmNhomLamViecREF,B.TenNhom,
			B.DmDiaDiemLamViecREF,B.TenDiaDiemLamViec,			
			CASE WHEN A.DmSanPhamREF = 337 THEN 6
				ELSE 7
			END AS DmHinhThucQuangCaoREF,
			CASE WHEN A.DmSanPhamREF = 337 THEN 'CPM'
				ELSE 'CPC'
			END AS TenHinhThucQuangCao,
			A.DmSanPhamREF, A.TenSanPham, 
			CASE WHEN A.DmSanPhamREF = 337 THEN 'View'
				ELSE 'Click'
			END DonViTinh,
			ISNULL(SUM(CAST(A.Click AS BIGINT)),0) AS TongClick,
			ISNULL(SUM(CAST(A.[View] AS BIGINT)),0) AS TongView,
			ISNULL(SUM(A.[Money]/1.1),0) AS ThanhTienThucChay,
			0 AS ThanhTienKhuyenMai,
			A.NgayThucHien,
			'nhatmq', GETDATE(),'nhatmq', GETDATE()
		FROM 
			(
				SELECT DISTINCT DmSanPhamREF, TenSanPham, Click, [View], [Money], NgayThucHien, [Contract]
				FROM ThucChayAdmarketHopDong
				WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
			)A
			LEFT JOIN HopDong B ON dbo.ThucChay_Admarket_FormatSoHopDong(A.[Contract]) = B.SoHopDong
		WHERE 1=1 
			AND CONVERT(Date,A.NgayThucHien) BETWEEN @StartDate AND @EndDate
		GROUP BY
			A.[Contract],
			A.DmSanPhamREF, A.TenSanPham, 
			--B.SoHopDong, 
			B.HopDongID,
			B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien,B.SoHopDong,B.NgayKyHopDong,B.NgayDanhSoHopDong,
			B.SysNhanVienREF,B.TenDangNhap,B.TenNhanVien,
			B.DmPhongBanREF,B.TenPhongBan,
			B.DmBoPhanREF,B.TenBoPhan,
			B.DmNhomLamViecREF,B.TenNhom,
			B.DmDiaDiemLamViecREF,B.TenDiaDiemLamViec,
			A.DmSanPhamREF, A.TenSanPham,A.NgayThucHien
		;
	
		-- insert gia tri khong hop dong
		EXEC ThucChayDaTinhAdmarketHopDong_InsertByDay 144,'CPC Admarket', 'Click', @NgayThucHien;
	
		EXEC ThucChayDaTinhAdmarketHopDong_InsertByDay 299,'CPC Plus Admarket', 'Click', @NgayThucHien;
	
		EXEC ThucChayDaTinhAdmarketHopDong_InsertByDay 337,'CPM Admarket', 'View', @NgayThucHien

		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
END

```
