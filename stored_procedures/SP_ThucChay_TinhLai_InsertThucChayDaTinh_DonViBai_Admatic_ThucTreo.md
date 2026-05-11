# Stored Procedure: `ThucChay_TinhLai_InsertThucChayDaTinh_DonViBai_Admatic_ThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-23 11:47:12.750000
- **Ngày sửa cuối**: 2023-09-13 17:32:40.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChuTinhLai` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
--EXEC [ThucChay_TinhLai_InsertThucChayDaTinh_CPM_DonViBai]
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_TinhLai_InsertThucChayDaTinh_DonViBai_Admatic_ThucTreo] 
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmSanPhamREF INT,
	@GhiChuTinhLai NVARCHAR(1000)
AS
BEGIN

	DECLARE @NgayGioiHanTinh DATETIME, @SoHopDong NVARCHAR(50), @NgayDanhSoGioiHan DATETIME, @DmBannerREF INT
	, @ThucChayHopDongChiTietREF INT
	SET @NgayGioiHanTinh = '2021-01-01'
	SET @NgayDanhSoGioiHan = '2021-06-10'
	SET @SoHopDong = ISNULL((SELECT TOP (1) hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'')
	--KIEM TRA TINH TON TAI CỦA THUC TREO VA THUC CHAY CUA HOP DONG DON VI BAI
	--THUC HIEN XOA DL THUC CHAY DONVIBAI TRUOC KHI TINH
	DELETE FROM [dbo].[ThucChay_DonViBai_Temp]

	INSERT INTO [dbo].[ThucChay_DonViBai_Temp]
			([ThucChayID]
			,[SoHopDong]
			,[HopDongREF]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[DmBannerREF]
			,[HopDongChiTietREF]
			,[ThucChayHopDongChiTietREF]
			,CreatedBy
			,CreatedAt
			,LastModifiedBy
			,LastModifiedAt
			,DeletedStatus
			,PrintStatus
			,RecordStatus
			)

	SELECT DISTINCT 0 as ThucChayID, hd.SoHopDong,  hd.HopDongID, hd.DmSanPhamREF, hd.TenSanPham, 0 AS DmBannerREF
		,hd.HopDongChiTietID as HopDongChiTietREF, hd.ThucChayHopDongChiTietID
		,'' AS CreatedBy, getdate() CreatedAt,'' AS LastModifiedBy, getdate() LastModifiedAt
		, 0 as DeletedStatus , 0 as PrintStatus , 0 as RecordStatus FROM
	
	(
		SELECT hd.HopDongID, hd.SoHopDong, hdct.HopDongChiTietID
		, hdct.DmSanPhamREF, hdct.TenSanPham, tchdct.DmBannerREF, tchdct.ThucChayHopDongChiTietID FROM
		(
			SELECT hd.SoHopDong, hd.HopDongID FROM dbo.HopDong hd 
			WHERE hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan AND hd.TrangThaiHopDong in (1,2,4) AND hd.HopDongID = @HopDongID
		)hd
		INNER JOIN
		(
			SELECT hdct.HopDongFK, hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham, hdct.DmViTriREF
			, hdct.DonViTinhREF FROM dbo.HopDongChiTiet hdct 
			WHERE hdct.DeletedStatus = 0
			AND ((hdct.DmSanPhamREF in (305,5312)) OR (hdct.DmSanPhamREF = 598 AND hdct.DmViTriREF = 9198)) 
			AND hdct.DonViTinhREF IN (7,84) --King size, Sponsor Page, Bai , URL
			AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) --loai mua ngoai
			AND hdct.DmLoaiREF = 42 --Admatic
			AND hdct.HopDongChiTietID=@HopDongChiTietREF
		)hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN (
			SELECT tchdct.* FROM dbo.ThucChayHopDongChiTiet tchdct 
			WHERE tchdct.DmSanPhamREF IN (305, 598,5312)
			AND tchdct.DmHinhThucQuangCaoREF = 42 --Admatic
			AND tchdct.DeletedStatus = 0
			AND tchdct.RecordStatus = 0
			AND CONVERT(DATE,tchdct.LastModifiedAt) <= @NgayThucHien
		)tchdct ON hdct.HopDongFK = tchdct.HopDongREF AND hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		AND hdct.DmSanPhamREF = tchdct.DmSanPhamREF 
	)hd 
	--AND tcc.DmBannerREF = hd.DmBannerREF --theo link bai và bannerid = 0, haidh comment 2021-07-23

	--THUC HIEN TINH GIA TRI THUC CHAY

	DECLARE Record_Cursor_DonViBai_AdTT CURSOR FOR 
	SELECT distinct [SoHopDong]
			,[HopDongREF]
			,[HopDongChiTietREF]
			,ThucChayHopDongChiTietREF
			,[DmSanPhamREF]
			,DmBannerREF
	FROM	dbo.[ThucChay_DonViBai_Temp]
	ORDER BY [HopDongREF], [HopDongChiTietREF]	

	OPEN Record_Cursor_DonViBai_AdTT

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_DonViBai_AdTT into @SoHopDong ,@HopDongID ,@HopDongChiTietREF,@ThucChayHopDongChiTietREF,@DmSanPhamREF, @DmBannerREF
			
	WHILE @@FETCH_STATUS = 0
		BEGIN
			DECLARE @ThanhTien_HDCT FLOAT = 0
			, @DonGia FLOAT = 0
			, @SoLuong INT = 0
			, @ChietKhau FLOAT = 0
			, @ThanhTienThucChayDaTinh FLOAT = 0
			, @ThanhTienKMThucChayDaTinh FLOAT = 0
			, @ThucChayDaTinhID_op NVARCHAR(200) = ''
				
			SELECT @ThanhTien_HDCT = hdct.ThanhTien
			, @DonGia = hdct.DonGia
			, @SoLuong = hdct.SoLuong
			, @ChietKhau = hdct.ChietKhau FROM dbo.HopDongChiTiet hdct
			WHERE hdct.HopDongChiTietID = @HopDongChiTietREF

			SET @ThanhTien_HDCT = ISNULL(@ThanhTien_HDCT,0)
			SET @DonGia = ISNULL(@DonGia,0)
			SET @SoLuong = ISNULL(@SoLuong,0)
			SET @ChietKhau = ISNULL(@ChietKhau,0)

			SELECT @ThanhTienThucChayDaTinh = sum(tcdt.ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
			, @ThanhTienKMThucChayDaTinh = SUM(tcdt.ThanhTienKM + GiaTriKMThayDoi) FROM dbo.ThucChayDaTinh tcdt
				WHERE tcdt.HopDongID = @HopDongID
				AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
				AND tcdt.NgayThucHien <= @NgayThucHien
				GROUP BY tcdt.HopDongChiTietREF

			--XAC DINH HOP DONG CHI TIET DA TINH THUC CHAY CHUA
			--NEU CHUA TINH THUC CHAY DU TIEN
			IF ( (@ChietKhau <> 100 AND @ThanhTien_HDCT > @ThanhTienThucChayDaTinh) OR (@ChietKhau = 100 AND @DonGia*@SoLuong > @ThanhTienKMThucChayDaTinh)	)
			BEGIN
				--THUC HIEN TINH THUC CHAY
				PRINT 'TINH THUC CHAY CHO TUNG THUC TREO CO PS THUC CHAY'
				--NEU KO TON TAI BANNER DA TINH TIEN
				IF(NOT EXISTS(SELECT tcdt.HopDongChiTietREF,SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)  FROM dbo.ThucChayDaTinh tcdt
					WHERE CONVERT(date,tcdt.NgayThucHien) <= @NgayThucHien
					AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.DmHinhThucQuangCao = 42 --Admatic
					--AND tcdt.DmVitriREF = 9198
					AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
					AND tcdt.SoLuongDotChayHD = @ThucChayHopDongChiTietREF
					AND (tcdt.DonViTinh = N'BÀI' OR tcdt.DonViTinh = N'URL')
					AND tcdt.DotChayHopDong = N'CPM_DonViBai'
					GROUP BY tcdt.DmBannerREF, tcdt.HopDongChiTietREF having (SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) <> 0
					OR SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) <> 0)
				))
				BEGIN
					PRINT 'TINH LAI'
					--select @NgayThucHien,@HopDongID,@HopDongChiTietREF,@DmSanPhamREF,@DmBannerREF, @ThucChayHopDongChiTietREF
					EXEC [dbo].[ThucChay_InsertGTTD_ThucChayDaTinh_DonViBai_Admatic_ThucTreo] 
						@NgayThucHien = @NgayThucHien,
						@HopDongID = @HopDongID,
						@HopDongChiTietREF = @HopDongChiTietREF,
						@DmSanPhamREF = @DmSanPhamREF,
						@DmBannerREF = @DmBannerREF,
						@ThucChayHopDongChiTietREF = @ThucChayHopDongChiTietREF,
						@ThucChayDaTinhID_output = @ThucChayDaTinhID_op OUTPUT
					IF(EXISTS(SELECT top (1) tcdt.HopDongChiTietREF FROM dbo.ThucChayDaTinh tcdt
					WHERE tcdt.ThucChayDaTinhID = @ThucChayDaTinhID_op
					AND tcdt.HopDongID = @HopDongID
					AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
					AND tcdt.NgayThucHien = @NgayThucHien))
					BEGIN
						UPDATE tt
						SET tt.RecordStatus = 1
						FROM dbo.ThucChayHopDongChiTiet tt
						WHERE tt.ThucChayHopDongChiTietID = @ThucChayHopDongChiTietREF
						AND tt.HopDongREF = @HopDongID
						AND tt.HopDongChiTietREF = @HopDongChiTietREF
					END
				END

			END
		FETCH NEXT FROM Record_Cursor_DonViBai_AdTT into @SoHopDong ,@HopDongID ,@HopDongChiTietREF,@ThucChayHopDongChiTietREF,@DmSanPhamREF, @DmBannerREF
		END

	CLOSE Record_Cursor_DonViBai_AdTT
	DEALLOCATE Record_Cursor_DonViBai_AdTT
	DELETE FROM dbo.[ThucChay_DonViBai_Temp]

END


```
