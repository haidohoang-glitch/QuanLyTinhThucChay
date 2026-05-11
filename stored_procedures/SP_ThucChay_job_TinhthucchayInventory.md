# Stored Procedure: `ThucChay_job_TinhthucchayInventory`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-01 09:47:26.860000
- **Ngày sửa cuối**: 2021-04-15 11:12:56.463000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE PROCEDURE [dbo].[ThucChay_job_TinhthucchayInventory] 
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
	EXEC [dbo].[ThucChay_ExecThucChayDaTinh_HopDongInventory] @NgayThucHien 
	EXEC [dbo].[ThucChay_ExecThucChayDaTinh_HopDongInventory_AdmaticProgrammatic] @NgayThucHien = @NgayThucHien

	EXEC [dbo].[ThucChay_Update_GTTD_ThucChayDaTinh_HopDongInventory] @NgayThucHien 
END



```
