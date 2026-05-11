# Stored Procedure: `ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-01-05 17:14:04.393000
- **Ngày sửa cuối**: 2020-05-18 14:45:01.257000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC  [dbo].[ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_BySoHopDong] '2019-01-04','QC8090918'	
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet_BySoHopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
	,@SoHopDong nvarchar(50)
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
			WHERE 1=1 AND TrangThaiTinhThucChay = 0
			AND CONVERT(DATE,tcmn.LastModifiedAt) = @NgayThucHien
			AND tcmn.TuNgay >= @NgayGioiHanTinh
			AND tcmn.DeletedStatus = 0
			AND tcmn.[status] in (2,4) --chi tinh khi trang thái là duyệt thực chạy hoặc duyệt thanh toán 20200514
		)tcmn
	
	)tcmn WHERE 1=1
	AND tcmn.HopDongChiTietREF NOT IN (SELECT  DISTINCT hopdongchiTietID FROM MuaNgoaiChot_TinhBoSung_2016)
and dbo.GetSoHopDongByID(HopDongREF) = @SoHopDong		
	OPEN pb_cursor
	
	FETCH NEXT FROM pb_cursor INTO @ThucChayMuaNgoaiChiTietID , @HopDongREF	, @HopDongChiTietREF 
	, @SoLuongThucChay , @DmDonViTinhREF , @ThanhTienThucChayBanSauCK 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT CONVERT(NVARCHAR(100),@ThucChayMuaNgoaiChiTietID)
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
		AND SoLuongDotChayBooking = @ThucChayMuaNgoaiChiTietID ORDER BY HopDongID))
		BEGIN
			--1. Tinh thanh tien lai thuc chay mua ngoai chot HAIDH 20200518
			--2. Update trang thai tinh thuc chay cua ThucChayMuaNgoaiChiTiet 
		    UPDATE dbo.ThucChayMuaNgoaiChiTiet
			SET TrangThaiTinhThucChay = 1
			WHERE ThucChayMuaNgoaiChiTietID = @ThucChayMuaNgoaiChiTietID
		END

		FETCH NEXT FROM pb_cursor INTO @ThucChayMuaNgoaiChiTietID , @HopDongREF	, @HopDongChiTietREF 
	, @SoLuongThucChay , @DmDonViTinhREF , @ThanhTienThucChayBanSauCK 
	END
	
	CLOSE pb_cursor
	DEALLOCATE pb_cursor
    
    SELECT 1
END

```
