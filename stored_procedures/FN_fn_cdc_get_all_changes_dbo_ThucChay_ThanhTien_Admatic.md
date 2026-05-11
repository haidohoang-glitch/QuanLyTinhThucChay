# Function: `fn_cdc_get_all_changes_dbo_ThucChay_ThanhTien_Admatic`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2023-08-07 14:19:32.807000
- **Ngày sửa cuối**: 2023-08-07 14:19:32.807000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_ThucChay_ThanhTien_Admatic]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucChay_ThanhTien_AdmaticID], NULL as [SoHopDong], NULL as [TypeProduct], NULL as [DmSanPhamREF], NULL as [TenSanPham], NULL as [TenNhanHang], NULL as [DmNhanHangREF], NULL as [DmBannerID], NULL as [DmWebsiteID], NULL as [TenWebsite], NULL as [DmViTriBannerSanPhamID], NULL as [TenViTriBannerSanPham], NULL as [SoLuongThucChay], NULL as [SoLuongThucChayKM], NULL as [DonViTinh], NULL as [ThanhTienThucChaySauCK_ChuaVAT], NULL as [ThanhTienThucChayKM], NULL as [NgayThucHien], NULL as [CreatedAt], NULL as [CreatedBy], NULL as [LastModifiedAt], NULL as [LastModifiedBy], NULL as [DeletedStatus]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay_ThanhTien_Admatic', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChay_ThanhTien_AdmaticID], t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[TenNhanHang], t.[DmNhanHangREF], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriBannerSanPhamID], t.[TenViTriBannerSanPham], t.[SoLuongThucChay], t.[SoLuongThucChayKM], t.[DonViTinh], t.[ThanhTienThucChaySauCK_ChuaVAT], t.[ThanhTienThucChayKM], t.[NgayThucHien], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[DeletedStatus]
	from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay_ThanhTien_Admatic', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChay_ThanhTien_AdmaticID], t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[TenNhanHang], t.[DmNhanHangREF], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriBannerSanPhamID], t.[TenViTriBannerSanPham], t.[SoLuongThucChay], t.[SoLuongThucChayKM], t.[DonViTinh], t.[ThanhTienThucChaySauCK_ChuaVAT], t.[ThanhTienThucChayKM], t.[NgayThucHien], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[DeletedStatus]
	from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay_ThanhTien_Admatic', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
