# Stored Procedure: `BaoCaoThongTinTongHop_Tree_Departments`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-24 14:13:08.200000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.897000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Level` | `int(4)` | No |
| `@ParentId` | `int(4)` | No |

## Definition (Source Code)

```sql
--[BaoCaoThongTinTongHop_Tree_Departments] 0, 0
CREATE PROCEDURE [dbo].[BaoCaoThongTinTongHop_Tree_Departments] 
	@Level		INT,
	@ParentId	INT				
AS
BEGIN
	DECLARE @Sql NVARCHAR(MAX)	
	SET @Sql = 'DECLARE @TypeId INT '
	SET @Sql += (	
		SELECT CASE(@Level)
			WHEN 0 THEN				
				'SET @TypeId = 1 SELECT pb.DmPhongBanID AS Id, pb.TenPhongBan AS [Text], @TypeId AS TypeId FROM DmPhongBan pb ORDER BY pb.TenPhongBan'
			WHEN 1 THEN 
				'SET @TypeId = 2 SELECT bpnv.DmBoPhanNghiepVuID AS Id, bpnv.TenBoPhanNghiepVu AS [Text], @TypeId AS TypeId FROM DmBoPhanNghiepVu bpnv 
				 WHERE bpnv.DmPhongBanFK = ' + CONVERT(NVARCHAR(256), @ParentId) + ' ORDER BY bpnv.TenBoPhanNghiepVu'
			WHEN 2 THEN 
				'SET @TypeId = 3 SELECT nlv.DmNhomLamViecID AS Id, nlv.TenNhomLamViec AS [Text], @TypeId AS TypeId FROM DmNhomLamViec nlv 
				 WHERE nlv.DmBoPhanREF = ' + CONVERT(NVARCHAR(256), @ParentId) + ' ORDER BY nlv.TenNhomLamViec'
		END
	)
	
	PRINT @Sql
	EXEC (@Sql)
END

```
