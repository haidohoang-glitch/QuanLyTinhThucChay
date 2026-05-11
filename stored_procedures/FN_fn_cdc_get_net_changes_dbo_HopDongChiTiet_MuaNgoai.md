# Function: `fn_cdc_get_net_changes_dbo_HopDongChiTiet_MuaNgoai`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:44.527000
- **Ngày sửa cuối**: 2021-08-31 08:38:44.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_net_changes_dbo_HopDongChiTiet_MuaNgoai]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return

	select NULL as __$start_lsn,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [HopDongChiTietID], NULL as [SoHopDongMua], NULL as [DonGiaMua], NULL as [SoLuongMua], NULL as [DonViTinh], NULL as [SoLuongText], NULL as [ChietKhauMua], NULL as [ThanhTienSauCKMua], NULL as [VAT], NULL as [AttachFile], NULL as [CreatedAt], NULL as [CreatedBy], NULL as [LastModifiedAt], NULL as [LastModifiedBy], NULL as [DeletedStatus], NULL as [ThanhTienBanSauCK], NULL as [ThanhTienLaiSauCK], NULL as [ID]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_HopDongChiTiet_MuaNgoai', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 0)

	union all
	
	select __$start_lsn,
	    case __$count_5B11C2F8
	    when 1 then __$operation
	    else
			case __$min_op_5B11C2F8 
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
		null as __$update_mask , [HopDongChiTietID], [SoHopDongMua], [DonGiaMua], [SoLuongMua], [DonViTinh], [SoLuongText], [ChietKhauMua], [ThanhTienSauCKMua], [VAT], [AttachFile], [CreatedAt], [CreatedBy], [LastModifiedAt], [LastModifiedBy], [DeletedStatus], [ThanhTienBanSauCK], [ThanhTienLaiSauCK], [ID]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_5B11C2F8 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] c with (nolock)   
			where  ( (c.[ID] = t.[ID]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_5B11C2F8, __$count_5B11C2F8, t.[HopDongChiTietID], t.[SoHopDongMua], t.[DonGiaMua], t.[SoLuongMua], t.[DonViTinh], t.[SoLuongText], t.[ChietKhauMua], t.[ThanhTienSauCKMua], t.[VAT], t.[AttachFile], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[DeletedStatus], t.[ThanhTienBanSauCK], t.[ThanhTienLaiSauCK], t.[ID] 
		from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] t with (nolock) inner join 
		(	select  r.[ID], max(r.__$seqval) as __$max_seqval_5B11C2F8,
		    count(*) as __$count_5B11C2F8 
			from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] r with (nolock)   
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[ID]) m
		on t.__$seqval = m.__$max_seqval_5B11C2F8 and
		    ( (t.[ID] = m.[ID]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_HopDongChiTiet_MuaNgoai', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] c with (nolock) 
							where  ( (c.[ID] = t.[ID]) )  
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
	    case __$count_5B11C2F8
	    when 1 then __$operation
	    else
			case __$min_op_5B11C2F8 
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
		case __$count_5B11C2F8
		when 1 then
			case __$operation
			when 4 then __$update_mask
			else null
			end
		else	
			case __$min_op_5B11C2F8 
			when 2 then null
			else
				case __$operation
				when 1 then null
				else __$update_mask 
				end
			end	
		end as __$update_mask , [HopDongChiTietID], [SoHopDongMua], [DonGiaMua], [SoLuongMua], [DonViTinh], [SoLuongText], [ChietKhauMua], [ThanhTienSauCKMua], [VAT], [AttachFile], [CreatedAt], [CreatedBy], [LastModifiedAt], [LastModifiedBy], [DeletedStatus], [ThanhTienBanSauCK], [ThanhTienLaiSauCK], [ID]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_5B11C2F8 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] c with (nolock)
			where  ( (c.[ID] = t.[ID]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_5B11C2F8, __$count_5B11C2F8, 
		m.__$update_mask , t.[HopDongChiTietID], t.[SoHopDongMua], t.[DonGiaMua], t.[SoLuongMua], t.[DonViTinh], t.[SoLuongText], t.[ChietKhauMua], t.[ThanhTienSauCKMua], t.[VAT], t.[AttachFile], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[DeletedStatus], t.[ThanhTienBanSauCK], t.[ThanhTienLaiSauCK], t.[ID]
		from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] t with (nolock) inner join 
		(	select  r.[ID], max(r.__$seqval) as __$max_seqval_5B11C2F8,
		    count(*) as __$count_5B11C2F8, 
		    [sys].[ORMask](r.__$update_mask) as __$update_mask
			from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[ID]) m
		on t.__$seqval = m.__$max_seqval_5B11C2F8 and
		    ( (t.[ID] = m.[ID]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with mask'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_HopDongChiTiet_MuaNgoai', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] c with (nolock)
							where  ( (c.[ID] = t.[ID]) )  
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
		null as __$update_mask , t.[HopDongChiTietID], t.[SoHopDongMua], t.[DonGiaMua], t.[SoLuongMua], t.[DonViTinh], t.[SoLuongText], t.[ChietKhauMua], t.[ThanhTienSauCKMua], t.[VAT], t.[AttachFile], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[DeletedStatus], t.[ThanhTienBanSauCK], t.[ThanhTienLaiSauCK], t.[ID]
		from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] t  with (nolock) inner join 
		(	select  r.[ID], max(r.__$seqval) as __$max_seqval_5B11C2F8
			from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[ID]) m
		on t.__$seqval = m.__$max_seqval_5B11C2F8 and
		    ( (t.[ID] = m.[ID]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with merge'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_HopDongChiTiet_MuaNgoai', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and 
				   (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_HopDongChiTiet_MuaNgoai_CT] c with (nolock)
							where  ( (c.[ID] = t.[ID]) )  
							and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
							and (c.__$start_lsn <= @to_lsn)
							and (c.__$start_lsn >= @from_lsn)
							order by c.__$seqval
						 ) 
	 				)
	 			 )
	 			)
	 
```
