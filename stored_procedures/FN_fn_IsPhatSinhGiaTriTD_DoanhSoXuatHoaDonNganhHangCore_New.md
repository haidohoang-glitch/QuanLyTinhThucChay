# Function: `fn_IsPhatSinhGiaTriTD_DoanhSoXuatHoaDonNganhHangCore_New`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-12 10:46:58.123000
- **Ngày sửa cuối**: 2015-06-12 10:46:58.123000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@ThongTinHoaDonID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[fn_IsPhatSinhGiaTriTD_DoanhSoXuatHoaDonNganhHangCore_New]
(
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT,
	@ThongTinHoaDonID INT
	
)
RETURNS INT
BEGIN
	DECLARE @IsPhatSinhGiaTriTD INT SET @IsPhatSinhGiaTriTD =0
	DECLARE @v_count INT
	IF(SELECT COUNT(*) FROM DoanhSoXuatHoaDonNganhHangCore dsxhdnhc 
	   WHERE dsxhdnhc.HopDongID = @HopDongID
		AND dsxhdnhc.HopDongChiTietREF = @HopDongChiTietID
		AND dsxhdnhc.ThongTinHoaDonREF = @ThongTinHoaDonID) > 0
	SET @IsPhatSinhGiaTriTD = 1
SET @v_count =
	(
		SELECT COUNT(hdct.HopDongChiTietID) 
		FROM HopDongChiTiet hdct
		WHERE HDCT.DeletedStatus = 1
		AND hdct.HopDongChiTietID = @HopDongChiTietID
		AND Convert(date,hdct.LastModifiedAt) = Convert(Date,@NgayThucHien)
	) 
	BEGIN
		SET @IsPhatSinhGiaTriTD = 1
	END
	SET @v_count =
	   ( 
		SELECT COUNT(hd.HopDongID) FROM HopDong hd 
	    WHERE hd.HopDongID = @HopDongID 
	    AND hd.TrangThaiHopDong = 3
	    AND CONVERT(DATE,CreatedAt) <> CONVERT(DATE,LastModifiedAt)
	    AND LastModifiedAt = @NgayThucHien
	   )
	IF(@v_count >0)
	BEGIN
		SET @IsPhatSinhGiaTriTD = 1
	END
	SET @IsPhatSinhGiaTriTD = ISNULL(@IsPhatSinhGiaTriTD, 0)
		
	RETURN @IsPhatSinhGiaTriTD;
END


```
