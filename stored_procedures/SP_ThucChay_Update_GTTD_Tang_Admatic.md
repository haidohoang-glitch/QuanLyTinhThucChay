# Stored Procedure: `ThucChay_Update_GTTD_Tang_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-09 17:10:55.533000
- **Ngày sửa cuối**: 2018-07-19 17:13:49.243000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongFK` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@GiaTriTang` | `float(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Update_GTTD_Tang_Admatic] 47330, 106061,100000,0.000034567, '2016-12-11'
CREATE  PROCEDURE [dbo].[ThucChay_Update_GTTD_Tang_Admatic] 
	@HopDongFK INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@GiaTriTang FLOAT
AS
BEGIN
	DECLARE @ThucChayDaTinhID NVARCHAR(400), @DmSanPhamREF INT, @DonGiaTheoDonViTinh FLOAT, @SoLuongThucChayLechTreoHa BIGINT
	, @ThanhTienLechTreoHa FLOAT, @ChietKhau FLOAT
	, @GiaTriThayDoi FLOAT, @SoLuongThayDoi INT
	DECLARE Cursor_hdct_tang CURSOR FOR

		SELECT ThucChayDaTinhID, DmSanPhamREF, DonGiaTheoDonVi
		, SoLuongThucChayLechTreoHa, ThanhTienLechTreoHa, ChietKhau
		FROM dbo.ThucChayDaTinh
		WHERE DmHinhThucQuangCao = 42
		AND HopDongChiTietREF = @HopDongChiTietID
		AND HopDongID = @HopDongFK
		AND NgayThucHien < @NgayThucHien
		AND ISNULL(SoLuongThucChayLechTreoHa,0) >0
		ORDER BY NgayThucHien DESC, CreatedAt DESC

	OPEN Cursor_hdct_tang
	FETCH NEXT FROM Cursor_hdct_tang INTO @ThucChayDaTinhID , @DmSanPhamREF 
	, @DonGiaTheoDonViTinh , @SoLuongThucChayLechTreoHa , @ThanhTienLechTreoHa, @ChietKhau
	WHILE @@FETCH_STATUS =0
	BEGIN
		--XAC DINH THANH TIEN LECH TREO HA SAU CHIET KHAU
		SET @ChietKhau = (SELECT TOP (1) ChietKhau FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
		IF(ISNULL(@ThanhTienLechTreoHa,0) <> 0)
		BEGIN
			SET @ThanhTienLechTreoHa = @ThanhTienLechTreoHa*(100-@ChietKhau)/100

			IF(@GiaTriTang > @ThanhTienLechTreoHa)
			BEGIN
				PRINT 'XAC DINH GIA TRI TANG CAN THEM VAO'
				SET @GiaTriTang = @GiaTriTang - @ThanhTienLechTreoHa
				SET @GiaTriThayDoi = @ThanhTienLechTreoHa
				SET @SoLuongThayDoi = @GiaTriThayDoi/(@DonGiaTheoDonViTinh * (100-@ChietKhau)/100)
			END
			ELSE
			BEGIN
				SET @GiaTriThayDoi = @GiaTriTang
				SET @GiaTriTang = 0
				SET @SoLuongThayDoi = @GiaTriThayDoi/(@DonGiaTheoDonViTinh * (100-@ChietKhau)/100)
				PRINT 'XAC DINH GIA TRI TANG CAN THEM VAO'
			END
		END
		PRINT 'XAC DINH BAN GHI TANG GIA GIA TRI'
		EXEC [dbo].[ThucChay_Insert_GTTD_Tang_ThucChayDaTinh_Admatic] 
			@ThucChayDaTinhID, --@ThucChayDaTinhID NVARCHAR(500),
			@NgayThucHien, --@NgayThucHien DATETIME,
			@HopDongFK, --@HopDongID INT, 
			@HopDongChiTietID, --@HopDongChiTietID INT,
			@DmSanPhamREF, --@DmSanPhamREF INT,
			@GiaTriThayDoi, --@GiaTriThucChayTang FLOAT,
			@SoLuongThayDoi --@SoLuongThucChayTang INT
		--THUC HIEN THOAT KHOI VONG LAP NEU DA DU TIEN
		IF(@GiaTriTang <= 0)
		BREAK --THOAT KHOI CON TRO

	FETCH NEXT FROM Cursor_hdct_tang INTO @ThucChayDaTinhID , @DmSanPhamREF 
	, @DonGiaTheoDonViTinh , @SoLuongThucChayLechTreoHa , @ThanhTienLechTreoHa, @ChietKhau
	END
	CLOSE Cursor_hdct_tang;
	DEALLOCATE Cursor_hdct_tang;
	
END

```
