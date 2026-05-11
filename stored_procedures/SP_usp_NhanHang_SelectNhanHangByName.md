# Stored Procedure: `usp_NhanHang_SelectNhanHangByName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 11:51:34.030000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.103000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNhanHang` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SelectNhanHangByName]
	@TenNhanHang NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	
	SET @TenNhanhang = REPLACE(@TenNhanhang, '''', '''''')
	
	SELECT [DmNhanHangID],
	       [TenNhanHang],
	       [MucDoNhan],
	       [DmNghanhHangREF],
	       TenChienDich AS DmChienDichREF,
	       [TenChienDichNhan] = STUFF(
	           (
	               SELECT ';' + B.TenChienDich
	               FROM   DmChienDichNhanhang AS B
	               WHERE  B.DmChienDichID IN (SELECT *
	                                          FROM   dbo.Split(DmNhanHang.TenChienDich, ','))
	                      FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       [DmNhanHangThayDoiID],
	       [TenNghanhHang] = STUFF(
	           (
	               SELECT ';' + md.TenNghanhHang
	               FROM   DmNghanhHang md
	               WHERE  md.DeletedStatus <> 1
	                      AND md.DmNghanhHangID IN (SELECT *
	                                                FROM   dbo.Split(DmNhanHang.DmNghanhHangREF, ','))
	                          FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       DmNhanHang.NhanHangCha,
	       (
	           SELECT A.TenNhanHang
	           FROM   DmNhanHang AS A
	           WHERE  A.DmNhanHangID = DmNhanHang.NhanHangCha
	       ) AS TenNhanCha,
	       DmNhanHang.DmNhaPhanPhoiREF,
	       [TenNhaPhanPhoi] = STUFF(
	           (
	               SELECT ';' + npp.TenKhachHang
	               FROM   KhachHangThongTinChung AS npp
	               WHERE  npp.KhachHangThongTinChungID IN (SELECT *
	                                          FROM   dbo.Split(DmNhanHang.DmNhaPhanPhoiREF, ','))
	                      FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       DmNhanHang.DmKhachhangSohuuREF,
	       (
	           SELECT shn.TenKhachHang
	           FROM   KhachHangThongTinChung AS shn
	           WHERE  shn.KhachHangThongTinChungID = DmKhachhangSohuuREF
	       ) AS TenKhachhangSohuu,
	       DmNhanHang.Ghichu,
	       DmNhanHang.[RecordStatus]
	FROM   [dbo].[DmNhanHang] AS DmNhanHang
	WHERE  TenNhanHang COLLATE SQL_Latin1_General_CP1_CI_AI LIKE N'%' + @TenNhanhang + '%'
	       AND DmNhanHang.DeletedStatus <> 1
	ORDER BY DmNhanHang.TenNhanHang ASC
END

```
