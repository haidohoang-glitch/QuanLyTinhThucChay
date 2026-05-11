# Function: `fn_cdc_get_net_changes_dbo_DataThucchay_Native_Ads`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2023-06-29 22:31:15.017000
- **Ngày sửa cuối**: 2023-06-29 22:31:15.017000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_net_changes_dbo_DataThucchay_Native_Ads]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return

	select NULL as __$start_lsn,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [SoHopDong], NULL as [TypeProduct], NULL as [TenSanPham], NULL as [TenNhanHang], NULL as [NhanHangID], NULL as [DmBannerID], NULL as [DmWebsiteID], NULL as [TenWebsite], NULL as [DmViTriREF], NULL as [TenViTri], NULL as [SoLuongThucChay], NULL as [SoLuongThucChayKhuyenMai], NULL as [DonViTinh], NULL as [ThanhTienThucChay], NULL as [ThanhTienThucChaykhuyenMai], NULL as [NgayThucHien], NULL as [createdBy], NULL as [createdAt], NULL as [id], NULL as [DmCampaignID], NULL as [VAT]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_DataThucchay_Native_Ads', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 0)

	union all
	
	select __$start_lsn,
	    case __$count_1FA0EFDE
	    when 1 then __$operation
	    else
			case __$min_op_1FA0EFDE 
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
		null as __$update_mask , [SoHopDong], [TypeProduct], [TenSanPham], [TenNhanHang], [NhanHangID], [DmBannerID], [DmWebsiteID], [TenWebsite], [DmViTriREF], [TenViTri], [SoLuongThucChay], [SoLuongThucChayKhuyenMai], [DonViTinh], [ThanhTienThucChay], [ThanhTienThucChaykhuyenMai], [NgayThucHien], [createdBy], [createdAt], [id], [DmCampaignID], [VAT]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_1FA0EFDE 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_DataThucchay_Native_Ads_CT] c with (nolock)   
			where  ( (c.[id] = t.[id]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_1FA0EFDE, __$count_1FA0EFDE, t.[SoHopDong], t.[TypeProduct], t.[TenSanPham], t.[TenNhanHang], t.[NhanHangID], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriREF], t.[TenViTri], t.[SoLuongThucChay], t.[SoLuongThucChayKhuyenMai], t.[DonViTinh], t.[ThanhTienThucChay], t.[ThanhTienThucChaykhuyenMai], t.[NgayThucHien], t.[createdBy], t.[createdAt], t.[id], t.[DmCampaignID], t.[VAT] 
		from [cdc].[dbo_DataThucchay_Native_Ads_CT] t with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_1FA0EFDE,
		    count(*) as __$count_1FA0EFDE 
			from [cdc].[dbo_DataThucchay_Native_Ads_CT] r with (nolock)   
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_1FA0EFDE and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_DataThucchay_Native_Ads', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_DataThucchay_Native_Ads_CT] c with (nolock) 
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
	    case __$count_1FA0EFDE
	    when 1 then __$operation
	    else
			case __$min_op_1FA0EFDE 
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
		case __$count_1FA0EFDE
		when 1 then
			case __$operation
			when 4 then __$update_mask
			else null
			end
		else	
			case __$min_op_1FA0EFDE 
			when 2 then null
			else
				case __$operation
				when 1 then null
				else __$update_mask 
				end
			end	
		end as __$update_mask , [SoHopDong], [TypeProduct], [TenSanPham], [TenNhanHang], [NhanHangID], [DmBannerID], [DmWebsiteID], [TenWebsite], [DmViTriREF], [TenViTri], [SoLuongThucChay], [SoLuongThucChayKhuyenMai], [DonViTinh], [ThanhTienThucChay], [ThanhTienThucChaykhuyenMai], [NgayThucHien], [createdBy], [createdAt], [id], [DmCampaignID], [VAT]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_1FA0EFDE 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_DataThucchay_Native_Ads_CT] c with (nolock)
			where  ( (c.[id] = t.[id]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_1FA0EFDE, __$count_1FA0EFDE, 
		m.__$update_mask , t.[SoHopDong], t.[TypeProduct], t.[TenSanPham], t.[TenNhanHang], t.[NhanHangID], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriREF], t.[TenViTri], t.[SoLuongThucChay], t.[SoLuongThucChayKhuyenMai], t.[DonViTinh], t.[ThanhTienThucChay], t.[ThanhTienThucChaykhuyenMai], t.[NgayThucHien], t.[createdBy], t.[createdAt], t.[id], t.[DmCampaignID], t.[VAT]
		from [cdc].[dbo_DataThucchay_Native_Ads_CT] t with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_1FA0EFDE,
		    count(*) as __$count_1FA0EFDE, 
		    [sys].[ORMask](r.__$update_mask) as __$update_mask
			from [cdc].[dbo_DataThucchay_Native_Ads_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_1FA0EFDE and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with mask'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_DataThucchay_Native_Ads', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_DataThucchay_Native_Ads_CT] c with (nolock)
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
		null as __$update_mask , t.[SoHopDong], t.[TypeProduct], t.[TenSanPham], t.[TenNhanHang], t.[NhanHangID], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriREF], t.[TenViTri], t.[SoLuongThucChay], t.[SoLuongThucChayKhuyenMai], t.[DonViTinh], t.[ThanhTienThucChay], t.[ThanhTienThucChaykhuyenMai], t.[NgayThucHien], t.[createdBy], t.[createdAt], t.[id], t.[DmCampaignID], t.[VAT]
		from [cdc].[dbo_DataThucchay_Native_Ads_CT] t  with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_1FA0EFDE
			from [cdc].[dbo_DataThucchay_Native_Ads_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_1FA0EFDE and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with merge'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_DataThucchay_Native_Ads', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and 
				   (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_DataThucchay_Native_Ads_CT] c with (nolock)
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
