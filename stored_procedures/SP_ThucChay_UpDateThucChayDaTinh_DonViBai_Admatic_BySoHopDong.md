# Stored Procedure: `ThucChay_UpDateThucChayDaTinh_DonViBai_Admatic_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-23 11:59:05.300000
- **Ngày sửa cuối**: 2021-07-23 17:38:57.950000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


/*HAM THUC HIEN XU LY CHO TRUONG HOP DA QUA THOI GIAN CHAY MA CHUA TINH THUC CHAY CHO HOP DONG CPM DON VI BAI*/
/*

EXEC [dbo].[ThucChay_UpDateThucChayDaTinh_DonViBai_BySoHopDong] 
        '2021-01-20' ,
        '2021-02-28' ,
        '2021-03-25' ,
        'QC5970121'
*/
CREATE PROCEDURE [dbo].[ThucChay_UpDateThucChayDaTinh_DonViBai_Admatic_BySoHopDong] 
	@NgayGhiNhanThucChay DATETIME,
	@pSoHopDong NVARCHAR(100)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT =0
	DECLARE @SoHopDong NVARCHAR(50)
			   ,@HopDongID INT
			   ,@HopDongChiTietREF INT
			   ,@DmSanPhamREF INT
			   ,@DmBannerREF INT
			   ,@ThucChayHopDongChiTietREF INT

	SET @NgayThucHien = @NgayGhiNhanThucChay
	SET @SoHopDong = @pSoHopDong

	--THUC HIEN XOA DL THUC CHAY DONVIBAI TRUOC KHI TINH
	DELETE FROM [dbo].[ThucChay_DonViBai_Temp]

	INSERT INTO [dbo].[ThucChay_DonViBai_Temp]
			(
			ThucChayID
			,[SoHopDong]
			,[HopDongREF]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[DmBannerREF]
			,[HopDongChiTietREF]
			,[ThucChayHopDongChiTietREF]
			)

	SELECT DISTINCT 0, hd.SoHopDong,  hd.HopDongID, hd.DmSanPhamREF, hd.TenSanPham, 0 AS DmBannerREF
		, hd.HopDongChiTietID as HopDongChiTietREF, hd.ThucChayHopDongChiTietID FROM
	
	(
		SELECT hd.HopDongID, hd.SoHopDong, hdct.HopDongChiTietID
		, hdct.DmSanPhamREF, hdct.TenSanPham, tchdct.DmBannerREF, tchdct.ThucChayHopDongChiTietID FROM
		(
			SELECT hd.SoHopDong, hd.HopDongID FROM dbo.HopDong hd 
			WHERE hd.NgayDanhSoHopDong >= '2021-01-01'	AND hd.TrangThaiHopDong <> 3
			AND hd.SoHopDong = @SoHopDong
		)hd
		INNER JOIN
		(
			SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmViTriREF
			, hdct.DonViTinhREF FROM dbo.HopDongChiTiet hdct 
			WHERE hdct.DeletedStatus = 0
			AND hdct.DmSanPhamREF = 598 AND hdct.DmViTriREF = 9198 AND hdct.DonViTinhREF = 7 --King size, Sponsor Page, Bai 
			AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) --loai mua ngoai
			AND hdct.DmLoaiREF = 42 --Admatic
		)hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN (
			SELECT tchdct.* FROM dbo.ThucChayHopDongChiTiet tchdct 
			WHERE tchdct.DmSanPhamREF = 598
			AND tchdct.DmHinhThucQuangCaoREF = 42 --Admatic
			AND tchdct.DeletedStatus = 0
			AND CONVERT(DATE, tchdct.LastModifiedAt) <= @NgayThucHien
		)tchdct ON hdct.HopDongFK = tchdct.HopDongREF AND hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		AND hdct.DmSanPhamREF = tchdct.DmSanPhamREF 
	)hd 
	--AND tcc.DmBannerREF = hd.DmBannerREF --theo link bai và bannerid = 0, haidh comment 2021-07-23

	--THUC HIEN TINH GIA TRI THUC CHAY

	--select * from  [ThucChay_DonViBai_Temp]

	DECLARE Record_Cursor_DonViBai_AdTT CURSOR FOR 
	SELECT distinct [SoHopDong]
			,[HopDongREF]
			,[HopDongChiTietREF]
			,[DmSanPhamREF]
			,[DmBannerREF]
			,ThucChayHopDongChiTietREF
		FROM	dbo.[ThucChay_DonViBai_Temp]
	ORDER BY [HopDongREF], [HopDongChiTietREF]	

	OPEN Record_Cursor_DonViBai_AdTT

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_DonViBai_AdTT into @SoHopDong ,@HopDongID ,@HopDongChiTietREF,@DmSanPhamREF,@DmBannerREF,@ThucChayHopDongChiTietREF
			
	WHILE @@FETCH_STATUS = 0
		BEGIN
			DECLARE @ThucChayDaTinhID_op NVARCHAR(200) = '',
			@ThanhTien float = 0
			SET @ThanhTien = (SELECT TOP (1) hdct.ThanhTien FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietREF order by hdct.HopDongChiTietID)
			--XAC DINH HOP DONG CHI TIET DA TINH THUC CHAY CHUA
			--NEU CHUA TINH THUC CHAY
			IF NOT EXISTS(
				SELECT tcdt.HopDongChiTietREF, sum(tcdt.ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM dbo.ThucChayDaTinh tcdt
				WHERE tcdt.HopDongID = @HopDongID
				AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
				AND tcdt.SoLuongDotChayHD = @ThucChayHopDongChiTietREF
				AND tcdt.NgayThucHien <= @NgayGhiNhanThucChay
				GROUP BY tcdt.HopDongChiTietREF HAVING abs(sum(tcdt.ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) >= 1
			)
			BEGIN
				--THUC HIEN TINH THUC CHAY
				--PRINT 'TINH THUC CHAY CHO TOAN BO PHAN BO'
				EXEC [dbo].ThucChay_InsertThucChayDaTinh_CPM_DonViBai_Admatic_ThucTreo 
					@NgayThucHien = @NgayGhiNhanThucChay,
					@HopDongID = @HopDongID,
					@HopDongChiTietREF = @HopDongChiTietREF,
					@DmSanPhamREF = @DmSanPhamREF,
					@DmBannerREF = @DmBannerREF,
					@ThucChayHopDongChiTietREF = @ThucChayHopDongChiTietREF,
					@ThucChayDaTinhID_output = @ThucChayDaTinhID_op output

				select @ThucChayDaTinhID_op
			END
		FETCH NEXT FROM Record_Cursor_DonViBai_AdTT into @SoHopDong ,@HopDongID ,@HopDongChiTietREF,@DmSanPhamREF,@DmBannerREF,@ThucChayHopDongChiTietREF
		END

	CLOSE Record_Cursor_DonViBai_AdTT
	DEALLOCATE Record_Cursor_DonViBai_AdTT

	DELETE FROM dbo.[ThucChay_DonViBai_Temp]

	
	SELECT '1'
END


```
