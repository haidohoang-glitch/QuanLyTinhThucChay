# Stored Procedure: `ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-11-22 16:20:15.083000
- **Ngày sửa cuối**: 2025-03-11 16:22:08.393000

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

CREATE PROCEDURE [dbo].[ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh] 
    @NgayGhiNhan DATE,
	@NgayPhatSinh_Tu DATE ,
	@NgayPhatSinh_Den DATE,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

	DECLARE @GhiChu NVARCHAR(MAX)
	SET @GhiChu = N'Tính mới: SP tối ưu [dbo].[ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh]'

	IF @SoHopDong IS NOT NULL
	BEGIN
		SET @GhiChu = @GhiChu + N' do xử lý tay'
		SET @NgayDanhSoGioiHan = NULL
	END


	DELETE FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien) = @NgayGhiNhan
		  AND (EXISTS(SELECT TOP (1) ch.ID FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
										   WHERE ch.DmSanPhamREF = ABM_Data_ThucChay.dbo.ThucChayDaTinh.DmSanPhamREF
												 AND ch.NhomTinhDoanhSoThucChay = 2 
												 AND ch.DeletedStatus = 0 
										   ORDER BY ch.ID))
		  AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 
		  AND NOT ( DmLoaiBannerREF IN (17,18) OR DmHinhThucQuangCao IN (13,42))
		  AND DonViTinh <> N'TRUE REACH'
		  AND DotChayHopDong = N'Tính mới CPM thuần'
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
			TongSoBaiViet INT,

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

			TongViewThucChay,
			TongClickThucChay,
			TongSoBaiViet,

			SoLuongThucChay )
	SELECT  tc.ID,
			tc.DmWebsiteREF,
			tc.TenWebsite,
			tc.DmBannerREF,
			tc.TypeProduct,
			@NgayGhiNhan,
			tchdctab.HopDongChiTietREF,
			
			ISNULL(tc.TongViewThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0) ,
			ISNULL(tc.TongClickThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0),
			ISNULL(tc.TongSoBaiViet,0),

			CASE WHEN UPPER (hdct.donvitinh) IN ('CPM', 'TRUE REACH', 'CPV')
					 THEN ISNULL(tc.TongViewThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0) 
					 WHEN UPPER (hdct.donvitinh) = 'CPC'
					 THEN ISNULL(tc.TongClickThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0)
					 ELSE 0
			END  
	FROM ABM_Data_ThucChay.dbo.thucchay tc
	INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdctab ON tchdctab.DmBannerID = CONVERT(NVARCHAR(50),tc.DmBannerREF) 
																				 AND tchdctab.DeletedStatus = 0
    INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK
	WHERE   hd.TrangThaiHopDong != 3
			AND hd.DeletedStatus = 0
			AND (EXISTS(SELECT TOP (1) ch.ID 
						FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
						WHERE	ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 2 
								AND ch.DeletedStatus = 0 
							))
			AND hdct.DmLoaiBannerREF NOT IN (17,18) 
			AND hdct.DmLoaiREF <> 13  
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3 
			AND CONVERT(DATE,tc.NgayThucHien) BETWEEN @NgayPhatSinh_Tu AND @NgayPhatSinh_Den
			AND tc.TypeProduct NOT IN (1,2,17, -3, 10)
			AND tc.DmWebsiteREF <> 0
			AND tc.SoHopDong NOT IN (N'HD DEMO',N'TONGSANPHAM')
			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
			AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
			AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)

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
	             FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
				 WHERE tcdt.NgayThucHien <= @NgayGhiNhan AND
					   tcdt.HopDongChiTietREF = temp.HopDongChiTietREF
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
	DECLARE @Thucchay_CPMthuan_DmTinhMoi DataType_Thucchay_CPMthuan_DmTinhMoi


	INSERT INTO @Thucchay_CPMthuan_DmTinhMoi
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
		   TongSoBaiViet = SUM(ISNULL(tcgn.TongSoBaiViet,0)) ,

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

	EXEC dbo.ThucChay_CPM_Insert_ThucChayDaTinh @Thucchay_CPMthuan_DmTinhMoi
		
	DROP TABLE #DmThucChay
	
END

```
