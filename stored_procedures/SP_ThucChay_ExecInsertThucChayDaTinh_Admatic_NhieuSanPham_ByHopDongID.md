# Stored Procedure: `ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham_ByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-15 18:00:52.073000
- **Ngày sửa cuối**: 2020-04-24 16:07:50.957000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham] '2017-09-12'
CREATE  PROCEDURE [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham_ByHopDongID] 
	@HopDongID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @SoHopDong NVARCHAR(200),@HopDongChiTietID INT
			--, @DonGia INT
			--, @SoLuong BIGINT
			, @ThanhTien BIGINT
			--, @ChietKhau BIGINT
			--, @ThanhtienThucChay BIGINT
			, @Ghichu NVARCHAR(1000)
			, @DmSanPhamREF INT
			, @DmWebsiteREF INT, @TenWebsite NVARCHAR(200), @DmBannerREF INT, @TypeProduct INT
			

	SET @Ghichu = ''
	set @SoHopDong = (Select SoHopDong from HopDong where HopDongID = @HopDongID)
	--0. Lay danh sach thuc chay can tinh trong ngay cua Admatic goi
	TRUNCATE TABLE ThucChay_Admatic 
	--HAIDH COMMENT : True View Them thong tin thuc chay True View vao table ThucChay_Admatic
	INSERT INTO dbo.ThucChay_Admatic
			( ThucChayID ,
			  SoHopDong ,
			  DanhsachDmBookingREF ,
			  DmSanPhamREF ,
			  TenSanPham ,
			  DmNhomWebsiteREF ,
			  TenNhomWebsite ,
			  DmWebsiteREF ,
			  TenWebsite ,
			  DmChienDichREF ,
			  TenChienDich ,
			  DmBannerREF ,
			  TenBanner ,
			  NgayThucHien ,
			  TongViewThucChay ,
			  TongClickThucChay ,
			  CreatedBy ,
			  CreatedAt ,
			  LastModifiedBy ,
			  LastModifiedAt ,
			  DeletedStatus ,
			  PrintStatus ,
			  RecordStatus ,
			  TongSoBaiViet ,
			  SoThuTuTheoNgay ,
			  TypeProduct ,
			  BannerType ,
			  UserName ,
			  SaleName ,
			  Email ,
			  LastTimeCalc ,
			  sys_date ,
			  IsReady ,
			  ProductUnitID ,
			--  ProductUnitName ,
			  BannerTypeName ,
			  HopDongChiTietREF ,
			  CampainStatus ,
			  BannerStatus ,
			  IsNoiBo,
			  HopDongID,
			  TongTrueViewThucChay
			)
	SELECT tc.ThucChayID ,
			  tc.SoHopDong ,
			  tc.DanhsachDmBookingREF ,
			  [dbo].[GetProductIDByTypeProduct](tc.TypeProduct)DmSanPhamREF ,
			  [dbo].[GetProductNameByTypeProduct](tc.TypeProduct) as TenSanPham,
			  tc.DmNhomWebsiteREF ,
			  tc.TenNhomWebsite ,
			  tc.DmWebsiteREF ,
			  tc.TenWebsite ,
			  tc.DmChienDichREF ,
			  tc.TenChienDich ,
			  tc.DmBannerREF ,
			  tc.TenBanner ,
			  tc.NgayThucHien ,
			  tc.TongViewThucChay ,
			  tc.TongClickThucChay ,
			  tc.CreatedBy ,
			  tc.CreatedAt ,
			  tc.LastModifiedBy ,
			  tc.LastModifiedAt ,
			  tc.DeletedStatus ,
			  tc.PrintStatus ,
			  tc.RecordStatus ,
			  tc.TongSoBaiViet ,
			  tc.SoThuTuTheoNgay ,
			  tc.TypeProduct ,
			  tc.BannerType ,
			  tc.UserName ,
			  tc.SaleName ,
			  tc.Email ,
			  tc.LastTimeCalc ,
			  tc.sys_date ,
			  tc.IsReady ,
			  tc.ProductUnitID ,
			 -- ISNULL(tc.ProductUnitName,'') ,
			  tc.BannerTypeName ,
			  tc.HopDongChiTietREF ,
			  tc.CampainStatus ,
			  tc.BannerStatus ,
			  tc.IsNoiBo, bn.HopDongID, 0 
			  FROM dbo.ThucChay tc 
	INNER JOIN (
		SELECT DISTINCT hd.SoHopDong, hd.HopDongID, bn.DmBannerID 
		FROM dbo.ThucChayHopDongChiTietAndBanner_admatic bn
		INNER JOIN dbo.HopDong hd ON bn.HopDongREF = hd.HopDongID
		WHERE bn.DonViTinh <> N'TRUE VIEW'
	)bn 
	ON tc.SoHopDong = bn.SoHopDong 
	AND tc.DmBannerREF = bn.DmBannerID
	WHERE tc.NgayThucHien = @NgayThucHien and bn.HopDongID = @HopDongID
	--AND bn.DmBannerID = 391402
	--AND bn.SoHopDong = 'QC2931016'
	EXEC [dbo].[ThucChay_Insert_ThucChay_Admatic_TrueView_BySoHopDong] @NgayThucHien, @SoHopDong

	DECLARE Cursor_hopdong CURSOR FOR
		--1. Xac dinh hop dong
	SELECT DISTINCT tc.HopDongID, tc.SoHopDong, tc.TypeProduct, tc.DmSanPhamREF, tc.DmWebsiteREF, tc.TenWebsite, tc.DmBannerREF FROM ThucChay_Admatic tc
	OPEN Cursor_hopdong
	FETCH NEXT FROM Cursor_hopdong INTO @HopDongID, @SoHopDong, @TypeProduct, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
	WHILE @@FETCH_STATUS =0
	BEGIN
		--Neu tren thuc treo cua Admatic co thong tin hopdongchitiet thi
		SET @HopDongChiTietID =
		ISNULL((
			SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
			INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
			AND att.DmSanPhamREF = tt.DmSanPhamID
			WHERE tt.DmBannerID = CONVERT(NVARCHAR(50),@DmBannerREF)
			AND tt.HopDongREF = @HopDongID
			AND tt.DmSanPhamID = @DmSanPhamREF
			AND tt.DmSanPhamID <> 733
			AND ISNULL(tt.HopDongChiTietREF,0) NOT IN (0,-1)
			AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
						AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
						))
					OR (att.DonViTinhREF = 10))
			AND att.DeletedStatus = 0
			ORDER BY tt.HopDongChiTietREF
		),0)
		IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
		BEGIN
			--PRINT 'Xac dinh hop dong chi tiet can tinh thuc chay'
			SET @HopDongChiTietID =
			ISNULL((
				SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
				INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
				AND att.DmSanPhamREF = tt.DmSanPhamID
				WHERE att.HopDongFK = @HopDongID
				AND att.trangthaithucchay <> 3
				AND att.DmSanPhamREF = @DmSanPhamREF
				AND ABS(att.DonGia - tt.DonGia_Banner) <1 --cho nay xem lai co anh huong den performance
				AND att.DmSanPhamREF <> 733 --khong phai la san pham "Nhieu san pham"
				AND tt.DmBannerID = CONVERT(NVARCHAR(50),@DmBannerREF)
				AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
						AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
						))
					OR (att.DonViTinhREF = 10))
				AND att.DeletedStatus = 0
				ORDER BY att.SoThuTuChay
			),0)

				IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
			BEGIN
				SET @HopDongChiTietID =
				ISNULL((
					SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
					AND att.DmSanPhamREF = tt.DmSanPhamID
					WHERE att.HopDongFK = @HopDongID
					AND att.trangthaithucchay <> 3
					AND att.DmSanPhamREF = @DmSanPhamREF
					AND att.DmSanPhamREF <> 733 --khong phai la san pham "Nhieu san pham"
					AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
						AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
						))
					OR (att.DonViTinhREF = 10))
					AND tt.DmBannerID = CONVERT(NVARCHAR(50),@DmBannerREF)
					AND att.DeletedStatus = 0
					ORDER BY att.SoThuTuChay
				),0)
				IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
				BEGIN
					SET @HopDongChiTietID =
					ISNULL((
					SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
					WHERE att.HopDongFK = @HopDongID
					AND tt.DmBannerID = CONVERT(NVARCHAR(50),@DmBannerREF)
					AND att.trangthaithucchay <> 3
					AND att.DmSanPhamREF = 733
					AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
						AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
						))
					OR (att.DonViTinhREF = 10))
					AND att.DeletedStatus = 0
					ORDER BY att.SoThuTuChay
					),0)

					IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
					BEGIN
						SET @HopDongChiTietID =
						(
							SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
							INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
							WHERE att.HopDongFK = @HopDongID
							AND (att.DmSanPhamREF = 733 OR att.DmSanPhamREF = @DmSanPhamREF)
							AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
							AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
								))
							OR (att.DonViTinhREF = 10))
							AND tt.DmBannerID = CONVERT(NVARCHAR(50),@DmBannerREF)
							AND att.DeletedStatus = 0
							ORDER BY att.SoThuTuChay
						)
					END
				END
			END
		END
		--IF(@DmBannerREF = 387673)
		--	PRINT 'Dung banner'
		--IF(@HopDongChiTietID = 100897)
		--	PRINT 'Dung hopdongchitiet'
		--PRINT @HopDongID
		--PRINT @HopDongChiTietID
		--PRINT @TypeProduct
		--PRINT @DmSanPhamREF
		--PRINT @DmWebsiteREF
		--PRINT @TenWebsite
		--PRINT @DmBannerREF
		--Tinh thuc chay cho hop dong chi tiet
		EXEC [dbo].[ThucChay_InsertThucChayDaTinh_Admatic] 	@NgayThucHien ,	@HopDongID , @SoHopDong , @HopDongChiTietID ,
															@TypeProduct , @DmSanPhamREF , @DmWebsiteREF , @TenWebsite , 
															@DmBannerREF 
		
		--Update lai thu tu tinh thuc chay cho hopdongchitiet
		EXEC [ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] @NgayThucHien,@HopDongChiTietID

		--XAC DINH NGAY PHAT SINH GIA TRI LECH TREO HA
		IF(EXISTS(SELECT TOP (1)  NgayThucHien, ThucChayDaTinhID FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @HopDongChiTietID
			AND HopDongID = @HopDongID
			AND SoLuongThucChayLechTreoHa <> 0
			AND NgayThucHien = @NgayThucHien
			AND ChietKhau <> 100
			ORDER BY NgayThucHien
			))
			BEGIN
				SET @ThanhTien = (SELECT TOP (1) ThanhTien FROM dbo.HopDongChiTiet
				WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
				----XU LY LECH TIEN VAI DONG KHI CO PHAT SINH LECH TREO HA
				EXEC [dbo].[ThucChay_Insert_GTTD_XuLyTienKhongDu_KhiKetThucChay_Admatic] @NgayThucHien ,@HopDongID ,@HopDongChiTietID ,	@DmSanPhamREF ,	@ThanhTien , @Ghichu
				----Update lai thu tu tinh thuc chay cho hopdongchitiet
				EXEC [ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] @NgayThucHien,@HopDongChiTietID
				--DAY TIEP THONG TIN LECH TREO HA CHO HOPDONGCHITIET KE TIEP NEU CO NHIEU HON 1 HOPDONGCHITIET    
				IF(EXISTS(SELECT HopDongFK FROM dbo.HopDongChiTiet
				WHERE HopDongFK = @HopDongID
				AND DmLoaiREF = 42
				AND DeletedStatus = 0
				GROUP BY HopDongFK HAVING COUNT(HopDongFK) >1))
				BEGIN
				    EXEC [dbo].[ThucChay_Insert_XuLyLechTreoHa_ThucChayDaTinh_Admatic_ByHopDong] 
						@NgayThucHien = @NgayThucHien,
						@HopDongID  = @HopDongID, 
						@DmBannerREF  = @DmBannerREF,
						@HopDongChiTietID  = @HopDongChiTietID,
						@DmWebsiteREF = @DmWebsiteREF, 
						@TenWebiste = @TenWebsite,
						@TypeProduct = @TypeProduct, 
						@DmSanPhamREF = @DmSanPhamREF,
						@ThanhTienHDCT = @ThanhTien,
						@GhiChu = ''
				END
					
			END
		
	
	FETCH NEXT FROM Cursor_hopdong INTO @HopDongID, @SoHopDong, @TypeProduct, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
	END
	CLOSE Cursor_hopdong;
	DEALLOCATE Cursor_hopdong;
	
	--SELECT 1;
END

```
