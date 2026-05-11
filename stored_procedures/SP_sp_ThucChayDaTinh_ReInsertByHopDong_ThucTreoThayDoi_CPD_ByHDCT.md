# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_CPD_ByHDCT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-12-18 11:41:04.053000
- **Ngày sửa cuối**: 2025-12-18 11:44:27.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_CPD_ByHDCT] '2025-12-17'

CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_CPD_ByHDCT]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
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

	--1. TH1: TINH CHO TH CO PHAN BO haidh comment 2024-01-23
	create table #ThucChayDatinh_HopDong_ThucTreoNhanHang
	(
		[HopDongREF] [int] NULL,
		[HopDongChiTietREF] [int] NULL,
		[DmNhanHangREF] [int] NULL,
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
				--WHERE CONVERT(DATE,ThoiGianLog) = @NgayThucHien
			)A
			WHERE a.stt =1
		)Lg ON tc.ThucChayHopDongChiTietID = Lg.ThucChayHopDongChiTietID 
		AND ((Lg.DmNhanHangREF <> tc.DmNhanHangREF) 
			--OR ((Lg.DmWebsiteREF <> tc.DmWebsiteREF) AND ( CONVERT(DATE,ThoiGianLog) >= @NgayBDCheck_Website)) --HAIDH them dk check them website thay doi
			)
		INNER JOIN dbo.HopDong hd ON hd.HopDongID = tc.HopDongREF
		INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tc.HopDongChiTietREF
		WHERE 1=1 AND hdct.DmSanPhamREF IN (140,228,564,549,5082) 
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1 --Đơn vị của hình thức CPD 
			AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF IN (17,18))
			AND YEAR(hd.NgayDanhSoHopDong) >= YEAR(GETDATE()) - 2 --2017-03-15 HAIDH COMMENT KHONG TINH GIA TRI THAY DOI SAU 2 NAM SO VOI NAM HIEN TAI
			AND tc.HopDongChiTietREF = @HopDongChiTietREF

	----- Update nhan hang bởi thực chạy hd chi tiết

	;WITH FirstNhanHang AS (
		SELECT 
			[HopDongREF],
			[HopDongChiTietREF],
			[DmNhanHangREF],
			-- Đánh số thứ tự cho từng nhóm, bản ghi có Id nhỏ nhất sẽ là số 1
			ROW_NUMBER() OVER (
				PARTITION BY HopDongREF, HopDongChiTietREF 
				ORDER BY [ThucChayHopDongChiTietID] ASC
			) AS RowNum
		FROM #ThucChayDatinh_HopDong_NhanHang
		WHERE [DmNhanHangREF] IS NOT NULL AND [DmNhanHangREF] <> 0 -- Loại bỏ các dòng trắng
	)

	insert into #ThucChayDatinh_HopDong_ThucTreoNhanHang
	SELECT 
		[HopDongREF],
		[HopDongChiTietREF],
		[DmNhanHangREF] AS NhanHangDauTien
	FROM FirstNhanHang
	WHERE RowNum = 1; -- Chỉ lấy bản ghi đầu tiên của mỗi cặp Hợp đồng - Phân bổ

	DECLARE @NhanHangMoi INT,@HDID INT, @PhanBoID INT , @websiteref_new int
	DECLARE cursor_hdct CURSOR FOR  

		select [HopDongREF], [HopDongChiTietREF],  [DmNhanHangREF]  
		FROM #ThucChayDatinh_HopDong_ThucTreoNhanHang

		OPEN cursor_hdct   	
	FETCH NEXT FROM cursor_hdct INTO @HDID, @PhanBoID, @NhanHangMoi

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
			print @PhanBoID
			EXEC  [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_CPD]
			-- Add the parameters for the stored procedure here
			@NgayThucHien = @NgayThucHien,
			@HopDongID = @HDID,
			@PhanBoID = @PhanBoID,
			@NhanHangMoi = @NhanHangMoi
		FETCH NEXT FROM cursor_hdct INTO @HDID, @PhanBoID, @NhanHangMoi
	END   

	CLOSE cursor_hdct   
	DEALLOCATE cursor_hdct

	DROP TABLE #ThucChayDatinh_HopDong_NhanHang;
	DROP TABLE #ThucChayDatinh_HopDong_ThucTreoNhanHang;
	
END



```
