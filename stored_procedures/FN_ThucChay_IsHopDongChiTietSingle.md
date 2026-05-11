# Function: `ThucChay_IsHopDongChiTietSingle`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-20 13:53:03.187000
- **Ngày sửa cuối**: 2016-11-18 12:58:58.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--select dbo.[ThucChay_IsHopDongChiTietSingle](88042)
CREATE FUNCTION [dbo].[ThucChay_IsHopDongChiTietSingle]
(
	-- Add the parameters for the function here
	@HopDongChiTietREF INT
)
RETURNS FLOAT
--1: Single
--0: Multi
---1: chua xac dinh
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result INT, @DmBannerID NVARCHAR(50), @AvgSoPhanBo FLOAT
	
	DECLARE @Table TABLE  (DmBannerID NVARCHAR(50), SoPhanBo INT)

	-- Add the T-SQL statements to compute the return value here
	SET @Result = 0
	
	--EXEC ThucChay_HopDongChiTietAndBannerByDmSanPhamREF 342
	
		DECLARE vendor_cursor CURSOR FOR 
			SELECT convert(nvarchar(50),DmBannerID)DmBannerID
			FROM ThucChayHopDongChiTietAndBanner a
			WHERE HopDongChiTietREF = @HopDongChiTietREF
			AND a.HopDongChiTietREF NOT IN (SELECT HopDongChiTietID
			                                  FROM HopDongChiTiet WHERE DmSanPhamREF = 342 AND DonViTinh= 'CPA')
			AND a.DeletedStatus <> 1
			ORDER BY a.DmBannerID
			
		OPEN vendor_cursor

		FETCH NEXT FROM vendor_cursor INTO @DmBannerID

		WHILE @@FETCH_STATUS = 0
		BEGIN
			 INSERT INTO @Table
		     SELECT DmBannerID, count(distinct HopDongChiTietREF) sophanbo
		      FROM  ThucChayHopDongChiTietAndBanner WHERE DmBannerID = @DmBannerID
		      AND DeletedStatus <> 1
			  AND HopDongChiTietREF  IN (SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 
			  AND DmSanPhamREF = 342 AND NOT (DmLoaiBannerREF = 17 OR DmLoaiNenTangREF = 8) )
	
		    GROUP BY DmBannerID 
		      
			FETCH NEXT FROM vendor_cursor INTO @DmBannerID
		END 
		CLOSE vendor_cursor;
		DEALLOCATE vendor_cursor;

	SET @AvgSoPhanBo = (SELECT AVG( CAST(sophanbo as FLOAT)) FROM @Table)
	SET @AvgSoPhanBo = ISNULL (@AvgSoPhanBo,0)
	IF @AvgSoPhanBo = 1 
		SET @Result = 1
	ELSE IF @AvgSoPhanBo < 1 
		SET @Result = -1
	ELSE IF @AvgSoPhanBo > 1
		SET @Result = 0
	

	-- Return the result of the function
	RETURN @Result

END

```
