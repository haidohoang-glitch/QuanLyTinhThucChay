# Stored Procedure: `KiemTra_DauVao_HopDong_DiaiemLV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:00.900000
- **Ngày sửa cuối**: 2016-11-24 10:46:00.960000

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
--EXEC [dbo].[KiemTra_DauVao_HopDong_DiaiemLV] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_DiaiemLV]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
DECLARE @Out_IDDiaDiem NVARCHAR(max)
	IF OBJECT_ID('#TempDiaDiemLamViec', 'U') IS NOT NULL 
		DROP TABLE #TempDiaDiemLamViec;  
	SELECT A.HopDongID, B.HopDongIDSyn INTO #TempDiaDiemLamViec 
	FROM (
	SELECT HopDongID, DmDiaDiemLamViecREF
	FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 and CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID HopDongIDSyn,DmDiaDiemLamViecREF FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongIDSyn
	where A.DmDiaDiemLamViecREF <> B.DmDiaDiemLamViecREF
	or A.HopDongID IS NULL OR B.HopDongIDSyn IS NULL OR A.DmDiaDiemLamViecREF IS NULL OR B.DmDiaDiemLamViecREF IS NULL

	SELECT @Out_IDDiaDiem =  CONVERT(NVARCHAR(5),A.ID) + COALESCE(','+@Out_IDDiaDiem + N',',N'')
	 FROM
	 (
	  SELECT DISTINCT temp.ID FROM (SELECT HopDongID ID FROM #TempDiaDiemLamViec WHERE HopDongID IS NOT NULL
								UNION ALL SELECT HopDongIDSyn ID FROM #TempDiaDiemLamViec  WHERE HopDongIDSyn  IS NOT NULL) temp
	 )A
	-- SELECT @Out_IDNgayDanhSo
	INSERT INTO ThongTinRaSoatThucChayDauVao
	SELECT 'Dau vao lay du lieu', 'HopDong','Lech du lieu', 'DmDiaDiemLamViecREF','HopDongID', @Out_IDDiaDiem, getdate(),@ThoiGian,getdate()

    
END



```
