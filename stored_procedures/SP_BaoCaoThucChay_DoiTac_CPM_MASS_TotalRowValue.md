# Stored Procedure: `BaoCaoThucChay_DoiTac_CPM_MASS_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:11.700000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.563000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-24
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_CPM_MASS_TotalRowValue]
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(2000),
	@DmWebsiteREFList nvarchar(2000),
	@SoHopDongList nvarchar(2000),
	@TenDangNhap nvarchar(50)
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
	
	SET @Sql = '
		SELECT
			COUNT(T.SoHopDong) AS TotalRow, 			
			dbo.FormatNumber(ISNULL(SUM(T2.SoLuongThucChayKM),0)) AS TongSoLuongThucChayKM,
			dbo.FormatNumber(ISNULL(SUM(T2.SoLuongThucChay),0)) AS TongSoLuongThucChay,
			dbo.FormatNumber(ISNULL(SUM(T2.ThanhTienKM),0)) AS TongThanhTienKM,
			dbo.FormatNumber(ISNULL(SUM(T2.ThanhTienThucChay),0)) AS TongThanhTienThucChay
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
		'	
	
	
	PRINT @Sql
	EXEC (@Sql)
END

```
