# Stored Procedure: `ThucChayDaTinh_MuaNgoai_ExcThucChayByDay_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-08 15:55:57.800000
- **Ngày sửa cuối**: 2017-11-08 15:55:57.800000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@startDate` | `datetime(8)` | No |
| `@endDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.ThucChayDaTinh_MuaNgoai_ExcThucChayByDay '2015-04-03', '2015-04-06'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_ExcThucChayByDay_test]
	-- Add the parameters for the stored procedure here
	@startDate	DATETIME,
	@endDate	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @ngayThucHien DATETIME,
			@ngayGioiHanTinh	DATETIME = '2013-01-01',
			@dmHinhThucQuangCaoId	INT		= 13 -- Hinh thuc mua ngoai
    DECLARE @phanBoId	INT
    
    SET @ngayThucHien = @startDate;
    
	DECLARE pb_cursor CURSOR FOR
	
	SELECT DISTINCT A.* FROM
	(
	SELECT  A.HopDongChiTietID, Convert(date,MN.NgaySuaThucChay)LastModifiedAt
	FROM HopDongChiTiet A
		INNER JOIN HopDong B ON B.HopDongID = A.HopDongFK
		INNER JOIN dbo.ThucChayMuaNgoai_HopDongChiTiet MN ON MN.HopDongChiTietREF = A.HopDongChiTietID
	WHERE B.TrangThaiHopDong <> 3
		AND A.DeletedStatus = 0
		AND A.CreatedAt >= @ngayGioiHanTinh
		-- doannv sua them dk 
		AND (A.DmLoaiREF = @dmHinhThucQuangCaoId OR A.DmLoaiBannerREF = 18)
		--AND A.ThanhTienThucChayMuaNgoaiTruocCK <> 0
		AND Convert(date,MN.NgaySuaThucChay) BETWEEN @startDate AND @endDate
		--bo sung dk loai bot phan bo 
		--AND A.HopDongChiTietID NOT IN (SELECT HopDongChiTietID FROM dbo.MuaNgoaiChot2015)

		UNION ALL

		SELECT CONTRACT_DETAIL_ID HopDongChiTietID,CONVERT(DATE,LAST_MODIFIED_AT) LastModifiedAt  FROM ThucChayMuaNgoaiChot
		WHERE 1=1
		AND Convert(date,LAST_MODIFIED_AT) BETWEEN @startDate AND @endDate
	)A
	WHERE 1=1 
	AND A.HopDongChiTietID NOT IN (SELECT DISTINCT hopdongchiTietID FROM MuaNgoaiChot_TinhBoSung_2016)
		
	OPEN pb_cursor
	
	FETCH NEXT FROM pb_cursor INTO @phanBoId, @ngayThucHien
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--SELECT @phanBoId, @ngayThucHien
		EXEC dbo.ThucChayDaTinh_MuaNgoai_InsertThucChayDaTinh_test
			@ngayThucHien	= @ngayThucHien,
			@phanBoId		= @phanBoId
		
		FETCH NEXT FROM pb_cursor INTO @phanBoId, @ngayThucHien
	END
	
	CLOSE pb_cursor
	DEALLOCATE pb_cursor
    
    SELECT 1
END

```
