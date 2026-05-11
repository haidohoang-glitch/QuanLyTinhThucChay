# Stored Procedure: `UpdateHopDongChiTietREFForThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-06 11:24:19.170000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.913000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerREF` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[UpdateHopDongChiTietREFForThucChay]
	-- Add the parameters for the stored procedure here
	@DmBannerREF nvarchar(50)
AS
BEGIN

Declare @HopDongChiTietREF nvarchar(50)

DECLARE Record_Cursor CURSOR FOR 
		SELECT A.HopDongChiTietREF FROM ThucChayHopDongChiTiet A
		WHERE 
		CONVERT(nvarchar(50),@DmBannerREF) IN (SELECT DmBannerREF FROM ThucChayHopDongChiTiet WHERE ThucChayHopDongChiTietID = A.ThucChayHopDongChiTietID)

OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into 
		@HopDongChiTietREF
		
WHILE @@FETCH_STATUS = 0
	BEGIN
			
	UPDATE ThucChay 
		SET HopDongChiTietREF = @HopDongChiTietREF,
			RecordStatus = 1
	WHERE 
		DmBannerREF = @DmBannerREF and		
		(HopDongChiTietREF is null or HopDongChiTietREF = '') and 
		(TongSoBaiViet <=0 or TongSoBaiViet is null) and 			
	(
		select	count(*) from dbo.DotChayHopDongChiTiet
		where 
			HopDongChiTietREF = @HopDongChiTietREF and
			NgayThucHien between ThoiGianBatDauBooking and ThoiGianKetThucBooking
	)	> 0
		

	FETCH NEXT FROM Record_Cursor into 
			@HopDongChiTietREF
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor		


END

```
