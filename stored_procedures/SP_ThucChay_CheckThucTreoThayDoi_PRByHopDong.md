# Stored Procedure: `ThucChay_CheckThucTreoThayDoi_PRByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-02 17:28:33.257000
- **Ngày sửa cuối**: 2014-12-04 15:44:36.540000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_CheckThucTreoThayDoi_PRByHopDong] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@ThoiGianBDTinh DATETIME,
	@SoHopDong NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @HopDongREF INT, @HopDongChiTietID INT, @DmSanPhamREF INT, @DmWebsiteREF INT
	DECLARE @GiaTien FLOAT,  @SoluongThucChay INT, @isKhuyenMai INT, @GiaTriThayDoiBF FLOAT, @GiaTriThayDoi FLOAT
	DECLARE @ThanhTienDaTinh FLOAT, @ChietKhau INT, @ISEXIST_HDCT INT, @GiaTienSauCK FLOAT
	DECLARE @GiaTriThayDoiHT FLOAT, @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(MAX)
	
	
	
	DECLARE Record_Cursor CURSOR  
	FOR
	    --LAY THONG TIN HOPDONGCHITIET CUA TAT CAC CAC THUC TREO DC NHAP HOAC SUA NGAYTHUCHIEN> THOIGIANBATDAU
	    SELECT DISTINCT A.HopDongREF, A.SoHopDong ,A.HopDongChiTietREF
	    FROM(
               SELECT tchdctp.HopDongREF,
					  hd.SoHopDong,
                      tchdctp.HopDongChiTietREF,
                      tchdctp.GiaTien,
                      tchdctp.ThoiGianBatDau,
                      (   CASE 
                               WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN tchdctp.CreatedAt
                               ELSE tchdctp.LastModifiedAt
                          END
                      ) NgayThucHien
               FROM   ThucChayHopDongChiTietPR tchdctp
               INNER JOIN
               HopDong hd ON hd.HopDongID = tchdctp.HopDongREF AND hd.TrangThaiHopDong <> 3
                WHERE  tchdctp.ThoiGianBatDau IS NOT NULL
                      AND (   CASE 
                                   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
                                   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
                              END
                          ) >= CONVERT(DATE,tchdctp.ThoiGianBatDau)--Haidh: Note cho nay dang can nhac 11-10-2013
                      AND (   CASE 
                                   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
                                   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
                              END
                          ) = @NgayThucHien
                      AND tchdctp.HopDongChiTietREF <> 0
                      AND convert(date,tchdctp.ThoiGianBatDau) >= @ThoiGianBDTinh
                      AND hd.SoHopDong = @SoHopDong
	        )A
	    ORDER BY
	           A.HopDongREF, A.HopDongChiTietREF
	
	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT @HopDongChiTietID
		SET @GiaTien = 0
		SET @SoluongThucChay = 0
		SET @GiaTriThayDoiBF = 0
		SET @GiaTriThayDoiHT = 0
		SET @GiaTienSauCK = 0
		SET @ThanhTienDaTinh = 0
		
		--GET SO TIEN VA SO LUONG THUCCHAY CUA HOPDONGCHITIET DEN NGAYTHUCHIEN
		SELECT @GiaTien = SUM(isnull(tchdctp.GiaTien,0)), @SoluongThucChay = COUNT(tchdctp.HopDongChiTietREF) 
		FROM ThucChayHopDongChiTietPR tchdctp
		WHERE tchdctp.HopDongChiTietREF = @HopDongChiTietID
			AND 
			(
				((   CASE 
					   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN convert(date,tchdctp.CreatedAt)
					   ELSE convert(date,tchdctp.LastModifiedAt)
					END
				) <= @NgayThucHien) OR (tchdctp.RecordStatus = 1)
			)
			 AND convert(date,tchdctp.ThoiGianBatDau) >= @ThoiGianBDTinh
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
	    PRINT 'thanhtiendatinh:' + convert(nvarchar(50),convert(bigint,@ThanhTienDaTinh)) + ';SauCK:' + convert(nvarchar(50),convert(bigint,@GiaTienSauCK))
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
				--UPDATE ThucChayDaTinh
				--SET
				--	GiaTriThayDoi = @GiaTriThayDoiHT - @GiaTriThayDoiBF, -- Cho nay check ky HAIDH 29/10/2013
				--	LastModifiedAt = GETDATE()
				--WHERE HopDongChiTietREF = @HopDongChiTietID
				--AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
				SET @GiaTriThayDoi = @GiaTriThayDoiHT - @GiaTriThayDoiBF
				EXEC ThucChay_InsertThucTreoThayDoi_PR @HopDongChiTietID, @NgayThucHien, @GiaTriThayDoi
		
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
	    FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID 
	END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
END

--EXEC [ThucChay_CheckThucTreoThayDoi_PRByHopDong] '2013-12-31', '2013-01-01', 'QC010211'

```
