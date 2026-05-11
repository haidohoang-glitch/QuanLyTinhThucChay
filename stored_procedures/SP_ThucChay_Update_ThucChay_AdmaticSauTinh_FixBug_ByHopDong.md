# Stored Procedure: `ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-04-24 10:19:29.577000
- **Ngày sửa cuối**: 2018-09-14 15:41:01.770000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug_ByHopDong] 1001735, '2018-04-13'
CREATE  PROCEDURE [dbo].[ThucChay_Update_ThucChay_AdmaticSauTinh_FixBug_ByHopDong]
	@HopDongID INT,
    @NgayThucHien DATETIME
AS
    BEGIN

        DECLARE @HDCTID_Tiep INT
        DECLARE @ChayXong TABLE ( HopDongChiTietID INT )

        DECLARE @ThucChayDaTinh_Temp TABLE
            (
              ThucChayDaTinhID NVARCHAR(50)
            )
        DECLARE @HopDongChiTietID INT

   IF(EXISTS(SELECT DISTINCT HopDongID FROM    dbo.ThucChayDaTinh
				WHERE   DmHinhThucQuangCao = 42
                AND CONVERT(DATE, NgayThucHien) = @NgayThucHien
				AND SoLuongThucChayLechTreoHa <> 0
				AND ThanhTienLechTreoHa <> 0
				AND HopDongID = @HopDongID
				AND DmSanPhamREF NOT IN  (736,817) -- chi phí công nghệ, chi phi marketing fee
				)
			)

	BEGIN
		DECLARE @DmSanPhamREF INT
		PRINT 'vao hop dong'
        DECLARE icursor2 CURSOR
        FOR
            SELECT  DmSanPhamREF
            FROM    dbo.AdmaticThuTuChayHopDongChiTiet
            WHERE   HopDongFK = @HopDongID
            GROUP BY DmSanPhamREF
            HAVING  COUNT(HopDongChiTietID) > 1
		
        OPEN icursor2  
		
        FETCH NEXT FROM icursor2   INTO @DmSanPhamREF
		
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
								
						OPEN icursor3  
								
						FETCH NEXT FROM icursor3   
						INTO @ThucChayDaTinhID
								
						WHILE @@FETCH_STATUS = 0  
						BEGIN  
							SELECT @SoLuongThucChayLechTreoHa = ISNULL(SoLuongThucChayLechTreoHa,0) ,
									@ThanhTienLechTreoHa =  ISNULL(ThanhTienLechTreoHa,0) ,
									@DonGiaDVT = ISNULL(DonGiaTheoDonVi,0)
							FROM    dbo.ThucChayDaTinh
							WHERE   ThucChayDaTinhID IN ( @ThucChayDaTinhID )

							SELECT @TongTienDaTinh = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0)) ,
									@SoLuongDaTinh = SUM(ISNULL(SoLuongThucChay,0) + ISNULL(SoLuongThayDoi,0))
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
											( CASE WHEN ChietKhau = 100 THEN @ThanhTienThucChayTruocTrietKhau 
											ELSE 0
											END) AS ThanhTienKM ,
											( CASE WHEN ChietKhau = 100 THEN @SLInsert 
											ELSE 0
											END) AS SoLuongThucChayKM ,
											@SLLechInsert SoLuongThucChayLechTreoHa ,
											@LechInsert ThanhTienLechTreoHa ,
											--TongSoBaiViet ,
											--@SLInsert , --SLTC
											--NgayThucHien ,
											--GiaTriThayDoi ,
											--@ThanhTienThucChayTruocTrietKhau ThanhTienThucChayTruocTrietKhau ,
											--GiaTriTrietKhauThucChay ,
											--@TienInsert ,
											--GiaTriHoaHongThucChay ,
											--ThanhTienThucThu ,
											--0 ThanhTienKM ,
											--0 SoLuongThucChayKM ,
											--@SLLechInsert SoLuongThucChayLechTreoHa ,
											--@LechInsert ThanhTienLechTreoHa ,
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
													AND ChietKhau = 100
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
		 
                FETCH NEXT FROM icursor2   INTO @DmSanPhamREF 
            END   
        CLOSE icursor2;  
        DEALLOCATE icursor2;  
	END
           
	
END

```
