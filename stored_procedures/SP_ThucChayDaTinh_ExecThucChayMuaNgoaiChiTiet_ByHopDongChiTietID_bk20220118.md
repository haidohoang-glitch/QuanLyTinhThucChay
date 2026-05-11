# Stored Procedure: `ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_ByHopDongChiTietID_bk20220118`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-01-18 15:58:38.507000
- **Ngày sửa cuối**: 2022-01-18 15:58:38.507000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC  [dbo].[ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_ByHopDongChiTietID] 583782 , '2020-05-29'
*/
create PROCEDURE [dbo].[ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_ByHopDongChiTietID_bk20220118]
	-- Add the parameters for the stored procedure here
	@HopDongChiTietREF int,
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    DECLARE	@NgayGioiHanTinh	DATETIME = '2013-01-01'
			
    DECLARE @ThucChayMuaNgoaiChiTietID INT, @HopDongREF	INT
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
	
	)tcmn WHERE 1=1
	AND tcmn.HopDongChiTietREF NOT IN (SELECT  DISTINCT hopdongchiTietID FROM MuaNgoaiChot_TinhBoSung_2016)
	AND tcmn.HopDongChiTietREF =@HopDongChiTietREF 
		
	OPEN pb_cursor
	
	FETCH NEXT FROM pb_cursor INTO @ThucChayMuaNgoaiChiTietID , @HopDongREF	, @HopDongChiTietREF 
	, @SoLuongThucChay , @DmDonViTinhREF , @ThanhTienThucChayBanSauCK 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		DECLARE @ThanhTienPhanBo FLOAT = 0, @TongThanhTienThucChay FLOAT = 0, @ChietKhau FLOAT = 0
		SET @ChietKhau = (SELECT Top (1) hdct.ChietKhau FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietREF ORDER BY hdct.HopDongChiTietID)
		--PRINT CONVERT(NVARCHAR(100),@ThucChayMuaNgoaiChiTietID)
		--TH PHAN BO KHONG PHAI LA KM HAIDH COMMENT 20211015
		IF(@ChietKhau <> 100)
		BEGIN
			SET @ThanhTienPhanBo = ISNULL((SELECT Top (1) hdct.ThanhTien FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietREF ORDER BY hdct.HopDongChiTietID),0)
			SET @TongThanhTienThucChay = ISNULL((SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) FROM dbo.ThucChayDaTinh tcdt WHERE tcdt.HopDongChiTietREF = @HopDongChiTietREF),0)
			--CHECK NEU VUOT GIA TRI PHAN BO THI KHONG THUC HIEN TINH --HAIDH COMMNET THEO YEU CAU Feature #11028 NGAY 20211015
			IF(@TongThanhTienThucChay + @ThanhTienThucChayBanSauCK > @ThanhTienPhanBo)
				SET @ThanhTienThucChayBanSauCK = 0 --SET @ThanhTienThucChayBanSauCK = 0 DE KHONG TINH THUC CHAY
		END
		--TH PHAN BO LA KHUYEN MAI HAIDH COMMENT 20211015
		ELSE
		BEGIN
			SET @ThanhTienPhanBo = ISNULL((SELECT Top (1) hdct.DonGia*hdct.SoLuong FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietREF ORDER BY hdct.HopDongChiTietID),0)
			SET @TongThanhTienThucChay = ISNULL((SELECT SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) FROM dbo.ThucChayDaTinh tcdt WHERE tcdt.HopDongChiTietREF = @HopDongChiTietREF),0)
			IF(@TongThanhTienThucChay + @ThanhTienThucChayBanSauCK > @ThanhTienPhanBo)
				SET @ThanhTienThucChayBanSauCK = 0 --SET @ThanhTienThucChayBanSauCK = 0 DE KHONG TINH THUC CHAY
		END
		--HAIDH COMMENT 20211015
		
		IF(@ThanhTienThucChayBanSauCK <> 0)
		BEGIN
			--PRINT CONVERT(NVARCHAR(100),@ThucChayMuaNgoaiChiTietID)
			SET @DonViTinhThucChay = (SELECT TOP(1) TenDonViTinh FROM dbo.DmDonViTinh
										WHERE DmDonViTinhID = @DmDonViTinhREF
										AND DeletedStatus = 0
										ORDER BY DmDonViTinhID
									)
			SET @ghiChu = N'MUA NGOAI'

			EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet]
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
				print 'Vao tinh lai'
				EXEC [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLaiMuaNgoai]
				@NgayThucHien						= @NgayThucHien,
				@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
				@HopDongREF							= @HopDongREF,
				@HopDongChiTietREF					= @HopDongChiTietREF,
				@DonViTinhThucChay					= @DonViTinhThucChay,
				@ghiChu								= @ghiChu

				--2. Update trang thai tinh thuc chay cua ThucChayMuaNgoaiChiTiet 
				UPDATE dbo.ThucChayMuaNgoaiChiTiet
				SET TrangThaiTinhThucChay = 1
				WHERE ThucChayMuaNgoaiChiTietID = @ThucChayMuaNgoaiChiTietID
			END
		END
		FETCH NEXT FROM pb_cursor INTO @ThucChayMuaNgoaiChiTietID , @HopDongREF	, @HopDongChiTietREF 
	, @SoLuongThucChay , @DmDonViTinhREF , @ThanhTienThucChayBanSauCK 
	END
	
	CLOSE pb_cursor
	DEALLOCATE pb_cursor
    
    SELECT 1
END

```
