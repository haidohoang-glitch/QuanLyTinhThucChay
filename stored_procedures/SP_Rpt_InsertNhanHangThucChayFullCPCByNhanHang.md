# Stored Procedure: `Rpt_InsertNhanHangThucChayFullCPCByNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:29.240000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.427000

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

CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHangThucChayFullCPCByNhanHang] 
	@DmNhanHangREF INT
AS
BEGIN
	DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT
	DECLARE @TenSanPham NVARCHAR(100), @DmSanPhamREF INT, @LstDmNhanHangREF NVARCHAR(200) 
    DECLARE @DoanhSoThucChay BIGINT, @TongThanhTienThucChayDT BIGINT
    DECLARE @TenNhanHang NVARCHAR(200), @SoluongHDCT INT, @SoLuongNhan INT, @TongThanhTienSP BIGINT
    DECLARE @TiLeDoanhSoKy FLOAT, @v_check_thucchay INT, @NgayThucHien DATETIME
    SET @Result = 0
    SET @SoluongHDCT = 1
    SET @TiLeDoanhSoKy = 0
    SET @v_check_thucchay = 0
	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT distinct a.*,b.NgayThucHien FROM 
	( 
	SELECT distinct hd.SoHopDong, hd.HopDongID ,hdct.HopDongChiTietID, hdct.TenSanPham, hdct.DmSanPhamREF, hdct.DanhSachNhanHangREF
			FROM hopdong hd 
			INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.TrangThaiHopDong <> 3
			AND hdct.DmSanPhamREF IN (144,299,337) 
			AND @DmNhanHangREF in 
			( 
				SELECT dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(hdct.DanhSachNhanHangREF,',') )
			)
	)a
	INNER JOIN
	(
		SELECT distinct tcdtahd.SoHopDong, tcdtahd.NgayThucHien
			FROM ThucChayDaTinhAdmarketHopDong tcdtahd
			WHERE 1= 1
			AND 
			(
				CASE WHEN tcdtahd.DmSanPhamREF = 5001 THEN 144
				WHEN tcdtahd.DmSanPhamREF = 5002 THEN 299
				WHEN  tcdtahd.DmSanPhamREF = 5003 THEN 337
				END
			) IN (144,299,337)
			--AND convert(date,tcdtahd.NgayThucHien) = @NgayThucHien	
	)b ON a.SoHopDong = b.SoHopDong	
	ORDER BY b.NgayThucHien
	
	OPEN Record_Cursor1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF, @NgayThucHien 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		BEGIN
			--Check HopDong co hopdongchitiet = 0 ?
			SELECT @SoLuongNhan = count(a.DmNhanHang) from
			(
				SELECT dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(@LstDmNhanHangREF,','))
			)a
			IF(@SoLuongNhan >0)
			BEGIN
				set @DoanhSoThucChay = 0
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
						
				SELECT @TongThanhTienThucChayDT = (sum(tcdtahd.TongTienThucChay)*@TiLeDoanhSoKy)/@SoLuongNhan
					FROM ThucChayDaTinhAdmarketHopDong tcdtahd
				WHERE tcdtahd.SoHopDong = @SoHopDong
				AND 
				(
					CASE WHEN tcdtahd.DmSanPhamREF = 5001 THEN 144
					WHEN tcdtahd.DmSanPhamREF = 5002 THEN 299
					WHEN  tcdtahd.DmSanPhamREF = 5003 THEN 337
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
		END
		
		FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF, @NgayThucHien
	END
	
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
	
	SELECT '1'
END

--EXEC [Rpt_InsertNhanHangThucChayFullCPC] '2013-12-31'

```
