# Stored Procedure: `BI_Report_HoSoNhanCha_Export`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:16.107000
- **Ngày sửa cuối**: 2015-06-25 16:17:16.107000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangChaID` | `int(4)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
	EXEC [dbo].[BI_Report_HoSoNhanCha_Export] 
		1654,
		'2015-01-01',
		'2015-04-01'
*/
CREATE PROCEDURE [dbo].[BI_Report_HoSoNhanCha_Export] 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    -- Thong tin chung
	EXEC dbo.BI_HoSoNhanCha_ThongTinChung @DmNhanHangChaID,@FromDate,@ToDate
	
	-- Doanh so ky
	EXEC dbo.BI_HoSoNhanCha_ThongTinDoanhSoChung @DmNhanHangChaID,@FromDate,@ToDate
	
	-- Hinh thuc ky
	EXEC dbo.BI_HoSoNhanCha_DoanhSoTheoHinhThucKy @DmNhanHangChaID,@FromDate,@ToDate		
	
	-- Doanh so kenh
	EXEC BI_HoSoNhanCha_DoanhSoHaiDauTheoKenh @DmNhanHangChaID,@FromDate,@ToDate
	
	-- Doanh so theo website
	EXEC BI_HoSoNhanCha_DoanhSoThucChayTheoWebsite @DmNhanHangChaID,@FromDate,@ToDate		
	
	-- Nhan vien kinh doanh
	EXEC BI_HoSoNhanCha_DoanhSoTheoNhanVien @DmNhanHangChaID,@FromDate,@ToDate
	
	-- Phan 3
	EXEC BI_HoSoNhanCha_DoanhSoTheoKhachHang @DmNhanHangChaID,@FromDate,@ToDate
	
	-- Phan 4 - San pham
	EXEC BI_HoSoNhanCha_DoanhSoTheoSanPham @DmNhanHangChaID,@FromDate,@ToDate
	
	-- Phan 4 - Doanh so Cha - Con
	EXEC BI_HoSoNhanCha_TiLeDoanhSoCacNhanHang @DmNhanHangChaID,@FromDate,@ToDate
	
	-- Phan 5: Chi tiet
	EXEC BI_HoSoNhanCha_DoanhSoChiTietNhanHangCha @DmNhanHangChaID,@FromDate,@ToDate
END

```
