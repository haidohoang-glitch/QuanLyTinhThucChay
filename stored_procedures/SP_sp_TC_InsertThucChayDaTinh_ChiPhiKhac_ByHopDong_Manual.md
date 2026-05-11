# Stored Procedure: `sp_TC_InsertThucChayDaTinh_ChiPhiKhac_ByHopDong_Manual`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-12-21 10:06:44.833000
- **Ngày sửa cuối**: 2021-05-10 08:54:18.903000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
--EXEC [ThucChay_InsertThucChayDaTinh_ChiPhiKhac] '2014-06-11 00:00:00.000','2014-06-11 15:42:55.690'
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[sp_TC_InsertThucChayDaTinh_ChiPhiKhac_ByHopDong_Manual]
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
			@v_SoLuongHDCN INT
		
		SET @NgayThucTreoTaoChiPhi = DATEADD(DAY,-180,GETDATE())
		IF(@pSoHopDong IS NOT NULL)
			SET @p_HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @pSoHopDong ORDER BY HopDongID)
		ELSE
			SET @p_HopDongID = 0

       	DECLARE Record_Cursor_SPChiPhi CURSOR FOR 

		SELECT  ct.HopDongFK, tchdctp.ThucChayHopDongChiTietID, ct.HopDongChiTietID, ct.ChietKhau, ct.ThanhTien, ct.DonGia, ct.SoLuong
            FROM
                (SELECT * FROM dbo.HopDongChiTiet 
					WHERE DmSanPhamREF IN (242, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542
								, 555, 556, 557, 558, 559, 560, 561, 586, 635, 563, 631, 651, 630, 726, 731
								, 730, 629, 729, 633, 734, 736, 771, 772,775,792, 805 , 806 ,817, 5012, 5075 ,5074 ,5073
																		,5072 ,5071 ,5070
																		,5094	--Youtube
									,5095	--Instagram
									,5096	--Chi phí tư vấn - Sáng tạo
									,5109
									,5119,5120,5121,5122,5123,5128,5129,5130,5136,550,5141,5142,5143,5149 --bizfly
									,5156,5157,5158,5159,5160,5161,5162,5163,5164,5165
									,5140,5207
									 )
						AND NOT ( DmLoaiREF = 13 OR DmLoaiBannerREF = 18)
					AND (HopDongFK = @p_HopDongID OR @p_HopDongID = 0)
					AND DeletedStatus = 0
				) ct
                INNER JOIN 
				(SELECT * FROM dbo.ThucChayHopDongChiTiet  tchdctp
						WHERE tchdctp.DmSanPhamREF IN (242, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542
								, 555, 556, 557, 558, 559, 560, 561, 586, 635, 563, 631, 651, 630, 726, 731
								, 730, 629, 729, 633, 734, 736, 771, 772,775,792, 805 , 806 ,817 , 5012, 5075 ,5074 ,5073
																		,5072 ,5071 ,5070
																		,5094	--Youtube
									,5095	--Instagram
									,5096	--Chi phí tư vấn - Sáng tạo
									,5109
									,5119,5120,5121,5122,5123,5128,5129,5130,5136,550,5141,5142,5143,5149 --bizfly
									,5156,5157,5158,5159,5160,5161,5162,5163,5164,5165
									,5140,5207
									 )
						AND tchdctp.DeletedStatus = 0
						AND tchdctp.RecordStatus = 0
						AND (tchdctp.HopDongREF = @p_HopDongID OR @p_HopDongID = 0)
						AND tchdctp.CreatedAt >= @NgayThucTreoTaoChiPhi
						AND CONVERT(DATE,tchdctp.CreatedAt) <= @NgayThucHien
				) tchdctp ON ct.HopDongChiTietID = tchdctp.HopDongChiTietREF
                 
                           
		OPEN Record_Cursor_SPChiPhi

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor_SPChiPhi INTO @v_HopDongID, @v_ThucChayHopDongChiTietID, @v_HopDongChiTietID, @v_ChietKhau, @v_thanhTienHDCN, @v_DonGiaHDCN, @v_SoLuongHDCN
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--CHECK GIA TRI THUCCHAYDATINH
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
										ISNULL(C.SoLuongThucTreo, 0) * ISNULL(C.DonGiaThucTreo, 0) AS ThanhTienThucChayTruocTrietKhau
								FROM      ( SELECT    *
											FROM      ( SELECT
															ct.* ,
															tchdctp.DmNhanHangREF DmNhanHangTreoID,
															tchdctp.SoLuongThucTreo ,
															tchdctp.DonGia DonGiaThucTreo ,
															tchdctp.ChietKhau ChietKhauThucTreo ,
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
