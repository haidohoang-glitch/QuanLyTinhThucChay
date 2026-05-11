# Stored Procedure: `BPTC_NhapChiTieu_Get_ThongTinChiTieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.317000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.317000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Nam` | `int(4)` | No |
| `@LoaiTienID` | `int(4)` | No |
| `@SanPhamID` | `int(4)` | No |
| `@LevelChiTieu` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_NhapChiTieu_Get_ThongTinChiTieu]
    (
      @Nam INT ,
      @LoaiTienID INT ,
      @SanPhamID INT,
      @LevelChiTieu INT
    )
AS 
    BEGIN
        SELECT  @SanPhamID SanPhamID, 
				ThongTinChiTieuID,
				MONTH(ThoiGianBatDau) Thang ,
                dbo.FormatNumber(DoanhSoChiTieu) DoanhSoChiTieu
        FROM    dbo.ThongTinChiTieu
        WHERE   (DmChiTieuBoPhanREF = @SanPhamID OR @SanPhamID < 0) 
                AND LoaiTien = @LoaiTienID
                AND YEAR(ThoiGianKetThuc) = @Nam
                AND MONTH(ThoiGianBatDau) BETWEEN 1 AND 12
                AND LevelChiTieu = @LevelChiTieu
                AND DeleteStatus = 0
    END

```
