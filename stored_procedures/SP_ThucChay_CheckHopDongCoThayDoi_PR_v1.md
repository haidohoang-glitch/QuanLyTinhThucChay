# Stored Procedure: `ThucChay_CheckHopDongCoThayDoi_PR_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-24 10:48:25.670000
- **Ngày sửa cuối**: 2015-12-03 14:12:44.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec ThucChay_CheckHopDongCoThayDoi_PR_v1 25611, 'DT160514', 57511, '2014-05-22'
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongCoThayDoi_PR_v1] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @CountHDTD INT, @HopDongChiTietThayDoiCK INT, @ChietKhau INT, @HopDongChiTiet INT
	DECLARE @DmSanPhamREF INT, @DmWebsiteREF INT, @TenWebsite NVARCHAR(100), @CONTENT_LOG NVARCHAR(200), @NGUON_LOG NVARCHAR(200)
	DECLARE @GiaTien BIGINT, @SoluongThucChay INT, @GiaTienSauCK BIGINT, @NgayGioiHanTinh DATETIME
	DECLARE @isKhuyenMai INT, @ThanhTienDaTinh FLOAT, @GiaTriThayDoiHT FLOAT, @ISEXIST_HDCT INT, @GiaTriThayDoiBF FLOAT
	
	SET @CountHDTD = 0
	SET @ThanhTienDaTinh = 0
	SET @NgayGioiHanTinh = '2013-01-01'
	SET @GiaTien = 0
	SET @SoluongThucChay = 0 
	SET @GiaTienSauCK = 0
	SET @ISEXIST_HDCT = 0
	SET @GiaTriThayDoiHT = 0
	SET @ThanhTienDaTinh = 0
	SET @GiaTriThayDoiBF = 0
	
	--XOA BAN NHUNG BAN GHI DA THUC HIEN INSERT VOI TRUONG HOP CHI CO GIA TRI THAY DOI
		DELETE FROM ThucChayDaTinh
		WHERE HopDongChiTietREF = @HopDongChiTietID
		AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
		AND DotChayHopDong = 'PR_TTR'
		
	--CHECK HOP DONG CO SU THAY DOI KHONG
	SET @CountHDTD = 
	(
		SELECT COUNT(*) FROM HopDongThayDoi hdtd
		WHERE hdtd.HopDongFK = @HopDongREF
		AND Convert(date,hdtd.NgayThayDoi) = @NgayThucHien
	)
	SET @CountHDTD = ISNULL(@CountHDTD,0)
	--NEU HOP DONG CO SU THAY DOI
	IF(@CountHDTD >0)
	BEGIN
		--CHECK HOPDONGCHITIET CO SU THAY DOI VE CHIET KHAU	
		SELECT @HopDongChiTietThayDoiCK = A.HopDongChiTietThayDoiID,
		@ChietKhau = A.ChietKhau, @HopDongChiTiet = A.HopDongChiTietREF 
		FROM 
		(
			SELECT TOP 1 hdcttd.HopDongChiTietThayDoiID, HDCTTD.HopDongChiTietREF ,HDTD.NgayThayDoi
			, HDCTTD.ChietKhau, HDCTTD.DonGia 
			FROM HopDongThayDoi hdtd
			INNER JOIN HopDongChiTietThayDoi hdcttd 
			ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
				WHERE hdcttd.HopDongChiTietREF = @HopDongChiTietID 
				AND Convert(date,hdtd.NgayThayDoi) =  Convert(date,@NgayThucHien)
				ORDER BY HDCTTD.HopDongChiTietThayDoiID 
		)A
		INNER JOIN HopDongChiTiet hdct ON HDCT.HopDongChiTietID = A.HopDongChiTietREF
		WHERE (A.ChietKhau != HDCT.ChietKhau)
		
		SELECT @DmSanPhamREF = hdct.DmSanPhamREF, @DmWebsiteREF = hdct.DmWebsiteREF 
		, @TenWebsite = hdct.TenWebsite
		FROM HopDongChiTiet hdct
		WHERE hdct.HopDongChiTietID = @HopDongChiTietID
		
		set @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
		SET @DmWebsiteREF = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF) 
		set @TenWebsite  = dbo.GetWebsiteLinkByDmWebsiteID(@DmWebsiteREF,@TenWebsite)

		--NEU CO THAY DOI VE CHIET KHAU
		IF(@HopDongChiTietThayDoiCK <>0)
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi chiết khấu =' + CONVERT(NVARCHAR(30),@ChietKhau) + '->' + CONVERT(NVARCHAR(30),@ChietKhau) + ');'
			SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi: '+ CONVERT(NVARCHAR(30),@HopDongChiTietID) 	
		END
		
		--GET SO TIEN VA SO LUONG THUCCHAY CUA HOPDONGCHITIET DEN NGAYTHUCHIEN
		SELECT @GiaTien = SUM(isnull(tchdctp.GiaTien,0)*ISNULL(tchdctp.SoLuong,0)), @SoluongThucChay = SUM(isnull(tchdctp.SoLuong,0)) 
		FROM ThucChayHopDongChiTietPR tchdctp
		WHERE tchdctp.HopDongChiTietREF = @HopDongChiTietID
			AND (   CASE 
					   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN convert(date,tchdctp.CreatedAt)
					   ELSE convert(date,tchdctp.LastModifiedAt)
					END
				) <= @NgayThucHien
			 AND convert(date,tchdctp.ThoiGianBatDau) >= @NgayGioiHanTinh
			 AND tchdctp.DeletedStatus = 0	
		GROUP BY tchdctp.HopDongChiTietREF
	
			
		SET @GiaTien = ISNULL(@GiaTien,0)
		SET @SoluongThucChay = ISNULL(@SoluongThucChay,0)
		
		--PRINT CONVERT(NVARCHAR(30),@GiaTien) + ': gia tien'
		--GET HOPDONGCHITIET LA KHUYEN MAI ?     
		SET @isKhuyenMai = 
		(
			SELECT hdct.IsKhuyenMai FROM HopDongChiTiet hdct
			WHERE hdct.HopDongChiTietID = @HopDongChiTietID
		)
	    --CHECK NEU LA HOPDONGCHITIET KHUYEN MAI
	    IF(@isKhuyenMai = 1)
	    BEGIN
			--1. GET THANHTIENKHUYENMAI DA TINH CUA HOPDONGCHITIET
			SET @ThanhTienDaTinh = 
			(
	    		SELECT SUM(ISNULL(tcdt.ThanhTienKM,0) + ISNULL(tcdt.GiaTriThayDoi,0)) 
	    		FROM ThucChayDaTinh tcdt
	    		WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
	    			AND CONVERT(DATE,tcdt.NgayThucHien) <= @NgayThucHien
			)
			SET @ThanhTienDaTinh = ISNULL(@ThanhTienDaTinh,0)
			SET @GiaTienSauCK = @GiaTien
			--HAIDH COMMENT
			SET @ThanhTienDaTinh = 0
			SET @GiaTienSauCK = 0
	    END
	    
	    --CHECK NEU LA HOPDONGCHITIET KHONG KHUYEN MAI
	    IF(@isKhuyenMai = 0)
	    BEGIN
			--1. GET THANHTIENSAUTRIETKHAU DA TINH CUA HOPDONGCHITIET					
			SET @ThanhTienDaTinh = 
			(
				SELECT SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0))
				FROM ThucChayDaTinh tcdt
				WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND CONVERT(DATE,tcdt.NgayThucHien) <= @NgayThucHien
			)
			SET @ThanhTienDaTinh = ISNULL(@ThanhTienDaTinh,0)
			--2. GET CHIET KHAU CUA HOP DONG
			SET @ChietKhau =
			(
				SELECT hdct.ChietKhau FROM HopDongChiTiet hdct
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID	
			)
			SET @ChietKhau = ISNULL(@ChietKhau,0)
			SET @GiaTienSauCK = @GiaTien*(100-@ChietKhau)/100 
	    END
	    
	    --1 IF THANHTIEN DA TINH = 0 HOAC = SO TIEN HIEN TAI THI KHONG LAM GI CA
	    --1 IF THANHTIEN DA TINH <>0 VA <> SO TIEN HIEN TAI THI THUC HIEN TINH
	    IF((@ThanhTienDaTinh <>0) AND (@ThanhTienDaTinh <> @GiaTienSauCK))
	    BEGIN
	    	SET @GiaTriThayDoiHT = @GiaTienSauCK - @ThanhTienDaTinh
	    	--PRINT convert(nvarchar(50),@ThanhTienDaTinh) + ': thanhtiendateinh'
	    	SET @DmSanPhamREF = 0
	    	SET @DmWebsiteREF = 0
	    	SELECT @DmSanPhamREF = hdct.DmSanPhamREF, @DmWebsiteREF = hdct.DmWebsiteREF
	    	  FROM HopDongChiTiet hdct
	    	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	    	SET @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
	    	SET @DmWebsiteREF = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF)
	    	
	    	--PRINT convert(nvarchar(50),@GiaTienSauCK) + ': gia tien csau ck'
	    	SET @ISEXIST_HDCT =
	    	(
	    		SELECT COUNT(tcdt.HopDongChiTietREF) FROM ThucChayDaTinh tcdt
	    		WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
	    		AND CONVERT(DATE,tcdt.NgayThucHien) = @NgayThucHien
	    	)
			--1.1 NEU DA TON TAI BAN GHI CUA HOPDONGCHITIET TAI NGAY HIEN TAI THI THUC HIEN UPDATE GIA TRI THAY DOI
			IF(@ISEXIST_HDCT >0)
			BEGIN
				--GET GIA TRI THAY DOI TRUOC DO
				SET @GiaTriThayDoiBF =
				(
					SELECT SUM(ISNULL(tcdt.GiaTriThayDoi,0)) FROM ThucChayDaTinh tcdt
					WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND CONVERT(DATE,tcdt.NgayThucHien) = @NgayThucHien	
				)
				UPDATE ThucChayDaTinh
				SET
					GiaTriThayDoi = @GiaTriThayDoiHT - @GiaTriThayDoiBF, -- Cho nay check ky HAIDH 29/10/2013
					LastModifiedAt = GETDATE()
				WHERE HopDongChiTietREF = @HopDongChiTietID
				AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
			END
			--1.2 NEU CHUA TON TAI THI TAO BAN GHI MOI CHO HOPDONGCHITIET TAI NGAY HIEN TAI VOI SO TIEN KHUYEN MAI	
			IF(@ISEXIST_HDCT = 0)
			BEGIN
				EXEC ThucChay_InsertThucTreoThayDoi_PR @HopDongChiTietID, @NgayThucHien, @GiaTriThayDoiHT
			END
			--1.3 GHI LOG
			SET @CONTENT_LOG = @CONTENT_LOG + N' (Có thay đổi thực treo, Giá trị:' + CONVERT(NVARCHAR(20),convert(bigint,@ThanhTienDaTinh)) + '->' + CONVERT(NVARCHAR(20),convert(bigint,@GiaTienSauCK)) 
			SET @NGUON_LOG = 'Table:ThucChayHopDongChiTietPR, NgayThucHien:' + CONVERT(NVARCHAR(20),@NgayThucHien) + ', HDCT:' + CONVERT(NVARCHAR(20),@HopDongChiTietID)
			--GHI LOG VIEC THAY DOI
			INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
			  (ThuChay_LogNNTinhGiaTriThayDoiID,HopDongREF,SoHopDong,HopDongChiTietREF,
				DmSanPhamREF,DmWebsiteREF,NgayThucHien,	GiaTriThayDoi,GiaSauCK1,
				Soluong1,GiaSauCK2,Soluong2,NoiDungLog,NguonLog,GhiChu,
				CreatedBy,CreatedAt,LastModifiedBy,LastModifiedAt,DeletedStatus,PrintStatus,RecordStatus
			  )
			VALUES
			  (NEWID(),@HopDongREF,@SoHopDong,@HopDongChiTietID,
			  @DmSanPhamREF , @DmWebsiteREF , @NgayThucHien,@GiaTriThayDoiHT,0,
			  0,0,0,@CONTENT_LOG,@NGUON_LOG,'PR',
			  'ThucChay',GETDATE(),'ThucChay',GETDATE(),0,0,0
			  )			
	    END
		
	END
END


```
