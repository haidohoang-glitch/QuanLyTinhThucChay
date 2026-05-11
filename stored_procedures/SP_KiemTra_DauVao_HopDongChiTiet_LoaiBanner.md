# Stored Procedure: `KiemTra_DauVao_HopDongChiTiet_LoaiBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:25:55.510000
- **Ngày sửa cuối**: 2016-11-23 15:18:27.533000

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
--EXeC [dbo].[KiemTra_DauVao_HopDongChiTiet_LoaiBanner] '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_HopDongChiTiet_LoaiBanner]
	-- Add the parameters for the stored procedure here
	@ThoiGian DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT A.*, B.* FROM (
	SELECT HopDongChiTietID, DmLoaiBannerREF FROM ABM_Data_ThucChay.dbo.hopdongchitiet 
	WHERE CONVERT(DATE,LastModifiedAt) >=@ThoiGian
	AND DeletedStatus = 0
	)A
	FULL OUTER JOIN 
	(
	SELECT HopDongChiTietID, DmLoaiBannerREF FROM HopDongChiTietSyn
	)B
	ON A.HopDongChiTietID =B.HopDongChiTietID
	AND A.DmLoaiBannerREF = B.DmLoaiBannerREF
	WHERE A.HopDongChiTietID IS NULL OR B.HopDongChiTietID IS NULL OR A.DmLoaiBannerREF IS NULL OR B.DmLoaiBannerREF IS NULL
    
END

```
