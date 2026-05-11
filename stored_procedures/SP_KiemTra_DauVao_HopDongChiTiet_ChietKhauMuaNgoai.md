# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_ChietKhauMuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:23:00.550000
- **Ngày sửa cuối**: 2016-11-23 15:13:48.573000

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

CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_ChietKhauMuaNgoai]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, ChietKhauMuaNgoai FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID, ChietKhauMuaNgoai FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	AND A.ChietKhauMuaNgoai = B.ChietKhauMuaNgoai
	WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.ChietKhauMuaNgoai IS NULL OR B.ChietKhauMuaNgoai IS NULL
    ORDER BY A.HopDongChiTietID
END

```
