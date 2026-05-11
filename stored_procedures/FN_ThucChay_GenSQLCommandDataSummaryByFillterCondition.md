# Function: `ThucChay_GenSQLCommandDataSummaryByFillterCondition`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-28 15:07:17.593000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.473000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@GroupByFildID` | `nvarchar(4000)` | No |
| `@GroupByFild` | `nvarchar(4000)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-28
-- Description:	Generate SQL command get summary 
-- =============================================
CREATE FUNCTION dbo.ThucChay_GenSQLCommandDataSummaryByFillterCondition
(
	-- Add the parameters for the function here
	@GroupFieldName nvarchar(50),
	@GroupByFildID NVARCHAR(2000),
	@GroupByFild NVARCHAR(2000),
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000)
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
    DECLARE @DauNhay NVARCHAR(50);
	DECLARE @FilterString NVARCHAR(4000);
	
    SET @DauNhay = '''';
    
    SET @FilterString =  dbo.GetThucChayFilterString(
														@StartDate ,
														@EndDate ,
														@DmSanPhamREFList ,
														@DmWebsiteREFList ,
														@SoHopDongList ,
														@DmPhongBanREFList ,
														@DmBoPhanREFList ,
														@DmNhomLamViecREFList ,
														@TenNhanVienList 
													)
	
	SET @Sql = 'SELECT  ' +
					@GroupFieldName + ',' + @GroupByFildID + 'HopDongChiTietREF,MAX(NgayThucHien) AS NgayThucHien,
					dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
					SUM(GiaTriThayDoi) AS GiaTriThayDoi,
					-- So luong theo Hop dong
					-- == So luong hop dong noi bo
					CASE WHEN UPPER(TenMaHopDong) LIKE '+ @DauNhay + 'NB%'+ @DauNhay +' THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongNoiBo,
					-- == So luong hop dong khuyen mai
					CASE WHEN isKhuyenMai = 1 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongKhuyenMai,
					-- == So luong hop dong thuc thu
					CASE WHEN (isKhuyenMai <> 1 AND UPPER(TenMaHopDong) NOT LIKE '+ @DauNhay + 'NB%'+ @DauNhay +') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongThucThu,
					
					-- So luong Thuc chay
					-- == So luong thuc chay noi bo
					CASE WHEN UPPER(TenMaHopDong) LIKE '+ @DauNhay + 'NB%'+ @DauNhay +' THEN ISNULL(SUM(SoLuongThucChay),0) 
						ELSE 0
					END AS SoLuongThucChayNoiBo,
					-- == So luong thuc chay khuyen mai
					CASE WHEN isKhuyenMai = 1 THEN ISNULL(SUM(SoLuongThucChay),0) 
						ELSE 0
					END AS SoLuongThucChayKhuyenMai,
					-- == So luong thuc chay thuc thu
					CASE WHEN (isKhuyenMai <> 1 AND UPPER(TenMaHopDong) NOT LIKE '+ @DauNhay + 'NB%'+ @DauNhay +') THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongThucChayThucThu,
										
					-- Thanh tien Thuc chay
					-- == Thanh tien thuc chay noi bo
					CASE WHEN UPPER(TenMaHopDong) LIKE '+ @DauNhay + 'NB%'+ @DauNhay +' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
						ELSE 0
					END AS ThanhTienThucChayNoiBo,
					-- == Thanh tien thuc chay khuyen mai
					CASE WHEN isKhuyenMai = 1 THEN ISNULL(SUM(ThanhTienThucChayTruocTrietKhau),0) 
						ELSE 0
					END AS ThanhTienThucChayKhuyenMai,
					-- == Thanh tien thuc chay thuc thu				
					CASE WHEN (isKhuyenMai <> 1 AND UPPER(TenMaHopDong) NOT LIKE '+ @DauNhay + 'NB%'+ @DauNhay +') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
						ELSE 0
					END AS ThanhTienThucThu
				FROM ThucChayDaTinh
				WHERE 1=1 
					AND dbo.ThucChay_CheckLechTreoHa(NgayThucHien, HopDongChiTietREF, TenSanPham) > 0 
					AND TrangThaiHopDong <> 3 
			'
	SET @Sql = @Sql + @FilterString;
	
	SET @Sql = @Sql +		
			'
			GROUP BY '
				+ @GroupFieldName+ ',' + @GroupByFild + ',dbo.FormatDonViTinh(DonViTinh),isKhuyenMai,TenMaHopDong,HopDongChiTietREF'

	-- Return the result of the function
	RETURN @Sql

END

```
