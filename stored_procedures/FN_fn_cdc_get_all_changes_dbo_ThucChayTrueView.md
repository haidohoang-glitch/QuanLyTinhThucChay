# Function: `fn_cdc_get_all_changes_dbo_ThucChayTrueView`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:41.197000
- **Ngày sửa cuối**: 2021-08-31 08:38:41.197000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_ThucChayTrueView]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [SoHopDong], NULL as [TypeProduct], NULL as [DmSanPhamREF], NULL as [TenSanPham], NULL as [campaignid], NULL as [bannerid], NULL as [SiteName], NULL as [SiteID], NULL as [True_View], NULL as [Views], NULL as [Clicks], NULL as [NgayThucHien], NULL as [CreatedBy], NULL as [CreatedAt], NULL as [LastModifiedBy], NULL as [LastModifiedAt], NULL as [DeletedStatus], NULL as [FormatName], NULL as [id]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayTrueView', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[campaignid], t.[bannerid], t.[SiteName], t.[SiteID], t.[True_View], t.[Views], t.[Clicks], t.[NgayThucHien], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[FormatName], t.[id]
	from [cdc].[dbo_ThucChayTrueView_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayTrueView', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[campaignid], t.[bannerid], t.[SiteName], t.[SiteID], t.[True_View], t.[Views], t.[Clicks], t.[NgayThucHien], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[FormatName], t.[id]
	from [cdc].[dbo_ThucChayTrueView_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayTrueView', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
