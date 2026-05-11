# Stored Procedure: `PhanQuyenNhanHang_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-22 16:28:24.373000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.493000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@OxUserID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <22,05,2014>
-- Description:	<Description,,>
-- =============================================
--PhanQuyenNhanHang_Delete 168, 23
CREATE PROCEDURE [dbo].[PhanQuyenNhanHang_Delete]
	@DmNhanHangID	INT,
	@OxUserID		INT
AS
BEGIN	
	DELETE FROM PhanQuyenNhanHang
	WHERE DmNhanHangREF = @DmNhanHangID AND OxUserREF = @OxUserID		
END

```
