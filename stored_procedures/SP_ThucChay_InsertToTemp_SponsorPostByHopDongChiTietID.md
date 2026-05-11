# Stored Procedure: `ThucChay_InsertToTemp_SponsorPostByHopDongChiTietID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-04 17:21:06.910000
- **Ngày sửa cuối**: 2015-03-28 09:44:13.750000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_InsertToTemp_SponsorPostByHopDongChiTietID]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongChiTietID INT
AS
BEGIN
	--XOA DU LIEU TRUOC KHI INSERT
	DELETE FROM ThucChay_SponsorPostTemp WHERE NgayThucHien = @NgayThucHien
	AND HopDongChiTietREF = @HopDongChiTietID;
	
	--INSERT DU LIEU
	INSERT INTO ThucChay_SponsorPostTemp	
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
      , IsNoiBo
       from ThucChay 
		where 
		DmSanPhamREF IN (381) AND
		DmWebsiteREF != 0 AND		
		Convert(nvarchar(50),NgayThucHien,103)  = Convert(nvarchar(50),@NgayThucHien,103)
		AND HopDongChiTietREF = @HopDongChiTietID;
END

```
