# Stored Procedure: `ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-16 10:44:32.170000
- **Ngày sửa cuối**: 2020-08-31 16:19:55.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug] '2016-09-05'
CREATE  PROCEDURE [dbo].[ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug]
    @NgayThucHien DATETIME
AS
    BEGIN


        DECLARE @HDCTID_Tiep INT
        DECLARE @ChayXong TABLE ( HopDongChiTietID INT )

        DECLARE @ThucChayDaTinh_Temp TABLE
            (
              ThucChayDaTinhID NVARCHAR(50)
            )


        DECLARE @HopDongID INT
        DECLARE @HopDongChiTietID INT

        DECLARE icursor CURSOR
        FOR
            SELECT DISTINCT
                    HopDongID
            FROM    dbo.ThucChayDaTinh
            WHERE   DmHinhThucQuangCao = 42
                    AND CONVERT(DATE, NgayThucHien) = @NgayThucHien
					AND SoLuongThucChayLechTreoHa > 0
					AND ThanhTienLechTreoHa > 0
					AND DmSanPhamREF NOT IN  (736,817) -- chi phí công nghệ, chi phi marketing fee
					AND CONVERT(DATE,NgayDanhSoHopDong) < '2020-07-20'
            --AND HopDongID = 504912

        OPEN icursor  

        FETCH NEXT FROM icursor   
