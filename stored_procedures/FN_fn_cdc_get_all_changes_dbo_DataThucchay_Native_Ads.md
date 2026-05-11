# Function: `fn_cdc_get_all_changes_dbo_DataThucchay_Native_Ads`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2023-06-29 22:31:14.990000
- **Ngày sửa cuối**: 2023-06-29 22:31:14.990000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_DataThucchay_Native_Ads]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [SoHopDong], NULL as [TypeProduct], NULL as [TenSanPham], NULL as [TenNhanHang], NULL as [NhanHangID], NULL as [DmBannerID], NULL as [DmWebsiteID], NULL as [TenWebsite], NULL as [DmViTriREF], NULL as [TenViTri], NULL as [SoLuongThucChay], NULL as [SoLuongThucChayKhuyenMai], NULL as [DonViTinh], NULL as [ThanhTienThucChay], NULL as [ThanhTienThucChaykhuyenMai], NULL as [NgayThucHien], NULL as [createdBy], NULL as [createdAt], NULL as [id], NULL as [DmCampaignID], NULL as [VAT]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_DataThucchay_Native_Ads', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[SoHopDong], t.[TypeProduct], t.[TenSanPham], t.[TenNhanHang], t.[NhanHangID], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriREF], t.[TenViTri], t.[SoLuongThucChay], t.[SoLuongThucChayKhuyenMai], t.[DonViTinh], t.[ThanhTienThucChay], t.[ThanhTienThucChaykhuyenMai], t.[NgayThucHien], t.[createdBy], t.[createdAt], t.[id], t.[DmCampaignID], t.[VAT]
	from [cdc].[dbo_DataThucchay_Native_Ads_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_DataThucchay_Native_Ads', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[SoHopDong], t.[TypeProduct], t.[TenSanPham], t.[TenNhanHang], t.[NhanHangID], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriREF], t.[TenViTri], t.[SoLuongThucChay], t.[SoLuongThucChayKhuyenMai], t.[DonViTinh], t.[ThanhTienThucChay], t.[ThanhTienThucChaykhuyenMai], t.[NgayThucHien], t.[createdBy], t.[createdAt], t.[id], t.[DmCampaignID], t.[VAT]
	from [cdc].[dbo_DataThucchay_Native_Ads_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_DataThucchay_Native_Ads', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
