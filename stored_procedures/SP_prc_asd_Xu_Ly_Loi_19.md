# Stored Procedure: `prc_asd_Xu_Ly_Loi_19`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-27 16:08:02.493000
- **Ngày sửa cuối**: 2017-04-27 16:08:02.493000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@SoHopDong` | `varchar(200)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.prc_asd_Xu_Ly_Loi_19
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@SoHopDong VARCHAR(200)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT @NgayThucHien, @HopDongID, @SoHopDong;
END

```
