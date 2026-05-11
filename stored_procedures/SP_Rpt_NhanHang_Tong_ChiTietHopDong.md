# Stored Procedure: `Rpt_NhanHang_Tong_ChiTietHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:31.687000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.430000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@LabelId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE  PROC [dbo].[Rpt_NhanHang_Tong_ChiTietHopDong]
(
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@LabelId	INT		
)
AS
BEGIN		
	SELECT dbo.FormatNumber(SUM(x.DoanhSoKyHaiDau)) TongDoanhSoKyHaiDau	
	FROM RptNhanHangThongTinChiTiet x
	WHERE x.DmNhanHangREF = @LabelId AND CONVERT(date, x.NgayThucHien) BETWEEN @StartDate AND @EndDate			
END

```
