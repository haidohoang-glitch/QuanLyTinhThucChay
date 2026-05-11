# Stored Procedure: `KiemTra_DauVao_HopDong_GiaTriHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:01.030000
- **Ngày sửa cuối**: 2016-11-24 10:46:01.083000

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
--EXEC [KiemTra_DauVao_HopDong_GiaTriHD] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_GiaTriHD] 
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
DECLARE @Out_IDGiaTriHopDong nvarchar(max)
		IF OBJECT_ID('#TempGiaTriHopDong', 'U') IS NOT NULL 
		DROP TABLE #TempGiaTriHopDong;  
	SELECT A.HopDongID, B.HopDongIDSyn INTO #TempGiaTriHopDong 
	FROM (
	SELECT HopDongID, GiaTriHopDong
	FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 and CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID HopDongIDSyn,GiaTriHopDong FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongIDSyn
	where A.GiaTriHopDong <> B.GiaTriHopDong
	or A.HopDongID IS NULL OR B.HopDongIDSyn IS NULL OR A.GiaTriHopDong IS NULL OR B.GiaTriHopDong IS NULL

	SELECT @Out_IDGiaTriHopDong =  CONVERT(NVARCHAR(5),A.ID) + COALESCE(','+@Out_IDGiaTriHopDong + N',',N'')
	 FROM
	 (
	  SELECT DISTINCT temp.ID FROM (SELECT HopDongID ID FROM #TempGiaTriHopDong WHERE HopDongID IS NOT NULL
								UNION ALL SELECT HopDongIDSyn ID FROM #TempGiaTriHopDong  WHERE HopDongIDSyn  IS NOT NULL) temp
	 )A
	-- SELECT @Out_IDNgayDanhSo
	INSERT INTO ThongTinRaSoatThucChayDauVao
	SELECT 'Dau vao lay du lieu', 'HopDong','Lech du lieu', 'GiaTriHopDong','HopDongID', @Out_IDGiaTriHopDong, getdate(),@ThoiGian,getdate()
	
END



```
