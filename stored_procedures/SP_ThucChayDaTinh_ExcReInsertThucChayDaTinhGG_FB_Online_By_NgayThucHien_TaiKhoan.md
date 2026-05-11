# Stored Procedure: `ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_Online_By_NgayThucHien_TaiKhoan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 13:48:29.853000
- **Ngày sửa cuối**: 2015-04-22 14:31:07.857000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@TaiKhoan` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-03-19
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_Online_By_NgayThucHien_TaiKhoan] '2015-04-19', 'Dai Hoc Bach Khoa HN'

CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_Online_By_NgayThucHien_TaiKhoan]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME,
	@TaiKhoan NVARCHAR(50)
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @account	NVARCHAR(255),
			@sanPhamId	INT
			
	DECLARE record_cursor CURSOR FOR
	SELECT DISTINCT
		TaiKhoan, DmSanPhamREF
	FROM ThucChayGoogleFacebookOnline
	WHERE 1=1
		AND NgayThucHien <= @NgayThucHien
		AND RecordStatus = 0	
		AND TaiKhoan = @TaiKhoan
		
	OPEN record_cursor
	
	FETCH NEXT FROM record_cursor INTO @account, @sanPhamId
	WHILE @@FETCH_STATUS = 0
	BEGIN
		EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_Online_ByAccount 
		@NgayThucHien, 
		@account,
		@sanPhamId
	
		FETCH NEXT FROM record_cursor INTO @account, @sanPhamId
	END
	
	CLOSE record_cursor
	DEALLOCATE record_cursor
END

```
