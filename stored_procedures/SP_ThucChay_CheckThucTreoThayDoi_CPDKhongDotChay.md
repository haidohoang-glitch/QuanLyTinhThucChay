# Stored Procedure: `ThucChay_CheckThucTreoThayDoi_CPDKhongDotChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:27.133000
- **Ngày sửa cuối**: 2024-08-21 16:13:52.833000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql


CREATE PROCEDURE [dbo].[ThucChay_CheckThucTreoThayDoi_CPDKhongDotChay] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongREF INT, @SoHopDong NVARCHAR(50), @HopDongChiTietID INT, @SoLuong INT, @ThanhTien INT
	
	DECLARE Record_Cursor CURSOR  
	FOR
	    --1. Lấy thông tin phân bổ thay đổi thực treo
		SELECT DISTINCT A.HopDongREF, A.SoHopDong ,A.HopDongChiTietREF, A.SoLuong, A.ThanhTien
		FROM(
			   SELECT tchdctp.HopDongREF,
					  hd.SoHopDong,
					  tchdctp.HopDongChiTietREF,
					  hdct.SoLuong,
					  hdct.ThanhTien,
					  tchdctp.ThoiGianBatDau,
					  tchdctp.ThoiGianKetThuc,
					  (   CASE 
							   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN tchdctp.CreatedAt
							   ELSE tchdctp.LastModifiedAt
						  END
					  ) NgayThucHien
			   FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			   INNER JOIN ThucChayHopDongChiTiet tchdctp ON hdct.HopDongChiTietID = tchdctp.HopDongChiTietREF
				WHERE  tchdctp.ThoiGianBatDau IS NOT NULL
					  AND (   CASE 
								   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
								   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
							  END
						  ) = @NgayThucHien
	                  AND hdct.DmSanPhamREF IN (140,228,564,549)
	                  AND hdct.DeletedStatus = 0
	                  AND hd.DeletedStatus = 0
	                  AND tchdctp.DeletedStatus = 0
					  AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1	 --Đơn vị của hình thức CPD 
					  AND [dbo].[ThucChay_CheckSanPhamCPDKhongDotChay](hdct.HopDongChiTietID, @NgayThucHien) = 1
			)A
		ORDER BY
			   A.HopDongREF, A.HopDongChiTietREF
			   
	
	OPEN Record_Cursor
	
	--2. Đối trừ
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuong, @ThanhTien
	WHILE @@FETCH_STATUS = 0
	BEGIN
		EXEC ThucChay_CheckHopDongCoThayDoi_CPDKhongDotChay @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien,@SoLuong, @ThanhTien  
	    FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuong, @ThanhTien 
	END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
END



```
