# Stored Procedure: `prc_asd_DmHinhThucQuangCao_GetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-14 17:21:48.913000
- **Ngày sửa cuối**: 2017-04-14 17:27:22.527000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC prc_asd_DmHinhThucQuangCao_GetAll
AS

BEGIN
	SELECT DmHinhThucQuangCaoID ID, TenHinhThucQuangCao Name FROM dbo.DmHinhThucQuangCao ORDER BY Name
	
END
```
