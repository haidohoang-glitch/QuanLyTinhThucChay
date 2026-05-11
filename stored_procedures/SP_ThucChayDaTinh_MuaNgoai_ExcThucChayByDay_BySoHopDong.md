# Stored Procedure: `ThucChayDaTinh_MuaNgoai_ExcThucChayByDay_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-12 10:01:00.317000
- **Ngày sửa cuối**: 2016-11-24 18:12:51.283000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@startDate` | `datetime(8)` | No |
| `@endDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-13
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.ThucChayDaTinh_MuaNgoai_ExcThucChayByDay '2014-01-01', '2014-12-31'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_ExcThucChayByDay_BySoHopDong]
	-- Add the parameters for the stored procedure here
	@startDate	DATETIME,
	@endDate	DATETIME,
	@SoHopDong NVARCHAR(50)
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
	SELECT  A.HopDongChiTietID, Convert(date,A.LastModifiedAt)LastModifiedAt
	FROM HopDongChiTiet A
		INNER JOIN HopDong B ON B.HopDongID = A.HopDongFK
	WHERE B.TrangThaiHopDong <> 3
		AND A.DeletedStatus = 0
		AND A.CreatedAt >= @ngayGioiHanTinh
		-- doannv sua them dk 
		AND (A.DmLoaiREF = @dmHinhThucQuangCaoId OR A.DmLoaiBannerREF = 18)
		--AND A.ThanhTienThucChayMuaNgoaiTruocCK <> 0
		AND Convert(date,A.LastModifiedAt) BETWEEN @startDate AND @endDate
		--bo sung dk loai bot phan bo 
		--AND A.HopDongChiTietID NOT IN (SELECT HopDongChiTietID FROM dbo.MuaNgoaiChot2015)
		AND B.SoHopDong = @SoHopDong
		UNION ALL
		SELECT CONTRACT_DETAIL_ID HopDongChiTietID,LAST_MODIFIED_AT LastModifiedAt  FROM ThucChayMuaNgoaiChot
		INNER JOIN HopDong B ON B.HopDongID = ThucChayMuaNgoaiChot.contract_id
		WHERE 1=1
		AND Convert(date,LAST_MODIFIED_AT) BETWEEN @startDate AND @endDate
		AND B.SoHopDong = @SoHopDong
	)A

	SELECT A.HopDongChiTietID, Convert(date,A.LastModifiedAt)LastModifiedAt
	FROM HopDongChiTiet A
		INNER JOIN HopDong B ON B.HopDongID = A.HopDongFK		
	WHERE B.TrangThaiHopDong <> 3
		AND A.DeletedStatus = 0
		AND A.CreatedAt >= @ngayGioiHanTinh
		AND (A.DmLoaiREF = @dmHinhThucQuangCaoId OR A.DmLoaiBannerREF = 18)
		--AND A.ThanhTienThucChayMuaNgoaiTruocCK <> 0
		AND convert(date,A.LastModifiedAt) BETWEEN @startDate AND @endDate
		AND B.SoHopDong = @SoHopDong
	OPEN pb_cursor
	
	FETCH NEXT FROM pb_cursor INTO @phanBoId, @ngayThucHien
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--SELECT @phanBoId, @ngayThucHien
		EXEC dbo.ThucChayDaTinh_MuaNgoai_InsertThucChayDaTinh
			@ngayThucHien	= @ngayThucHien,
			@phanBoId		= @phanBoId
		
		FETCH NEXT FROM pb_cursor INTO @phanBoId, @ngayThucHien
	END
	
	CLOSE pb_cursor
	DEALLOCATE pb_cursor
    
    SELECT 1
END

```
