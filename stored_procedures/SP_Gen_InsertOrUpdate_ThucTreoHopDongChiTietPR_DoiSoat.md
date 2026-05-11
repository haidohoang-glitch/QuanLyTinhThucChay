# Stored Procedure: `Gen_InsertOrUpdate_ThucTreoHopDongChiTietPR_DoiSoat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-09 15:39:19.310000
- **Ngày sửa cuối**: 2015-03-09 15:39:19.310000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@thoigianbd` | `datetime(8)` | No |
| `@hd_id` | `bigint(8)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@giatien` | `bigint(8)` | No |
| `@website` | `nvarchar(400)` | No |
| `@chuyenmuc` | `nvarchar(400)` | No |
| `@link` | `nvarchar(400)` | No |
| `@phanbosite_id` | `bigint(8)` | No |
| `@createdby` | `nvarchar(400)` | No |
| `@createddate` | `datetime(8)` | No |
| `@modifiedby` | `nvarchar(400)` | No |
| `@modifieddate` | `datetime(8)` | No |
| `@domainname` | `nvarchar(400)` | No |
| `@code` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucTreoHopDongChiTietPR_DoiSoat] 	
@thoigianbd datetime ,	
@hd_id bigint ,	
@SoHopDong nvarchar (200) ,	
@giatien bigint ,	
@website nvarchar (200) ,	
@chuyenmuc nvarchar (200) ,	
@link nvarchar (200) ,	
@phanbosite_id bigint ,	
@createdby nvarchar (200) ,	
@createddate datetime ,	
@modifiedby nvarchar (200) ,	
@modifieddate datetime ,	
@domainname nvarchar (200) ,	
@code nvarchar (200) 	
As 	
INSERT INTO [dbo].[ThucTreoHopDongChiTietPR_DoiSoat] (	
[thoigianbd],	
[hd_id],	
[SoHopDong],	
[giatien],	
[website],	
[chuyenmuc],	
[link],	
[phanbosite_id],	
[createdby],	
[createddate],	
[modifiedby],	
[modifieddate],	
[domainname],	
[code])	
Values 	
(	
@thoigianbd,	
@hd_id,	
@SoHopDong,	
@giatien,	
@website,	
@chuyenmuc,	
@link,	
@phanbosite_id,	
@createdby,	
@createddate,	
@modifiedby,	
@modifieddate,	
@domainname,	
@code)
```
