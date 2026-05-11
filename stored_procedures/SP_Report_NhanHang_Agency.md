# Stored Procedure: `Report_NhanHang_Agency`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-02-12 15:17:42.233000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.460000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Report_NhanHang_Agency]
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @AbmNhanHangID NVARCHAR(50), @NhanHang NVARCHAR(100), @DmKhachHangREF INT, @DmNhanHangID INT, @TenKhachHang NVARCHAR(200)
DECLARE @TenNhanHang NVARCHAR(100), @nhan NVARCHAR(500)

DELETE FROM dbo.tbl_NhanHang_Agency

DECLARE Record_Cursor CURSOR FOR 
	SELECT b.abm_nhanhang_id, b.nhanhang, b.khachhang_id, khf.TenKhachHang
	  from dbo.ds_NhanHangAgency_2013$ b
	LEFT JOIN KhachHangFull khf ON b.khachhang_id = khf.KhachHangID
WHERE b.abm_nhanhang_id IS NOT NULL
AND b.abm_nhanhang_id <> 'null'	
	
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into	@AbmNhanHangID, @NhanHang, @DmKhachHangREF, @TenKhachHang
		
WHILE @@FETCH_STATUS = 0
	BEGIN
	PRINT 'dau tien :' + @AbmNhanHangID
	SET @AbmNhanHangID = ISNULL(@AbmNhanHangID,'')
	set @nhan = ISNULL(@AbmNhanHangID,'')
	PRINT @nhan
	IF(@AbmNhanHangID IS NOT NULL)
	BEGIN
		PRINT 'vao roi'
		DECLARE Record_Cursor1 CURSOR FOR 
		SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(isnull(@AbmNhanHangID,''),','))
		OPEN Record_Cursor1
		FETCH NEXT FROM Record_Cursor1 into @DmNhanHangID
		WHILE @@FETCH_STATUS = 0
			BEGIN
			PRINT @DmNhanHangID
			SET @DmNhanHangID = ISNULL(@DmNhanHangID,'')
			SET @TenNhanHang =
			(
				SELECT dnh.TenNhanHang FROM DmNhanHang dnh
				WHERE dnh.DmNhanHangID = @DmNhanHangID
				AND dnh.RecordStatus = 1
			)
			SET @TenNhanHang = isnull(@TenNhanHang,'')
			PRINT 'vao insser'
			--Insert thuc chay ThucChayHopDongChiTietID	
			INSERT INTO dbo.tbl_NhanHang_Agency
			(
				TenNhanHang, TenKhachHang, dmNhanHangREF, dmKhachHangREF
			)
			VALUES
			(
				@TenNhanHang, @TenKhachHang, @DmNhanHangID, @DmKhachHangREF	
			)
			
			
			FETCH NEXT FROM Record_Cursor1 into @DmNhanHangID
			end
		CLOSE Record_Cursor1
		DEALLOCATE Record_Cursor1
	END	
	
	
	FETCH NEXT FROM Record_Cursor into	@AbmNhanHangID, @NhanHang, @DmKhachHangREF, @TenKhachHang 
		
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

SELECT '1'



END

--EXEC [dbo].[Report_NhanHang_Agency]

--SELECT * from dbo.tbl_NhanHang_Agency

```
