# Stored Procedure: `KiemTra_DauVao_HopDong_LoaiKH`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-24 10:46:01.340000
- **Ngày sửa cuối**: 2016-11-24 10:46:01.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThoiGian` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--=========================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [KiemTra_DauVao_HopDong_LoaiKH] '2013-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDong_LoaiKH]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
		declare @Out_IDDmLoaiKhachHangREF nvarchar(max)
	IF OBJECT_ID('#TempDmLoaiKhachHangREF', 'U') IS NOT NULL 
		DROP TABLE #TempDmLoaiKhachHangREF;  
	SELECT A.HopDongID, B.HopDongIDSyn INTO #TempDmLoaiKhachHangREF 
	FROM (
	SELECT HopDongID, DmLoaiKhachHangREF
	FROM ABM_Data_ThucChay.dbo.hopdong 
	WHERE 1=1 and CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongID HopDongIDSyn,DmLoaiKhachHangREF FROM HopDongSyn
	)B
	ON A.HopDongID =B.HopDongIDSyn
	where A.DmLoaiKhachHangREF <> B.DmLoaiKhachHangREF
	or A.HopDongID IS NULL OR B.HopDongIDSyn IS NULL OR A.DmLoaiKhachHangREF IS NULL OR B.DmLoaiKhachHangREF IS NULL

	SELECT @Out_IDDmLoaiKhachHangREF =  CONVERT(NVARCHAR(5),A.ID) + COALESCE(','+@Out_IDDmLoaiKhachHangREF + N',',N'')
	 FROM
	 (
	  SELECT DISTINCT temp.ID FROM (SELECT HopDongID ID FROM #TempDmLoaiKhachHangREF WHERE HopDongID IS NOT NULL
								UNION ALL SELECT HopDongIDSyn ID FROM #TempDmLoaiKhachHangREF  WHERE HopDongIDSyn  IS NOT NULL) temp
	 )A
	-- SELECT @Out_IDNgayDanhSo
	INSERT INTO ThongTinRaSoatThucChayDauVao
	SELECT 'Dau vao lay du lieu', 'HopDong','Lech du lieu', 'DmLoaiKhachHangREF','HopDongID', @Out_IDDmLoaiKhachHangREF, getdate(),@ThoiGian,getdate()

    
END



```
