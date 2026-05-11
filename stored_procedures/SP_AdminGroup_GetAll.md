# Stored Procedure: `AdminGroup_GetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.113000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.023000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroup_GetAll]
AS
SELECT * FROM AdminGroup ORDER BY Priority

```
