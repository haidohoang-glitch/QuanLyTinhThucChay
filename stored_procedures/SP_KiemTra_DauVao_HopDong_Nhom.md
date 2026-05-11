# Stored Procedure: `KiemTra_DauVao_HopDong_Nhom`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:02.047000
- **Ngày sửa cuối**: 2016-11-24 10:50:27.330000

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
--EXEC [KiemTra_DauVao_HopDong_Nhom]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_Nhom]
	-- Add the parameters for the stored procedure here
	@ThoiGian datetime
AS
BEGIN
	DECLARE @Out_IDDmNhomREF NVARCHAR(max)
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
		IF OBJECT_ID('#TempDmNhomREF', 'U') IS NOT NULL 
		DROP TABLE #TempDmNhomREF;  
	SELECT A.HopDongID, B.HopDongIDSyn INTO #TempDmNhomREF 
	FROM (
	SELECT HopDongID, DmNhomREF
	FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 --and CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID HopDongIDSyn,DmNhomREF FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongIDSyn
	where A.DmNhomREF <> B.DmNhomREF
	or A.HopDongID IS NULL OR B.HopDongIDSyn IS NULL OR A.DmNhomREF IS NULL OR B.DmNhomREF IS NULL

	SELECT @Out_IDDmNhomREF =  CONVERT(NVARCHAR(5),A.ID) + COALESCE(','+@Out_IDDmNhomREF + N',',N'')
	 FROM
	 (
	  SELECT DISTINCT temp.ID FROM (SELECT HopDongID ID FROM #TempDmNhomREF WHERE HopDongID IS NOT NULL
								UNION ALL SELECT HopDongIDSyn ID FROM #TempDmNhomREF  WHERE HopDongIDSyn  IS NOT NULL) temp
	 )A
	-- SELECT @Out_IDDmNhomREF
	INSERT INTO ThongTinRaSoatThucChayDauVao
	SELECT 'Dau vao lay du lieu', 'HopDong','Lech du lieu', 'DmNhomREF','HopDongID', @Out_IDDmNhomREF, getdate(),@ThoiGian,getdate()
  
    
END



```
