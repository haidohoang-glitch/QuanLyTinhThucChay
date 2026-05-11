# Stored Procedure: `ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet_BK20200525`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-25 16:27:52.607000
- **Ngày sửa cuối**: 2020-05-25 16:27:52.607000

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
	EXEC  [dbo].[ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet] '2018-05-10'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet_BK20200525]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @ThucChayMuaNgoaiChiTietID INT, @HopDongREF INT, @HopDongChiTietREF int, @SoLuongThucChay INT, @DmDonViTinhREF INT
	, @ThanhTienThucChayBanSauCK FLOAT, @LastModifiedAt DATETIME, @DeletedStatus SMALLINT
	DECLARE @GhiChu NVARCHAR(MAX) ='', @ThanhTienThucChayMuaNgoaiSauCK_Bf FLOAT, @SoLuongThucChay_Bf BIGINT, @DonViTinhThucChay NVARCHAR(100)

	--CHECK THONG TIN PHAT SINH GIA TRI THAY DOI
	  
	DECLARE MuaNgoai_Cursor CURSOR FOR

	SELECT DISTINCT A.ThucChayMuaNgoaiChiTietID, A.HopDongREF, A.HopDongChiTietREF, ISNULL(A.SoLuongThucChay,0)SoLuongThucChay, A.DmDonViTinhREF
	, ISNULL(A.ThanhTienThucChayBanSauCK,0)ThanhTienThucChayBanSauCK, A.LastModifiedAt, A.DeletedStatus 
	FROM
	(
		--HDCT - HOPDONGCHITIET - THAY DOI
		SELECT ThucChayMuaNgoaiChiTietID, HopDongREF, HopDongChiTietREF, SoLuongThucChay
		, DmDonViTinhREF, ThanhTienThucChayBanSauCK, LastModifiedAt, DeletedStatus 
		FROM dbo.ThucChayMuaNgoaiChiTiet
		WHERE 1=1 AND EXISTS(SELECT hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct
			WHERE 1=1 AND hdct.DeletedStatus = 0 
			AND hdct.HopDongChiTietID = HopDongChiTietREF 
			AND (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
			AND CONVERT(DATE,hdct.LastModifiedAt) = @NgayThucHien
		)
		UNION
		--DU TOAN THAY DOI - HOPDONGCHITIET_MUANGOAI - THAY DOI
		SELECT ThucChayMuaNgoaiChiTietID, HopDongREF, HopDongChiTietREF, SoLuongThucChay
		, DmDonViTinhREF, ThanhTienThucChayBanSauCK, LastModifiedAt, DeletedStatus 
		FROM dbo.ThucChayMuaNgoaiChiTiet
		WHERE 1=1 AND EXISTS(SELECT hdctm.HopDongChiTietID FROM dbo.HopDongChiTiet_MuaNgoai hdctm
			WHERE 1=1 AND hdctm.DeletedStatus = 0 
			AND hdctm.HopDongChiTietID = HopDongChiTietREF 
			AND CONVERT(DATE,hdctm.LastModifiedAt) = @NgayThucHien
		)
		UNION
		--THUC CHAY MUA NGOAI THAY DOI
		SELECT ThucChayMuaNgoaiChiTietID, HopDongREF, HopDongChiTietREF, SoLuongThucChay
		, DmDonViTinhREF, ThanhTienThucChayBanSauCK, LastModifiedAt, DeletedStatus  
		FROM dbo.ThucChayMuaNgoaiChiTiet
		WHERE 1=1 AND CONVERT(DATE,LastModifiedAt) = @NgayThucHien
	)A

	OPEN MuaNgoai_Cursor
	
	FETCH NEXT FROM MuaNgoai_Cursor INTO @ThucChayMuaNgoaiChiTietID, @HopDongREF, @HopDongChiTietREF , @SoLuongThucChay , @DmDonViTinhREF 
	, @ThanhTienThucChayBanSauCK , @LastModifiedAt , @DeletedStatus 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT CONVERT(NVARCHAR(100),@ThucChayMuaNgoaiChiTietID)
		
		--CHECK CO THONG TIN THUCCHAYMUANGOAICHITIET CO BI XOA
		IF(@DeletedStatus = 1)
		BEGIN
		    --1.THUC HIEN DOI TRU GIAM GIA TRI CỦA THUCCHAYMUANGOAICHITIET
			--PRINT 'THUC HIEN DOI TRU GIAM GIA TRI CỦA THUCCHAYMUANGOAICHITIET'
			SET @GhiChu = N'Doi tru thuc chay do xoa ThucChayMuaNgoaiChiTietID = ' + CONVERT(NVARCHAR(100),@ThucChayMuaNgoaiChiTietID)

			EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_DoiTruGiam]
			@NgayThucHien						= @NgayThucHien,
			@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
			@HopDongREF							= @HopDongREF,
			@HopDongChiTietREF					= @HopDongChiTietREF,
			@ghiChu								= @GhiChu

			--2.THUC HIEN DOI TRU GIAM GIA TRI CUA LAI MUA NGOAI

		END
		--CHECK CO THONG TIN THUCCHAYMUANGOAICHITIET CO THAY DOI SOLUONGTHUCCHAY/THANHTIENBANSAUCHIETKHAU?
		ELSE
		BEGIN
		    --PRINT 'CHECK CO THONG TIN THUCCHAYMUANGOAICHITIET CO THAY DOI SOLUONGTHUCCHAY/THANHTIENBANSAUCHIETKHAU?'
			IF(EXISTS(SELECT TOP (1) HopDongID FROM dbo.ThucChayDaTinh
			WHERE HopDongID = @HopDongREF
			AND HopDongChiTietREF = @HopDongChiTietREF
			AND SoLuongDotChayBooking = @ThucChayMuaNgoaiChiTietID
			AND (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
			AND NgayThucHien < @NgayThucHien ORDER BY HopDongID))
			BEGIN
				--1. CHECK VA TINH GIA TRI THAY DOI CHO THUC CHAY BAN
			    SELECT TOP (1) @ThanhTienThucChayMuaNgoaiSauCK_Bf =  (CASE WHEN ChietKhau <> 100  THEN SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) 
																ELSE SUM(ThanhTienKM + GiaTriKMThayDoi)
															END)
				, @SoLuongThucChay_Bf = (CASE WHEN ChietKhau <> 100 THEN SUM(SoLuongThucChay + SoLuongThayDoi)
											ELSE SUM(SoLuongThucChayKM + SoLuongKMThayDoi)
										END)
				FROM dbo.ThucChayDaTinh
					WHERE HopDongID = @HopDongREF
					AND HopDongChiTietREF = @HopDongChiTietREF
					AND SoLuongDotChayBooking = @ThucChayMuaNgoaiChiTietID
					AND (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
					AND NgayThucHien < @NgayThucHien 
					GROUP BY ChietKhau

				SET @SoLuongThucChay_Bf = ISNULL(@SoLuongThucChay_Bf,0)
				SET @ThanhTienThucChayMuaNgoaiSauCK_Bf = ISNULL(@ThanhTienThucChayMuaNgoaiSauCK_Bf,0)

				IF(ROUND(@ThanhTienThucChayBanSauCK,0) <> ROUND(@ThanhTienThucChayMuaNgoaiSauCK_Bf,0))
				BEGIN
					SET @DonViTinhThucChay = (SELECT TOP (1) TenDonViTinh FROM dbo.DmDonViTinh  WHERE DmDonViTinhID = @DmDonViTinhREF)
					SET @GhiChu = N'DOI TRU MUA NGOAI, THAY DOI THANH TIEN THUC CHAY: ' + CONVERT(NVARCHAR(100), @ThucChayMuaNgoaiChiTietID)
					--TINH DOI TRU THUC CHAY
					EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_DoiTruGiam]
					@NgayThucHien						= @NgayThucHien,
					@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
					@HopDongREF							= @HopDongREF,
					@HopDongChiTietREF					= @HopDongChiTietREF,
					@ghiChu								= @GhiChu
					--THUC HIEN TINH LAI GIA TRI THAY DOI
					SET @GhiChu =  N'TINH LAI, THAY DOI THANH TIEN THUC CHAY: ' + CONVERT(NVARCHAR(100), @ThucChayMuaNgoaiChiTietID)

					EXEC [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_ThayDoi]
					@NgayThucHien						= @NgayThucHien,
					@ThucChayMuaNgoaiChiTietID			= @ThucChayMuaNgoaiChiTietID,
					@HopDongREF							= @HopDongREF,
					@HopDongChiTietREF					= @HopDongChiTietREF,
					@SoLuongThucChay					= @SoLuongThucChay,
					@ThanhTienThucChayBanSauCK			= @ThanhTienThucChayBanSauCK,
					@DonViTinhThucChay					= @DonViTinhThucChay,
					@ghiChu								= @GhiChu

					--UPDATE TRANG THAI DA TINH THUC CHAY MUA NGOAI
					IF(EXISTS(SELECT TOP (1) HopDongID FROM dbo.ThucChayDaTinh 
						WHERE HopDongID = @HopDongREF AND HopDongChiTietREF = @HopDongChiTietREF
						AND SoLuongDotChayBooking = @ThucChayMuaNgoaiChiTietID ORDER BY HopDongID))
					BEGIN
						UPDATE dbo.ThucChayMuaNgoaiChiTiet
						SET TrangThaiTinhThucChay = 1
						WHERE ThucChayMuaNgoaiChiTietID = @ThucChayMuaNgoaiChiTietID
					END
				END

				--2. CHECK VA TINH GIA TRI THAY DOI CHO LAI MUA NGOAI HAIDH 20200518

			END

		END

	FETCH NEXT FROM MuaNgoai_Cursor INTO @ThucChayMuaNgoaiChiTietID, @HopDongREF, @HopDongChiTietREF , @SoLuongThucChay , @DmDonViTinhREF 
	, @ThanhTienThucChayBanSauCK , @LastModifiedAt , @DeletedStatus  
	END
	
	CLOSE MuaNgoai_Cursor
	DEALLOCATE MuaNgoai_Cursor

END

```
