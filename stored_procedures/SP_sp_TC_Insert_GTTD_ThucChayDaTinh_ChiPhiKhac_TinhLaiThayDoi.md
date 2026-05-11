# Stored Procedure: `sp_TC_Insert_GTTD_ThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-15 10:08:04.203000
- **Ngày sửa cuối**: 2024-11-05 17:14:25.940000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucTreoID` | `nvarchar(2000)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@count` | `int(4)` | Yes |

## Definition (Source Code)

```sql
/*

DECLARE @KQ INT = 0
--- TINH LAI GIA TRI
EXEC [sp_TC_Insert_GTTD_ThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi] 550608, 616003, '2021-06-02', @KQ  OUTPUT

*/
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_Insert_GTTD_ThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi]
    @ThucTreoID NVARCHAR(1000),
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@count INT OUTPUT
AS
    BEGIN
	DECLARE @v_TongThucChayDaTinh BIGINT = 0,
	@v_GiaTriThucTreo BIGINT = 0,
	@v_ChietKhau FLOAT = 0,
	@v_ThanhTien BIGINT = 0,
	@v_DonGia FLOAT = 0,
	@v_SoLuong INT = 0

	DECLARE @TABLE_OP TABLE(ThucChayDaTinhID nvarchar(100),HopDongChitietID int)
	set @count = 0

	SELECT @v_ChietKhau = ChietKhau, @v_ThanhTien = ThanhTien 
	, @v_DonGia = DonGia, @v_SoLuong = SoLuong
	FROM dbo.HopDongChiTiet
	WHERE HopDongChiTietID = @HopDongChiTietID

	SET @v_TongThucChayDaTinh =
	ISNULL((
		SELECT (CASE WHEN @v_ChietKhau <> 100 THEN SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
		ELSE SUM(ThanhTienKM + GiaTriKMThayDoi)
		END)
   		FROM dbo.ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietID
	),0)

	SET @v_GiaTriThucTreo =
	(
		SELECT CASE WHEN @v_ChietKhau <> 100 THEN DonGia*SoLuongThucTreo*(100-ChietKhau)/100
		ELSE DonGia*SoLuongThucTreo
		END
		FROM dbo.ThucChayHopDongChiTiet
		WHERE ThucChayHopDongChiTietID = @ThucTreoID
		AND LoaiThucTreo = 'ChiPhi'
	)

	--PRINT @v_TongThucChayDaTinh
	--PRINT @v_GiaTriThucTreo
	--PRINT @v_ThanhTien
	--PRINT @v_ChietKhau
	--PRINT @v_DonGia
	--PRINT @v_SoLuong

	IF((((@v_TongThucChayDaTinh + @v_GiaTriThucTreo) <= @v_ThanhTien) AND @v_ChietKhau <> 100)
	OR (((@v_TongThucChayDaTinh + @v_GiaTriThucTreo) <= @v_DonGia*@v_SoLuong) AND @v_ChietKhau = 100)
	)
	BEGIN

			    INSERT  INTO dbo.ThucChayDaTinh
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
				OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.HopdongChiTietREF INTO @TABLE_OP
		SELECT NEWID() AS ThucChayDaTinhID , 
							TD.HopDongID ,
                            TD.SoHopDong ,
                            TD.DmMaHopDongREF ,
                            TD.TenMaHopDong , 
                            TD.NgayDanhSoHopDong ,
                            TD.NgayKyHopDong ,
                            TD.NhanHopDong ,
                            TD.NgayNhanBanFax ,
                            TD.NgayNhanHopDongBanCung ,
                            TD.NgayChuyenHopDongChoKeToan ,
                            TD.So ,
                            TD.Thang ,
                            TD.Nam , 
                            TD.GiaTriHopDong ,
                            TD.CongNo ,
                            TD.HopDongChiTietID ,
                            TD.DangSuDung ,
                            TD.IsGiayPhep ,
                            TD.TrangThaiHopDong ,
                            TD.IsBanCung , 
                            TD.DmPhongBanREF ,
                            TD.TenPhongBan ,
                            TD.DmBoPhanREF ,
                            TD.TenBoPhan ,
                            TD.DmNhomLamViecREF ,
                            TD.TenNhom ,
                            TD.DmDiaDiemLamViecREF ,
                            TD.TenDiaDiemLamViec ,
                            TD.SysNhanVienREF ,
                            TD.TenDangNhap ,
                            TD.TenNhanVien , 
                            TD.TenKhachHang , 
                            TD.NhanHang ,
                            TD.DmNhomNganhREF ,
                            TD.TenNhomNganh , 
                            TD.DmHinhThucQuangCao ,
                            TD.TenHinhThucQuangCao , 
                            TD.DmSanPhamREF ,
                            TD.TenSanPham ,
                            TD.DmNhomWebsiteREF ,
                            TD.TenNhomWebsite , 
                            TD.DmChuyenMucREF ,
                            TD.TenChuyenMuc ,
                            TD.DmLoaiBannerREF ,
                            TD.TenLoaiBanner ,
                            TD.DmViTriREF ,
                            TD.TenViTri ,
                            TD.DotChayHopDong ,
                            TD.SoLuongDotChayHD ,
                            TD.DotChayBooking ,
                            TD.SoLuongDotChayBooking , 
                            TD.SoLuong ,
                            TD.DonViTinh ,
                            TD.DonGia , 
                            TD.DonGiaTheoDonViTinh ,
                            TD.ChietKhau ,
                            TD.GiamGia ,
                            TD.ThanhTien ,
                            TD.TiLeTuVan ,
                            TD.ChiPhiTuVan ,
                            TD.IsKhuyenMai ,
                            TD.KhuyenMai ,
                            TD.DmBannerREF ,--A.DmBannerREF,
                            TD.DmChienDichREF ,--A.DmChienDichREF,
                            TD.DmWebsiteREF ,
                            TD.TenWebsite ,
                            TD.TongViewThucChay ,
                            TD.TongClickThucChay ,
                            TD.TongSoBaiViet ,
                            0 AS SoLuongThucChay ,
							TD.NgayThucHien ,
                            TD.ThanhTienSauTrietKhauThucChay AS GiaTriThayDoi ,
                            0 AS ThanhTienThucChayTruocTrietKhau ,
							0 AS GiaTriTrietKhauThucChay ,
							0 AS ThanhTienSauTrietKhauThucChay ,
							0 AS GiaTriHoaHongThucChay ,
							0 AS ThanhTienThucThu ,
							0 AS ThanhTienKM ,
							0 AS SoLuongThucChayKM ,
							0 AS SoLuongLechTreoHa ,
							0 AS ThanhTienLechTreoHa ,
							TD.CreatedAt ,
							TD.LastModifiedAt,
							TD.IsPheDuyet ,
							TD.PheDuyetBy ,
							TD.PheDuyetAt ,
							TD.SoLuongThucChay AS SoLuongThayDoi ,
							TD.SoLuongThucChayKM AS SoLuongKMThayDoi ,
							TD.ThanhTienKM AS GiaTriKMThayDoi ,
							TD.GhiChu 
				FROM (	SELECT  NEWID() AS ThucChayDaTinhID , 
							TD.HopDongID ,
                            TD.SoHopDong ,
                            TD.DmMaHopDongREF ,
                            TD.TenMaHopDong , 
                            TD.NgayDanhSoHopDong ,
                            TD.NgayKyHopDong ,
                            TD.NhanHopDong ,
                            TD.NgayNhanBanFax ,
                            TD.NgayNhanHopDongBanCung ,
                            TD.NgayChuyenHopDongChoKeToan ,
                            TD.So ,
                            TD.Thang ,
                            TD.Nam , 
                            TD.GiaTriHopDong ,
                            TD.CongNo ,
                            TD.HopDongChiTietID ,
                            TD.DangSuDung ,
                            TD.IsGiayPhep ,
                            TD.TrangThaiHopDong ,
                            TD.IsBanCung , 
                            TD.DmPhongBanREF ,
                            TD.TenPhongBan ,
                            TD.DmBoPhanREF ,
                            TD.TenBoPhan ,
                            TD.DmNhomLamViecREF ,
                            TD.TenNhom ,
                            TD.DmDiaDiemLamViecREF ,
                            TD.TenDiaDiemLamViec ,
                            TD.SysNhanVienREF ,
                            TD.TenDangNhap ,
                            TD.TenNhanVien , 
                            TD.TenKhachHang , 
                            TD.NhanHang ,
                            TD.DmNhomNganhREF ,
                            TD.TenNhomNganh , 
                            TD.DmHinhThucQuangCao ,
                            TD.TenHinhThucQuangCao , 
                            TD.DmSanPhamREF ,
                            TD.TenSanPham ,
                            TD.DmNhomWebsiteREF ,
                            TD.TenNhomWebsite , 
                            TD.DmChuyenMucREF ,
                            TD.TenChuyenMuc ,
                            TD.DmLoaiBannerREF ,
                            TD.TenLoaiBanner ,
                            TD.DmViTriREF ,
                            TD.TenViTri ,
                            TD.DotChayHopDong ,
                            TD.SoLuongDotChayHD ,
                            TD.DotChayBooking ,
                            TD.SoLuongDotChayBooking , 
                            TD.SoLuong ,
                            TD.DonViTinh ,
                            TD.DonGia , 
                            TD.DonGiaTheoDonViTinh ,
                            TD.ChietKhau ,
                            TD.GiamGia ,
                            TD.ThanhTien ,
                            TD.TiLeTuVan ,
                            TD.ChiPhiTuVan ,
                            TD.IsKhuyenMai ,
                            TD.KhuyenMai ,
                            TD.DmBannerREF ,--A.DmBannerREF,
                            TD.DmChienDichREF ,--A.DmChienDichREF,
                            TD.DmWebsiteREF ,
                            TD.TenWebsite ,
                            TD.TongViewThucChay ,
                            TD.TongClickThucChay ,
                            TD.TongSoBaiViet ,
                            TD.SoLuongThucChay ,
							TD.NgayThucHien ,
                            TD.GiaTriThayDoi ,
                            TD.ThanhTienThucChayTruocTrietKhau ,
							ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
										* TD.ChietKhau ) / 100, 0) AS GiaTriTrietKhauThucChay ,
							ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
										- ( TD.ThanhTienThucChayTruocTrietKhau
											* TD.ChietKhau ) / 100 ), 0) AS ThanhTienSauTrietKhauThucChay ,
							ISNULL(( ( TD.ThanhTienThucChayTruocTrietKhau
										- ( TD.ThanhTienThucChayTruocTrietKhau
											* TD.ChietKhau ) / 100 )
										* TD.TiLeTuVan ) / 100, 0) AS GiaTriHoaHongThucChay ,
							ISNULL(( TD.ThanhTienThucChayTruocTrietKhau
										- ( TD.ThanhTienThucChayTruocTrietKhau
											* TD.ChietKhau ) / 100
										- ( ( TD.ThanhTienThucChayTruocTrietKhau
											- ( TD.ThanhTienThucChayTruocTrietKhau
												* TD.ChietKhau ) / 100 )
											* TD.TiLeTuVan ) / 100 ), 0) AS ThanhTienThucThu ,
							( CASE WHEN ( ( TD.IsKhuyenMai = 1 )
											OR ( TD.ChietKhau = 100 )
										)
									THEN TD.ThanhTienThucChayTruocTrietKhau
									ELSE 0
								END ) AS ThanhTienKM ,
							( CASE WHEN ( ( TD.IsKhuyenMai = 1 )
											OR ( TD.ChietKhau = 100 )
										)
									THEN TD.SoLuong
									ELSE 0
								END ) AS SoLuongThucChayKM ,
							0 SoLuongLechTreoHa ,
							0 ThanhTienLechTreoHa ,
							GETDATE() AS CreatedAt ,
							GETDATE() AS LastModifiedAt,
							0 IsPheDuyet ,
							'' PheDuyetBy ,
							'' PheDuyetAt ,
							0 SoLuongThayDoi ,
							0 SoLuongKMThayDoi ,
							0 GiaTriKMThayDoi ,
							N'Tính lại sau đối trừ' GhiChu
						 FROM    ( SELECT 
								D.HopDongID ,
								D.SoHopDong ,
								D.DmMaHopDongREF ,
								D.TenMaHopDong , 
								D.NgayDanhSoHopDong ,
								D.NgayKyHopDong ,
								ISNULL(D.NhanHopDong, '') AS NhanHopDong ,
								D.NgayNhanBanFax ,
								D.NgayNhanHopDongBanCung ,
								D.NgayChuyenHopDongChoKeToan ,
								D.So ,
								D.Thang ,
								D.Nam , 
								D.GiaTriHopDong ,
								D.CongNo ,
								C.HopDongChiTietID ,
								D.DangSuDung ,
								D.IsGiayPhep ,
								D.TrangThaiHopDong ,
								D.IsBanCung , 
								D.DmPhongBanREF ,
								ISNULL(D.TenPhongBan, '') AS TenPhongBan ,
								D.DmBoPhanREF ,
								ISNULL(D.TenBoPhan, '') AS TenBoPhan ,
								D.DmNhomLamViecREF ,
								ISNULL(D.TenNhom, '') AS TenNhom ,
								D.DmDiaDiemLamViecREF ,
								D.TenDiaDiemLamViec ,
								D.SysNhanVienREF ,
								ISNULL(D.TenDangNhap, '') AS TenDangNhap ,
								D.TenNhanVien , 
								D.TenKhachHang , 
								C.DmNhanHangTreoREF NhanHang ,
								C.DmNhomNganhREF ,
								C.TenNhomNganh , 
								C.DmLoaiREF AS DmHinhThucQuangCao ,
								C.TenLoai AS TenHinhThucQuangCao , 
								C.DmSanPhamREF AS DmSanPhamREF ,
								E.TenSanPham ,
								C.DmNhomWebsiteREF ,
								C.TenNhomWebsite , 
								C.DmChuyenMucREF ,
								C.TenChuyenMuc ,
								C.DmLoaiBannerREF ,
								C.TenLoaiBanner ,
								C.DmViTriREF ,
								C.TenViTri ,
								'' DotChayHopDong ,
								0 AS SoLuongDotChayHD ,
								C.ThucChayHopDongChiTietID DotChayBooking ,
								0 AS SoLuongDotChayBooking , 
								C.SoLuongThucTreo AS SoLuong ,
								ISNULL(C.DonViTinh, N'đ/v') AS DonViTinh ,
								dbo.ThucChay_GetDonGiaByNgayThucHien(C.Ngay,C.HopDongChiTietID,C.DonGia) AS DonGia , 
								dbo.ThucChay_GetDonGiaByNgayThucHien(C.Ngay,C.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh ,
								C.ChietKhauThucTreo ChietKhau ,
								C.GiamGia ,
								C.ThanhTien ,
								C.TiLeTuVan ,
								C.ChiPhiTuVan ,
								C.IsKhuyenMai ,
								C.KhuyenMai ,
								0 DmBannerREF ,--A.DmBannerREF,
								0 DmChienDichREF ,--A.DmChienDichREF,
								CASE WHEN ISNULL(C.DmWebsiteREF,265) = 265 THEN dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF_thuctreo) 
								ELSE dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF)
								END	DmWebsiteREF ,
								CASE WHEN ISNULL(C.DmWebsiteREF,265) = 265 THEN dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF_thuctreo, C.TenWebsite_thuctreo) 
								ELSE dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF, C.TenWebsite) 
								END TenWebsite ,
								0 TongViewThucChay ,
								0 TongClickThucChay ,
								0 TongSoBaiViet ,
								( CASE WHEN C.IsKhuyenMai = 0 THEN C.SoLuongThucTreo
										ELSE 0
									END ) AS SoLuongThucChay ,
								@NgayThucHien AS NgayThucHien ,
								0 AS GiaTriThayDoi ,
								ISNULL( C.SoLuongThucTreo, 0) * ISNULL(C.DonGiaThucTreo, 0) AS ThanhTienThucChayTruocTrietKhau
						FROM      ( SELECT *
									FROM (
											SELECT    ct.*,
													tchdctp.SoLuongThucTreo,
													tchdctp.DonGia DonGiaThucTreo,
													tchdctp.ChietKhau ChietKhauThucTreo,
													tchdctp.ThucChayHopDongChiTietID,
													tchdctp.DmNhanHangREF AS DmNhanHangTreoREF,
													ISNULL(tchdctp.DmWebsiteREF,265) DmWebsiteREF_thuctreo,
													ISNULL(tchdctp.TenWebsite,N'(Blanks)') TenWebsite_thuctreo,
													(CASE when tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN Convert(date, tchdctp.CreatedAt) 
															else Convert(date, tchdctp.LastModifiedAt)
															END
														) as Ngay
											FROM      dbo.HopDongChiTiet ct
													INNER JOIN dbo.ThucChayHopDongChiTiet tchdctp ON ct.HopDongChiTietID = tchdctp.HopDongChiTietREF
											WHERE     1=1
													AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = ct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
													)) 	 
													AND ct.DeletedStatus = 0
													AND NOT ( ct.DmLoaiREF = 13 OR ct.DmLoaiBannerREF = 18 )

													------
													AND CONVERT(NVARCHAR(200),tchdctp.ThucChayHopDongChiTietID) = @ThucTreoID
													AND tchdctp.DeletedStatus = 0
													AND ct.HopDongChiTietID = @HopDongChiTietID
											) T
											WHERE (ISNULL(T.SoLuong, 0) * ISNULL(T.DonGia, 0)) >= (ISNULL(T.SoLuongThucTreo, 0) * ISNULL(T.DonGiaThucTreo, 0))
								) C
								INNER JOIN ( SELECT * FROM dbo.HopDong hd
												WHERE hd.TrangThaiHopDong <> 3
													AND hd.DeletedStatus = 0
											) D ON D.HopDongID = C.HopDongFK
								INNER JOIN dbo.DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
															AND C.SoLuongThucTreo > 0
															AND C.SoLuong > 0
															AND C.DmWebsiteREF NOT IN ( 307, 285 ) -- loai tru website Google, Facebook
                ) TD	
		)TD

		SET @count = ISNULL((SELECT top (1) HopDongChiTietID FROM @TABLE_OP ORDER BY HopDongChiTietID),0)
	END
            
END


```
