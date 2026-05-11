# Table: `BaoCaoSPvuotHD`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `STT` | `INT` PK IDENTITY |  |
| `NgayDanhso` | `DATE` nullable |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `HopDongID` | `BIGINT` nullable |  |
| `HopDongChiTietID` | `BIGINT` nullable |  |
| `DmLoaiREF` | `INT` nullable |  |
| `htqc` | `NVARCHAR(255)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(255)` nullable |  |
| `TenLoaiBanner` | `NVARCHAR(255)` nullable |  |
| `DmViTriREF` | `INT` nullable |  |
| `TenViTri` | `NVARCHAR(255)` nullable |  |
| `SoLuong` | `FLOAT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `DonGia` | `FLOAT` nullable |  |
| `ChietKhau` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable |  |
| `SoLuong_SP` | `FLOAT` nullable |  |
| `ThucChayBanSP` | `FLOAT` nullable |  |
| `Lech` | `FLOAT` nullable |  |
| `TyLeVuot` | `FLOAT` nullable |  |
| `CreatedDate` | `DATETIME` DEFAULT getdate nullable |  |
| `NguonSP` | `VARCHAR(50)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__BaoCaoSP__CA1EB690BA284D3C` | `STT` | PRIMARY KEY |
