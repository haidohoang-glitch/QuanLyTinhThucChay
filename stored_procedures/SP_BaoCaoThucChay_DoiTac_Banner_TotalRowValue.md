# Stored Procedure: `BaoCaoThucChay_DoiTac_Banner_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:09.667000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.400000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_Banner_TotalRowValue] 
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime,
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
    DECLARE @DmSanPhamREFList nvarchar(50)=''
    
    SET @DauNhay = ''''
		
	SET @FillterString = dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
		
    SET @Sql = '
    SELECT 
		COUNT(T.SoHopDong) AS TotalRow,
		dbo.FormatNumber(SUM(T.GiaTriPhanBo)) AS TongGiaTriPhanBo,
		dbo.FormatNumber(SUM(T.SoLuongThucChay)) AS TongSoLuongThucChay,
		dbo.FormatNumber(SUM(T.ThanhTienThucChay)) AS TongThanhTienThucChay		
    FROM
    (
		SELECT DISTINCT 
			tcdt.SoHopDong,
			TCDT.HopDongChiTietREF,
			tcdt.ThanhTien AS GiaTriPhanBo,
			tcdt.SoLuongThucChay,
			tcdt.SoLuongThucChayKM,
			tcdt.ThanhTienSauTrietKhauThucChay AS ThanhTienThucChay
			, ISNULL(tchdctab.DmBannerID, ' + @DauNhay + '' + @DauNhay + ') DmBannerID
			, ISNULL(dmb.MoTa, ' + @DauNhay + '' + @DauNhay + ') MoTa,
			ISNULL(dmb.NgayBatDau, ' + @DauNhay + '' + @DauNhay + ') NgayBatDau,
			ISNULL(dmb.NgayKetThuc, ' + @DauNhay + '' + @DauNhay + ') NgayKetThuc,
			ISNULL(dmb.TenFile, ' + @DauNhay + '' + @DauNhay + ') TenFile
		FROM   
		(
		 SELECT DISTINCT
			tcdt.SoHopDong,
			tcdt.HopDongChiTietREF,
			max(tcdt.ThanhTien) ThanhTien,
			sum(tcdt.SoLuongThucChay) SoLuongThucChay,
			SUM(tcdt.SoLuongThucChayKM)SoLuongThucChayKM,
			sum(tcdt.ThanhTienSauTrietKhauThucChay) ThanhTienSauTrietKhauThucChay
		 FROM ThucChayDaTinh tcdt
		 WHERE tcdt.DmSanPhamREF = 140 --Banner 
		 '
	
	SET @Sql += @FillterString
	
	SET @Sql += '		
		 GROUP BY tcdt.SoHopDong, tcdt.HopDongChiTietREF
		) tcdt
	    LEFT JOIN ThucChayHopDongChiTietAndBanner tchdctab
			ON  tcdt.HopDongChiTietREF = tchdctab.HopDongChiTietREF
	    LEFT JOIN DmBanners dmb
			ON  CONVERT(NVARCHAR(20), dmb.DmBannerID) = tchdctab.DmBannerID
		WHERE dmb.NgayBatDau IS NOT NULL
	)T
	'
		
	PRINT @Sql;
	EXEC (@Sql);
END

```
