# Stored Procedure: `PhanQuyenNhanHang_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-22 16:24:06.260000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.470000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@OxUserID` | `int(4)` | No |
| `@Username` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <22,05,2014>
-- Description:	<Description,,>
-- =============================================
--PhanQuyenNhanHang_Insert 168, 23, 'admin'
CREATE PROCEDURE [dbo].[PhanQuyenNhanHang_Insert]
	@DmNhanHangID	INT,
	@OxUserID		INT,
	@Username		NVARCHAR(50)
AS
BEGIN
	IF NOT EXISTS(SELECT * FROM PhanQuyenNhanHang WHERE DmNhanHangREF = @DmNhanHangID AND OxUserREF = @OxUserID)
	BEGIN
		INSERT INTO PhanQuyenNhanHang 
		(
			DmNhanHangREF,
			OxUserREF,		
			CreatedBy,
			CreatedAt,
			LastModifiedBy,
			LastModifiedAt
		)
		VALUES(
			@DmNhanHangID, 
			@OxUserID,
			@Username,
			GETDATE(),
			@Username,
			GETDATE()		
		)			
	END			
END

```
