# Table: `CheckThongTinDauVao`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `STT` | `INT` PK IDENTITY |  |
| `NhomTruongDuLieu` | `NVARCHAR(500)` nullable |  |
| `DoiTuong` | `NVARCHAR(500)` nullable |  |
| `DoiTuongID` | `FLOAT` nullable |  |
| `DuLieuTrenSQL` | `NVARCHAR(1000)` nullable |  |
| `DuLieuTrenMySQL` | `NVARCHAR(1000)` nullable |  |
| `LoaiVanDe` | `NVARCHAR(1000)` nullable |  |
| `ThoiGianLog` | `DATETIME` nullable |  |
| `TrangThaiXuLy` | `INT` nullable |  |
| `IDLoai` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__CheckTho__CA1EB690D52A8307` | `STT` | PRIMARY KEY |
