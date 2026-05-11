# Stored Procedure: `ThucChay_TinhLaiThucChayDaTinhBySoHopDongVaSP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-19 17:51:15.383000
- **Ngày sửa cuối**: 2014-11-19 12:17:00.353000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE PROCEDURE [dbo].[ThucChay_TinhLaiThucChayDaTinhBySoHopDongVaSP]
	@StartDate datetime,
	@EndDate DATETIME,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT
AS
BEGIN
	DECLARE @Count INT, @TypeProduct INT
	--1. Thuc hien xoa hop dong tren table thucchaydatinh theo SoHopDong, DmSanPhamREF, StartDate, EndDate
	DELETE FROM ThucChayDaTinh
	WHERE SoHopDong = @SoHopDong
	AND Convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
	AND DmSanPhamREF = @DmSanPhamREF
	--2. Thuc hien dieu huong goi store procedure chay tuong ung cho san pham.
	IF(@DmSanPhamREF IN (231,238,339,342,337,240,370)) --Thuc hien cho dm hinh thuc san pham CPM
		BEGIN
			SET @Count =
			(
				SELECT COUNT(*) FROM 
				(
					SELECT MAX(HDCT.DonGia) DonGiaMax, MIN(hdct.DonGia) DonGiaMin  
					FROM HopDong hd
					INNER JOIN HopDongChiTiet hdct ON HD.HopDongID = HDCT.HopDongFK
					WHERE HD.SoHopDong = Upper(@SoHopDong)
					AND HDCT.DmSanPhamREF = @DmSanPhamREF
					AND HDCT.DonGia >0
				)A
				WHERE A.DonGiaMax >A.DonGiaMin
			)
			SET @TypeProduct = dbo.GetDmSanPhamIDByTypeProductID(@DmSanPhamREF)
			EXEC [ThucChay_ExcInsertThucChayDaTinhBySoHopDong] @StartDate ,	@EndDate , @SoHopDong ,	@TypeProduct 
		END	
	ELSE IF(@DmSanPhamREF IN (140,228,241)) --Thuc hien cho dm hinh thuc san pham CPD
		BEGIN
			EXEC [ThucChay_InsertThucChayDaTinh_CPDBySoHopDong] @StartDate, @EndDate, @SoHopDong, @DmSanPhamREF
		END
	ELSE IF (@DmSanPhamREF IN (141,245,250)) -- Thuc hien cho dm hinh thuc san pham PR
		BEGIN
			EXEC [ThucChay_InsertThucChayDaTinh_PRBySoHopDong] @StartDate, @EndDate, @SoHopDong, @DmSanPhamREF
		END 
	
END


--EXEC [ThucChay_TinhLaiThucChayDaTinhBySoHopDongVaSP] '2013-05-06','2013-05-07', '', 3

```
