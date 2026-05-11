# Stored Procedure: `Notify_warning_brand_calc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-03 17:14:25.790000
- **Ngày sửa cuối**: 2021-03-22 14:54:12.670000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[Notify_warning_brand_calc]	'2018-08-29'
*/
CREATE PROCEDURE [dbo].[Notify_warning_brand_calc]
	@NgayChay DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @NgayChay
	DECLARE @table_thucchaydatinh TABLE(HopDongID INT, HopDongChiTietID INT, DmSanPhamID INT, DsNhanHangID NVARCHAR(200), ThucChay BIGINT)
	
	DECLARE @Table_ThucChayThuctreoNhan TABLE(HopDongID INT,HopDongChiTietID INT, DmNhanHangID int)

	DECLARE @Table_ThucChayHopDongNhan TABLE(HopDongID INT, HopDongChiTietID INT, DmNhanNhangID INT, DsNhanHangID NVARCHAR(300))
	----KHOI TAO THONG TIN GIA TRI CAN CHECK
	INSERT INTO @table_thucchaydatinh
	        ( HopDongID ,
	          HopDongChiTietID ,
	          DmSanPhamID ,
	          DsNhanHangID,
			  ThucChay
	        )
	SELECT * FROM
	(
		SELECT HopDongID, HopDongChiTietREF, DmSanPhamREF, NhanHang 
		, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThucChay
		FROM dbo.ThucChayDaTinh
		WHERE NgayThucHien <= @NgayThucHien
		AND HopDongChiTietREF IN 
			(
				SELECT DISTINCT HopDongChiTietREF FROM dbo.ThucChayDaTinh
				WHERE NgayThucHien = @NgayThucHien
				AND HopDongChiTietREF <> 0
				
			)
		GROUP BY HopDongID, HopDongChiTietREF, DmSanPhamREF, NhanHang 
	)TCDT
	WHERE ROUND(TCDT.ThucChay,0) <> 0

	------************XAC DINH DANH SACH NHAN TINH THUC CHAY HANG NGAY THUOC DANH SACH NHAN THUC TREO*******-------
	----1. XAC DINH DANH SACH CAC HOP DONG CHI TIET UNG VOI NHAN HANG CHAY DUOC TINH TRONG NGAY (TONGTHUCCHAY THEO HOPDONGCHITIET <> 0)
	INSERT INTO @Table_ThucChayThuctreoNhan
	SELECT DISTINCT HopDongFK  ,
	HopDongChiTietID ,CONVERT(INT,B.items) DmNhanHangChiTietREF
	FROM (SELECT a.* FROM
			(
				SELECT hdct.HopDongFK, tc.HopDongChiTietID, tc.DsNhanHangID  DmNhanHangREF
				FROM @table_thucchaydatinh tc
				INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tc.HopDongChiTietID
				WHERE 1=1
				AND NOT(hdct.DmLoaiREF IN (13,42) OR hdct.DmLoaiBannerREF =18) ---- KHONG PHAI LA MUA NGOAI
				AND NOT(hdct.DonViTinhREF = 19)	----DON VI TINH LA CPA
				AND hdct.HopDongFK NOT IN (SELECT DISTINCT HopDongREF FROM dbo.DmThongTinHopDongBanInventory)
				AND hdct.DmSanPhamREF IN (242,240, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542, 555, 556, 557 , 558, 559, 560, 561, 635
							, 563,631,613, 651,630,140,228,549,564,231,238, 531, 370, 339,342, 385, 598, 680,726,731,734,729)
			)a
	) A
	OUTER APPLY
	(
		SELECT * FROM dbo.Split(A.DmNhanHangREF,',')
						
	) B

	--2. KIEM TRA DANH SACH NHAN HANG UNG VOI HOPDONGCHITIET DO CO NAM TRONG DANH SACH NHAN TREO
	INSERT INTO [dbo].[ThongTinCanhBaoNhanHangHopDongChiTiet]
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
        ,[LoaiDulieu]
        ,[LoaiVanDe]
        ,[TenLoaiVanDe]
        ,[GhiChu]
        ,[CreatedAt]
        ,[CreatedBy])
	
	SELECT a.HopDongID, a.HopDongChiTietID,hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmLoaiBannerREF,hdct.TenSanPham
	, 0 ThucChayHopDongChiTietID, ISNULL(nh.TenNhanHang,'') TenNhanHang, A.DmNhanHangID 
	, @NgayThucHien, 1 LoaiDuLieu, 1 LoaiVanDe, N'Nhãn hàng thực chạy đã tinh không có trên ThucChayHopDongChiTiet' TenLoaiVanDe
	, '' GhiChu, GETDATE() CreatedAt, 'ASD' CreatedBy
	FROM
	(
		SELECT TC.HopDongID, tc.HopDongChiTietID, tc.DmNhanHangID, ISNULL(tchdct.HopDongChiTietREF,0)HopDongChiTietREF
		, ISNULL(tchdct.DmNhanHangREF,0)DmNhanHangREF
		FROM @Table_ThucChayThuctreoNhan tc
		LEFT JOIN (
				SELECT * FROM dbo.ThucChayHopDongChiTiet t	WHERE t.DeletedStatus = 0
			) tchdct ON tc.HopDongChiTietID = tchdct.HopDongChiTietREF
		AND CONVERT(NVARCHAR(50),tc.DmNhanHangID) = tchdct.DmNhanHangREF
	)A
	INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietID = hdct.HopDongChiTietID
	LEFT JOIN [asd14].BRAND.dbo.DmNhanHang nh ON nh.DmNhanHangID = A.DmNhanHangID
	WHERE 1=1 --AND A.HopDongChiTietREF <> 0 
	AND A.DmNhanHangREF = 0
	----*NOTE: VOI SANPHAM: DANGTIN VA TUYENBAI THI CHUA CHECK

	----************XAC DINH DANH SACH NHAN TINH THUC CHAY HANG NGAY THUOC DANH SACH NHAN HOPDONGCHITIET*******-------
	--1. XAC DINH DANH SACH CAC HOP DONG CHI TIET UNG VOI NHAN HANG CHAY DUOC TINH TRONG NGAY (TONGTHUCCHAY THEO HOPDONGCHITIET <> 0)
	INSERT INTO @Table_ThucChayHopDongNhan
	        ( HopDongID ,
	          HopDongChiTietID ,
	          DmNhanNhangID,
			  DsNhanHangID
	        )
	SELECT DISTINCT HopDongFK  ,
	HopDongChiTietID ,CONVERT(INT,B.items) DmNhanHangChiTietREF
	, DanhSachNhanHangREF
	FROM (SELECT a.* FROM
			(
				SELECT hdct.HopDongFK, tc.HopDongChiTietID, tc.DsNhanHangID  DmNhanHangREF
				, hdct.DanhSachNhanHangREF
				FROM @table_thucchaydatinh tc
				INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tc.HopDongChiTietID
				WHERE 1=1 
				AND NOT (hdct.DmSanPhamREF in (306,423) or hdct.DmViTriREF in (100093,100478)) -- tuyetnta bo sung ngay 22/03/2021, loại sp GGFB
				AND (
						 (hdct.DmLoaiREF in (13,42) OR hdct.DmLoaiBannerREF =18) ---- KHONG PHAI LA MUA NGOAI
						OR (hdct.DonViTinhREF = 19)	----DON VI TINH LA CPA
						OR hdct.DmSanPhamREF NOT IN (242,240, 251, 252, 253, 535, 537, 538, 539, 540, 541, 542, 555, 556, 557 , 558, 559, 560, 561, 635
								, 563,631,613, 651,630,140,228,549,564,231,238, 531, 370, 339,342, 385, 598, 680, 141, 144,628,585,637,560,144,726,731,734,729)
					)
			)a
	) A
	OUTER APPLY
	(
		SELECT * FROM dbo.Split(A.DmNhanHangREF,',')
						
	) B
	----HAIDH CHECK LAI CHO NAY ?????????????????
	----2. KIEM TRA DANH SACH NHAN HANG UNG VOI HOPDONGCHITIET DO CO NAM TRONG DANH SACH NHAN TREN HOPDONGCHITIET
	--INSERT INTO [dbo].[ThongTinCanhBaoNhanHangHopDongChiTiet]
 --          ([HopDongID]
 --          ,[HopDongChiTietID]
 --          ,[DmHinhThucQuangCaoID]
 --          ,[DmSanPhamID]
 --          ,[DmLoaiBannerID]
 --          ,[TenSanPham]
 --          ,[ThucChayHopDongChiTietID]
 --          ,[TenNhanHang]
 --          ,[DmNhanHangID]
 --          ,[NgayThucHien]
 --          ,[LoaiDulieu]
 --          ,[LoaiVanDe]
 --          ,[TenLoaiVanDe]
 --          ,[GhiChu]
 --          ,[CreatedAt]
 --          ,[CreatedBy])
     
	--SELECT tc.HopDongID, tc.HopDongChiTietID, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmLoaiBannerREF,hdct.TenSanPham
	--, 0 ThucChayHopDongChiTietID, nh.TenNhanHang , tc.DmNhanNhangID
	--, @NgayThucHien, 1 LoaiDuLieu, 2 LoaiVanDe, N'Nhãn hàng thực chạy đã tinh không có trên hopdongchitiet' TenLoaiVanDe
	--, '' GhiChu, GETDATE() CreatedAt, 'ASD' CreatedBy
	--FROM @Table_ThucChayHopDongNhan tc
	--INNER JOIN dbo.HopDongChiTiet hdct ON tc.HopDongChiTietID = hdct.HopDongChiTietID
	--INNER JOIN [asd14].BRAND.dbo.DmNhanHang nh ON nh.DmNhanHangID = tc.DmNhanNhangID
	--WHERE tc.DmNhanNhangID NOT IN (SELECT CONVERT(INT,items)DmNhanHangID FROM dbo.Split(tc.DsNhanHangID,','))

	--SELECT * FROM dbo.[ThongTinCanhBaoNhanHangHopDongChiTiet] where ngaythuchien = '2021-03-21'
END

```
