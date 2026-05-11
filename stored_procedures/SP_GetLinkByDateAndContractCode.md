# Stored Procedure: `GetLinkByDateAndContractCode`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-07 11:35:00.020000
- **Ngày sửa cuối**: 2019-05-07 11:35:06.317000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
--='QC7951017'
CREATE PROCEDURE [GetLinkByDateAndContractCode] @SoHopDong NVARCHAR(100)
-- WITH ENCRYPTION, RECOMPILE, EXECUTE AS CALLER|SELF|OWNER| 'user_name'
AS
BEGIN
    SELECT hd.SoHopDong,
           t.NhanHang,
           t.ThoiGianBatDau,
           t.GiaTien,
           t.ChietKhau,
           t.SoLuong,
           ISNULL(t.Link, '') Link,
           t.TenWebsite,
           ISNULL(t.ChuyenMuc, '') ChuyenMuc,
           t.TenViTri
    FROM dbo.ThucChayHopDongChiTietPR t
        INNER JOIN dbo.HopDong hd
            ON t.HopDongREF = hd.HopDongID
    WHERE (hd.SoHopDong = @SoHopDong OR t.Link =@SoHopDong)
          AND t.DeletedStatus = 0;
END;

```
