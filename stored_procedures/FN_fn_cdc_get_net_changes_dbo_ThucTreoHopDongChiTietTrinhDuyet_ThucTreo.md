# Function: `fn_cdc_get_net_changes_dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:42.857000
- **Ngày sửa cuối**: 2021-08-31 08:38:42.857000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_net_changes_dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return

	select NULL as __$start_lsn,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucTreoHopDongChiTietTrinhDuyetID], NULL as [HopDongREF], NULL as [HopDongChiTietREF], NULL as [DmHinhThucQuangCaoREF], NULL as [DmSanPhamREF], NULL as [TenNhanHang], NULL as [NhanHangREF], NULL as [DmWebsiteREF], NULL as [TenWebsite], NULL as [Soluong], NULL as [DmDonViTinhREF], NULL as [DonViTinh], NULL as [DonGia], NULL as [ChietKhau], NULL as [TongTien], NULL as [NgayBatDau], NULL as [NgayKetThuc], NULL as [TrangThai], NULL as [IsLocked], NULL as [CreatedAt], NULL as [CreatedBy], NULL as [LastModifiedAt], NULL as [LastModifiedBy], NULL as [SubmittedAt], NULL as [SubmittedBy], NULL as [ApprovedAt], NULL as [ApprovedBy], NULL as [Note], NULL as [ThucChayHopDongChiTietREF], NULL as [DeletedStatus], NULL as [Linkbai], NULL as [Lst_NhanVienSoYeuLyLichREF], NULL as [id], NULL as [TenBanner]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 0)

	union all
	
	select __$start_lsn,
	    case __$count_2254E15E
	    when 1 then __$operation
	    else
			case __$min_op_2254E15E 
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
		null as __$update_mask , [ThucTreoHopDongChiTietTrinhDuyetID], [HopDongREF], [HopDongChiTietREF], [DmHinhThucQuangCaoREF], [DmSanPhamREF], [TenNhanHang], [NhanHangREF], [DmWebsiteREF], [TenWebsite], [Soluong], [DmDonViTinhREF], [DonViTinh], [DonGia], [ChietKhau], [TongTien], [NgayBatDau], [NgayKetThuc], [TrangThai], [IsLocked], [CreatedAt], [CreatedBy], [LastModifiedAt], [LastModifiedBy], [SubmittedAt], [SubmittedBy], [ApprovedAt], [ApprovedBy], [Note], [ThucChayHopDongChiTietREF], [DeletedStatus], [Linkbai], [Lst_NhanVienSoYeuLyLichREF], [id], [TenBanner]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_2254E15E 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] c with (nolock)   
			where  ( (c.[id] = t.[id]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_2254E15E, __$count_2254E15E, t.[ThucTreoHopDongChiTietTrinhDuyetID], t.[HopDongREF], t.[HopDongChiTietREF], t.[DmHinhThucQuangCaoREF], t.[DmSanPhamREF], t.[TenNhanHang], t.[NhanHangREF], t.[DmWebsiteREF], t.[TenWebsite], t.[Soluong], t.[DmDonViTinhREF], t.[DonViTinh], t.[DonGia], t.[ChietKhau], t.[TongTien], t.[NgayBatDau], t.[NgayKetThuc], t.[TrangThai], t.[IsLocked], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[SubmittedAt], t.[SubmittedBy], t.[ApprovedAt], t.[ApprovedBy], t.[Note], t.[ThucChayHopDongChiTietREF], t.[DeletedStatus], t.[Linkbai], t.[Lst_NhanVienSoYeuLyLichREF], t.[id], t.[TenBanner] 
		from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] t with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_2254E15E,
		    count(*) as __$count_2254E15E 
			from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] r with (nolock)   
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_2254E15E and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] c with (nolock) 
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
	    case __$count_2254E15E
	    when 1 then __$operation
	    else
			case __$min_op_2254E15E 
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
		case __$count_2254E15E
		when 1 then
			case __$operation
			when 4 then __$update_mask
			else null
			end
		else	
			case __$min_op_2254E15E 
			when 2 then null
			else
				case __$operation
				when 1 then null
				else __$update_mask 
				end
			end	
		end as __$update_mask , [ThucTreoHopDongChiTietTrinhDuyetID], [HopDongREF], [HopDongChiTietREF], [DmHinhThucQuangCaoREF], [DmSanPhamREF], [TenNhanHang], [NhanHangREF], [DmWebsiteREF], [TenWebsite], [Soluong], [DmDonViTinhREF], [DonViTinh], [DonGia], [ChietKhau], [TongTien], [NgayBatDau], [NgayKetThuc], [TrangThai], [IsLocked], [CreatedAt], [CreatedBy], [LastModifiedAt], [LastModifiedBy], [SubmittedAt], [SubmittedBy], [ApprovedAt], [ApprovedBy], [Note], [ThucChayHopDongChiTietREF], [DeletedStatus], [Linkbai], [Lst_NhanVienSoYeuLyLichREF], [id], [TenBanner]
	from
	(
		select t.__$start_lsn as __$start_lsn, __$operation,
		case __$count_2254E15E 
		when 1 then __$operation 
		else
		(	select top 1 c.__$operation
			from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] c with (nolock)
			where  ( (c.[id] = t.[id]) )  
			and ((c.__$operation = 2) or (c.__$operation = 4) or (c.__$operation = 1))
			and (c.__$start_lsn <= @to_lsn)
			and (c.__$start_lsn >= @from_lsn)
			order by c.__$seqval) end __$min_op_2254E15E, __$count_2254E15E, 
		m.__$update_mask , t.[ThucTreoHopDongChiTietTrinhDuyetID], t.[HopDongREF], t.[HopDongChiTietREF], t.[DmHinhThucQuangCaoREF], t.[DmSanPhamREF], t.[TenNhanHang], t.[NhanHangREF], t.[DmWebsiteREF], t.[TenWebsite], t.[Soluong], t.[DmDonViTinhREF], t.[DonViTinh], t.[DonGia], t.[ChietKhau], t.[TongTien], t.[NgayBatDau], t.[NgayKetThuc], t.[TrangThai], t.[IsLocked], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[SubmittedAt], t.[SubmittedBy], t.[ApprovedAt], t.[ApprovedBy], t.[Note], t.[ThucChayHopDongChiTietREF], t.[DeletedStatus], t.[Linkbai], t.[Lst_NhanVienSoYeuLyLichREF], t.[id], t.[TenBanner]
		from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] t with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_2254E15E,
		    count(*) as __$count_2254E15E, 
		    [sys].[ORMask](r.__$update_mask) as __$update_mask
			from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_2254E15E and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with mask'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and
				  (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] c with (nolock)
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
		null as __$update_mask , t.[ThucTreoHopDongChiTietTrinhDuyetID], t.[HopDongREF], t.[HopDongChiTietREF], t.[DmHinhThucQuangCaoREF], t.[DmSanPhamREF], t.[TenNhanHang], t.[NhanHangREF], t.[DmWebsiteREF], t.[TenWebsite], t.[Soluong], t.[DmDonViTinhREF], t.[DonViTinh], t.[DonGia], t.[ChietKhau], t.[TongTien], t.[NgayBatDau], t.[NgayKetThuc], t.[TrangThai], t.[IsLocked], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[SubmittedAt], t.[SubmittedBy], t.[ApprovedAt], t.[ApprovedBy], t.[Note], t.[ThucChayHopDongChiTietREF], t.[DeletedStatus], t.[Linkbai], t.[Lst_NhanVienSoYeuLyLichREF], t.[id], t.[TenBanner]
		from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] t  with (nolock) inner join 
		(	select  r.[id], max(r.__$seqval) as __$max_seqval_2254E15E
			from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] r with (nolock)
			where  (r.__$start_lsn <= @to_lsn)
			and (r.__$start_lsn >= @from_lsn)
			group by   r.[id]) m
		on t.__$seqval = m.__$max_seqval_2254E15E and
		    ( (t.[id] = m.[id]) ) 	
		where lower(rtrim(ltrim(@row_filter_option))) = N'all with merge'
			and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 1) = 1)
			and (t.__$start_lsn <= @to_lsn)
			and (t.__$start_lsn >= @from_lsn)
			and ((t.__$operation = 2) or (t.__$operation = 4) or 
				 ((t.__$operation = 1) and 
				   (2 not in 
				 		(	select top 1 c.__$operation
							from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] c with (nolock)
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
