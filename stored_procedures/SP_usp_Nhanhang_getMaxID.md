# Stored Procedure: `usp_Nhanhang_getMaxID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:44.697000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.767000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Nhanhang_getMaxID]

AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT MAX(dmNhanhangid) FROM DmNhanHang dnh;	
END

```
