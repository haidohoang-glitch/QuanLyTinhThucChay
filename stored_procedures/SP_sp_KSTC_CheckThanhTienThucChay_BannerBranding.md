# Stored Procedure: `sp_KSTC_CheckThanhTienThucChay_BannerBranding`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-09-23 11:34:41.923000
- **Ngày sửa cuối**: 2024-02-20 15:38:37.523000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--sp_KSTC_CheckThanhTienThucChay_BannerBranding 
CREATE PROCEDURE [dbo].[sp_KSTC_CheckThanhTienThucChay_BannerBranding] 
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	-- kingsize, Mobile, TVC
	select A.*, B.* from (
	select distinct tt.DmBannerREF, SoHopDong from ThucChayHopDongChiTiet tt 
	inner join HopDong hd on tt.HopDongREF = HopDongID
	left join HopDongChiTiet hdct on tt.HopDongChiTietREF = HopDongChiTietID and hdct.DeletedStatus <> 1
	where 1=1
	and DmHinhThucQuangCaoREF = 42 and tt.DeletedStatus =0
	--and len(tt.DmBannerREF) = 6 
	AND tt.DmBannerREF IN (SELECT DmBannerREF FROM dbo.ThucChayHopDongChiTiet WHERE LEN(DmBannerREF) = 6 AND CreatedBy LIKE N'%Branding%' ) ---Nhung sửa chỉ check vs các banner treo trên tool Branding
	AND tt.DmSanPhamREF not in (817,140)
	and NgayDanhSoHopDong>='2020-07-20'
	--
	and exists (select top 1 DmBannerREF from ThucChay tc where convert(nvarchar(10),tc.DmBannerREF) = tt.DmBannerREF and TypeProduct not in (1,-3))  
	--and tt.DmBannerREF = 574840
	)A

	full outer join
	(
	select distinct SoHopDong, DmBannerID from ThucChay_ThanhTien_Admatic 
	WHERE 	DmBannerID IN (SELECT DmBannerREF FROM dbo.ThucChayHopDongChiTiet WHERE LEN(DmBannerREF) = 6 AND CreatedBy LIKE N'%Branding%' ) ---Nhung sửa chỉ check vs các banner treo trên tool Branding
	AND DmSanPhamREF not in (5133,821)
	and DmBannerID not in (567461,567464,567497 --banner gắn vào pbo xóa
	)
	)B
	on A.DmBannerREF = B.DmBannerID
	where A.DmBannerREF is null or B.DmBannerID is null
	order by A.DmBannerREF, B.DmBannerID


	-- native, onimage
	select A.*, B.* from (
	select distinct tt.DmBannerREF, SoHopDong from ThucChayHopDongChiTiet tt 
	inner join HopDong hd on tt.HopDongREF = HopDongID
	left join HopDongChiTiet hdct on tt.HopDongChiTietREF = HopDongChiTietID and hdct.DeletedStatus <> 1
	where 1=1
	and DmHinhThucQuangCaoREF = 42 and tt.DeletedStatus =0
	--and tt.DmBannerREF >= 500000 --banner chạy trên tool Branding
	AND tt.DmBannerREF IN (SELECT DmBannerREF FROM dbo.ThucChayHopDongChiTiet WHERE LEN(DmBannerREF) = 6 AND CreatedBy LIKE N'%Branding%' ) ---Nhung sửa chỉ check vs các banner treo trên tool Branding
	AND tt.DmSanPhamREF not in (817,140)
	and NgayDanhSoHopDong>='2020-07-20'
	and year(NgayDanhSoHopDong)>=2021
	--
	and exists (select top 1 DmBannerID from ThucChay_Native_Ads tc where convert(nvarchar(10),tc.DmBannerID) = tt.DmBannerREF)  
	--and tt.DmBannerREF = 574840
	)A
	full outer join
	(
	select distinct tc.SoHopDong, DmBannerID from ThucChay_ThanhTien_Admatic tc
	inner join HopDong hd on hd.SoHopDong = tc.SoHopDong
	WHERE 1=1 --AND DmBannerID >= 500000  -- banner chạy trên tool Branding
	AND tc.DmBannerID IN (SELECT DmBannerREF FROM dbo.ThucChayHopDongChiTiet WHERE LEN(DmBannerREF) = 6 AND CreatedBy LIKE N'%Branding%' ) ---Nhung sửa chỉ check vs các banner treo trên tool Branding
	AND DmSanPhamREF  in (5133,821)
	and DmBannerID not in (567461,567464,567497 --banner gắn vào pbo xóa	
	)
	and year(NgayDanhSoHopDong)>=2021
	)B
	on A.DmBannerREF = B.DmBannerID
	where A.DmBannerREF is null or B.DmBannerID is null
	order by A.DmBannerREF, B.DmBannerID
  
END



```
