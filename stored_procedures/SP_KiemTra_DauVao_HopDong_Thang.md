# Stored Procedure: `KiemTra_DauVao_HopDong_Thang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:02.527000
- **Ngày sửa cuối**: 2016-11-24 10:46:02.580000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [KiemTra_DauVao_HopDong_Thang]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_Thang]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongID, Thang FROM ABM_Data_ThucChay.dbo.hopdong 
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID,thang FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongID
	AND A.Thang = B.thang
	WHERE A.HopDongID IS NULL OR B.HopDongID IS NULL OR A.Thang IS NULL OR B.thang IS NULL
    
END


```
