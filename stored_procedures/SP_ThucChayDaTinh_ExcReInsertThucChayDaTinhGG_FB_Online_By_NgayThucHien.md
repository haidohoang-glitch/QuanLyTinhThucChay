# Stored Procedure: `ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_Online_By_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-19 12:12:29.313000
- **Ngày sửa cuối**: 2015-05-05 18:16:15.450000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-03-19
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_Online_By_NgayThucHien]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @account	NVARCHAR(255),
			@sanPhamId	INT
			
	DECLARE Record_Cursor_ReInsert CURSOR FOR
	SELECT DISTINCT
		TaiKhoan, DmSanPhamREF
	FROM ThucChayGoogleFacebookOnline
	WHERE 1=1
		AND NgayThucHien <= @NgayThucHien
		AND RecordStatus = 0	
		
	OPEN Record_Cursor_ReInsert
	
	FETCH NEXT FROM Record_Cursor_ReInsert INTO @account, @sanPhamId
	WHILE @@FETCH_STATUS = 0
	BEGIN
		EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_Online_ByAccount 
		@NgayThucHien, 
		@account,
		@sanPhamId
	
		FETCH NEXT FROM Record_Cursor_ReInsert INTO @account, @sanPhamId
	END
	
	CLOSE Record_Cursor_ReInsert
	DEALLOCATE Record_Cursor_ReInsert
END

```
