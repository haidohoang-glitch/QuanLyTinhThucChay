# Stored Procedure: `ThucChay_InsertToTemp_MobileByHopDongChiTietID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-29 11:35:36.037000
- **Ngày sửa cuối**: 2015-02-28 13:13:42.490000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@hdct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [ThucChay_InsertToTemp_Mobile] '2014-02-01'
CREATE PROCEDURE [dbo].[ThucChay_InsertToTemp_MobileByHopDongChiTietID]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@hdct INT
AS
BEGIN
	--XOA DU LIEU TRUOC KHI INSERT
	DELETE FROM ThucChay_MobileTemp WHERE NgayThucHien = @NgayThucHien AND
	 HopDongChiTietREF = @hdct;
	--INSERT DU LIEU
	INSERT INTO ThucChay_MobileTemp	
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
		TypeProduct IN (10) AND
		DmWebsiteREF != 0 AND		
		Convert(nvarchar(50),NgayThucHien,103)  = Convert(nvarchar(50),@NgayThucHien,103)  AND
		HopDongChiTietREF = @hdct;
END

```
