# Stored Procedure: `KiemTra_DauVao_HopDong_NhanVien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:01.920000
- **Ngày sửa cuối**: 2016-11-24 10:46:01.977000

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
--EXEC [KiemTra_DauVao_HopDong_NhanVien]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_NhanVien]
	-- Add the parameters for the stored procedure here
	@ThoiGian datetime
AS
BEGIN
	DECLARE @Out_IDSysNhanVienREF NVARCHAR(max)
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
		IF OBJECT_ID('#TempSysNhanVienREF', 'U') IS NOT NULL 
		DROP TABLE #TempSysNhanVienREF;  
	SELECT A.HopDongID, B.HopDongIDSyn INTO #TempSysNhanVienREF 
	FROM (
	SELECT HopDongID, SysNhanVienREF
	FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 --and CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID HopDongIDSyn,SysNhanVienREF FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongIDSyn
	where A.SysNhanVienREF <> B.SysNhanVienREF
	or A.HopDongID IS NULL OR B.HopDongIDSyn IS NULL OR A.SysNhanVienREF IS NULL OR B.SysNhanVienREF IS NULL

	SELECT @Out_IDSysNhanVienREF =  CONVERT(NVARCHAR(5),A.ID) + COALESCE(','+@Out_IDSysNhanVienREF + N',',N'')
	 FROM
	 (
	  SELECT DISTINCT temp.ID FROM (SELECT HopDongID ID FROM #TempSysNhanVienREF WHERE HopDongID IS NOT NULL
								UNION ALL SELECT HopDongIDSyn ID FROM #TempSysNhanVienREF  WHERE HopDongIDSyn  IS NOT NULL) temp
	 )A
	-- SELECT @Out_IDSysNhanVienREF
	INSERT INTO ThongTinRaSoatThucChayDauVao
	SELECT 'Dau vao lay du lieu', 'HopDong','Lech du lieu', 'SysNhanVienREF','HopDongID', @Out_IDSysNhanVienREF, getdate(),@ThoiGian,getdate()
  
    
END



```
