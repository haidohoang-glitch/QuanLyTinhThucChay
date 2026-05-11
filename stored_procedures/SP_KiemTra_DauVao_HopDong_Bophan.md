# Stored Procedure: `KiemTra_DauVao_HopDong_Bophan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:00.787000
- **Ngày sửa cuối**: 2016-11-24 10:46:00.837000

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
--EXEC [dbo].[KiemTra_DauVao_HopDong_Bophan]  '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_Bophan]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
DECLARE @Out_IDNgayDanhSo NVARCHAR(max), @Out_IDBoPhan NVARCHAR(max)
	IF OBJECT_ID('#TempDmBoPhan', 'U') IS NOT NULL 
		DROP TABLE #TempDmBoPhan;  
	SELECT A.HopDongID, B.HopDongIDSyn INTO #TempDmBoPhan 
	FROM (
	SELECT HopDongID, DmBoPhanREF
	FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 --and CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID HopDongIDSyn,DmBoPhanREF FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongIDSyn
	where A.DmBoPhanREF <> B.DmBoPhanREF
	or A.HopDongID IS NULL OR B.HopDongIDSyn IS NULL OR A.DmBoPhanREF IS NULL OR B.DmBoPhanREF IS NULL

	SELECT @Out_IDBoPhan =  CONVERT(NVARCHAR(5),A.ID) + COALESCE(','+@Out_IDBoPhan + N',',N'')
	 FROM
	 (
	  SELECT DISTINCT temp.ID FROM (SELECT HopDongID ID FROM #TempDmBoPhan WHERE HopDongID IS NOT NULL
								UNION ALL SELECT HopDongIDSyn ID FROM #TempDmBoPhan  WHERE HopDongIDSyn  IS NOT NULL) temp
	 )A
	-- SELECT @Out_IDNgayDanhSo
	INSERT INTO ThongTinRaSoatThucChayDauVao
	SELECT 'Dau vao lay du lieu', 'HopDong','Lech du lieu', 'DmBoPhanREF','HopDongID', @Out_IDBoPhan, getdate(),@ThoiGian,getdate()
	
END



```
