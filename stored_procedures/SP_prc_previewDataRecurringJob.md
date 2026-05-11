# Stored Procedure: `prc_previewDataRecurringJob`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-09-24 10:10:05.773000
- **Ngày sửa cuối**: 2023-09-27 10:28:24.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableNameNew` | `nvarchar(4000)` | No |
| `@TableNameOld` | `nvarchar(4000)` | No |
| `@FromDate` | `nvarchar(206)` | No |
| `@ToDate` | `nvarchar(206)` | No |
| `@Contract` | `nvarchar(4000)` | No |
| `@isTest` | `bit(1)` | No |

## Definition (Source Code)

```sql


CREATE PROCEDURE [dbo].[prc_previewDataRecurringJob]
	-- Add the parameters for the stored procedure here
	@TableNameNew Nvarchar(2000),
	@TableNameOld Nvarchar(2000),
	@FromDate Nvarchar(103),
	@ToDate Nvarchar(103),
	@Contract Nvarchar(2000) = '',
	@isTest bit = 0

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @admatic Nvarchar(500) = 'contract_number,banner_id,domain_tt_view,domain_tt_click,domain_tt_money,domain_tt_promotion';
	Declare @checkColumn int = 0;
	Declare @queryNew Nvarchar(MAX) = 'SELECT * FROM ' + @TableNameNew + ' WHERE CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE)';
	Declare @queryOld Nvarchar(MAX) = 'SELECT * FROM ' + @TableNameOld + ' WHERE CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE)';
	Declare @queryTotalNew Nvarchar(MAX);
	Declare @queryTotalOld Nvarchar(MAX);
	Declare @queryTotalAll Nvarchar(MAX);
	DECLARE @tableTyproduct TABLE(
		typeProduct int
	)
	Select @checkColumn = Count(*) From (SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = @TableNameNew) a
	Where a.COLUMN_NAME In (select Name from STRING_SPLIT_QLTC(@admatic));

	Declare @checkTyProduct int = 0;
	--DECLARE @queryCheckTyProduct NVARCHAR(MAX) = 'SET ' + @checkTyProduct +' = (SELECT TOP(1) TypeProduct FROM ' + @TableNameNew + ' WHERE CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE))';
	DECLARE @queryCheckTyProduct NVARCHAR(MAX) = 'SELECT TOP(1) TypeProduct FROM ' + @TableNameNew + ' WHERE CAST(NgayThucHien AS DATE) >= CAST(''' + @FromDate + ''' AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(''' + @ToDate + ''' AS DATE)';
	--Check xem dữ liệu thuộc nhóm Admatic hay Branding
	If(@checkColumn = 6)
		Begin
			Print 'Admatic';
			--thuộc nhóm Admatic
			Set @queryNew = @queryNew + ' And (CASE WHEN (IsNull(''' + @Contract + ''','''') <> '''') THEN (CASE WHEN(Lower(contract_number)  In (Select Lower(Name) From STRING_SPLIT_QLTC(''' + @Contract + '''))) THEN 1 ELSE 0 END) ELSE 1 END ) > 0';
			Set @queryOld = @queryOld + ' And (CASE WHEN (IsNull(''' + @Contract + ''','''') <> '''') THEN (CASE WHEN(Lower(contract_number)  In (Select Lower(Name) From STRING_SPLIT_QLTC(''' + @Contract + '''))) THEN 1 ELSE 0 END) ELSE 1 END ) > 0';
			


			If(@isTest = 1)
				Begin
					Set @queryTotalNew = 'Select contract_number,banner_id,tenSanPham,
					Sum(IsNull(Cast(domain_tt_click As Float),0)) As domain_tt_click,
					Sum(IsNull(Cast(domain_tt_view As Float),0)) As domain_tt_view,
					Sum(IsNull(Cast(domain_tt_money As Float),0)) As domain_tt_money,
					Sum(IsNull(Cast(domain_tt_promotion As Float),0)) As domain_tt_promotion,
					Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
					From (' + @queryNew + ') dtNew Group By contract_number,banner_id,tenSanPham';

					Set @queryTotalOld = 'Select contract_number,banner_id,tenSanPham,
					Sum(IsNull(Cast(domain_tt_click As Float),0)) As domain_tt_click,
					Sum(IsNull(Cast(domain_tt_view As Float),0)) As domain_tt_view,
					Sum(IsNull(Cast(domain_tt_money As Float),0)) As domain_tt_money,
					Sum(IsNull(Cast(domain_tt_promotion As Float),0)) As domain_tt_promotion,
					Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
					From (' + @queryOld + ') dtNew Group By contract_number,banner_id,tenSanPham';

					Set @queryTotalAll = 'Select dtTotalNew.contract_number, dtTotalNew.banner_id, dtTotalNew.tenSanPham,
							dbo.FormatNumber(dtTotalNew.domain_tt_click) As domain_tt_click_Moi,
							dbo.FormatNumber(dtTotalOld.domain_tt_click) As domain_tt_click_Cu,
							dbo.FormatNumber(dtTotalNew.domain_tt_view) As domain_tt_view_Moi,
							dbo.FormatNumber(dtTotalOld.domain_tt_view) As domain_tt_view_Cu,
							dbo.FormatNumber(dtTotalNew.domain_tt_money) As domain_tt_money_Moi,
							dbo.FormatNumber(dtTotalOld.domain_tt_money) As domain_tt_money_Cu,
							dbo.FormatNumber(dtTotalNew.domain_tt_promotion) As domain_tt_promotion_Moi,
							dbo.FormatNumber(dtTotalOld.domain_tt_promotion) As domain_tt_promotion_Cu,
							dbo.FormatNumber(dtTotalNew.domain_tt_click - dtTotalOld.domain_tt_click) As domain_tt_click_Chenh_Lech,
							dbo.FormatNumber(dtTotalNew.domain_tt_view - dtTotalOld.domain_tt_view) As domain_tt_view_Chenh_Lech,
							dbo.FormatNumber(dtTotalNew.domain_tt_money - dtTotalOld.domain_tt_money) As domain_tt_money_Chenh_Lech,
							dbo.FormatNumber(dtTotalNew.domain_tt_promotion - dtTotalOld.domain_tt_promotion) As domain_tt_promotion_Chenh_Lech,
							dtTotalNew.tuNgay,
							dtTotalNew.denNgay
							From (' + @queryTotalNew + ') dtTotalNew Left Join (' + @queryTotalOld + ') dtTotalOld 
							On dtTotalNew.banner_id = dtTotalOld.banner_id'

					--Đọc dữ liệu ra
					EXECUTE sp_executesql @queryTotalAll, N'@queryNew Nvarchar(Max), @queryOld Nvarchar(Max), @TableNameNew Nvarchar(200), @TableNameOld Nvarchar(200), @queryTotalNew Nvarchar(Max), @queryTotalOld Nvarchar(Max), @FromDate DateTime, @ToDate DateTime, @Contract Nvarchar(50)',
					@queryNew = @queryNew,
					@queryOld = @queryOld,
					@queryTotalNew = @queryTotalNew,
					@queryTotalOld = @queryTotalOld,
					@TableNameNew = @TableNameNew,
					@TableNameOld = @TableNameOld,
					@FromDate = @FromDate,
					@ToDate = @ToDate,
					@Contract = @Contract
				End
			Else
				Begin
					Set @queryTotalAll = 'Select contract_number,banner_id,tenSanPham,
					dbo.FormatNumber(Sum(IsNull(Cast(domain_tt_click As Float),0))) As domain_tt_click,
					dbo.FormatNumber(Sum(IsNull(Cast(domain_tt_view As Float),0))) As domain_tt_view,
					dbo.FormatNumber(Sum(IsNull(Cast(domain_tt_money As Float),0))) As domain_tt_money,
					dbo.FormatNumber(Sum(IsNull(Cast(domain_tt_promotion As Float),0))) As domain_tt_promotion,
					Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
					From (' + @queryNew + ') dtNew Group By contract_number,banner_id,tenSanPham';

					--Đọc dữ liệu ra
					EXECUTE sp_executesql @queryTotalAll, N'@queryNew Nvarchar(Max), @TableNameNew Nvarchar(200), @FromDate DateTime, @ToDate DateTime, @Contract Nvarchar(50)',
					@queryNew = @queryNew,
					@TableNameNew = @TableNameNew,
					@FromDate = @FromDate,
					@ToDate = @ToDate,
					@Contract = @Contract
				End
		End
	Else
		BEGIN
			Print 'Branding';
			--thuộc nhóm Branding
			Set @queryNew = @queryNew + ' And soHopDong <> ''TONGSANPHAM'' And (CASE WHEN (IsNull(''' + @Contract + ''','''') <> '''') THEN (CASE WHEN(Lower(soHopDong) In (Select Lower(Name) From STRING_SPLIT_QLTC(''' + @Contract + '''))) THEN 1 ELSE 0 END) ELSE 1 END ) > 0';
			Set @queryOld = @queryOld + ' And soHopDong <> ''TONGSANPHAM'' And (CASE WHEN (IsNull(''' + @Contract + ''','''') <> '''') THEN (CASE WHEN(Lower(soHopDong) In (Select Lower(Name) From STRING_SPLIT_QLTC(''' + @Contract + '''))) THEN 1 ELSE 0 END) ELSE 1 END ) > 0';
			
			INSERT INTO @tableTyproduct
			EXECUTE sp_executesql @queryCheckTyProduct, N'@TableNameNew Nvarchar(200), @FromDate DateTime, @ToDate DateTime',
			@TableNameNew = @TableNameNew,
			@FromDate = @FromDate,
			@ToDate = @ToDate
			
			Print @queryCheckTyProduct;

			SELECT TOP(1) @checkTyProduct = typeProduct FROM @tableTyproduct
			If(@isTest = 1)
				BEGIN
					Print @checkTyProduct;
					IF(@checkTyProduct <> 19 AND @checkTyProduct <> 5133)
						BEGIN
							Print 'a';
							Set @queryTotalNew = 'SELECT soHopDong,bannerid,tenSanPham,
								Sum(IsNull(Cast(tongViewThucChay As Float),0)) As tongViewThucChay,
								Sum(IsNull(Cast(tongClickThucChay As Float),0)) As tongClickThucChay,
								Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
								From (' + @queryNew + ') dtNew Group By soHopDong,bannerid,tenSanPham';

							Set @queryTotalOld = 'SELECT soHopDong,bannerid,tenSanPham,
								Sum(IsNull(Cast(tongViewThucChay As Float),0)) As tongViewThucChay,
								Sum(IsNull(Cast(tongClickThucChay As Float),0)) As tongClickThucChay,
								Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
								From (' + @queryOld + ') dtNew Group By soHopDong,bannerid,tenSanPham';

							Set @queryTotalAll = 'Select dtTotalNew.SoHopDong, dtTotalNew.bannerid,dtTotalNew.tenSanPham,
								dbo.FormatNumber(dtTotalNew.tongViewThucChay) As domain_tt_view_Moi,
								dbo.FormatNumber(dtTotalOld.tongViewThucChay) As domain_tt_view_Cu,
								dbo.FormatNumber(dtTotalNew.tongClickThucChay) As domain_tt_click_Moi,
								dbo.FormatNumber(dtTotalOld.tongClickThucChay) As domain_tt_click_Cu,
								dbo.FormatNumber(dtTotalNew.tongViewThucChay - dtTotalOld.tongViewThucChay) As tongViewThucChay_Chenh_Lech,
								dbo.FormatNumber(dtTotalNew.tongClickThucChay - dtTotalOld.tongClickThucChay) As tongClickThucChay_Chenh_Lech,
								dtTotalNew.tuNgay,
								dtTotalNew.denNgay
									From (' + @queryTotalNew + ') dtTotalNew Left Join (' + @queryTotalOld + ') dtTotalOld 
									On dtTotalNew.bannerid = dtTotalOld.bannerid'
							--Đọc dữ liệu ra
							EXECUTE sp_executesql @queryTotalAll, N'@queryNew Nvarchar(Max), @queryOld Nvarchar(Max), @TableNameNew Nvarchar(200), @TableNameOld Nvarchar(200), @queryTotalNew Nvarchar(Max), @queryTotalOld Nvarchar(Max), @FromDate DateTime, @ToDate DateTime, @Contract Nvarchar(50)',
							@queryNew = @queryNew,
							@queryOld = @queryOld,
							@queryTotalNew = @queryTotalNew,
							@queryTotalOld = @queryTotalOld,
							@TableNameNew = @TableNameNew,
							@TableNameOld = @TableNameOld,
							@FromDate = @FromDate,
							@ToDate = @ToDate,
							@Contract = @Contract
						END
					ELSE
						BEGIN
							Print 'b';
							Set @queryTotalNew = 'SELECT SoHopDong,DmBannerID,TenSanPham,
								Sum(IsNull(Cast(SoLuongThucChay As Float),0)) As tongSoLuongThucChay,
								Sum(IsNull(Cast(ThanhTienThucChay As Float),0)) As tongThanhTienThucChay,
								
								Sum(IsNull(Cast(SoLuongThucChayKhuyenMai As Float),0)) As tongSoLuongThucChayKM,
								Sum(IsNull(Cast(ThanhTienThucChaykhuyenMai As Float),0)) As tongThanhTienThucChayKM,

								Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
								From (' + @queryNew + ') dtNew Group By SoHopDong,DmBannerID,tenSanPham';
							Set @queryTotalOld = 'SELECT SoHopDong,DmBannerID,tenSanPham,
								Sum(IsNull(Cast(SoLuongThucChay As Float),0)) As tongSoLuongThucChay,
								Sum(IsNull(Cast(ThanhTienThucChay As Float),0)) As tongThanhTienThucChay,

								Sum(IsNull(Cast(SoLuongThucChayKhuyenMai As Float),0)) As tongSoLuongThucChayKM,
								Sum(IsNull(Cast(ThanhTienThucChaykhuyenMai As Float),0)) As tongThanhTienThucChayKM,

								Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
								From (' + @queryOld + ') dtNew Group By SoHopDong,DmBannerID,tenSanPham';
							
							Set @queryTotalAll = 'Select dtTotalNew.SoHopDong, dtTotalNew.DmBannerID,dtTotalNew.tenSanPham,
								dbo.FormatNumber(dtTotalNew.tongSoLuongThucChay) As tongSoLuongThucChay_Moi,
								dbo.FormatNumber(dtTotalOld.tongSoLuongThucChay) As tongSoLuongThucChay_Cu,								
								dbo.FormatNumber(dtTotalNew.tongThanhTienThucChay) As tongThanhTienThucChay_Moi,
								dbo.FormatNumber(dtTotalOld.tongThanhTienThucChay) As tongThanhTienThucChay_Cu,
								dbo.FormatNumber(dtTotalNew.tongSoLuongThucChay - dtTotalOld.tongSoLuongThucChay) As tongSoLuongThucChay_Chenh_Lech,
								dbo.FormatNumber(dtTotalNew.tongThanhTienThucChay - dtTotalOld.tongThanhTienThucChay) As tongThanhTienThucChay_Chenh_Lech,

								dbo.FormatNumber(dtTotalNew.tongSoLuongThucChayKM) As tongSoLuongThucChayKM_Moi,
								dbo.FormatNumber(dtTotalOld.tongSoLuongThucChayKM) As tongSoLuongThucChayKM_Cu,
								dbo.FormatNumber(dtTotalNew.tongThanhTienThucChayKM) As tongThanhTienThucChayKM_Moi,
								dbo.FormatNumber(dtTotalOld.tongThanhTienThucChayKM) As tongThanhTienThucChayKM_Cu,
								dbo.FormatNumber(dtTotalNew.tongSoLuongThucChayKM - dtTotalOld.tongSoLuongThucChayKM) As tongSoLuongThucChayKM_Chenh_Lech,
								dbo.FormatNumber(dtTotalNew.tongThanhTienThucChayKM - dtTotalOld.tongThanhTienThucChayKM) As tongThanhTienThucChayKM_Chenh_Lech,
								
								dtTotalNew.tuNgay,
								dtTotalNew.denNgay
									From (' + @queryTotalNew + ') dtTotalNew Left Join (' + @queryTotalOld + ') dtTotalOld 
									On dtTotalNew.DmBannerID = dtTotalOld.DmBannerID'
							--Đọc dữ liệu ra
							EXECUTE sp_executesql @queryTotalAll, N'@queryNew Nvarchar(Max), @queryOld Nvarchar(Max), @TableNameNew Nvarchar(200), @TableNameOld Nvarchar(200), @queryTotalNew Nvarchar(Max), @queryTotalOld Nvarchar(Max), @FromDate DateTime, @ToDate DateTime, @Contract Nvarchar(50)',
							@queryNew = @queryNew,
							@queryOld = @queryOld,
							@queryTotalNew = @queryTotalNew,
							@queryTotalOld = @queryTotalOld,
							@TableNameNew = @TableNameNew,
							@TableNameOld = @TableNameOld,
							@FromDate = @FromDate,
							@ToDate = @ToDate,
							@Contract = @Contract
						END
					
				END
			Else
				BEGIN
					IF(@checkTyProduct <> 19 AND @checkTyProduct <> 5133)
						BEGIN
							SET @queryTotalAll = 'SELECT soHopDong,bannerid,tenSanPham,
							dbo.FormatNumber(Sum(IsNull(Cast(tongViewThucChay As Float),0))) As tongViewThucChay,
							dbo.FormatNumber(Sum(IsNull(Cast(tongClickThucChay As Float),0))) As tongClickThucChay,
							Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
							From (' + @queryNew + ') dtNew Group By SoHopDong,bannerid,tenSanPham';
							--Đọc dữ liệu ra
							EXECUTE sp_executesql @queryTotalAll, N'@queryNew Nvarchar(Max), @TableNameNew Nvarchar(200), @FromDate DateTime, @ToDate DateTime, @Contract Nvarchar(50)',
							@queryNew = @queryNew,
							@TableNameNew = @TableNameNew,
							@FromDate = @FromDate,
							@ToDate = @ToDate,
							@Contract = @Contract
						END
					ELSE
						BEGIN
							SET @queryTotalAll = 'SELECT soHopDong,DmBannerID,tenSanPham,
							dbo.FormatNumber(Sum(IsNull(Cast(SoLuongThucChay As Float),0))) As tongSoLuongThucChay,
							dbo.FormatNumber(Sum(IsNull(Cast(ThanhTienThucChay As Float),0))) As tongThanhTienThucChay,
							dbo.FormatNumber(Sum(IsNull(Cast(SoLuongThucChayKM As Float),0))) As tongSoLuongThucChayKM,
							dbo.FormatNumber(Sum(IsNull(Cast(ThanhTienThucChayKM As Float),0))) As tongThanhTienThucChayKM,
							Min(NgayThucHien) As tuNgay, Max(NgayThucHien) As denNgay
							From (' + @queryNew + ') dtNew Group By SoHopDong,DmBannerID,tenSanPham';
							--Đọc dữ liệu ra
							EXECUTE sp_executesql @queryTotalAll, N'@queryNew Nvarchar(Max), @TableNameNew Nvarchar(200), @FromDate DateTime, @ToDate DateTime, @Contract Nvarchar(50)',
							@queryNew = @queryNew,
							@TableNameNew = @TableNameNew,
							@FromDate = @FromDate,
							@ToDate = @ToDate,
							@Contract = @Contract
						END

				End
		End

	--Đọc dữ liệu ra
	EXECUTE sp_executesql @queryNew, N'@TableNameNew Nvarchar(200), @FromDate DateTime, @ToDate DateTime, @Contract Nvarchar(50)',
	@TableNameNew = @TableNameNew,
	@FromDate = @FromDate,
	@ToDate = @ToDate,
	@Contract = @Contract
END

```
