# Table: `QLTC_Log_Branding_NativeAds_OnImages`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `LogId` | `INT` PK IDENTITY |  |
| `NativeAds_Onimages` | `NVARCHAR(MAX)` nullable |  |
| `TypeProduct` | `NVARCHAR(MAX)` nullable |  |
| `TenSanPham` | `NVARCHAR(MAX)` nullable |  |
| `DmSanPhamREF` | `NVARCHAR(MAX)` nullable |  |
| `SL HN (ASD/Tool)` | `NVARCHAR(MAX)` nullable |  |
| `TT HN (ASD/Tool)` | `NVARCHAR(MAX)` nullable |  |
| `SL % (HN vs HQ)` | `NVARCHAR(MAX)` nullable |  |
| `TT % (HN vs HQ)` | `NVARCHAR(MAX)` nullable |  |
| `TrangThai` | `NVARCHAR(MAX)` nullable |  |
| `NgayThucHien` | `DATE` nullable |  |
| `NguoiThucHien` | `NVARCHAR(255)` nullable |  |
| `NgayKiemTra` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__QLTC_Log__5E5486480D666D85` | `LogId` | PRIMARY KEY |
