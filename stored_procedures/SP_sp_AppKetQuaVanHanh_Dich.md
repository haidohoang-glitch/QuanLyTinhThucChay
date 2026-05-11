# Stored Procedure: `sp_AppKetQuaVanHanh_Dich`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:49:51.720000
- **Ngày sửa cuối**: 2026-03-06 16:49:51.720000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE sp_AppKetQuaVanHanh_Dich
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH src AS (
        SELECT *
        FROM ABM_Data_ThucChay.dbo.AppKetQuaVanHanh_CreatorContent
        WHERE IsDeleted = 0
          AND PhanBoRef = @HopDongChiTietID
    ),
    x AS (
        SELECT
            s.*,
            ca.PbSoLuong_n,
            ca.pbDonGia_n,
            ca.PbChietKhau_n,
            ca.PbThanhTien_n,
            ca.TcDonGia_n,
            ca.TcSoLuong_n,
            ca.TcThanhTien_n,
            ca.LaiLo_n
        FROM src s
        CROSS APPLY (
            SELECT
                TRY_CONVERT(decimal(18,2), REPLACE(REPLACE(CAST(s.PbSoLuong   AS varchar(50)), ',', ''), ' ', '')) AS PbSoLuong_n,
                TRY_CONVERT(decimal(18,2), REPLACE(REPLACE(CAST(s.pbDonGia    AS varchar(50)), ',', ''), ' ', '')) AS pbDonGia_n,
                TRY_CONVERT(decimal(18,2), REPLACE(REPLACE(CAST(s.PbChietKhau AS varchar(50)), ',', ''), ' ', '')) AS PbChietKhau_n,
                TRY_CONVERT(decimal(18,2), REPLACE(REPLACE(CAST(s.PbThanhTien AS varchar(50)), ',', ''), ' ', '')) AS PbThanhTien_n,
                TRY_CONVERT(decimal(18,2), REPLACE(REPLACE(CAST(s.TcDonGia    AS varchar(50)), ',', ''), ' ', '')) AS TcDonGia_n,
                TRY_CONVERT(decimal(18,2), REPLACE(REPLACE(CAST(s.TcSoLuong   AS varchar(50)), ',', ''), ' ', '')) AS TcSoLuong_n,
                TRY_CONVERT(decimal(18,2), REPLACE(REPLACE(CAST(s.TcThanhTien AS varchar(50)), ',', ''), ' ', '')) AS TcThanhTien_n,
                TRY_CONVERT(decimal(18,2), REPLACE(REPLACE(CAST(s.LaiLo       AS varchar(50)), ',', ''), ' ', '')) AS LaiLo_n
        ) ca
    )

    SELECT
           AppKetQuaVanHanh_CreatorContent_id AS ID,
           HopDongBanRef,
           PhanBoRef,
           dbo.FormatNumber(COALESCE(PbSoLuong_n,0))    AS PbSoLuong,
           dbo.FormatNumber(COALESCE(pbDonGia_n,0))     AS pbDonGia,
           dbo.FormatNumber(COALESCE(PbChietKhau_n,0))  AS PbChietKhau,
           dbo.FormatNumber(COALESCE(PbThanhTien_n,0))  AS PbThanhTien,
           NgayThucHien,
           Link,
           dbo.FormatNumber(COALESCE(TcDonGia_n,0))     AS TcDonGia,
           dbo.FormatNumber(COALESCE(TcSoLuong_n,0))    AS TcSoLuong,
           dbo.FormatNumber(COALESCE(TcThanhTien_n,0))  AS TcThanhTien,
           dbo.FormatNumber(COALESCE(LaiLo_n,0))        AS ThanhtienLaiLo,
           dbo.FormatNumber(COALESCE(PbThanhTien_n,0) - COALESCE(TcThanhTien_n,0)) AS [LechPB ky],
           RecordStatus,
           CASE
                WHEN TrangThai = 1 THEN N'1: Mới (k tính)'
                WHEN TrangThai = 2 THEN N'2: Gửi duyệt (gửi leader duyệt)(k tính)'
                WHEN TrangThai = 3 THEN N'3: Duyệt KQVH (leader duyệt)'
                WHEN TrangThai = 4 THEN N'4: Từ chối duyệt KQVH (k tính)'
                WHEN TrangThai = 5 THEN N'5: Gửi duyệt TT: Gửi kế toán duyệt TT'
                WHEN TrangThai = 6 THEN N'6: Duyệt TT: Kế toán duyệt TT'
                WHEN TrangThai = 7 THEN N'7: Từ chối duyệt TT'
                WHEN TrangThai = 8 THEN N'8: Gửi review TT'
                ELSE N''
           END AS TrangThai,
           CreationTime,
           CreatedBy,
           LastModificationTime,
           LastModifiedBy
    FROM x

    UNION ALL

    SELECT
           NULL AS ID,
           NULL AS HopDongBanRef,
           NULL AS PhanBoRef,
           dbo.FormatNumber(SUM(COALESCE(PbSoLuong_n,0)))    AS PbSoLuong,
           NULL AS pbDonGia,
           NULL AS PbChietKhau,
           NULL AS PbThanhTien,
           NULL AS NgayThucHien,
           NULL AS Link,
           NULL AS TcDonGia,
           dbo.FormatNumber(SUM(COALESCE(TcSoLuong_n,0)))    AS TcSoLuong,
           dbo.FormatNumber(SUM(COALESCE(TcThanhTien_n,0)))  AS TcThanhTien,
           dbo.FormatNumber(SUM(COALESCE(LaiLo_n,0)))        AS ThanhtienLaiLo,
           dbo.FormatNumber(
                SUM(COALESCE(PbThanhTien_n,0)) - SUM(COALESCE(TcThanhTien_n,0))
           ) AS [LechPB ky],
           NULL AS RecordStatus,
           N'TỔNG' AS TrangThai,
           NULL AS CreationTime,
           NULL AS CreatedBy,
           NULL AS LastModificationTime,
           NULL AS LastModifiedBy
    FROM x;

END

```
