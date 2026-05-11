# Stored Procedure: `ThucChayDaTinh_Mobile_CheckHopDongThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-16 15:53:23.410000
- **Ngày sửa cuối**: 2014-11-19 12:24:55.023000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
-- EXEC ThucChayDaTinh_Mobile_CheckHopDongThayDoi '2014-06-10'

CREATE PROCEDURE [dbo].[ThucChayDaTinh_Mobile_CheckHopDongThayDoi]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    --DECLARE @NgayThucHien DATETIME
    DECLARE @HopDongID INT,
			@SoHopDong	NVARCHAR(50),
			@HopDongChiTietREF	INT,
			@SoLuongPhanBo		INT,
			@ThanhTienPhanBo	FLOAT
			
	DECLARE 
			@SoLuongPhanBoNew		INT,
			@ThanhTienPhanBoNew		FLOAT
			
	DECLARE @ThanhTienThucChayPhanBo	FLOAT
    
    DECLARE record_cursor CURSOR FOR
    SELECT hd.HopDongID, hd.SoHopDong, hdcttd.HopDongChiTietREF, hdcttd.SoLuong, hdcttd.ThanhTien
    FROM HopDong hd
		INNER JOIN HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK
		INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
			AND Convert(date,hdtd.NgayThayDoi) = @NgayThucHien
			AND hdcttd.DmSanPhamREF IN (342)
	 --AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdcttd.DonViTinh) = 1 --Đơn vị của hình thức CPD 
	WHERE hd.TrangThaiHopDong <> 3
	ORDER BY hd.SoHopDong 
	
	OPEN record_cursor
	
	FETCH NEXT FROM record_cursor INTO @HopDongID, @SoHopDong, @HopDongChiTietREF, @SoLuongPhanBo, @ThanhTienPhanBo
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		
		SELECT @ThanhTienPhanBoNew = ThanhTien
		FROM HopDongChiTiet AS hdct 
		WHERE hdct.HopDongChiTietID = @HopDongChiTietREF
		
		PRINT 'ThanhTienNew: ' + CONVERT(NVARCHAR(50), @ThanhTienPhanBoNew)
		PRINT 'ThanhTien: ' + CONVERT(NVARCHAR(50), @ThanhTienPhanBo)
		
		IF @ThanhTienPhanBo <> @ThanhTienPhanBoNew
		BEGIN
			IF EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinh AS tcdt WHERE tcdt.HopDongChiTietREF = @HopDongChiTietREF)
			BEGIN
				PRINT 'Co phan bo'
				SET @ThanhTienThucChayPhanBo = (
				SELECT SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0))
				FROM ThucChayDaTinh AS tcdt
				WHERE tcdt.DmSanPhamREF = 342
					AND tcdt.SoHopDong = @SoHopDong
					AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
					AND tcdt.TrangThaiHopDong <> 3	
					AND tcdt.NgayThucHien <= @NgayThucHien
				)
			END
			ELSE
			BEGIN
				PRINT 'Ko phan bo'
				SET @ThanhTienThucChayPhanBo = (
				SELECT SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0))
				FROM ThucChayDaTinh AS tcdt
				WHERE tcdt.DmSanPhamREF = 342
					AND tcdt.SoHopDong = @SoHopDong
					AND tcdt.TrangThaiHopDong <> 3	
					AND tcdt.NgayThucHien <= @NgayThucHien
				)
			END
		END
		
		FETCH NEXT FROM record_cursor INTO @HopDongID, @SoHopDong, @HopDongChiTietREF, @SoLuongPhanBo, @ThanhTienPhanBo
	END
	
	CLOSE record_cursor
	DEALLOCATE record_cursor
    
END

```
