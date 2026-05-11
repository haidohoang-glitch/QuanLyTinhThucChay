# Stored Procedure: `ThucChay_TheoDoiTheoChiTietHopDong_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-03 08:35:56.527000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.580000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC ThucChay_TheoDoiTheoChiTietHopDong 'QC1080713'

CREATE PROCEDURE [dbo].[ThucChay_TheoDoiTheoChiTietHopDong_BySQLJobs] 
	
AS
BEGIN
	
--Insert or Update HopDongChiTiet
EXEC [dbo].[ThucChay_TheoDoiTheoChiTietHopDong] 

--Update Trang Thai ThucChay va So Luong ThucChay HopDongChiTiet
DECLARE 
	@HopDongChiTietID int,@dtStart DATETIME, @dtEnd DATETIME
	,@ThucChayDenNgay DATETIME
	,@SoLuong FLOAT
	,@DonViTinh FLOAT
	
	SET @dtStart = (SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh)	
	SET @dtEnd = GETDATE()
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)	
	SET @dtStart = DATEADD(dd,1, @dtStart)
	
DECLARE Record_Cursor CURSOR FOR 
	SELECT A.HopDongChiTietREF,SoLuong,DonViTinh FROM dbo.ThucChayDaTinh A
	WHERE 
	A.NgayThucHien BETWEEN @dtStart AND @dtEnd

OPEN Record_Cursor

FETCH NEXT FROM Record_Cursor into @HopDongChiTietID,@SoLuong,@DonViTinh
 
WHILE @@FETCH_STATUS = 0
	BEGIN

SET @ThucChayDenNgay = (SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF=@HopDongChiTietID)

IF(EXISTS(SELECT * FROM ThucChayTheoDoiHopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID))
BEGIN
UPDATE [dbo].[ThucChayTheoDoiHopDongChiTiet]
   SET     
      [DotChayHopDongChiTiet] = dbo.GetDotChayHopDongChiTiet(@HopDongChiTietID)
      ,[NgayDaChay] = dbo.GetDotDaChayHopDongChiTiet(@HopDongChiTietID)
      ,[ThucChayDenNgay] = @ThucChayDenNgay
      ,[SoLuongDaChay] = dbo.ThucChay_GetSoLuongThucChayByHopDongChiTietID(@HopDongChiTietID)
      ,[SoLuongChuaChay] = dbo.ThucChay_GetSoLuongChuaChayTheoDonViTinh(@SoLuong,@DonViTinh,@HopDongChiTietID)
      ,[ThanhTienDaChay] = dbo.ThucChay_GetThanhTienThucChayByHopDongChiTietID(@HopDongChiTietID)
      ,[ThanhTienChuaChay] = dbo.ThucChay_GetThanhTienChuaChayByHopDongChiTietID(@HopDongChiTietID)

 WHERE [HopDongChiTietID] = @HopDongChiTietID 

UPDATE dbo.ThucChayTheoDoiHopDongChiTiet
SET TrangThaiHopDongChiTietThucChay = [dbo].[GetTrangThaiThucChayHopDongChiTiet](@HopDongChiTietID)
WHERE [HopDongChiTietID] = @HopDongChiTietID 

END

 FETCH NEXT FROM Record_Cursor into @HopDongChiTietID,@SoLuong,@DonViTinh
      	
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

	
END

```
