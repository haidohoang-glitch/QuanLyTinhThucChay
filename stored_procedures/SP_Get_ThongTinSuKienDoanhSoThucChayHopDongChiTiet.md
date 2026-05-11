# Stored Procedure: `Get_ThongTinSuKienDoanhSoThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-02-02 16:10:30.740000
- **Ngày sửa cuối**: 2015-02-02 16:29:38.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@DmThongTinSuKienREF` | `int(4)` | No |
| `@TenThongTinSuKien` | `nvarchar(400)` | No |
| `@LoaiSuKien` | `int(4)` | No |
| `@TenLoaiSuKien` | `nvarchar(200)` | No |
| `@GiaTriChinhSachApDung` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[Get_ThongTinSuKienDoanhSoThucChayHopDongChiTiet] '2014-12-01', '2014-12-31', 1, N'Khuyến mại CPM T12',1, N'Su kien ap dung sau', 10
CREATE PROCEDURE [dbo].[Get_ThongTinSuKienDoanhSoThucChayHopDongChiTiet] 
		@FromDate DATETIME,
		@ToDate DATETIME,
		@DmThongTinSuKienREF INT,
		@TenThongTinSuKien NVARCHAR(200),
		@LoaiSuKien INT,
		@TenLoaiSuKien NVARCHAR(100),
		@GiaTriChinhSachApDung INT
		
AS
BEGIN

	SELECT TT.* FROM 
	(
		SELECT @DmThongTinSuKienREF ThongTinSuKienREF, @TenThongTinSuKien TenThongTinSuKien, @LoaiSuKien ThongTinLoaiSuKien, A.HopDongID HopDongFK, A.SoHopDong, A.HopDongChiTietREF
		, A.DmKhachHangREF KhachHangREF, A.DmSanPhamREF,
		(
			CASE WHEN (SUM(A.SoLuongThucChay) <0) THEN 0
				ELSE  (SUM(A.SoLuongThucChay))
			END
		)SoLuongThucChay, A.DonViTinh
		, 0 DonGiaHopDong, @FromDate ThoiGianBatDau, @ToDate ThoiGianKetThuc, SUM(A.ThucThuTrongKy)GiaTriApDung, @GiaTriChinhSachApDung GiaTriChinhSachApDung
		, (SUM(A.ThucThuTrongKy)*@GiaTriChinhSachApDung)/100 ThanhTienSauApDung
		, (SUM(A.ThucThuTrongKy)*@GiaTriChinhSachApDung)/100 ChinhSachApDungThucTe
		, @GiaTriChinhSachApDung ThanhTienSauApDungThucTe
		, '' MoTa
		, 'Admin' CreatedBy
		, Getdate() CreatedAt
		, 'Admin' LastModifiedBy
		, getdate() LastModifiedAt
		, 0 DeletedStatus
		, 0 RecordStatus
		, 0	PrintStatus
		FROM
		(
			SELECT * 
			
			  FROM
			(
			SELECT tcdt.HopDongID, tcdt.SoHopDong
			, tcdt.HopDongChiTietREF, hd.DmKhachHangREF, tcdt.DmSanPhamREF, tcdt.DonViTinh
			, SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) SoLuongThucChay
			, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThucThuTrongKy
			, 'Admin' CreatedBy
			, Getdate() CreatedAt
			, 'Admin' LastModifiedBy
			, getdate() LastModifiedAt
			, 0 DeletedStatus
			, 0 RecordStatus
			, 0	PrintStatus
			  FROM ThucChayDaTinh tcdt
			  INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
			WHERE 1=1
			AND convert(date,tcdt.NgayThucHien) BETWEEN @FromDate AND @ToDate
			AND tcdt.TrangThaiHopDong <> 3
			AND tcdt.HopDongID <> 0	
			GROUP BY tcdt.HopDongID, tcdt.SoHopDong,hd.DmKhachHangREF
			, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.DonViTinh
			)A
			WHERE 1=1 
			AND round(A.ThucThuTrongKy,0) <> 0 
			UNION ALL
			SELECT * FROM
			(
			SELECT tcdt.HopDongID, tcdt.SoHopDong
			, tcdt.HopDongChiTietREF,hd.DmKhachHangREF, tcdt.DmSanPhamREF, tcdt.DonViTinh
			, SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) SoLuongThucChay
			, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThucThuTrongKy
			, 'Admin' CreatedBy
			, Getdate() CreatedAt
			, 'Admin' LastModifiedBy
			, getdate() LastModifiedAt
			, 0 DeletedStatus
			, 0 RecordStatus
			, 0	PrintStatus
			  FROM ThucChayDaTinhAdmarket tcdt
			  INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
			WHERE 1=1
			AND convert(date,tcdt.NgayThucHien) BETWEEN @FromDate AND @ToDate
			AND tcdt.HopDongID <> 0
			AND tcdt.TrangThaiHopDong <> 3	
			GROUP BY tcdt.HopDongID, tcdt.SoHopDong,hd.DmKhachHangREF
			, tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.DonViTinh
			)A
			WHERE 1=1 
			AND (round(A.ThucThuTrongKy,0) <> 0)
		)A
		GROUP BY A.HopDongID, A.SoHopDong, A.HopDongChiTietREF
		, A.DmKhachHangREF, A.DmSanPhamREF, A.DonViTinh
	)TT
	WHERE TT.SoLuongThucChay >0
	AND TT.GiaTriApDung >0

END

```
