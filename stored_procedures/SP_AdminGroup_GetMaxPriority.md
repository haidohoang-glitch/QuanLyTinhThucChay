# Stored Procedure: `AdminGroup_GetMaxPriority`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.080000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.420000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroup_GetMaxPriority]	
AS
BEGIN
	SELECT MAX(ag.Priority) + 1 From AdminGroup ag
END

```
