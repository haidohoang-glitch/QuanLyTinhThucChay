# Stored Procedure: `usp_NghanhHang_SelectTreeview`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:46.450000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.277000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NghanhHang_SelectTreeview]

AS
BEGIN
	; WITH cte
	AS
	(
	    SELECT DmNghanhHangID,TenNghanhHang,DmNghanhHangREF,
	           levels = 0,
	           RIGHT('000' + CONVERT(VARCHAR(MAX), DmNghanhHangID), 3) AS Lvl
	    FROM   DmNghanhHang
	    WHERE  DmNghanhHangREF  = 0 AND DeletedStatus <> 1
	    
	    UNION ALL
	    
	    SELECT s.DmNghanhHangID,
	           s.TenNghanhHang,
	           s.DmNghanhHangREF,
	           levels = c.levels + 1,
	           c.lvl + RIGHT('000' + CONVERT(VARCHAR(MAX), s.DmNghanhHangID), 3) AS 
	           lvl
	    FROM   cte c
	           INNER JOIN DmNghanhHang s
	                ON  c.DmNghanhHangID = s.DmNghanhHangREF WHERE s.DeletedStatus <> 1
	)
	SELECT DmNghanhHangID,
	       LEFT(REPLICATE('- ', cte.levels) + cte.TenNghanhHang, 512) AS 
	       TenNghanhHang,
	       DmNghanhHangREF,
	       levels
	FROM   cte
	ORDER BY
	       lvl
END

```
