# Stored Procedure: `ThucChay_Mobile_Job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-02-11 14:53:13.100000
- **Ngày sửa cuối**: 2025-10-27 09:53:40.803000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:    <Author,,Name>
-- Create date: <Create Date,,>
-- Description:  <Description,,>
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_Mobile_Job]
AS
BEGIN
  DECLARE @dtStart DATETIME, @dtEnd DATETIME,  @NgayDanhSoGioiHan DATE

  SET @dtStart = (
          SELECT TOP 1 tcdt.NgayThucHien
          FROM ABM_data_thucchay.dbo.ThucChayDaTinh tcdt
          INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct  ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
          WHERE  tcdt.DmSanPhamREF = 342
              AND NOT (tcdt.DmHinhThucQuangCao in (13,42) or tcdt.DmLoaiBannerREF in (17,18))
              AND tcdt.DotChayHopDong NOT in ( N'NGAY', N'CPM_DonViGoi',N'Tính mới CPM DonViGoi')
          ORDER BY tcdt.NgayThucHien desc
           )  
  SET @dtStart =  DATEADD(dd,1, @dtStart)
  SET @dtStart = CONVERT(DATE, @dtStart)

  SET @dtEnd = CONVERT(DATE,GETDATE())
  SET @dtEnd = DATEADD(dd,-1, @dtEnd)
  
  SET @NgayDanhSoGioiHan = DATEADD(YEAR, -3, @dtStart)

  EXEC [dbo].[ThucChay_mobile_Update_HopDongChiTietAndBanner] @EndDate = @dtEnd, @NgayDanhSoGioiHan = @NgayDanhSoGioiHan


  EXEC [dbo].[ThucChay_Mobile_GhiNhanThayDoi_ThucChayDaTinh] @NgayGhiNhan = @dtEnd, @NgayCheckThayDoi=@dtEnd, @NgayDanhSoGioiHan=@NgayDanhSoGioiHan
  EXEC [dbo].[ThucChay_Mobile_GhiNhanPhatSinh_ThucChayDaTinh] @NgayThucHien = @dtEnd, @NgayDanhSoGioiHan=@NgayDanhSoGioiHan

  

END


```
