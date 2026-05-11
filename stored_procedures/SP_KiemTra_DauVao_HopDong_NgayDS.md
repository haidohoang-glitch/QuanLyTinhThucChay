# Stored Procedure: `KiemTra_DauVao_HopDong_NgayDS`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:01.683000
- **Ngày sửa cuối**: 2016-11-24 10:46:01.740000

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
--EXEC [KiemTra_DauVao_HopDong_NgayDS] 
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_NgayDS]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
DECLARE @Out_IDNgayDanhSo NVARCHAR(max)
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
		IF OBJECT_ID('#TempNgayDanhSo', 'U') IS NOT NULL 
		DROP TABLE #TempNgayDanhSo;  
	SELECT A.HopDongID, B.HopDongIDSyn INTO #TempNgayDanhSo 
	FROM (
	SELECT HopDongID, NgayDanhSoHopDong,CreatedAt, LastModifiedAt
	FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 --and CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID HopDongIDSyn,NgayDanhSoHopDong FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongIDSyn
	where A.NgayDanhSoHopDong <> B.NgayDanhSoHopDong
	or A.HopDongID IS NULL OR B.HopDongIDSyn IS NULL OR A.NgayDanhSoHopDong IS NULL OR B.NgayDanhSoHopDong IS NULL

	SELECT @Out_IDNgayDanhSo =  CONVERT(NVARCHAR(5),A.ID) + COALESCE(','+@Out_IDNgayDanhSo + N',',N'')
	 FROM
	 (
	  SELECT DISTINCT temp.ID FROM (SELECT HopDongID ID FROM #TempNgayDanhSo WHERE HopDongID IS NOT NULL
								UNION ALL SELECT HopDongIDSyn ID FROM #TempNgayDanhSo  WHERE HopDongIDSyn  IS NOT NULL) temp
	 )A
	-- SELECT @Out_IDNgayDanhSo
	INSERT INTO ThongTinRaSoatThucChayDauVao
	SELECT 'Dau vao lay du lieu', 'HopDong','Lech du lieu', 'NgayDanhSo','HopDongID', @Out_IDNgayDanhSo, getdate(),@ThoiGian,getdate()
  
END



```
