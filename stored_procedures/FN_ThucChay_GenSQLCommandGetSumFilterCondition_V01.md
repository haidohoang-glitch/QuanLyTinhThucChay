# Function: `ThucChay_GenSQLCommandGetSumFilterCondition_V01`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-30 14:02:37.173000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.923000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@GroupFieldName` | `nvarchar(400)` | No |
| `@GroupByFildID` | `nvarchar(400)` | No |
| `@GroupByFild` | `nvarchar(400)` | No |
| `@FilterString` | `nvarchar(800)` | No |
| `@IsHaveValue` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-29
-- Description:	Generate SQL Command GetSumFilterCondition
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandGetSumFilterCondition_V01]
(
	-- Add the parameters for the function here
	@GroupFieldName NVARCHAR(200),
	@GroupByFildID NVARCHAR(200),
	@GroupByFild NVARCHAR(200),
	@FilterString NVARCHAR(400),
	@IsHaveValue NVARCHAR(4000)
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	
	SET @DauNhay='''' 

	SET @Sql = 
	'
		SELECT T.' + @GroupFieldName + ',T.ID,T.DonViTinh,
				SUM(GiaTriThayDoi) AS GiaTriThayDoi,
				SUM(SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
				SUM(SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
				SUM(SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
				SUM(SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo,
				SUM(SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
				SUM(SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
				ROUND(SUM(ThanhTienThucChayNoiBo),0) AS ThanhTienThucChayNoiBo,
				ROUND(SUM(ThanhTienThucChayKhuyenMai),0) AS ThanhTienThucChayKhuyenMai,
				ROUND(SUM(ThanhTienThucThu),0) AS ThanhTienThucThu,
				ROW_NUMBER() OVER (ORDER BY T.' + @GroupFieldName + ') AS num
			FROM 
			(
				SELECT '
					+ @GroupFieldName + ','
					+ @GroupByFildID + ' HopDongChiTietREF,MAX(NgayThucHien) AS NgayThucHien,
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
					CASE WHEN isKhuyenMai = 1 THEN ISNULL(SUM(ThanhTienKM),0) 
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
				+ @GroupFieldName+ ',' + @GroupByFild + ',dbo.FormatDonViTinh(DonViTinh),isKhuyenMai,TenMaHopDong,HopDongChiTietREF			
			) T
			WHERE ' + @IsHaveValue + '
			GROUP BY T.ID,T.DonViTinh,' + @GroupFieldName +'
	'
	RETURN @Sql

END

```
