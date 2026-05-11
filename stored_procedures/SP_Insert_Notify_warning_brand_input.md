# Stored Procedure: `Insert_Notify_warning_brand_input`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-03 09:51:36.003000
- **Ngày sửa cuối**: 2020-06-08 09:16:06.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[Insert_Notify_warning_brand_input]	'2016-10-31'
*/
CREATE PROCEDURE [dbo].[Insert_Notify_warning_brand_input]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Table_ThucChayHopDongChiTiet TABLE(HopDongID INT, HopDongChiTietID INT, DmHinhThucQuangCaoID INT
	, DmSanPhamID INT, DmLoaiBannerID INT, TenSanPham NVARCHAR(200), ThucChayHopDongChiTietID INT, TenNhanHang NVARCHAR(500), DmNhanHangID INT)

	DELETE FROM [dbo].[ThongTinCanhBaoNhanHang]
	WHERE LoaiDulieu = 1 --dulieu input
	AND LoaiVanDe IN (1,2,3,4,5,6)
	AND NgayThucHien = @NgayThucHien

	----***********CHECK THONG TIN DAU VAO************-----------------
	----0. CO DU LIEU DONG BO NGAY THUC HIEN
	----1. DANH SACH CAC SAN PHAM CHAY CO NHAN TINH THEO THUC TREO	

	----1.1 DANH SACH CAC SAN PHAM CHAY CO NHAN TINH THEO THUC TREO KHONG PHAI DANG TIN
	INSERT INTO @Table_ThucChayHopDongChiTiet
	SELECT tchdct.HopDongREF, tchdct.HopDongChiTietREF , hdct.DmLoaiREF
	, hdct.DmSanPhamREF, hdct.DmLoaiBannerREF, hdct.TenSanPham, tchdct.ThucChayHopDongChiTietID, tchdct.NhanHang, CONVERT(INT,ISNULL(tchdct.DmNhanHangREF,0))DmNhanHangREF
	FROM dbo.HopDongChiTiet hdct
	INNER JOIN dbo.ThucChayHopDongChiTiet tchdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
	WHERE hdct.DeletedStatus = 0
	AND tchdct.DeletedStatus = 0
	AND NOT(hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18) ---- KHONG PHAI LA MUA NGOAI
	AND NOT(hdct.DonViTinhREF = 19)	----DON VI TINH LA CPA
	AND hdct.HopDongFK NOT IN (SELECT DISTINCT HopDongREF FROM dbo.DmThongTinHopDongBanInventory)
	AND hdct.DmSanPhamREF IN (242,240, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542, 555, 556, 557 , 558, 559, 560, 561, 635
				, 563,631,613, 651,630,140,228,549,564,231,238, 531, 370, 339,342, 385, 598, 680,726,731)
	AND CONVERT(DATE,tchdct.LastModifiedAt) = @NgayThuchien
	UNION ALL
	------1.2 DANH SACH CAC SAN PHAM CHAY CO NHAN TINH THEO THUC TREO - DANG TIN
	SELECT tchdct.HopDongREF, tchdct.HopDongChiTietREF, tchdct.DmHinhThucQuangCaoREF
	,tchdct.DmSanPhamREF,0 AS DmLoaiBannerREF, (SELECT TOP (1) sp.TenSanPham FROM dbo.DmSanPham sp WHERE sp.DmSanPhamID = tchdct.DmSanPhamREF ORDER BY sp.DmSanPhamID) AS TenSanPham
	, tchdct.ThucChayHopDongChiTietPRID, tchdct.NhanHang, CONVERT(INT,ISNULL(tchdct.DmNhanHangREF,0))DmNhanHangREF
	FROM dbo.ThucChayHopDongChiTietPR tchdct
	WHERE 1=1
	AND tchdct.DeletedStatus = 0
	AND CONVERT(DATE,tchdct.LastModifiedAt) = @NgayThuchien

	--TH1: Ko có ID nhãn nhưng Tên nhãn đã có trên ABM : LoaiVanDe = 1, 
	INSERT INTO [dbo].[ThongTinCanhBaoNhanHang]
           ([HopDongID]
           ,[HopDongChiTietID]
           ,[DmHinhThucQuangCaoID]
           ,[DmSanPhamID]
           ,[DmLoaiBannerID]
           ,[TenSanPham]
           ,[ThucChayHopDongChiTietID]
           ,[TenNhanHang]
           ,[DmNhanHangID]
           ,[NgayThucHien]
           ,[LoaiDulieu] --1 input du lieu, 2 du lieu tinh thuc chay
           ,[LoaiVanDe] --loai van de loi
           ,[TenLoaiVanDe]
           ,[GhiChu]
           ,[CreatedAt]
           ,[CreatedBy])
	SELECT tchdct.HopDongID, tchdct.HopDongChiTietID, tchdct.DmHinhThucQuangCaoID, tchdct.DmSanPhamID
	, tchdct.DmLoaiBannerID, tchdct.TenSanPham, tchdct.ThucChayHopDongChiTietID, tchdct.TenNhanHang
	, tchdct.DmNhanHangID, @NgayThucHien, 1 LoaiDuLieu, 1 LoaiVanDe, N'Ko có ID nhãn nhưng Tên nhãn đã có trên ABM' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'asd' CreatedBy
	FROM @Table_ThucChayHopDongChiTiet tchdct
	INNER JOIN [asd14].BRAND.dbo.DmNhanHang nh ON nh.TenNhanHang = tchdct.TenNhanHang
	WHERE ISNULL(tchdct.TenNhanHang,'') <> ''
	AND tchdct.DmNhanHangID = 0

	--TH2:  Ko có ID nhãn & Tên nhãn chưa có trên ABM : LoaiVanDe = 1, 
	INSERT INTO [dbo].[ThongTinCanhBaoNhanHang]
           ([HopDongID]
           ,[HopDongChiTietID]
           ,[DmHinhThucQuangCaoID]
           ,[DmSanPhamID]
           ,[DmLoaiBannerID]
           ,[TenSanPham]
           ,[ThucChayHopDongChiTietID]
           ,[TenNhanHang]
           ,[DmNhanHangID]
           ,[NgayThucHien]
           ,[LoaiDulieu] --1 input du lieu, 2 du lieu tinh thuc chay
           ,[LoaiVanDe] --loai van de loi
           ,[TenLoaiVanDe]
           ,[GhiChu]
           ,[CreatedAt]
           ,[CreatedBy])
	SELECT HopDongID, HopDongChiTietID, DmHinhThucQuangCaoID, DmSanPhamID
	, DmLoaiBannerID, TenSanPham, ThucChayHopDongChiTietID, TenNhanHang
	, DmNhanHangID, @NgayThucHien, 1 LoaiDuLieu, 2 LoaiVanDe, N'Ko có ID nhãn và Tên nhãn chưa có trên ABM' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'asd' CreatedBy
	FROM @Table_ThucChayHopDongChiTiet
	WHERE 1=1
	AND DmNhanHangID = 0
	AND ISNULL(TenNhanHang,'') <> ''
	AND  NOT (ISNULL(TenNhanHang,'') IN(SELECT TenNhanHang FROM [asd14].BRAND.dbo.DmNhanHang))


    --TH3:  ID ko đúng với tên
	INSERT INTO [dbo].[ThongTinCanhBaoNhanHang]
           ([HopDongID]
           ,[HopDongChiTietID]
           ,[DmHinhThucQuangCaoID]
           ,[DmSanPhamID]
           ,[DmLoaiBannerID]
           ,[TenSanPham]
           ,[ThucChayHopDongChiTietID]
           ,[TenNhanHang]
           ,[DmNhanHangID]
           ,[NgayThucHien]
           ,[LoaiDulieu] --1 input du lieu, 2 du lieu tinh thuc chay
           ,[LoaiVanDe] --loai van de loi
           ,[TenLoaiVanDe]
           ,[GhiChu]
           ,[CreatedAt]
           ,[CreatedBy])
	SELECT tchdct.HopDongID, tchdct.HopDongChiTietID, tchdct.DmHinhThucQuangCaoID, tchdct.DmSanPhamID
	, tchdct.DmLoaiBannerID, tchdct.TenSanPham, tchdct.ThucChayHopDongChiTietID, tchdct.TenNhanHang
	, tchdct.DmNhanHangID, @NgayThucHien, 1 LoaiDuLieu, 3 LoaiVanDe, N'ID ko đúng với tên' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'asd' CreatedBy
	FROM @Table_ThucChayHopDongChiTiet tchdct
	INNER JOIN [asd14].BRAND.dbo.DmNhanHang nh ON nh.DmNhanHangID =tchdct.DmNhanHangID
	WHERE ISNULL(tchdct.TenNhanHang,'') <> ''
	AND tchdct.DmNhanHangID <> 0
	AND tchdct.TenNhanHang <> nh.TenNhanHang

	--TH4:  ID nhãn đã bị chuẩn hóa về nhãn khác nhưng chưa cập nhật lại đúng
	INSERT INTO [dbo].[ThongTinCanhBaoNhanHang]
           ([HopDongID]
           ,[HopDongChiTietID]
           ,[DmHinhThucQuangCaoID]
           ,[DmSanPhamID]
           ,[DmLoaiBannerID]
           ,[TenSanPham]
           ,[ThucChayHopDongChiTietID]
           ,[TenNhanHang]
           ,[DmNhanHangID]
           ,[NgayThucHien]
           ,[LoaiDulieu] --1 input du lieu, 2 du lieu tinh thuc chay
           ,[LoaiVanDe] --loai van de loi
           ,[TenLoaiVanDe]
           ,[GhiChu]
           ,[CreatedAt]
           ,[CreatedBy])
	SELECT tchdct.HopDongID, tchdct.HopDongChiTietID, tchdct.DmHinhThucQuangCaoID, tchdct.DmSanPhamID
	, tchdct.DmLoaiBannerID, tchdct.TenSanPham, tchdct.ThucChayHopDongChiTietID, tchdct.TenNhanHang
	, tchdct.DmNhanHangID, @NgayThucHien, 1 LoaiDuLieu, 4 LoaiVanDe, N'ID nhãn đã bị chuẩn hóa về nhãn khác nhưng chưa cập nhật lại đúng' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'asd' CreatedBy
	FROM @Table_ThucChayHopDongChiTiet tchdct
	INNER JOIN [asd14].BRAND.dbo.DmNhanHang nh ON nh.DmNhanHangID =tchdct.DmNhanHangID
	WHERE ISNULL(tchdct.TenNhanHang,'') <> ''
	AND tchdct.DmNhanHangID <> 0
	AND tchdct.TenNhanHang <> nh.TenNhanHang
	AND nh.DeletedStatus = 1
	AND nh.RecordStatus = 1
	AND ISNULL(nh.DmNhanHangThayDoiID,0) <> 0

	--TH5:   Không có tên nhãn,không có ID nhãn
	INSERT INTO [dbo].[ThongTinCanhBaoNhanHang]
           ([HopDongID]
           ,[HopDongChiTietID]
           ,[DmHinhThucQuangCaoID]
           ,[DmSanPhamID]
           ,[DmLoaiBannerID]
           ,[TenSanPham]
           ,[ThucChayHopDongChiTietID]
           ,[TenNhanHang]
           ,[DmNhanHangID]
           ,[NgayThucHien]
           ,[LoaiDulieu] --1 input du lieu, 2 du lieu tinh thuc chay
           ,[LoaiVanDe] --loai van de loi
           ,[TenLoaiVanDe]
           ,[GhiChu]
           ,[CreatedAt]
           ,[CreatedBy])
	SELECT tchdct.HopDongID, tchdct.HopDongChiTietID, tchdct.DmHinhThucQuangCaoID, tchdct.DmSanPhamID
	, tchdct.DmLoaiBannerID, tchdct.TenSanPham, tchdct.ThucChayHopDongChiTietID, tchdct.TenNhanHang
	, tchdct.DmNhanHangID, @NgayThucHien, 1 LoaiDuLieu, 5 LoaiVanDe, N'Không có tên nhãn, không có ID nhãn' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'asd' CreatedBy
	FROM @Table_ThucChayHopDongChiTiet tchdct
	WHERE ISNULL(tchdct.TenNhanHang,'') = ''
	AND tchdct.DmNhanHangID = 0

	--TH6: Không có tên nhãn, có ID nhãn
	INSERT INTO [dbo].[ThongTinCanhBaoNhanHang]
           ([HopDongID]
           ,[HopDongChiTietID]
           ,[DmHinhThucQuangCaoID]
           ,[DmSanPhamID]
           ,[DmLoaiBannerID]
           ,[TenSanPham]
           ,[ThucChayHopDongChiTietID]
           ,[TenNhanHang]
           ,[DmNhanHangID]
           ,[NgayThucHien]
           ,[LoaiDulieu] --1 input du lieu, 2 du lieu tinh thuc chay
           ,[LoaiVanDe] --loai van de loi
           ,[TenLoaiVanDe]
           ,[GhiChu]
           ,[CreatedAt]
           ,[CreatedBy])
	SELECT tchdct.HopDongID, tchdct.HopDongChiTietID, tchdct.DmHinhThucQuangCaoID, tchdct.DmSanPhamID
	, tchdct.DmLoaiBannerID, tchdct.TenSanPham, tchdct.ThucChayHopDongChiTietID, tchdct.TenNhanHang
	, tchdct.DmNhanHangID, @NgayThucHien, 1 LoaiDuLieu, 6 LoaiVanDe, N'Không có tên nhãn, có ID nhãn' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'asd' CreatedBy
	FROM @Table_ThucChayHopDongChiTiet tchdct
	WHERE ISNULL(tchdct.TenNhanHang,'') = ''
	AND tchdct.DmNhanHangID <> 0


	SELECT * FROM [ThongTinCanhBaoNhanHang]
END

```
