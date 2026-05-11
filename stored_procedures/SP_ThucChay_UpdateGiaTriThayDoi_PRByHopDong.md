# Stored Procedure: `ThucChay_UpdateGiaTriThayDoi_PRByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-02-08 09:45:25.127000
- **Ngày sửa cuối**: 2015-04-17 12:18:26.590000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoi_PRByHopDong] '2015-04-15','QC1071114',68164
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoi_PRByHopDong] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @HopDongREF INT, @DmSanPhamREF INT, @DmWebsiteREF INT
	DECLARE @GiaTien FLOAT,  @SoluongThucChay INT, @isKhuyenMai INT, @GiaTriThayDoiBF FLOAT
	DECLARE @ThanhTienDaTinh FLOAT, @ChietKhau INT, @ISEXIST_HDCT INT, @GiaTienSauCK FLOAT
	DECLARE @GiaTriThayDoiHT FLOAT, @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(MAX), @ThoiGianBDTinh DATETIME
	SET @ThoiGianBDTinh = '2013-01-01'
	
	PRINT @HopDongChiTietID
	SET @GiaTien = 0
	SET @SoluongThucChay = 0
	SET @GiaTriThayDoiBF = 0
	SET @GiaTriThayDoiHT = 0
	SET @GiaTienSauCK = 0
	SET @ThanhTienDaTinh = 0
	--
	SELECT @HopDongREF = hd.HopDongID FROM HopDong hd
	WHERE hd.SoHopDong = @SoHopDong
	
	UPDATE ThucChayDaTinh
	SET
		GiaTriThayDoi = 0, -- Cho nay check ky HAIDH 29/10/2013
		LastModifiedAt = GETDATE()
	WHERE HopDongChiTietREF = @HopDongChiTietID
	AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
				 
	--GET SO TIEN VA SO LUONG THUCCHAY CUA HOPDONGCHITIET DEN NGAYTHUCHIEN
	SELECT @GiaTien = SUM(isnull(tchdctp.GiaTien,0)), @SoluongThucChay = COUNT(tchdctp.HopDongChiTietREF) 
	FROM ThucChayHopDongChiTietPR tchdctp
	WHERE tchdctp.HopDongChiTietREF = @HopDongChiTietID
		AND (   CASE 
				   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN convert(date,tchdctp.CreatedAt)
				   ELSE convert(date,tchdctp.LastModifiedAt)
				END
			) <= @NgayThucHien
		 AND convert(date,tchdctp.ThoiGianBatDau) >= @ThoiGianBDTinh
		 AND tchdctp.DeletedStatus = 0
		 AND tchdctp.RecordStatus = 1	
	GROUP BY tchdctp.HopDongChiTietREF
	
	SET @GiaTien = ISNULL(@GiaTien,0)
	SET @SoluongThucChay = ISNULL(@SoluongThucChay,0)
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
		SET @CONTENT_LOG = N'(Có thay đổi thực treo, Giá trị:' + CONVERT(NVARCHAR(20),convert(bigint,@ThanhTienDaTinh)) + '->' + CONVERT(NVARCHAR(20),convert(bigint,@GiaTienSauCK)) 
		SET @NGUON_LOG = 'Table:ThucChayHopDongChiTietPR, NgayThucHien:' + CONVERT(NVARCHAR(20),@NgayThucHien) + ', HDCT:' + CONVERT(NVARCHAR(20),@HopDongChiTietID)
		--GHI LOG VIEC THAY DOI
		INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
		  ([ThuChay_LogNNTinhGiaTriThayDoiID],
			[HopDongREF],[SoHopDong],[HopDongChiTietREF],[NgayThucHien],
			[GiaTriThayDoi],[GiaSauCK1],[Soluong1],[GiaSauCK2],[Soluong2],
			[NoiDungLog],[NguonLog],[GhiChu],[CreatedBy],[CreatedAt],
			[LastModifiedBy],[LastModifiedAt],[DeletedStatus],
			[PrintStatus],[RecordStatus]
		  )
		VALUES
		  (NEWID(),
			@HopDongREF,@SoHopDong,@HopDongChiTietID,@NgayThucHien,
			@GiaTriThayDoiHT,0,0,0,0,@CONTENT_LOG
			,@NGUON_LOG,'PR',	'ThucChay',	GETDATE(),
			'ThucChay',GETDATE(),0,
			0,0
		  )			
    END
    SELECT 2
END
--EXEC [ThucChay_UpdateGiaTriThayDoi_PRByHopDong] '2013-11-13', 'DT741013' ,48332
--44525
--44528
--44529
--44530
--44531


```
