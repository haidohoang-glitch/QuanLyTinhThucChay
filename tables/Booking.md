# Table: `Booking`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `BookingID` | `INT` PK |  |
| `NgayBatDau` | `DATETIME` nullable |  |
| `NgayKetThuc` | `DATETIME` nullable |  |
| `Status` | `INT` nullable |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `SoLuongTheoDV` | `INT` nullable |  |
| `DonViTinh` | `INT` nullable | WEEK = 1, THANG = 2, NGAY = 3, CPM = 4 |
| `SoLuong` | `FLOAT` nullable |  |
| `TenWebsite` | `NVARCHAR(250)` nullable |  |
| `DmWebsiteREF` | `NVARCHAR(400)` nullable |  |
| `HinhThucSP` | `TINYINT` PK | Hình Thức sản phẩm: <br>=1 CPD<br>=2 CPM<br>= 3 PR |
| `TenHinhSanPham` | `NVARCHAR(250)` nullable |  |
| `MaSanPham` | `TINYINT` PK | MaSanPham: <br>when 1 then  N'Banner - CPD'<br>when 2 then  N'Box App CPD'<br>when 3 then  N'CPM 7000 - CPM'<br>when 4 then  N'CPM Mass - CPM'<br>when 5 then  N'Balloon Ads - CPM'<br>when 6 then  N'CPM mobile - CPM'<br>when 7 then  N'CPM Admarket - CPM'<br>when 8 then  N'TVC Online - CPM'<br>when 9 then  N'Box App CPM' |
| `TenSanPham` | `NVARCHAR(250)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` NN |  |
| `TenDonViTinh` | `NVARCHAR(50)` nullable |  |
| `TagNhomWebsite` | `NVARCHAR(250)` nullable |  |
| `DmTagNhomWebsiteID` | `INT` nullable |  |
| `ChuyenMuc` | `NVARCHAR(250)` nullable |  |
| `DmChuyenMucID` | `INT` nullable |  |
| `TenBanner` | `NVARCHAR(250)` nullable |  |
| `DmBannerID` | `NCHAR(10)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `Booking_IDX` | `BookingID, NgayBatDau, NgayKetThuc, Status, HinhThucSP` | BTREE |
| `PK_Booking` | `BookingID, HinhThucSP, MaSanPham` | PRIMARY KEY |
