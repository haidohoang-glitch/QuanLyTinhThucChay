# Stored Procedure: `usp_SelectSysChucNangsBySysNhomChucNangFK`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-28 09:07:39.203000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.427000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SysNhomChucNangFK` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE proc [dbo].[usp_SelectSysChucNangsBySysNhomChucNangFK]
	@SysNhomChucNangFK nvarchar(50)
as
SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED	
SELECT
	SysChucNangID,
	SysNhomChucNangFK,
	MaChucNang,
	TenChucNang,
	ThuTuSapXep	
FROM
	[dbo].[SysChucNang]
Where SysNhomChucNangFK = @SysNhomChucNangFK AND DeletedStatus <> 1

```
