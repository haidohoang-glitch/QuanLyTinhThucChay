# Stored Procedure: `Delete_ThucChayAdmarketTaiKhoanByDate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-10 14:39:11.563000
- **Ngày sửa cuối**: 2015-04-16 13:36:11.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@TaiKhoan` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[Delete_ThucChayAdmarketTaiKhoanByDate] '2015-01-01', 'TH true milk'

CREATE PROCEDURE [dbo].[Delete_ThucChayAdmarketTaiKhoanByDate]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@TaiKhoan	NVARCHAR(200),
	@DmSanPhamREF int

AS
BEGIN
	PRINT @NgayThucHien
	--1. XAC DINH PHAN BO TINH CHO TAI KHOAN DAY TRONG NGAY THUC HIEN
	DELETE  ThucChayDaTinhAdmarket 
	FROM	ThucChayDaTinhAdmarket	
	INNER JOIN	HopDongChiTiet ON HopDongChiTiet.HopDongChiTietID = ThucChayDaTinhAdmarket.HopDongChiTietREF
	WHERE Convert(date,NgayThucHien) = @NgayThucHien
	AND HopDongChiTiet.TK_AdMarket = @TaiKhoan
	and HopDongChiTiet.DmSanPhamREF = @DmSanPhamREF  
	
	--2. UPDATE LAI TRANG THAI CUA DU LIEU TAI KHOAN TRONG TABLE ThucChayAdmarketOnline
	UPDATE ThucChayAdmarketOnline
	SET ThucChayAdmarketOnline.RecordStatus = 0	
	WHERE Convert(date,LastModifiedAt) = @NgayThucHien
	and TaiKhoan = @TaiKhoan
	and DmSanPhamREF = @DmSanPhamREF  
	
	--3. XOA DU LIEU ONLINE TAI NGAY THUC HIEN
	DELETE FROM ThucChayAdmarketOnline
	WHERE ThucChayAdmarketOnline.TaiKhoan = @TaiKhoan
	AND CONVERT(DATE,NgayThucHien) = @NgayThucHien
	and DmSanPhamREF = @DmSanPhamREF  
	
END
```
