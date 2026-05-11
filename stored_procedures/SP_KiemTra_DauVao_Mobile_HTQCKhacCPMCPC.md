# Stored Procedure: `KiemTra_DauVao_Mobile_HTQCKhacCPMCPC`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-18 10:14:48.693000
- **Ngày sửa cuối**: 2016-11-24 14:23:54.447000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KiemTra_DauVao_Mobile_HTQCKhacCPMCPC]
	-- Add the parameters for the stored procedure here
	--Check xem có hd nào khác HTQC CPM, CPC

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT HopDongFK, hd.SoHopDong, TenLoai, ThanhTien, hdct.ThanhtienThucChay,
	 (ThanhTien- hdct.ThanhtienThucChay)lech, hdct.DmSanPhamREF
	FROM dbo.HopDong hd INNER JOIN hopdongchitiet hdct ON hd.HopDongID = hdct.HopDongFK
 WHERE TenLoai NOT IN ('CPC','CPM',N'Mua ngoài','Default',N'HD hợp tác','Content Marketing')
AND hdct.DeletedStatus = 0 AND 
hd.TrangThaiHopDong <> 3
AND hd.Nam >=2014
AND hdct.DmSanPhamREF = 342
AND hd.TenMaHopDong NOT IN ('ht')
ORDER BY (ThanhTien - hdct.ThanhtienThucChay)

END

```
