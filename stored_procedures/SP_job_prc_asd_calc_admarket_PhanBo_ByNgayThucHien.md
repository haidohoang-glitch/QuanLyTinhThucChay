# Stored Procedure: `job_prc_asd_calc_admarket_PhanBo_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 10:58:22.503000
- **Ngày sửa cuối**: 2024-02-28 11:33:30.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv	
-- Create date: 20170909
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[job_prc_asd_calc_admarket_PhanBo_ByNgayThucHien] @NgayThucHien = '2024-02-18'
*/
CREATE PROCEDURE [dbo].[job_prc_asd_calc_admarket_PhanBo_ByNgayThucHien]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @NgayHienTai DATETIME = CONVERT(DATE,DATEADD(dd,1,@ngayThucHien))

	--SELECT TOP (100) * FROM dbo.ThucChayAdmarket_PhanBo

	---- 1.tinh cac san pham performance base, chi cho truong hop phanbo <> 0 thucchaydatinhadmarket
	print N'1.tinh cac san pham performance base, chi cho truong hop phanbo <> 0 thucchaydatinhadmarket'
	exec [dbo].[prc_asd_tinhthucchay_sanphamadmarket_PhanBo] @ngaythuchien;

	---- 2.insert theo chieu domain vao ThucChayDaTinh
	print N'2.insert theo chieu domain vao ThucChayDaTinh'
	exec [dbo].[prc_insert_thucchaydatinh_admarket_PhanBo] @ngaythuchien;

	-- 3.huy hop dong
	print '3. Check va tinh thuc chay khi huy hopdong'
	exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_PhanBo] @ngaythuchien; 

	---- 4.thay doi gia tri hop dong
	print '4. thay doi gia tri hop dong'
	exec [dbo].[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong_PhanBo] @ngaythuchien;

	-- 5.can chieu domain va hop dong va tinh luon phan khong co phanbo (online) vào table thucchaydatinhadmarket
	print N'5.can chieu domain va hop dong va tinh luon phan khong co phanbo (online) vào table thucchaydatinhadmarket'
	exec [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract_PhanBo]  @ngaythuchien;


END 



```
