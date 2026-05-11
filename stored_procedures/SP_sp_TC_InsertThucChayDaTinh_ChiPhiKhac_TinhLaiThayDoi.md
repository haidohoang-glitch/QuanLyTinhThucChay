# Stored Procedure: `sp_TC_InsertThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:21:48.703000
- **Ngày sửa cuối**: 2024-11-05 17:12:18.970000

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
EXEC sp_TC_InsertThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi 504534, 559436, '2020-05-21', @KQ  OUTPUT
DECLARE @KQ INT = 0
--- TINH LAI GIA TRI
EXEC sp_TC_InsertThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi 520086, 580309, '2020-09-16', @KQ  OUTPUT
*/

-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_ChiPhiKhac_TinhLaiThayDoi]
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

	SET @count = 0
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
	)
	PRINT 'Vao roi'
	PRINT @v_TongThucChayDaTinh
	PRINT @v_GiaTriThucTreo
	PRINT @v_ThanhTien
	PRINT @v_ChietKhau

	IF((((@v_TongThucChayDaTinh + @v_GiaTriThucTreo) <= @v_ThanhTien) AND @v_ChietKhau <> 100)
	OR (((@v_TongThucChayDaTinh + @v_GiaTriThucTreo) <= @v_DonGia*@v_SoLuong) AND @v_ChietKhau = 100)
	--OR (@v_TongThucChayDaTinh <> @v_GiaTriThucTreo) -- bô sung, haidh comment lại phan thong tin nay 2021-06-22
	)
	BEGIN
				print 'tinh thuc chay'
			    INSERT  INTO dbo.ThucChayDaTinh
				SELECT TCDT.ThucChayDaTinhID,
							TCDT.HopDongID ,
                            TCDT.SoHopDong ,
                            TCDT.DmMaHopDongREF ,
                            TCDT.TenMaHopDong , 
                            TCDT.NgayDanhSoHopDong ,
                            TCDT.NgayKyHopDong ,
                            TCDT.NhanHopDong ,
                            TCDT.NgayNhanBanFax ,
                            TCDT.NgayNhanHopDongBanCung ,
                            TCDT.NgayChuyenHopDongChoKeToan ,
                            TCDT.So ,
                            TCDT.Thang ,
                            TCDT.Nam , 
                            TCDT.GiaTriHopDong ,
                            TCDT.CongNo ,
                            TCDT.HopDongChiTietID ,
                            TCDT.DangSuDung ,
                            TCDT.IsGiayPhep ,
                            TCDT.TrangThaiHopDong ,
                            TCDT.IsBanCung , 
                            TCDT.DmPhongBanREF ,
                            TCDT.TenPhongBan ,
                            TCDT.DmBoPhanREF ,
                            TCDT.TenBoPhan ,
                            TCDT.DmNhomLamViecREF ,
                            TCDT.TenNhom ,
                            TCDT.DmDiaDiemLamViecREF ,
                            TCDT.TenDiaDiemLamViec ,
                            TCDT.SysNhanVienREF ,
                            TCDT.TenDangNhap ,
                            TCDT.TenNhanVien , 
                            TCDT.TenKhachHang , 
                            TCDT.NhanHang ,
                            TCDT.DmNhomNganhREF ,
                            TCDT.TenNhomNganh , 
                            TCDT.DmHinhThucQuangCao ,
                            TCDT.TenHinhThucQuangCao , 
                            TCDT.DmSanPhamREF ,
                            TCDT.TenSanPham ,
                            TCDT.DmNhomWebsiteREF ,
                            TCDT.TenNhomWebsite , 
                            TCDT.DmChuyenMucREF ,
                            TCDT.TenChuyenMuc ,
                            TCDT.DmLoaiBannerREF ,
                            TCDT.TenLoaiBanner ,
                            TCDT.DmViTriREF ,
                            TCDT.TenViTri ,
                            TCDT.DotChayHopDong ,
                            TCDT.SoLuongDotChayHD ,
                            TCDT.DotChayBooking ,
                            TCDT.SoLuongDotChayBooking , 
                            TCDT.SoLuong ,
                            TCDT.DonViTinh ,
                            TCDT.DonGia , 
                            TCDT.DonGiaTheoDonViTinh ,
                            TCDT.ChietKhau ,
                            TCDT.GiamGia ,
                            TCDT.ThanhTien ,
                            TCDT.TiLeTuVan ,
                            TCDT.ChiPhiTuVan ,
                            TCDT.IsKhuyenMai ,
                            TCDT.KhuyenMai ,
                            TCDT.DmBannerREF ,--A.DmBannerREF,
                            TCDT.DmChienDichREF ,--A.DmChienDichREF,
                            TCDT.DmWebsiteREF ,
                            TCDT.TenWebsite ,
                            TCDT.TongViewThucChay ,
                            TCDT.TongClickThucChay ,
                            TCDT.TongSoBaiViet ,
                            0 AS SoLuongThucChay ,
							TCDT.NgayThucHien ,
                            TCDT.ThanhTienSauTrietKhauThucChay AS GiaTriThayDoi ,
                            0 AS ThanhTienThucChayTruocTrietKhau,
							0 AS GiaTriTrietKhauThucChay ,
							0 AS ThanhTienSauTrietKhauThucChay ,
							0 AS GiaTriHoaHongThucChay ,
							0 AS ThanhTienThucThu ,
							0 AS ThanhTienKM ,
							0 AS SoLuongThucChayKM ,
							0 AS SoLuongLechTreoHa ,
							0 AS ThanhTienLechTreoHa ,
							TCDT.CREATEDAT,
							TCDT.LASTMODIFIEDBY,
							TCDT.IsPheDuyet ,
							TCDT.PheDuyetBy ,
							TCDT.PheDuyetAt ,
							TCDT.SoLuongThucChay AS SoLuongThucChaySoLuongThayDoi ,
							TCDT.SoLuongThucChayKM AS SoLuongKMThayDoi ,
							TCDT.ThanhTienKM AS GiaTriKMThayDoi ,
							TCDT.GhiChu
			FROM 
			(
				SELECT  NEWID() as ThucChayDaTinhID, TD.* ,
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
                GETDATE() AS CREATEDAT,
                GETDATE() AS LASTMODIFIEDBY,
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
                            dbo.ThucChay_GetDonGiaByNgayThucHien(C.Ngay,
                                                C.HopDongChiTietID,
                                                C.DonGia) AS DonGia , 
                            dbo.ThucChay_GetDonGiaByNgayThucHien(C.Ngay,
                                                C.HopDongChiTietID,
                                                C.DonGia) AS DonGiaTheoDonViTinh ,
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
										WHERE   1=1 
										AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = ct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										))
												AND ct.DeletedStatus = 0
												AND NOT ( ct.DmLoaiREF = 13
														OR ct.DmLoaiBannerREF = 18
														)

												------
												AND CONVERT(NVARCHAR(200),tchdctp.ThucChayHopDongChiTietID) = @ThucTreoID
												AND tchdctp.DeletedStatus = 0
												AND ct.HopDongChiTietID = @HopDongChiTietID
										) T
										WHERE (ISNULL(T.SoLuong, 0) * ISNULL(T.DonGia, 0)) >= (ISNULL(T.SoLuongThucTreo, 0) * ISNULL(T.DonGiaThucTreo, 0))
                            ) C
                            INNER JOIN ( SELECT
                                                *
                                            FROM dbo.HopDong hd
                                            WHERE
                                                hd.TrangThaiHopDong <> 3
                                                AND hd.DeletedStatus = 0
                                        ) D ON D.HopDongID = C.HopDongFK
                            INNER JOIN dbo.DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
														AND C.SoLuongThucTreo > 0-- tuyetnta comment ngày 22/5/2020
														AND C.SoLuong > 0
														AND C.DmWebsiteREF NOT IN ( 307, 285 ) -- loai tru website Google, Facebook
                ) TD	
			)TCDT

		SET @count = @count + 1
			
		--INSERT THONG TIN THUC TREO DA TINH VAO HE THONG
		INSERT INTO [dbo].[ThucChayHopDongChiTiet_TCDT]
							([HopDongChiTietREF]
							,[ThucChayHopDongChiTietREF]
							,[NgayThucHien]
							,[DmSanPhamREF]
							,[ChietKhauHDCT]
							,[ThanhTienHDCT]
							,[DonGiaHDCT]
							,[SoluongHDCT]
							,[CreatedAt]
							,[RecordStatus])
						VALUES
							(@HopDongChiTietID
							, @ThucTreoID
							, @NgayThucHien
							, 0 
							, @v_ChietKhau
							, @v_ThanhTien
							, @v_DonGia
							, @v_SoLuong
							, GETDATE()
							, 0)
	END
	
	            
	END


```
