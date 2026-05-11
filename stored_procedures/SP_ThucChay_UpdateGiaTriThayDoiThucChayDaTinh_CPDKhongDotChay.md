# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-01 14:35:30.430000
- **Ngày sửa cuối**: 2024-08-21 16:04:33.307000

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
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDKhongDotChay] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE	@HopDongREF INT,@SoHopDong NVARCHAR(50),@HopDongChiTietID INT
	DECLARE @SoLuongDotChayHD INT,@ThanhTienHDCT FLOAT, @count_hdct INT

	PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
	set @count_hdct = 0
	DECLARE Record_Cursor CURSOR FOR 

    --1. Xác định phân bổ có thay đổi thông tin đánh số
	SELECT hd.HopDongID, hd.SoHopDong, hdcttd.HopDongChiTietREF, hdcttd.SoLuong, hdcttd.ThanhTien
	  FROM HopDong hd
	INNER JOIN HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK
	INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
	AND Convert(date,hdtd.NgayThayDoi) = @NgayThucHien
	AND hdcttd.DmSanPhamREF IN (140,228,564,549)
	AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdcttd.DonViTinh) = 1	  
	AND [dbo].[ThucChay_CheckSanPhamCPDKhongDotChay](hdcttd.HopDongChiTietREF, @NgayThucHien) = 1
	WHERE hd.TrangThaiHopDong <> 3
	AND hdcttd.DmLoaiREF <> 13  
	ORDER BY hd.SoHopDong	
	
	OPEN Record_Cursor

	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
	
	--2. Đối trừ
	WHILE @@FETCH_STATUS = 0
		BEGIN
			SET @count_hdct = 
			(
				SELECT count(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID
				AND hdct.DeletedStatus = 0	
			)
			-- TH phân bổ có thay đổi
			IF(@count_hdct > 0) 
				EXEC ThucChay_CheckHopDongCoThayDoi_CPDKhongDotChay @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien ,@SoLuongDotChayHD ,@ThanhTienHDCT
			-- TH phân bổ bị xóa
			ELSE
				EXEC ThucChay_CheckHopDongXoaPhanBo_CPDKhongDotChay @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien ,@SoLuongDotChayHD ,@ThanhTienHDCT
			set @count_hdct = 0				
		FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
		END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	SELECT 2
END



```
