# Stored Procedure: `ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-17 11:45:01.457000
- **Ngày sửa cuối**: 2018-05-24 15:46:30.507000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC  [dbo].[ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet_ByHopDongChiTiet] '2018-05-10',777777
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet_ByHopDongChiTiet]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongChiTietID INT
AS
BEGIN
	DECLARE @ThucChayMuaNgoaiChiTietID INT, @HopDongREF INT, @HopDongChiTietREF int, @SoLuongThucChay INT, @DmDonViTinhREF INT
	, @ThanhTienThucChayBanSauCK FLOAT, @LastModifiedAt DATETIME, @DeletedStatus SMALLINT
	DECLARE @GhiChu NVARCHAR(MAX) ='', @ThanhTienThucChayMuaNgoaiSauCK_Bf FLOAT, @SoLuongThucChay_Bf BIGINT, @DonViTinhThucChay NVARCHAR(100)

	--THUC HIEN DOI TRU GIAM TOAN BO HOPDONGCHITIET
	SET @GhiChu = 'MUA NGOAI - DO TRU GIAM TOAN BO HOPDONGCHITIET '
	EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_DoiTruGiam_ByHopDongChiTiet]
	@NgayThucHien						= @NgayThucHien,
	@HopDongChiTietREF					= @HopDongChiTietID,
	@ghiChu								= @GhiChu

	--THUC HIEN TINH LAI THUC CHAY
	DECLARE MuaNgoai_Cursor CURSOR FOR

	SELECT DISTINCT A.ThucChayMuaNgoaiChiTietID, A.HopDongREF, A.HopDongChiTietREF, ISNULL(A.SoLuongThucChay,0)SoLuongThucChay, A.DmDonViTinhREF
	, ISNULL(A.ThanhTienThucChayBanSauCK,0)ThanhTienThucChayBanSauCK, A.LastModifiedAt, A.DeletedStatus 
	FROM
	(
	
		SELECT ThucChayMuaNgoaiChiTietID, HopDongREF, HopDongChiTietREF, SoLuongThucChay
		, DmDonViTinhREF, ThanhTienThucChayBanSauCK, LastModifiedAt, DeletedStatus  
		FROM dbo.ThucChayMuaNgoaiChiTiet
		WHERE 1=1 AND HopDongChiTietREF = @HopDongChiTietID
		AND DeletedStatus = 0
	)A

	OPEN MuaNgoai_Cursor
	
	FETCH NEXT FROM MuaNgoai_Cursor INTO @ThucChayMuaNgoaiChiTietID, @HopDongREF, @HopDongChiTietREF , @SoLuongThucChay , @DmDonViTinhREF 
	, @ThanhTienThucChayBanSauCK , @LastModifiedAt , @DeletedStatus 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT CONVERT(NVARCHAR(100),@ThucChayMuaNgoaiChiTietID)

		SET @DonViTinhThucChay = (SELECT TOP (1) TenDonViTinh FROM dbo.DmDonViTinh
									WHERE DmDonViTinhID = @DmDonViTinhREF
									ORDER BY DmDonViTinhID)
		--THUC HIEN TINH LAI GIA TRI THAY DOI
		SET @GhiChu =  N'MUA NGOAI - TINH LAI TOAN BO HOPDONGCHITIET'

		EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_ThayDoi]
		@NgayThucHien						= @NgayThucHien,
		@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
		@HopDongREF							= @HopDongREF,
		@HopDongChiTietREF					= @HopDongChiTietREF,
		@SoLuongThucChay					= @SoLuongThucChay,
		@ThanhTienThucChayBanSauCK			= @ThanhTienThucChayBanSauCK,
		@DonViTinhThucChay					= @DonViTinhThucChay,
		@ghiChu								= @GhiChu

		--CAP NHAT TRANG THAI TINH THUC CHAY
		IF(EXISTS(SELECT * FROM dbo.ThucChayDaTinh
		WHERE HopDongID = @HopDongREF
		AND HopDongChiTietREF = @HopDongChiTietREF
		AND SoLuongDotChayBooking = @ThucChayMuaNgoaiChiTietID
		AND NgayThucHien = @NgayThucHien)
		)
		BEGIN
		    UPDATE dbo.ThucChayMuaNgoaiChiTiet
			SET TrangThaiTinhThucChay = 1
			WHERE ThucChayMuaNgoaiChiTietID = @ThucChayMuaNgoaiChiTietID
			AND HopDongREF = @HopDongREF
			AND HopDongChiTietREF = @HopDongChiTietID
		END
	FETCH NEXT FROM MuaNgoai_Cursor INTO @ThucChayMuaNgoaiChiTietID, @HopDongREF, @HopDongChiTietREF , @SoLuongThucChay , @DmDonViTinhREF 
	, @ThanhTienThucChayBanSauCK , @LastModifiedAt , @DeletedStatus  
	END
	
	CLOSE MuaNgoai_Cursor
	DEALLOCATE MuaNgoai_Cursor

END

```
