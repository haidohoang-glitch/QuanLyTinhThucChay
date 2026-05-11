# Stored Procedure: `BI_HoSoNhanCha_DoanhSoChiTietNhanHangCha`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:14.677000
- **Ngày sửa cuối**: 2015-06-25 16:17:14.677000

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

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoChiTietNhanHangCha] 1523,'2014-01-01','2015-01-01'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_DoanhSoChiTietNhanHangCha] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	SELECT [DmNhanHangID]
      ,[TenNhanHang]
      ,[DmNganhHangREF]
      ,[TenNganhHang]
      ,[NhanHangChaREF]
      ,[NhanHangGocID]
      ,[levels]
      ,[SoHopDong]
      ,[HopDongREF]
      ,[TenNhanVien]
      ,[TenBoPhan]
      ,[TenKhachHang]
      ,[DoanhSoHaiDau]
      ,[ThucChay]
      ,[DmSanPhamREF]
      ,[TenSanPham]
  FROM [dbo].[HoSoNhan_DoanhSoChiTiet]
  WHERE NhanHangGocID = @DmNhanHangChaID
  AND (DoanhSoHaiDau <> 0 OR ThucChay <> 0)
  ORDER BY STT
			
END

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoChiTietNhanHangCha] 4152,'2015-01-01','2014-01-01'

```
