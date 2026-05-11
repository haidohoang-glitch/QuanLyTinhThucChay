# Stored Procedure: `KiemTra_DauVao_DotChay_ThoiGianBatDau`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 09:12:49.387000
- **Ngày sửa cuối**: 2016-11-22 09:12:49.387000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_DotChay_ThoiGianBatDau]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT DotChayHopDongChiTietID,ThoiGianBatDau FROM ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet 
	)A
	FULL OUTER JOIN 
	(
	SELECT id, Tungay FROM DotChayHopDongChiTietSyn 
	)B
	ON A.DotChayHopDongChiTietID =B.id
	AND CONVERT(DATE,A.ThoiGianBatDau) = CONVERT(DATE,B.TuNgay)
	WHERE A.DotChayHopDongChiTietID IS NULL OR B.id IS NULL OR A.ThoiGianBatDau IS NULL OR B.TuNgay IS NULL
    
END
--SELECT * FROM  dbo.HopDong
--SELECT * FROM  hdcn_dotchaySyn 
--SELECT CONVERT(date,Tungay ) FROM  hdcn_dotchaySyn 
```
