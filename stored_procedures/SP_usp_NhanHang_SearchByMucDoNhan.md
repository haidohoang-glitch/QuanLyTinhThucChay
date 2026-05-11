# Stored Procedure: `usp_NhanHang_SearchByMucDoNhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:59.010000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.583000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@MucDoNhan` | `varchar(10)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SearchByMucDoNhan]
	@MucDoNhan VARCHAR(10)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT [DmNhanHangID],
	       [TenNhanHang],
	       [MucDoNhan],
	       [TenChienDichNhan] = STUFF(
	           (
	               SELECT ';' + B.TenChienDich
	               FROM   DmChienDichNhanhang AS B
	               WHERE  B.DmChienDichID IN (SELECT *
	                                          FROM   dbo.Split(n.TenChienDich, ','))
	                      FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       [DmNghanhHangREF] = STUFF(
	           (
	               SELECT '; ' + md.TenNghanhHang
	               FROM   DmNghanhHang md
	               WHERE  md.DeletedStatus <> 1
	                      AND md.DmNghanhHangID IN (SELECT *
	                                                FROM   dbo.Split(n.DmNghanhHangREF, ','))
	                          FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       (
	           SELECT shn.TenKhachHang
	           FROM   KhachHangThongTinChung AS shn
	           WHERE  shn.KhachHangThongTinChungID = DmKhachhangSohuuREF
	       ) AS DSKhachHangSoHuu,
	       [TenNhaPhanPhoi] = STUFF(
	           (
	               SELECT ';' + npp.TenKhachHang
	               FROM   KhachHangThongTinChung AS npp
	               WHERE  npp.KhachHangThongTinChungID IN (SELECT *
	                                          FROM   dbo.Split(n.DmNhaPhanPhoiREF, ','))
	                      FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       )
	FROM   DmNhanHang n
	WHERE  DeletedStatus <> 1
	       AND n.RecordStatus = 1
	       AND n.MucDoNhan = @MucDoNhan
END

```
