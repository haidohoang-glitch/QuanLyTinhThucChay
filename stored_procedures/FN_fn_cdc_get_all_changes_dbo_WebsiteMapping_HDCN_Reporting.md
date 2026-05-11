# Function: `fn_cdc_get_all_changes_dbo_WebsiteMapping_HDCN_Reporting`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:43.470000
- **Ngày sửa cuối**: 2021-08-31 08:38:43.470000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_WebsiteMapping_HDCN_Reporting]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [DmWebsiteID], NULL as [WebsiteLink], NULL as [DmWebsiteReportingdbID], NULL as [CREATED_AT], NULL as [LASTMODIFIED_AT]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_WebsiteMapping_HDCN_Reporting', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[DmWebsiteID], t.[WebsiteLink], t.[DmWebsiteReportingdbID], t.[CREATED_AT], t.[LASTMODIFIED_AT]
	from [cdc].[dbo_WebsiteMapping_HDCN_Reporting_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_WebsiteMapping_HDCN_Reporting', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[DmWebsiteID], t.[WebsiteLink], t.[DmWebsiteReportingdbID], t.[CREATED_AT], t.[LASTMODIFIED_AT]
	from [cdc].[dbo_WebsiteMapping_HDCN_Reporting_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_WebsiteMapping_HDCN_Reporting', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
