# Stored Procedure: `ThucChay_UpdateLechTreoHaThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-10 13:46:15.347000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.290000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE PROCEDURE [dbo].[ThucChay_UpdateLechTreoHaThucChayDaTinh] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN

DECLARE @NgayThucHien DATETIME
set @NgayThucHien = @StartDate
	--XOA DU LIEU LECH TREO HA
	DELETE FROM ThucChay_TienLechTreoHaTheoSanPham
	WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
	
	while(@NgayThucHien < @EndDate)
	Begin

		INSERT INTO dbo.ThucChay_TienLechTreoHaTheoSanPham 
		SELECT NEWID()
			, TH.DmSanPhamREF
			, TH.TenSanPham
			, TH.SoHopDong
			, TH.HopDongChiTietREF
			, 'VIEW' AS DonViTinh
			, ISNULL((TH.TongPageView - TH.TongSoLuongHD),0) AS TongViewLechTreoHa
			, ISNULL((TH.TongPageView - TH.TongSoLuongHD)*(TH.DonGiaSauCK/1000),0) AS ThanhTienLechTreoHa
			, TH.NgayThucHien
			, 'ASD' CreatedBy
			, GETDATE() CreatedAt
			, 'ASD' LastModifiedBy
			, GETDATE() LastModifiedAt
			, 0 DeletedStatus
			, 0 PrintStatus
			, 0 RecordStatus
		FROM 
			(
			SELECT	 tcdt.DmSanPhamREF
					, tcdt.TenSanPham
					, tcdt.SoHopDong
					, tcdt.HopDongChiTietREF	
					, tcdt.NgayThucHien
					, (
						SELECT SUM(isnull(TongViewThucChay,0)) FROM ThucChayDaTinh
						WHERE SoHopDong = tcdt.SoHopDong
						AND DmSanPhamREF = tcdt.DmSanPhamREF
						AND Convert(date,NgayThucHien) <= @NgayThucHien
						AND HopDongChiTietREF = tcdt.HopDongChiTietREF
					  ) TongPageView
					, MAX(tcdt.SoLuong) TongSoLuongHD
					, MAX(tcdt.DonGiaTheoDonVi) DonGiaSauCK
			FROM ThucChayDaTinh tcdt
			WHERE tcdt.DmSanPhamREF IN (231,238,339,342,337,240,370)
			AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
			GROUP BY tcdt.SoHopDong, tcdt.DmSanPhamREF,tcdt.TenSanPham, tcdt.NgayThucHien, tcdt.HopDongChiTietREF
			)TH
			WHERE th.TongPageView > th.TongSoLuongHD
			ORDER BY th.SoHopDong, th.DmSanPhamREF, th.NgayThucHien

	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
		
	end 	 

SELECT '1'
END


--EXEC [ThucChay_InsertThucChayDaTinh_PR] '2013-01-01','2013-07-11'

```
