# Stored Procedure: `DongBoDuLieu_Lai_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-11-06 09:17:10.250000
- **Ngày sửa cuối**: 2020-11-06 09:17:10.250000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql



create PROCEDURE [dbo].[DongBoDuLieu_Lai_GGFB]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	--BEGIN TRY
	--BEGIN TRANSACTION
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	

		--3. ThucChayDaTinh_MuaNgoai
		DELETE FROM
		--SELECT * FROM 
		[ASDAG].ABM_Data_Release.dbo.ThucChayDaTinh_MuaNgoai 
		WHERE NgayThucHien = '2020-11-02' and HopDongChiTietref = 594595
		
		
		
		
		
	--COMMIT TRANSACTION
	--END TRY
	--BEGIN CATCH
	--IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION
	---- Error Message
	--DECLARE @Err nvarchar(1000)
	--SET @Err = ERROR_MESSAGE()
	--RAISERROR (@Err,16,1)
	--END CATCH
END

```
