# Stored Procedure: `ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_ByHopDongChiTietID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-28 17:38:54.033000
- **Ngày sửa cuối**: 2018-07-23 16:47:19.670000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
exec [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_ByHopDongChiTietID] '2018-07-20',524562
*/
CREATE  PROCEDURE [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_ByHopDongChiTietID] 
	@NgayThucHien DATETIME,
	@HopDongChiTietID INT
AS
BEGIN
	DECLARE @HopDongID INT , @NgayThayDoi DATETIME
	, @ThanhTien BIGINT, @ThanhTienThucChay BIGINT, @TrangThayChayHopDongChiTiet INT =0
	DECLARE @TongGiaTriGiam FLOAT=0, @TiLeGiam FLOAT =0, @TongGiaTriTang FLOAT = 0, @ThanhTienThucChayTruocCK FLOAT = 0
	, @ChietkhauHT FLOAT = 0, @ChietKhau_Bf FLOAT = 0, @ghiChu NVARCHAR(1000) = '', @ThucChayDaTinhID NVARCHAR(2000)
	, @DmBannerID INT, @DmWebsiteREF INT

	SET @ChietkhauHT = (SELECT TOP (1) hdct.ChietKhau FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID ORDER BY hdct.HopDongChiTietID)
	SET @ChietKhau_Bf = (SELECT TOP (1) tcdt.ChietKhau FROM dbo.ThucChayDaTinh tcdt WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien ORDER BY tcdt.NgayThucHien DESC)
	SET @HopDongID = (SELECT TOP (1) HopDongFK FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)

	IF (ISNULL(@HopDongChiTietID,0) <>0)
	BEGIN
		--NEU PHAN BO CO THAY DOI CHIET KHAU THI THUC HIEN DOI TRU DI VA TINH LẠI TOAN BO
		IF(@ChietKhau_Bf <> @ChietkhauHT) AND (@ChietKhau_Bf IS NOT NULL)
		BEGIN
			PRINT 'CHIET KHAU THAY DOI => THI THUC HIEN DOI TRU DI VA TINH LẠI TOAN BO'
			SET @ghiChu =  N'ADMATIC_ChietKhau_TD_GTTD đối trừ giảm từ '
			EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_Admatic] 
			@NgayThucHien = @NgayThucHien,
			@HopDongID  = @HopDongID, 
			@HopDongChiTietID = @HopDongChiTietID,
			@GhiChu = @ghiChu
			--2. XAC DINH CAC HOP DONG CHI TIET CHAY UNG VOI DANH SACH BANNER THAY DOI GIA
			DECLARE Cursor_chietkhautd_admatic CURSOR FOR
				SELECT ThucChayDaTinhID
				FROM dbo.ThucChayDaTinh 
				WHERE DmHinhThucQuangCao = 42
				AND HopDongChiTietREF = @HopDongChiTietID
				AND HopDongID = @HopDongID
				AND NgayThucHien < @NgayThucHien --CHO NAY XEM LAI
				AND (TongClickThucChay <> 0 OR TongViewThucChay <> 0)
				ORDER BY CreatedAt
				--AND HopDongID =504166
		
			OPEN Cursor_chietkhautd_admatic
			FETCH NEXT FROM Cursor_chietkhautd_admatic INTO @ThucChayDaTinhID
			WHILE @@FETCH_STATUS =0
			BEGIN
				SET @ghiChu = N'ADMATIC_ChietKhau_TD_GTTD Tăng với chiết khấu mới '
				--4. TINH GIA TRI THUC CHAY CHO CAC HOP DONG CHI TIET
				EXEC [dbo].[ThucChay_Insert_GTTD_ChietKhauMoi_ThucChayDaTinh_Admatic] 
					@NgayThucHien = @NgayThucHien, --@NgayThucHien DATETIME,
					@HopDongID = @HopDongID, --@HopDongID INT, 
					@HopDongChiTietID = @HopDongChiTietID, --@HopDongChiTietID INT
					@ThucChayDaTinhID = @ThucChayDaTinhID,
					@GhiChu = @ghiChu

				--4.1 UPDATE TRANG THAI THUC CHAY TREN THU TU CHAY
				EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay_ByHopDongID] @HopDongID, @NgayThucHien

			FETCH NEXT FROM Cursor_chietkhautd_admatic INTO @ThucChayDaTinhID
			END
			CLOSE Cursor_chietkhautd_admatic;
			DEALLOCATE Cursor_chietkhautd_admatic;
		END
		--CHIET KHAU KHONG THAY DOI
		ELSE
        BEGIN
            --PRINT 'HopDong Admatic co thay doi thanhtien hoac chietkhau'
			SET @ThanhTien = ISNULL((
				SELECT TOP 1 ThanhTien FROM dbo.HopDongChiTiet
				WHERE HopDongChiTietID = @HopDongChiTietID
			),0)

			SET @ThanhTienThucChay = ISNULL((
				SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh
				WHERE HopDongID = @HopDongID
				AND HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien < @NgayThucHien
			),0)

			SET @TrangThayChayHopDongChiTiet = ISNULL((
				SELECT TrangthaiThucChay FROM dbo.AdmaticThuTuChayHopDongChiTiet
				WHERE HopDongChiTietID = @HopDongChiTietID
			),0)
			---*******NOTE: VOI HOP DONG DA CHAY XONG VA CO LECH TREO HA NHUNG THAY DOI TANG THI PHAI THAY DOI LAI TRANG THAI CUA HOP DONG CHI TIET DE CHAY TINH\

			--1.	NEU TRANG THAI CHAY CUA HOP DONG CHI TIET <> 3 (@TrangThayChayHopDongChiTiet<> 3) CHUA CHAY XONG
			IF(@TrangThayChayHopDongChiTiet <> 3)
			BEGIN
				--1.1	NEU @ThanhTien >= @ThanhTienThucChay  VA CHIET KHAU THAY DOI => TINH GIA TRI THAY DOI
				IF(@ThanhTien >= @ThanhTienThucChay)
					BEGIN
						--NEU CO SU THAY DOI VE CHIET KHAU
						IF(EXISTS(SELECT DISTINCT hdcttd.HopDongChiTietREF
							FROM dbo.HopDongThayDoi hdtd
							INNER JOIN dbo.HopDongChiTietThayDoi hdcttd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
							INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = hdcttd.HopDongChiTietREF
							WHERE hdtd.LoaiThayDoi = 1
							AND CONVERT(DATE,hdtd.NgayThayDoi) = @NgayThucHien
							AND((hdct.DmLoaiREF = 42) AND (hdct.ChietKhau <> hdcttd.ChietKhau))
							AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
							AND hdcttd.HopDongChiTietREF = @HopDongChiTietID))
						BEGIN
					    		--XAC DINH THANHTIENTHUCCHAYTRUOCCK
								SET @ThanhTienThucChayTruocCK = ISNULL((
									SELECT SUM((CASE WHEN ChietKhau <> 100 THEN (ThanhTienSauTrietKhauThucChay*(100/(100-ChietKhau)) + GiaTriThayDoi*(100/(100-ChietKhau)))
										ELSE 0
									END))ThanhTienThucChayTruocCK FROM dbo.ThucChayDaTinh
									WHERE HopDongID = @HopDongID
									AND HopDongChiTietREF = @HopDongChiTietID
									AND NgayThucHien < @NgayThucHien
								),0)
								SET @ChietkhauHT = ISNULL((SELECT TOP (1) ChietKhau FROM dbo.HopDongChiTiet
													WHERE HopDongChiTietID = @HopDongChiTietID
													ORDER BY HopDongChiTietID),0)
								SET @TongGiaTriGiam = @ThanhTienThucChayTruocCK*(100/(100-@ChietkhauHT)) - @ThanhTienThucChay

								IF(@ThanhTienThucChay = 0)
									SET @ThanhTienThucChay =1
								SET @TiLeGiam = @TongGiaTriGiam/CONVERT(FLOAT,@ThanhTienThucChay)
								IF(@ThanhTien = 0)
									SET @TiLeGiam = 1
								--PRINT 'CALL HAM TINH GIA TRI THAY DOI'

								EXEC [dbo].[ThucChay_Update_GTTD_Giam_Admatic] 
								@HopDongID, --@HopDongFK INT,
								@HopDongChiTietID, --@HopDongChiTietID INT,
								@TongGiaTriGiam, --@TongGiaTriGiam FLOAT,
								@TiLeGiam, --@TiLeGiam FLOAT,
								@NgayThucHien --@NgayThucHien DATETIME

									--Update lai thu tu tinh thuc chay cho hopdongchitiet
								EXEC [ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] @NgayThucHien =@NgayThucHien,
																					 @HopDongChiTietID =@HopDongChiTietID
						END
						ELSE
							PRINT N'KHONG THAY DOI CHIET KHAU=>KHONG PHAI LAM GI CA'

					END
				--1.2	NEU @ThanhTien < @ThanhTienThucChay =>PHAT SINH GIA TRI THAY DOI GIAM
				ELSE
					BEGIN
						SET @TongGiaTriGiam = @ThanhTienThucChay - @ThanhTien
						IF(@ThanhTienThucChay = 0)
							SET @ThanhTienThucChay =1
						SET @TiLeGiam = @TongGiaTriGiam/CONVERT(FLOAT,@ThanhTienThucChay)
						IF(@ThanhTien = 0)
							SET @TiLeGiam = 1
						--PRINT 'CALL HAM TINH GIA TRI THAY DOI'

						EXEC [dbo].[ThucChay_Update_GTTD_Giam_Admatic] 
						@HopDongID, --@HopDongFK INT,
						@HopDongChiTietID, --@HopDongChiTietID INT,
						@TongGiaTriGiam, --@TongGiaTriGiam FLOAT,
						@TiLeGiam, --@TiLeGiam FLOAT,
						@NgayThucHien --@NgayThucHien DATETIME

						--UPDATE TRANG THAI CHAY CUA HOP DONG = 3 VA GIA TRI THUC CHAY
							--Update lai thu tu tinh thuc chay cho hopdongchitiet
						EXEC [ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] @NgayThucHien =@NgayThucHien,
																			 @HopDongChiTietID =@HopDongChiTietID

					END
			END
			--2.	NEU TRANG THAI CHAY CUA HOP DONG CHI TIET = 3 (@TrangThayChayHopDongChiTiet = 3) DA THUC HIEN CHAY XONG
			ELSE
			BEGIN
				--2.1	NEU @ThanhTien > @ThanhTienThucChay
				IF(@ThanhTien > @ThanhTienThucChay)
				BEGIN
					--2.1.1	NEU CO THONG TIN LECH TREO HA VOI CAC BANNER UNG VOI HOP DONG CHI TIET NAY THI THUC HIEN TINH THEM VAO CHU DU
					--PRINT 'CHECK THONG TIN LECH TREO HA UNG VOI CAC BANNER CUA HOPDONGCHITIET'
					IF(EXISTS(SELECT A.* FROM
						(
							SELECT DonViTinh, SUM(SoLuongThucChay)SoLuongThucChay
							, (CASE WHEN DonViTinh = N'VIEW' THEN SUM(TongViewThucChay)
									WHEN DonViTInh = N'CLICK' THEN SUM(TongClickThucChay)
									WHEN DonViTInh = N'TRUE VIEW' THEN SUM(TongSoBaiViet) --Dung cho true View
									ELSE 0
								END
							)SoLuongChay
							FROM dbo.ThucChayDaTinh
							where DmBannerREF IN
							(
								SELECT DISTINCT DmBannerREF 
								FROM dbo.ThucChayDaTinh
								WHERE HopDongChiTietREF = @HopDongChiTietID
								AND DmHinhThucQuangCao = 42
								AND NgayThucHien <= @NgayThucHien
							)
							AND NgayThucHien <= @NgayThucHien
							GROUP BY DonViTinh
						)A
								WHERE A.SoLuongChay > A.SoLuongThucChay
					))
					BEGIN
						BEGIN
							SET @TongGiaTriTang = @ThanhTien - @ThanhTienThucChay
							--PRINT 'UPDATE TRANG THAI CHAY CUA HOP DONG = 2'
							UPDATE dbo.AdmaticThuTuChayHopDongChiTiet
							SET TrangthaiThucChay = 2
							WHERE HopDongFK = @HopDongID
							AND HopDongChiTietID = @HopDongChiTietID

							PRINT 'THUC HIEN TINH THEM GIA TRI THUC CHAY UNG VOI PHAN VUOT'

							EXEC [dbo].[ThucChay_Update_GTTD_Tang_Admatic] 
							@HopDongID, --@HopDongFK INT,
							@HopDongChiTietID, --@HopDongChiTietID INT,
							@NgayThucHien, --@NgayThucHien DATETIME,
							@TongGiaTriTang --@GiaTriTang FLOAT
						END
					END
					ELSE
					BEGIN
						--2.1.2 NEU KHONG CO THONG TIN LECH TREO HA THI -> THAY DOI TRANG THAI TrangThayChayHopDongChiTiet = 2 VA TIEP TUC TINH
						--PRINT 'UPDATE TRANG THAI CHAY CUA HOP DONG =2'
						UPDATE dbo.AdmaticThuTuChayHopDongChiTiet
						SET TrangthaiThucChay = 2
						WHERE HopDongFK = @HopDongID
						AND HopDongChiTietID = @HopDongChiTietID
						AND ThanhtienThucChay <> 0
					END
				END
				--2.2	NEU @ThanhTien = @ThanhTienThucChay => KHONG PHAI LAM GI CA
				ELSE IF(@ThanhTien = @ThanhTienThucChay)
					BEGIN
						PRINT 'Trangthai = 3 va Thanhtien = ThanhTienThucChay => KHONG PHAI LAM GI CA'
					END
				--2.3	NEU @ThanhTien < @ThanhTienThucChay => PHAT SINH  GIA TRI THAY DOI GIAM
				ELSE IF(@ThanhTien < @ThanhTienThucChay)
					BEGIN
						SET @TongGiaTriGiam = @ThanhTienThucChay - @ThanhTien
						IF(@ThanhTienThucChay = 0)
							SET @ThanhTienThucChay =1
						SET @TiLeGiam = @TongGiaTriGiam/CONVERT(FLOAT,@ThanhTienThucChay)

						IF(@ThanhTien = 0)
							SET @TiLeGiam = 1
						--PRINT 'CALL HAM TINH GIA TRI THAY DOI'
						--PRINT 'TONG GIA TRI GIAM: ' +CONVERT(NVARCHAR(50),@TongGiaTriGiam)
						--PRINT 'TI LE GIAM: ' +CONVERT(NVARCHAR(50),@TiLeGiam)

						EXEC [dbo].[ThucChay_Update_GTTD_Giam_Admatic] 
						@HopDongID, --@HopDongFK INT,
						@HopDongChiTietID, --@HopDongChiTietID INT,
						@TongGiaTriGiam, --@TongGiaTriGiam FLOAT,
						@TiLeGiam, --@TiLeGiam FLOAT,
						@NgayThucHien --@NgayThucHien DATETIME

						--Update lai thu tu tinh thuc chay cho hopdongchitiet
						EXEC [ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] @NgayThucHien =@NgayThucHien,
																			 @HopDongChiTietID =@HopDongChiTietID

					END
			
			END
        END
		
	END

END


```
