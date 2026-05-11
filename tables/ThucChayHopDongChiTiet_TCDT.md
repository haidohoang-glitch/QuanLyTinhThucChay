# Table: `ThucChayHopDongChiTiet_TCDT`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayHopDongChiTiet_TCDT_ID` | `INT` PK IDENTITY |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `ThucChayHopDongChiTietREF` | `INT` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `ChietKhauHDCT` | `FLOAT` nullable |  |
| `ThanhTienHDCT` | `BIGINT` nullable |  |
| `DonGiaHDCT` | `FLOAT` nullable |  |
| `SoluongHDCT` | `INT` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `RecordStatus` | `SMALLINT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayHopDongChiTiet_TCDT` | `ThucChayHopDongChiTiet_TCDT_ID` | PRIMARY KEY |
