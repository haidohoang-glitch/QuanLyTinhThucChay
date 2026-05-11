# Stored Procedure: `prc_QLTC_GetListDataDelete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.697000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.697000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `nvarchar(206)` | No |
| `@ToDate` | `nvarchar(206)` | No |
| `@Contract` | `nvarchar(4000)` | No |
| `@Banner` | `nvarchar(4000)` | No |
| `@Product` | `int(4)` | No |
| `@Table` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
---- =============================================
--Exec [dbo].[prc_QLTC_GetListDataDelete] @FromDate = '2021-07-08', --Datetime = NULL,
--										@ToDate = '2021-07-08',--Datetime = NULL,
--										@Contract = 'QC0110421',--Nvarchar(500) = '',
--										@Banner = '572662',--Nvarchar(500) = '',
--										@Product = 0,--Int = 0,
--										@Table = 'DataThucChay'--Nvarchar(500) = ''

CREATE PROCEDURE [dbo].[prc_QLTC_GetListDataDelete]
	@FromDate Nvarchar(103) = NULL,
	@ToDate Nvarchar(103) = NULL,
	@Contract Nvarchar(2000) = '',
	@Banner Nvarchar(2000) = '',
	@Product Int = null ,
	@Table Nvarchar(2000) = ''
AS
BEGIN
	SET NOCOUNT ON;
	Set @Contract = IsNull(@Contract ,'');
	Set @Banner = IsNull(@Banner ,'');
	Set @Product = IsNull(@Product ,0);

	Declare @querySql Nvarchar(Max) = '';
	If(@Table = N'DataThucChay_test' Or @Table = N'DataThucChay') --Branding
		Begin
			Set @querySql = 'Select SoHopDong From [dbo].[ThucChay] Where SoHopDong <> N''TONGSANPHAM'' AND CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
			 And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + ''')))
			 And (''' + @Banner + ''' = '''' Or DmBannerREF In (Select Name From STRING_SPLIT_QLTC(''' + @Banner + ''')))
			 And (' + Convert(nvarchar,@Product) + ' = 0 Or DmSanPhamREF = ' + Convert(nvarchar,@Product) + ')';
		End
	Else If(@Table = N'DataThucchay_Native_Ads_test' Or @Table = N'DataThucchay_Native_Ads') --Native Ads
		Begin
			Set @querySql = 'Select SoHopDong From [dbo].[ThucChay_Native_Ads] Where SoHopDong <> N''TONGSANPHAM'' AND CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
			 And (''' + @Contract + ''' = '''' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + ''')))
			 And (''' + @Banner + ''' = '''' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(''' + @Banner + ''')))
			 And (' + Convert(nvarchar,@Product) + ' = 0 Or DmSanPhamREF = ' + Convert(nvarchar,@Product) + ')';
		End
	Else If(@Table = N'DataThucchay_OnImageAds_test' Or @Table = N'DataThucchay_OnImageAds')--OnImage Ads
		Begin
			Set @querySql = 'Select SoHopDong From [dbo].[ThucChay_Native_Ads] Where SoHopDong <> N''TONGSANPHAM'' AND CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
			 And (''' + @Contract + ''' = '''' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + ''')))
			 And (''' + @Banner + ''' = '''' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(''' + @Banner + ''')))
			 And (' + Convert(nvarchar,@Product) + ' = 0 Or DmSanPhamREF = ' + Convert(nvarchar,@Product) + ')';
		End
	Else If(@Table = N'DataThucChay_Admatic_v2_test' Or @Table = N'DataThucChay_Admatic_v2')--Admatic
		Begin
			Set @querySql = 'Select SoHopDong From [dbo].[ThucChay_ThanhTien_Admatic] Where SoHopDong <> N''TONGSANPHAM'' AND CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
			 And (''' + @Contract + ''' = '''' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + ''')))
			 And (''' + @Banner + ''' = '''' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(''' + @Banner + ''')))
			 And (' + Convert(nvarchar,@Product) + ' = 0 Or DmSanPhamREF = ' + Convert(nvarchar,@Product) + ')';
		End

	Print @querySql;

	EXECUTE sp_executesql @querySql, N'@FromDate Nvarchar(103), @ToDate Nvarchar(103), @Contract Nvarchar(500), @Banner Nvarchar(500), @Product Int',
	@FromDate = @FromDate,
	@ToDate = @ToDate,
	@Contract = @Contract,
	@Banner = @Banner,
	@Product = @Product
END

```
