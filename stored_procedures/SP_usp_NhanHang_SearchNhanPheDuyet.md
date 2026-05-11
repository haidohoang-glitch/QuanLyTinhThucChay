# Stored Procedure: `usp_NhanHang_SearchNhanPheDuyet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:57.157000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.523000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNhanhang` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SearchNhanPheDuyet]
	@TenNhanhang NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	
	SET @TenNhanhang = REPLACE(@TenNhanhang, '''', '''''')	
	
	SELECT TOP 30 DmNhanHangID AS id,
	       TenNhanHang AS ten,
	       [DmNhanHangID],
	       [TenNhanHang],
	       [MucDoNhan],
	       [DmNghanhHangREF],
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
	       [TenNhanCha] = (
	           SELECT A.TenNhanHang
	           FROM   DmNhanHang AS A
	           WHERE  A.DmNhanHangID = DmNhanHang.NhanHangCha
	       ),
	       DmNhanHang.DmKhachhangSohuuREF,
	       [TenKhachhangSohuu] = (
	           SELECT shn.TenKhachHang
	           FROM   KhachHangThongTinChung AS shn
	           WHERE  shn.KhachHangThongTinChungID = DmKhachhangSohuuREF
	       )
	FROM   [dbo].[DmNhanHang] AS DmNhanHang
	WHERE  TenNhanHang COLLATE SQL_Latin1_General_CP1_CI_AI LIKE N'%' + @TenNhanhang + '%'
	       AND DmNhanHang.DeletedStatus <> 1
	       AND DmNhanHang.RecordStatus = 1
	ORDER BY
	       DmNhanHang.TenNhanHang ASC
END

```
