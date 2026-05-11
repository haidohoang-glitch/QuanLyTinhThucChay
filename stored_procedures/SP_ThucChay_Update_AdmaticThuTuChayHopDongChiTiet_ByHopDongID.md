# Stored Procedure: `ThucChay_Update_AdmaticThuTuChayHopDongChiTiet_ByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-15 17:59:15.923000
- **Ngày sửa cuối**: 2020-05-27 14:34:26.397000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongFK` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
[dbo].[ThucChay_Update_AdmaticThuTuChayHopDongChiTiet_ByHopDongID] 1023391
*/

CREATE  PROCEDURE [dbo].[ThucChay_Update_AdmaticThuTuChayHopDongChiTiet_ByHopDongID] 
	@HopDongFK INT
AS
BEGIN
	DECLARE @HopDongID INT
	CREATE Table #AdmaticThuTuChayHopDongChiTiet (
	[SoHopDong] [NVARCHAR](50) NULL,
	[HopDongFK] [INT] NOT NULL,
	[HopDongChiTietID] [INT] NOT NULL,
	[SoThuTuChay] [INT] NULL,
	[DmLoaiREF] [INT] NULL,
	[TenLoai] [NVARCHAR](250) NULL,
	[DmSanPhamREF] [INT] NULL,
	[TenSanPham] [NVARCHAR](500) NULL,
	[DmLoaiBannerREF] [INT] NULL,
	[TenLoaiBanner] [NVARCHAR](250) NULL,
	[SoLuong] [INT] NULL,
	[DonViTinhREF] [INT] NULL,
	[DonViTinh] [NVARCHAR](50) NULL,
	[DonGia] [FLOAT] NULL,
	[ChietKhau] [FLOAT] NULL,
	[KhuyenMai] [NVARCHAR](250) NULL,
	[IsKhuyenMai] [INT] NULL,
	[ThanhTien] [FLOAT] NULL,
	[SoluongThucChay] [FLOAT] NULL,
	[ThanhtienThucChayTruocChietKhau] [FLOAT] NULL,
	[TrangthaiThucChay] [INT] NULL,
	[ThucChayDenNgay] [DATETIME] NULL,
	[ThoiGianMinDotChay] [DATETIME] NULL,
	[ThoiGianMaxDotChay] [DATETIME] NULL,
	[GhiChu] [NVARCHAR](255) NULL,
	[CreatedBy] [NVARCHAR](50) NULL,
	[CreatedAt] [DATETIME] NOT NULL,
	[LastModifiedBy] [NVARCHAR](50) NULL,
	[LastModifiedAt] [DATETIME] NOT NULL,
	[DeletedStatus] [INT] NOT NULL,
	[PrintStatus] [INT] NOT NULL,
	[RecordStatus] [INT] NOT NULL,
	[status] [INT] 
)
	DECLARE Cursor_ThuTuHopdongChiTiet CURSOR FOR
	--1. Xac dinh hop dong
	SELECT DISTINCT hd.HopDongID FROM dbo.HopDong hd
	INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE hdct.DmLoaiREF =42
	AND hd.DeletedStatus =0
	AND hdct.DeletedStatus = 0
	AND hd.HopDongID = @HopDongFK

	OPEN Cursor_ThuTuHopdongChiTiet
	FETCH NEXT FROM Cursor_ThuTuHopdongChiTiet INTO @HopDongID
	WHILE @@FETCH_STATUS =0
	BEGIN
		--Neu tren thuc treo cua Admatic co thong tin hopdongchitiet thi
		TRUNCATE TABLE #AdmaticThuTuChayHopDongChiTiet
		--VIET FUNCTION XÁC ĐỊNH THỨ TỰ ƯU TIÊN TÍNH THỰC CHẠY. CHO TỪNG PHÂN BỔ
		--1. ƯU TIÊN THEO PHÂN BỔ CHÍNH SAU ĐẾN PHÂN BỔ KHUYÊN MẠI
		--2. ƯU TIÊN THEO THÔNG TIN ĐỢT CHẠY
		--3. ƯU TIÊN THEO THÔNG TIN THỨ TỰ PHÂN BỔ TẠO TRƯỚC
		INSERT INTO #AdmaticThuTuChayHopDongChiTiet
	
		SELECT hd.SoHopDong, hd.HopDongID, hdct.HopDongChiTietID
		,ROW_NUMBER() OVER (PARTITION BY hd.HopDongID ORDER BY hd.HopDongID, hdct.loaichietkhau, dchdct.minThoiGianBatDau, dchdct.HopDongChiTietREF) as SoThuTuChay
		, hdct.DmLoaiREF, hdct.TenLoai, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmLoaiBannerREF, hdct.TenLoaiBanner, hdct.SoLuong, hdct.DonViTinhREF,hdct.DonViTinh
		, hdct.DonGia, hdct.ChietKhau, hdct.KhuyenMai, hdct.IsKhuyenMai, hdct.ThanhTien, hdct.SoluongThucChay
		, 0 ThanhtienThucChayTruocChietKhau, 0 TrangthaiThucChay, hdct.ThucChayDenNgay
		, ISNULL(dchdct.minThoiGianBatDau,'1900-01-01')minThoiGianBatDau
		, ISNULL(dchdct.MaxThoiGianKetThuc,'1900-01-01')MaxThoiGianKetThuc
		, hd.GhiChu, hdct.CreatedBy, hdct.CreatedAt CreatedAt, hdct.LastModifiedBy, hdct.LastModifiedAt, hdct.DeletedStatus, 0 PrintStatus, 0 RecordStatus
		, 0 [status]
		FROM dbo.HopDong hd
		INNER JOIN (SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DmLoaiREF, hdct.TenLoai, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmLoaiBannerREF
			, hdct.TenLoaiBanner, hdct.SoLuong, hdct.DonViTinhREF,hdct.DonViTinh, hdct.ThucChayDenNgay
			, (CASE WHEN hdct.chietkhau = 100 THEN 100
			ELSE 0
			END ) AS loaichietkhau
			, hdct.DonGia, hdct.ChietKhau, hdct.KhuyenMai, hdct.IsKhuyenMai, hdct.ThanhTien, hdct.SoluongThucChay
			, hdct.CreatedBy, hdct.CreatedAt CreatedAt, hdct.LastModifiedBy, hdct.LastModifiedAt, hdct.DeletedStatus 
			FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongFK = @HopDongID
		) hdct ON hd.HopDongID = hdct.HopDongFK
		LEFT JOIN (
			SELECT MIN(ThoiGianBatDau)minThoiGianBatDau, MAX(ThoiGianKetThuc)MaxThoiGianKetThuc, HopDongChiTietREF
			FROM dbo.DotChayHopDongChiTiet
			WHERE DeletedStatus = 0
			GROUP BY HopDongChiTietREF
		)dchdct ON hdct.HopDongChiTietID = dchdct.HopDongChiTietREF
		WHERE hdct.DmLoaiREF =42
		AND hd.DeletedStatus =0
		AND hdct.DeletedStatus = 0
		AND hd.HopDongID = @HopDongID
		AND hdct.DmSanPhamREF NOT IN  (736,817) -- chi phí công nghệ, chi phi marketing fee
		--Update ban ghi da ton tai
		UPDATE #AdmaticThuTuChayHopDongChiTiet
		SET    [STATUS] = 1
		FROM  #AdmaticThuTuChayHopDongChiTiet t INNER JOIN AdmaticThuTuChayHopDongChiTiet dc
		ON t.HopDongChiTietID = dc.HopDongChiTietID

		--select * from #AdmaticThuTuChayHopDongChiTiet

		--Update

		UPDATE [dbo].[AdmaticThuTuChayHopDongChiTiet]
		   SET [SoHopDong] = hdct.SoHopDong
			  ,[HopDongFK] = hdct.HopDongFK
			  ,[HopDongChiTietID] = hdct.HopDongChiTietID
			  ,[SoThuTuChay] = hdct.SoThuTuChay
			  ,[DmLoaiREF] = hdct.DmLoaiREF
			  ,[TenLoai] = hdct.TenLoai
			  ,[DmSanPhamREF] = hdct.DmSanPhamREF
			  ,[TenSanPham] = hdct.TenSanPham
			  ,[DmLoaiBannerREF] = hdct.DmLoaiBannerREF
			  ,[TenLoaiBanner] = hdct.TenLoaiBanner
			  ,[SoLuong] = hdct.SoLuong
			  ,[DonViTinhREF] = hdct.DonViTinhREF
			  ,[DonViTinh] = hdct.DonViTinh
			  ,[DonGia] = hdct.DonGia
			  ,[ChietKhau] = hdct.ChietKhau
			  ,[KhuyenMai] = hdct.KhuyenMai
			  ,[IsKhuyenMai] = hdct.IsKhuyenMai
			  ,[ThanhTien] = hdct.ThanhTien
			  --haidh(07-12-2016)Cho nay phai xem lai vi soluongthucchay nay dang theo donvitinhthucchay
			  --,[SoluongThucChay] = hdct.SoluongThucChay 
			  --,[ThanhtienThucChay] = hdct.ThanhtienThucChayTruocChietKhau
			  --,[TrangthaiThucChay] = hdct.TrangthaiThucChay
			  --,[ThucChayDenNgay] = hdct.ThucChayDenNgay
			  ,[ThoiGianMinDotChay] = hdct.ThoiGianMinDotChay
			  ,[ThoiGianMaxDotChay] = hdct.ThoiGianMaxDotChay
			  ,[GhiChu] = hdct.GhiChu
			  ,[CreatedBy] = hdct.CreatedBy
			  ,[CreatedAt] = hdct.CreatedAt
			  ,[LastModifiedBy] = hdct.LastModifiedBy
			  ,[LastModifiedAt] = hdct.LastModifiedAt
			  ,[DeletedStatus] = hdct.DeletedStatus
			  ,[PrintStatus] = hdct.PrintStatus
			  ,[RecordStatus] = hdct.RecordStatus
		 FROM #AdmaticThuTuChayHopDongChiTiet hdct
		 WHERE [dbo].[AdmaticThuTuChayHopDongChiTiet].HopDongChiTietID = hdct.HopDongChiTietID AND hdct.[status] = 1

		INSERT INTO [dbo].[AdmaticThuTuChayHopDongChiTiet]
				   ([SoHopDong]
				   ,[HopDongFK]
				   ,[HopDongChiTietID]
				   ,[SoThuTuChay]
				   ,[DmLoaiREF]
				   ,[TenLoai]
				   ,[DmSanPhamREF]
				   ,[TenSanPham]
				   ,[DmLoaiBannerREF]
				   ,[TenLoaiBanner]
				   ,[SoLuong]
				   ,[DonViTinhREF]
				   ,[DonViTinh]
				   ,[DonGia]
				   ,[ChietKhau]
				   ,[KhuyenMai]
				   ,[IsKhuyenMai]
				   ,[ThanhTien]
				   ,[SoluongThucChay]
				   ,[ThanhtienThucChay]
				   ,[TrangthaiThucChay]
				   ,[ThucChayDenNgay]
				   ,[ThoiGianMinDotChay]
				   ,[ThoiGianMaxDotChay]
				   ,[GhiChu]
				   ,[CreatedBy]
				   ,[CreatedAt]
				   ,[LastModifiedBy]
				   ,[LastModifiedAt]
				   ,[DeletedStatus]
				   ,[PrintStatus]
				   ,[RecordStatus])
			SELECT [SoHopDong]
				   ,[HopDongFK]
				   ,[HopDongChiTietID]
				   ,[SoThuTuChay]
				   ,[DmLoaiREF]
				   ,[TenLoai]
				   ,[DmSanPhamREF]
				   ,[TenSanPham]
				   ,[DmLoaiBannerREF]
				   ,[TenLoaiBanner]
				   ,[SoLuong]
				   ,[DonViTinhREF]
				   ,[DonViTinh]
				   ,[DonGia]
				   ,[ChietKhau]
				   ,[KhuyenMai]
				   ,[IsKhuyenMai]
				   ,[ThanhTien]
				   ,[SoluongThucChay]
				   ,[ThanhtienThucChayTruocChietKhau]
				   ,[TrangthaiThucChay]
				   ,[ThucChayDenNgay]
				   ,[ThoiGianMinDotChay]
				   ,[ThoiGianMaxDotChay]
				   ,[GhiChu]
				   ,[CreatedBy]
				   ,[CreatedAt]
				   ,[LastModifiedBy]
				   ,[LastModifiedAt]
				   ,[DeletedStatus]
				   ,[PrintStatus]
				   ,[RecordStatus] 
				   FROM #AdmaticThuTuChayHopDongChiTiet
			WHERE [status] =0

		
	--SELECT 1;
	FETCH NEXT FROM Cursor_ThuTuHopdongChiTiet INTO @HopDongID
	END
	CLOSE Cursor_ThuTuHopdongChiTiet;
	DEALLOCATE Cursor_ThuTuHopdongChiTiet;
	--select * from [AdmaticThuTuChayHopDongChiTiet] where HopDongFK = @HopDongID
	
	DROP TABLE #AdmaticThuTuChayHopDongChiTiet
END

```
