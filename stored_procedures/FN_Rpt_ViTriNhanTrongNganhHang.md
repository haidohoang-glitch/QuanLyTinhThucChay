# Function: `Rpt_ViTriNhanTrongNganhHang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-22 17:42:28.510000
- **Ngày sửa cuối**: 2014-10-14 11:28:39.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(200)` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmNganhHangREF` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[Rpt_ViTriNhanTrongNganhHang]
(
	-- Add the parameters for the function here
	@DmNhanHangREF INT,
	@StartDate DATETIME,
	@EndDate DATETIME,
	@DmNganhHangREF NVARCHAR(50)
)
RETURNS nvarchar(100)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(100), @TongDoanhSoNhan BIGINT, @DmNganhHangID INT, @TongSoNhanHangInNganh INT
	DECLARE @TongSoNhanHangInAdmicro INT
	DECLARE @ViTriTrongNganh INT, @ThongTinViTriCuaNhan NVARCHAR(500), @TenNganhHang NVARCHAR(100)
	SET @TongDoanhSoNhan = 0
	SET @TongSoNhanHangInNganh = 0
	set @TongSoNhanHangInNganh = ''
	SET @TongSoNhanHangInAdmicro = 0
	SET @ThongTinViTriCuaNhan = ''
	IF(@DmNganhHangREF <> '0')
	BEGIN
		--Get tong doanh so cua nhan
		SET @TongDoanhSoNhan = 
		(
			SELECT SUM(rnhttct.DoanhSoKyHaiDau) DoanhSoKyHaiDau 
			FROM RptNhanHangThongTinChiTiet rnhttct
			WHERE rnhttct.DmNhanHangREF = @DmNhanHangREF
			AND CONVERT(date, rnhttct.NgayThucHien) BETWEEN @StartDate AND @EndDate	
		)
		--check dmnganhhang cua nhan
		
		DECLARE Record_Cursor CURSOR FOR 
		SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(@DmNganhHangREF,','))
		OPEN Record_Cursor
		FETCH NEXT FROM Record_Cursor into @DmNganhHangID
		WHILE @@FETCH_STATUS = 0
		BEGIN
			SET @TongSoNhanHangInNganh = 0
			SET @TenNganhHang = ''
			--Ten nganh hang
			SET @TenNganhHang =
			(
				SELECT dnh.TenNghanhHang FROM DmNghanhHang dnh
				WHERE dnh.DmNghanhHangID = @DmNganhHangID
			)	
			--Tong so nhan trong nganh
			SET @TongSoNhanHangInNganh = 20
			SET @TongSoNhanHangInNganh =
			(
				SELECT COUNT(dnh.DmNhanHangID) FROM DmNhanHang dnh
				WHERE convert(nvarchar(50),@DmNganhHangID) in (select * from dbo.SPLIT(dnh.DmNghanhHangREF,','))
			)
			--Vi tri doanh so nhan trong nganh
			SET @ViTriTrongNganh =
			(
				SELECT COUNT(a.DmNhanHangREF) FROM 
				(
				SELECT rnhttct.DmNhanHangREF, SUM(rnhttct.TongDoanhSoKyHaiDau) TongDoanhSoKyHaiDau 
				  FROM RptNhanHangThongTinChiTiet rnhttct
				WHERE @DmNganhHangID  in (select * from dbo.SPLIT(rnhttct.DmNganhHangREF,','))
				AND rnhttct.NgayThucHien BETWEEN @StartDate AND @EndDate
				AND rnhttct.DmNhanHangREF <> 0
				GROUP BY rnhttct.DmNhanHangREF
				)a
				WHERE a.TongDoanhSoKyHaiDau >= @TongDoanhSoNhan
			)
			SET @ThongTinViTriCuaNhan = @ThongTinViTriCuaNhan + convert(nvarchar(50),@ViTriTrongNganh) 
			+ '/' +  CONVERT(NVARCHAR(50),@TongSoNhanHangInNganh) + N' nhãn c?a ngành ' + @TenNganhHang + ', '
			FETCH NEXT FROM Record_Cursor into @DmNganhHangID
		END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
	END
	ELSE
		BEGIN
			--Get tong doanh so cua nhan
			SET @TongDoanhSoNhan = 
			(
				SELECT SUM(rnhttct.DoanhSoKyHaiDau) DoanhSoKyHaiDau 
				FROM RptNhanHangThongTinChiTiet rnhttct
				WHERE rnhttct.DmNhanHangREF = @DmNhanHangREF
				AND CONVERT(date, rnhttct.NgayThucHien) BETWEEN @StartDate AND @EndDate	
			)
			--Tong so nhan trong nganh
			SET @TongSoNhanHangInAdmicro =
			(
				SELECT COUNT(dnh.DmNhanHangID) FROM DmNhanHang dnh
				WHERE dnh.RecordStatus = 1
			)
			--Vi tri doanh so nhan trong nganh
			SET @ViTriTrongNganh =
			(
				SELECT COUNT(a.DmNhanHangREF) FROM 
				(
				SELECT rnhttct.DmNhanHangREF, SUM(rnhttct.TongDoanhSoKyHaiDau) TongDoanhSoKyHaiDau 
				  FROM RptNhanHangThongTinChiTiet rnhttct
				WHERE rnhttct.NgayThucHien BETWEEN @StartDate AND @EndDate
				AND rnhttct.DmNhanHangREF <> 0
				GROUP BY rnhttct.DmNhanHangREF
				)a
				WHERE a.TongDoanhSoKyHaiDau >= @TongDoanhSoNhan
			)
			SET @ThongTinViTriCuaNhan = convert(nvarchar(50),@ViTriTrongNganh) 
			+ '/' +  CONVERT(NVARCHAR(50),@TongSoNhanHangInAdmicro)
			
		END
	
    SET @Result = @ThongTinViTriCuaNhan        
	-- Return the result of the function
	RETURN @Result

END

```
