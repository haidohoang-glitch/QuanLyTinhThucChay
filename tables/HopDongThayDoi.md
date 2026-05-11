# Table: `HopDongThayDoi`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongThayDoiID` | `INT` PK | ID primary key của table HopDongThayDoi |
| `HopDongFK` | `INT` NN | ID Foreign key từ table HopDong (HopDongID) |
| `LoaiThayDoi` | `INT` nullable | Loại thay đổi |
| `NgayThayDoi` | `DATETIME` nullable | Ngày thay đổi |
| `NganhHang` | `NVARCHAR(200)` nullable | Tên ngành hàng |
| `NhanHopDong` | `NVARCHAR(1000)` nullable | tên nhãn hàng của hợp đồng |
| `GiaTriHopDong` | `FLOAT` nullable | Giá trị hợp đồng |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csHopDongThayDoi` | `HopDongThayDoiID` | PRIMARY KEY |
| `HopDong_ChiTiet_IDX` | `HopDongFK` | BTREE |
