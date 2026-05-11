# Stored Procedure: `BaoCaoThucChay_DoiTac_CPD_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:10.687000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.580000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@IsNoiBo` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_CPD_TotalRowValue] 
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(2000),
	@DmWebsiteREFList nvarchar(2000),
	@SoHopDongList nvarchar(2000),
	@TenDangNhap nvarchar(50),
	@IsNoiBo INT
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
	
	SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'
	
	--IF @IsNoiBo = 1
	--	SET @FillterString =  @FillterString + ' AND UPPER(SoHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay
	--ELSE IF @IsNoiBo = 0
	--	SET @FillterString = @FillterString + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
				
    SET @Sql = '
		SELECT
			COUNT(DISTINCT T1.SoHopDong) AS TotalRow,
			dbo.FormatNumber(SUM(T1.GiaTriPhanBo)) AS TongGiaTriPhanBo,
			dbo.FormatNumber(SUM(T1.SoLuongThucChay)) AS TongSoLuongThucChay,
			dbo.FormatNumber(SUM(T1.SoLuongThucChayKM)) AS TongSoLuongThucChayKM,
			dbo.FormatNumber(SUM(T1.ThanhTienThucChay)) AS TongThanhTienThucChay
		FROM
		(
			SELECT 
				T.SoHopDong, T.HopDongChiTietREF,
				SUM(DISTINCT T.GiaTriPhanBo) AS GiaTriPhanBo,
				SUM(T.SoLuongThucChay) AS SoLuongThucChay,
				SUM(T.SoLuongThucChayKM) AS SoLuongThucChayKM,
				SUM(T.ThanhTienThucChay) AS ThanhTienThucChay		
			FROM
			(
				SELECT DISTINCT 
							tcdt.SoHopDong,
							TCDT.HopDongChiTietREF,
							tcdt.ThanhTien AS GiaTriPhanBo,
							tcdt.SoLuongThucChay,
							tcdt.SoLuongThucChayKM,
							tcdt.ThanhTienSauTrietKhauThucChay AS ThanhTienThucChay
							--,
							--ISNULL(tchdctab.DmBannerID, ' + @DauNhay + '' + @DauNhay + ') DmBannerID,
							--ISNULL(dmb.MoTa, ' + @DauNhay + '' + @DauNhay + ') MoTa,
							--ISNULL(dmb.NgayBatDau, ' + @DauNhay + '' + @DauNhay + ') NgayBatDau,
							--ISNULL(dmb.NgayKetThuc, ' + @DauNhay + '' + @DauNhay + ') NgayKetThuc,
							--ISNULL(dmb.TenFile, ' + @DauNhay + '' + @DauNhay + ') TenFile,
							--dmb.Width,
							--dmb.Height
						FROM   
						(
						 SELECT DISTINCT
							tcdt.SoHopDong,
							tcdt.HopDongChiTietREF,
							max(tcdt.ThanhTien) ThanhTien,
							sum(tcdt.SoLuongThucChay) SoLuongThucChay,
							SUM(tcdt.SoLuongThucChayKM)SoLuongThucChayKM,
							sum(dbo.ThucChay_GetThanhTienThucChayKenh(SoHopDong,tcdt.ThanhTienSauTrietKhauThucChay,'+@DauNhay + @TenDangNhap + @DauNhay +')) ThanhTienSauTrietKhauThucChay
						 FROM ThucChayDaTinh tcdt
						 WHERE 1=1 
						 ' + @FillterString + ' 		
						 GROUP BY tcdt.SoHopDong, tcdt.HopDongChiTietREF
						) tcdt
						--LEFT JOIN ThucChayHopDongChiTietAndBanner tchdctab
						--	ON  tcdt.HopDongChiTietREF = tchdctab.HopDongChiTietREF
						--LEFT JOIN DmBanners dmb
						--	ON  CONVERT(NVARCHAR(20), dmb.DmBannerID) = tchdctab.DmBannerID 
						--WHERE dmb.NgayBatDau IS NOT NULL
			)T 
			GROUP BY T.SoHopDong, T.HopDongChiTietREF
		)T1
		'
		
	PRINT @Sql;
	EXEC (@Sql);
END

```
