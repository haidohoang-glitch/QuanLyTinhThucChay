# Table: `ThucChayMuaNgoaiChiTiet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayMuaNgoaiChiTietID` | `INT` NN |  |
| `HopDongREF` | `INT` NN |  |
| `HopDongChiTietREF` | `INT` NN |  |
| `TuNgay` | `DATETIME` nullable |  |
| `DenNgay` | `DATETIME` nullable |  |
| `NgayThucChay` | `DATETIME` nullable |  |
| `SoLuongThucChay` | `FLOAT` nullable |  |
| `DmDonViTinhREF` | `INT` nullable |  |
| `ChietKhauMuaNgoai` | `FLOAT` nullable |  |
| `ThanhTienMuaNgoaiTruocCK` | `FLOAT` nullable |  |
| `ThanhTienThucChayBanSauCK` | `FLOAT` nullable |  |
| `ThanhTienLaiThucChaySauCK` | `FLOAT` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `Status` | `SMALLINT` nullable |  |
| `DeletedStatus` | `SMALLINT` nullable |  |
| `TrangThaiTinhThucChay` | `SMALLINT` nullable |  |
| `id` | `INT` PK IDENTITY |  |
| `NgayDuyet` | `DATETIME` nullable |  |
| `NguoiDuyet` | `NVARCHAR(100)` nullable |  |
| `NgayChot` | `DATETIME` nullable |  |
| `NguoiChot` | `NVARCHAR(100)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayMuaNgoaiChiTiet_1` | `id` | PRIMARY KEY |
