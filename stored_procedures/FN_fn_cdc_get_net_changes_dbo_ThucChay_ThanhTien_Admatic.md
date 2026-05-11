# Function: `fn_cdc_get_net_changes_dbo_ThucChay_ThanhTien_Admatic`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2023-08-07 14:19:32.833000
- **Ngày sửa cuối**: 2023-08-07 14:19:32.833000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_net_changes_dbo_ThucChay_ThanhTien_Admatic]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return

	select NULL as __$start_lsn,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucChay_ThanhTien_AdmaticID], NULL as [SoHopDong], NULL as [TypeProduct], NULL as [DmSanPhamREF], NULL as [TenSanPham], NULL as [TenNhanHang], NULL as [DmNhanHangREF], NULL as [DmBannerID], NULL as [DmWebsiteID], NULL as [TenWebsite], NULL as [DmViTriBannerSanPhamID], NULL as [TenViTriBannerSanPham], NULL as [SoLuongThucChay], NULL as [SoLuongThucChayKM], NULL as [DonViTinh], NULL as [ThanhTienThucChaySauCK_ChuaVAT], NULL as [ThanhTienThucChayKM], NULL as [NgayThucHien], NULL as [CreatedAt], NULL as [CreatedBy], NULL as [LastModifiedAt], NULL as [LastModifiedBy], NULL as [DeletedStatus]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay_ThanhTien_Admatic', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 0)

	union all
	
	select __$start_lsn,
	    case __$count_7B4DFFDA
	    when 1 then __$operation
	    else
			case __$min_op_7B4DFFDA 
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
		null as __$update_mask , [ThucChay_ThanhTien_AdmaticID], [SoHopDong], [TypeProduct], [DmSanPhamREF], [TenSanPham], [TenNhanHang], [DmNhanHangREF], [DmBannerID], [DmWebsiteID], [TenWebsite], [DmViTriBannerSanPhamID], [TenViTriBannerSanPham], [SoLuongThucChay], [SoLuongThucChayKM], [DonViTinh], [ThanhTienThucChaySauCK_ChuaVAT], [ThanhTienThucChayKM], [NgayThucHien], [CreatedAt], [CreatedBy], [LastModifiedAt], [LastModifiedBy], [DeletedStatus]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_7B4DFFDA 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] c with (nolock)   
			where  ( (c.[ThucChay_ThanhTien_AdmaticID] = t.[ThucChay_ThanhTien_AdmaticID]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_7B4DFFDA, __$count_7B4DFFDA, t.[ThucChay_ThanhTien_AdmaticID], t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[TenNhanHang], t.[DmNhanHangREF], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriBannerSanPhamID], t.[TenViTriBannerSanPham], t.[SoLuongThucChay], t.[SoLuongThucChayKM], t.[DonViTinh], t.[ThanhTienThucChaySauCK_ChuaVAT], t.[ThanhTienThucChayKM], t.[NgayThucHien], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[DeletedStatus] 
		from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] t with (nolock) inner join 
		(	select  r.[ThucChay_ThanhTien_AdmaticID], max(r.__$seqval) as __$max_seqval_7B4DFFDA,
		    count(*) as __$count_7B4DFFDA 
			from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] r with (nolock)   
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[ThucChay_ThanhTien_AdmaticID]) m
		on t.__$seqval = m.__$max_seqval_7B4DFFDA and
		    ( (t.[ThucChay_ThanhTien_AdmaticID] = m.[ThucChay_ThanhTien_AdmaticID]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay_ThanhTien_Admatic', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] c with (nolock) 
							where  ( (c.[ThucChay_ThanhTien_AdmaticID] = t.[ThucChay_ThanhTien_AdmaticID]) )  
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
	    case __$count_7B4DFFDA
	    when 1 then __$operation
	    else
			case __$min_op_7B4DFFDA 
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
		case __$count_7B4DFFDA
		when 1 then
			case __$operation
			when 4 then __$update_mask
			else null
			end
		else	
			case __$min_op_7B4DFFDA 
			when 2 then null
			else
				case __$operation
				when 1 then null
				else __$update_mask 
				end
			end	
		end as __$update_mask , [ThucChay_ThanhTien_AdmaticID], [SoHopDong], [TypeProduct], [DmSanPhamREF], [TenSanPham], [TenNhanHang], [DmNhanHangREF], [DmBannerID], [DmWebsiteID], [TenWebsite], [DmViTriBannerSanPhamID], [TenViTriBannerSanPham], [SoLuongThucChay], [SoLuongThucChayKM], [DonViTinh], [ThanhTienThucChaySauCK_ChuaVAT], [ThanhTienThucChayKM], [NgayThucHien], [CreatedAt], [CreatedBy], [LastModifiedAt], [LastModifiedBy], [DeletedStatus]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_7B4DFFDA 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] c with (nolock)
			where  ( (c.[ThucChay_ThanhTien_AdmaticID] = t.[ThucChay_ThanhTien_AdmaticID]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_7B4DFFDA, __$count_7B4DFFDA, 
		m.__$update_mask , t.[ThucChay_ThanhTien_AdmaticID], t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[TenNhanHang], t.[DmNhanHangREF], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriBannerSanPhamID], t.[TenViTriBannerSanPham], t.[SoLuongThucChay], t.[SoLuongThucChayKM], t.[DonViTinh], t.[ThanhTienThucChaySauCK_ChuaVAT], t.[ThanhTienThucChayKM], t.[NgayThucHien], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[DeletedStatus]
		from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] t with (nolock) inner join 
		(	select  r.[ThucChay_ThanhTien_AdmaticID], max(r.__$seqval) as __$max_seqval_7B4DFFDA,
		    count(*) as __$count_7B4DFFDA, 
		    [sys].[ORMask](r.__$update_mask) as __$update_mask
			from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[ThucChay_ThanhTien_AdmaticID]) m
		on t.__$seqval = m.__$max_seqval_7B4DFFDA and
		    ( (t.[ThucChay_ThanhTien_AdmaticID] = m.[ThucChay_ThanhTien_AdmaticID]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with mask'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay_ThanhTien_Admatic', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] c with (nolock)
							where  ( (c.[ThucChay_ThanhTien_AdmaticID] = t.[ThucChay_ThanhTien_AdmaticID]) )  
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
		null as __$update_mask , t.[ThucChay_ThanhTien_AdmaticID], t.[SoHopDong], t.[TypeProduct], t.[DmSanPhamREF], t.[TenSanPham], t.[TenNhanHang], t.[DmNhanHangREF], t.[DmBannerID], t.[DmWebsiteID], t.[TenWebsite], t.[DmViTriBannerSanPhamID], t.[TenViTriBannerSanPham], t.[SoLuongThucChay], t.[SoLuongThucChayKM], t.[DonViTinh], t.[ThanhTienThucChaySauCK_ChuaVAT], t.[ThanhTienThucChayKM], t.[NgayThucHien], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[DeletedStatus]
		from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] t  with (nolock) inner join 
		(	select  r.[ThucChay_ThanhTien_AdmaticID], max(r.__$seqval) as __$max_seqval_7B4DFFDA
			from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[ThucChay_ThanhTien_AdmaticID]) m
		on t.__$seqval = m.__$max_seqval_7B4DFFDA and
		    ( (t.[ThucChay_ThanhTien_AdmaticID] = m.[ThucChay_ThanhTien_AdmaticID]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with merge'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChay_ThanhTien_Admatic', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and 
				   (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucChay_ThanhTien_Admatic_CT] c with (nolock)
							where  ( (c.[ThucChay_ThanhTien_AdmaticID] = t.[ThucChay_ThanhTien_AdmaticID]) )  
							and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
							and (c.__$start_lsn <= @to_lsn)
							and (c.__$start_lsn >= @from_lsn)
							order by c.__$seqval
						 ) 
	 				)
	 			 )
	 			)
	 
```
