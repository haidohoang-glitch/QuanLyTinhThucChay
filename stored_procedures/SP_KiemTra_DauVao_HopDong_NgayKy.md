# Stored Procedure: `KiemTra_DauVao_HopDong_NgayKy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:01.800000
- **Ngày sửa cuối**: 2016-11-24 10:46:01.857000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [KiemTra_DauVao_HopDong_NgayKy]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_NgayKy]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongID, NgayKyHopDong FROM ABM_Data_ThucChay.dbo.hopdong 
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID,NgayKyHopDong FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongID
	AND A.NgayKyHopDong = B.NgayKyHopDong
	WHERE A.HopDongID IS NULL OR B.HopDongID IS NULL OR A.NgayKyHopDong IS NULL OR B.NgayKyHopDong IS NULL
    
END



```
