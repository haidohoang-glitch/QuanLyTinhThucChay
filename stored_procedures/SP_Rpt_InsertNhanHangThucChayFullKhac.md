# Stored Procedure: `Rpt_InsertNhanHangThucChayFullKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:34.863000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.393000

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

CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHangThucChayFullKhac] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT
	DECLARE @TenSanPham NVARCHAR(100), @DmSanPhamREF INT, @ThanhTienThucChay BIGINT , @LstDmNhanHangREF NVARCHAR(200) 
    DECLARE @DoanhSoThucChay BIGINT, @CheckHopDongChiTietTcID INT, @TongThanhTienThucChayDT BIGINT
    DECLARE @DmNhanHangREF INT, @TenNhanHang NVARCHAR(200), @SoluongHDCT INT, @SoLuongNhan INT, @TongThanhTienSP BIGINT
    DECLARE @TiLeDoanhSoKy FLOAT
    SET @Result = 0
    SET @SoluongHDCT = 1
    SET @TiLeDoanhSoKy = 0
	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT a.* from
	(
			SELECT distinct hd.SoHopDong, hd.HopDongID ,hdct.HopDongChiTietID, hdct.TenSanPham, hdct.DmSanPhamREF, hdct.DanhSachNhanHangREF
			FROM hopdong hd 
			INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.TrangThaiHopDong <> 3
			AND hdct.DmSanPhamREF IN (381,305,342,239,253,252,251,243,242,271,385,247,306,423,284,437,375,245,531)
	)a
	INNER JOIN 
	(
		select DISTINCT tcdt.SoHopDong from ThucChayDaTinh tcdt
		WHERE 1= 1 
		and tcdt.DmSanPhamREF IN (381,305,342,239,253,252,251,243,242,271,385,247,306,423,284,437,5004,245,531) 
		AND convert(date,tcdt.NgayThucHien) = @NgayThucHien  
	) tcdt ON tcdt.SoHopDong = a.SoHopDong
	 
	OPEN Record_Cursor1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--Check HopDong co hopdongchitiet = 0 ?
		set @TiLeDoanhSoKy = 0
		set @DoanhSoThucChay = 0
		SET @TongThanhTienThucChayDT = 0
		SELECT @SoLuongNhan = count(a.DmNhanHang) from
		(
			SELECT dbo.FormatString(item) DmNhanHang
			FROM dbo.ArrayToTable(dbo.Array(@LstDmNhanHangREF,','))
		)a
		IF(@SoLuongNhan >0)
		BEGIN
			DECLARE Record_Cursor2 CURSOR FOR
			SELECT dbo.FormatString(item) DmNhanHang
			FROM dbo.ArrayToTable(dbo.Array(@LstDmNhanHangREF,','))
			OPEN Record_Cursor2
			FETCH NEXT FROM Record_Cursor2 INTO @DmNhanHangREF
			WHILE @@FETCH_STATUS = 0
			BEGIN
				SET @TenNhanHang = 
				(
					SELECT dnh.TenNhanHang FROM DmNhanHang dnh
					WHERE dnh.DmNhanHangID = @DmNhanHangREF	
				)
				SET @TenNhanHang = ISNULL(@TenNhanHang,'')
				SET @SoluongHDCT =
				(
					SELECT count(distinct hdct.HopDongChiTietID)
					FROM hopdong hd 
					INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
					WHERE hd.TrangThaiHopDong <> 3
					AND hd.HopDongID = @HopDongFK
					AND hdct.DmSanPhamREF = @DmSanPhamREF
				)
				IF(@SoluongHDCT >0)
				BEGIN
					SET @TongThanhTienSP =
					(
						SELECT SUM(hdct.ThanhTien) FROM HopDongChiTiet hdct
						WHERE hdct.HopDongFK = @HopDongFK
						AND hdct.DmSanPhamREF = @DmSanPhamREF
						AND hdct.DeletedStatus = 0	
					)
					SET @TiLeDoanhSoKy = 
					(
						SELECT
						(
							CASE WHEN @TongThanhTienSP = 0 THEN 0
							ELSE (convert(float,hdct.ThanhTien)/convert(float,@TongThanhTienSP))
							END 
						) TileDoanhSo
						FROM HopDongChiTiet hdct
						WHERE hdct.HopDongChiTietID = @HopDongChiTietID	
						AND hdct.DeletedStatus = 0
					)
					SET @TiLeDoanhSoKy = ISNULL(@TiLeDoanhSoKy,0)
				END
				SELECT @TongThanhTienThucChayDT = (sum(isnull(tcdtahd.ThanhTienSauTrietKhauThucChay,0)  + isnull(tcdtahd.GiaTriThayDoi,0))*@TiLeDoanhSoKy)/@SoLuongNhan
				FROM ThucChayDaTinh tcdtahd
				WHERE tcdtahd.SoHopDong = @SoHopDong
				AND 
				(
					CASE WHEN tcdtahd.DmSanPhamREF = 5004 THEN 375 -- Boxapp self serving
					ELSE tcdtahd.DmSanPhamREF
					END
				) = @DmSanPhamREF
				AND convert(date,tcdtahd.NgayThucHien) = @NgayThucHien
						
				SET @DoanhSoThucChay = ISNULL(@TongThanhTienThucChayDT,0)
				IF(@DoanhSoThucChay <> 0)
				BEGIN
					INSERT INTO [dbo].[RptNhanHangThucChayFull]
					  (
						[DmNhanHangREF],[TenNhanHang],[HopDongREF],[SoHopDong],[HopDongChiTietREF],[DmSanPhamREF],
						[TenSanPham],[DmKenhREF],[Kenh],[NgayThucHien], [DoanhSoThucChay],[CreatedBy],[CreatedAt],[RecordStatus]
					  )
					VALUES
					  (
						@DmNhanHangREF, @TenNhanHang, @HopDongFK, @SoHopDong, @HopDongChiTietID, @DmSanPhamREF, @TenSanPham,0,'',
						@NgayThucHien,  @DoanhSoThucChay, '', GETDATE(), 0
					  )	
				END	
				FETCH NEXT FROM Record_Cursor2 INTO @DmNhanHangREF
			END
			CLOSE Record_Cursor2
			DEALLOCATE Record_Cursor2
		END
		FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF
	END
	
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
		
		 
	SELECT '1'
END

--EXEC [Rpt_InsertNhanHangThucChayFullKhac] '2013-12-31'

```
