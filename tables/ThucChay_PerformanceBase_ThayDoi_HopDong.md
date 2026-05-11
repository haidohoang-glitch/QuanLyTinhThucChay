# Table: `ThucChay_PerformanceBase_ThayDoi_HopDong`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `ThucChay_PerformanceBase_ThayDoi_ID` | `INT` NN |  |
| `HopDongID` | `BIGINT` NN |  |
| `HopDongChitietID` | `BIGINT` NN |  |
| `DmSanPhamID` | `INT` NN |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `TK_Admarket` | `NVARCHAR(500)` NN |  |
| `DmViTriID` | `INT` NN |  |
| `TenViTri` | `NVARCHAR(500)` nullable |  |
| `NgayGhiNhanThayDoi` | `DATETIME` NN |  |
| `TienThucChay_GhiNhan` | `FLOAT` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `CreatedBy` | `NVARCHAR(50)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` NN |  |
| `RecordStatus` | `SMALLINT` NN |  |
| `DeletedStatus` | `SMALLINT` NN |  |
| `LyDoLoi` | `NVARCHAR(200)` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `TienThucChayKPI` | `FLOAT` nullable |  |
| `LoaiGhiNhan` | `SMALLINT` nullable | 0: thuc chay điều chỉnh - chi ap dung voi Adx, Viewplus, CPC admarket, 1: thuc chay thang du giai phap - all san pham |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChay_PerformanceBase_ThayDoi_HopDong` | `ID` | PRIMARY KEY |
