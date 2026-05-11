# Stored Procedure: `prc_QLTC_GetListDataThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.710000
- **Ngày sửa cuối**: 2024-01-11 17:15:34.893000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `nvarchar(206)` | No |
| `@ToDate` | `nvarchar(206)` | No |
| `@Contract` | `nvarchar(4000)` | No |
| `@Table` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
---- =============================================
/*
Exec [dbo].[prc_QLTC_GetListDataThucChay] @FromDate = '2023-07-01', --Datetime = NULL,
										@ToDate = '2023-08-29',--Datetime = NULL,
										@Contract = 'qc4550723',--Nvarchar(500) = '',
    									@Table = 'DataThucChay_Admatic_v2_test'--Nvarchar(500) = ''
*/

CREATE PROCEDURE [dbo].[prc_QLTC_GetListDataThucChay]
	@FromDate Nvarchar(103) = NULL,
	@ToDate Nvarchar(103) = NULL,
	@Contract Nvarchar(2000) = '',
	@Table Nvarchar(2000) = ''
AS
BEGIN
	SET NOCOUNT ON;
	Set @Contract = IsNull(@Contract ,'');

	Declare @querySql Nvarchar(Max) = '';
	If(@Table = N'DataThucChay_test' Or @Table = N'DataThucChay') --Branding
		Begin
			Set @querySql = 'SELECT dataTest.soHopDong, dataTest.DmBannerREF, dataTest.tenSanPham, 
								dbo.FormatNumber(dataTest.tongViewThucChay) tongViewThucChay_Moi, dbo.FormatNumber(dataTC.tongViewThucChay) tongViewThucChay_Cu,
								dbo.FormatNumber(dataTest.tongClickThucChay) tongClickThucChay_Moi, dbo.FormatNumber(dataTC.tongClickThucChay) tongClickThucChay_Cu,
								dbo.FormatNumber(dataTest.tongViewThucChay - dataTC.tongViewThucChay) As tongViewThucChay_Chech_Lech,
								dbo.FormatNumber(dataTest.tongClickThucChay - dataTC.tongClickThucChay) As tongClickThucChay_Chech_Lech,
								dataTest.tuNgay, dataTest.denNgay FROM 
									(SELECT soHopDong,DmBannerREF,tenSanPham,
										Sum(IsNull(Cast(tongViewThucChay As Float),0)) As tongViewThucChay,
										Sum(IsNull(Cast(tongClickThucChay As Float),0)) As tongClickThucChay,
										Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
										FROM ' + @Table + ' Where SoHopDong <> N''' + 'TONGSANPHAM' + ''' AND CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
										And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + '''))) Group By SoHopDong,DmBannerREF,TenSanPham) dataTest
								LEFT Join
									(SELECT soHopDong,DmBannerREF,tenSanPham,
										Sum(IsNull(Cast(tongViewThucChay As Float),0)) As tongViewThucChay,
										Sum(IsNull(Cast(tongClickThucChay As Float),0)) As tongClickThucChay,
										Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
										FROM [dbo].[ThucChay] Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
										And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + '''))) Group By SoHopDong,DmBannerREF,TenSanPham) dataTC ON dataTest.DmBannerREF = dataTC.DmBannerREF';
		END
	Else If(@Table = N'DataThucchay_Native_Ads_test' Or @Table = N'DataThucchay_Native_Ads') --Native Ads
		Begin
			Set @querySql = 'SELECT dataTest.soHopDong, dataTest.DmBannerID, dataTest.tenSanPham, 
								dbo.FormatNumber(dataTest.tongSoLuongThucChay) tongSoLuongThucChay_Moi, dbo.FormatNumber(dataTC.tongSoLuongThucChay) tongSoLuongThucChay_Cu,
								dbo.FormatNumber(dataTest.tongSoLuongThucChayKM) tongSoLuongThucChayKM_Moi,dbo.FormatNumber(dataTC.tongSoLuongThucChayKM) tongSoLuongThucChayKM_Cu,
								dbo.FormatNumber(dataTest.tongThanhTienThucChay) tongThanhTienThucChay_Moi, dbo.FormatNumber(dataTC.tongThanhTienThucChay) tongThanhTienThucChay_Cu,
								dbo.FormatNumber(dataTest.tongThanhTienThucChayKM) tongThanhTienThucChayKM_Moi, dbo.FormatNumber(dataTC.tongThanhTienThucChayKM) tongThanhTienThucChayKM_Cu,

								dbo.FormatNumber(dataTest.tongSoLuongThucChay - dataTC.tongSoLuongThucChay) As tongSoLuongThucChay_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongThanhTienThucChay - dataTC.tongThanhTienThucChay) As tongThanhTienThucChay_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongSoLuongThucChayKM - dataTC.tongSoLuongThucChayKM) AS tongSoLuongThucChayKM_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongThanhTienThucChayKM - dataTC.tongThanhTienThucChayKM) AS tongThanhTienThucChayKM_Chenh_Lech,
								dataTest.tuNgay, dataTest.denNgay FROM 
									(SELECT soHopDong,DmBannerID,tenSanPham,
										IsNull(Sum(Cast(SoLuongThucChay As Float)),0) As tongSoLuongThucChay,
										Sum(CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/(1+CONVERT(FLOAT,vat)/100)) As tongThanhTienThucChay,
										ISNULL(SUM(CAST(SoLuongThucChayKhuyenMai AS FLOAT)), 0) AS tongSoLuongThucChayKM,
										SUM(CONVERT(FLOAT, ISNULL([ThanhTienThucChaykhuyenMai], 0)) /(1+CONVERT(FLOAT,vat)/100)) AS tongThanhTienThucChayKM,
										Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
										FROM ' + @Table + ' Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
										And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + '''))) Group By SoHopDong,DmBannerID,TenSanPham) dataTest
								LEFT Join
									(SELECT soHopDong,DmBannerID,tenSanPham,
										IsNull(Sum(Cast(SoLuongThucChay As Float)),0) As tongSoLuongThucChay,
										IsNull(Sum(Cast(ThanhTienThucChaySauCK As Float)),0) As tongThanhTienThucChay,
										ISNULL(SUM(CAST(SoLuongThucChayKM AS FLOAT)), 0) AS tongSoLuongThucChayKM,
										ISNULL(SUM(CAST(ThanhTienThucChayKM AS FLOAT)), 0) AS tongThanhTienThucChayKM,
										Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
										FROM [dbo].[ThucChay_Native_Ads] Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
										And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + ''')))
										And DmSanPhamREF = 821 Group By SoHopDong,DmBannerID,TenSanPham) dataTC ON dataTest.DmBannerID = dataTC.DmBannerID';
		End
	Else If(@Table = N'DataThucchay_OnImageAds_test' Or @Table = N'DataThucchay_OnImageAds')--OnImage Ads
		Begin
			Set @querySql = 'SELECT dataTest.soHopDong, dataTest.DmBannerID, dataTest.tenSanPham, 
								dbo.FormatNumber(dataTest.tongSoLuongThucChay) tongSoLuongThucChay_Moi, dbo.FormatNumber(dataTC.tongSoLuongThucChay) tongSoLuongThucChay_Cu,
								dbo.FormatNumber(dataTest.tongSoLuongThucChayKM) tongSoLuongThucChayKM_Moi,dbo.FormatNumber(dataTC.tongSoLuongThucChayKM) tongSoLuongThucChayKM_Cu,
								dbo.FormatNumber(dataTest.tongThanhTienThucChay) tongThanhTienThucChay_Moi, dbo.FormatNumber(dataTC.tongThanhTienThucChay) tongThanhTienThucChay_Cu,
								dbo.FormatNumber(dataTest.tongThanhTienThucChayKM) tongThanhTienThucChayKM_Moi, dbo.FormatNumber(dataTC.tongThanhTienThucChayKM) tongThanhTienThucChayKM_Cu,
								dbo.FormatNumber(dataTest.tongSoLuongThucChay - dataTC.tongSoLuongThucChay) As tongSoLuongThucChay_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongThanhTienThucChay - dataTC.tongThanhTienThucChay) As tongThanhTienThucChay_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongSoLuongThucChayKM - dataTC.tongSoLuongThucChayKM) AS tongSoLuongThucChayKM_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongThanhTienThucChayKM - dataTC.tongThanhTienThucChayKM) AS tongThanhTienThucChayKM_Chenh_Lech,
								dataTest.tuNgay, dataTest.denNgay FROM 
									(SELECT soHopDong,DmBannerID,tenSanPham,
										IsNull(Sum(Cast(SoLuongThucChay As Float)),0) As tongSoLuongThucChay,
										Sum(CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/(1+CONVERT(FLOAT,vat)/100)) As tongThanhTienThucChay,
										 ISNULL(SUM(CAST(SoLuongThucChayKhuyenMai AS FLOAT)), 0) AS tongSoLuongThucChayKM,
										SUM(CONVERT(FLOAT, ISNULL([ThanhTienThucChaykhuyenMai], 0)) /(1+CONVERT(FLOAT,vat)/100)) AS tongThanhTienThucChayKM,
										Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
										FROM ' + @Table + ' Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
										And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + '''))) Group By SoHopDong,DmBannerID,TenSanPham) dataTest
								LEFT Join
									(SELECT soHopDong,DmBannerID,tenSanPham,
										IsNull(Sum(Cast(SoLuongThucChay As Float)),0) As tongSoLuongThucChay,
										IsNull(Sum(Cast(ThanhTienThucChaySauCK As Float)),0) As tongThanhTienThucChay,
										ISNULL(SUM(CAST(SoLuongThucChayKM AS FLOAT)), 0) AS tongSoLuongThucChayKM,
										ISNULL(SUM(CAST(ThanhTienThucChayKM AS FLOAT)), 0) AS tongThanhTienThucChayKM,
										Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
										FROM [dbo].[ThucChay_Native_Ads] Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
										And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + ''')))
										And DmSanPhamREF = 5133 Group By SoHopDong,DmBannerID,TenSanPham) dataTC ON dataTest.DmBannerID = dataTC.DmBannerID';
		End
	Else If(@Table = N'DataThucChay_Admatic_v2_test' Or @Table = N'DataThucChay_Admatic_v2')--Admatic
		--Begin
		--	Set @querySql = 'SELECT dataTest.contract_number SoHopDong, dataTest.banner_id DmBannerID, dataTest.tenSanPham, 
		--						dbo.FormatNumber(dataTest.tongSoLuongThucChay) tongSoLuongThucChay_Moi, dbo.FormatNumber(dataTC.tongSoLuongThucChay) tongSoLuongThucChay_Cu,
		--						dbo.FormatNumber(dataTest.tongThanhTienThucChay) tongThanhTienThucChay_Moi, dbo.FormatNumber(dataTC.tongThanhTienThucChay) tongThanhTienThucChay_Cu,
		--						dbo.FormatNumber(dataTest.tongSoLuongThucChayKM) tongSoLuongThucChayKM_Moi, dbo.FormatNumber(dataTC.tongSoLuongThucChayKM) tongSoLuongThucChayKM_Cu,
		--						dbo.FormatNumber(dataTest.tongThanhTienThucChayKM) tongThanhTienThucChayKM_Moi, dbo.FormatNumber(dataTC.tongThanhTienThucChayKM) tongThanhTienThucChayKM_Cu,

		--						dbo.FormatNumber(dataTest.tongSoLuongThucChay - dataTC.tongSoLuongThucChay) As tongSoLuongThucChay_Chenh_Lech,
		--						dbo.FormatNumber(dataTest.tongThanhTienThucChay - dataTC.tongThanhTienThucChay) As tongThanhTienThucChay_Chenh_Lech,
		--						dbo.FormatNumber(dataTest.tongSoLuongThucChayKM - dataTC.tongSoLuongThucChayKM) As tongSoLuongThucChayKM_Chenh_Lech,
		--						dbo.FormatNumber(dataTest.tongThanhTienThucChayKM - dataTC.tongThanhTienThucChayKM) As tongThanhTienThucChayKM_Chenh_Lech,
		--						dataTest.tuNgay, dataTest.denNgay FROM 
		--							(SELECT contract_number,banner_id,tenSanPham,
		--								Sum(CASE WHEN ProductUnitName = N''CPM'' AND ((CONVERT(FLOAT,domain_tt_money)  <> 0 AND CONVERT(FLOAT,domain_tt_promotion) = 0) 
		--																			OR (CONVERT(FLOAT,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))   
		--									THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
		--								WHEN ProductUnitName = N''CPC'' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)  
		--																or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))
		--									THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0)) 
		--								WHEN ProductUnitName = N''TRUEVIEW'' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)   
		--																or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))
		--									THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
		--								WHEN ProductUnitName = N''TRUE VIEW'' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)
		--																or   (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0) )
		--									THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
		--								ELSE 0--CONVERT(BIGINT,ISNULL(domain_tt_view,0)) --tuyetnta cf
		--								END ) As tongSoLuongThucChay,

		--								Sum(CASE WHEN ProductUnitName = N''CPM'' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) 
		--												THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
		--										WHEN ProductUnitName = N''CPC'' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) 
		--												THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0)) 
		--										WHEN ProductUnitName = N''TRUEVIEW'' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) 
		--												THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
		--										WHEN ProductUnitName = N''TRUE VIEW'' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) 
		--												THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
		--										ELSE 0
		--								END ) AS  tongSoLuongThucChayKM,

		--								Sum(CONVERT(FLOAT,ISNULL(domain_tt_money,0))/(1+(Cast(vat as NUMERIC(18,2))/100.00))) As tongThanhTienThucChay,
		--								Sum(CONVERT(FLOAT,ISNULL(domain_tt_promotion,0))/(1+(Cast(vat as NUMERIC(18,2))/100.00))) As tongThanhTienThucChayKM,
		--								Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
		--								FROM ' + @Table + ' Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
		--								And (''' + @Contract + ''' = '''' Or Lower(contract_number) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + '''))) Group By contract_number,banner_id,TenSanPham) dataTest
		--						LEFT Join
		--							(SELECT soHopDong,DmBannerID,tenSanPham,
		--								IsNull(Sum(Cast(SoLuongThucChay As Float)),0) As tongSoLuongThucChay,
		--								IsNull(Sum(Cast(SoLuongThucChayKM As Float)),0) As tongSoLuongThucChayKM,
		--								IsNull(Sum(Cast(ThanhTienThucChaySauCK_ChuaVAT As Float)),0) As tongThanhTienThucChay,
		--								IsNull(Sum(Cast(ThanhTienThucChayKM As Float)),0) As tongThanhTienThucChayKM,
		--								Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
		--								FROM [dbo].[ThucChay_ThanhTien_Admatic] Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
		--								And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + ''')))
		--								Group By SoHopDong,DmBannerID,TenSanPham) dataTC ON dataTest.banner_id = dataTC.DmBannerID';
		--End
		Begin
			DECLARE @queryTest NVARCHAR(MAX) = 'SELECT contract_number,banner_id,tenSanPham,
										Sum(CASE WHEN ProductUnitName = N''CPM'' AND ((CONVERT(FLOAT,domain_tt_money)  <> 0 AND CONVERT(FLOAT,domain_tt_promotion) = 0) 
																					OR (CONVERT(FLOAT,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))   
											THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
										WHEN ProductUnitName = N''CPC'' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)  
																		or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))
											THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0)) 
										WHEN ProductUnitName = N''TRUEVIEW'' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)   
																		or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))
											THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
										WHEN ProductUnitName = N''TRUE VIEW'' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)
																		or   (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0) )
											THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
										ELSE 0--CONVERT(BIGINT,ISNULL(domain_tt_view,0)) --tuyetnta cf
										END ) As tongSoLuongThucChay,

										Sum(CASE WHEN ProductUnitName = N''CPM'' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) 
														THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
												WHEN ProductUnitName = N''CPC'' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) 
														THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0)) 
												WHEN ProductUnitName = N''TRUEVIEW'' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) 
														THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
												WHEN ProductUnitName = N''TRUE VIEW'' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) 
														THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
												ELSE 0
										END ) AS  tongSoLuongThucChayKM,

										Sum(CONVERT(FLOAT,ISNULL(domain_tt_money,0))/(1+(Cast(vat as NUMERIC(18,2))/100.00))) As tongThanhTienThucChay,
										Sum(CONVERT(FLOAT,ISNULL(domain_tt_promotion,0))/(1+(Cast(vat as NUMERIC(18,2))/100.00))) As tongThanhTienThucChayKM,
										Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
										FROM ' + @Table + ' Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
										And (''' + @Contract + ''' = '''' Or Lower(contract_number) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + '''))) Group By contract_number,banner_id,TenSanPham';

			DECLARE @queryTC NVARCHAR(MAX) = 'SELECT soHopDong,DmBannerID,tenSanPham,
										IsNull(Sum(Cast(SoLuongThucChay As Float)),0) As tongSoLuongThucChay,
										IsNull(Sum(Cast(SoLuongThucChayKM As Float)),0) As tongSoLuongThucChayKM,
										IsNull(Sum(Cast(ThanhTienThucChaySauCK_ChuaVAT As Float)),0) As tongThanhTienThucChay,
										IsNull(Sum(Cast(ThanhTienThucChayKM As Float)),0) As tongThanhTienThucChayKM,
										Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
										FROM [dbo].[ThucChay_ThanhTien_Admatic] Where CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE) 
										And (''' + @Contract + ''' = '''' Or Lower(SoHopDong) In (Select Name From STRING_SPLIT_QLTC(''' + @Contract + ''')))
										Group By SoHopDong,DmBannerID,TenSanPham';

			DECLARE @tblDataTC TABLE(
				soHopDong NVARCHAR(200) NULL,
				DmBannerID INT NULL,
				tenSanPham NVARCHAR(200) NULL,
				tongSoLuongThucChay FLOAT NULL,
				tongSoLuongThucChayKM FLOAT NULL,
				tongThanhTienThucChay FLOAT NULL,
				tongThanhTienThucChayKM FLOAT NULL,
				tuNgay DATETIME2 NULL,
				denNgay DATETIME2 NULL
			)


			INSERT INTO @tblDataTC
			EXECUTE sp_executesql @queryTC, N'@FromDate Nvarchar(103), @ToDate Nvarchar(103), @Contract Nvarchar(500), @Table Nvarchar(500)',
			@FromDate = @FromDate,
			@ToDate = @ToDate,
			@Contract = @Contract,
			@Table = @Table

			DECLARE @tblDataTest TABLE(
				contract_number NVARCHAR(200) NULL,
				banner_id INT NULL,
				tenSanPham NVARCHAR(200) NULL,
				tongSoLuongThucChay FLOAT NULL,
				tongSoLuongThucChayKM FLOAT NULL,
				tongThanhTienThucChay FLOAT NULL,
				tongThanhTienThucChayKM FLOAT NULL,
				tuNgay DATETIME2 NULL,
				denNgay DATETIME2 NULL
			)
			INSERT INTO @tblDataTest
			EXECUTE sp_executesql @queryTest, N'@FromDate Nvarchar(103), @ToDate Nvarchar(103), @Contract Nvarchar(500), @Table Nvarchar(500)',
			@FromDate = @FromDate,
			@ToDate = @ToDate,
			@Contract = @Contract,
			@Table = @Table

			--SELECT * FROM @tblDataTest
			--SELECT * FROM @tblDataTC

			SELECT dataTest.contract_number SoHopDong, dataTest.banner_id DmBannerID, dataTest.tenSanPham, 
								dbo.FormatNumber(dataTest.tongSoLuongThucChay) tongSoLuongThucChay_Moi, dbo.FormatNumber(dataTC.tongSoLuongThucChay) tongSoLuongThucChay_Cu,
								dbo.FormatNumber(dataTest.tongThanhTienThucChay) tongThanhTienThucChay_Moi, dbo.FormatNumber(dataTC.tongThanhTienThucChay) tongThanhTienThucChay_Cu,
								dbo.FormatNumber(dataTest.tongSoLuongThucChayKM) tongSoLuongThucChayKM_Moi, dbo.FormatNumber(dataTC.tongSoLuongThucChayKM) tongSoLuongThucChayKM_Cu,
								dbo.FormatNumber(dataTest.tongThanhTienThucChayKM) tongThanhTienThucChayKM_Moi, dbo.FormatNumber(dataTC.tongThanhTienThucChayKM) tongThanhTienThucChayKM_Cu,

								dbo.FormatNumber(dataTest.tongSoLuongThucChay - dataTC.tongSoLuongThucChay) As tongSoLuongThucChay_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongThanhTienThucChay - dataTC.tongThanhTienThucChay) As tongThanhTienThucChay_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongSoLuongThucChayKM - dataTC.tongSoLuongThucChayKM) As tongSoLuongThucChayKM_Chenh_Lech,
								dbo.FormatNumber(dataTest.tongThanhTienThucChayKM - dataTC.tongThanhTienThucChayKM) As tongThanhTienThucChayKM_Chenh_Lech,
								dataTest.tuNgay, dataTest.denNgay FROM @tblDataTest dataTest
								LEFT Join @tblDataTC dataTC ON dataTest.banner_id = dataTC.DmBannerID;
			RETURN;
		End

	Print @querySql;

	EXECUTE sp_executesql @querySql, N'@FromDate Nvarchar(103), @ToDate Nvarchar(103), @Contract Nvarchar(500), @Table Nvarchar(500)',
	@FromDate = @FromDate,
	@ToDate = @ToDate,
	@Contract = @Contract,
	@Table = @Table
END

```
