# Stored Procedure: `sp_kiemtrachotsoB6`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 17:39:27.650000
- **Ngày sửa cuối**: 2026-03-17 17:39:27.650000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |

## Definition (Source Code)

```sql


CREATE PROCEDURE dbo.sp_kiemtrachotsoB6
    @NgayBatDau DATE
AS
BEGIN
    SET NOCOUNT ON;

    -----------------------------------------
    -- B6: Check sai nhãn / nhãn rác
    -----------------------------------------
    SELECT 
        a.*,
        b.IDnhanPB,
        b.NhanHangPB,
        CASE 
            WHEN ISNULL(a.NhanHang, '0') = ISNULL(b.IDnhanPB, '0') 
                THEN N'PB không có nhãn'
            ELSE N'Sai nhãn - KT lại'
        END AS GhiChu
    FROM (
        SELECT 
            SoHopDong,
            HopDongChiTietREF,
            NhanHang,
            dbo.FormatNumber(
                SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) 
                  + ISNULL(GiaTriThayDoi,0))
            ) AS TT,
            TenSanPham,
            TenHinhThucQuangCao,
            TenLoaiBanner
        FROM dbo.ThucChayDaTinh
        WHERE CONVERT(DATE, NgayThucHien) >= @NgayBatDau
            AND (
                NhanHang LIKE N'%566846%' 
                OR NhanHang LIKE N'%212536%' 
                OR ISNULL(NhanHang,'') = '' 
                OR NhanHang = '0' 
                OR NhanHang = '1423152'   -- Nhãn rác
            )
            AND HopDongChiTietREF <> 0
        GROUP BY 
            SoHopDong, HopDongChiTietREF, NhanHang,
            TenSanPham, TenHinhThucQuangCao, TenLoaiBanner
        HAVING 
            ROUND(SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) 
                    + ISNULL(GiaTriThayDoi,0)),2) <> 0
    ) a
    LEFT JOIN (
        SELECT 
            HopDongChiTietID,
            DanhSachNhanHangREF AS IDnhanPB,
            NhanHang AS NhanHangPB
        FROM dbo.HopDongChiTiet
    ) b 
        ON a.HopDongChiTietREF = b.HopDongChiTietID

    ORDER BY a.HopDongChiTietREF

END

```
