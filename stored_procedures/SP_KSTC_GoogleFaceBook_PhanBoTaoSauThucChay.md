# Stored Procedure: `KSTC_GoogleFaceBook_PhanBoTaoSauThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:23.670000
- **Ngày sửa cuối**: 2015-04-08 10:00:23.670000

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
CREATE PROCEDURE [dbo].[KSTC_GoogleFaceBook_PhanBoTaoSauThucChay] 
	@NgayThucHien DATETIME
	AS
BEGIN
DECLARE @SoHopDong NVARCHAR(50), @HopDongChiTietID INT, @TK_AdMarketList NVARCHAR(max), @TK_AdMarket NVARCHAR(50),@CreatedAt DATETIME
DECLARE @Table TABLE (
	HopDongChiTietID INT,
	TK_Admarket NVARCHAR(50),
	CreatedAt DATETIME
	)


DECLARE vendor_cursor CURSOR FOR 
SELECT hd.SoHopDong, hdct.HopDongChiTietID, hdct.TK_AdMarket
	  FROM HopDong hd INNER JOIN HopDongChiTiet hdct
	ON hd.HopDongID = hdct.HopDongFK 
	WHERE hdct.DmSanPhamREF IN (306,423)
	AND hdct.DeletedStatus <> 1
	AND hd.TrangThaiHopDong <> 3
	AND hd.NgayDanhSoHopDong >='2014-01-01'

OPEN vendor_cursor

FETCH NEXT FROM vendor_cursor INTO @SoHopDong, @HopDongChiTietID, @TK_AdMarketList

WHILE @@FETCH_STATUS = 0
BEGIN
	DECLARE TK_cursor CURSOR FOR 
	SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(@TK_AdMarketList,','))
	ORDER BY item;

	OPEN TK_cursor

	FETCH NEXT FROM TK_cursor INTO @TK_AdMarket

	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @CreatedAt = CreatedAt 
		FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID 
		
		IF @CreatedAt > dateadd(d,1,@NgayThucHien) 
	    INSERT INTO @Table
		SELECT @HopDongChiTietID, @TK_AdMarket, @CreatedAt
		FETCH NEXT FROM TK_cursor INTO @TK_AdMarket
	END 
	CLOSE TK_cursor;
	DEALLOCATE TK_cursor;
    FETCH NEXT FROM vendor_cursor INTO @SoHopDong, @HopDongChiTietID, @TK_AdMarketList
END 
CLOSE vendor_cursor;
DEALLOCATE vendor_cursor;
	
SELECT * FROM @Table	
	 
END

```
