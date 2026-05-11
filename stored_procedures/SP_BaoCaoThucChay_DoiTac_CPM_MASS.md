# Stored Procedure: `BaoCaoThucChay_DoiTac_CPM_MASS`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:11.480000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.567000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ColumnSort` | `nvarchar(100)` | No |
| `@OrderBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-24
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_CPM_MASS] 
	-- Add the parameters for the stored procedure here
	@PageIndex int,
	@RecordCount int,
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(2000),
	@DmWebsiteREFList nvarchar(2000),
	@SoHopDongList nvarchar(2000),
	@TenDangNhap nvarchar(50),
	@ColumnSort nvarchar(50),
	@OrderBy nvarchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Sql nvarchar(4000)
    DECLARE @DauNhay nvarchar(50)
    DECLARE @FillterString nvarchar(4000)
    DECLARE @OrderByString nvarchar(2000)
    
    SET @DauNhay = ''''
	
	SET @FillterString = ' AND IsPheDuyet = 1'	
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	SET @FillterString += ' AND (SoLuongThucChay <> 0 OR ThanhTienSauTrietKhauThucChay <> 0 OR SoLuongThucChayKM <> 0 OR ThanhTienKM <> 0)'
	
	IF @ColumnSort = 'SoHopDong'
		SET @OrderByString = 'SoHopDong'
	ELSE IF @ColumnSort = 'SoLuongThucChay'
		SET @OrderByString = 'SoLuongThucChay'
	ELSE IF @ColumnSort = 'ThanhTienThucChay'
		SET @OrderByString = 'ThanhTienThucChay'
	ELSE IF @ColumnSort = 'SoLuongThucChayKM'
		SET @OrderByString = 'SoLuongThucChayKM'
	
	SET @Sql = '
		SELECT 
			T.SoHopDong,
			dbo.FormatNumber(ISNULL(T2.SoLuongThucChayKM,0)) AS SoLuongThucChayKM,
			dbo.FormatNumber(ISNULL(T2.SoLuongThucChay,0)) AS SoLuongThucChay,
			dbo.FormatNumber(ISNULL(T2.ThanhTienKM,0)) AS ThanhTienKM,
			dbo.FormatNumber(ISNULL(T2.ThanhTienThucChay,0)) AS ThanhTienThucChay,
			' + @DauNhay + @DauNhay + ' AS TenFile
		FROM 	
		(	
			SELECT 
				T1.SoHopDong,
				ROW_NUMBER() OVER(ORDER BY T1.SoHopDong) num
			FROM
			(
				SELECT DISTINCT SoHopDong
				FROM ThucChayDaTinh
				WHERE 1 =1 
					AND DmSanPhamREF = 238 ' + @FillterString + ' 
			)T1			
		)T 
		INNER JOIN 
			(
			SELECT 
				tcdt.SoHopDong, tcdt.HopDongID, 
				SUM(tcdt.SoLuongThucChayKM) SoLuongThucChayKM,
				SUM(tcdt.SoLuongThucChay) SoLuongThucChay,
				SUM(tcdt.ThanhTienKM) ThanhTienKM, 
				SUM(tcdt.ThanhTienSauTrietKhauThucChay) ThanhTienThucChay 
			FROM ThucChayDaTinh tcdt
			WHERE 1 =1 
				AND tcdt.DmSanPhamREF = 238 ' + @FillterString +' 
			GROUP BY tcdt.SoHopDong,tcdt.HopDongID
			)T2 ON T2.SoHopDong = T.SoHopDong 
		WHERE T.num BETWEEN ' + CONVERT(NVARCHAR(50),((@PageIndex-1)*@RecordCount + 1)) + ' AND ' + CONVERT(NVARCHAR(50),(@PageIndex*@RecordCount)) + '
		ORDER BY ' + @ColumnSort + ' ' + @OrderBy 	
	
	
	PRINT @Sql
	EXEC (@Sql)
END

```
