# Table: `DataLog_QLTC_XuLylaiDuLieu`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `BIGINT` PK IDENTITY |  |
| `SoHopDong` | `NVARCHAR(200)` nullable |  |
| `BannerREF` | `NVARCHAR(200)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `Name_Table` | `NVARCHAR(500)` nullable |  |
| `Message` | `NVARCHAR(500)` nullable |  |
| `FromDate` | `DATETIME2` nullable |  |
| `ToDate` | `DATETIME2` nullable |  |
| `TimeExecutedSeconds` | `FLOAT` nullable |  |
| `Status` | `INT` nullable | 0: mới, 1: đang chạy, 2:thành công, 3:thất bại |
| `creationTime` | `DATETIME` nullable |  |
| `creatorUserId` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DataLog_XuLylaiDuLieu` | `Id` | PRIMARY KEY |
