# Stored Procedure: `ThucChay_Booking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-13 20:48:49.197000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.970000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_Booking]
	-- Add the parameters for the stored procedure here

AS
BEGIN


--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @ThucChayID nvarchar(50), @DanhsachDmBookingREF nvarchar(4000), @BookingID int


DECLARE Record_Cursor CURSOR FOR 
	SELECT ThucChayID,DanhsachDmBookingREF FROM dbo.ThucChay

	
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into 
		@ThucChayID,@DanhsachDmBookingREF
		
WHILE @@FETCH_STATUS = 0
	BEGIN

	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT Convert(int,dbo.FormatString(item)) FROM dbo.ArrayToTable(dbo.Array(@DanhsachDmBookingREF,','))
	OPEN Record_Cursor1
	FETCH NEXT FROM Record_Cursor1 into @BookingID
	WHILE @@FETCH_STATUS = 0
		Begin
		Insert into dbo.ThucChayAndBooKing select @ThucChayID,@BookingID
		FETCH NEXT FROM Record_Cursor1 into @BookingID
		end
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
	
FETCH NEXT FROM Record_Cursor into 
		@ThucChayID,@DanhsachDmBookingREF

END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor


END

```