INTO @HopDongID

        WHILE @@FETCH_STATUS = 0
            BEGIN  

                DECLARE @DmSanPhamREF INT
		
                DECLARE icursor2 CURSOR
                FOR
                    SELECT  DmSanPhamREF
                    FROM    dbo.AdmaticThuTuChayHopDongChiTiet
                    WHERE   HopDongFK = @HopDongID
                    GROUP BY DmSanPhamREF
                    HAVING  COUNT(HopDongChiTietID) > 1
		
                OPEN icursor2  
		
                FETCH NEXT FROM icursor2   
		INTO @DmSanPhamREF
		
                WHILE @@FETCH_STATUS = 0
                    BEGIN  
		    
                        INSERT  INTO @ChayXong
                                SELECT  A.HopDongChiTietID
                                FROM    dbo.AdmaticThuTuChayHopDongChiTiet A
                                WHERE   A.TrangthaiThucChay = 3
                                        AND A.HopDongFK = @HopDongID
                                        AND A.DmSanPhamREF = @DmSanPhamREF
                                ORDER BY A.SoThuTuChay


                        SET @HDCTID_Tiep = ( SELECT TOP 1
                                                    A.HopDongChiTietID
                                             FROM   dbo.AdmaticThuTuChayHopDongChiTiet A
                                             WHERE  A.TrangthaiThucChay <> 3
                                                    AND A.HopDongFK = @HopDongID
                                                    AND A.DmSanPhamREF = @DmSanPhamREF
                                             ORDER BY A.SoThuTuChay
                                           )

                        IF @HDCTID_Tiep IS NOT NULL
                            BEGIN
								DECLARE @ThucChayDaTinhID NVARCHAR(50)
								DECLARE @SoLuongThucChayLechTreoHa INT
								DECLARE @ThanhTienLechTreoHa FLOAT
								DECLARE @SoLuongDaTinh INT
								DECLARE @TongTienDaTinh FLOAT
								DECLARE @ThanhTienHDCT FLOAT
								DECLARE @CK FLOAT
								DECLARE @LechSauCK FLOAT
								DECLARE @TienInsert FLOAT
								DECLARE @LechInsert FLOAT
								DECLARE @SLLechInsert INT
								DECLARE @SLInsert INT
								DECLARE @ThanhTienThucChayTruocTrietKhau FLOAT
								DECLARE @DonGiaDVT FLOAT
								
								-- Lay cac hop dong chi tiet co phat sinh lech treo ha sau khi da do day tien
								DECLARE icursor3 CURSOR FOR   
									SELECT  TC.ThucChayDaTinhID
											FROM    dbo.ThucChayDaTinh TC
													INNER JOIN @ChayXong CX ON TC.HopDongChiTietREF = CX.HopDongChiTietID
											WHERE   TC.NgayThucHien = @NgayThucHien
													AND TC.HopDongID = @HopDongID
													AND TC.SoLuongThucChayLechTreoHa <> 0
													AND TC.ThanhTienLechTreoHa <> 0
													AND TC.DmSanPhamREF NOT IN  (736,817) -- chi phí công nghệ, chi phi marketing fee
								
								OPEN icursor3  
								
								FETCH NEXT FROM icursor3   
								INTO @ThucChayDaTinhID
								
								WHILE @@FETCH_STATUS = 0  
								BEGIN  
									SELECT @SoLuongThucChayLechTreoHa = SoLuongThucChayLechTreoHa ,
											@ThanhTienLechTreoHa =  ThanhTienLechTreoHa ,
											@DonGiaDVT = DonGiaTheoDonVi
									FROM    dbo.ThucChayDaTinh
									WHERE   ThucChayDaTinhID IN ( @ThucChayDaTinhID )

									SELECT @TongTienDaTinh = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ,
											@SoLuongDaTinh = SUM(SoLuongThucChay + SoLuongThayDoi)
									FROM dbo.ThucChayDaTinh
									WHERE HopDongChiTietREF = @HDCTID_Tiep
										AND DmHinhThucQuangCao = 42

									SELECT @ThanhTienHDCT = ThanhTien ,
											@CK = ChietKhau
									FROM dbo.HopDongChiTiet 
									WHERE HopDongChiTietID = @HDCTID_Tiep

									SET @TongTienDaTinh = ISNULL(@TongTienDaTinh,0)
									SET @SoLuongDaTinh = ISNULL(@SoLuongDaTinh,0)
									SET @ThanhTienHDCT = ISNULL(@ThanhTienHDCT,0)
									SET @CK = ISNULL(@CK,0)

									IF @CK <> 100
										BEGIN
										    SET @LechSauCK = @ThanhTienLechTreoHa * ((100 - @CK)/100)
											SET @ThanhTienThucChayTruocTrietKhau = @ThanhTienLechTreoHa

											IF (@ThanhTienHDCT - @TongTienDaTinh) - @LechSauCK >= 0 
												BEGIN
													SET @TienInsert = @LechSauCK
													SET @LechInsert = 0
													SET @SLInsert = @SoLuongThucChayLechTreoHa
													SET @SLLechInsert = 0
												END
											ELSE
												BEGIN
													SET @TienInsert = @ThanhTienHDCT - @TongTienDaTinh
													SET @LechInsert = @LechSauCK - (@ThanhTienHDCT - @TongTienDaTinh)
													SET @SLInsert = (@ThanhTienHDCT - @TongTienDaTinh)/@DonGiaDVT
													SET @SLLechInsert = (@LechSauCK - (@ThanhTienHDCT - @TongTienDaTinh))/@DonGiaDVT
												END
										END
									ELSE
										BEGIN
											SET @SLInsert = 0
										    SET @TienInsert = 0
											SET @SLLechInsert = @SoLuongThucChayLechTreoHa
											SET @LechInsert = @ThanhTienLechTreoHa
										END

									

								    -- Day lech treo ha tu phan bo chinh sang phan bo ke tiep
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
								
											SELECT  NEWID() ,
													HopDongID ,
													SoHopDong ,
													DmMaHopDongREF ,
													TenMaHopDong ,
													NgayDanhSoHopDong ,
													NgayKyHopDong ,
													NhanHopDong ,
													NgayNhanBanFax ,
													NgayNhanHopDongBanCung ,
													NgayChuyenHopDongChoKeToan ,
													So ,
													Thang ,
													Nam ,
													GiaTriHopDong ,
													CongNo ,
													@HDCTID_Tiep ,
													DangSuDung ,
													IsGiayPhep ,
													TrangThaiHopDong ,
													IsBanCung ,
													DmPhongBanREF ,
													TenPhongBan ,
													DmBoPhanREF ,
													TenBoPhan ,
													DmNhomLamViecREF ,
													TenNhomLamViec ,
													DmDiaDiemLamViecREF ,
													TenDiaDiemLamViec ,
													SysNhanVienREF ,
													TenDangNhap ,
													TenNhanVien ,
													TenKhachHang ,
													NhanHang ,
													DmNhomNganhREF ,
													TenNhomNganh ,
													DmHinhThucQuangCao ,
													TenHinhThucQuangCao ,
													DmSanPhamREF ,
													TenSanPham ,
													DmNhomWebsiteREF ,
													TenNhomWebsite ,
													DmChuyenMucREF ,
													TenChuyenMuc ,
													DmLoaiBannerREF ,
													TenLoaiBanner ,
													DmViTriREF ,
													TenViTri ,
													DotChayHopDong ,
													SoLuongDotChayHD ,
													DotChayBooking ,
													SoLuongDotChayBooking ,
													SoLuong ,
													DonViTinh ,
													DonGia ,
													DonGiaTheoDonVi ,
													ChietKhau ,
													GiamGia ,
													ThanhTien ,
													TiLeTuVan ,
													ChiPhiTuVan ,
													IsKhuyenMai ,
													KhuyenMai ,
													DmBannerREF ,
													DmChienDichREF ,
													DmWebsiteREF ,
													TenWebsite ,
													TongViewThucChay ,
													TongClickThucChay ,
													TongSoBaiViet ,
													( CASE WHEN ChietKhau <> 100 THEN @SLInsert 
													ELSE 0
													END) AS SoLuongThucChay , --SLTC
													NgayThucHien ,
													GiaTriThayDoi ,
													( CASE WHEN ChietKhau <> 100 THEN @ThanhTienThucChayTruocTrietKhau 
													ELSE 0
													END) AS  ThanhTienThucChayTruocTrietKhau ,
													GiaTriTrietKhauThucChay ,
													( CASE WHEN ChietKhau <> 100 THEN @TienInsert 
													ELSE 0
													END) AS  ThanhTienSauTrietKhauThucChay,
													GiaTriHoaHongThucChay ,
													ThanhTienThucThu ,
													( CASE WHEN ChietKhau = 100 THEN @LechInsert 
													ELSE 0
													END) AS ThanhTienKM ,
													( CASE WHEN ChietKhau = 100 THEN @SLLechInsert 
													ELSE 0
													END) AS SoLuongThucChayKM ,
													0 SoLuongThucChayLechTreoHa ,
													0 ThanhTienLechTreoHa ,
													GETDATE() ,
													GETDATE() ,
													IsPheDuyet ,
													PheDuyetBy ,
													PheDuyetAt ,
													SoLuongThayDoi ,
													SoLuongKMThayDoi ,
													GiaTriKMThayDoi ,
													CONVERT(NVARCHAR(50), HopDongChiTietREF)
													+ N': day lech treo ha sang phan bo ke tiep'
											FROM    dbo.ThucChayDaTinh
											WHERE   ThucChayDaTinhID IN ( @ThucChayDaTinhID )

							-- Cap nhat lech treo ha cua phan bo truoc do ve 0 sau khi day
									UPDATE  dbo.ThucChayDaTinh
									SET     SoLuongThucChayLechTreoHa = 0 ,
											ThanhTienLechTreoHa = 0 ,
											GhiChu = GhiChu + ' | SLLechTreoHa:' + dbo.FormatNumber(SoLuongThucChayLechTreoHa) +  ' | TTLechTreoHa:' + dbo.FormatNumber(ThanhTienLechTreoHa)
									WHERE   ThucChayDaTinhID IN ( @ThucChayDaTinhID )


							-- Fix bug do du lieu ca hai truong KM va lech treo ha
									IF @ThucChayDaTinhID IS NOT NULL
										BEGIN
											UPDATE  dbo.ThucChayDaTinh
											SET     SoLuongThucChayKM = 0 ,
													ThanhTienKM = 0 ,
													GhiChu = GhiChu + ' | SoLuongThucChayKM:' + dbo.FormatNumber(SoLuongThucChayKM) +  ' | ThanhTienKM:' + dbo.FormatNumber(ThanhTienKM)
											WHERE   ThucChayDaTinhID IN (
													SELECT  ThucChayDaTinhID
													FROM    dbo.ThucChayDaTinh
													WHERE   HopDongChiTietREF = @HDCTID_Tiep
															AND CONVERT(DATE, NgayThucHien) = @NgayThucHien
															AND DmHinhThucQuangCao = 42
															AND DmSanPhamREF = @DmSanPhamREF
															AND IsKhuyenMai = 1
															AND ThanhTienKM = ThanhTienLechTreoHa
															AND SoLuongThucChayKM = SoLuongThucChayLechTreoHa )
										END									
									 
								    FETCH NEXT FROM icursor3   
								    INTO @ThucChayDaTinhID 
								END   
								CLOSE icursor3;  
								DEALLOCATE icursor3;  


                            END
				
                        DELETE  FROM @ChayXong
                        SET @HDCTID_Tiep = NULL

			 
                        FETCH NEXT FROM icursor2   
		    INTO @DmSanPhamREF 
                    END   
                CLOSE icursor2;  
                DEALLOCATE icursor2;  
    

	 
                FETCH NEXT FROM icursor   
    INTO @HopDongID
            END   
        CLOSE icursor;  
        DEALLOCATE icursor;  
	
    END

```
