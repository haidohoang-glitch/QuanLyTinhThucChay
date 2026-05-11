# Table: `KhachHangNguoiLienHe`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `KhachHangNguoiLienHeID` | `INT` PK |  |
| `KhachHangThongTinChungFK` | `INT` nullable |  |
| `TenNguoiLienHe` | `NVARCHAR(200)` nullable |  |
| `AccountNguoiLienHe` | `NVARCHAR(200)` nullable |  |
| `ChucVu` | `NVARCHAR(200)` nullable |  |
| `Email` | `NVARCHAR(200)` nullable |  |
| `Email2` | `NVARCHAR(200)` nullable |  |
| `Mobile` | `NVARCHAR(200)` nullable |  |
| `Mobile2` | `NVARCHAR(200)` nullable |  |
| `SoDienThoai` | `NVARCHAR(200)` nullable |  |
| `SoFax` | `NVARCHAR(200)` nullable |  |
| `DiaChiLienHe` | `NVARCHAR(200)` nullable |  |
| `NgaySinh` | `DATETIME` nullable |  |
| `GioiTinh` | `NVARCHAR(200)` nullable |  |
| `ThongTinKhac` | `NVARCHAR(200)` nullable |  |
| `Active` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(200)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_KhachHangNguoiLienHe` | `KhachHangNguoiLienHeID` | PRIMARY KEY |
