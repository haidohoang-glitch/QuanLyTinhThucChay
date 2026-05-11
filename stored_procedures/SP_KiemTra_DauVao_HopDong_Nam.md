# Stored Procedure: `KiemTra_DauVao_HopDong_Nam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:01.567000
- **Ngày sửa cuối**: 2016-11-24 10:46:01.620000

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
--EXEC [KiemTra_DauVao_HopDong_Nam] '2013-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_Nam]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongID, Nam,CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 AND CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID,Nam,CreatedAt, LastModifiedAt FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongID
	where A.Nam <> B.Nam
	or A.HopDongID IS NULL OR B.HopDongID IS NULL OR A.Nam IS NULL OR B.Nam IS NULL
    
END


```
