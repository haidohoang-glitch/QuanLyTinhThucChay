# Stored Procedure: `AdminBoPhanWebsite_CheckByLoaiDoiTuong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:06.883000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.120000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmLoaiDoiTuongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-09
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminBoPhanWebsite_CheckByLoaiDoiTuong]
	-- Add the parameters for the stored procedure here
	@TenDangNhap NVARCHAR(50),
	@DmLoaiDoiTuongREF INT -- 1: Admicro, 2: Doi tac
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT 
		A.Username AS TenDangNhap, 
		B.AdminGroupId AS DmLoaiDoiTuongREF
	FROM AdminUser A
		INNER JOIN AdminGroupUser B ON A.AdminUserId = B.AdminUserId
	WHERE
		A.Username = @TenDangNhap AND B.AdminGroupId = @DmLoaiDoiTuongREF 
	
END

```
