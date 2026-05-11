# Function: `fn_cdc_get_all_changes_dbo_ThucChay`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:46.120000
- **Ngày sửa cuối**: 2021-08-31 08:38:46.120000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_ThucChay]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucChayID], NULL as [SoHopDong], NULL as [DanhsachDmBookingREF], NULL as [DmSanPhamREF], NULL as [TenSanPham], NULL as [DmNhomWebsiteREF], NULL as [TenNhomWebsite], NULL as [DmWebsiteREF], NULL as [TenWebsite], NULL as [DmChienDichREF], NULL as [TenChienDich], NULL as [DmBannerREF], NULL as [TenBanner], NULL as [NgayThucHien], NULL as [TongViewThucChay], NULL as [TongClickThucChay], NULL as [CreatedBy], NULL as [CreatedAt], NULL as [LastModifiedBy], NULL as [LastModifiedAt], NULL as [DeletedStatus], NULL as [PrintStatus], NULL as [RecordStatus], NULL as [TongSoBaiViet], NULL as [SoThuTuTheoNgay], NULL as [TypeProduct], NULL as [BannerType], NULL as [UserName], NULL as [SaleName], NULL as [Email], NULL as [LastTimeCalc], NULL as [sys_date], NULL as [IsReady], NULL as [ProductUnitID], NULL as [ProductUnitName], NULL as [BannerTypeName], NULL as [HopDongChiTietREF], NULL as [CampainStatus], NULL as [BannerStatus], NULL as [IsNoiBo], NULL as [ID]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChayID], t.[SoHopDong], t.[DanhsachDmBookingREF], t.[DmSanPhamREF], t.[TenSanPham], t.[DmNhomWebsiteREF], t.[TenNhomWebsite], t.[DmWebsiteREF], t.[TenWebsite], t.[DmChienDichREF], t.[TenChienDich], t.[DmBannerREF], t.[TenBanner], t.[NgayThucHien], t.[TongViewThucChay], t.[TongClickThucChay], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[PrintStatus], t.[RecordStatus], t.[TongSoBaiViet], t.[SoThuTuTheoNgay], t.[TypeProduct], t.[BannerType], t.[UserName], t.[SaleName], t.[Email], t.[LastTimeCalc], t.[sys_date], t.[IsReady], t.[ProductUnitID], t.[ProductUnitName], t.[BannerTypeName], t.[HopDongChiTietREF], t.[CampainStatus], t.[BannerStatus], t.[IsNoiBo], t.[ID]
	from [cdc].[dbo_ThucChay_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChayID], t.[SoHopDong], t.[DanhsachDmBookingREF], t.[DmSanPhamREF], t.[TenSanPham], t.[DmNhomWebsiteREF], t.[TenNhomWebsite], t.[DmWebsiteREF], t.[TenWebsite], t.[DmChienDichREF], t.[TenChienDich], t.[DmBannerREF], t.[TenBanner], t.[NgayThucHien], t.[TongViewThucChay], t.[TongClickThucChay], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[PrintStatus], t.[RecordStatus], t.[TongSoBaiViet], t.[SoThuTuTheoNgay], t.[TypeProduct], t.[BannerType], t.[UserName], t.[SaleName], t.[Email], t.[LastTimeCalc], t.[sys_date], t.[IsReady], t.[ProductUnitID], t.[ProductUnitName], t.[BannerTypeName], t.[HopDongChiTietREF], t.[CampainStatus], t.[BannerStatus], t.[IsNoiBo], t.[ID]
	from [cdc].[dbo_ThucChay_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
