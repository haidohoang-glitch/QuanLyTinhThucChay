# Stored Procedure: `sp_TC_InsertThucChayDaTinh_ChiPhiKhac_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-01-04 15:19:43.823000
- **Ngày sửa cuối**: 2024-11-14 10:16:31.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[sp_TC_InsertThucChayDaTinh_ChiPhiKhac_ByHopDong] '2019-05-28', 'TR0030818'
*/
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_ChiPhiKhac_ByHopDong]
   @NgayThucHien DATETIME
  , @pSoHopDong NVARCHAR(100)
AS
     BEGIN

        DECLARE @v_HopDongID INT, @p_HopDongID INT = 0,
			@NgayThucTreoTaoChiPhi DATETIME ,
			@v_HopDongChiTietID INT,
			@v_ThucChayHopDongChiTietID INT,
			@v_ThanhTienThucChayDaTinh BIGINT = 0,
			@v_ThanhTienThucTreo BIGINT = 0,
			@v_ChietKhau FLOAT = 0,
			@v_thanhTienHDCN BIGINT = 0,
			@v_DonGiaHDCN FLOAT = 0,
			@v_SoLuongHDCN INT,
			@NgayDanhSoGioiHan DATETIME = '2021-10-01',
			@NgayDanhSoGioiHan_Tiktok DATETIME = '2022-01-01'
		
		SET @NgayThucTreoTaoChiPhi = DATEADD(DAY,-365,GETDATE())
		IF(@pSoHopDong IS NOT NULL)
			SET @p_HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @pSoHopDong ORDER BY HopDongID)
		ELSE
			SET @p_HopDongID = 0

       	DECLARE Record_Cursor_SPChiPhi CURSOR FOR 

		SELECT  ct.HopDongFK, tchdctp.ThucChayHopDongChiTietID, ct.HopDongChiTietID, ct.ChietKhau, ct.ThanhTien, ct.DonGia, ct.SoLuong
            FROM
                (SELECT * FROM dbo.HopDongChiTiet hdct
					WHERE 1=1 
						AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 		
						AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
						AND NOT (hdct.DmViTriREF in (100093,100478))
						--AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9) --INVENTORY ADMANTIC, thay doi ngay 06/07/2022
					AND (hdct.HopDongFK = @p_HopDongID OR @p_HopDongID = 0)
					AND hdct.DeletedStatus = 0
				) ct
                INNER JOIN 
				(SELECT * FROM dbo.ThucChayHopDongChiTiet  tchdctp
						WHERE 1=1
						AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = tchdctp.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
										)) 	
						AND tchdctp.DeletedStatus = 0
						AND tchdctp.RecordStatus = 0
						AND tchdctp.[TrangThaiTreo] = 2 -- Đa Duyệt
						AND (tchdctp.HopDongREF = @p_HopDongID OR @p_HopDongID = 0)
						AND tchdctp.CreatedAt >= @NgayThucTreoTaoChiPhi
						AND CONVERT(DATE,tchdctp.CreatedAt) <= @NgayThucHien
				) tchdctp ON ct.HopDongChiTietID = tchdctp.HopDongChiTietREF
				INNER JOIN dbo.HopDong hd on hd.HopDongID = ct.HopDongFk
				WHERE 1=1 
				AND NOT (ct.DmSanPhamREF = 5184 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
				AND NOT ((ct.DmSanPhamREF = 5188  OR ct.DmViTriREF = 100774) AND  (hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok)) --haidh comment 20211026 TikTok tinh theo pp GGFB
                 
                           
		OPEN Record_Cursor_SPChiPhi

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor_SPChiPhi INTO @v_HopDongID, @v_ThucChayHopDongChiTietID, @v_HopDongChiTietID, @v_ChietKhau, @v_thanhTienHDCN, @v_DonGiaHDCN, @v_SoLuongHDCN
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--CHECK GIA TRI THUCCHAYDATINH
				--PRINT 'Vonglap' + CONVERT(NVARCHAR(50),@v_ThucChayHopDongChiTietID)
				SET @v_ThanhTienThucChayDaTinh =
					(SELECT  CASE WHEN (@v_ChietKhau <> 100) THEN SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
							ELSE SUM(ThanhTienKM + GiaTriKMThayDoi)
							END 
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
								
				--NEU TIEN THUC CHAY CHUA DU THI SE THUC HIEN TINH
				IF(((@v_ThanhTienThucChayDaTinh + @v_ThanhTienThucTreo)<= @v_thanhTienHDCN) AND @v_ChietKhau <> 100)
				OR (((@v_ThanhTienThucChayDaTinh + @v_ThanhTienThucTreo)<= @v_DonGiaHDCN*@v_SoLuongHDCN) AND @v_ChietKhau = 100)
				BEGIN
					PRINT CONVERT(NVARCHAR(50),@v_ThucChayHopDongChiTietID)

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
										C.DmNhanHangTreoID NhanHang ,
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
										CASE WHEN ISNULL(C.DmWebsiteREF,265) = 265 THEN dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF_thuctreo) 
										ELSE dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF)
										END	DmWebsiteREF ,
										CASE WHEN ISNULL(C.DmWebsiteREF,265) = 265 THEN dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF_thuctreo, C.TenWebsite_thuctreo) 
										ELSE dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF, C.TenWebsite) 
										END TenWebsite ,
										0 TongViewThucChay ,
										0 TongClickThucChay ,
										0 TongSoBaiViet ,
										( CASE WHEN C.IsKhuyenMai = 0
												THEN C.SoLuongThucTreo
												ELSE 0
											END ) AS SoLuongThucChay ,
										@NgayThucHien AS NgayThucHien ,
										0 AS GiaTriThayDoi ,
										ISNULL(C.SoLuongThucTreo, 0) * ISNULL(C.DonGiaThucTreo, 0) AS ThanhTienThucChayTruocTrietKhau
								FROM      ( SELECT    *
											FROM      ( SELECT
															ct.* ,
															tchdctp.DmNhanHangREF DmNhanHangTreoID,
															tchdctp.SoLuongThucTreo ,
															tchdctp.DonGia DonGiaThucTreo ,
															tchdctp.ChietKhau ChietKhauThucTreo ,
															ISNULL(tchdctp.DmWebsiteREF,265) DmWebsiteREF_thuctreo,
															ISNULL(tchdctp.TenWebsite,N'(Blanks)') TenWebsite_thuctreo,
															tchdctp.ThucChayHopDongChiTietID
														FROM
															(SELECT * FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @v_HopDongChiTietID) ct
															INNER JOIN 
															(SELECT * FROM dbo.ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID = @v_ThucChayHopDongChiTietID) tchdctp 
															ON ct.HopDongChiTietID = tchdctp.HopDongChiTietREF
													) T
											WHERE     ( ISNULL(T.SoLuong, 0)
														* ISNULL(T.DonGia, 0) ) >= ( ISNULL(T.SoLuongThucTreo,0) * ISNULL(T.DonGiaThucTreo,0) ) - 1000
										) C
										INNER JOIN 
										( SELECT * FROM dbo.HopDong hd
											WHERE hd.TrangThaiHopDong <> 3
											AND hd.DeletedStatus = 0
											AND  hd.HopDongID = @v_HopDongID
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
							  	
			FETCH NEXT FROM Record_Cursor_SPChiPhi INTO @v_HopDongID, @v_ThucChayHopDongChiTietID, @v_HopDongChiTietID, @v_ChietKhau, @v_thanhTienHDCN, @v_DonGiaHDCN, @v_SoLuongHDCN
			END

		CLOSE Record_Cursor_SPChiPhi
		DEALLOCATE Record_Cursor_SPChiPhi
        SELECT  '1'
    END


```
