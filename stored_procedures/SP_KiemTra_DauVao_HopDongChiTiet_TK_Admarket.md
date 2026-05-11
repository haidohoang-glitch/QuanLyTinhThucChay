# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_TK_Admarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:29:30.177000
- **Ngày sửa cuối**: 2016-11-23 16:15:57.590000

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
--EXEC [dbo].[KiemTra_DauVao_HopDongChiTiet_TK_Admarket] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_TK_Admarket]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongFK, HopDongChiTietID, TK_Admarket,CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongFK, HopDongChiTietID, TK_Admarket,CreatedAt, LastModifiedAt FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	where A.TK_Admarket <> B.TK_Admarket
	or A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.TK_Admarket IS NULL OR B.TK_Admarket IS NULL
    
END

```
