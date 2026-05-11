# Function: `fn_cdc_get_all_changes_dbo_DmWebsiteReportingdb`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:38.543000
- **Ngày sửa cuối**: 2021-08-31 08:38:38.543000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_DmWebsiteReportingdb]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [DmWebsiteReportingdbID], NULL as [TenWebsite], NULL as [CreatedBy], NULL as [CreatedAt], NULL as [LastModifiedBy], NULL as [LastModifiedAt], NULL as [DeletedStatus], NULL as [PrintStatus], NULL as [RecordStatus], NULL as [ID]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_DmWebsiteReportingdb', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[DmWebsiteReportingdbID], t.[TenWebsite], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[PrintStatus], t.[RecordStatus], t.[ID]
	from [cdc].[dbo_DmWebsiteReportingdb_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_DmWebsiteReportingdb', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[DmWebsiteReportingdbID], t.[TenWebsite], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[PrintStatus], t.[RecordStatus], t.[ID]
	from [cdc].[dbo_DmWebsiteReportingdb_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_DmWebsiteReportingdb', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
