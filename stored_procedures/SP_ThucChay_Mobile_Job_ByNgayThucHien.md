# Stored Procedure: `ThucChay_Mobile_Job_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-27 09:44:51.247000
- **Ngày sửa cuối**: 2025-10-27 09:57:31.120000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:    <Author,,Name>
-- Create date: <Create Date,,>
-- Description:  <Description,,>
-- =============================================

/*
Exec [dbo].[ThucChay_Mobile_Job_ByNgayThucHien]
	@dtStart = '2025-10-26', 
	@dtEnd = '2025-10-26' 
*/

CREATE PROCEDURE [dbo].[ThucChay_Mobile_Job_ByNgayThucHien]
	@dtStart DATETIME, 
	@dtEnd DATETIME
AS
BEGIN
  DECLARE @NgayDanhSoGioiHan DATE

  --SET @dtStart = (
  --        SELECT TOP 1 tcdt.NgayThucHien
  --        FROM ABM_data_thucchay.dbo.ThucChayDaTinh tcdt
  --        INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct  ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
  --        WHERE  tcdt.DmSanPhamREF = 342
  --            AND NOT (tcdt.DmHinhThucQuangCao in (13,42) or tcdt.DmLoaiBannerREF in (17,18))
  --            AND tcdt.DotChayHopDong NOT in ( N'NGAY', N'CPM_DonViGoi')
  --        ORDER BY tcdt.NgayThucHien desc
  --         )  
  --SET @dtStart =  DATEADD(dd,1, @dtStart)
  --SET @dtStart = CONVERT(DATE, @dtStart)

  --SET @dtEnd = CONVERT(DATE,GETDATE())
  --SET @dtEnd = DATEADD(dd,-1, @dtEnd)
  
  SET @NgayDanhSoGioiHan = DATEADD(YEAR, -3, @dtStart)

  EXEC [dbo].[ThucChay_mobile_Update_HopDongChiTietAndBanner] @EndDate = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan


  EXEC [dbo].[ThucChay_Mobile_GhiNhanThayDoi_ThucChayDaTinh] @NgayGhiNhan = @dtEnd, @NgayCheckThayDoi=@dtEnd, @NgayDanhSoGioiHan=@NgayDanhSoGioiHan
  EXEC [dbo].[ThucChay_Mobile_GhiNhanPhatSinh_ThucChayDaTinh] @NgayThucHien = @dtEnd, @NgayDanhSoGioiHan=@NgayDanhSoGioiHan

  

END


```
