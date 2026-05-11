# Function: `fn_cdc_get_all_changes_dbo_ThucChayHopDongChiTietPR`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-09-29 00:46:48.510000
- **Ngày sửa cuối**: 2021-09-29 00:46:48.510000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_ThucChayHopDongChiTietPR]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucChayHopDongChiTietPRID], NULL as [HopDongREF], NULL as [HopDongChiTietREF], NULL as [NhanHang], NULL as [TenWebsite], NULL as [ChuyenMuc], NULL as [TieuDiem], NULL as [KhuyenMai], NULL as [GiaTien], NULL as [ThoiGianBatDau], NULL as [Link], NULL as [GhiChu], NULL as [CreatedBy], NULL as [CreatedAt], NULL as [LastModifiedBy], NULL as [LastModifiedAt], NULL as [DeletedStatus], NULL as [PrintStatus], NULL as [RecordStatus], NULL as [DmWebsiteREF], NULL as [DmChuyenMucREF], NULL as [TenChuyenMuc], NULL as [DmNhanHangREF], NULL as [DmHinhThucQuangCaoREF], NULL as [TenHinhThucQuangCao], NULL as [MaLinkBai], NULL as [SoHopDong], NULL as [SoLuong], NULL as [ChietKhau], NULL as [DmViTriREF], NULL as [TenViTri], NULL as [ThucChayHopDongChiTietPrREF], NULL as [DmSanPhamREF], NULL as [DmDonViTinhREF], NULL as [parent_id], NULL as [chuyenmuccms_id]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayHopDongChiTietPR', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChayHopDongChiTietPRID], t.[HopDongREF], t.[HopDongChiTietREF], t.[NhanHang], t.[TenWebsite], t.[ChuyenMuc], t.[TieuDiem], t.[KhuyenMai], t.[GiaTien], t.[ThoiGianBatDau], t.[Link], t.[GhiChu], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[PrintStatus], t.[RecordStatus], t.[DmWebsiteREF], t.[DmChuyenMucREF], t.[TenChuyenMuc], t.[DmNhanHangREF], t.[DmHinhThucQuangCaoREF], t.[TenHinhThucQuangCao], t.[MaLinkBai], t.[SoHopDong], t.[SoLuong], t.[ChietKhau], t.[DmViTriREF], t.[TenViTri], t.[ThucChayHopDongChiTietPrREF], t.[DmSanPhamREF], t.[DmDonViTinhREF], t.[parent_id], t.[chuyenmuccms_id]
	from [cdc].[dbo_ThucChayHopDongChiTietPR_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayHopDongChiTietPR', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChayHopDongChiTietPRID], t.[HopDongREF], t.[HopDongChiTietREF], t.[NhanHang], t.[TenWebsite], t.[ChuyenMuc], t.[TieuDiem], t.[KhuyenMai], t.[GiaTien], t.[ThoiGianBatDau], t.[Link], t.[GhiChu], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[PrintStatus], t.[RecordStatus], t.[DmWebsiteREF], t.[DmChuyenMucREF], t.[TenChuyenMuc], t.[DmNhanHangREF], t.[DmHinhThucQuangCaoREF], t.[TenHinhThucQuangCao], t.[MaLinkBai], t.[SoHopDong], t.[SoLuong], t.[ChietKhau], t.[DmViTriREF], t.[TenViTri], t.[ThucChayHopDongChiTietPrREF], t.[DmSanPhamREF], t.[DmDonViTinhREF], t.[parent_id], t.[chuyenmuccms_id]
	from [cdc].[dbo_ThucChayHopDongChiTietPR_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayHopDongChiTietPR', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
