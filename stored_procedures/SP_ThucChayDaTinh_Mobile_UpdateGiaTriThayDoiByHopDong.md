# Stored Procedure: `ThucChayDaTinh_Mobile_UpdateGiaTriThayDoiByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-29 11:48:27.470000
- **Ngày sửa cuối**: 2014-11-19 12:24:51.740000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC [dbo].[ThucChayDaTinh_Mobile_UpdateGiaTriThayDoiByHopDong] '2014-08-07', 'NB030514', 342
CREATE PROCEDURE [dbo].[ThucChayDaTinh_Mobile_UpdateGiaTriThayDoiByHopDong]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME,
	@SoHopDong		NVARCHAR(50),
	@DmSanPhamREF	INT
AS
BEGIN
	
	DECLARE	@HopDongREF INT,
			@HopDongChiTietID INT
			
	DECLARE @SoLuongDotChayHD INT,
			@ThanhTienHDCT FLOAT, 
			@DmWebsiteREF INT, 
			@TenWebsite		NVARCHAR(50),
			@TenSanPham		NVARCHAR(50) = 'Mobile'
			
	DECLARE 
			@count_HDCT INT, 
			@SoLuongThucChayBF INT
			
	DECLARE @SoLuongCurrent	INT,
			@DonGiaCurrent	INT,
			@ChietKhauCurrent	INT,
			@ThanhTienCurrent	FLOAT,
			@DeltaValue			FLOAT,
			@GiaTriThayDoiByWebsite	FLOAT
			
	DECLARE @SoLuongOld	INT,
			@DonGiaOld	INT,
			@ChietKhauOld	INT,
			@ThanhTienOld	FLOAT	
	
	DECLARE @NgayThayDoiMax	DATETIME,
			@HopDongThayDoiREFMax INT	
	
	DECLARE @Count INT,
			@ThucChayTheoSite FLOAT,
			@Tyle				FLOAT,
			@TongTienThucChay	FLOAT
		
	DECLARE @NoiDungLog			NVARCHAR(MAX),
			@GhiChu				NVARCHAR(MAX)
    
    DECLARE Record_Cursor CURSOR FOR 
	    
	SELECT distinct  hd.HopDongID, hd.SoHopDong, hdcttd.HopDongChiTietREF, hdcttd.DmSanPhamREF
	FROM HopDong hd
		INNER JOIN HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK AND hd.TrangThaiHopDong <> 3
		INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
			AND hdcttd.DmSanPhamREF = @DmSanPhamREF 
	WHERE CONVERT(Date,hdtd.NgayThayDoi) = @NgayThucHien
		AND hd.SoHopDong = @SoHopDong
	ORDER BY hd.SoHopDong	
	
	OPEN Record_Cursor
	
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT '@SoHopDong: ' + CONVERT(NVARCHAR(50), @SoHopDong);
		PRINT '@HopDongREF: ' + CONVERT(NVARCHAR(50), @HopDongREF);
		
		SELECT 
			@SoLuongCurrent = ISNULL(SUM(SoLuong),0),
			@DonGiaCurrent = ISNULL(SUM(hdct.DonGia),0),
			@ChietKhauCurrent = ISNULL(SUM(hdct.ChietKhau),0),
			@ThanhTienCurrent = ISNULL(SUM(hdct.ThanhTien),0)
		FROM HopDong hd
			INNER JOIN HopDongChiTiet AS hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE 
			hd.HopDongID = @HopDongREF
			AND hdct.HopDongChiTietID = @HopDongChiTietID
			AND hdct.DmSanPhamREF = @DmSanPhamREF
			AND hdct.DeletedStatus = 0
			AND hdct.IsKhuyenMai <> 1
			
		PRINT '@SoLuongCurrent: ' + CONVERT(NVARCHAR(50), @SoLuongCurrent);
		PRINT '@DonGiaCurrent: ' + CONVERT(NVARCHAR(50), @DonGiaCurrent);
		PRINT '@ChietKhauCurrent: ' + CONVERT(NVARCHAR(50), @ChietKhauCurrent);
		PRINT '@ThanhTienCurrent: ' + CONVERT(NVARCHAR(50), @ThanhTienCurrent);
			
		SELECT 
			@NgayThayDoiMax = convert(date,MAX(B.NgayThayDoi)),
			@HopDongThayDoiREFMax = MAX(B.HopDongThayDoiID)
		FROM dbo.HopDongChiTietThayDoi A
		INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
		WHERE 
			A.DeletedStatus <> 1 AND 
			B.DeletedStatus <> 1 AND
			A.HopDongFK = @HopDongREF
			AND A.DmSanPhamREF = @DmSanPhamREF
			AND A.IsKhuyenMai <> 1
			
		PRINT '@NgayThayDoiMax: ' + CONVERT(NVARCHAR(50), @NgayThayDoiMax);
		PRINT '@HopDongThayDoiREFMax: ' + CONVERT(NVARCHAR(50), @HopDongThayDoiREFMax);
		
		SELECT 
			@SoLuongOld = ISNULL(SUM(SoLuong),0),
			@DonGiaOld = ISNULL(SUM(A.DonGia),0),
			@ChietKhauOld = ISNULL(SUM(A.ChietKhau),0),
			@ThanhTienOld = ISNULL(SUM(A.ThanhTien),0)
		FROM dbo.HopDongChiTietThayDoi A
		WHERE 
			A.DeletedStatus <> 1 AND 
			A.HopDongFK = @HopDongREF
			AND A.DmSanPhamREF = @DmSanPhamREF
			AND A.IsKhuyenMai <> 1
			AND A.HopDongThayDoiREF = @HopDongThayDoiREFMax
			
		PRINT '@SoLuongOld: ' + CONVERT(NVARCHAR(50), @SoLuongOld);
		PRINT '@DonGiaOld: ' + CONVERT(NVARCHAR(50), @DonGiaOld);
		PRINT '@ChietKhauOld: ' + CONVERT(NVARCHAR(50), @ChietKhauOld);
		PRINT '@ThanhTienOld: ' + CONVERT(NVARCHAR(50), @ThanhTienOld);
		
		IF @ThanhTienCurrent <> @ThanhTienOld
		BEGIN
			PRINT 'Change***';
					
			SET @NoiDungLog = N'Giá trị thay đổi: - PhanBoID: ' + CONVERT(NVARCHAR(50),@HopDongChiTietID) + ' - ';
			SET @GhiChu		= '';
			
			IF @SoLuongOld <> @SoLuongCurrent
				SET @NoiDungLog += N'Thay đổi số lượng - Trước: ' + CONVERT(NVARCHAR(50),@SoLuongOld) + N' - Sau: ' + CONVERT(NVARCHAR(50),@SoLuongCurrent) + '; ';
				
			IF @DonGiaOld <> @DonGiaCurrent 
				SET @NoiDungLog += N'Thay đổi đơn giá - Trước: ' + CONVERT(NVARCHAR(50),@DonGiaOld) + N' - Sau: ' + CONVERT(NVARCHAR(50),@DonGiaCurrent) + '; ';
				
			IF @ChietKhauOld <> @ChietKhauCurrent
				SET @NoiDungLog += N'Thay đổi chiết khấu - Trước: ' + CONVERT(NVARCHAR(50),@ChietKhauOld) + N' - Sau: ' + CONVERT(NVARCHAR(50),@ChietKhauCurrent) + '; ';
				
			PRINT 'Log: ' + @NoiDungLog;
			--EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
			--			@HopDongREF
			--			,@SoHopDong
			--			,@HopDongChiTietID
			--			,@DmSanPhamREF
			--			,@DmWebsiteREF
			--			,@NgayThucHien
			--			,@DeltaValue
			--			,@DonGiaCurrent
			--			,@SoLuongCurrent
			--			,@DonGiaOld
			--			,@SoLuongOld
			--			,@NoiDungLog
			--			,'HopDongChiTiet_Mobile'
			--			,@GhiChu
			
			SET @DeltaValue = @ThanhTienCurrent - @ThanhTienOld;
			PRINT '@DeltaValue: ' + CONVERT(NVARCHAR(50), @DeltaValue);
			
			IF EXISTS(SELECT HopDongChiTietREF 
			          FROM ThucChayDaTinh AS tcdt 
			          WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID 
						AND (ThanhTienKM = 0 OR IsKhuyenMai <> 1))
			BEGIN
				PRINT 'Ton tai phan bo Id: 1';
				PRINT 'Phan bo Id: ' + CONVERT(NVARCHAR(50), @HopDongChiTietID);
				SELECT 
					@Count = COUNT(DISTINCT DmWebsiteREF),
					@TongTienThucChay = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
				FROM ThucChayDaTinh AS tcdt
				WHERE tcdt.HopDongID = @HopDongREF 
					AND tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND tcdt.NgayThucHien <= @NgayThucHien;

				PRINT 'SoLuongWebsite: ' + CONVERT(NVARCHAR(50),@Count);						
				PRINT '@TongTienThucChay: ' + CONVERT(NVARCHAR(50),@TongTienThucChay);
			END
			ELSE
			BEGIN
				PRINT 'Ton tai phan bo Id: 0';
				SELECT 
					@Count = COUNT(DISTINCT DmWebsiteREF),
					@TongTienThucChay = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
				FROM ThucChayDaTinh AS tcdt
				WHERE tcdt.HopDongID = @HopDongREF 
					AND tcdt.DmSanPhamREF = @DmSanPhamREF
					AND (tcdt.ThanhTienKM = 0 OR tcdt.IsKhuyenMai <> 1)
					AND tcdt.NgayThucHien <= @NgayThucHien;

				PRINT 'SoLuongWebsite: ' + CONVERT(NVARCHAR(50),@Count);						
				PRINT '@TongTienThucChay: ' + CONVERT(NVARCHAR(50),@TongTienThucChay);
			END
		END
				
		FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF
	END 
	
	CLOSE Record_Cursor;
	DEALLOCATE Record_Cursor;
END

```
