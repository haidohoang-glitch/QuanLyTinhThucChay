# Stored Procedure: `KiemTra_DauVao_HopDong_KhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:01.253000
- **Ngày sửa cuối**: 2016-11-24 10:46:01.277000

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
--EXEC [KiemTra_DauVao_HopDong_KhachHang]
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_KhachHang]
	-- Add the parameters for the stored procedure here
	@ThoiGian datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	declare @Out_IDDmHinhThucKhachHangREF nvarchar(max)
		IF OBJECT_ID('#TempDmHinhThucKhachHangREF', 'U') IS NOT NULL 
		DROP TABLE #TempDmHinhThucKhachHangREF;  
	SELECT A.HopDongID, B.HopDongIDSyn INTO #TempDmHinhThucKhachHangREF 
	FROM (
	SELECT HopDongID, DmHinhThucKhachHangREF
	FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 and CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID HopDongIDSyn,DmHinhThucKhachHangREF FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongIDSyn
	where A.DmHinhThucKhachHangREF <> B.DmHinhThucKhachHangREF
	or A.HopDongID IS NULL OR B.HopDongIDSyn IS NULL OR A.DmHinhThucKhachHangREF IS NULL OR B.DmHinhThucKhachHangREF IS NULL

	SELECT @Out_IDDmHinhThucKhachHangREF =  CONVERT(NVARCHAR(5),A.ID) + COALESCE(','+@Out_IDDmHinhThucKhachHangREF + N',',N'')
	 FROM
	 (
	  SELECT DISTINCT temp.ID FROM (SELECT HopDongID ID FROM #TempDmHinhThucKhachHangREF WHERE HopDongID IS NOT NULL
								UNION ALL SELECT HopDongIDSyn ID FROM #TempDmHinhThucKhachHangREF  WHERE HopDongIDSyn  IS NOT NULL) temp
	 )A
	-- SELECT @Out_IDNgayDanhSo
	INSERT INTO ThongTinRaSoatThucChayDauVao
	SELECT 'Dau vao lay du lieu', 'HopDong','Lech du lieu', 'DmHinhThucKhachHangREF','HopDongID', @Out_IDDmHinhThucKhachHangREF, getdate(),@ThoiGian,getdate()
	
    
END


```
