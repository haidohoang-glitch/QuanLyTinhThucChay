# Stored Procedure: `Rpt_InsertNhanHangThucChayFullKhacByNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:32.580000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.360000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHangThucChayFullKhacByNhanHang] 
	@DmNhanHangREF INT
AS
BEGIN
	DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT
	DECLARE @TenSanPham NVARCHAR(100), @DmSanPhamREF INT, @LstDmNhanHangREF NVARCHAR(200) 
    DECLARE @DoanhSoThucChay BIGINT, @TongThanhTienThucChayDT BIGINT
    DECLARE @TenNhanHang NVARCHAR(200), @SoluongHDCT INT, @SoLuongNhan INT, @TongThanhTienSP BIGINT
    DECLARE @TiLeDoanhSoKy FLOAT, @NgayThucHien DATETIME
    SET @Result = 0
    SET @SoluongHDCT = 1
    SET @TiLeDoanhSoKy = 0
	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT DISTINCT a.*, tcdt.NgayThucHien from
	(
			SELECT distinct hd.SoHopDong, hd.HopDongID ,hdct.HopDongChiTietID, hdct.TenSanPham, hdct.DmSanPhamREF, hdct.DanhSachNhanHangREF
			FROM hopdong hd 
			INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.TrangThaiHopDong <> 3
			--AND hdct.DmSanPhamREF IN (381,305,342,239,253,252,251,243,242,271,385,247,306,423,284,437,375,245,531)
			AND hdct.DmSanPhamREF = 375
			AND @DmNhanHangREF in 
			( 
				SELECT dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(hdct.DanhSachNhanHangREF,',') )
			)
	)a
	INNER JOIN 
	(
		select DISTINCT tcdt.SoHopDong,tcdt.NgayThucHien
		  from ThucChayDaTinh tcdt
		WHERE 1= 1 
		--tcdt.DmSanPhamREF IN (381,305,342,239,253,252,251,243,242,271,385,247,306,423,284,437,375,245,531) 
		--AND convert(date,tcdt.NgayThucHien) = @NgayThucHien  
	) tcdt ON tcdt.SoHopDong = a.SoHopDong
	 
	OPEN Record_Cursor1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF, @NgayThucHien
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
				PRINT @TongThanhTienSP
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
		END
		FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF, @NgayThucHien
	END
	
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
		
	SELECT '1'
END

--EXEC [dbo].[Rpt_InsertNhanHangThucChayFullKhacByNhanHang]  1251

```
