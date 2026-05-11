# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinhCPMByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-07 09:41:40.690000
- **Ngày sửa cuối**: 2017-05-16 17:26:50.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinhCPMByNgayThucHien] '2014-06-12','SH020614',	0,	370
	
CREATE  PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinhCPMByNgayThucHien] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@DmSanPhamID INT
AS
BEGIN
	DECLARE	@HopDongREF INT, @MinDate DATETIME, @SoLuongLechTreoHa BIGINT, @SoLuongThucChayDuocTinh BIGINT
	DECLARE @SoLuongThucChay BigINT, @SoLuongHopDong BigINT , @HopDongChiTietREF INT, @TTChenhLechDuocTinh BIGINT
	DECLARE @count_HDCT INT, @DonGiaTheoDonViTinh FLOAT, @TTThucChaySauChietKhau INT, @GiaTriThayDoi INT

	
	DECLARE Record_Cursor CURSOR FOR 
	SELECT distinct  hd.HopDongID, hd.SoHopDong,  hdct.DmSanPhamREF, hdct.HopDongChiTietID
	FROM HopDong hd
	INNER JOIN  HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE 
	(	
		CASE WHEN @HopDongChiTietID = 0 THEN 0
		ELSE hdct.HopDongChiTietID
		END
	) = @HopDongChiTietID 
	AND hdct.DmSanPhamREF = @DmSanPhamID
	AND @SoHopDong = hd.SoHopDong
	AND hdct.DeletedStatus = 0
	AND hd.DeletedStatus = 0
	AND hd.TrangThaiHopDong != 3
	AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh)  = 3
	ORDER BY hd.SoHopDong	

	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong,  @DmSanPhamID, @HopDongChiTietREF
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @count_HDCT = 0
		SET @SoLuongLechTreoHa = 0
		SET @SoLuongThucChayDuocTinh = 0
		SET @SoLuongThucChay = 0
		SET @SoLuongHopDong = 0
		SET @DonGiaTheoDonViTinh = 0
		SET @TTThucChaySauChietKhau = 0
		SET @GiaTriThayDoi = 0
		SET @TTChenhLechDuocTinh = 0
		--XAC DINH PHUONG PHAP TINH THUC CHAY
		SELECT @count_HDCT = COUNT(tcdt.HopDongChiTietREF) FROM ThucChayDaTinh tcdt
		WHERE tcdt.HopDongChiTietREF = 0
		AND tcdt.DmSanPhamREF = @DmSanPhamID
		AND tcdt.HopDongID = @HopDongREF
		
		IF(@count_HDCT  = 0)--T/c tinh theo phuong phap thuc treo
		BEGIN
			PRINT 'Tinh theo pp thuc treo'
			EXEC [ThucChay_UpdateGiaTriTDTCCPMThucTreoByNgay] @NgayThucHien ,@HopDongREF ,	@DmSanPhamID ,	@HopDongChiTietREF
		END
		ELSE--T/c tinh theo phuong phap san pham
		BEGIN
			PRINT 'Tinh theo pp san pham'
			EXEC [ThucChay_UpdateGiaTriTDTCCPMSanPhamByNgay] 	@NgayThucHien,	@HopDongREF,	@DmSanPhamID 
			BREAK;
		END
						
	FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @DmSanPhamID, @HopDongChiTietREF
	END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	SELECT 2
END

```
