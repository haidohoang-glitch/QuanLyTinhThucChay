# Stored Procedure: `ThucChayDaTinh_UpdateSoLuongLechTreoHa`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-12 23:57:33.623000
- **Ngày sửa cuối**: 2015-04-08 15:49:12.240000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
-- EXEC dbo.ThucChayDaTinh_UpdateSoLuongLechTreoHa '2014-06-11','QC010614', 342

CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateSoLuongLechTreoHa] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@SoHopDong		NVARCHAR(50),
	@DmSanPhamREF	INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @SoLuongThucChay INT,
			@ThucChayDaTinhID	NVARCHAR(100)
			
	DECLARE lth_cursor CURSOR FOR
	SELECT tcdt.ThucChayDaTinhID, tcdt.SoLuongThucChay
	FROM ThucChayDaTinhMobile AS tcdt
	WHERE tcdt.NgayThucHien = @NgayThucHien
		AND tcdt.DmSanPhamREF = @DmSanPhamREF
		AND tcdt.SoLuongThucChay > 0 
		AND tcdt.ThanhTienSauTrietKhauThucChay = 0
	
	OPEN lth_cursor
	
	FETCH NEXT FROM lth_cursor INTO @ThucChayDaTinhID, @SoLuongThucChay
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT '@ThucChayDaTinhID: ' + CONVERT(NVARCHAR(50),@ThucChayDaTinhID);
		PRINT '@SoLuongThucChay: ' + CONVERT(NVARCHAR(50),@SoLuongThucChay);
		
		UPDATE  ThucChayDaTinhMobile
		SET SoLuongThucChay = 0,
			ThanhTienThucChayTruocTrietKhau = 0,
			GiaTriTrietKhauThucChay = 0,
			ThanhTienThucThu = 0,
			SoLuongThucChayLechTreoHa = @SoLuongThucChay
		WHERE
			ThucChayDaTinhID = @ThucChayDaTinhID
			AND NgayThucHien = @NgayThucHien
			AND SoHopDong = @SoHopDong
			AND DmSanPhamREF = @DmSanPhamREF;
		
		FETCH NEXT FROM lth_cursor INTO @ThucChayDaTinhID, @SoLuongThucChay;
	END
	
	CLOSE lth_cursor;
	DEALLOCATE lth_cursor;
END

```
