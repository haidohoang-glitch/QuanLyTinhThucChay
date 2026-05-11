# Stored Procedure: `KiemTra_DauVao_HopDong_SoBanGhiActive`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:02.287000
- **Ngày sửa cuối**: 2016-11-24 10:46:02.340000

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
--EXEC [KiemTra_DauVao_HopDong_SoBanGhiActive] 0
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_SoBanGhiActive] 
	-- Add the parameters for the stored procedure here
	@IsActive int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE  @ThoiGian DATETIME, @demSQLActive FLOAT=0, @demMySQLActive FLOAT =0,@demSQLHuy INT = 0, @demMySQLHuy INT =0
	TRUNCATE TABLE HopDongSyn


    -- Insert statements for procedure here
	--SET @ThoiGian = (SELECT MAX(LastModifiedAt) FROM dbo.HopDong)
	SET @demSQLActive = (SELECT COUNT(*) FROM  dbo.HopDong WHERE TrangThaiHopDong <> 3)
	SET @demSQLHuy = (SELECT COUNT(*) FROM  dbo.HopDong WHERE TrangThaiHopDong = 3)
    
	EXEC [ASD-SQLSVR_UUTP].ABM_Data_Release.dbo.KiemTra_DauVao_HopDong_Insert
	--CHU Y NGAY LAY DU LIEU, HIEN TAI LA MAC DINH TU NAM 2016-01-01
	SET @demMySQLActive = (SELECT COUNT(*)  FROM HopDongSyn WHERE TrangThaiHopDong <> 3)
	SET @demMySQLHuy = (SELECT COUNT(*)  FROM HopDongSyn WHERE TrangThaiHopDong = 3)
	
	-------------
	IF @IsActive = 1 
		BEGIN
			IF @demMySQLActive <> @demMySQLActive 
				PRINT 'Du So Ban ghi Active'
				ELSE
				PRINT 'Khong Du So Ban ghi Active'
		END
    ELSE
    
		BEGIN
			IF @demSQLHuy <> @demMySQLHuy 
				PRINT 'Du So Ban ghi Huy'
				ELSE
				PRINT 'Khong Du So Ban ghi Huy'
		END
END


```
