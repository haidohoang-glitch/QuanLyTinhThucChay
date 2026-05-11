# Stored Procedure: `Check_CPV_CPR_ChuaChayXong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-17 15:43:07.570000
- **Ngày sửa cuối**: 2017-04-17 15:45:17.700000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE Check_CPV_CPR_ChuaChayXong
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT hd.SoHopDong, hdct.DmSanPhamREF, hdct.DonViTinh,  hdct.ThanhTien,hdct.ThanhTienThucChay FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE hdct.DeletedStatus = 0 AND hdct.DonViTinh IN ('CPV','CPR')
	AND hdct.ThanhTien <> hdct.ThanhTienThucChay
	ORDER BY hdct.DmSanPhamREF, hd.HopDongID
END

```
