# Stored Procedure: `ThucChay_InsertToTemp_MobileAllTime_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-05-24 10:19:25.823000
- **Ngày sửa cuối**: 2016-05-24 10:20:16.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [ThucChay_InsertToTemp_Mobile] '2014-02-01'
CREATE PROCEDURE [dbo].[ThucChay_InsertToTemp_MobileAllTime_BySoHopDong]
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@SoHopDong NVARCHAR(50)
AS
BEGIN
	--XOA DU LIEU TRUOC KHI INSERT
	DELETE FROM ThucChay_MobileTemp WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
	AND SoHopDong = @SoHopDong
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
      ,@EndDate[NgayThucHien]
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
		Convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
		AND SoHopDong = @SoHopDong
		
END

```
