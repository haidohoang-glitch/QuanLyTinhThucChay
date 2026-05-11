# Stored Procedure: `InsertTCDT_Test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-25 18:31:26.577000
- **Ngày sửa cuối**: 2021-05-25 18:45:29.457000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopdongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--InsertTCDT_Test 621982
CREATE PROCEDURE [dbo].[InsertTCDT_Test] 
	-- Add the parameters for the stored procedure here
	@HopdongChiTietREF int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	
	Insert into ABM_test_ag.dbo.ThucChayDaTinh
	select * from ThucChayDaTinh where HopDongChiTietREF = @HopdongChiTietREF and NgayThucHien >='2021-05-24'
END

```
