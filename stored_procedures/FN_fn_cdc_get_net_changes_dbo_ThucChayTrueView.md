# Function: `fn_cdc_get_net_changes_dbo_ThucChayTrueView`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:41.210000
- **Ngày sửa cuối**: 2021-08-31 08:38:41.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_net_changes_dbo_ThucChayTrueView]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return

	select NULL as __$start_lsn,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [SoHopDong], NULL as [TypeProduct], NULL as [DmSanPhamREF], NULL as [TenSanPham], NULL as [campaignid], NULL as [bannerid], NULL as [SiteName], NULL as [SiteID], NULL as [True_View], NULL as [Views], NULL as [Clicks], NULL as [NgayThucHien], NULL as [CreatedBy], NULL as [CreatedAt], NULL as [LastModifiedBy], NULL as [LastModifiedAt], NULL as [DeletedStatus], NULL as [FormatName], NULL as [id]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayTrueView', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 0)

	union all
	
	select __$start_lsn,
	    case __$count_6F9F918A
	    when 1 then __$operation
	    else
			case __$min_op_6F9F918A 
				when 2 then 2
				when 4 then
				case __$operation
					when 1 then 1
					else 4
					end
				else
				case __$operation
					when 2 then 4
					when 4 then 4
					else 1
					end
			end
		end as __$operation,
		null as __$update_mask , [SoHopDong], [TypeProduct], [DmSanPhamREF], [TenSanPham], [campaignid], [bannerid], [SiteName], [SiteID], [True_View], [Views], [Clicks], [NgayThucHien], [CreatedBy], [CreatedAt], [LastModifiedBy], [LastModifiedAt], [DeletedStatus], [FormatName], [id]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_6F9F918A 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_ThucChayTrueView_CT] c with (nolock)   
			where  ( (c.[id] = t.[id]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_6F9F918A, __$count_6F9F918A, t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[campaignid], t.[bannerid], t.[SiteName], t.[SiteID], t.[True_View], t.[Views], t.[Clicks], t.[NgayThucHien], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[FormatName], t.[id] 
		from [cdc].[dbo_ThucChayTrueView_CT] t with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_6F9F918A,
		    count(*) as __$count_6F9F918A 
			from [cdc].[dbo_ThucChayTrueView_CT] r with (nolock)   
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_6F9F918A and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayTrueView', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChayTrueView_CT] c with (nolock) 
							where  ( (c.[id] = t.[id]) )  
							and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
							and (c.__$start_lsn <= @to_lsn)
							and (c.__$start_lsn >= @from_lsn)
							order by c.__$seqval
						 ) 
	 			   )
	 			 )
	 			) 	
	) Q
	
	union all
	
	select __$start_lsn,
	    case __$count_6F9F918A
	    when 1 then __$operation
	    else
			case __$min_op_6F9F918A 
				when 2 then 2
				when 4 then
				case __$operation
					when 1 then 1
					else 4
					end
				else
				case __$operation
					when 2 then 4
					when 4 then 4
					else 1
					end
			end
		end as __$operation,
		case __$count_6F9F918A
		when 1 then
			case __$operation
			when 4 then __$update_mask
			else null
			end
		else	
			case __$min_op_6F9F918A 
			when 2 then null
			else
				case __$operation
				when 1 then null
				else __$update_mask 
				end
			end	
		end as __$update_mask , [SoHopDong], [TypeProduct], [DmSanPhamREF], [TenSanPham], [campaignid], [bannerid], [SiteName], [SiteID], [True_View], [Views], [Clicks], [NgayThucHien], [CreatedBy], [CreatedAt], [LastModifiedBy], [LastModifiedAt], [DeletedStatus], [FormatName], [id]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_6F9F918A 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_ThucChayTrueView_CT] c with (nolock)
			where  ( (c.[id] = t.[id]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_6F9F918A, __$count_6F9F918A, 
		m.__$update_mask , t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[campaignid], t.[bannerid], t.[SiteName], t.[SiteID], t.[True_View], t.[Views], t.[Clicks], t.[NgayThucHien], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[FormatName], t.[id]
		from [cdc].[dbo_ThucChayTrueView_CT] t with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_6F9F918A,
		    count(*) as __$count_6F9F918A, 
		    [sys].[ORMask](r.__$update_mask) as __$update_mask
			from [cdc].[dbo_ThucChayTrueView_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_6F9F918A and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with mask'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayTrueView', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChayTrueView_CT] c with (nolock)
							where  ( (c.[id] = t.[id]) )  
							and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
							and (c.__$start_lsn <= @to_lsn)
							and (c.__$start_lsn >= @from_lsn)
							order by c.__$seqval
						 ) 
	 			   )
	 			 )
	 			) 	
	) Q
	
	union all
	
		select t.__$start_lsn as __$start_lsn,
		case t.__$operation
			when 1 then 1
			else 5
		end as __$operation,
		null as __$update_mask , t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[campaignid], t.[bannerid], t.[SiteName], t.[SiteID], t.[True_View], t.[Views], t.[Clicks], t.[NgayThucHien], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[FormatName], t.[id]
		from [cdc].[dbo_ThucChayTrueView_CT] t  with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_6F9F918A
			from [cdc].[dbo_ThucChayTrueView_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_6F9F918A and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with merge'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayTrueView', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and 
				   (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChayTrueView_CT] c with (nolock)
							where  ( (c.[id] = t.[id]) )  
							and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
							and (c.__$start_lsn <= @to_lsn)
							and (c.__$start_lsn >= @from_lsn)
							order by c.__$seqval
						 ) 
	 				)
	 			 )
	 			)
	 
```
