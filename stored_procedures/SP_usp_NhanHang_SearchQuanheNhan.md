# Stored Procedure: `usp_NhanHang_SearchQuanheNhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:56.920000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.503000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `varchar(50)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SearchQuanheNhan]
	@DmNhanHangID VARCHAR(50)
AS
BEGIN
	; WITH cte
	AS
	(
	    SELECT n.DmNhanHangID,
	           n.TenNhanHang,
	           n.MucDoNhan,
	           n.TenChienDich,
	           n.DmNghanhHangREF AS NganhHangID,
	           n.DmKhachhangSohuuREF,
	           n.DmNhaPhanPhoiREF,
	           levels = 0,
	           RIGHT('000' + CONVERT(VARCHAR(MAX), n.DmNhanHangID), 3) AS Lvl
	    FROM   DmNhanHang AS n
	    WHERE  n.RecordStatus = 1
	           AND DeletedStatus <> 1
	           AND n.DmNhanHangID IN (SELECT * FROM   dbo.Split(@DmNhanHangID, ','))
	    
	    UNION ALL
	    
	    SELECT s.DmNhanHangID,
	           s.TenNhanHang,
	           s.MucDoNhan,
	           s.TenChienDich,
	           s.DmNghanhHangREF AS NganhHangID,
	           s.DmKhachhangSohuuREF,
	           s.DmNhaPhanPhoiREF,
	           levels = c.levels + 1,
	           c.lvl + RIGHT('000' + CONVERT(VARCHAR(MAX), s.DmNhanHangID), 3) AS 
	           lvl
	    FROM   cte c
	           INNER JOIN DmNhanHang s
	                ON  c.DmNhanHangID = s.NhanHangCha
	    WHERE  s.DeletedStatus <> 1
	)
	SELECT DmNhanHangID,
	       LEFT(REPLICATE('|-- ', cte.levels) + cte.TenNhanHang, 512) AS 
	       TenNhanHang,
	       TenChienDich,
	       [TenChienDichNhan] = STUFF(
	           (
	               SELECT ';' + B.TenChienDich
	               FROM   DmChienDichNhanhang AS B
	               WHERE  B.DmChienDichID IN (SELECT *
	                                          FROM   dbo.Split(cte.TenChienDich, ','))
	                      FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       MucDoNhan,
	       NganhHangID,
	       --DmNghanhHangREF,
	       [DmNghanhHangREF] = STUFF(
	           (
	               SELECT '; ' + md.TenNghanhHang
	               FROM   DmNghanhHang md
	               WHERE  md.DeletedStatus <> 1
	                      AND md.DmNghanhHangID IN (SELECT *
	                                                FROM   dbo.Split(NganhHangID, ','))
	                          FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       DmKhachhangSohuuREF,
	       (
	           SELECT shn.TenKhachHang
	           FROM   KhachHangThongTinChung AS shn
	           WHERE  shn.KhachHangThongTinChungID = DmKhachhangSohuuREF
	       ) AS DSKhachHangSoHuu,
	       DmNhaPhanPhoiREF,
	       [TenNhaPhanPhoi] = STUFF(
	           (
	               SELECT ';' + npp.TenKhachHang
	               FROM   KhachHangThongTinChung AS npp
	               WHERE  npp.KhachHangThongTinChungID IN (SELECT *
	                                          FROM   dbo.Split(DmNhaPhanPhoiREF, ','))
	                      FOR XML PATH(''), TYPE
	           ).value('.', 'NVARCHAR(MAX)'),
	           1,
	           1,
	           ''
	       ),
	       levels
	FROM   cte
	ORDER BY
	       lvl
END

```
