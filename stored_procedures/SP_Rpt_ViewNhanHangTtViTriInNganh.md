# Stored Procedure: `Rpt_ViewNhanHangTtViTriInNganh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:31.487000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.453000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmNhanHangREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_ViewNhanHangTtViTriInNganh]
	@StartDate DATETIME,
	@EndDate DATETIME,
	@DmNhanHangREF INT
AS
BEGIN
	DECLARE @Result nvarchar(100), @TongDoanhSoNhan BIGINT, @DmNganhHangID INT, @TongSoNhanHangInNganh INT
	DECLARE @TongSoNhanHangInAdmicro INT, @DmNganhHangREF NVARCHAR(50)
	DECLARE @ViTriTrongNganh INT, @ThongTinViTriCuaNhan NVARCHAR(500), @TenNganhHang NVARCHAR(100)
	DECLARE @Table_NhanHangInNganh TABLE (ViTri NVARCHAR(50), TenNganhHang NVARCHAR(300))
	
	SET @TongDoanhSoNhan = 0
	SET @TongSoNhanHangInNganh = 0
	set @TongSoNhanHangInNganh = ''
	SET @TongSoNhanHangInAdmicro = 0
	SET @ThongTinViTriCuaNhan = ''
	--GET nganh hang
	SET @DmNganhHangREF = 
	(
		SELECT dnh.DmNghanhHangREF FROM DmNhanHang dnh
		WHERE dnh.DmNhanHangID = @DmNhanHangREF
		AND dnh.DeletedStatus = 0	
	)
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
			SET @ThongTinViTriCuaNhan = convert(nvarchar(50),@ViTriTrongNganh)+ '/' +  CONVERT(NVARCHAR(50),@TongSoNhanHangInNganh)
			INSERT INTO @Table_NhanHangInNganh
			(
				ViTri,
				TenNganhHang
			)
			VALUES
			(
				@ThongTinViTriCuaNhan,
				@TenNganhHang
			)
			
			--SET @ThongTinViTriCuaNhan = @ThongTinViTriCuaNhan + convert(nvarchar(50),@ViTriTrongNganh) 
			--+ '/' +  CONVERT(NVARCHAR(50),@TongSoNhanHangInNganh) + N' nhãn c?a ngành ' + @TenNganhHang + ', '
			FETCH NEXT FROM Record_Cursor into @DmNganhHangID
		END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
	END
    SELECT * FROM @Table_NhanHangInNganh tnhin
END
--EXEC [Rpt_ViewNhanHangTtViTriInNganh]'2013-01-01','2013-12-31',	2516

```
