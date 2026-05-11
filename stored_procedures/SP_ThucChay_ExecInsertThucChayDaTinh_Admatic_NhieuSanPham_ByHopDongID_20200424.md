# Stored Procedure: `ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham_ByHopDongID_20200424`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-04-24 16:03:09.670000
- **Ngày sửa cuối**: 2020-04-24 16:03:09.670000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongFK` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham_ByHopDongID] 1001352, '2018-06-10'
CREATE  PROCEDURE [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_NhieuSanPham_ByHopDongID_20200424] 
	@HopDongFK INT,
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongID INT, @SoHopDong NVARCHAR(200),@HopDongChiTietID INT, @CreatedAt DATETIME
			, @DonGia INT
			, @SoLuong BIGINT
			, @ThanhTien BIGINT
			, @ChietKhau BIGINT
			, @ThanhtienThucChay BIGINT
			, @DmSanPhamREF INT
			, @DmWebsiteREF INT, @TenWebsite NVARCHAR(200), @DmBannerREF INT, @TypeProduct INT
			, @GhiChu NVARCHAR(1000)

	SET @GhiChu = ''

	--0. Lay danh sach thuc chay can tinh trong ngay cua Admatic goi
	TRUNCATE TABLE ThucChay_Admatic
	SET @SoHopDong = (SELECT TOP 1 SoHopDong FROM dbo.HopDong WHERE HopDongID = @HopDongFK)
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
			  ProductUnitName ,
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
			  tc.ProductUnitName ,
			  tc.BannerTypeName ,
			  tc.HopDongChiTietREF ,
			  tc.CampainStatus ,
			  tc.BannerStatus ,
			  tc.IsNoiBo, bn.HopDongID,0 FROM dbo.ThucChay tc
	INNER JOIN (
		SELECT DISTINCT hd.SoHopDong, hd.HopDongID, bn.DmBannerID 
		FROM dbo.ThucChayHopDongChiTietAndBanner_admatic bn
		INNER JOIN dbo.HopDong hd ON bn.HopDongREF = hd.HopDongID
		WHERE bn.DonViTinh <> N'TRUE VIEW'
	)bn 
	ON tc.SoHopDong = bn.SoHopDong 
	AND tc.DmBannerREF = bn.DmBannerID
	WHERE tc.NgayThucHien = @NgayThucHien
	AND bn.HopDongID = @HopDongFK

	EXEC [dbo].[ThucChay_Insert_ThucChay_Admatic_TrueView_BySoHopDong] @NgayThucHien ,@SoHopDong 

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
			SELECT TOP (1) HopDongChiTietREF FROM dbo.ThucChayHopDongChiTietAndBanner_Admatic
			WHERE DmBannerID = CONVERT(NVARCHAR(50),@DmBannerREF)
			AND HopDongREF = @HopDongID
			AND DmSanPhamID = @DmSanPhamREF
			AND DmSanPhamID <> 733
			AND ISNULL(HopDongChiTietREF,0) NOT IN (0,-1)
			ORDER BY HopDongChiTietREF
		),0)
		IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
		BEGIN
			PRINT 'Xac dinh hop dong chi tiet can tinh thuc chay'
			SET @HopDongChiTietID =
			ISNULL((
				SELECT TOP (1) HopdongchitietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
				INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
				AND att.DmSanPhamREF = tt.DmSanPhamID
				WHERE att.HopDongFK = @HopDongID
				AND att.trangthaithucchay <> 3
				AND att.DmSanPhamREF = @DmSanPhamREF
				AND ABS(att.DonGia - tt.DonGia_Banner) <1 --cho nay xem lai co anh huong den performance
				AND att.DmSanPhamREF <> 733 --khong phai la san pham "Nhieu san pham"
				AND att.DonViTinhREF <> 10 --KHONG PHAI LA GOI
				AND att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
				AND tt.DmBannerID = @DmBannerREF
				ORDER BY att.SoThuTuChay
			),0)
			
			IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
			BEGIN
				SET @HopDongChiTietID =
				ISNULL((
					SELECT TOP (1) HopdongchitietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
					AND att.DmSanPhamREF = tt.DmSanPhamID
					WHERE att.HopDongFK = @HopDongID
					AND att.trangthaithucchay <> 3
					AND att.DmSanPhamREF = @DmSanPhamREF
					AND att.DmSanPhamREF <> 733 --khong phai la san pham "Nhieu san pham"
					AND att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
					AND tt.DmBannerID = @DmBannerREF
					ORDER BY att.SoThuTuChay
				),0)
				IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
				BEGIN
					SET @HopDongChiTietID =
					ISNULL((
					SELECT TOP (1) HopdongchitietID FROM dbo.AdmaticThuTuChayHopDongChiTiet
					WHERE HopDongFK = @HopDongID
					AND trangthaithucchay <> 3
					AND DmSanPhamREF = 733
					ORDER BY SoThuTuChay
					),0)

					IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
					BEGIN
						SET @HopDongChiTietID =
						(
							SELECT TOP (1) HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet
							WHERE HopDongFK = @HopDongID
							AND (DmSanPhamREF = 733 OR DmSanPhamREF = @DmSanPhamREF)
							ORDER BY SoThuTuChay
						)
					END
				END
			END
				
		END
		--IF(@DmBannerREF = 387673)
		--	PRINT 'Dung banner'
		--IF(@HopDongChiTietID = 100897)
		--	PRINT 'Dung hopdongchitiet'
		PRINT 'hopdongid =' + CONVERT(NVARCHAR(50), @HopDongID)
		PRINT @HopDongChiTietID
		PRINT @TypeProduct
		PRINT @DmSanPhamREF
		PRINT @DmWebsiteREF
		PRINT @TenWebsite
		PRINT @DmBannerREF
		--Tinh thuc chay cho hop dong chi tiet
		EXEC [dbo].[ThucChay_InsertThucChayDaTinh_Admatic] 	@NgayThucHien ,	@HopDongID , @SoHopDong , @HopDongChiTietID ,
															@TypeProduct , @DmSanPhamREF , @DmWebsiteREF , @TenWebsite , 
															@DmBannerREF 

		--XAC DINH NGAY PHAT SINH GIA TRI LECH TREO HA
		IF(EXISTS(SELECT TOP 1  NgayThucHien, ThucChayDaTinhID FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @HopDongChiTietID
			AND HopDongID = @HopDongID
			AND SoLuongThucChayLechTreoHa <> 0
			AND NgayThucHien = @NgayThucHien
			AND ChietKhau <> 100
			))
			BEGIN
				SET @ThanhTien = (SELECT ThanhTien FROM dbo.HopDongChiTiet
				WHERE HopDongChiTietID = @HopDongChiTietID)
				EXEC [dbo].[ThucChay_Insert_GTTD_XuLyTienKhongDu_KhiKetThucChay_Admatic]  @NgayThucHien ,	@HopDongID ,@HopDongChiTietID ,	@DmSanPhamREF ,	@ThanhTien, @GhiChu  
			END
		--Update lai thu tu tinh thuc chay cho hopdongchitiet
		EXEC [ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] @NgayThucHien,@HopDongChiTietID
	FETCH NEXT FROM Cursor_hopdong INTO @HopDongID, @SoHopDong, @TypeProduct, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
	END
	CLOSE Cursor_hopdong;
	DEALLOCATE Cursor_hopdong;
	
	--SELECT 1;
END

```
