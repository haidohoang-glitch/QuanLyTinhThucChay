# Stored Procedure: `sp_TC_InsertThucChayDaTinh_TinhTheoChiPhiKhac_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-06 09:47:28.893000
- **Ngày sửa cuối**: 2020-08-06 09:49:31.410000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC  [dbo].[sp_TC_InsertThucChayDaTinh_TinhTheoChiPhiKhac_ByHopDongChiTiet] '2018-08-29','QC0199320', 12456
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_TinhTheoChiPhiKhac_ByHopDongChiTiet]
    @NgayThucHien DATETIME ,
    @pSoHopDong NVARCHAR(50),
	@pHopDongChiTietID INT
AS
    BEGIN

        DECLARE @NgayGioiHanTinh DATETIME,
			@v_HopDongID INT =0,
			@v_HopDongChiTietID INT,
			@v_ThucChayHopDongChiTietID INT,
			@v_ThanhTienThucChayDaTinh BIGINT = 0,
			@v_ThanhTienThucTreo BIGINT = 0,
			@v_ChietKhau FLOAT = 0,
			@v_thanhTienHDCN BIGINT = 0,
			@v_DonGiaHDCN FLOAT = 0,
			@v_SoLuongHDCN INT
        SET @NgayGioiHanTinh = '2010-01-01'
		SET @v_HopDongChiTietID = @pHopDongChiTietID
		
		IF(@pSoHopDong IS NOT NULL)
			SET @v_HopDongID = (SELECT TOP 1 HopDongID FROM dbo.HopDong WHERE SoHopDong = @pSoHopDong)
		
 		--CAP NHAT TRANG THAI THUC TREO DUOC TINH THUC CHAY TRONG NGAY TRUOC KHI TINH
        UPDATE  dbo.ThucChayHopDongChiTiet
        SET     RecordStatus = 0
        WHERE   CONVERT(NVARCHAR(500), ThucChayHopDongChiTietID) IN (
                SELECT  DotChayBooking
                FROM    dbo.ThucChayDaTinh
                WHERE   NgayThucHien = @NgayThucHien
                        AND NOT ( DmHinhThucQuangCao = 13
                                    OR DmLoaiBannerREF IN ( 18 )
                                )
                        AND ( HopDongID = @v_HopDongID ) )

		--XOA THONG TIN THUC TREO DUOC TINH TRONG NGAY
        DELETE  FROM dbo.ThucChayDaTinh
        WHERE   NgayThucHien = @NgayThucHien
                AND NOT ( DmHinhThucQuangCao = 13 OR DmLoaiBannerREF IN ( 18 ) )
                AND HopDongID = @v_HopDongID
				AND HopDongChiTietREF = @v_HopDongChiTietID
	

			DECLARE Record_Cursor_SPChiPhi CURSOR FOR 

			SELECT   tchdctp.ThucChayHopDongChiTietID, ct.HopDongChiTietID, ct.ChietKhau, ct.ThanhTien, ct.DonGia, ct.SoLuong
                FROM
                    (SELECT * FROM dbo.HopDongChiTiet 
						WHERE 1=1 AND NOT ( DmLoaiREF = 13 OR DmLoaiBannerREF = 18 )
						AND (HopDongFK = @v_HopDongID )
						AND DeletedStatus = 0 ) ct
                    INNER JOIN 
					(SELECT * FROM dbo.ThucChayHopDongChiTiet  tchdctp
							WHERE 1=1 AND tchdctp.HopDongChiTietREF = @v_HopDongChiTietID
							AND tchdctp.DeletedStatus = 0
							AND tchdctp.RecordStatus = 0
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
							--PRINT @v_ThucChayHopDongChiTietID
							--PRINT @v_HopDongChiTietID
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
												) THEN TD.SoLuong --HAIDH COMMENT: DAY LA THONG TIN SO LUONG TREO DUNG CHO TRUONG HOP KHUYEN MAI
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
									'sp_TC_InsertThucChayDaTinh_TinhTheoChiPhiKhac_ByHopDongChiTiet' GhiChu
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
												C.DmNhanHangREF_thuctreo AS NhanHang,
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
																	ISNULL(tchdctp.DmNhanHangREF,'') DmNhanHangREF_thuctreo,
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
										(@v_HopDongChiTietID
										, @v_ThucChayHopDongChiTietID
										, @NgayThucHien
										, 0 
										, @v_ChietKhau
										, @v_thanhTienHDCN
										, @v_DonGiaHDCN
										, @v_SoLuongHDCN
										, GETDATE()
										, 0)

							--CHECK VA THUC HIEN UPDATE TRANG THAI THUC TREO
							IF(EXISTS(SELECT HopDongChiTietREF FROM dbo.ThucChayDaTinh 
										WHERE HopDongChiTietREF = @v_HopDongChiTietID 
										AND DotChayBooking = CONVERT(NVARCHAR(100),@v_ThucChayHopDongChiTietID)
										AND NgayThucHien = @NgayThucHien
										AND GiaTriThayDoi = 0 )
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


```
