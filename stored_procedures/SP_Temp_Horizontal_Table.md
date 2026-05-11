# Stored Procedure: `Temp_Horizontal_Table`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-09 15:33:08.387000
- **Ngày sửa cuối**: 2014-10-14 10:39:56.977000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC Temp_Horizontal_Table
AS
	SELECT
	b.TenWebsite, b.DmWebsiteREF 
	, sum(b.Adpage)Adpage, SUM(b.Sponsorpost)Sponsorpost, SUM(b.DangTin)DangTin
	, SUM(b.BalloonAds)BalloonAds , SUM(b.TVCOnline)TVCOnline
	, SUM(b.CPMMass)CPMMass, SUM(b.Mobile)Mobile
	, SUM(b.BannerCPD)BannerCPD
	, SUM(b.BannerCPDChuyentrang)BannerCPDChuyentrang
	, SUM(b.BoxappCPD)BoxappCPD
	, SUM(b.BoxappCPM)BoxappCPM
	, SUM(b.BoxappSelfServing)BoxappSelfServing
	, SUM(b.BoxappMultiBrand)BoxappMultiBrand
	, SUM(b.CPCAdmarket)CPCAdmarket
	, SUM(b.CPC_Plus)CPC_Plus
	, SUM(b.CPA)CPA
	, SUM(b.CPM_Admarket)CPM_Admarket
	, SUM(b.Google_Ads)Google_Ads
	, (SUM(b.Baotrothongtin) + SUM(b.BoxappGiaVang)
		+ SUM(b.ChiPhiHosting) + SUM(b.ChiPhiKhac)
		+ SUM(b.KhaosatThiTruongOnline) + SUM(b.ChiPhiQuanLy)
		+ SUM(b.ChiPhiSanXuat) + SUM(b.ChiPhiThietKe)
		+ SUM(b.CPM_Chuyentrang) + SUM(b.CPMMulti)
		+ SUM(b.FacebookAds) + SUM(b.Forum_Seeding)
		+ SUM(b.GiaoLuuTrucTuyen) + SUM(b.HDNguyenTac)
		+ SUM(b.Luotup) + SUM(b.MuaNgoaiKhac)
		+ SUM(b.TaiTro) + SUM(b.TinNoiBat) + SUM(b.TinVip) + SUM(b.SPKhac)) SPkhac
	FROM 
	(
	SELECT 
	( CASE WHEN (a.DmSanPhamREF = 305) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
	  END 
  
	) Adpage
	,
	( CASE WHEN (a.DmSanPhamREF = 339) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) BalloonAds
	,
	( CASE WHEN (a.DmSanPhamREF = 140) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) BannerCPD
	,
	( CASE WHEN (a.DmSanPhamREF = 549) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) BannerCPDChuyentrang
	,
	( CASE WHEN (a.DmSanPhamREF = 245) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) Baotrothongtin
	,
	( CASE WHEN (a.DmSanPhamREF = 339 AND a.TenHinhThucQuangCao = 'CPD') THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) BoxappCPD
	,
	( CASE WHEN (a.DmSanPhamREF = 370 AND a.TenHinhThucQuangCao = 'CPM') THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) BoxappCPM
	,
	( CASE WHEN (a.DmSanPhamREF = 370 AND a.DmHinhThucQuangCao = 26) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) BoxappSelfServing
	, 
	( CASE WHEN (a.DmSanPhamREF = 564) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) BoxappMultiBrand
	,
	( CASE WHEN (a.DmSanPhamREF = 385) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) BoxappGiaVang
	,
	( CASE WHEN (a.DmSanPhamREF = 252) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) ChiPhiHosting
	,
	( CASE WHEN (a.DmSanPhamREF = 253) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) ChiPhiKhac
	,
	( CASE WHEN (a.DmSanPhamREF = 561) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) KhaosatThiTruongOnline
	,
	( CASE WHEN (a.DmSanPhamREF = 535) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) ChiPhiQuanLy
	,
	( CASE WHEN (a.DmSanPhamREF = 560) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) ChiPhiSanXuat
	,
	( CASE WHEN (a.DmSanPhamREF = 251) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) ChiPhiThietKe
	,
	( CASE WHEN (a.DmSanPhamREF = 420) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) CPA
	,
	( CASE WHEN (a.DmSanPhamREF = 144) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) CPCAdmarket
	,
	( CASE WHEN (a.DmSanPhamREF = 299) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) CPC_Plus
	,
	( CASE WHEN (a.DmSanPhamREF = 337) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) CPM_Admarket
	,
	( CASE WHEN (a.DmSanPhamREF = 231) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) CPM_Chuyentrang
	,
	( CASE WHEN (a.DmSanPhamREF = 238) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) CPMMass
	,
	( CASE WHEN (a.DmSanPhamREF = 531) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) CPMMulti
	,
	( CASE WHEN (a.DmSanPhamREF = 141) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) DangTin
	,
	( CASE WHEN (a.DmSanPhamREF = 306) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) FacebookAds
	,
	( CASE WHEN (a.DmSanPhamREF = 563) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) Forum_Seeding
	,
	( CASE WHEN (a.DmSanPhamREF = 250) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) GiaoLuuTrucTuyen
	,
	( CASE WHEN (a.DmSanPhamREF = 423) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) Google_Ads
	,
	( CASE WHEN (a.DmSanPhamREF = 269) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) HDNguyenTac
	,
	( CASE WHEN (a.DmSanPhamREF = 242) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) Luotup
	,
	( CASE WHEN (a.DmSanPhamREF = 342) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) Mobile
	,
	( CASE WHEN (a.DmSanPhamREF = 247) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) MuaNgoaiKhac
	,
	( CASE WHEN (a.DmSanPhamREF = 381) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) Sponsorpost
	,
	( CASE WHEN (a.DmSanPhamREF = 271) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) TaiTro
	,
	( CASE WHEN (a.DmSanPhamREF = 243) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) TinNoiBat
	,
	( CASE WHEN (a.DmSanPhamREF = 241) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) TinVip
	,
	( CASE WHEN (a.DmSanPhamREF = 240) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) TVCOnline
	,
	( CASE WHEN (a.DmSanPhamREF NOT IN (240,241,243,271,381,247,342,242,269,423,250,563,306,141,531,238,231,337,
		299,144,420,251,560,535,561,253,252,385,564,370,339,245,549,140,339,305)) THEN (a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)
		ELSE 0 
		END
	) SPKhac
	, a.DmWebsiteREF
	, a.TenWebsite
	, a.DmSanPhamREF  
	FROM ThucChayDaTinh a
	WHERE CONVERT(DATE,a.NgayThucHien) = '2013-01-02'
	)b
	WHERE b.DmWebsiteREF IN 
	(
		SELECT rptDmWebsite.DmWebsiteID FROM rptDmWebsite
	)
	GROUP BY b.DmWebsiteREF, b.TenWebsite
```
