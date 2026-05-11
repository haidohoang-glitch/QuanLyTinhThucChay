# Stored Procedure: `Insert_DoanhSoHaiDauHopDongCore_PhatSinhGiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 16:42:57.177000
- **Ngày sửa cuối**: 2015-04-22 16:42:57.177000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |
| `@LyDoThayDoi` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[Insert_DoanhSoHaiDauHopDongCore_PhatSinhGiaTriThayDoi] '2013-01-01', 222, 33466, 123
CREATE PROCEDURE [dbo].[Insert_DoanhSoHaiDauHopDongCore_PhatSinhGiaTriThayDoi]
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmMaHopDongREF INT,
	@LyDoThayDoi NVARCHAR(200)
AS
BEGIN
	DECLARE @IsHopDongNoiBo INT --1: HD Noi Bo, 0: HopDong KHONG la Noi Bo
    DECLARE @IsCheckThayDoi INT, @countbefor INT, @countaffter INT ;
    SET @IsCheckThayDoi =0 
    SET @countbefor = 0
    SET @countaffter = 0
    
	SET @IsHopDongNoiBo = [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](@DmMaHopDongREF, @NgayThucHien)
	--INSERT GIA TRI CHO CAC DOI TUONG BI THAY DOI VE 0
	INSERT INTO DoanhSoHaiDauHopDongCore
	SELECT TOP 1
	  @NgayThucHien
	  ,dskc.HopDongID
	  ,dskc.SoHopDong
	  ,dskc.TenNhanVien
	  ,dskc.DmNhanVienREF
	  ,dskc.TenPhongBan
	  ,dskc.PhongBanREF
	  ,dskc.TenBoPhan
	  ,dskc.BoPhanREF
	  ,dskc.TenNhom
	  ,dskc.NhomREF
	  ,dskc.TenKhachHang
	  ,dskc.DmKhachHangREF
	  ,dskc.DmHinhThucKhachHangREF
	  ,dskc.TenHinhThucKhachHang
	  ,dskc.HopDongChiTietREF
	  ,dskc.DmHinhThucQuangCaoREF
	  ,dskc.TenHinhThucQuangCao
	  ,dskc.DmSanPhamREF
	  ,dskc.TenSanPham
	  ,dskc.NhomWebsite_TagREF
	  ,dskc.TenNhomWebsite_Tag
	  ,dskc.TenWebsite
	  ,dskc.DmWebsiteREF
	  ,dskc.DmChuyenMucREF
	  ,dskc.TenChuyenMuc
	  ,dskc.TenViTriBanner
	  ,dskc.ViTriBannerREF
	  ,dskc.DmLoaiNenTangREF
	  ,dskc.TenLoaiNenTang
	  --SoLuongThucThu
	  ,dskc.SoLuongPhatSinhCuoiKy AS SoLuongPhatSinhDauKy
	  ,-dskc.SoLuongPhatSinhCuoiKy AS SoLuongPhatSinhTrongKy
	  ,0 SoLuongPhatSinhCuoiKy
	  --SoLuongKM
	  ,dskc.SoLuongKMPhatSinhCuoiKy AS SoLuongKMPhatSinhDauKy
	  ,- dskc.SoLuongKMPhatSinhCuoiKy SoLuongKMPhatSinhTrongKy
	  ,0 SoLuongKMPhatSinhCuoiKy
	  --SoLuongNOIBo
	  ,dskc.SoLuongNoiBoPhatSInhCuoiKy SoLuongNoiBoPhatSinhDauKy
	  ,-dskc.SoLuongNoiBoPhatSInhCuoiKy SoLuongNoiBoPhatSinhTrongKy
	  ,0 SoLuongNoiBoPhatSInhCuoiKy
	  ,dskc.DonViTinhREF
	  ,dskc.DonViTinh
	  ,dskc.TenDangNhap
	  ,dskc.DonGia
	  ,dskc.ChietKhau
	  --ThanhTienThucThu
	  ,dskc.ThucThuPhatSinhCuoiKy ThucThuPhatSinhDauKy
	  ,- dskc.ThucThuPhatSinhCuoiKy ThucThuPhatSinhTrongKy
	  ,0 ThucThuPhatSinhCuoiKy
	  --ThanhTienKM
	  ,dskc.KhuyenMaiPhatSinhCuoiKy KhuyenMaiPhatSinhDauKy
	  ,-dskc.KhuyenMaiPhatSinhCuoiKy KhuyenMaiPhatSinhTrongKy
	  ,0 KhuyenMaiPhatSinhCuoiKy
	  --ThanhTienNOIBo
	  ,dskc.NoiBoPhatSinhCuoiKy NoiBoPhatSinhDauKy
	  ,-dskc.NoiBoPhatSinhCuoiKy NoiBoPhatSinhTrongKy
	  ,0 NoiBoPhatSinhCuoiKy
	  ,dskc.TrangThaiHopDong
	  ,'Update gia tri thay doi' + @LyDoThayDoi as DienGiai
	  ,'ASD' CreatedBy
	  ,GETDATE() CreatedAt
	  ,'ASD' LastModifiedBy
	  ,GETDATE() lastModifiedAt
	  ,0 RecordStatus
	  ,0 DeletedStatus
	  ,0 PrintStatus
	  ,2 --Phat sinh gia tri thay doi de can bang ve 0
	  ,'' AS TenFileType
	  ,0
	  ,dskc.NgayNhanBanCung
	  ,dskc.NgayChuyenKeToan
	  ,dskc.NgayDanhSo
	  ,dskc.NgayKyHopDong
	  ,dskc.DmMaHopDongREF
	FROM DoanhSoHaiDauHopDongCore dskc
	WHERE dskc.HopDongID = @HopDongID
	AND dskc.HopDongChiTietREF = @HopDongChiTietREF
	AND CONVERT(date,NgayThucHien) <= @NgayThucHien
	AND dskc.TypeRecordStatus IN (0,1,3)
	ORDER BY NgayThucHien DESC
	
	--1. TINH DU LIEU THAY DOI CHO HOP DONG KHONG PHAI LA NOI BO
	IF(@IsHopDongNoiBo = 0)
	BEGIN
		--INSERT GIA TRI PHAT SINH CHO CAC DOI TUONG THAY DOI
		INSERT INTO DoanhSoHaiDauHopDongCore
		SELECT * FROM
		(
			SELECT @NgayThucHien NgayThucHien
			, hd.HopDongID
			, hd.SoHopDong
			, hd.TenNhanVien
			, hd.SysNhanVienREF DmNhanVienREF
			, hd.TenPhongBan
			, isnull(hd.DmPhongBanREF,0) PhongBanREF
			, hd.TenBoPhan
			, isnull(hd.DmBoPhanREF,0)  BoPhanREF
			, hd.TenNhom
			, isnull(hd.DmNhomREF,0) NhomREF
			, hd.TenKhachHang
			, hd.DmKhachHangREF
			, khttc.DmHinhThucKhachHangREF
			, khttc.TenHinhThucKhachHang
			, hdct.HopDongChiTietID
			, hdct.DmLoaiREF DmHinhThucQuangCaoREF
			, hdct.TenLoai TenHinhThucQuangCao
			, hdct.DmSanPhamREF
			, hdct.TenSanPham
			, hdct.DmNhomWebsiteREF DmNhomWebsite_TagREF
			, hdct.TenNhomWebsite NhomWebsite_Tag
			, hdct.TenWebsite	
			, isnull(hdct.DmWebsiteREF,0) AS DmWebsiteREF
			, isnull(hdct.DmChuyenMucREF,0)	 AS DmChuyenMucREF
			, hdct.TenChuyenMuc
			, hdct.TenViTri TenViTriBanner	
			, isnull(hdct.DmViTriREF,0) ViTriBannerREF
			, isnull(hdct.DmLoaiNenTangREF,0) AS DmLoaiNenTangREF
			, hdct.TenLoaiNenTang
			--SoLuongThucThu
			, 0 SoLuongPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE hdct.SoLuong 
					END) SoLuongPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE  hdct.SoLuong
			  END	)SoLuongPhatSinhCuoiKy
			--SoLuongKM
			,0 SoLuongKMPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong
					ELSE 0	END ) SoLuongKMPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong
					ELSE 0  END	)SoLuongKMPhatSinhCuoiKy
			--SoLuongNB
			, 0 SoLuongNoiBoPhatSinhDauKy
			, 0 SoLuongNoiBoPhatSinhTrongKy
			, 0 SoLuongNoiBoPhatSinhCuoiKy
			, hdct.DonViTinhREF
			
			, isnull(hdct.DonViTinh,'') AS DonViTinh
			, hd.TenDangNhap
			, hdct.DonGia
			, hdct.ChietKhau
			--ThanhTienThucThu
			, 0 ThucThuPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE hdct.ThanhTien
				END) ThucThuPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE hdct.ThanhTien  
				END	)ThucThuPhatSinhCuoiKy
			--ThanhTienKM
			, 0 KhuyenMaiPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN (hdct.SoLuong*hdct.DonGia)
					ELSE 0
				END) KhuyenMaiPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN (hdct.SoLuong*hdct.DonGia)
					ELSE  0
				END	)KhuyenMaiPhatSinhCuoiKy
			--ThanhTienNoiBo
			, 0 NoiBoPhatSinhDauKy
			, 0 NoiBoPhatSinhTrongKy
			, 0 NoiBoPhatSinhCuoiKy
			, hd.TrangThaiHopDong	
			, N'Chay du lieu thay doi' DienGiai
			, 'ASD' CreatedBy
			, GETDATE() CreatedAt
			, 'ASD' LastModifiedBy
			, GETDATE() LastModifiedAt
			, 0 RecordStatus
			, 0 DeletedStatus
			, 0 PrintStatus
			, 3 TypeRecordStatus -- 0 La chay du lieu hien tai
			, (SELECT top 1 dft.FileTypeName
			   FROM HopDongAttachFile hdaf INNER JOIN 
			   DmFileType dft ON dft.DmFileTypeID = hdaf.FileTypeREF
			   WHERE hdaf.HopDongREF = hd.HopDongID
			   and hdaf.LastModifiedAt = @NgayThucHien
			  ) AS TenFileType
			, (SELECT top 1 hdaf.FileTypeREF
			   FROM HopDongAttachFile hdaf WHERE hdaf.HopDongREF = hd.HopDongID
			   and hdaf.LastModifiedAt = @NgayThucHien
			  ) AS FileTypeREF
			, (SELECT top 1 hdafbc.NgayNhanBanCung FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
			AND hdafbc.NgayNhanBanCung IS NOT NULL
			) AS NgayNhanBanCung
			, (SELECT top 1 hdafbc.NgayChuyenChoKeToan FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
			AND hdafbc.NgayChuyenChoKeToan IS NOT NULL) AS NgayChuyenChoKeToan
			, hd.NgayDanhSoHopDong
			, hd.NgayKyHopDong
			,hd.DmMaHopDongREF
			FROM HopDong hd
			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
			WHERE hd.HopDongID = @HopDongID
			AND hdct.HopDongChiTietID = @HopDongChiTietREF
			AND hd.IsBanCung = 1
			AND hd.TrangThaiHopDong <>3
			AND hdct.DeletedStatus =0
		)A
		WHERE 	(A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
		OR A.ThucThuPhatSinhTrongKy<> 0 OR A.KhuyenMaiPhatSinhTrongKy <> 0) 			
	END
	--2. TINH DU LIEU PHAT SINH CHO HOP DONG NOI BO
	ELSE
		BEGIN
			INSERT INTO DoanhSoHaiDauHopDongCore
			SELECT * FROM
			(
				SELECT @NgayThucHien NgayThucHien
				, hd.HopDongID
				, hd.SoHopDong
				, hd.TenNhanVien
				, hd.SysNhanVienREF DmNhanVienREF
				, hd.TenPhongBan
				, isnull(hd.DmPhongBanREF,0) PhongBanREF
				, hd.TenBoPhan
				, isnull(hd.DmBoPhanREF,0)  BoPhanREF
				, hd.TenNhom
				, isnull(hd.DmNhomREF,0) NhomREF
				, hd.TenKhachHang
				, hd.DmKhachHangREF
				, khttc.DmHinhThucKhachHangREF
				, khttc.TenHinhThucKhachHang
				, hdct.HopDongChiTietID
				, hdct.DmLoaiREF DmHinhThucQuangCaoREF
				, hdct.TenLoai TenHinhThucQuangCao
				, hdct.DmSanPhamREF
				, hdct.TenSanPham
				, hdct.DmNhomWebsiteREF DmNhomWebsite_TagREF
				, hdct.TenNhomWebsite NhomWebsite_Tag
				, hdct.TenWebsite	
				, isnull(hdct.DmWebsiteREF,0) AS DmWebsiteREF
				, isnull(hdct.DmChuyenMucREF,0)	 AS DmChuyenMucREF
				, hdct.TenChuyenMuc
				, hdct.TenViTri TenViTriBanner	
				, isnull(hdct.DmViTriREF,0) ViTriBannerREF
				, isnull(hdct.DmLoaiNenTangREF,0) AS DmLoaiNenTangREF
				, hdct.TenLoaiNenTang
				--SoLuongThucThu
				, 0 SoLuongPhatSinhDauKy
				, 0 SoLuongPhatSinhTrongKy
				, 0 SoLuongPhatSinhCuoiKy
				--SoLuongKM
				, 0 SoLuongKMPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong
						ELSE 0
						END
				) SoLuongKMPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong
						ELSE  0
				  END	
				) SoLuongKMPhatSinhCuoiKy
						
				--SoLuongNB
				, 0 SoLuongNoiBoPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE hdct.SoLuong
						END
				) SoLuongNoiBoPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE  hdct.SoLuong
				  END	
				) SoLuongNoiBoPhatSinhCuoiKy
				, hdct.DonViTinhREF
				, isnull(hdct.DonViTinh,'') AS DonViTinh
				, hd.TenDangNhap
				, hdct.DonGia
				, hdct.ChietKhau
				--ThanhTienThucThu
				, 0 ThucThuPhatSinhDauKy
				, 0 ThucThuPhatSinhTrongKy
				, 0 ThucThuPhatSinhCuoiKy
				--ThanhTienKM
				, 0 KhuyenMaiPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN hdct.ThanhTien
						ELSE 0
					END
				) KhuyenMaiPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN hdct.ThanhTien
						ELSE 0  
					END	
				) KhuyenMaiPhatSinhCuoiKy
				--ThanhTienNoiBo
				, 0 NoiBoPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE hdct.ThanhTien
					END
				) NoiBoPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE hdct.ThanhTien  
					END	
				) NoiBoPhatSinhCuoiKy
				, hd.TrangThaiHopDong	
				, N'Chay du lieu thay doi' DienGiai
				, 'ASD' CreatedBy
				, GETDATE() CreatedAt
				, 'ASD' LastModifiedBy
				, GETDATE() LastModifiedAt
				, 0 RecordStatus
				, 0 DeletedStatus
				, 0 PrintStatus
				, 3 TypeRecordStatus -- 0 La chay du lieu hien tai
				, (SELECT top 1 dft.FileTypeName
				   FROM HopDongAttachFile hdaf INNER JOIN 
				   DmFileType dft ON dft.DmFileTypeID = hdaf.FileTypeREF
				   WHERE hdaf.HopDongREF = hd.HopDongID
				   and hdaf.LastModifiedAt = @NgayThucHien
				  ) AS TenFileType
				, (SELECT top 1 hdaf.FileTypeREF
				   FROM HopDongAttachFile hdaf WHERE hdaf.HopDongREF = hd.HopDongID
				   and hdaf.LastModifiedAt = @NgayThucHien
				  ) AS FileTypeREF
				, (SELECT top 1 hdafbc.NgayNhanBanCung FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
				AND hdafbc.NgayNhanBanCung IS NOT NULL
				) AS NgayNhanBanCung
				, (SELECT top 1 hdafbc.NgayChuyenChoKeToan FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
				AND hdafbc.NgayChuyenChoKeToan IS NOT NULL) AS NgayChuyenChoKeToan
				, hd.NgayDanhSoHopDong
			, hd.NgayKyHopDong
			,hd.DmMaHopDongREF
				FROM HopDong hd
				INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
				WHERE hd.HopDongID = @HopDongID
				AND hdct.HopDongChiTietID = @HopDongChiTietREF
				AND hd.IsBanCung = 1
				AND hd.TrangThaiHopDong <>3
				AND hdct.DeletedStatus =0
			)A
			WHERE (A.SoLuongKMPhatSinhTrongKy <> 0 OR A.SoLuongNoiBoPhatSinhTrongKy <> 0
			OR A.KhuyenMaiPhatSinhTrongKy <> 0 OR A.NoiBoPhatSinhTrongKy <>0)		
		END
END

```
