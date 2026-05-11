# Stored Procedure: `BaoCaoThucChay_DoiTac_Banner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:09.457000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.450000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ColumnSort` | `nvarchar(100)` | No |
| `@OrderBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_Banner]
	-- Add the parameters for the stored procedure here
	@PageIndex int,
	@RecordCount int,
	@StartDate datetime,
	@EndDate datetime,
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
    DECLARE @DmSanPhamREFList nvarchar(50)=''
    
    SET @DauNhay = ''''
		
	SET @FillterString = dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	
	IF @ColumnSort = 'SoHopDong'
		SET @OrderByString = 'SoHopDong'
	ELSE IF @ColumnSort = 'GiaTriPhanBo'
		SET @OrderByString = 'ThanhTien'
	ELSE IF @ColumnSort = 'SoLuongThucChay'
		SET @OrderByString = 'SUM(SoLuongThucChay)'
	ELSE IF @ColumnSort = 'ThanhTienThucChay'
		SET @OrderByString = 'ThanhTienSauTrietKhauThucChay'
	ELSE IF @ColumnSort = 'SoLuongKhuyenMai'
		SET @OrderByString = 'SUM(SoLuongThucChayKM/1000)'
	ELSE IF @ColumnSort = 'ThanhTienKhuyenMai'
		SET @OrderByString = 'SUM(ThanhTienKM)'
	ELSE IF @ColumnSort = 'TenBanner'
		SET @OrderByString = 'TenBanner'
	ELSE IF @ColumnSort = 'NgayBatDau'
		SET @OrderByString = 'NgayBatDau'
	ELSE IF @ColumnSort = 'NgayKetThuc'
		SET @OrderByString = 'NgayKetThuc'
		
    SET @Sql = '
    SELECT TOP ' + CONVERT(NVARCHAR,@RecordCount) + '
		T.SoHopDong, T.HopDongChiTietREF,
		dbo.FormatNumber(T.GiaTriPhanBo) AS GiaTriPhanBo,
		dbo.FormatNumber(T.SoLuongThucChay) AS SoLuongThucChay,
		dbo.FormatNumber(T.SoLuongThucChayKM) AS SoLuongThucChayKM,
		dbo.FormatNumber(T.ThanhTienThucChay) AS ThanhTienThucChay,
		T.DmBannerID,
		T.MoTa,
		dbo.FormatDate(T.NgayBatDau) AS NgayBatDau,
		dbo.FormatDate(T.NgayKetThuc) AS NgayKetThuc,
		T.TenFile,
		T.num AS STT
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
			ISNULL(dmb.TenFile, ' + @DauNhay + '' + @DauNhay + ') TenFile,
			   ROW_NUMBER() OVER (ORDER BY ' + @OrderByString + ' ' + @OrderBy + ') AS num
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
	WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount)
		
	PRINT @Sql;
	EXEC (@Sql);
END

```
