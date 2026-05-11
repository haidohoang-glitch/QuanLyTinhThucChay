# Table: `QuyenChiTietNhomQuyenDoiTuongQuyenLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `QuyenChiTietNhomQuyenDoiTuongQuyenLogID` | `BIGINT` PK IDENTITY |  |
| `DmNhomNguoiDungREF` | `INT` NN |  |
| `DmDoiTuongQuyenFK` | `INT` NN |  |
| `TenDoiTuongQuyen` | `NVARCHAR(200)` nullable |  |
| `ChiTietDoiTuongQuyenREF` | `INT` nullable |  |
| `TenChiTietDoiTuongQuyen` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `ThoiGianLog` | `DATETIME` nullable |  |
| `NguoiLog` | `NVARCHAR(200)` nullable |  |
| `LoaiLog` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `QuyenChiTietNQTungDoiTuongQuyenREF` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_QuyenChiTietNhomQuyenDoiTuongQuyenLog` | `QuyenChiTietNhomQuyenDoiTuongQuyenLogID` | PRIMARY KEY |
