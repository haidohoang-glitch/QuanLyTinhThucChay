# Table: `DmThongTinHopDongBanInventory`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmThongTinHopDongBanInventoryID` | `INT` NN IDENTITY |  |
| `HopDongREF` | `INT` NN |  |
| `SoHopDong` | `NVARCHAR(100)` NN |  |
| `NgayDanhSo` | `DATETIME` NN |  |
| `DmNhanVienREF` | `INT` NN |  |
| `DmKhachHangREF` | `INT` NN |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(300)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
