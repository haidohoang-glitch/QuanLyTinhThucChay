# Stored Procedure: `sp_TC_InsertThucChayDaTinh_ChiPhi_SanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-12 09:24:09.637000
- **Ngày sửa cuối**: 2020-04-22 15:52:04.813000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--EXEC [sp_TC_InsertThucChayDaTinh_ChiPhi_SanPhamChinh] '2017-08-15','2017-08-15', 'QC4900717'
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_ChiPhi_SanPhamChinh]
    @StartDate DATETIME ,
    @EndDate DATETIME,
	@pSoHopDong NVARCHAR(50)
AS
    BEGIN

        DECLARE @NgayThucHien DATETIME ,
            @NgayGioiHanTinh DATETIME , 
            @PhanBoID INT, @ThucChayHopDongChiTietID INT;
		DECLARE @v_ThanhTienThucChayDaTinh BIGINT = 0,
			@v_ThanhTienThucTreo BIGINT = 0,
			@v_ChietKhau FLOAT = 0,
			@v_thanhTienHDCN BIGINT = 0,
			@v_DonGiaHDCN FLOAT = 0,
			@v_SoLuongHDCN INT

		DECLARE @HopDongID INT = NULL

        SET @NgayThucHien = CONVERT(DATE, @StartDate)
        SET @NgayGioiHanTinh = '2013-01-01'
