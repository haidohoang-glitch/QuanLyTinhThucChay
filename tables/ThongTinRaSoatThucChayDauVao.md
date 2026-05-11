# Table: `ThongTinRaSoatThucChayDauVao`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `LoaiCheck` | `NVARCHAR(50)` nullable |  |
| `DoiTuong` | `NVARCHAR(50)` nullable |  |
| `VanDe` | `NVARCHAR(200)` nullable |  |
| `TruongDuLieuCheck` | `NVARCHAR(50)` nullable |  |
| `TruongDuLieuLuu` | `NVARCHAR(50)` nullable |  |
| `DanhSachID` | `NVARCHAR(MAX)` nullable |  |
| `NgayLog` | `DATETIME` nullable |  |
| `ThoiGianBatDauCheck` | `DATETIME` nullable |  |
| `ThoiGianKetThucCheck` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_RaSoatThucChayDauVao` | `ID` | PRIMARY KEY |
