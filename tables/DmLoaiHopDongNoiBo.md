# Table: `DmLoaiHopDongNoiBo`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmLoaiHopDongNoiBoID` | `INT` PK |  |
| `TenLoaiHopDongNoiBo` | `NVARCHAR(100)` nullable |  |
| `MaLoaiHopDong` | `NVARCHAR(50)` nullable |  |
| `DmLoaiHopDongREF` | `INT` nullable |  |
| `ThoiGiaBatDauHieuLuc` | `DATE` nullable |  |
| `ThoiGianKetThucHieuLuc` | `DATE` nullable |  |
| `CreateAt` | `DATETIME` NN |  |
| `CreatedBy` | `NVARCHAR(100)` NN |  |
| `LastModifiedBy` | `NVARCHAR(100)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmLoaiHopDongNoiBo` | `DmLoaiHopDongNoiBoID` | PRIMARY KEY |
