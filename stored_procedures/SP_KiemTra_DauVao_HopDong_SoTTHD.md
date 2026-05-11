# Stored Procedure: `KiemTra_DauVao_HopDong_SoTTHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:02.407000
- **Ngày sửa cuối**: 2016-11-24 10:46:02.460000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [KiemTra_DauVao_HopDong_SoTTHD]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_SoTTHD]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongID, So FROM ABM_Data_ThucChay.dbo.hopdong 
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID,so FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongID
	AND A.So = B.so
	WHERE A.HopDongID IS NULL OR B.HopDongID IS NULL OR A.So IS NULL OR B.so IS NULL
    
END


```
