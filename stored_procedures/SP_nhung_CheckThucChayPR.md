# Stored Procedure: `nhung_CheckThucChayPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:37:58.070000
- **Ngày sửa cuối**: 2026-03-05 14:37:58.070000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_CheckThucChayPR
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

;WITH A AS
(
    SELECT
        ThucChayHopDongChiTietPRID AS ID_treo,
        HopDongREF,
        HopDongChiTietREF,
        DmSanPhamREF,
        DmNhanHangREF,
        NhanHang,
        SoLuong,
        GiaTien,
        ChietKhau,
        (SoLuong * GiaTien * (100 - ChietKhau) / 100.0) AS thanhtien,
        TenWebsite,
        Link,
        parent_id,
        RecordStatus,
        ChuyenMuc,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy,
        TenViTri
    FROM dbo.ThucChayHopDongChiTietPR
    WHERE DeletedStatus = 0
      AND DmSanPhamREF IN (141,305,637)
      AND HopDongChiTietREF = @HopDongChiTietID
),

B AS
(
    SELECT
        TRY_CAST(
            LTRIM(RTRIM(
                LEFT(tc.DotChayBooking, CHARINDEX(':', tc.DotChayBooking + ':') - 1)
            )) AS INT
        ) AS ID_treo,

        SUM(tc.ThanhTienSauTrietKhauThucChay + tc.GiaTriThayDoi) AS thanhtienTC,
        SUM(tc.ThanhTienKM + tc.GiaTriKMThayDoi) AS ThanhtienKM

    FROM dbo.ThucChayDaTinh tc
    WHERE tc.DmSanPhamREF IN (141,637,305)
      AND tc.HopDongChiTietREF = @HopDongChiTietID

    GROUP BY
        TRY_CAST(
            LTRIM(RTRIM(
                LEFT(tc.DotChayBooking, CHARINDEX(':', tc.DotChayBooking + ':') - 1)
            )) AS INT
        )
),

DATA_CHECK AS
(
    SELECT
        A.*,
        B.thanhtienTC,
        B.ThanhtienKM
    FROM A
    LEFT JOIN B 
        ON A.ID_treo = B.ID_treo
    WHERE (B.ID_treo IS NULL OR A.thanhtien <> B.thanhtienTC)
),

FINAL AS
(
    -- Chi tiết chưa treo / lệch tiền
    SELECT
        0 AS SortKey,
        ID_treo,
        HopDongREF,
        HopDongChiTietREF,
        DmSanPhamREF,
        DmNhanHangREF,
        NhanHang,
        SoLuong,
        GiaTien,
        ChietKhau,
        thanhtien,
        TenWebsite,
        Link,
        parent_id,
        RecordStatus,
        ChuyenMuc,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy,
        TenViTri,
        thanhtienTC,
        ThanhtienKM
    FROM DATA_CHECK

    UNION ALL

    -- Tổng tiền chưa tính
    SELECT
        1,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        N'TỔNG CHƯA TÍNH',
        NULL,
        NULL,
        NULL,
        SUM(thanhtien),
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL
    FROM DATA_CHECK
)

SELECT
    ID_treo,
    HopDongREF,
    HopDongChiTietREF,
    DmSanPhamREF,
    DmNhanHangREF,
    NhanHang,
    SoLuong,
    dbo.FormatNumber(GiaTien) AS GiaTien,
    ChietKhau,
    dbo.FormatNumber(thanhtien) AS thanhtien,
    TenWebsite,
    Link,
    parent_id,
    RecordStatus,
    ChuyenMuc,
    CreatedAt,
    CreatedBy,
    LastModifiedAt,
    LastModifiedBy,
    TenViTri,
    dbo.FormatNumber(thanhtienTC) AS thanhtienTC,
    dbo.FormatNumber(ThanhtienKM) AS ThanhtienKM
FROM FINAL
ORDER BY SortKey, ID_treo;

END

```
