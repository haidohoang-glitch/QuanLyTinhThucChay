# Stored Procedure: `BaoCaoThucChay_DoiTac_CPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:10.293000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.590000

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
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_CPD]
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
	@OrderBy nvarchar(50),
	@IsNoiBo INT,
	@DmHinhThucQuangCaoList NVARCHAR(200)
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
	
	SET @FillterString = ' '
	
	IF @DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1'
		SET @FillterString += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')';
	
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	
	SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'
	--IF @IsNoiBo = 1
	--	SET @FillterString =  @FillterString + ' AND UPPER(TenMaHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay
	--ELSE IF @IsNoiBo = 0
	--	SET @FillterString = @FillterString + ' AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
	
	IF @ColumnSort = 'SoHopDong'
		SET @OrderByString = 'SoHopDong'
	ELSE IF @ColumnSort = 'GiaTriPhanBo'
		SET @OrderByString = 'T2.GiaTriPhanBo'
	ELSE IF @ColumnSort = 'SoLuongThucChay'
		SET @OrderByString = 'T2.SoLuongThucChay'
	ELSE IF @ColumnSort = 'SoLuongThucChayKM'
		SET @OrderByString = 'T2.SoLuongThucChayKM'
	ELSE IF @ColumnSort = 'ThanhTienThucChay'
		SET @OrderByString = 'T2.ThanhTienThucChay'
	ELSE IF @ColumnSort = 'MoTa'
		SET @OrderByString = 'T2.MoTa'
	ELSE IF @ColumnSort = 'NgayBatDau'
		SET @OrderByString = 'T2.NgayBatDau'
	ELSE IF @ColumnSort = 'NgayKetThuc'
		SET @OrderByString = 'T2.NgayKetThuc'
		
	DECLARE @TempTable TABLE (
		SoHopDong NVARCHAR(50),
		HopDongChiTietREF INT,
		GiaTriPhanBo FLOAT,
		SoLuongThucChayKM INT,
		SoLuongThucChay INT,
		ThanhTienThucChay FLOAT,
		DmBannerID NVARCHAR(50),
		MoTa NVARCHAR(MAX),
		NgayBatDau DATETIME,
		NgayKetThuc DATETIME,
		TenFile NVARCHAR(MAX),
		Width INT,
		Height INT,
		CreatedAt DATETIME
		--,
		--Num INT
	)	
		
    SET @Sql = '
		SELECT DISTINCT 
					tcdt.SoHopDong,
					TCDT.HopDongChiTietREF,
					tcdt.ThanhTien AS GiaTriPhanBo,
					tcdt.SoLuongThucChayKM,
					tcdt.SoLuongThucChay,					
					tcdt.ThanhTienThucChayThucThu AS ThanhTienThucChay,
					ISNULL(dmb.DmBannerID, ' + @DauNhay + '' + @DauNhay + ') DmBannerID,
					ISNULL(dmb.MoTa, ' + @DauNhay + '' + @DauNhay + ') MoTa,
					ISNULL(dmb.NgayBatDau, ' + @DauNhay + '' + @DauNhay + ') NgayBatDau,
					ISNULL(dmb.NgayKetThuc, ' + @DauNhay + '' + @DauNhay + ') NgayKetThuc,
					ISNULL(dmb.TenFile, ' + @DauNhay + '' + @DauNhay + ') TenFile,
					dmb.Width,
					dmb.Height,
					dmb.CreatedAt
					--,
					--ROW_NUMBER() OVER (ORDER BY tcdt.SoHopDong) num 
				FROM   
				(
				 SELECT DISTINCT
					tcdt.SoHopDong,
					tcdt.HopDongChiTietREF,
					max(tcdt.ThanhTien) ThanhTien,
					sum(tcdt.SoLuongThucChayNoiBo + SoLuongThucChayThucThu) SoLuongThucChay,
					SUM(tcdt.SoLuongThucChayKhuyenMai)SoLuongThucChayKM,
					sum(dbo.ThucChay_GetThanhTienThucChayKenh(SoHopDong,(tcdt.ThanhTienThucChayThucThu + tcdt.GiaTriThayDoi),'+@DauNhay + @TenDangNhap + @DauNhay +')) ThanhTienThucChayThucThu
				 FROM GetDataThucChayPartnerByParams(' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ', ' + @DauNhay +  CONVERT(NVARCHAR(50),@EndDate)  + @DauNhay + ') tcdt
				 WHERE 1=1  
				 ' + @FillterString + ' 		
				 GROUP BY tcdt.SoHopDong, tcdt.HopDongChiTietREF
				) tcdt
				LEFT JOIN 
				(
					SELECT tchdctab.HopDongChiTietREF, db.DmBannerID, db.MoTa, db.NgayBatDau, db.NgayKetThuc, db.TenFile, db.Width, db.Height, db.CreatedAt
						
					FROM 	ThucChayHopDongChiTietAndBanner tchdctab
						INNER JOIN DmBanner db ON CONVERT(NVARCHAR(20), db.DmBannerID) = tchdctab.DmBannerID
					WHERE 1 = 1
						AND 
						(
							' + @DauNhay + CONVERT(NVARCHAR(50), @StartDate) + @DauNhay + ' BETWEEN db.NgayBatDau AND db.NgayKetThuc 
							OR ' + @DauNhay + CONVERT(NVARCHAR(50), @EndDate) + @DauNhay + ' BETWEEN db.NgayBatDau AND db.NgayKetThuc 
							OR ' + @DauNhay + CONVERT(NVARCHAR(50), @StartDate) + @DauNhay + ' > db.NgayBatDau AND ' + @DauNhay + CONVERT(NVARCHAR(50), @EndDate) + @DauNhay + ' < db.NgayKetThuc 
							OR ' + @DauNhay + CONVERT(NVARCHAR(50), @StartDate) + @DauNhay + ' < db.NgayBatDau AND ' + @DauNhay + CONVERT(NVARCHAR(50), @EndDate) + @DauNhay + ' > db.NgayKetThuc   
						)
				) dmb ON dmb.HopDongChiTietREF = tcdt.HopDongChiTietREF 
		WHERE ROUND(tcdt.ThanhTienThucChayThucThu,0) <> 0'
		
	PRINT @Sql;
	
	INSERT INTO @TempTable
	EXEC (@Sql)
	
		SELECT
			CASE T2.SoHopDong
				WHEN '-' THEN N'MuaOnline'
				ELSE T2.SoHopDong
			END SoHopDong, 
			dbo.FormatNumber(T2.GiaTriPhanBo) AS GiaTriPhanBo,
			dbo.FormatNumber(T2.SoLuongThucChay) AS SoLuongThucChay,
			dbo.FormatNumber(T2.SoLuongThucChayKM) AS SoLuongThucChayKM,
			dbo.FormatNumber(T2.ThanhTienThucChay) AS ThanhTienThucChay,
			T2.DmBannerID,
			T2.MoTa,
			dbo.FormatDate(T2.NgayBatDau) AS NgayBatDau,
			dbo.FormatDate(T2.NgayKetThuc) AS NgayKetThuc,
			T2.TenFile,
			T2.Width,
			T2.Height,
			T2.CreatedAt,
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
