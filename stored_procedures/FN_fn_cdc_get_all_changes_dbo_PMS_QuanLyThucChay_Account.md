# Function: `fn_cdc_get_all_changes_dbo_PMS_QuanLyThucChay_Account`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:45.110000
- **Ngày sửa cuối**: 2021-08-31 08:38:45.110000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_PMS_QuanLyThucChay_Account]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [Id], NULL as [B_QuanLyThucChayREF], NULL as [D_NhanSuREF], NULL as [CreationTime], NULL as [CreatorUserId], NULL as [LastModificationTime], NULL as [LastModifierUserId], NULL as [IsDeleted]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_PMS_QuanLyThucChay_Account', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[Id], t.[B_QuanLyThucChayREF], t.[D_NhanSuREF], t.[CreationTime], t.[CreatorUserId], t.[LastModificationTime], t.[LastModifierUserId], t.[IsDeleted]
	from [cdc].[dbo_PMS_QuanLyThucChay_Account_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_PMS_QuanLyThucChay_Account', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[Id], t.[B_QuanLyThucChayREF], t.[D_NhanSuREF], t.[CreationTime], t.[CreatorUserId], t.[LastModificationTime], t.[LastModifierUserId], t.[IsDeleted]
	from [cdc].[dbo_PMS_QuanLyThucChay_Account_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_PMS_QuanLyThucChay_Account', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
