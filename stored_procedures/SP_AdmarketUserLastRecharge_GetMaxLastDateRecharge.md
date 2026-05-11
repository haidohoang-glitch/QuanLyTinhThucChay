# Stored Procedure: `AdmarketUserLastRecharge_GetMaxLastDateRecharge`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-25 14:31:05.380000
- **Ngày sửa cuối**: 2015-09-17 15:12:59.183000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdmarketUserLastRecharge_GetMaxLastDateRecharge]
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = (
	        SELECT MAX(tcau.NgayThucHien)
	        FROM   ThucChayAdmarketUsers tcau
	    )
	--SELECT DISTINCT Code,UserName FROM admarketBalanceUserDaily bl
	SELECT DISTINCT 'cpc' Code,
	       bl.username
	FROM   ThucChayAdmarketUsers bl
	WHERE bl.NgayThucHien = @NgayThucHien
	UNION 
	SELECT DISTINCT(
	           CASE 
	                WHEN bl.DmViTriREF = 1 THEN 'adx'
	                WHEN bl.DmViTriREF = 2 THEN 'mobx'
	                WHEN bl.DmViTriREF = 3 THEN 'ecomx'
	                ELSE 'adx'
	           END
	       )Code
	       ,bl.username
	FROM   ThucChayAdXForUsers bl
	WHERE @NgayThucHien = @NgayThucHien
	UNION 
	SELECT DISTINCT 'ViewPlus' Code,
	       bl.username
	FROM   ThucChayViewPlusForUsers bl
	WHERE bl.NgayThucHien = @NgayThucHien
	       --INNER JOIN AdmarketUserLastRecharge aulr  ON bl.Code = aulr.Code AND bl.UserName = aulr.UserName
END



```