---------***********DANH SACH CAC SAN PHAM CHINH CO TINH CHI PHI*******-------------
					--Banner CPD 140
					--Banner CPD Chuyên Trang 228
					--BoxApp CPD 549
					--BoxApp Multi	564
					--Box App Self-serving	375
					--CPM Chuyên Trang 231
					--CPM Mass 238
					--CPM Admarket 337
					--CPMulti 531
					--BoxApp CPM	 370
					--Balloon Ads	339
					--Mobile	342
					--Ad page	305
					--Sponsor Post	381
					--TVC online  240
					--Sponsor Page 735

		SELECT @HopDongID = hd.HopDongID FROM dbo.HopDong hd WHERE hd.SoHopDong = @pSoHopDong

        WHILE ( @NgayThucHien <= @EndDate )
            BEGIN	
	
				----- update gia tri thay doi cac phan bo da tinh
                DECLARE db_cursor_ChiPhiSanPhamChinh CURSOR
                FOR
				SELECT C.HopDongChiTietID, tchdt.ThucChayHopDongChiTietID, C.ChietKhau, C.ThanhTien, C.DonGia, C.SoLuong FROM
					(	
						SELECT * FROM  dbo.HopDongChiTiet
						WHERE DmSanPhamREF IN ( 140, 228, 549, 564, 375, 231, 238, 337, 531, 370, 339, 342, 381, 240, 680, 598, 680, 821,735)
						AND DeletedStatus = 0
						AND DmLoaiBannerREF = 17 --Loai banner CHI PHI cua sanpham chinh
                    ) C
                    INNER JOIN 
					( SELECT * FROM dbo.HopDong hd
                                    WHERE hd.TrangThaiHopDong <> 3
                                        AND hd.DeletedStatus = 0
										AND (@HopDongID IS NULL OR hd.HopDongID = @HopDongID)
										AND hd.NgayDanhSoHopDong >= '2015-01-01'
                    ) D ON D.HopDongID = C.HopDongFK
					INNER JOIN 
					( SELECT ThucChayHopDongChiTietID,
										DmBannerREF,
										DmNhanHangREF AS DmNhanHangREF_ThucTreo,
										HopDongChiTietREF
									FROM   dbo.ThucChayHopDongChiTiet
									WHERE  DeletedStatus = 0
									AND RecordStatus = 0
									AND (CASE WHEN CreatedAt >= LastModifiedAt THEN Convert(date,CreatedAt) 
											ELSE Convert(date,LastModifiedAt)
											END
									)   = CONVERT(DATE,@NgayThucHien)
					) tchdt ON C.HopDongChiTietID = tchdt.HopDongChiTietREF
		
                OPEN db_cursor_ChiPhiSanPhamChinh   
                FETCH NEXT FROM db_cursor_ChiPhiSanPhamChinh INTO @PhanBoID  , @ThucChayHopDongChiTietID , @v_ChietKhau, @v_thanhTienHDCN, @v_DonGiaHDCN, @v_SoLuongHDCN

                WHILE @@FETCH_STATUS = 0
                    BEGIN   
						--CHECK GIA TRI THUCCHAYDATINH
						SET @v_ThanhTienThucChayDaTinh =
							(SELECT  CASE WHEN (@v_ChietKhau <> 100) THEN SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
									ELSE SUM(ThanhTienKM + GiaTriKMThayDoi)
									end 
							FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF = @PhanBoID)
							SET @v_ThanhTienThucTreo =
							(
								SELECT CASE WHEN (@v_ChietKhau <> 100) THEN (SoLuongThucTreo * DonGia * (100-ChietKhau)/100)
										ELSE (SoLuongThucTreo*DonGia)
										end
								FROM dbo.ThucChayHopDongChiTiet
								WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
							)
							SET @v_ThanhTienThucChayDaTinh = ISNULL(@v_ThanhTienThucChayDaTinh,0)
							SET @v_ThanhTienThucTreo = ISNULL(@v_ThanhTienThucTreo,0)
							----
							--PRINT @v_ThucChayHopDongChiTietID
							----NEU TIEN THUC CHAY CHUA DU THI SE THUC HIEN TINH
							--PRINT '---------'
							--PRINT @v_ThanhTienThucChayDaTinh
							--PRINT @v_ThanhTienThucTreo
							--PRINT @v_thanhTienHDCN
							--PRINT @v_ChietKhau
							--PRINT @v_DonGiaHDCN
							--PRINT @v_SoLuongHDCN
							--PRINT '---------'
							IF(((@v_ThanhTienThucChayDaTinh + @v_ThanhTienThucTreo)<= @v_thanhTienHDCN) AND @v_ChietKhau <> 100)
							OR (((@v_ThanhTienThucChayDaTinh + @v_ThanhTienThucTreo)<= @v_DonGiaHDCN*@v_SoLuongHDCN) AND @v_ChietKhau = 100)
							BEGIN
							     --- insert data 
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
                                            )
                                       THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh(@NgayThucHien,
                                                              @NgayGioiHanTinh,
                                                              TD.HopDongChiTietID),
                                                   0)
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
                                            --                  @NgayThucHien) NhanHang ,
											tchdt.DmNhanHangREF_ThucTreo AS NhanHang,
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
                                            tchdt.ThucChayHopDongChiTietID DotChayBooking ,
                                            0 AS SoLuongDotChayBooking , 
                                            ISNULL(C.SoLuong, 0) AS SoLuong ,
                                            ISNULL(C.DonViTinh, N'đ/v') AS DonViTinh ,
                                            C.DonGia AS DonGia ,
                                            C.DonGia AS DonGiaTheoDonViTinh ,
                                            C.ChietKhau ,
                                            C.GiamGia ,
                                            C.ThanhTien ,
                                            C.TiLeTuVan ,
                                            C.ChiPhiTuVan ,
                                            C.IsKhuyenMai ,
                                            C.KhuyenMai ,
                                            tchdt.DmBannerREF DmBannerREF ,--A.DmBannerREF,
                                            0 DmChienDichREF ,--A.DmChienDichREF,
                                            dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF ,
                                            dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite ,
                                            0 TongViewThucChay ,
                                            0 TongClickThucChay ,
                                            0 TongSoBaiViet ,
                                            C.SoLuong AS SoLuongThucChay , 
                                            @NgayThucHien AS NgayThucHien ,
                                            C.ThanhTien AS GiaTriThayDoi ,
                                            0 AS ThanhTienThucChayTruocTrietKhau
	                             FROM      (	
												SELECT * FROM  dbo.HopDongChiTiet
												WHERE DmSanPhamREF IN ( 140, 228, 549, 564, 375, 231, 238, 337, 531, 370, 339, 342, 381, 240, 680, 598, 680, 821,735)
												AND DeletedStatus = 0
												AND DmLoaiBannerREF = 17 --Loai banner CHI PHI cua sanpham chinh
                                            ) C
                                            INNER JOIN 
											( SELECT * FROM dbo.HopDong hd
                                                         WHERE hd.TrangThaiHopDong <> 3
                                                              AND hd.DeletedStatus = 0
															  AND (@HopDongID IS NULL OR hd.HopDongID = @HopDongID)
															  AND hd.NgayDanhSoHopDong >= '2015-01-01'
                                            ) D ON D.HopDongID = C.HopDongFK
											INNER JOIN 
											( SELECT ThucChayHopDongChiTietID,
																DmBannerREF,
																DmNhanHangREF AS DmNhanHangREF_ThucTreo,
																HopDongChiTietREF
														 FROM   dbo.ThucChayHopDongChiTiet
														 WHERE  DeletedStatus = 0
														 AND RecordStatus = 0
														 AND (CASE WHEN CreatedAt >= LastModifiedAt THEN Convert(date,CreatedAt) 
																	ELSE Convert(date,LastModifiedAt)
																  END
															)   = CONVERT(DATE,@NgayThucHien)
											) tchdt ON C.HopDongChiTietID = tchdt.HopDongChiTietREF
                                            INNER JOIN dbo.DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
                                            AND C.SoLuong > 0
                                ) TD	
							END
							

                        FETCH NEXT FROM db_cursor_ChiPhiSanPhamChinh INTO @PhanBoID  , @ThucChayHopDongChiTietID , @v_ChietKhau, @v_thanhTienHDCN, @v_DonGiaHDCN, @v_SoLuongHDCN
                    END   

                CLOSE db_cursor_ChiPhiSanPhamChinh   
                DEALLOCATE db_cursor_ChiPhiSanPhamChinh

				EXEC [sp_TC_UpdateThucChayHopDongChiTiet_ChiPhi_SanPhamChinh] @NgayThucHien
                SET @NgayThucHien = DATEADD(d, 1, @NgayThucHien)
            END 
        SELECT  '1'
    END

```
