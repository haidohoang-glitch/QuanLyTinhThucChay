# Stored Procedure: `PerformanceBase_Input_HopDong_thieu_Phanbo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-03-08 15:58:12.310000
- **Ngày sửa cuối**: 2024-03-08 16:34:12.900000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>

--EXEC [PerformanceBase_Input_HopDong_thieu_Phanbo]
-- =============================================
CREATE PROCEDURE [dbo].[PerformanceBase_Input_HopDong_thieu_Phanbo]
    -- Add the parameters for the stored procedure here 
 
AS
BEGIN

DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = DATEADD(DAY,-1,CONVERT(DATE,GETDATE()))
	--SELECT @NgayThucHien
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
 SET NOCOUNT ON;
 SELECT contract_number,username,phanbo,dbo.FormatNumber(isnull(sum(CONVERT(FLOAT,domain_tt_money)),0)) AS ThucChay_NoVAT, dbo.FormatDate(NgayThucHien) [NgayThucHien]
 FROM dbo.ThucChayAdmarket_PhanBo  WHERE NgayThucHien= @Ngaythuchien
 AND ISNULL(contract_number,'') <> N'' 
 AND contract_number <> N'BLANK'
 AND phanbo=0
 GROUP BY  username,NgayThucHien,phanbo,contract_number
 ORDER BY NgayThucHien
END;

```
