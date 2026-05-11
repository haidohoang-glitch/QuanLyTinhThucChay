# Stored Procedure: `ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-04-15 10:06:40.263000
- **Ngày sửa cuối**: 2025-10-28 09:46:34.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |
| `@NgayCheckThayDoi` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

/*
EXEC dbo.[ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh] @NgayGhiNhan = '2025-09-30',       -- date
                                                         @SoHopDong = N'P3940825',                  -- nvarchar(50)
                                                         @HopDongChiTietID = 767388              -- int
*/

CREATE PROCEDURE [dbo].[ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh]
    @NgayGhiNhan DATE,
	@NgayCheckThayDoi DATE = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN
    IF @SoHopDong IS NOT NULL 
	BEGIN 
		SET @NgayDanhSoGioiHan = NULL
		SET @NgayCheckThayDoi = NULL
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
		  AND DotChayHopDong IN (N'Đối trừ CPM', N'Tính lại CPM')
		  AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
		  AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)


	--========================================= 1. Xác định phân bổ thay đổi tỉ lệ/banner và pb có thay đổi số lượng, đơn giá, chiết khấu ==============================
    CREATE TABLE #DmPBThayDoi (
					NgayThucHien DATETIME,
					HopDongID INT,
					HopDongChiTietREF INT,
					LoaiThayDoi INT,     --1: thay đổi thông tin hợp đồng, 2: phân bổ hủy, 3: pb thay đổi tỷ lệ / banner
					LyDo NVARCHAR(MAX)
					)
	BEGIN
		-- phân bổ thay đổi thông tin
        INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongID,
						--DmSanPhamREF,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo
        )
        SELECT DISTINCT @NgayGhiNhan,
                        hd.HopDongID ,
                        --hdcttd.DmSanPhamREF ,
                        hdct.HopDongChiTietID,
						LoaiThayDoi = IIF(hdct.DeletedStatus = 1 OR  hd.TrangThaiHopDong = 3, 2, 1),
						LyDo = CASE WHEN hd.TrangThaiHopDong = 3
									THEN N'hợp đồng hủy'
									WHEN hdct.DeletedStatus = 1
									THEN N'phân bổ bị xóa'
									ELSE N'phân bổ thay đổi số lượng'
							   END 
        FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
		WHERE(CONVERT(DATE, hd.LastModifiedAt) =  @NgayCheckThayDoi OR CONVERT(DATE, hdct.LastModifiedAt) =  @NgayCheckThayDoi)  AND 
			 (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan ) AND
			 EXISTS(SELECT TOP (1) ch.ID 
					FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
					WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
							AND ch.NhomTinhDoanhSoThucChay = 2 
							AND ch.DeletedStatus = 0 
					ORDER BY ch.ID ) AND
			 NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) AND
			 ( [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 3 ) AND
			 [dbo].[ThucChay_CheckSanPhamBoxAppSelfServing](hdct.DmSanPhamREF, ISNULL(hdct.TenViTri, '')) = 0

		-- loại TH phân bổ có thay đổi thông tin nhưng không thay đổi số lượng đánh số
		DELETE dm
		FROM #DmPBThayDoi dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietREF
		OUTER APPLY (SELECT TOP 1 SoLuong, DonGia, ChietKhau
					 FROM ABM_Data_ThucChay.dbo.HopDongChiTietLog l 
					 WHERE LastModifiedAt < @NgayCheckThayDoi AND 
						   l.HopDongChiTietREF = dm.HopDongChiTietREF
					 ORDER BY HopDongChiTietLogID desc ) l 
		WHERE (hdct.soluong = ISNULL(l.SoLuong, hdct.SoLuong)) 
		AND (hdct.DonGia = ISNULL(l.DonGia, hdct.DonGia)) 
		AND (hdct.ChietKhau = ISNULL(l.ChietKhau, hdct.ChietKhau)) 
		AND (dm.LoaiThayDoi = 1)


		-- phân bổ bị ảnh hưởng tỉ lệ hopdongchitiet/banner do phân bổ phía trên thay đổi
		INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongID,
						--DmSanPhamREF,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo )
		SELECT DISTINCT
			   @NgayGhiNhan,
		       tchdctab.HopDongREF,
			   tchdctab.HopDongChiTietREF,
			   LoaiThayDoi = 3,
			   LyDo = N'tỉ lệ phân bổ trên banner thay đổi'
		FROM ( SELECT tchdctab.DmBannerID
			   FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdctab
			   WHERE EXISTS (SELECT HopDongChiTietREF 
							 FROM #DmPBThayDoi dm 
							 WHERE dm.HopDongChiTietREF = tchdctab.HopDongChiTietREF ) 
					 AND DaThucHienUpdateTiLe = 1 ) b
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdctab ON b.DmBannerID = tchdctab.DmBannerID 
		INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = tchdctab.HopDongREF
		WHERE tchdctab.HopDongChiTietREF NOT IN (SELECT HopDongChiTietREF FROM #DmPBThayDoi dm )
		      AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
			 AND EXISTS(SELECT TOP (1) ch.ID 
					FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
					WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
							AND ch.NhomTinhDoanhSoThucChay = 2 
							AND ch.DeletedStatus = 0 
					ORDER BY ch.ID ) 
			 AND NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) 
			 AND ( [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 3 ) 
			 AND [dbo].[ThucChay_CheckSanPhamBoxAppSelfServing](hdct.DmSanPhamREF, ISNULL(hdct.TenViTri, '')) = 0

		IF @SoHopDong IS NOT NULL 
		BEGIN
			INSERT INTO #DmPBThayDoi
			(
				NgayThucHien,
				HopDongID,
				HopDongChiTietREF,
				LoaiThayDoi,
				LyDo
			)
			SELECT @NgayGhiNhan,
			       hd.HopDongID,
				   hdct.HopDongChiTietID,
				   LoaiThayDoi = IIF(hdct.DeletedStatus = 1 OR  hd.TrangThaiHopDong = 3, 2, 1),
				   LyDo = CASE WHEN hd.TrangThaiHopDong = 3
									THEN N'xử lý tay hợp đồng hủy'
									WHEN hdct.DeletedStatus = 1
									THEN N'xử lý tay phân bổ bị xóa'
									ELSE N'xử lý tay phân bổ'
							   END 
			FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
		    INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID
			WHERE hd.SoHopDong = @SoHopDong AND
                  (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID) AND 
				  EXISTS(SELECT TOP (1) ch.ID 
						 FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
						 WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 2 
								AND ch.DeletedStatus = 0 
						 ORDER BY ch.ID ) AND
				  NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) AND
				  [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 3  AND
				  [dbo].[ThucChay_CheckSanPhamBoxAppSelfServing](hdct.DmSanPhamREF, ISNULL(hdct.TenViTri, '')) = 0 AND
                  hdct.HopDongChiTietID NOT IN (SELECT HopDongChiTietREF FROM #DmPBThayDoi)
		END

		

	END	
     
	--========================================= 2. Xác định thucchayID của các phân bổ trên ====================================================================================================================
	CREATE TABLE #DmTinhLai 
				(	ThucChayID INT,
					DmNhanHangREF NVARCHAR(MAX),
					DmWebsiteREF BIGINT,
					TenWebsite NVARCHAR(MAX),
					DmBannerREF INT,
					DmSanPhamREF INT, 
					TenSanPham NVARCHAR(200),
					NgayThucHien DATETIME,
					HopDongChiTietREF INT,

					SoLuongDanhSoPhanBo INT,
					SoLuongThucChay INT,
					SoLuongThucChay_GhiNhan INT,
					SoLuongLechTreoHa INT,

					LyDo NVARCHAR(MAX))
	INSERT INTO #DmTinhLai
	(				ThucChayID,
					DmWebsiteREF,
					TenWebsite,
					DmBannerREF,
					DmSanPhamREF , 
					TenSanPham ,
					NgayThucHien ,
					HopDongChiTietREF ,

					SoLuongThucChay,
					SoLuongDanhSoPhanBo,

					LyDo)
	SELECT  tc.ID,
			tc.DmWebsiteREF,
			tc.TenWebsite,
			tc.DmBannerREF,
			dbo.GetProductIDByTypeProduct(tc.TypeProduct), 
			dbo.GetProductNameByTypeProduct(tc.TypeProduct),
			@NgayGhiNhan,
			tchdctab.HopDongChiTietREF,
			--hdct.DmSanPhamREF,
			CASE WHEN UPPER (hdct.donvitinh) IN ('CPM', 'TRUE REACH', 'CPV')
						THEN ISNULL(tc.TongViewThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0) 
						WHEN UPPER (hdct.donvitinh) = 'CPC'
						THEN ISNULL(tc.TongClickThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0)
						ELSE 0
			END ,
			hdct.SoLuong*IIF(UPPER(LTRIM(RTRIM(hdct.DonViTinh)))= N'CPM', 1000, 1) ,
			dm.LyDo 
	FROM ABM_Data_ThucChay.dbo.thucchay tc
	INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdctab ON tchdctab.DmBannerID = CONVERT(NVARCHAR(50),tc.DmBannerREF) 
																				 AND tchdctab.DeletedStatus = 0
	INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tchdctab.HopDongChiTietREF 
	INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK and hd.SoHopDong = tc.SoHopDong
	WHERE   hd.TrangThaiHopDong <> 3
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
			AND CONVERT(DATE,tc.NgayThucHien) <= @NgayGhiNhan
			AND tc.TypeProduct NOT IN (1,2,17, -3, 10)
			AND tc.DmWebsiteREF <> 0
			AND tc.SoHopDong NOT IN (N'HD DEMO',N'TONGSANPHAM')
			AND dm.LoaiThayDoi IN (1,3)
	
	UPDATE dm
	SET dm.DmNhanHangREF = ISNULL(tchdct.DmNhanHangREF, '')
	FROM #DmTinhLai dm
	OUTER APPLY  (SELECT STUFF ((   SELECT DISTINCT  ',' + tchdct.DmNhanHangREF
									FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
									WHERE DeletedStatus = 0 AND 
										  tchdct.HopDongChiTietREF = dm.HopDongChiTietREF AND 
										  tchdct.DmBannerREF = CONVERT(NVARCHAR(50),dm.DmBannerREF) 
									FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 
									1, 1, '') AS DmNhanHangREF
							) tchdct



	--========================================= 3. Xác định lệch treo hạ và ghi nhận của các thucchayID trên ==========================
	;WITH CTE_Base AS (
		SELECT 
			ThucChayID,
			SoLuongThucChay,
			SoLuongDanhSoPhanBo,
			HopDongChiTietREF,
			ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ThucChayID) AS RowNum
		FROM #DmTinhLai
	),
	CTE_Recursive AS (
		SELECT 
			ThucChayID,
			SoLuongThucChay,
			SoLuongDanhSoPhanBo,
			HopDongChiTietREF,
			RowNum,
			TichLuyGhiNhan = IIF (SoLuongThucChay>= SoLuongDanhSoPhanBo,SoLuongDanhSoPhanBo, SoLuongThucChay ), -- Giá trị của hàng đầu tiên
			ThucChayGhiNhan = IIF (SoLuongThucChay>= SoLuongDanhSoPhanBo,SoLuongDanhSoPhanBo, SoLuongThucChay )
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
			TichLuyGhiNhan = IIF(r.TichLuyGhiNhan + b.SoLuongThucChay>=  b.SoLuongDanhSoPhanBo, 
								 b.SoLuongDanhSoPhanBo, r.TichLuyGhiNhan + b.SoLuongThucChay ), 
			ThucChayGhiNhan = IIF(r.TichLuyGhiNhan + b.SoLuongThucChay>=  b.SoLuongDanhSoPhanBo, 
								  b.SoLuongDanhSoPhanBo - r.TichLuyGhiNhan, b.SoLuongThucChay )
		FROM CTE_Base b
		INNER JOIN CTE_Recursive r
			ON r.HopDongChiTietREF = b.HopDongChiTietREF AND b.RowNum - 1 = r.RowNum 
	)

	UPDATE temp
	SET  SoLuongThucChay_GhiNhan = sl.ThucChayGhiNhan,
		 SoLuongLechTreoHa =  temp.SoLuongThucChay - sl.ThucChayGhiNhan
	FROM #DmTinhLai temp
	INNER JOIN CTE_Recursive sl ON sl.ThucChayID = temp.ThucChayID
	OPTION (MAXRECURSION 0);


	--========================================= 4. Tiến hành đối trừ  ===========================================================
	INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
	(
		ThucChayDaTinhID,
		HopDongID,
		SoHopDong,
		DmMaHopDongREF,
		TenMaHopDong,
		NgayDanhSoHopDong,
		NgayKyHopDong,
		NhanHopDong,
		NgayNhanBanFax,
		NgayNhanHopDongBanCung,
		NgayChuyenHopDongChoKeToan,
		So,
		Thang,
		Nam,
		GiaTriHopDong,
		CongNo,
		HopDongChiTietREF,
		DangSuDung,
		IsGiayPhep,
		TrangThaiHopDong,
		IsBanCung,
		DmPhongBanREF,
		TenPhongBan,
		DmBoPhanREF,
		TenBoPhan,
		DmNhomLamViecREF,
		TenNhomLamViec,
		DmDiaDiemLamViecREF,
		TenDiaDiemLamViec,
		SysNhanVienREF,
		TenDangNhap,
		TenNhanVien,
		TenKhachHang,
		NhanHang,
		DmNhomNganhREF,
		TenNhomNganh,
		DmHinhThucQuangCao,
		TenHinhThucQuangCao,
		DmSanPhamREF,
		TenSanPham,
		DmNhomWebsiteREF,
		TenNhomWebsite,
		DmChuyenMucREF,
		TenChuyenMuc,
		DmLoaiBannerREF,
		TenLoaiBanner,
		DmViTriREF,
		TenViTri,
		DotChayHopDong,
		SoLuongDotChayHD,
		DotChayBooking,
		SoLuongDotChayBooking,
		SoLuong,
		DonViTinh,
		DonGia,
		DonGiaTheoDonVi,
		ChietKhau,
		GiamGia,
		ThanhTien,
		TiLeTuVan,
		ChiPhiTuVan,
		IsKhuyenMai,
		KhuyenMai,
		DmBannerREF,
		DmChienDichREF,
		DmWebsiteREF,
		TenWebsite,
		TongViewThucChay,
		TongClickThucChay,
		TongSoBaiViet,
		SoLuongThucChay,
		NgayThucHien,
		GiaTriThayDoi,
		ThanhTienThucChayTruocTrietKhau,
		GiaTriTrietKhauThucChay,
		ThanhTienSauTrietKhauThucChay,
		GiaTriHoaHongThucChay,
		ThanhTienThucThu,
		ThanhTienKM,
		SoLuongThucChayKM,
		SoLuongThucChayLechTreoHa,
		ThanhTienLechTreoHa,
		CreatedAt,
		LastModifiedAt,
		IsPheDuyet,
		PheDuyetBy,
		PheDuyetAt,
		SoLuongThayDoi,
		SoLuongKMThayDoi,
		GiaTriKMThayDoi,
		GhiChu
	)
SELECT	  NEWID()
		, tcdt.HopDongID
		, SoHopDong
		, DmMaHopDongREF
		, TenMaHopDong
		, NgayDanhSoHopDong
		, NgayKyHopDong
		, NhanHopDong
		, NgayNhanBanFax
		, NgayNhanHopDongBanCung
		, NgayChuyenHopDongChoKeToan
		, So
		, Thang
		, Nam
		, GiaTriHopDong
		, CongNo
		, tcdt.HopDongChiTietREF
		, DangSuDung
		, IsGiayPhep
		, TrangThaiHopDong
		, IsBanCung
		, DmPhongBanREF
		, TenPhongBan
		, DmBoPhanREF
		, TenBoPhan
		, DmNhomLamViecREF
		, TenNhomLamViec
		, DmDiaDiemLamViecREF
		, TenDiaDiemLamViec
		, SysNhanVienREF
		, TenDangNhap
		, TenNhanVien
		, TenKhachHang
		, NhanHang
		, DmNhomNganhREF
		, TenNhomNganh
		, DmHinhThucQuangCao
		, TenHinhThucQuangCao
		, DmSanPhamREF
		, TenSanPham
		, DmNhomWebsiteREF
		, TenNhomWebsite
		, DmChuyenMucREF
		, TenChuyenMuc
		, DmLoaiBannerREF
		, TenLoaiBanner
		, DmViTriREF
		, TenViTri
		, N'Đối trừ CPM' AS DotChayHopDong
		, 0 AS SoLuongDotChayHD
		, '' AS DotChayBooking
		, 0 AS SoLuongDotChayBooking
		, SoLuong
		, DonViTinh
		, DonGia
		, DonGiaTheoDonVi
		, ChietKhau
		, GiamGia
		, ThanhTien
		, TiLeTuVan
		, ChiPhiTuVan
		, IsKhuyenMai
		, KhuyenMai
		, DmBannerREF
		, DmChienDichREF
		, DmWebsiteREF
		, TenWebsite
		, 0 TongViewThucChay
		, 0 TongClickThucChay
		, 0 TongSoBaiViet
		, 0 AS SoLuongThucChay
		, @NgayGhiNhan
		, -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi
		, 0 AS ThanhTienThucChayTruocTrietKhau
		, 0 AS GiaTriTrietKhauThucChay
		, 0 AS ThanhTienSauTrietKhauThucChay
		, 0 AS GiaTriHoaHongThucChay
		, 0 AS ThanhTienThucThu
		, 0 AS ThanhTienKM
		, 0 AS SoLuongThucChayKM
		, -SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa
		, -SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
		, GETDATE()
		, GETDATE()
		, 0 AS IsPheDuyet
		, '' AS PheDuyetBy
		, GETDATE() PheDuyetAt
		, -SUM(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi
		, -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi
		, -SUM(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi
		, N'Đối trừ: SP tối ưu [dbo].[ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh] do ' + dm.LyDo AS GhiChu
FROM    ABM_Data_ThucChay.dbo.thucchaydatinh tcdt
INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tcdt.HopDongChiTietREF 
WHERE   DmSanPhamREF IN ( 231, 238, 339, 240, 598, 613, 370, 680, 735, 5056 )
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	
		AND NOT ( DmLoaiBannerREF IN ( 17, 18 )
					OR DmHinhThucQuangCao IN ( 13, 42 ))
		AND DonViTinh <> N'TRUE REACH'
		AND tcdt.NgayThucHien <= @NgayGhiNhan
GROUP BY  tcdt.HopDongID
		, SoHopDong
		, DmMaHopDongREF
		, TenMaHopDong
		, NgayDanhSoHopDong
		, NgayKyHopDong
		, NhanHopDong
		, NgayNhanBanFax
		, NgayNhanHopDongBanCung
		, NgayChuyenHopDongChoKeToan
		, So
		, Thang
		, Nam
		, GiaTriHopDong
		, CongNo
		, tcdt.HopDongChiTietREF
		, DangSuDung
		, IsGiayPhep
		, TrangThaiHopDong
		, IsBanCung
		, DmPhongBanREF
		, TenPhongBan
		, DmBoPhanREF
		, TenBoPhan
		, DmNhomLamViecREF
		, TenNhomLamViec
		, DmDiaDiemLamViecREF
		, TenDiaDiemLamViec
		, SysNhanVienREF
		, TenDangNhap
		, TenNhanVien
		, TenKhachHang
		, NhanHang
		, DmNhomNganhREF
		, TenNhomNganh
		, DmHinhThucQuangCao
		, TenHinhThucQuangCao
		, DmSanPhamREF
		, TenSanPham
		, DmNhomWebsiteREF
		, TenNhomWebsite
		, DmChuyenMucREF
		, TenChuyenMuc
		, DmLoaiBannerREF
		, TenLoaiBanner
		, DmViTriREF
		, TenViTri
		, SoLuong
		, DonViTinh
		, DonGia
		, DonGiaTheoDonVi
		, ChietKhau
		, GiamGia
		, ThanhTien
		, TiLeTuVan
		, ChiPhiTuVan
		, IsKhuyenMai
		, KhuyenMai
		, DmBannerREF
		, DmChienDichREF
		, DmWebsiteREF
		, TenWebsite
		, dm.NgayThucHien
		, dm.LyDo

	--========================================= 5. Tiến hành tính lại
	DECLARE @Thucchay_CPMthuan_DmTinhlai DataType_Thucchay_CPMthuan_DmTinhlai
	INSERT INTO @Thucchay_CPMthuan_DmTinhlai
	(
	    HopDongChiTietREF,
		NgayThucHien,
		DmBannerREF,
		TenWebsite,
		DmWebsiteREF,
		DmNhanHangREF,
		DmSanPhamREF,
		TenSanPham,

	    SoLuongGhiNhan,
	    SoLuongLechTreoHa,
	    SoLuongKhuyenMai,

	    ThanhTienGhiNhan,
	    ThanhTienLechTreoHa,
	    ThanhTienKhuyenMai,

		LyDo
	)
	SELECT				tcgn.HopDongChiTietREF,
						tcgn.NgayThucHien,
						tcgn.DmBannerREF ,
						tcgn.TenWebsite,
						tcgn.DmWebsiteREF ,
						tcgn.DmNhanHangREF,
						tcgn.DmSanPhamREF,
						tcgn.TenSanPham,

						SoLuongGhiNhan = SUM(ISNULL(IIF(hdct.ChietKhau = 100, 0, tcgn.SoLuongThucChay_GhiNhan), 0)) ,
						SoLuongLechTreoHa = SUM(ISNULL(tcgn.SoLuongLechTreoHa, 0)),
						SoLuongKhuyenMai = SUM(ISNULL(IIF(hdct.ChietKhau = 100, tcgn.SoLuongThucChay_GhiNhan, 0), 0)),

						ThanhTienGhiNhan = SUM(ISNULL(IIF(hdct.ChietKhau = 100, 0, tcgn.SoLuongThucChay_GhiNhan*hdct.DonGia*(1-hdct.ChietKhau/100) / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)), 0)) ,
						ThanhTienLechTreoHa = SUM(ISNULL(tcgn.SoLuongLechTreoHa*hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh), 0)),
						ThanhTienKhuyenMai = SUM(ISNULL(IIF(hdct.ChietKhau = 100, tcgn.SoLuongThucChay_GhiNhan*hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh), 0), 0)),
						tcgn.LyDo
	FROM #DmTinhLai tcgn
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcgn.HopDongChiTietREF
	GROUP BY	tcgn.HopDongChiTietREF,
				tcgn.NgayThucHien,
				tcgn.DmBannerREF ,
				tcgn.TenWebsite,
				tcgn.DmWebsiteREF ,
				tcgn.DmNhanHangREF,
				tcgn.DmSanPhamREF,
				tcgn.TenSanPham,
				tcgn.LyDo,
				hdct.ChietKhau,
				hdct.DonGia,
				hdct.DonViTinh

	EXEC [dbo].[ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh] @Thucchay_CPMthuan_DmTinhlai

	DROP TABLE #DmTinhLai
	DROP TABLE #DmPBThayDoi

END

```
