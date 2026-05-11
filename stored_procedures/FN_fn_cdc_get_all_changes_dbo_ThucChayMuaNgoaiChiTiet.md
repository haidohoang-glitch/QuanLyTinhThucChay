# Function: `fn_cdc_get_all_changes_dbo_ThucChayMuaNgoaiChiTiet`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2021-08-31 08:38:40.163000
- **Ngày sửa cuối**: 2021-08-31 08:38:40.163000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@from_lsn` | `binary(10)` | No |
| `@to_lsn` | `binary(10)` | No |
| `@row_filter_option` | `nvarchar(60)` | No |

## Definition (Source Code)

```sql

	create function [cdc].[fn_cdc_get_all_changes_dbo_ThucChayMuaNgoaiChiTiet]
	(	@from_lsn binary(10),
		@to_lsn binary(10),
		@row_filter_option nvarchar(30)
	)
	returns table
	return
	
	select NULL as __$start_lsn,
		NULL as __$seqval,
		NULL as __$operation,
		NULL as __$update_mask, NULL as [ThucChayMuaNgoaiChiTietID], NULL as [HopDongREF], NULL as [HopDongChiTietREF], NULL as [TuNgay], NULL as [DenNgay], NULL as [NgayThucChay], NULL as [SoLuongThucChay], NULL as [DmDonViTinhREF], NULL as [ChietKhauMuaNgoai], NULL as [ThanhTienMuaNgoaiTruocCK], NULL as [ThanhTienThucChayBanSauCK], NULL as [ThanhTienLaiThucChaySauCK], NULL as [CreatedAt], NULL as [CreatedBy], NULL as [LastModifiedAt], NULL as [LastModifiedBy], NULL as [Status], NULL as [DeletedStatus], NULL as [TrangThaiTinhThucChay], NULL as [id], NULL as [NgayDuyet], NULL as [NguoiDuyet], NULL as [NgayChot], NULL as [NguoiChot]
	where ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayMuaNgoaiChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 0)

	union all
	
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChayMuaNgoaiChiTietID], t.[HopDongREF], t.[HopDongChiTietREF], t.[TuNgay], t.[DenNgay], t.[NgayThucChay], t.[SoLuongThucChay], t.[DmDonViTinhREF], t.[ChietKhauMuaNgoai], t.[ThanhTienMuaNgoaiTruocCK], t.[ThanhTienThucChayBanSauCK], t.[ThanhTienLaiThucChaySauCK], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[Status], t.[DeletedStatus], t.[TrangThaiTinhThucChay], t.[id], t.[NgayDuyet], t.[NguoiDuyet], t.[NgayChot], t.[NguoiChot]
	from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] t with (nolock)    
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayMuaNgoaiChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4)
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
		
	union all	
		
	select t.__$start_lsn as __$start_lsn,
		t.__$seqval as __$seqval,
		t.__$operation as __$operation,
		t.__$update_mask as __$update_mask, t.[ThucChayMuaNgoaiChiTietID], t.[HopDongREF], t.[HopDongChiTietREF], t.[TuNgay], t.[DenNgay], t.[NgayThucChay], t.[SoLuongThucChay], t.[DmDonViTinhREF], t.[ChietKhauMuaNgoai], t.[ThanhTienMuaNgoaiTruocCK], t.[ThanhTienThucChayBanSauCK], t.[ThanhTienLaiThucChaySauCK], t.[CreatedAt], t.[CreatedBy], t.[LastModifiedAt], t.[LastModifiedBy], t.[Status], t.[DeletedStatus], t.[TrangThaiTinhThucChay], t.[id], t.[NgayDuyet], t.[NguoiDuyet], t.[NgayChot], t.[NguoiChot]
	from [cdc].[dbo_ThucChayMuaNgoaiChiTiet_CT] t with (nolock)     
	where (lower(rtrim(ltrim(@row_filter_option))) = 'all update old')
	    and ( [sys].[fn_cdc_check_parameters]( N'dbo_ThucChayMuaNgoaiChiTiet', @from_lsn, @to_lsn, lower(rtrim(ltrim(@row_filter_option))), 0) = 1)
		and (t.__$operation = 1 or t.__$operation = 2 or t.__$operation = 4 or
		     t.__$operation = 3 )
		and (t.__$start_lsn <= @to_lsn)
		and (t.__$start_lsn >= @from_lsn)
	
```
