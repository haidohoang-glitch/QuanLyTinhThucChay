# Stored Procedure: `GetLikeNganhHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:32.903000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.383000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNganhHang` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE proc [dbo].[GetLikeNganhHang]
@TenNganhHang nvarchar(50)
as
begin
 select top 30 DmNghanhHangID, TenNghanhHang, DmNghanhHangREF from DmNghanhHang 
 where TenNghanhHang COLLATE  SQL_Latin1_General_CP1_CI_AI like N'%' +@TenNganhHang +'%' AND DeletedStatus = 0
 order by TenNghanhHang
end

```
