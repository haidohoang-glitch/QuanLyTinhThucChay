# Stored Procedure: `sp_Update_NgayThucHien_Table_tc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-04-09 09:09:57.860000
- **Ngày sửa cuối**: 2020-04-09 10:41:32.017000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_Update_NgayThucHien_Table_tc 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	Declare @NgayThucHien datetime
	set @NgayThucHien = DATEADD(DAY,-2,getdate())
	set @NgayThucHien = convert(date,@NgayThucHien)
	select @NgayThucHien
	Update Table_tc set DATE_REAL_RUNING = @NgayThucHien where DATE_REAL_RUNING is null
END

```
