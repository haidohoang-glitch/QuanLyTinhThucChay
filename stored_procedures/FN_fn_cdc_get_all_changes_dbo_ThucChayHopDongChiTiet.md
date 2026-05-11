# Function: `fn_cdc_get_all_changes_dbo_ThucChayHopDongChiTiet`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:39.580000
- **Ngày sửa cuối**: 2021-08-31 08:38:39.580000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_ThucChayHopDongChiTiet]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucChayHopDongChiTietID], NULL as [HopDongREF], NULL as [NhanHang], NULL as [ThoiGianBatDau], NULL as [ThoiGianKetThuc], NULL as [Link], NULL as [DmBannerREF], NULL as [TenBanner], NULL as [ViTri], NULL as [GhiChu], NULL as [BookingREF], NULL as [HopDongChiTietREF], NULL as [TypeThucChay], NULL as [CreatedBy], NULL as [CreatedAt], NULL as [LastModifiedBy], NULL as [LastModifiedAt], NULL as [DeletedStatus], NULL as [PrintStatus], NULL as [RecordStatus], NULL as [DmViTriREF], NULL as [DmNhanHangREF], NULL as [SoLuongThucTreo], NULL as [SoLuongThucChay], NULL as [DmDonViTinhREF], NULL as [DonViTinh], NULL as [DmHinhThucQuangCaoREF], NULL as [TenHinhThucQuangCao], NULL as [DmSanPhamREF], NULL as [TenSanPham], NULL as [InputType], NULL as [IsReadBooking], NULL as [KichThuoc], NULL as [DonGia], NULL as [ChietKhau], NULL as [ThanhTien], NULL as [Id], NULL as [LoaiThucTreo]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayHopDongChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChayHopDongChiTietID], t.[HopDongREF], t.[NhanHang], t.[ThoiGianBatDau], t.[ThoiGianKetThuc], t.[Link], t.[DmBannerREF], t.[TenBanner], t.[ViTri], t.[GhiChu], t.[BookingREF], t.[HopDongChiTietREF], t.[TypeThucChay], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[PrintStatus], t.[RecordStatus], t.[DmViTriREF], t.[DmNhanHangREF], t.[SoLuongThucTreo], t.[SoLuongThucChay], t.[DmDonViTinhREF], t.[DonViTinh], t.[DmHinhThucQuangCaoREF], t.[TenHinhThucQuangCao], t.[DmSanPhamREF], t.[TenSanPham], t.[InputType], t.[IsReadBooking], t.[KichThuoc], t.[DonGia], t.[ChietKhau], t.[ThanhTien], t.[Id], t.[LoaiThucTreo]
	from [cdc].[dbo_ThucChayHopDongChiTiet_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayHopDongChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChayHopDongChiTietID], t.[HopDongREF], t.[NhanHang], t.[ThoiGianBatDau], t.[ThoiGianKetThuc], t.[Link], t.[DmBannerREF], t.[TenBanner], t.[ViTri], t.[GhiChu], t.[BookingREF], t.[HopDongChiTietREF], t.[TypeThucChay], t.[CreatedBy], t.[CreatedAt], t.[LastModifiedBy], t.[LastModifiedAt], t.[DeletedStatus], t.[PrintStatus], t.[RecordStatus], t.[DmViTriREF], t.[DmNhanHangREF], t.[SoLuongThucTreo], t.[SoLuongThucChay], t.[DmDonViTinhREF], t.[DonViTinh], t.[DmHinhThucQuangCaoREF], t.[TenHinhThucQuangCao], t.[DmSanPhamREF], t.[TenSanPham], t.[InputType], t.[IsReadBooking], t.[KichThuoc], t.[DonGia], t.[ChietKhau], t.[ThanhTien], t.[Id], t.[LoaiThucTreo]
	from [cdc].[dbo_ThucChayHopDongChiTiet_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayHopDongChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
