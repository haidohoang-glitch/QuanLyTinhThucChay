# Function: `Rpt_GetDoanhSoThucChayByNhanHang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-22 17:42:36.303000
- **Ngày sửa cuối**: 2014-10-14 11:28:45.073000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE  FUNCTION [dbo].[Rpt_GetDoanhSoThucChayByNhanHang]
(
   @DmNhanHangREF INT,
   @StartDate DATETIME,
   @EndDate DATETIME
)
 RETURNS BIGINT
  AS
 BEGIN
    DECLARE @Result BIGINT, @SoHopDong NVARCHAR(50),@HopDongFK INT,@HopDongChiTietID INT  
    DECLARE @LstTenNhanHang NVARCHAR(300), @DmLstNhanHang NVARCHAR(50), @ThanhTien BIGINT
    DECLARE @DoanhSoThucChay BIGINT, @CheckHopDongChiTietTcID INT, @DmSanPhamREF INT, @TongThanhTienThucChayDT BIGINT
    DECLARE @SoLuongNhan INT
    SET @Result = 0
    --TINH DU LIEU THONG TIN NHAN HANG
	DECLARE Record_Cursor CURSOR FOR 
	SELECT hd.SoHopDong, hdct.HopDongFK, HDCT.HopDongChiTietID, hdct.NhanHang
		, hdct.DanhSachNhanHangREF,hdct.DmSanPhamREF, hdct.ThanhTien
	  FROM HopDong hd 
	INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE hd.TrangThaiHopDong <> 3
	AND hdct.DeletedStatus = 0
	--AND hd.IsBanCung = 1 
	--AND Convert(date,hd.NgayDanhSoHopDong) <= @EndDate 
	AND convert(nvarchar(50),@DmNhanHangREF) IN (hdct.DanhSachNhanHangREF) 
	AND hdct.DeletedStatus = 0 
	ORDER BY hd.NgayDanhSoHopDong
		
	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor into @SoHopDong, @HopDongFK, @HopDongChiTietID
			, @LstTenNhanHang, @DmLstNhanHang,@DmSanPhamREF,@ThanhTien
			
	WHILE @@FETCH_STATUS = 0
	BEGIN
			--PRINT @HopDongChiTietID
			SET @HopDongChiTietID = ISNULL(@HopDongChiTietID,0)
			SET @LstTenNhanHang = ISNULL(@LstTenNhanHang,'')
			SET @DmLstNhanHang = ISNULL(@DmLstNhanHang,'')
			
			SELECT @SoLuongNhan = count(a.DmNhanHang) from
			(
				SELECT dbo.FormatString(item) DmNhanHang
				FROM dbo.ArrayToTable(dbo.Array(@DmLstNhanHang,','))
			)a
			IF(@SoLuongNhan <> 0)
			BEGIN
				SELECT @CheckHopDongChiTietTcID = COUNT(A.HopDongChiTietREF) FROM 
							(
							SELECT DISTINCT tcdt.HopDongChiTietREF
								  FROM ThucChayDaTinh tcdt
								WHERE tcdt.HopDongID = @HopDongFK
								AND tcdt.HopDongChiTietREF = 0
								AND tcdt.DmSanPhamREF = @DmSanPhamREF 
							)A
				SET @DoanhSoThucChay = 0
				IF(@CheckHopDongChiTietTcID > 0)--Neu co hopdongchitiet = 0
					BEGIN
						SELECT @TongThanhTienThucChayDT = sum(tcdt.ThanhTienSauTrietKhauThucChay)
						  FROM ThucChayDaTinh tcdt
						WHERE tcdt.HopDongID = @HopDongFK
						AND tcdt.DmSanPhamREF = @DmSanPhamREF 
						AND convert(date,tcdt.NgayThucHien) BETWEEN @StartDate AND @EndDate
						
						SET @DoanhSoThucChay = @DoanhSoThucChay + ISNULL(@TongThanhTienThucChayDT,0)/@SoLuongNhan
														
					END
				ELSE
					BEGIN
						SELECT @TongThanhTienThucChayDT = sum(tcdt.ThanhTienSauTrietKhauThucChay)
						  FROM ThucChayDaTinh tcdt
						WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
						AND tcdt.DmSanPhamREF = @DmSanPhamREF 
						AND tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
						
						SET @DoanhSoThucChay = @DoanhSoThucChay + ISNULL(@TongThanhTienThucChayDT,0)/@SoLuongNhan
					END
		END
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @HopDongFK, @HopDongChiTietID
			, @LstTenNhanHang, @DmLstNhanHang,@DmSanPhamREF,@ThanhTien
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor  
   
   RETURN @Result
 END

```
