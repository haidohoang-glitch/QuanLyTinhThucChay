# Stored Procedure: `KiemTra_DauVao_HopDong_PhongBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:02.180000
- **Ngày sửa cuối**: 2016-11-24 10:46:02.230000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [KiemTra_DauVao_HopDong_PhongBan]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_PhongBan]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongID, DmPhongBanREF FROM ABM_Data_ThucChay.dbo.hopdong 
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID,DmPhongBanREF FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongID
	AND A.DmPhongBanREF = B.DmPhongBanREF
	WHERE A.HopDongID IS NULL OR B.HopDongID IS NULL OR A.DmPhongBanREF IS NULL OR B.DmPhongBanREF IS NULL
    
END



```
