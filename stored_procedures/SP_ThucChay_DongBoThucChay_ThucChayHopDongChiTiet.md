# Stored Procedure: `ThucChay_DongBoThucChay_ThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:14:53.657000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.430000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_DongBoThucChay_ThucChayHopDongChiTiet]
	-- Add the parameters for the stored procedure here

AS
BEGIN


--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @DmBannerREF int, @HopDongChiTietREF nvarchar(50)

DECLARE Record_Cursor CURSOR FOR 

	SELECT DISTINCT DmBannerREF FROM dbo.ThucChay
	WHERE 
	HopDongChiTietREF IS NULL AND 
	DmBannerREF IS NOT NULL And
	DeletedStatus <> 1 and
	(HopDongChiTietREF is null or HopDongChiTietREF = '')

	
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into 
		@DmBannerREF
		
WHILE @@FETCH_STATUS = 0
	BEGIN
	SET @HopDongChiTietREF = (
							SELECT TOP 1 A. HopDongChiTietREF FROM ThucChayHopDongChiTiet A
							WHERE 
							CONVERT(nvarchar(50),@DmBannerREF) IN (SELECT DmBannerREF FROM ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID = A.ThucChayHopDongChiTietID)
							 )
	
	
	UPDATE ThucChay 
		SET HopDongChiTietREF = @HopDongChiTietREF,
			RecordStatus = 2
	WHERE DmBannerREF = @DmBannerREF and 
	(HopDongChiTietREF is null or HopDongChiTietREF = '') and 
	(TongSoBaiViet <=0 or TongSoBaiViet is null)

	FETCH NEXT FROM Record_Cursor into  
			@DmBannerREF

END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

--Update HopDongChiTietREF Tu Viec Ket Noi Boooking & Phan Bo Hop Dong Thong Quan Dot Chay
update ThucChay set 
HopDongChiTietREF = dbo.ThucChay_GetHopDongChiTietID(HopDongChiTietREF, DanhsachDmBookingREF,SoHopDong),
RecordStatus = 3  
where 
(HopDongChiTietREF is null or HopDongChiTietREF = '') and 
(TongSoBaiViet <=0 or TongSoBaiViet is null)

END

```
