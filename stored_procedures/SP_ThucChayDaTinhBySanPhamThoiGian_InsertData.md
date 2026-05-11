# Stored Procedure: `ThucChayDaTinhBySanPhamThoiGian_InsertData`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-01-26 14:51:29.817000
- **Ngày sửa cuối**: 2015-01-26 14:51:29.817000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-23
-- Description:	<Description,,>
-- =============================================
/*
	Nam 2013
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-01-01', '2013-01-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-02-01', '2013-02-28'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-03-01', '2013-03-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-04-01', '2013-04-30'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-05-01', '2013-05-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-06-01', '2013-06-30'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-07-01', '2013-07-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-08-01', '2013-08-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-09-01', '2013-09-30'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-10-01', '2013-10-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-11-01', '2013-11-30'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2013-12-01', '2013-12-31'
	
	Nam 2014
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-01-01', '2014-01-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-02-01', '2014-02-28'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-03-01', '2014-03-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-04-01', '2014-04-30'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-05-01', '2014-05-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-06-01', '2014-06-30'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-07-01', '2014-07-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-08-01', '2014-08-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-09-01', '2014-09-30'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-10-01', '2014-10-31'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-11-01', '2014-11-30'
	EXEC dbo.ThucChayDaTinhBySanPhamThoiGian_InsertData '2014-12-01', '2014-12-31'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinhBySanPhamThoiGian_InsertData]
	-- Add the parameters for the stored procedure here
	@StartDate	DATETIME, 
	@EndDate	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	-- delete data truoc khi insert
	DELETE FROM ThucChayDaTinhBySanPhamThoiGian WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
	
	-- Insert data
	INSERT INTO ThucChayDaTinhBySanPhamThoiGian
    SELECT
		NEWID(),
		A.DmSanPhamREF, A.TenSanPham, A.DonViTinh,
		A.DmHinhThucQuangCao, A.TenHinhThucQuangCao,
		A.HopDongID, A.SoHopDong, A.DmMaHopDongREF, A.TenMaHopDong,
		A.DmPhongBanREF, A.TenPhongBan,
		A.DmBoPhanREF, A.TenBoPhan, 
		A.DmNhomLamViecREF, A.TenNhomLamViec, 
		A.SysNhanVienREF, A.TenDangNhap, A.TenNhanVien,		
		-- SoLuong
		CAST(A.SoLuongThucChayNoiBo AS BIGINT) AS SoLuongThucChayNoiBo, 
		CAST(A.SoLuongThucChayKhuyenMai AS BIGINT) AS SoLuongThucChayKhuyenMai, 
		CAST(A.SoLuongThucChayThucThu AS BIGINT) AS SoLuongThucChayThucThu,
		-- ThanhTien
		A.ThanhTienThucChayNoiBo, 
		A.ThanhTienThucChayKhuyenMai, 
		A.ThanhTienThucThu AS ThanhTienThucChay,
		-- GiaTriThayDoi
		A.GiaTriThayDoiNB, 
		A.GiaTriThayDoiTC,
		A.NgayThucHien,
		GETDATE() CreatedAt,
		'nhatmq' CreatdBy,
		GETDATE() CreatedAt,
		'nhatmq' CreatdBy,
		'' GhiChu
	FROM
	(
		SELECT
			DmSanPhamREF, TenSanPham, DmHinhThucQuangCao, TenHinhThucQuangCao, HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong,
			MAX(NgayThucHien) AS NgayThucHien,			
			CASE WHEN DmPhongBanREF > 0 THEN TenPhongBan
				 WHEN DmPhongBanREF = 0 THEN 'Management'
				 ELSE '-'
			END AS TenPhongBan, 
			DmPhongBanREF, 
			CASE WHEN DmBoPhanREF > 0 THEN TenBoPhan
				 WHEN DmBoPhanREF = 0 THEN 'Management'
				 ELSE '-'   
			END AS TenBoPhan, 
			DmBoPhanREF, 
			CASE WHEN DmNhomLamViecREF > 0 THEN TenNhomLamViec
				 WHEN DmNhomLamViecREF = 0 THEN 'Management'
				 ELSE '-'   
			END AS TenNhomLamViec, 
			DmNhomLamViecREF,
			SysNhanVienREF,TenDangNhap, TenNhanVien,
			SUM(GiaTriThayDoi) AS GiaTriThayDoi,
			dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
			CASE WHEN (UPPER(TenMaHopDong) LIKE 'NB%' OR TenMaHopDong LIKE '%SH%' OR SoHopDong LIKE '%soha%') THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
				ELSE 0
			END AS SoLuongThucChayNoiBo,
			ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
			CASE WHEN (UPPER(TenMaHopDong) NOT LIKE 'NB%' AND TenMaHopDong NOT LIKE '%SH%' AND SoHopDong NOT LIKE '%soha%') THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
				ELSE 0
			END AS SoLuongThucChayThucThu,
			CASE WHEN (UPPER(TenMaHopDong) LIKE 'NB%' OR TenMaHopDong LIKE '%SH%' OR SoHopDong LIKE '%soha%') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
				ELSE 0
			END AS ThanhTienThucChayNoiBo,
			ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,						
			CASE WHEN (UPPER(TenMaHopDong) NOT LIKE 'NB%' AND TenMaHopDong NOT LIKE '%SH%' AND SoHopDong NOT LIKE '%Soha%') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
				ELSE 0
			END AS ThanhTienThucThu,
			CASE WHEN (UPPER(TenMaHopDong) LIKE 'NB%' OR TenMaHopDong LIKE '%SH%' OR SoHopDong LIKE '%soha%') THEN ISNULL(SUM(GiaTriThayDoi),0) 
				ELSE 0
			END AS GiaTriThayDoiNB,
			CASE WHEN (UPPER(TenMaHopDong) NOT LIKE 'NB%' AND TenMaHopDong NOT LIKE '%SH%' AND SoHopDong NOT LIKE '%Soha%') THEN ISNULL(SUM(GiaTriThayDoi),0) 
				ELSE 0
			END AS GiaTriThayDoiTC
		FROM ThucChayDaTinh 
		WHERE TrangThaiHopDong <> 3
			AND CONVERT(Date,NgayThucHien) BETWEEN @StartDate AND @EndDate
		GROUP BY DmSanPhamREF,TenSanPham, DmHinhThucQuangCao, TenHinhThucQuangCao, HopDongID,SoHopDong,TenMaHopDong,dbo.FormatDonViTinh(DonViTinh),SoHopDong,
			TenPhongBan,DmPhongBanREF,DmMaHopDongREF,
			TenBoPhan, DmBoPhanREF, TenNhomLamViec, DmNhomLamViecREF, SysNhanVienREF, TenDangNhap,TenNhanVien, NgayThucHien	)A
	WHERE 
		ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucThu <> 0 OR GiaTriThayDoi <> 0
		OR SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayThucThu <> 0 OR SoLuongThucChayKhuyenMai <> 0
END

```
