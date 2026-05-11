# Stored Procedure: `KiemTra_DauVao_HopDong_MaHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:01.457000
- **Ngày sửa cuối**: 2016-11-24 10:46:01.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThoiGian` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [KiemTra_DauVao_HopDong_MaHopDong] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_MaHopDong]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongID, DmMaHopDongREF,CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 AND CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID,DmMaHopDongREF,CreatedAt, LastModifiedAt FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongID
	where A.DmMaHopDongREF <> B.DmMaHopDongREF
	or A.HopDongID IS NULL OR B.HopDongID IS NULL OR A.DmMaHopDongREF IS NULL OR B.DmMaHopDongREF IS NULL
    
END


```
