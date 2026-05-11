# Stored Procedure: `ThucChayDaTinh_UpdateHopDongChiTietREFByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-01 13:53:34.690000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmHinhThucQuangCao` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-07-01
-- Description:	Update HopDongChiTietREF theo HopDongID doi voi nhung truong hop hop dong chi co duy nhat 1 phan bo
-- =============================================
-- 
-- EXEC ThucChayDaTinh_UpdateHopDongChiTietREFByHopDongID 375, 26
CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateHopDongChiTietREFByHopDongID] 
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF		INT,
	@DmHinhThucQuangCao	INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @HopDongID			INT,
			@SoHopDong			NVARCHAR(50),
			@HopDongChiTietREF	INT
			
    -- select nhung hop dong chi co duy nhat mot phan bo
    DECLARE record_cursor CURSOR FOR
    
	SELECT DISTINCT tcdt.HopDongID,tcdt.SoHopDong
	FROM ThucChayDaTinh AS tcdt
	WHERE tcdt.HopDongID IN 
	(
	SELECT 
		hdct.HopDongFK	
	FROM HopDongChiTiet AS hdct
	WHERE
		hdct.DmSanPhamREF = 375
		AND hdct.DeletedStatus = 0
		AND hdct.IsKhuyenMai <> 1
	GROUP BY hdct.HopDongFK
	HAVING COUNT(hdct.HopDongChiTietID) = 1
	)
	AND tcdt.DmSanPhamREF = @DmSanPhamREF 
	AND tcdt.DmHinhThucQuangCao = @DmHinhThucQuangCao
	AND tcdt.NgayThucHien >= '2014-01-01'
	AND tcdt.HopDongChiTietREF = 0;
	
	OPEN record_cursor
	
	FETCH NEXT FROM record_cursor INTO @HopDongID, @SoHopDong
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @HopDongChiTietREF = HopDongChiTietID
		FROM HopDongChiTiet AS hdct
		WHERE hdct.HopDongFK = @HopDongID
			AND hdct.IsKhuyenMai <> 1
			
		--PRINT 'HopDongID: ' + CONVERT(NVARCHAR(50),@HopDongID)
		IF @HopDongChiTietREF > 0
		BEGIN
			--SELECT * 
			--FROM ThucChayDaTinh AS tcdt
			--WHERE 
			--	HopDongID = @HopDongID
			--	AND SoHopDong = @SoHopDong
			--	AND DmSanPhamREF = @DmSanPhamREF
			--	AND DmHinhThucQuangCao = @DmHinhThucQuangCao
			--	AND HopDongChiTietREF = 0
			--	AND NgayThucHien >= '2014-01-01'
				
			UPDATE ThucChayDaTinh
			SET
				HopDongChiTietREF = @HopDongChiTietREF
			WHERE 
				HopDongID = @HopDongID
				AND SoHopDong = @SoHopDong
				AND DmSanPhamREF = @DmSanPhamREF
				AND DmHinhThucQuangCao = @DmHinhThucQuangCao
				AND HopDongChiTietREF = 0
				AND NgayThucHien >= '2014-01-01'
		END
		
		
		FETCH NEXT FROM record_cursor INTO @HopDongID, @SoHopDong
	END
	
	CLOSE record_cursor;
	DEALLOCATE record_cursor;
END

```
