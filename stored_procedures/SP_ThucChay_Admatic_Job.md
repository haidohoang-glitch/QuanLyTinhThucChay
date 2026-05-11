# Stored Procedure: `ThucChay_Admatic_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-10 17:06:00.957000
- **Ngày sửa cuối**: 2025-10-28 10:11:10.620000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChay_Admatic_Job] 
AS
BEGIN
	DECLARE @dtStart DATE, @dtEnd DATE, @NgayDanhSoGioiHan DATE, @NgayDanhSoGioiHan_Admatic DATE, @NgayDanhSoGioiHan_Admatic_DonViBai DATE

	SET @dtStart = (
						SELECT TOP (1) tcdt.NgayThucHien
						FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
						LEFT JOIN  ( SELECT hdct.HopDongChiTietID, hdct.HopDongFK 
									 FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
									 WHERE hdct.DeletedStatus = 0
										   AND ISNULL(hdct.DmLoaiNenTangREF,0) <> 8 ) hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
						WHERE tcdt.DmHinhThucQuangCao = 42
							  AND tcdt.DonViTinh <> N'CPV'
							  AND not (tcdt.DmHinhThucQuangCao= 13 OR tcdt.DmLoaiBannerREF IN (17,18))
							  AND tcdt.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821,342,585,5056,5268)
							  AND tcdt.DotChayBooking <> N'HDBAN_INVENTORY'
						ORDER BY tcdt.NgayThucHien DESC
	)	

	SET @dtStart = DATEADD(dd,1, @dtStart)
	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	SET @NgayDanhSoGioiHan = DATEADD(YEAR, -3, @dtStart)
	SET @NgayDanhSoGioiHan_Admatic = IIF(@NgayDanhSoGioiHan >= '2020-07-20', @NgayDanhSoGioiHan, '2020-07-20')
	SET @NgayDanhSoGioiHan_Admatic_DonViBai = IIF(@NgayDanhSoGioiHan >= '2021-06-10', @NgayDanhSoGioiHan, '2021-06-10')

	print N' end khaibao'
	EXEC [dbo].[ThucChay_Admatic_Update_HopDongChiTietAndBanner] @dtEnd, @NgayDanhSoGioiHan
	print N' end AndBanner'
	/*BEGIN PPT THUC CHAY ADMATIC THEO THUC TREO*/
	EXEC [dbo].[ThucChay_Admatic_GhiNhanThayDoi_ThucChayDaTinh] @dtEnd, @dtEnd , @NgayDanhSoGioiHan_Admatic
	print N' end ghinhanthaydoi'
	EXEC [dbo].[ThucChay_Admatic_GhiNhanPhatSinh_ThucChayDaTinh]  @dtStart, @dtEnd, @NgayDanhSoGioiHan_Admatic
	print N' end Phatsinh'
	/*END PPT THUC CHAY ADMATIC THEO THUC TREO*/

	/*BEGIN PPT THUC CHAY ADMATIC THEO HOPDONGCHITIET TREN THUCCHAY_THANHTIEN_ADMATIC*/

	/*AND PPT THUC CHAY ADMATIC THEO HOPDONGCHITIET TREN THUCCHAY_THANHTIEN_ADMATIC*/

	EXEC [dbo].[ThucChay_AdmaticDonViBai]  @dtEnd, @dtEnd, @NgayDanhSoGioiHan
	print N' end donviBai'

	EXEC [dbo].[ThucChay_Admatic_Adx_Insert_ThucChayDaTinhAdmarket] @dtEnd 
	print N' end Adx'


END


```
