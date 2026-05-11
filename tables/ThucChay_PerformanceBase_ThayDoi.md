# Table: `ThucChay_PerformanceBase_ThayDoi`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `HopDongID` | `INT` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `TK_Admarket` | `NVARCHAR(50)` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(50)` nullable |  |
| `TienThucChayTong` | `FLOAT` nullable |  |
| `TienThucChay` | `FLOAT` nullable |  |
| `ThucChayDenNgay` | `DATETIME` nullable |  |
| `SoTienThayDoi` | `FLOAT` nullable |  |
| `NgayGhiNhanThayDoi` | `DATETIME` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `LyDoTuChoi` | `NVARCHAR(200)` nullable |  |
| `Request_key` | `NVARCHAR(50)` nullable |  |
| `TienThucChayKPI` | `FLOAT` nullable |  |
| `LoaiGhiNhan` | `INT` DEFAULT 0 nullable | 0: thuc chay điều chỉnh - chi ap dung voi Adx, Viewplus, CPC admarket. 1: thuc chay thang du giai phap - all san pham. |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChay_PerformanceBase_ThayDoi` | `Id` | PRIMARY KEY |
