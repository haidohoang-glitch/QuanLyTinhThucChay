# Stored Procedure: `KSTC_CheckGoogleFacebook`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:24.457000
- **Ngày sửa cuối**: 2015-04-08 10:00:24.457000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--KSTC_CheckGoogleFacebook '2014-12-20', '2014-12-20'
CREATE PROCEDURE [dbo].[KSTC_CheckGoogleFacebook] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
	
AS
BEGIN	
	DECLARE @DmSanPhamREF INT, @TenSanPham NVARCHAR(50), @TaiKhoan NVARCHAR(50), 
			@SoNgayChay INT, @Click INT, @ThanhTienTC FLOAT, @Type NVARCHAR(50)
				
	DECLARE @NgayThucHien DATETIME;
	
	SET @NgayThucHien = @EndDate	
	--Danh sach du lieu import sai	
	SELECT * FROM ThucChayGoogleFacebook tcgf 
	WHERE tcgf.NgayThucHien = @NgayThucHien
	AND  (tcgf.DmSanPhamREF = 423 AND [Type] = 'like' -- Google 
	--OR tcgf.DmSanPhamREF = 306 AND [Type] = 'click' -- Facebook
	)
	AND tcgf.DeletedStatus = 0 AND tcgf.RecordStatus = 1
	IF OBJECT_ID(N'dbo.#temp', N'U') IS NOT NULL
	DROP TABLE dbo.#temp;
	
	CREATE TABLE #temp (
    DmSanPhamREF INT, 
	TenSanPham NVARCHAR(50), 
	TaiKhoan NVARCHAR(50), 
	[Type] NVARCHAR(50), 
	NgayThucHien DATETIME,
	GhiChu NVARCHAR(200)
);

	DECLARE vendor_cursor CURSOR FOR 
		Select tcgf.DmSanPhamREF, tcgf.TenSanPham, tcgf.TaiKhoan,SUM(tcgf.SoNgayChay) SoNgayChay,
		SUM(tcgf.Click) Click, SUM(tcgf.ThanhTien) ThanhTien, tcgf.[Type]
		  FROM ThucChayGoogleFacebook tcgf
		WHERE tcgf.DeletedStatus = 0
		AND tcgf.RecordStatus = 1
		AND convert(date,tcgf.NgayThucHien)= '2014-12-20'--@NgayThucHien
		--AND tcgf.TaiKhoan = 'Nha Hang Cong Vien Nho'
		GROUP BY tcgf.DmSanPhamREF, tcgf.TenSanPham, tcgf.TaiKhoan, tcgf.[Type]
		ORDER BY tcgf.[Type],tcgf.DmSanPhamREF, tcgf.TaiKhoan; 
	OPEN vendor_cursor

	FETCH NEXT FROM vendor_cursor 
	INTO @DmSanPhamREF, @TenSanPham, @TaiKhoan, @SoNgayChay, @Click, @ThanhTienTC, @Type

	WHILE @@FETCH_STATUS = 0
	BEGIN
		
		--SELECT @TaiKhoan
		IF @Type = 'phi_quan_ly'
			BEGIN
				--SELECT 1
				EXEC dbo.KSTC_GoogleFacebook_chiphiquanly @DmSanPhamREF, @TenSanPham, @TaiKhoan, @ThanhTienTC, @Type, @NgayThucHien
			END
		ELSE IF @Type = 'thoi_gian'
			BEGIN
				EXEC dbo.KSTC_GoogleFacebook_thoigian @DmSanPhamREF, @TenSanPham, @TaiKhoan, @SoNgayChay, @Type, @NgayThucHien
			END
		ELSE IF @Type = 'like'		
			BEGIN
				--SELECT 2
				EXEC dbo.KSTC_GoogleFacebook_like @DmSanPhamREF, @TenSanPham, @TaiKhoan, @Click, @Type, @NgayThucHien
			END
		ELSE IF @Type = 'click'
			BEGIN
				--SELECT 3
				EXEC dbo.KSTC_GoogleFacebook_click @DmSanPhamREF, @TenSanPham, @TaiKhoan, @Click, @Type, @NgayThucHien
				
			END	
		FETCH NEXT FROM vendor_cursor INTO @DmSanPhamREF, @TenSanPham, @TaiKhoan, @SoNgayChay, @Click, @ThanhTienTC, @Type
	END 
	CLOSE vendor_cursor;
	DEALLOCATE vendor_cursor;
;
SELECT * FROM #temp t
END

```
