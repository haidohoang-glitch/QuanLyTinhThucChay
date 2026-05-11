# Table: `ThucTreoHopDongChiTietAdmarket`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucTreoHopDongChiTietAdmarketID` | `INT` PK |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `HopDongREF` | `INT` nullable |  |
| `SoHopDong` | `NVARCHAR(200)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `CampaignID` | `INT` nullable |  |
| `CampaignName` | `NVARCHAR(200)` nullable |  |
| `TK_AdmarketID` | `INT` nullable |  |
| `TK_Admarket` | `NVARCHAR(200)` nullable |  |
| `NgayNhanVienYeuCau` | `DATETIME` nullable |  |
| `RetryCount` | `INT` nullable |  |
| `ThoiGianCapNhat` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecodStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucTreoHopDongChiTietAdmarket` | `ThucTreoHopDongChiTietAdmarketID` | PRIMARY KEY |
