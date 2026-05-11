# Stored Procedure: `Insert_Notify_warning_brand_input_contractdetails`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-03 10:20:18.783000
- **Ngày sửa cuối**: 2020-06-08 09:16:22.977000

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
EXEC [dbo].[Insert_Notify_warning_brand_input_contractdetails]	'2016-10-31'
*/
CREATE PROCEDURE [dbo].[Insert_Notify_warning_brand_input_contractdetails]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Table_NhanHangHopDongChiTiet TABLE(HopDongID INT, HopDongChiTietID INT, DmHinhThucQuangCaoID INT
	, DmSanPhamID INT, DmLoaiBannerID INT, TenSanPham NVARCHAR(200), TenNhanHang NVARCHAR(500), DmNhanHangID INT)

	DECLARE @table_HopDongChiTiet TABLE(HopDongID INT, HopDongChiTietID INT,DmHinhThucQuangCaoID INT, DmSanPhamID INT
	, DmLoaiBannerID INT, TenSanPham NVARCHAR(200) , TenNhanHang NVARCHAR(1000), DmNhanHangID INT, DanhSachNhanHangID NVARCHAR(200))

	DECLARE @table_HopDongChiTietTenNhanHang TABLE(HopDongChiTietID INT, DanhSachNhanHangID NVARCHAR(200), TenNhanHang NVARCHAR(500), DanhSachTenNhanHang NVARCHAR(2000))

	DELETE FROM [dbo].[ThongTinCanhBaoNhanHang]
	WHERE LoaiDulieu = 1 --dulieu input
	AND LoaiVanDe IN (7,8)
	AND NgayThucHien = @NgayThucHien


	----***********CHECK THONG TIN DAU VAO************-----------------
	----0. CO DU LIEU DONG BO NGAY THUC HIEN
	------2. DANH SACH CAC SAN PHAM CHAY CO NHAN TINH THEO HOP DONG CHI TIET
	
	INSERT INTO @table_HopDongChiTiet
	SELECT A.HopDongFK, A.HopDongChiTietID, A.DmLoaiREF,A.DmSanPhamREF,A.DmLoaiBannerREF, A.TenSanPham, A.NhanHang 
	,CONVERT(INT,B.items) DmNhanHangChiTietREF
	, A.DmNhanHangREF
	FROM (SELECT a.* FROM
			(
				SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DmLoaiREF, hdct.DmLoaiBannerREF
				, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.NhanHang,hdct.DanhSachNhanHangREF DmNhanHangREF
				FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				WHERE hdct.DeletedStatus = 0
				AND hd.TrangThaiHopDong <> 3
				AND (
						(hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18) ---- KHONG PHAI LA MUA NGOAI
						OR (hdct.DonViTinhREF = 19)	----DON VI TINH LA CPA
						OR hdct.DmSanPhamREF NOT IN (242,240, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542, 555, 556, 557 , 558, 559, 560, 561, 635
								, 563,631,613, 651,630,140,228,549,564,231,238, 531, 370, 339,342, 385, 598, 680, 141, 144,628,585,637,560,144,726,731)
					)
				AND CONVERT(DATE,hdct.LastModifiedAt) = @NgayThuchien
				AND hd.DmMaHopDongREF NOT IN (693)
			)a
	) A
	OUTER APPLY
	(
		SELECT * FROM dbo.Split(A.DmNhanHangREF,',')
						
	) B

	

	----TH1: Ko có ID nhãn nhưng Tên nhãn đã có trên ABM : LoaiVanDe = 1, tren HopDongChiTiet
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

	SELECT DISTINCT tchdct.HopDongID, tchdct.HopDongChiTietID, tchdct.DmHinhThucQuangCaoID, tchdct.DmSanPhamID
	, tchdct.DmLoaiBannerID, tchdct.TenSanPham, 0 ThucChayHopDongChiTietID, tchdct.TenNhanHang
	, 0 DmNhanHangID, @NgayThucHien, 1 LoaiDuLieu, 7 LoaiVanDe, N'Ko có ID nhãn trên hợp đồng chi tiết nhưng Tên nhãn đã có trên ABM' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'asd' CreatedBy
	FROM @table_HopDongChiTiet tchdct
	WHERE ISNULL(tchdct.TenNhanHang,'') <> ''
	AND (ISNULL(tchdct.DanhSachNhanHangID,'0') = 0 OR ISNULL(tchdct.DanhSachNhanHangID,'') = '')

	
	--TH2: Ko có ID nhãn & Tên nhãn chưa có trên ABM


	--TH3: ID ko đúng với tên


	--TH4: ID nhãn đã bị chuẩn hóa về nhãn khác nhưng chưa cập nhật lại đúng
	--TH5: Không có tên nhãn, ko có ID nhãn
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

	SELECT DISTINCT tchdct.HopDongID, tchdct.HopDongChiTietID, tchdct.DmHinhThucQuangCaoID, tchdct.DmSanPhamID
	, tchdct.DmLoaiBannerID, tchdct.TenSanPham, 0 ThucChayHopDongChiTietID, tchdct.TenNhanHang
	, 0 DmNhanHangID, @NgayThucHien, 1 LoaiDuLieu, 8 LoaiVanDe, N'Không có tên nhãn, có ID nhãn trên hợp đồng chi tiết' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'asd' CreatedBy
	FROM @table_HopDongChiTiet tchdct
	WHERE ISNULL(tchdct.TenNhanHang,'') = ''
	AND (ISNULL(tchdct.DanhSachNhanHangID,'0') <> '0' OR ISNULL(tchdct.DanhSachNhanHangID,'') <> '')

END

```
