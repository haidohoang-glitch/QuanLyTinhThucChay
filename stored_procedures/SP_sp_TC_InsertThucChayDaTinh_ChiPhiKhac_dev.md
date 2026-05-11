# Stored Procedure: `sp_TC_InsertThucChayDaTinh_ChiPhiKhac_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-17 15:00:36.897000
- **Ngày sửa cuối**: 2018-11-21 10:48:25.637000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--EXEC [sp_TC_InsertThucChayDaTinh_ChiPhiKhac_dev] '2014-06-11 00:00:00.000','2014-06-11 15:42:55.690'
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_ChiPhiKhac_dev]
    @StartDate DATETIME ,
    @EndDate DATETIME ,
    @pSoHopDong NVARCHAR(50)
AS
    BEGIN

        DECLARE @NgayThucHien DATETIME ,
            @NgayGioiHanTinh DATETIME,
			@v_HopDongID INT,
			@v_HopDongChiTietID INT,
			@v_ThucChayHopDongChiTietID INT,
			@v_ThanhTienThucChayDaTinh BIGINT = 0,
			@v_ThanhTienThucTreo BIGINT = 0,
			@v_ChietKhau FLOAT = 0,
			@v_thanhTienHDCN BIGINT = 0,
			@v_DonGiaHDCN FLOAT = 0,
			@v_SoLuongHDCN INT
        SET @NgayThucHien = CONVERT(DATE, @StartDate)
        SET @NgayGioiHanTinh = '2010-01-01'
		
		IF(@pSoHopDong IS NOT NULL)
			SET @v_HopDongID = (SELECT TOP 1 HopDongID FROM dbo.HopDong WHERE SoHopDong = @pSoHopDong)
		
        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN	 
				--CAP NHAT TRANG THAI THUC TREO DUOC TINH THUC CHAY TRONG NGAY TRUOC KHI TINH
                UPDATE  ThucChayHopDongChiTiet
                SET     RecordStatus = 0
                WHERE   CONVERT(NVARCHAR(500), ThucChayHopDongChiTietID) IN (
                        SELECT  DotChayBooking
                        FROM    dbo.ThucChayDaTinh
                        WHERE   NgayThucHien = @NgayThucHien
                                AND NOT ( DmHinhThucQuangCao = 13
                                          OR DmLoaiBannerREF IN ( 18 )
                                        )
                                AND DmSanPhamREF IN (242, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542
									, 555, 556, 557, 558, 559, 560, 561, 635, 563, 631, 651, 630, 726
									, 731, 730, 629, 729, 633, 734, 736 )
                                AND ( @pSoHopDong IS NULL
                                      OR HopDongID = @v_HopDongID
                                    ) )
				--XOA THONG TIN THUC TREO DUOC TINH TRONG NGAY
                DELETE  FROM dbo.ThucChayDaTinh
                WHERE   NgayThucHien = @NgayThucHien
                        AND NOT ( DmHinhThucQuangCao = 13
                                  OR DmLoaiBannerREF IN ( 18 )
                                )
                        AND DmSanPhamREF IN (242, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542
									, 555, 556, 557, 558, 559, 560, 561, 635, 563, 631, 651, 630, 726
									, 731, 730, 629, 729, 633, 734, 736 )
                        AND ( @pSoHopDong IS NULL
                                OR HopDongID = @v_HopDongID
                            ) 

					DECLARE Record_Cursor_SPChiPhi CURSOR FOR 

					SELECT   tchdctp.ThucChayHopDongChiTietID, ct.HopDongChiTietID, ct.ChietKhau, ct.ThanhTien, ct.DonGia, ct.SoLuong
                        FROM
                            (SELECT * FROM dbo.HopDongChiTiet 
								WHERE DmSanPhamREF IN (242, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542
											, 555, 556, 557, 558, 559, 560, 561, 635, 563, 631, 651, 630, 726, 731
											, 730, 629, 729, 633, 734, 736 )
								 AND NOT ( DmLoaiREF = 13
									OR DmLoaiBannerREF = 18
								)
								AND ( @pSoHopDong IS NULL
									OR HopDongFK = @v_HopDongID
								)
								AND DeletedStatus = 0
							) ct
                            INNER JOIN 
							(SELECT * FROM dbo.ThucChayHopDongChiTiet  tchdctp
									WHERE tchdctp.DmSanPhamREF IN (242, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542
											, 555, 556, 557, 558, 559, 560, 561, 635, 563, 631, 651, 630, 726, 731
											, 730, 629, 729, 633, 734, 736 )
									 AND ( CASE
											WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt
											THEN CONVERT(DATE, tchdctp.CreatedAt)
											ELSE CONVERT(DATE, tchdctp.LastModifiedAt)
											END 
										) = CONVERT(DATE, @NgayThucHien)
									AND tchdctp.DeletedStatus = 0
									AND tchdctp.RecordStatus = 0
									AND CONVERT(DATE, ISNULL(tchdctp.ThoiGianBatDau,
									'2013-01-01')) >= @NgayGioiHanTinh
							) tchdctp ON ct.HopDongChiTietID = tchdctp.HopDongChiTietREF
                 
                           
					OPEN Record_Cursor_SPChiPhi

					-- Perform the first fetch.
					FETCH NEXT FROM Record_Cursor_SPChiPhi into @v_ThucChayHopDongChiTietID, @v_HopDongChiTietID, @v_ChietKhau, @v_thanhTienHDCN, @v_DonGiaHDCN, @v_SoLuongHDCN
			
					WHILE @@FETCH_STATUS = 0
						BEGIN
							--CHECK GIA TRI THUCCHAYDATINH
							SET @v_ThanhTienThucChayDaTinh =
								(SELECT  CASE WHEN (@v_ChietKhau <> 100) THEN SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
										ELSE SUM(ThanhTienKM + GiaTriKMThayDoi)
										end 
								FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF = @v_HopDongChiTietID)
							SET @v_ThanhTienThucTreo =
								(
									SELECT CASE WHEN (@v_ChietKhau <> 100) THEN (SoLuongThucTreo * DonGia * (100-ChietKhau)/100)
											ELSE (SoLuongThucTreo*DonGia)
											end
									FROM dbo.ThucChayHopDongChiTiet
									WHERE ThucChayHopDongChiTietID = @v_ThucChayHopDongChiTietID
								)
								--NEU TIEN THUC CHAY CHUA DU THI SE THUC HIEN TINH
								IF(((@v_ThanhTienThucChayDaTinh + @v_ThanhTienThucTreo)<= @v_thanhTienHDCN) AND @v_ChietKhau <> 100)
								OR (((@v_ThanhTienThucChayDaTinh + @v_ThanhTienThucTreo)<= @v_DonGiaHDCN*@v_SoLuongHDCN) AND @v_ChietKhau = 100)
								BEGIN
								    INSERT  INTO dbo.ThucChayDaTinh
									SELECT  NEWID() ,
											TD.* ,
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
														) THEN TD.SoLuongThucChay
												   ELSE 0
											  END ) AS SoLuongThucChayKM ,
											0 SoLuongLechTreoHa ,
											0 ThanhTienLechTreoHa ,
											GETDATE() ,
											GETDATE() ,
											0 IsPheDuyet ,
											'' PheDuyetBy ,
											'' PheDuyetAt ,
											0 SoLuongThayDoi ,
											0 SoLuongKMThayDoi ,
											0 GiaTriKMThayDoi ,
											'' GhiChu
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
														--[dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID,
														--				  @NgayThucHien) NhanHang ,
														C.DmNhanHangREF_ThucTreo AS NhanHang,
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
														dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,
																		  C.HopDongChiTietID,
																		  C.DonGia) AS DonGia , 
														dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,
																		  C.HopDongChiTietID,
																		  C.DonGia) AS DonGiaTheoDonViTinh ,
														C.ChietKhauThucTreo ChietKhau ,
														C.GiamGia ,
														C.ThanhTien ,
														C.TiLeTuVan ,
														C.ChiPhiTuVan ,
														C.IsKhuyenMai ,
														C.KhuyenMai ,
														0 DmBannerREF ,
														0 DmChienDichREF ,
														dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF ,
														dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,
																		  C.TenWebsite) TenWebsite ,
														0 TongViewThucChay ,
														0 TongClickThucChay ,
														0 TongSoBaiViet ,
														( CASE WHEN C.IsKhuyenMai = 0
															   THEN C.SoLuongThucTreo
															   ELSE 0
														  END ) AS SoLuongThucChay ,
														@NgayThucHien AS NgayThucHien ,
														0 AS GiaTriThayDoi ,
														ISNULL(C.SoLuongThucTreo, 0)
														* ISNULL(C.DonGiaThucTreo, 0) AS ThanhTienThucChayTruocTrietKhau
											  FROM      ( SELECT    *
														  FROM      ( SELECT
																		  ct.* ,
																		  tchdctp.SoLuongThucTreo ,
																		  tchdctp.DonGia DonGiaThucTreo ,
																		  tchdctp.ChietKhau ChietKhauThucTreo ,
																		  tchdctp.DmNhanHangREF AS DmNhanHangREF_ThucTreo,
																		  tchdctp.ThucChayHopDongChiTietID
																	  FROM
																		  (SELECT * FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @v_HopDongChiTietID) ct
																		  INNER JOIN 
																		  (SELECT * FROM dbo.ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID = @v_ThucChayHopDongChiTietID) tchdctp 
																		  ON ct.HopDongChiTietID = tchdctp.HopDongChiTietREF
																	) T
														  WHERE     ( ISNULL(T.SoLuong, 0)
																	  * ISNULL(T.DonGia, 0) ) >= ( ISNULL(T.SoLuongThucTreo,
																		  0)
																		  * ISNULL(T.DonGiaThucTreo,
																		  0) ) - 1000
														) C
														INNER JOIN 
														( SELECT
																		  *
																	 FROM dbo.HopDong hd
																	 WHERE
																		  hd.TrangThaiHopDong <> 3
																		  AND hd.DeletedStatus = 0
																		  AND ( @pSoHopDong IS NULL
																		  OR hd.HopDongID = @v_HopDongID
																		  )
														) D ON D.HopDongID = C.HopDongFK
														INNER JOIN dbo.DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
																		  AND C.SoLuongThucTreo > 0
																		  AND C.SoLuong > 0
																		  AND C.DmWebsiteREF NOT IN (
																		  307, 285 ) -- loai tru website Google, Facebook
											) TD

											--CHECK VA THUC HIEN UPDATE TRANG THAI THUC TREO
											IF(EXISTS(SELECT HopDongChiTietREF FROM dbo.ThucChayDaTinh 
														WHERE HopDongChiTietREF = @v_HopDongChiTietID 
														AND DotChayBooking = CONVERT(NVARCHAR(100),@v_ThucChayHopDongChiTietID)
														AND NgayThucHien = @NgayThucHien)
											)
											BEGIN
											    --THUC HIEN UPDATE TRANG THAI TREO LA DA TINH
												UPDATE dbo.ThucChayHopDongChiTiet
												SET RecordStatus = 1
												WHERE ThucChayHopDongChiTietID = @v_ThucChayHopDongChiTietID
											END
											
								END
							--TINH THUC CHAY THEO THUC TREO
							  	
						FETCH NEXT FROM Record_Cursor_SPChiPhi into @v_ThucChayHopDongChiTietID, @v_HopDongChiTietID, @v_ChietKhau, @v_thanhTienHDCN, @v_DonGiaHDCN, @v_SoLuongHDCN
						END

					CLOSE Record_Cursor_SPChiPhi
					DEALLOCATE Record_Cursor_SPChiPhi
             
		
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END 
        SELECT  '1'
    END


```
