# Stored Procedure: `ThucChay_InsertToTemp_Mobile_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-26 11:02:28.130000
- **Ngày sửa cuối**: 2016-11-26 11:03:25.107000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [ThucChay_InsertToTemp_Mobile_BySoHopDong] '2016-11-14','QC1871016'
CREATE PROCEDURE [dbo].[ThucChay_InsertToTemp_Mobile_BySoHopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
	,@SoHopDong NVARCHAR(50)
AS
BEGIN
	--XOA DU LIEU TRUOC KHI INSERT
	DELETE FROM ThucChay_MobileTemp WHERE NgayThucHien = @NgayThucHien AND dbo.ThucChay_FormatSoHopDong([SoHopDong]) = @SoHopDong
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
      ,IsNoiBo
       from ThucChay 
		where 
		TypeProduct = 10 AND
		DmWebsiteREF != 0 AND			
		Convert(date,NgayThucHien)  = Convert(date,@NgayThucHien)
		AND dbo.ThucChay_FormatSoHopDong([SoHopDong]) = @SoHopDong
END

```
