# Stored Procedure: `Rpt_InsertNhanHangThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:33.753000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.553000

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

CREATE  PROCEDURE [dbo].[Rpt_InsertNhanHangThucChay] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT
	DECLARE @TenSanPham NVARCHAR(100), @DmSanPhamREF INT, @ThanhTienThucChay BIGINT  
    DECLARE @DoanhSoThucChay BIGINT, @CheckHopDongChiTietTcID INT, @TongThanhTienThucChayDT BIGINT
    DECLARE @DmNhanHangREF INT, @TenNhanHang NVARCHAR(200), @SoluongHDCT INT
    SET @Result = 0
    SET @SoluongHDCT = 1
    --TINH DU LIEU THONG TIN NHAN HANG
	DECLARE Record_Cursor CURSOR FOR 
	SELECT dnh.DmNhanHangID, dnh.TenNhanHang FROM DmNhanHang dnh
	WHERE dnh.DmNhanHangID IN (1654, 433, 760, 2905, 1174, 1827, 32698, 2844, 2775, 1931,2516, 777,27351, 1853, 455, 133,2161, 1283, 1607, 471, 1458,1626)
	--(2516, 777,27351, 1853, 455, 133,2161, 1283, 1607, 471, 1458,1626)
	AND dnh.RecordStatus = 1
	AND dnh.DeletedStatus = 0	
	
	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @DmNhanHangREF, @TenNhanHang
			
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT @DmNhanHangREF
		DECLARE Record_Cursor1 CURSOR FOR 
		SELECT distinct hd.SoHopDong, hd.HopDongID ,hdct.HopDongChiTietID, hdct.TenSanPham, hdct.DmSanPhamREF
		FROM hopdong hd 
		INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.TrangThaiHopDong <> 3
		AND CONVERT(NVARCHAR(50),@DmNhanHangREF) in (hdct.DanhSachNhanHangREF)
		 
		OPEN Record_Cursor1
		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF
		WHILE @@FETCH_STATUS = 0
		BEGIN
			--PRINT @HopDongChiTietID
			--Check HopDong co hopdongchitiet = 0 ?
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
			SET @SoluongHDCT =
			(
				SELECT count(distinct hdct.HopDongChiTietID)
				FROM hopdong hd 
				INNER JOIN	HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				WHERE hd.TrangThaiHopDong <> 3
				AND CONVERT(NVARCHAR(50),@DmNhanHangREF) in (hdct.DanhSachNhanHangREF)
				AND hd.HopDongID = @HopDongFK
				AND hdct.DmSanPhamREF = @DmSanPhamREF
			)		
			IF(@CheckHopDongChiTietTcID > 0)--Neu co hopdongchitiet = 0
				BEGIN
					SELECT @TongThanhTienThucChayDT = sum(tcdt.ThanhTienSauTrietKhauThucChay)
					  FROM ThucChayDaTinh tcdt
					WHERE tcdt.HopDongID = @HopDongFK
					AND tcdt.DmSanPhamREF = @DmSanPhamREF 
					AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
					
					SET @DoanhSoThucChay = ISNULL(@TongThanhTienThucChayDT,0)/@SoluongHDCT
													
				END
			ELSE
				BEGIN
					SELECT @TongThanhTienThucChayDT = sum(tcdt.ThanhTienSauTrietKhauThucChay)
					  FROM ThucChayDaTinh tcdt
					WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND tcdt.DmSanPhamREF = @DmSanPhamREF 
					AND tcdt.NgayThucHien = @NgayThucHien
					
					SET @DoanhSoThucChay = ISNULL(@TongThanhTienThucChayDT,0)
				END
			IF(@DoanhSoThucChay <> 0)
			BEGIN
				INSERT INTO [dbo].[RptNhanHangThucChay]
				  (
				    [DmNhanHangREF],
				    [TenNhanHang],
				    [HopDongREF],
				    [SoHopDong],
				    [HopDongChiTietREF],
				    [DmSanPhamREF],
				    [TenSanPham],
				    [NgayThucHien],
				    [DoanhSoThucChay],
				    [CreatedBy],
				    [CreatedAt],
				    [RecordStatus]
				  )
				VALUES
				  (
				    @DmNhanHangREF,
				    @TenNhanHang,
				    @HopDongFK,
				    @SoHopDong,
				    @HopDongChiTietID,
				    @DmSanPhamREF,
				    @TenSanPham,
				    @NgayThucHien,
				    @DoanhSoThucChay,
				    '',
				    GETDATE(),
				    0
				  )	
			END	
			--PRINT 'ket thuc'
			FETCH NEXT FROM Record_Cursor1 INTO @SoHopDong, @HopDongFK, @HopDongChiTietID, @TenSanPham, @DmSanPhamREF
		END
		
		CLOSE Record_Cursor1
		DEALLOCATE Record_Cursor1
		FETCH NEXT FROM Record_Cursor INTO @DmNhanHangREF, @TenNhanHang
	END
	
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor  
	--SELECT '1'
END

--EXEC [Rpt_InsertNhanHangThongTinChiTiet] '2013-01-01'

```
