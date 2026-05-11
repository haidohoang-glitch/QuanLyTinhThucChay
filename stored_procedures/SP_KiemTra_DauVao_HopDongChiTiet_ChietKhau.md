# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_ChietKhau`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:22:39.693000
- **Ngày sửa cuối**: 2016-11-23 15:16:16.717000

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
--EXEC [KiemTra_DauVao_HopDongChiTiet_ChietKhau] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_ChietKhau]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongFK, HopDongChiTietID, ChietKhau,CreatedAt, LastModifiedAt FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongFK, HopDongChiTietID, ChietKhau,CreatedAt, LastModifiedAt FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	AND A.ChietKhau = B.ChietKhau
	AND A.HopDongFK = B.HopDongFK
	WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.ChietKhau IS NULL OR B.ChietKhau IS NULL
    
END

```
