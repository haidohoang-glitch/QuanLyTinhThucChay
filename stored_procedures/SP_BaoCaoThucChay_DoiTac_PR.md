# Stored Procedure: `BaoCaoThucChay_DoiTac_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:09.880000
- **Ngày sửa cuối**: 2014-11-19 12:17:55.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ColumnSort` | `nvarchar(100)` | No |
| `@OrderBy` | `nvarchar(100)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_PR] 
	-- Add the parameters for the stored procedure here
	@PageIndex int,
	@RecordCount int,
	@StartDate datetime,
	@EndDate datetime,
	@DmWebsiteREFList nvarchar(2000),
	@DmSanPhamREFList nvarchar(2000),
	@SoHopDongList nvarchar(2000),
	@TenDangNhap nvarchar(50),
	@ColumnSort nvarchar(50),
	@OrderBy nvarchar(50),
	@IsNoiBo INT,
	@DmHinhThucQuangCaoList NVARCHAR(50)
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
    
    DECLARE @TempTable TABLE (
		SoHopDong NVARCHAR(50),
		HopDongChiTietREF INT,
		SoLuongBaiHD INT,
		SoLuongThucChayKM INT,
		SoLuongThucChay INT,
		ThanhTienThucChay FLOAT,
		Link NVARCHAR(2000),
		Num INT
	)	
	
	SET @FillterString = ' AND IsPheDuyet = 1 AND DmSanPhamREF = 141 '
	
	IF @DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1'
		SET @FillterString += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')';
		 
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	
	SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'
	
	--IF @IsNoiBo = 1
	--	SET @FillterString =  @FillterString + ' AND UPPER(SoHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay
	--ELSE IF @IsNoiBo = 0
	--	SET @FillterString = @FillterString + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
		
	IF @ColumnSort = 'SoHopDong'
		SET @OrderByString = 'A.SoHopDong'
	ELSE IF @ColumnSort = 'SoLuongBaiHD'
		SET @OrderByString = 'A.SoLuongBaiHD'
	ELSE IF @ColumnSort = 'SoLuongThucChay'
		SET @OrderByString = 'A.SoLuongThucChay'
	ELSE IF @ColumnSort = 'SoLuongThucChayKM'
		SET @OrderByString = 'A.SoLuongThucChayKM'
	ELSE IF @ColumnSort = 'ThanhTienThucChay'
		SET @OrderByString = 'A.ThanhTienSauTrietKhauThucChay'
	ELSE IF @ColumnSort = 'Link'
		SET @OrderByString = 'B.LISTOFPARTS'
		
    SET @Sql = '
		SELECT 
			A.SoHopDong, A.HopDongChiTietREF,
			A.SoLuongBaiHD,
			A.SoLuongThucChayKM,
			A.SoLuongThucChay,			
			A.ThanhTienSauTrietKhauThucChay AS ThanhTienThucChay,
			A.Link,
			ROW_NUMBER() OVER (ORDER BY ' + @OrderByString + ' ' + @OrderBy + ') num 
		FROM 
			(
			SELECT tcdt.SoHopDong,
					tcdt.HopDongChiTietREF,
					max(tcdt.SoLuong) SoLuongBaiHD,
					SUM(tcdt.SoLuongThucChayKM)SoLuongThucChayKM,
					sum(tcdt.SoLuongThucChay) SoLuongThucChay,
					sum(dbo.ThucChay_GetThanhTienThucChayKenh(SoHopDong,tcdt.ThanhTienSauTrietKhauThucChay,'+@DauNhay + @TenDangNhap + @DauNhay +')) ThanhTienSauTrietKhauThucChay,
					dbo.ThucChay_GetLinkPR(tcdt.HopDongChiTietREF ,' + @DauNhay + 
											CONVERT(NVARCHAR(50),@StartDate) + 
											@DauNhay + ',' + @DauNhay + 
											CONVERT(NVARCHAR(50),@EndDate) + @DauNhay + '
											) AS Link 
			FROM ThucChayDaTinh tcdt
			WHERE 1 =1 '
	SET @Sql += @FillterString
	SET @Sql += '
			GROUP BY tcdt.SoHopDong, tcdt.HopDongChiTietREF
			)A 
	'
	PRINT @Sql;
	
	INSERT INTO @TempTable
	EXEC (@Sql)
	
	SELECT
		T2.SoHopDong, 
		dbo.FormatNumber(T2.SoLuongBaiHD) AS SoLuongBaiHD,
		dbo.FormatNumber(T2.SoLuongThucChayKM) AS SoLuongThucChayKM,
		dbo.FormatNumber(T2.SoLuongThucChay) AS SoLuongBaiThucChay,
		dbo.FormatNumber(T2.ThanhTienThucChay) AS ThanhTienThucChay,
		T2.Link,
		T2.HopDongChiTietREF
		FROM
		(
			SELECT 
				T.SoHopDong
			FROM
			(
				SELECT 
					A.SoHopDong,
					ROW_NUMBER() OVER(ORDER BY A.SoHopDong) num
				FROM
				(
					SELECT DISTINCT
						SoHopDong
					FROM @TempTable 
				)A 
			)T
			WHERE 
				T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
		)T1 INNER JOIN @TempTable T2 ON T1.SoHopDong = T2.SoHopDong
	ORDER BY T2.SoHopDong
		
	
END

```
