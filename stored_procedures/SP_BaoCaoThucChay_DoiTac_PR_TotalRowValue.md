# Stored Procedure: `BaoCaoThucChay_DoiTac_PR_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:10.090000
- **Ngày sửa cuối**: 2014-11-19 12:17:55.243000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_PR_TotalRowValue] 
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime,
	@DmWebsiteREFList nvarchar(2000),
	@DmSanPhamREFList nvarchar(2000),
	@SoHopDongList nvarchar(2000),
	@TenDangNhap nvarchar(50),
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
	
	SET @FillterString = ' AND IsPheDuyet = 1 AND DmSanPhamREF = 141 '	
	
	IF @DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1'
		SET @FillterString += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')';
		
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	
	SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'
	
	--IF @IsNoiBo = 1
	--	SET @FillterString =  @FillterString + ' AND UPPER(SoHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay
	--ELSE IF @IsNoiBo = 0
	--	SET @FillterString = @FillterString + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
			
    SET @Sql = '
    SELECT 
		COUNT(DISTINCT T.SoHopDong) AS TotalRow,
		dbo.FormatNumber(SUM(T.SoLuongBaiHD)) AS TongSoLuongBaiHD,
		dbo.FormatNumber(SUM(T.SoLuongThucChayKM)) AS TongSoLuongThucChayKM,
		dbo.FormatNumber(SUM(T.SoLuongThucChay)) AS TongSoLuongThucChay,		
		dbo.FormatNumber(SUM(T.ThanhTienThucChay)) AS TongThanhTienThucChay
	FROM
	(
		SELECT 
			A.SoHopDong, A.HopDongChiTietREF,
			A.SoLuongBaiHD,
			A.SoLuongThucChay,
			A.SoLuongThucChayKM,
			A.ThanhTienSauTrietKhauThucChay AS ThanhTienThucChay,
			A.Link,
			ROW_NUMBER() OVER (ORDER BY A.SoHopDong) num 
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
			WHERE 1=1 ' 
	SET @Sql += @FillterString
	SET @Sql += '
			GROUP BY tcdt.SoHopDong, tcdt.HopDongChiTietREF
			)A 	
	)T
    
	'
		
	PRINT @Sql;
	EXEC (@Sql);
END

```
