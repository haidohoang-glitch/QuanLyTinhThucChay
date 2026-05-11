# Stored Procedure: `usp_NhanHang_DeActivePhanQuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-29 15:00:53.267000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.190000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhanQuyenID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_DeActivePhanQuyen]
	@DmPhanQuyenID INT	
AS
BEGIN
	SET NOCOUNT ON;
	
	UPDATE PhanQuyenNhanHang
	SET
		ThoiGianHetHieuLuc = GETDATE(),
		KichHoat = 0	
	WHERE DmPhanQuyenID = @DmPhanQuyenID
END

```
