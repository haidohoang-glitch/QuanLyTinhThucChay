# Function: `ThucChay_GenSQLCommandGetContractFilterCondition`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-29 16:36:30.360000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.027000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@GroupFieldName` | `nvarchar(400)` | No |
| `@GroupByFildID` | `nvarchar(400)` | No |
| `@GroupByFild` | `nvarchar(400)` | No |
| `@FilterString` | `nvarchar(800)` | No |
| `@IsHaveValue` | `nvarchar(8000)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-29
-- Description:	GenSQLCommandGetContractFilterCondition 
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandGetContractFilterCondition] 
(
	-- Add the parameters for the function here
	@GroupFieldName NVARCHAR(200),
	@GroupByFildID NVARCHAR(200),
	@GroupByFild NVARCHAR(200),
	@FilterString NVARCHAR(400),
	@IsHaveValue NVARCHAR(4000),
	@DonViTinh NVARCHAR(50)
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
		SELECT 
				T.SoHopDong,T.DonViTinh,
				SUM(T.GiaTriThayDoi) AS GiaTriThayDoi,
				SUM(T.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
				SUM(T.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
				SUM(T.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
				SUM(T.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo,
				SUM(T.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
				SUM(T.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
				SUM(T.ThanhTienNoiBo) AS ThanhTienNoiBo,
				SUM(T.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(T.ThanhTienThucThu) AS ThanhTienThucChaySauChietKhau,
				CASE WHEN SUM(T.ThanhTienThucThu)-SUM(T.ThanhTienKhuyenMai) > 0 THEN (SUM(T.ThanhTienThucThu)-SUM(T.ThanhTienKhuyenMai)) 
					ELSE SUM(T.ThanhTienThucThu)
				END AS ThanhTienThucThu,
				ROW_NUMBER() OVER (ORDER BY SoHopDong) AS num
			FROM
			(
				SELECT 
					SoHopDong,'
					+ @GroupFieldName + ',
					dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
					MAX(NgayThucHien) AS NgayThucHien,SUM(GiaTriThayDoi) AS GiaTriThayDoi,
					
						CASE WHEN UPPER(TenMaHopDong) LIKE '+@DauNhay+'NB%'+@DauNhay+' THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
							ELSE 0
						END AS SoLuongHopDongNoiBo,
						CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
							ELSE 0
						END AS SoLuongHopDongKhuyenMai,
						CASE WHEN (ThanhTienKM = 0 AND UPPER(TenMaHopDong) NOT LIKE '+@DauNhay+'NB%'+@DauNhay+') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
							ELSE 0
						END AS SoLuongHopDongThucThu,
						
						CASE WHEN UPPER(TenMaHopDong) LIKE '+@DauNhay+'NB%'+@DauNhay+' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
							ELSE 0
						END AS SoLuongThucChayNoiBo,
						CASE WHEN ThanhTienKM > 0 THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
							ELSE 0
						END AS SoLuongThucChayKhuyenMai,
						CASE WHEN (ThanhTienKM = 0 AND UPPER(TenMaHopDong) NOT LIKE '+@DauNhay+'NB%'+@DauNhay+') THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
							ELSE 0
						END AS SoLuongThucChayThucThu,
																	
						CASE WHEN UPPER(TenMaHopDong) LIKE '+@DauNhay+'NB%'+@DauNhay+' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
							ELSE 0
						END AS ThanhTienNoiBo,
						CASE WHEN ThanhTienKM > 0 THEN ISNULL(SUM(ThanhTienKM),0) 
							ELSE 0
						END AS ThanhTienKhuyenMai,			
						CASE WHEN (ThanhTienKM = 0 AND UPPER(TenMaHopDong) NOT LIKE '+@DauNhay+'NB%'+@DauNhay+') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
							ELSE 0
						END AS ThanhTienThucThu
				FROM ThucChayDaTinh
				WHERE 1=1  
					AND dbo.ThucChay_CheckLechTreoHa(NgayThucHien, HopDongChiTietREF, TenSanPham) > 0 
					AND TrangThaiHopDong <> 3
				'
				
			SET @Sql = @Sql + @FilterString;
			
			SET @Sql = @Sql + ' AND dbo.FormatDonViTinh(DonViTinh) = ' + @DauNhay + @DonViTinh + @DauNhay
			
			SET @Sql = @Sql +		
				'
				GROUP BY '
					+ @GroupFieldName+ ',dbo.FormatDonViTinh(DonViTinh),SoHopDong,ThanhTienKM,TenMaHopDong
			) AS T
			GROUP BY T.SoHopDong,T.DonViTinh
	'

	-- Return the result of the function
	RETURN @Sql

END

```
