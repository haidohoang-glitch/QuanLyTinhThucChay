# Function: `fn_cdc_get_net_changes_dbo_ThucChayMuaNgoaiChiTiet`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:40.180000
- **Ngày sửa cuối**: 2021-08-31 08:38:40.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_net_changes_dbo_ThucChayMuaNgoaiChiTiet]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return

	select NULL as __$start_lsn,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucChayMuaNgoaiChiTietID], NULL as [HopDongREF], NULL as [HopDongChiTietREF], NULL as [TuNgay], NULL as [DenNgay], NULL as [NgayThucChay], NULL as [SoLuongThucChay], NULL as [DmDonViTinhREF], NULL as [ChietKhauMuaNgoai], NULL as [ThanhTienMuaNgoaiTruocCK], NULL as [ThanhTienThucChayBanSauCK], NULL as [ThanhTienLaiThucChaySauCK], NULL as [CreatedAt], NULL as [CreatedBy], NULL as [LastModifiedAt], NULL as [LastModifiedBy], NULL as [Status], NULL as [DeletedStatus], NULL as [TrangThaiTinhThucChay], NULL as [id], NULL as [NgayDuyet], NULL as [NguoiDuyet], NULL as [NgayChot], NULL as [NguoiChot]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayMuaNgoaiChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 0)

	union all
	
	select __$start_lsn,
	    case __$count_9E2E0608
	    when 1 then __$operation
	    else
			case __$min_op_9E2E0608 
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
		null as __$update_mask , [ThucChayMuaNgoaiChiTietID], [HopDongREF], [HopDongChiTietREF], [TuNgay], [DenNgay], [NgayThucChay], [SoLuongThucChay], [DmDonViTinhREF], [ChietKhauMuaNgoai], [ThanhTienMuaNgoaiTruocCK], [ThanhTienThucChayBanSauCK], [ThanhTienLaiThucChaySauCK], [CreatedAt], [CreatedBy], [LastModifiedAt], [LastModifiedBy], [Status], [DeletedStatus], [TrangThaiTinhThucChay], [id], [NgayDuyet], [NguoiDuyet], [NgayChot], [NguoiChot]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_9E2E0608 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] c with (nolock)   
			where  ( (c.[id] = t.[id]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_9E2E0608, __$count_9E2E0608, t.[ThucChayMuaNgoaiChiTietID], t.[HopDongREF], t.[HopDongChiTietREF], t.[TuNgay], t.[DenNgay], t.[NgayThucChay], t.[SoLuongThucChay], t.[DmDonViTinhREF], t.[ChietKhauMuaNgoai], t.[ThanhTienMuaNgoaiTruocCK], t.[ThanhTienThucChayBanSauCK], t.[ThanhTienLaiThucChaySauCK], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[Status], t.[DeletedStatus], t.[TrangThaiTinhThucChay], t.[id], t.[NgayDuyet], t.[NguoiDuyet], t.[NgayChot], t.[NguoiChot] 
		from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] t with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_9E2E0608,
		    count(*) as __$count_9E2E0608 
			from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] r with (nolock)   
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_9E2E0608 and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayMuaNgoaiChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] c with (nolock) 
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
	    case __$count_9E2E0608
	    when 1 then __$operation
	    else
			case __$min_op_9E2E0608 
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
		case __$count_9E2E0608
		when 1 then
			case __$operation
			when 4 then __$update_mask
			else null
			end
		else	
			case __$min_op_9E2E0608 
			when 2 then null
			else
				case __$operation
				when 1 then null
				else __$update_mask 
				end
			end	
		end as __$update_mask , [ThucChayMuaNgoaiChiTietID], [HopDongREF], [HopDongChiTietREF], [TuNgay], [DenNgay], [NgayThucChay], [SoLuongThucChay], [DmDonViTinhREF], [ChietKhauMuaNgoai], [ThanhTienMuaNgoaiTruocCK], [ThanhTienThucChayBanSauCK], [ThanhTienLaiThucChaySauCK], [CreatedAt], [CreatedBy], [LastModifiedAt], [LastModifiedBy], [Status], [DeletedStatus], [TrangThaiTinhThucChay], [id], [NgayDuyet], [NguoiDuyet], [NgayChot], [NguoiChot]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_9E2E0608 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] c with (nolock)
			where  ( (c.[id] = t.[id]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_9E2E0608, __$count_9E2E0608, 
		m.__$update_mask , t.[ThucChayMuaNgoaiChiTietID], t.[HopDongREF], t.[HopDongChiTietREF], t.[TuNgay], t.[DenNgay], t.[NgayThucChay], t.[SoLuongThucChay], t.[DmDonViTinhREF], t.[ChietKhauMuaNgoai], t.[ThanhTienMuaNgoaiTruocCK], t.[ThanhTienThucChayBanSauCK], t.[ThanhTienLaiThucChaySauCK], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[Status], t.[DeletedStatus], t.[TrangThaiTinhThucChay], t.[id], t.[NgayDuyet], t.[NguoiDuyet], t.[NgayChot], t.[NguoiChot]
		from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] t with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_9E2E0608,
		    count(*) as __$count_9E2E0608, 
		    [sys].[ORMask](r.__$update_mask) as __$update_mask
			from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_9E2E0608 and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with mask'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayMuaNgoaiChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] c with (nolock)
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
		null as __$update_mask , t.[ThucChayMuaNgoaiChiTietID], t.[HopDongREF], t.[HopDongChiTietREF], t.[TuNgay], t.[DenNgay], t.[NgayThucChay], t.[SoLuongThucChay], t.[DmDonViTinhREF], t.[ChietKhauMuaNgoai], t.[ThanhTienMuaNgoaiTruocCK], t.[ThanhTienThucChayBanSauCK], t.[ThanhTienLaiThucChaySauCK], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[Status], t.[DeletedStatus], t.[TrangThaiTinhThucChay], t.[id], t.[NgayDuyet], t.[NguoiDuyet], t.[NgayChot], t.[NguoiChot]
		from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] t  with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_9E2E0608
			from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_9E2E0608 and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with merge'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayMuaNgoaiChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and 
				   (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] c with (nolock)
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
