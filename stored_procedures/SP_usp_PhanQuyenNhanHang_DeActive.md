# Stored Procedure: `usp_PhanQuyenNhanHang_DeActive`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:13:27.710000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.623000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhanQuyenID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_PhanQuyenNhanHang_DeActive]
	@DmPhanQuyenID INT
AS
BEGIN
	SET NOCOUNT ON;
	
	UPDATE PhanQuyenNhanHang
	SET    ThoiGianHetHieuLuc = GETDATE(),
	       KichHoat = 0
	WHERE  DmPhanQuyenID = @DmPhanQuyenID
END

```
