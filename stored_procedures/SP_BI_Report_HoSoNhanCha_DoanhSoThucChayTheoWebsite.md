# Stored Procedure: `BI_Report_HoSoNhanCha_DoanhSoThucChayTheoWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:16.227000
- **Ngày sửa cuối**: 2015-06-25 16:17:16.227000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangChaID` | `int(4)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BI_Report_HoSoNhanCha_DoanhSoThucChayTheoWebsite] 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @TempTable as Table(
		DmNhanHangID	int,
		TenNhanhang		nvarchar(255),
		TinhTrangNhanHang	nvarchar(50),
		KhachHangSoHuuREF	int,
		TenKhachHangSoHuu	nvarchar(512),
		MaSoThue	nvarchar(50),
		DiaChiKhachHang	nvarchar(512),
		SoDienThoai	nvarchar(255)
	  )
	  
	insert into @TempTable
	exec [dbo].BI_HoSoNhanCha_ThongTinChung @DmNhanHangChaID, @FromDate, @ToDate;
  
	exec [dbo].BI_HoSoNhanCha_DoanhSoThucChayTheoWebsite @DmNhanHangChaID, @FromDate, @ToDate;
END

```
