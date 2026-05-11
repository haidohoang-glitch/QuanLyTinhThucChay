# Stored Procedure: `ChiTietADX`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-01-05 14:02:16.473000
- **Ngày sửa cuối**: 2026-01-05 14:17:13.270000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE ChiTietADX
    @SoHopDong        NVARCHAR(100),
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    /*
      Output trả về 1 result-set duy nhất, gồm:
      - BlockKey/BlockTitle: accordion cấp 1
      - TableKey/TableTitle: bảng con trong accordion
      - DataJson: dữ liệu dạng JSON array để UI render table
    */

    SELECT
        'block_contract'                  AS BlockKey,
        N'Thông tin hợp đồng'             AS BlockTitle,
        'tbl_hopdong'                     AS TableKey,
        N'Thông tin HĐ'                   AS TableTitle,
        JSON_QUERY(ISNULL((
            SELECT
                N'Thông tin HĐ' AS HĐ,
                SoHopDong, HopDongID, DmKhachHangREF, TenKhachHang, TrangThaiHopDong,
                DmNhanGocREF, TenNhanGoc,
                dbo.FormatNumber(GiaTriHopDong) AS GiaTriHopDong,
                CreatedAt, LastModifiedAt
            FROM dbo.HopDong
            WHERE SoHopDong = @SoHopDong
              AND DeletedStatus = 0
            FOR JSON PATH, INCLUDE_NULL_VALUES
        ), '[]')) AS DataJson

    UNION ALL

    SELECT
        'block_contract'                  AS BlockKey,
        N'Thông tin hợp đồng'             AS BlockTitle,
        'tbl_phanbo'                      AS TableKey,
        N'Thông tin Phân bổ'              AS TableTitle,
        JSON_QUERY(ISNULL((
            SELECT
                N'Thông tin Phân bô' AS HĐCT,
                HopDongFK, HopDongChiTietID, DmSanPhamREF, TenSanPham, TenLoai,
                SoLuong, DonViTinh,
                dbo.FormatNumber(DonGia) AS DonGia,
                ChietKhau,
                dbo.FormatNumber(ThanhTien) AS ThanhTien,
                DeletedStatus, DmLoaiREF, DmLoaiNenTangREF, DanhSachNhanHangREF,
                NhanHang, CreatedAt, LastModifiedAt
            FROM dbo.HopDongChiTiet
            WHERE HopDongChiTietID = @HopDongChiTietID
            FOR JSON PATH, INCLUDE_NULL_VALUES
        ), '[]')) AS DataJson;
END

```
