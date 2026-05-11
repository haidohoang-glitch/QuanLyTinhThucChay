# Stored Procedure: `KiemTra_DauVao_DotChay_ThoiGianKetThuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-22 09:13:20.333000
- **Ngày sửa cuối**: 2016-11-22 09:13:20.333000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[KiemTra_DauVao_DotChay_ThoiGianKetThuc]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT DotChayHopDongChiTietID,ThoiGianKetThuc FROM ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet 
	)A
	FULL OUTER JOIN 
	(
	SELECT id, dengay FROM DotChayHopDongChiTietSyn 
	)B
	ON A.DotChayHopDongChiTietID =B.id
	AND CONVERT(DATE,A.ThoiGianKetThuc) = CONVERT(DATE,B.dengay)
	WHERE A.DotChayHopDongChiTietID IS NULL OR B.id IS NULL OR A.ThoiGianKetThuc IS NULL OR B.dengay IS NULL
    
END

```
