# Stored Procedure: `ThucChay_TinhLaiSanPhamCPD_Booking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-09 13:03:01.837000
- **Ngày sửa cuối**: 2014-11-19 12:17:00.130000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_TinhLaiSanPhamCPD_Booking]
	-- Add the parameters for the stored procedure here

AS
BEGIN
DECLARE 
@NgayBatDau DATETIME, @NgayKetThuc DATETIME, @SoHopDong NVARCHAR(50), @DmSanPhamREF INT 

DECLARE Record_Cursor CURSOR FOR 
	SELECT NgayBatDau,NgayKetThuc,SoHopDong,

	(
	SELECT TOP 1 B.DmSanPhamREF FROM dbo.HopDong A
	INNER JOIN dbo.HopDongChiTiet B ON A.HopDongID = B.HopDongFK
	INNER JOIN dbo.DotChayHopDongChiTiet C ON C.HopDongChiTietREF = B.HopDongChiTietID
	INNER JOIN dbo.Booking D ON D.BookingID = C.BookingREF
	WHERE
	BookingID = BookingID 
	AND HinhThucSP = 1 

	) AS DmSanPhamREF

	--,BookingID, HinhThucSP,MaSanPham,[Status],LastModifiedAt 

	FROM dbo.Booking
	WHERE 
	BookingID IN 
	(
	44111,44116,44120,44118,44119,45702,45698,45699,
	46102,46103,46101,45814,45633,45634
	)
	--ORDER BY BookingID
	
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into 
	@NgayBatDau,@NgayKetThuc,@SoHopDong,@DmSanPhamREF
		
WHILE @@FETCH_STATUS = 0
BEGIN

SET @NgayKetThuc = DATEADD(dd,1,@NgayKetThuc)

EXEC [ThucChay_InsertThucChayDaTinh_CPDBySoHopDong] @NgayBatDau,@NgayKetThuc, @SoHopDong, @DmSanPhamREF

FETCH NEXT FROM Record_Cursor into 
	@NgayBatDau,@NgayKetThuc,@SoHopDong,@DmSanPhamREF

END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor
END

```
