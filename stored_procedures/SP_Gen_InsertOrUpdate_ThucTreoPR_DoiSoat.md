# Stored Procedure: `Gen_InsertOrUpdate_ThucTreoPR_DoiSoat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-09 15:38:46.330000
- **Ngày sửa cuối**: 2015-03-09 15:38:46.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Ngay` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@Code` | `nvarchar(400)` | No |
| `@Chuyenmuc` | `nvarchar(400)` | No |
| `@banner` | `nvarchar(400)` | No |
| `@link` | `nvarchar(400)` | No |
| `@domainname` | `nvarchar(400)` | No |
| `@sitedomain` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucTreoPR_DoiSoat] 	
@Ngay datetime ,	
@SoHopDong nvarchar (200) ,	
@TenWebsite nvarchar (200) ,	
@Code nvarchar (200) ,	
@Chuyenmuc nvarchar (200) ,	
@banner nvarchar (200) ,	
@link nvarchar (200) ,	
@domainname nvarchar (200) ,	
@sitedomain nvarchar (200) 	
As 	
INSERT INTO [dbo].[ThucTreoPR_DoiSoat] (	
[Ngay],	
[SoHopDong],	
[TenWebsite],	
[Code],	
[Chuyenmuc],	
[banner],	
[link],	
[domainname],	
[sitedomain])	
Values 	
(	
@Ngay,	
@SoHopDong,	
@TenWebsite,	
@Code,	
@Chuyenmuc,	
@banner,	
@link,	
@domainname,	
@sitedomain)
```
