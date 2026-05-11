# Stored Procedure: `ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet_xulyDoiTruVaTinhLai_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-01-02 09:12:49.760000
- **Ngày sửa cuối**: 2026-01-02 09:17:03.480000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		haidh
-- Create date: 2015-01-13
-- Description:	Phuc vu viec xl thuc chay mua ngoai, doi tru va tinh lai khong chan gia tri vuot thanhtien phan bo
-- =============================================
/*
	EXEC  [dbo].[ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet_xulyDoiTruVaTinhLai_dev] 
	    @NgayThucHien = '2025-12-31',  -- datetime
    @HopDongChiTietREF = 769378  -- int
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet_xulyDoiTruVaTinhLai_dev]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
AS
BEGIN
	DECLARE @ThucChayMuaNgoaiChiTietID INT, @HopDongREF INT, @SoLuongThucChay INT, @DmDonViTinhREF INT
	, @ThanhTienThucChayBanSauCK FLOAT, @LastModifiedAt DATETIME, @DeletedStatus SMALLINT
	DECLARE @GhiChu NVARCHAR(MAX) ='', @ThanhTienThucChayMuaNgoaiSauCK_Bf FLOAT, @SoLuongThucChay_Bf BIGINT, @DonViTinhThucChay NVARCHAR(100)

	--CHECK THONG TIN PHAT SINH GIA TRI THAY DOI
	DECLARE MuaNgoai_Cursor CURSOR FOR

	SELECT DISTINCT A.ThucChayMuaNgoaiChiTietID, A.HopDongREF, A.HopDongChiTietREF, ISNULL(A.SoLuongThucChay,0)SoLuongThucChay, A.DmDonViTinhREF
	, ISNULL(A.ThanhTienThucChayBanSauCK,0)ThanhTienThucChayBanSauCK, A.LastModifiedAt, A.DeletedStatus 
	FROM
	(
		--DU TOAN THAY DOI - HOPDONGCHITIET_MUANGOAI - THAY DOI
		SELECT ThucChayMuaNgoaiChiTietID, HopDongREF, HopDongChiTietREF, SoLuongThucChay
		, DmDonViTinhREF, ThanhTienThucChayBanSauCK, LastModifiedAt, DeletedStatus 
		FROM dbo.ThucChayMuaNgoaiChiTiet
		WHERE 1=1 AND EXISTS(SELECT hdctm.HopDongChiTietID FROM dbo.HopDongChiTiet_MuaNgoai hdctm
			WHERE 1=1 AND hdctm.DeletedStatus = 0 
			AND hdctm.HopDongChiTietID = HopDongChiTietREF 
		)
		AND HopDongChiTietREF = @HopDongChiTietREF
		UNION
		--THUC CHAY MUA NGOAI THAY DOI
		SELECT ThucChayMuaNgoaiChiTietID, HopDongREF, HopDongChiTietREF, SoLuongThucChay
		, DmDonViTinhREF, ThanhTienThucChayBanSauCK, LastModifiedAt, DeletedStatus  
		FROM dbo.ThucChayMuaNgoaiChiTiet
		WHERE 1=1 AND HopDongChiTietREF = @HopDongChiTietREF
	)A

	OPEN MuaNgoai_Cursor
	
	FETCH NEXT FROM MuaNgoai_Cursor INTO @ThucChayMuaNgoaiChiTietID, @HopDongREF, @HopDongChiTietREF , @SoLuongThucChay , @DmDonViTinhREF 
	, @ThanhTienThucChayBanSauCK , @LastModifiedAt , @DeletedStatus 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @DonViTinhThucChay = (SELECT TOP (1) TenDonViTinh FROM dbo.DmDonViTinh  WHERE DmDonViTinhID = @DmDonViTinhREF)
		SET @GhiChu = N'DOI TRU MUA NGOAI, XU LY THUC CHAY: ' + CONVERT(NVARCHAR(100), @ThucChayMuaNgoaiChiTietID)
		print @HopDongChiTietREF
		print @GhiChu
		----TINH DOI TRU THUC CHAY
		--EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_DoiTruGiam]
		--@NgayThucHien						= @NgayThucHien,
		--@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
		--@HopDongREF							= @HopDongREF,
		--@HopDongChiTietREF					= @HopDongChiTietREF,
		--@ghiChu								= @GhiChu
		----THUC HIEN TINH LAI GIA TRI THAY DOI
		--SET @GhiChu =  N'TINH LAI, XU LY THUC CHAY: ' + CONVERT(NVARCHAR(100), @ThucChayMuaNgoaiChiTietID)
		--IF (@DeletedStatus <> 1)
		--BEGIN
		--	EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_ThayDoi]
		--	@NgayThucHien						= @NgayThucHien,
		--	@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
		--	@HopDongREF							= @HopDongREF,
		--	@HopDongChiTietREF					= @HopDongChiTietREF,
		--	@SoLuongThucChay					= @SoLuongThucChay,
		--	@ThanhTienThucChayBanSauCK			= @ThanhTienThucChayBanSauCK,
		--	@DonViTinhThucChay					= @DonViTinhThucChay,
		--	@ghiChu								= @GhiChu
		--END

		----UPDATE TRANG THAI DA TINH THUC CHAY MUA NGOAI
		--IF(EXISTS(SELECT TOP (1) HopDongID FROM dbo.ThucChayDaTinh 
		--	WHERE HopDongID = @HopDongREF AND HopDongChiTietREF = @HopDongChiTietREF
		--	AND SoLuongDotChayBooking = @ThucChayMuaNgoaiChiTietID ORDER BY HopDongID))
		--BEGIN
		--	UPDATE dbo.ThucChayMuaNgoaiChiTiet
		--	SET TrangThaiTinhThucChay = 1
		--	WHERE ThucChayMuaNgoaiChiTietID = @ThucChayMuaNgoaiChiTietID
		--END

		----2. CHECK VA TINH GIA TRI THAY DOI CHO LAI MUA NGOAI HAIDH 20200518
		--DECLARE @ThanhTienLaiThucChayMuaNgoai_bf float = 0, @ThanhTienLaiThucChayMuaNgoai float = 0
		--, @GhiChuGiamLai nvarchar(max) = N'Đỗi trừ giam lai mua ngoài, XU LY THUC CHAY: ' + Convert(nvarchar(50),@ThucChayMuaNgoaiChiTietID)
		--, @GhiChuTinhLai nvarchar(max) = N'Tính lại lãi mua ngoài, XU LY THUC CHAY: ' + Convert(nvarchar(50),@ThucChayMuaNgoaiChiTietID)

		----PRINT 'THUC HIEN DOI TRU GIAM THUC CHAY LAI MUA NGOAI ' + CONVERT(NVARCHAR(100), @ThucChayMuaNgoaiChiTietID)
		--EXEC [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLaiMuaNgoai_DoiTruGiam]
		--@NgayThucHien						= @NgayThucHien,
		--@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
		--@HopDongREF							= @HopDongREF,
		--@HopDongChiTietREF					= @HopDongChiTietREF,
		--@ghiChu								= @GhiChuGiamLai

		----PRINT 'THUC HIEN TINH LAI GIA TRI THUC CHAY LAI MUA NGOAI ' + CONVERT(NVARCHAR(100), @ThucChayMuaNgoaiChiTietID)
		--IF(@DeletedStatus <> 1)
		--BEGIN
		--	EXEC [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLaiMuaNgoai_ThayDoi]
		--	@NgayThucHien						= @NgayThucHien,
		--	@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
		--	@HopDongREF							= @HopDongREF,
		--	@HopDongChiTietREF					= @HopDongChiTietREF,
		--	@DonViTinhThucChay					= @DonViTinhThucChay,
		--	@ghiChu								= @GhiChuTinhLai
		--END

	FETCH NEXT FROM MuaNgoai_Cursor INTO @ThucChayMuaNgoaiChiTietID, @HopDongREF, @HopDongChiTietREF , @SoLuongThucChay , @DmDonViTinhREF 
	, @ThanhTienThucChayBanSauCK , @LastModifiedAt , @DeletedStatus  
	END
	
	CLOSE MuaNgoai_Cursor
	DEALLOCATE MuaNgoai_Cursor

END

```
