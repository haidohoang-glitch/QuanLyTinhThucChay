# Stored Procedure: `prc_asd_DmLoaiBanner_GetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-14 11:43:30.307000
- **Ngày sửa cuối**: 2017-04-14 11:43:30.307000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROC prc_asd_DmLoaiBanner_GetAll
AS

BEGIN
	SELECT DmLoaiBannerID [ID], TenLoaiBanner [Name] FROM dbo.DmLoaiBanner;
	
END
```
