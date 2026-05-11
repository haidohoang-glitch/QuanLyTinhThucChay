# Stored Procedure: `ThucChay_InsertToTemp_Sponsor`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-01 15:55:32.043000
- **Ngày sửa cuối**: 2015-04-02 14:31:10.717000

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
CREATE PROCEDURE [dbo].[ThucChay_InsertToTemp_Sponsor]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	--XOA DU LIEU TRUOC KHI INSERT
	DELETE FROM ThucChay_SponsorTemp WHERE NgayThucHien = @NgayThucHien 
	--INSERT DU LIEU
	INSERT INTO ThucChay_SponsorTemp	
	select [ThucChayID]
      ,dbo.ThucChay_FormatSoHopDong([SoHopDong])
      ,[DanhsachDmBookingREF]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmNhomWebsiteREF]
      ,[TenNhomWebsite]
      ,[DmWebsiteREF]
      ,dbo.ThucChay_FormatDomainName([TenWebsite])[TenWebsite]
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
       from ThucChay 
		where 
		TypeProduct =-1 AND
		DmWebsiteREF != 0 AND			
		Convert(nvarchar(50),NgayThucHien,103)  = Convert(nvarchar(50),@NgayThucHien,103)
END

```
