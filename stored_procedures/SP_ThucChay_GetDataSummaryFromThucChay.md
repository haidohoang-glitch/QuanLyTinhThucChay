# Stored Procedure: `ThucChay_GetDataSummaryFromThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-27 23:18:11.020000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.593000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmBookingREF` | `nvarchar(8000)` | No |
| `@DmBannerREF` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-05
-- Description:	Lay thong tin du lieu thuc chay tra ve group theo San pham
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetDataSummaryFromThucChay]
	@PageIndex Int,
	@RecordCount Int,
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmBookingREF nvarchar(4000),
	@DmBannerREF nvarchar(4000)
AS
BEGIN
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	
	SET @DauNhay = ''''
	
	SET @Sql = '
	SELECT TOP (10)
		T.SoHopDong
		,T.DmSanPhamREF
		,T.TenSanPham
		,T.TenWebsite
		,T.DanhSachDmBookingREF
		,T.DmBannerREF
		,T.NgayThucHien
		,T.TongViewThucChay
		,T.TongClickThucChay
	FROM
	(' +
		dbo.ThucChay_GenSQLCommandDataSummaryFromThucChay(@StartDate,
														  @EndDate,
														  @DmSanPhamREFList,
														  @DmWebsiteREFList,
														  @SoHopDongList,
														  @DmBookingREF,
														  @DmBannerREF)
		+
	') AS T
	WHERE num >0 '
	
	PRINT @SoHopDongList;
	
	PRINT @Sql
	exec (@Sql)
END

```
