# Stored Procedure: `ThucChay_BaoCaoThucChayLechTreoHa`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-15 11:59:58.023000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.293000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_BaoCaoThucChayLechTreoHa]
-- Add the parameters for the stored procedure here		
	@PageIndex Int,
	@RecordCount Int,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000)
AS
BEGIN	
	--- Declare Variable --------
	declare @StartIndex Int
	declare @MaxRecords Int
	declare @i Int
	declare @PageCount INT
	declare @ApproximatedNumber float	

	Declare @DauNhay nvarchar(50)
	set @DauNhay = ''''
	Declare @FilterSQLCommandLTH nvarchar(4000)
	Declare @FilterSQLCommand nvarchar(4000)
	DECLARE @SQL NVARCHAR(max)	
	
	SET @FilterSQLCommandLTH = ' AND CONVERT(DATE,NgayThucHien) = ' + @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	SET @FilterSQLCommand = ' '
	
	IF(@DmSanPhamREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and a.DmSanPhamREF in (' + @DmSanPhamREFList + ')'
	if(@SoHopDongList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and a.SoHopDong in (' + @SoHopDongList + ')'	

	SET @SQL = '
		SELECT TOP (' + CONVERT(NVARCHAR,@RecordCount) + ') T.* FROM 
		(
			SELECT a.NgayThucHien
			, a.SoHopDong
			, a.TenSanPham
			, b.TongTTSauTrietKhau
			, b.SoLuong
			, (b.SoLuong + a.TongViewLechTreoHa) TongViewThucChay
			, b.DonGiaTheoDonVi
			, a.TongViewLechTreoHa
			, a.ThanhTienLechTreoHa
			, ROW_NUMBER() OVER (ORDER BY a.NgayThucHien,a.SoHopDong,a.TenSanPham ) AS num
			  FROM
			(
				SELECT * FROM ThucChay_TienLechTreoHaTheoSanPham a
				WHERE ' + @FilterSQLCommandLTH + '
			)a
			LEFT JOIN 
			(
				SELECT b.SoHopDong, b.DmSanPhamREF, b.TenSanPham,b.SoLuong, b.DonGiaTheoDonVi
				FROM ThucChayDaTinh b 
			)b ON a.SoHopDong = b.SoHopDong AND a.DmSanPhamREF = b.DmSanPhamREF
		)T 
		WHERE num >' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount)
	
	IF(@DmSanPhamREFList <> '')
		set @SQL = @SQL + ' and T.DmSanPhamREF in (' + @DmSanPhamREFList + ') '
	if(@SoHopDongList <> '')
		set @SQL = @SQL + ' and T.SoHopDong in (' + @SoHopDongList + ') '
		+ ' ORDER BY T.num '
	
	PRINT @SQL;
	EXEC sp_executesql @SQL;
END

```
