# Stored Procedure: `ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_DEV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-18 17:15:41.607000
- **Ngày sửa cuối**: 2021-07-08 12:27:19.623000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC  [dbo].[ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_dev] '2021-07-06'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_DEV]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    DECLARE	@NgayGioiHanTinh	DATETIME = '2013-01-01'
			
    DECLARE @ThucChayMuaNgoaiChiTietID INT, @HopDongREF	INT, @HopDongChiTietREF INT
	, @SoLuongThucChay INT, @DmDonViTinhREF INT, @ThanhTienThucChayBanSauCK FLOAT,
	@DonViTinhThucChay NVARCHAR(50),@ghiChu NVARCHAR(512)

    
	DECLARE pb_cursor CURSOR FOR
	
	SELECT tcmn.ThucChayMuaNgoaiChiTietID, tcmn.HopDongREF, tcmn.HopDongChiTietREF, ISNULL(tcmn.SoLuongThucChay,0)SoLuongThucChay, tcmn.DmDonViTinhREF
		, ISNULL(tcmn.ThanhTienThucChayBanSauCK,0)ThanhTienThucChayBanSauCK
	FROM
	(
		SELECT tcmn.ThucChayMuaNgoaiChiTietID, tcmn.HopDongREF, tcmn.HopDongChiTietREF, tcmn.SoLuongThucChay, tcmn.DmDonViTinhREF
			, tcmn.ThanhTienThucChayBanSauCK 
		FROM
		(
			SELECT tcmn.ThucChayMuaNgoaiChiTietID, tcmn.HopDongREF, tcmn.HopDongChiTietREF, tcmn.SoLuongThucChay, tcmn.DmDonViTinhREF
			, tcmn.ThanhTienThucChayBanSauCK 
			FROM dbo.ThucChayMuaNgoaiChiTiet tcmn
			WHERE 1=1 
			--AND TrangThaiTinhThucChay = 0
			AND CONVERT(DATE,tcmn.LastModifiedAt) = @NgayThucHien
			AND tcmn.TuNgay >= @NgayGioiHanTinh
			AND tcmn.DeletedStatus = 0
			AND tcmn.[status] in (1,2,4) --chi tinh khi trang thái là duyệt thực chạy hoặc gửi duyệt thanh toán, duyệt thanh toán 20200514
		)tcmn
		INNER JOIN 
		(SELECT ct.HopDongFK, ct.HopDongChiTietID FROM dbo.HopDongChiTiet ct 
			WHERE ct.DeletedStatus = 0
			AND (ct.DmLoaiREF = 13 OR ct.DmLoaiBannerREF = 18)
		)hdct ON hdct.HopDongFK = tcmn.HopDongREF AND hdct.HopDongChiTietID = tcmn.HopDongChiTietREF
		INNER JOIN 
		(
			SELECT hd.SoHopDong, hd.HopDongID FROM dbo.HopDong hd
			WHERE hd.TrangThaiHopDong <> 3
			AND hd.DeletedStatus = 0
		)hd ON hd.HopDongID = hdct.HopDongFK
	
	)tcmn WHERE 1=1
	AND tcmn.HopDongChiTietREF NOT IN (SELECT  DISTINCT hopdongchiTietID FROM MuaNgoaiChot_TinhBoSung_2016)
	AND tcmn.HopDongChiTietREF = 626570
		
	OPEN pb_cursor
	
	FETCH NEXT FROM pb_cursor INTO @ThucChayMuaNgoaiChiTietID , @HopDongREF	, @HopDongChiTietREF 
	, @SoLuongThucChay , @DmDonViTinhREF , @ThanhTienThucChayBanSauCK 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--PRINT CONVERT(NVARCHAR(100),@ThucChayMuaNgoaiChiTietID)
		SET @DonViTinhThucChay = (SELECT TOP(1) TenDonViTinh FROM dbo.DmDonViTinh
									WHERE DmDonViTinhID = @DmDonViTinhREF
									AND DeletedStatus = 0
									ORDER BY DmDonViTinhID
								)
		SET @ghiChu = N'MUA NGOAI'
		

		EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_dev]
		@NgayThucHien						= @NgayThucHien,
		@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
		@HopDongREF							= @HopDongREF,
		@HopDongChiTietREF					= @HopDongChiTietREF,
		@SoLuongThucChay					= @SoLuongThucChay,
		@ThanhTienThucChayBanSauCK			= @ThanhTienThucChayBanSauCK,
		@DonViTinhThucChay					= @DonViTinhThucChay,
		@ghiChu								= @ghiChu
		
		--UPDATE TRANG THAI THUCCHAYMUANGOAICHI TIET DA TINH
		IF(EXISTS(SELECT TOP (1) HopDongID FROM dbo.ThucChayDaTinh WHERE HopDongID = @HopDongREF AND HopDongChiTietREF = @HopDongChiTietREF
		AND SoLuongDotChayBooking = @ThucChayMuaNgoaiChiTietID AND NgayThucHien = @NgayThucHien ORDER BY HopDongID))
		BEGIN
			--1. Tinh thanh tien lai thuc chay mua ngoai chot HAIDH 20200518
			SET @ghiChu = N'TINH THUC CHAY LAI MUA NGOAI'

			--EXEC [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLaiMuaNgoai]
			--@NgayThucHien						= @NgayThucHien,
			--@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
			--@HopDongREF							= @HopDongREF,
			--@HopDongChiTietREF					= @HopDongChiTietREF,
			--@DonViTinhThucChay					= @DonViTinhThucChay,
			--@ghiChu								= @ghiChu

			--2. Update trang thai tinh thuc chay cua ThucChayMuaNgoaiChiTiet 
		 --   UPDATE dbo.ThucChayMuaNgoaiChiTiet
			--SET TrangThaiTinhThucChay = 1
			--WHERE ThucChayMuaNgoaiChiTietID = @ThucChayMuaNgoaiChiTietID
		END

		FETCH NEXT FROM pb_cursor INTO @ThucChayMuaNgoaiChiTietID , @HopDongREF	, @HopDongChiTietREF 
	, @SoLuongThucChay , @DmDonViTinhREF , @ThanhTienThucChayBanSauCK 
	END
	
	CLOSE pb_cursor
	DEALLOCATE pb_cursor
    
    SELECT 1
END

```
