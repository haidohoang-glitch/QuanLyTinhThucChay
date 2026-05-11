# Stored Procedure: `KiemTra_DauVao_ThucChayHopDongChiTietPR_SoBanGhiActive`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 11:05:32.017000
- **Ngày sửa cuối**: 2016-11-22 11:05:32.017000

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
CREATE PROCEDURE [dbo].[KiemTra_DauVao_ThucChayHopDongChiTietPR_SoBanGhiActive] 
	-- Add the parameters for the stored procedure here
	@IsActive int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @demSQLActive FLOAT=0, @demMySQLActive FLOAT =0,@demSQLHuy INT = 0, @demMySQLHuy INT =0
	
	TRUNCATE TABLE ThucChayHopDongChiTietPRSyn

	INSERT INTO ThucChayHopDongChiTietPRSyn
	EXEC [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.[KiemTra_DauVao_ThucChayHopDongChiTietPR_Insert] 
   
	SET @demMySQLActive = (SELECT COUNT(*)  FROM ThucChayHopDongChiTietPRSyn)
	SET @demSQLActive = (SELECT COUNT(*)  FROM ThucChayHopDongChiTietPR WHERE DeletedStatus = 0)
	
	

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
