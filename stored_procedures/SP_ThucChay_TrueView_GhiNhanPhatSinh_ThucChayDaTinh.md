# Stored Procedure: `ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-07 17:16:53.667000
- **Ngày sửa cuối**: 2025-07-23 10:24:18.780000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |
| `@NgayPhatSinh_Tu` | `date(3)` | No |
| `@NgayPhatSinh_Den` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh] 
	@NgayGhiNhan DATE,
	@NgayPhatSinh_Tu DATE,
	@NgayPhatSinh_Den DATE,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

	DECLARE @GhiChu NVARCHAR(MAX)
	SET @GhiChu = N'Tính mới: SP tối ưu [dbo].[ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh]' + IIF(@SoHopDong IS NOT NULL, N' do xử lý tay', N'')

	DELETE FROM ABM_Data_ThucChay.dbo.thucchaydatinh
	WHERE	CONVERT(date,NgayThucHien) = @NgayGhiNhan
			AND DmSanPhamREF IN (240)
			AND (DonViTinh = N'True View' OR DonViTinh = N'TRUE REACH')
			AND DotChayHopDong = N'Tính mới TrueView'
		    AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
		    AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)
	--======================================= 1. Xác định dữ liệu cần insert ===============================
	CREATE TABLE #DmThucChay  ( 
			ThucChayID INT,
			DmNhanHangREF NVARCHAR(MAX), 
			DmWebsiteREF INT,
			TenWebsite NVARCHAR(MAX),
			DmBannerREF INT,
			TypeProduct INT, 
		    NgayThucHien DATETIME,
			HopDongChiTietREF INT,

			TongViewThucChay INT,
			TongClickThucChay INT,
			TongTrueView INT,

			SoLuongDanhSoPhanBo INT,
			SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien INT,
			SoLuongLechTreohaDaTinhPhanBo_TrcNgayThucHien INT,
			SoLuongThucChay INT,
			SoLuongThucChay_GhiNhan INT,
			SoLuongLechTreoHa INT)

	INSERT INTO #DmThucChay( 
			ThucChayID,
			DmWebsiteREF,
			TenWebsite,
			DmBannerREF,
			TypeProduct,
		    NgayThucHien ,
			HopDongChiTietREF ,
			
			TongViewThucChay ,
			TongClickThucChay ,
			TongTrueView ,

			SoLuongThucChay )
	SELECT  tc.ID,
	        tc.SiteID,
			tc.SiteName,
			tc.bannerid,
			tc.TypeProduct,
			@NgayGhiNhan,
			tchdctab.HopDongChiTietREF,

			ISNULL(tc.Views * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0),
			ISNULL(tc.Clicks * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0),
			ISNULL(tc.True_View * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0),

			ISNULL(tc.True_View * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0)
	FROM ABM_Data_ThucChay.dbo.ThucChayTrueView tc
	INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.SoHopDong = tc.SoHopDong
	INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdctab ON tchdctab.DmBannerID = CONVERT(NVARCHAR(50),tc.bannerid) 
																		         AND tchdctab.DeletedStatus = 0
																				 AND hd.HopDongID = tchdctab.HopDongREF
    INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF AND 
													        (tc.DmSanPhamREF = hdct.DmSanPhamREF OR hdct.DmSanPhamREF = 733)
	WHERE   hd.TrangThaiHopDong != 3
			AND hd.DeletedStatus = 0
			AND hdct.DmSanPhamREF IN (240,733) 
			AND NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) 
			AND hdct.DonViTinhREF IN (31, 32)
			AND CONVERT(DATE,tc.NgayThucHien) BETWEEN @NgayPhatSinh_Tu AND @NgayPhatSinh_Den 
			AND CONVERT(DATE,tc.NgayThucHien) <= @NgayGhiNhan
			AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
			AND (@HopDongChiTietID is NULL OR tchdctab.HopDongChiTietREF = @HopDongChiTietID)
			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )

	UPDATE dm
	SET dm.DmNhanHangREF = ISNULL(tchdct.DmNhanHangREF, '')
	FROM #DmThucChay dm
	OUTER APPLY  (SELECT STUFF ((   SELECT DISTINCT  ',' + tchdct.DsNhanHangREF
									FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdct
									WHERE DeletedStatus = 0 AND 
										  tchdct.HopDongChiTietREF = dm.HopDongChiTietREF AND 
										  tchdct.DmBannerID = CONVERT(NVARCHAR(50),dm.DmBannerREF) 
									FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 
									1, 1, '') AS DmNhanHangREF
							) tchdct

	UPDATE temp
	SET temp.SoLuongDanhSoPhanBo = hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh),
		temp.SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien = ISNULL(tcdt.SoluongGhiNhanDaTinh, 0),
		temp.SoLuongLechTreohaDaTinhPhanBo_TrcNgayThucHien = ISNULL(tcdt.SoLuongLechTreoHaDaTinh, 0)
	FROM #DmThucChay temp
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = temp.HopDongChiTietREF
	OUTER APPLY (SELECT HopDongChiTietREF, SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi + tcdt.SoLuongKMThayDoi + tcdt.SoLuongThucChayKM) AS SoluongGhiNhanDaTinh,
						SUM(tcdt.SoLuongThucChayLechTreoHa) AS SoLuongLechTreoHaDaTinh
	             FROM ABM_Data_ThucChay.dbo.thucchaydatinh tcdt
				 WHERE tcdt.NgayThucHien <= @NgayGhiNhan AND 
					   tcdt.HopDongChiTietREF = temp.HopDongChiTietREF AND
					   tcdt.dmsanphamref IN (240,733) 
				 GROUP BY tcdt.HopDongChiTietREF ) tcdt



	--=============================================== 2. Xác định lệch treo hạ ==========================
	;WITH CTE_Base AS (
		SELECT 
		  ThucChayID,
		  SoLuongThucChay,
		  SoLuongDanhSoPhanBo,
		  SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien,
		  HopDongChiTietREF,
		  ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ThucChayID) AS RowNum
		FROM #DmThucChay
	  ),
	  CTE_Recursive AS (
		SELECT 
		  ThucChayID,
		  SoLuongThucChay,
		  SoLuongDanhSoPhanBo,
		  HopDongChiTietREF,
		  RowNum,
		  TichLuyGhiNhan = IIF (SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien + SoLuongThucChay>= SoLuongDanhSoPhanBo,
								SoLuongDanhSoPhanBo ,  SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien + SoLuongThucChay ),
		  ThucChayGhiNhan = IIF (SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien + SoLuongThucChay>= SoLuongDanhSoPhanBo,
								 SoLuongDanhSoPhanBo - SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien,  SoLuongThucChay ) 
		FROM CTE_Base
		WHERE RowNum = 1

		UNION ALL
		-- Tính toán đệ quy
		SELECT 
		  b.ThucChayID,
		  b.SoLuongThucChay,
		  b.SoLuongDanhSoPhanBo,
		  b.HopDongChiTietREF,
		  b.RowNum,
		  TichLuyGhiNhan = IIF(  r.TichLuyGhiNhan + b.SoLuongThucChay>=  b.SoLuongDanhSoPhanBo, 
								 b.SoLuongDanhSoPhanBo , r.TichLuyGhiNhan + b.SoLuongThucChay ),
		  ThucChayGhiNhan = IIF (r.TichLuyGhiNhan + b.SoLuongThucChay>= b.SoLuongDanhSoPhanBo,
								 b.SoLuongDanhSoPhanBo - r.TichLuyGhiNhan,  b.SoLuongThucChay )
		FROM CTE_Base b
		INNER JOIN CTE_Recursive r
				   ON r.HopDongChiTietREF = b.HopDongChiTietREF AND b.RowNum  - 1 = r.RowNum 
			  
	  )
  
	UPDATE temp
	SET  SoLuongThucChay_GhiNhan = sl.ThucChayGhiNhan,
		 SoLuongLechTreoHa =   temp.SoLuongThucChay - sl.ThucChayGhiNhan
	FROM #DmThucChay temp
	INNER JOIN CTE_Recursive sl ON sl.ThucChayID = temp.ThucChayID
	OPTION (MAXRECURSION 0);

	--=========================================== 3. INSERT ThucChayDaTinh
	DECLARE @Thucchay_TrueView_DmTinhMoi DataType_Thucchay_CPMthuan_DmTinhMoi


	INSERT INTO @Thucchay_TrueView_DmTinhMoi
	(
	    HopDongChiTietREF,
		NgayThucHien,
		DmBannerREF,
		TenWebsite,
		DmWebsiteREF,
		DmNhanHangREF,
		TypeProduct,

		TongViewThucChay,
		TongClickThucChay,
		TongSoBaiViet,

	    SoluongGhiNhan,
	    SoLuongLechTreoHa,
		GhiChu 
	)
	SELECT tcgn.HopDongChiTietREF,
		   tcgn.NgayThucHien,
		   tcgn.DmBannerREF,
		   tcgn.TenWebsite,
		   tcgn.DmWebsiteREF,
		   tcgn.DmNhanHangREF,
		   tcgn.TypeProduct,

		   TongViewThucChay = SUM(ISNULL(tcgn.TongViewThucChay,0)) ,
		   TongClickThucChay = SUM(ISNULL(tcgn.TongClickThucChay,0)) ,
		   TongTrueView = SUM(ISNULL(tcgn.TongTrueView,0)) ,

		   SoLuongGhiNhan = SUM(tcgn.SoLuongThucChay_GhiNhan),
		   SoLuongLechTreoHa = SUM(tcgn.SoLuongLechTreoHa),

		   GhiChu = @GhiChu
	FROM #DmThucChay tcgn
	GROUP BY   tcgn.HopDongChiTietREF,
			   tcgn.NgayThucHien,
			   tcgn.DmBannerREF,
			   tcgn.TenWebsite,
			   tcgn.DmWebsiteREF,
			   tcgn.DmNhanHangREF,
			   tcgn.TypeProduct
	HAVING SUM(tcgn.SoLuongThucChay_GhiNhan) <> 0 OR 
			SUM(tcgn.SoLuongLechTreoHa) <> 0 

	EXEC dbo.ThucChay_TrueView_Insert_ThucChayDaTinh @Thucchay_TrueView_DmTinhMoi
		
	DROP TABLE #DmThucChay
	
END

```
