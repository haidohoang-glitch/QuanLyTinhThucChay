# Stored Procedure: `KiemTra_DauVao_ThucChayHopDongChiTiet_SoBanGhiActive`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 10:54:27.407000
- **Ngày sửa cuối**: 2016-11-22 10:54:27.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@IsActive` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC KiemTra_DauVao_HopDong_SoBanGhiActive 0
CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThucChayHopDongChiTiet_SoBanGhiActive] 
	-- Add the parameters for the stored procedure here
	@IsActive int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @demSQLActive FLOAT=0, @demMySQLActive FLOAT =0,@demSQLHuy INT = 0, @demMySQLHuy INT =0

	TRUNCATE TABLE ThucChayHopDongChiTietSyn
	EXEC [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.[KiemTra_DauVao_ThucChayHopDongChiTiet_Insert] 
   
	SET @demMySQLActive = (SELECT COUNT(*)  FROM ThucChayHopDongChiTietSyn)
	SET @demSQLActive = (SELECT COUNT(*)  FROM ThucChayHopDongChiTiet WHERE DeletedStatus = 0)
	
	

	-------------
	IF @IsActive = 1 
		BEGIN
			IF @demMySQLActive <> @demMySQLActive 
				PRINT 'Du So Ban ghi Active'
				ELSE
				PRINT 'Khong Du So Ban ghi Active'
		END
   
END

```
