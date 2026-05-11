# Table: `CauHinhNhomTinhDoanhSoThucChay`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `DmSanPhamREF` | `INT` NN |  |
| `TenSanPham` | `NVARCHAR(200)` nullable |  |
| `NhomTinhDoanhSoThucChay` | `INT` NN | NhomTinhDoanhSoThucChay: 1- Nhom san pham Chi Phi, 2: Branding, 3: PR, 4: Admatic, 5: Performance Base |
| `ThongtinJobChay` | `NVARCHAR(200)` nullable |  |
| `DeletedStatus` | `SMALLINT` nullable |  |
| `RecordStatus` | `SMALLINT` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_CauHinhNhomTinhDoanhSoThucChay` | `ID` | PRIMARY KEY |
