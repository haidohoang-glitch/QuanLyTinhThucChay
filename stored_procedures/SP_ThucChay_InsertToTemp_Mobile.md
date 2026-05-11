# Stored Procedure: `ThucChay_InsertToTemp_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-29 09:40:24.050000
- **Ngày sửa cuối**: 2023-07-15 08:48:14.950000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [ThucChay_InsertToTemp_Mobile] '2014-02-01'
CREATE PROCEDURE [dbo].[ThucChay_InsertToTemp_Mobile]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	--XOA DU LIEU TRUOC KHI INSERT
	DELETE FROM ThucChay_MobileTemp WHERE NgayThucHien = @NgayThucHien
	--INSERT DU LIEU
	--SELECT * FROM dbo.ThucChay_MobileTemp	
	--WHERE NgayThucHien = '2016-12-23'

	INSERT INTO ThucChay_MobileTemp	
	select [ThucChayID]
      ,ISNULL(dbo.ThucChay_FormatSoHopDong([SoHopDong]),0)SoHopDong
      ,[DanhsachDmBookingREF]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmNhomWebsiteREF]
      ,[TenNhomWebsite]
      ,[DmWebsiteREF]
      --,dbo.ThucChay_FormatDomainName([TenWebsite])[TenWebsite] --HAIDH CHO NAY CAN XEM LAI
	  ,[TenWebsite]
      ,[DmChienDichREF]
      ,[TenChienDich]
      ,[DmBannerREF]
      ,[TenBanner]
      ,[NgayThucHien]
      ,[TongViewThucChay]
      ,[TongClickThucChay]
      ,[CreatedBy]
      ,[CreatedAt]
      ,[LastModifiedBy]
      ,[LastModifiedAt]
      ,[DeletedStatus]
      ,[PrintStatus]
      ,[RecordStatus]
      ,[TongSoBaiViet]
      ,[SoThuTuTheoNgay]
      ,[TypeProduct]
      ,[BannerType]
      ,[UserName]
      ,[SaleName]
      ,[Email]
      ,[LastTimeCalc]
      ,[sys_date]
      ,[IsReady]
      ,[ProductUnitID]
      ,[ProductUnitName]
      ,[BannerTypeName]
      ,[HopDongChiTietREF]
      ,[CampainStatus]
      ,[BannerStatus]
      ,IsNoiBo
       from dbo.ThucChay 
	where 
	TypeProduct = 10 AND
	DmWebsiteREF <> 0 AND			
	Convert(date,NgayThucHien)  = Convert(date,@NgayThucHien)
END

```
