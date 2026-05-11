# Function: `fn_cdc_get_all_changes_dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:42.840000
- **Ngày sửa cuối**: 2021-08-31 08:38:42.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucTreoHopDongChiTietTrinhDuyetID], NULL as [HopDongREF], NULL as [HopDongChiTietREF], NULL as [DmHinhThucQuangCaoREF], NULL as [DmSanPhamREF], NULL as [TenNhanHang], NULL as [NhanHangREF], NULL as [DmWebsiteREF], NULL as [TenWebsite], NULL as [Soluong], NULL as [DmDonViTinhREF], NULL as [DonViTinh], NULL as [DonGia], NULL as [ChietKhau], NULL as [TongTien], NULL as [NgayBatDau], NULL as [NgayKetThuc], NULL as [TrangThai], NULL as [IsLocked], NULL as [CreatedAt], NULL as [CreatedBy], NULL as [LastModifiedAt], NULL as [LastModifiedBy], NULL as [SubmittedAt], NULL as [SubmittedBy], NULL as [ApprovedAt], NULL as [ApprovedBy], NULL as [Note], NULL as [ThucChayHopDongChiTietREF], NULL as [DeletedStatus], NULL as [Linkbai], NULL as [Lst_NhanVienSoYeuLyLichREF], NULL as [id], NULL as [TenBanner]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucTreoHopDongChiTietTrinhDuyetID], t.[HopDongREF], t.[HopDongChiTietREF], t.[DmHinhThucQuangCaoREF], t.[DmSanPhamREF], t.[TenNhanHang], t.[NhanHangREF], t.[DmWebsiteREF], t.[TenWebsite], t.[Soluong], t.[DmDonViTinhREF], t.[DonViTinh], t.[DonGia], t.[ChietKhau], t.[TongTien], t.[NgayBatDau], t.[NgayKetThuc], t.[TrangThai], t.[IsLocked], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[SubmittedAt], t.[SubmittedBy], t.[ApprovedAt], t.[ApprovedBy], t.[Note], t.[ThucChayHopDongChiTietREF], t.[DeletedStatus], t.[Linkbai], t.[Lst_NhanVienSoYeuLyLichREF], t.[id], t.[TenBanner]
	from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucTreoHopDongChiTietTrinhDuyetID], t.[HopDongREF], t.[HopDongChiTietREF], t.[DmHinhThucQuangCaoREF], t.[DmSanPhamREF], t.[TenNhanHang], t.[NhanHangREF], t.[DmWebsiteREF], t.[TenWebsite], t.[Soluong], t.[DmDonViTinhREF], t.[DonViTinh], t.[DonGia], t.[ChietKhau], t.[TongTien], t.[NgayBatDau], t.[NgayKetThuc], t.[TrangThai], t.[IsLocked], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[SubmittedAt], t.[SubmittedBy], t.[ApprovedAt], t.[ApprovedBy], t.[Note], t.[ThucChayHopDongChiTietREF], t.[DeletedStatus], t.[Linkbai], t.[Lst_NhanVienSoYeuLyLichREF], t.[id], t.[TenBanner]
	from [cdc].[dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
