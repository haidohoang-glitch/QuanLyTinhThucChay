# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-04-21 14:41:17.823000
- **Ngày sửa cuối**: 2025-04-21 16:02:35.120000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--SELECT * FROM dbo.ThucChayDaTinh
--WHERE HopDongChiTietREF = 102434
--AND NgayThucHien = '2017-01-09'
--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_NhanHang] '2017-01-09'
CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @NgayBDCheck_Website DATETIME = '2025-04-22'
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	--1. TH1: TINH CHO TH CO PHAN BO haidh comment 2024-01-23
	create table #ThucChayDatinh_HopDong_NhanHang
	(
		[HopDongREF] [int] NULL,
		[HopDongChiTietREF] [int] NULL,
		[ThucChayHopDongChiTietID] int NULL,
		[DmNhanHangREF] [int] NULL,
		[DmWebsiteREF] [int] NULL,
		status_record [smallint]
	)
    -- Insert statements for procedure here
    declare 
	@HopDongID INT,
	@HopDongChiTietID INT,
	@ThucChayHopDongChiTietID INT,
	@SoHopDong_new NVARCHAR(50),
	@NgayDanhSo_new DATETIME,
	@DmNhanVienREF_new INT,
	@DmKhachHangREF_new NVARCHAR(200),
	@DmSanPhamREF_new INT,
	@DsNhanHangREF_new NVARCHAR(200),
	@HinhThucQuangCaoREF_new INT, @TenDangNhap_new NVARCHAR(50),
	@MaSoHopDong_new INT , @Note NVARCHAR(50), @IsThayDoi INT,@GiaTriThucChay FLOAT,@GiaTriThucChayAd FLOAT, @IsExistData INT ,@IsExistData1 INT  ;
	DECLARE @out NVARCHAR(2000);

	--
	INSERT INTO #ThucChayDatinh_HopDong_NhanHang
	SELECT DISTINCT tc.HopDongREF, 
	tc.HopDongChiTietREF, 
	Lg.ThucChayHopDongChiTietID, 
	tc.DmNhanHangREF ,
	tc.DmWebsiteREF,
	0 status_record
	FROM dbo.ThucChayHopDongChiTiet tc 
		INNER JOIN
		(
			SELECT * FROM
			(
				SELECT ROW_NUMBER() OVER (PARTITION BY ThucChayHopDongChiTietID ORDER By ThucChayHopDongChiTietID ASC ,ThoiGianLog ASC) as stt,
				ThucChayHopDongChiTietID, HopDongREF, HopDongChiTietREF, DmNhanHangREF, NhanHang, DmWebsiteREF, TenWebsite, ThoiGianLog
				FROM dbo.ThucChayHopDongChiTietLog
				WHERE CONVERT(DATE,ThoiGianLog) = @NgayThucHien
			)A
			WHERE a.stt =1
		)Lg ON tc.ThucChayHopDongChiTietID = Lg.ThucChayHopDongChiTietID 
		AND ((Lg.DmNhanHangREF <> tc.DmNhanHangREF) 
			OR ((Lg.DmWebsiteREF <> tc.DmWebsiteREF) AND ( CONVERT(DATE,ThoiGianLog) >= @NgayBDCheck_Website)) --HAIDH them dk check them website thay doi
			)
		INNER JOIN dbo.HopDong hd ON hd.HopDongID = tc.HopDongREF
		INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tc.HopDongChiTietREF
		WHERE (EXISTS(SELECT TOP (1) ch.ID  FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
											WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
											AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
											AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))  AND
			 NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF in (18))--Khong tinh thuc chay cho HTQC Mua Ngoai	
						AND NOT (hdct.DmViTriREF in (100093,100478))	--banner của GGFB,774 --banner của GGFB 28/02/2021
						AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) ) --haidh comment 20211026 TikTok tinh theo pp GGFB
						AND hdct.GhiChu <> N'HDBAN_INVENTORY'
						AND NOT (hdct.DmLoaiREF IN (26,5010,5000) ) --Haidh comment 23/09/2022 Loai ThangduGP cua ben Performance Base
			AND YEAR(hd.NgayDanhSoHopDong) >= YEAR(GETDATE()) - 2 --2017-03-15 HAIDH COMMENT KHONG TINH GIA TRI THAY DOI SAU 2 NAM SO VOI NAM HIEN TAI
			--AND tc.HopDongChiTietREF = 102434

	--- Update nhan hang bởi thực chạy hd chi tiết
	DECLARE @NhanHangMoi NVARCHAR(500),@HDID INT, @PhanBoID INT , @websiteref_new int
	DECLARE cursor_hdct CURSOR FOR  

		select [HopDongREF], [HopDongChiTietREF], [ThucChayHopDongChiTietID], [DmNhanHangREF]  , [DmWebsiteREF]
		FROM #ThucChayDatinh_HopDong_NhanHang

		OPEN cursor_hdct   	
	FETCH NEXT FROM cursor_hdct INTO @HDID, @PhanBoID, @ThucChayHopDongChiTietID, @NhanHangMoi, @websiteref_new

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		--CHECK NEU TON TAI PHAN BO DA GHI NHAN THAY DOI NHAN THI THOI --haidh comment 2024-01-23
		IF(NOT EXISTS(SELECT TOP 1 @PhanBoID FROM #ThucChayDatinh_HopDong_NhanHang 	
			WHERE [HopDongREF] = @HDID
			AND [HopDongChiTietREF] = @PhanBoID
			AND [DmNhanHangREF] = @NhanHangMoi	
			AND [ThucChayHopDongChiTietID] = @ThucChayHopDongChiTietID
			AND [DmWebsiteREF] = @websiteref_new
			AND status_record = 1))
		BEGIN
			--THUC HIEN XL THUC TREO THAY DOI (NHANHANG \ WEBSITE)
			--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang] @NgayThucHien ,@HDID ,@PhanBoID , @ThucChayHopDongChiTietID

			EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi] @NgayThucHien ,@HDID ,@PhanBoID , @ThucChayHopDongChiTietID

			--Update trang thai da cap nhap haidh comment 2024-01-23
			UPDATE #ThucChayDatinh_HopDong_NhanHang
			SET status_record = 1
			WHERE [HopDongREF] = @HDID
			AND [HopDongChiTietREF] = @PhanBoID
			AND [ThucChayHopDongChiTietID] = @ThucChayHopDongChiTietID
			AND [DmNhanHangREF] = @NhanHangMoi
			AND [DmWebsiteREF] = @websiteref_new
		END
		FETCH NEXT FROM cursor_hdct INTO @HDID, @PhanBoID, @ThucChayHopDongChiTietID, @NhanHangMoi, @websiteref_new 
	END   

	CLOSE cursor_hdct   
	DEALLOCATE cursor_hdct

	drop table #ThucChayDatinh_HopDong_NhanHang;
	
END



```
