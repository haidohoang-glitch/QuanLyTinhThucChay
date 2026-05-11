# Stored Procedure: `Rpt_InsertNhanHangThucChayFullByNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:32.370000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.497000

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

CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHangThucChayFullByNhanHang] 
	@DmNhanHangREF INT
AS
BEGIN
	DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT
	DECLARE @TenSanPham NVARCHAR(100), @DmSanPhamREF INT, @LstDmNhanHangREF NVARCHAR(200) 
    DECLARE @DoanhSoThucChay BIGINT, @CheckHopDongChiTietTcID INT, @TongThanhTienThucChayDT BIGINT
    DECLARE @TenNhanHang NVARCHAR(200), @SoluongHDCT INT, @SoLuongNhan INT
    DECLARE @TongThanhTienSP BIGINT, @TiLeDoanhSoKy FLOAT, @v_count_checkthucchay INT, @NgayThucHien DATETIME
    SET @Result = 0
    SET @SoluongHDCT = 1
    SET @v_count_checkthucchay = 0
	--PRINT @DmNhanHangREF
	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT distinct a.*, tcdt.NgayThucHien from
	(
			SELECT distinct hd.SoHopDong, hd.HopDongID ,hdct.HopDongChiTietID, hdct.TenSanPham, hdct.DmSanPhamREF, hdct.DanhSachNhanHangREF
			FROM hopdong hd 
			INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			WHERE hd.TrangThaiHopDong <> 3
			--AND hdct.DmSanPhamREF NOT IN (381,305,342,239,253,252,251,243,242,271,385,247,306,423,284,437,375,245,531)
			AND @DmNhanHangREF in 
			( 
				SELECT dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(hdct.DanhSachNhanHangREF,',') )
			)
	)a
	INNER JOIN 
	(
		select DISTINCT tcdt.SoHopDong, tcdt.NgayThucHien from ThucChayDaTinh tcdt
		WHERE 1 = 1 
		--AND tcdt.DmSanPhamREF NOT IN (381,305,342,239,253,252,251,243,242,271,385,247,306,423,284,437,375,245,531)
		--AND convert(date,tcdt.NgayThucHien) = @NgayThucHien  
	) tcdt ON tcdt.SoHopDong = a.SoHopDong
	ORDER BY tcdt.NgayThucHien
	 
	OPEN Record_Cursor1
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF, @LstDmNhanHangREF, @NgayThucHien
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--Check hop dong, san pham co thuc chay ngay
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
				SELECT @CheckHopDongChiTietTcID = COUNT(A.HopDongChiTietREF) FROM 
				(
				SELECT DISTINCT tcdt.HopDongChiTietREF
					  FROM ThucChayDaTinh tcdt
					WHERE tcdt.HopDongID = @HopDongFK
					AND tcdt.HopDongChiTietREF = 0
					AND tcdt.DmSanPhamREF = @DmSanPhamREF 
					AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
				)A

				IF(@CheckHopDongChiTietTcID > 0)--Neu co hopdongchitiet = 0
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
					
						SELECT @TongThanhTienThucChayDT = (sum(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))*@TiLeDoanhSoKy)/@SoLuongNhan
						  FROM ThucChayDaTinh tcdt
						WHERE tcdt.HopDongID = @HopDongFK
						AND tcdt.DmSanPhamREF = @DmSanPhamREF 
						AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
						
						SET @DoanhSoThucChay = ISNULL(@TongThanhTienThucChayDT,0)
														
					END
				ELSE
					BEGIN
						SELECT @TongThanhTienThucChayDT = sum(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))/@SoLuongNhan
						  FROM ThucChayDaTinh tcdt
						WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
						AND tcdt.DmSanPhamREF = @DmSanPhamREF 
						AND tcdt.NgayThucHien = @NgayThucHien
						
						SET @DoanhSoThucChay = ISNULL(@TongThanhTienThucChayDT,0)
					END
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

--EXEC [Rpt_InsertNhanHangThucChayFullByNhanHang] '2013-01-01'

```
