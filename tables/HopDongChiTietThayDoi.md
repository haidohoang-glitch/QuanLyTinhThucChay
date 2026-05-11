# Table: `HopDongChiTietThayDoi`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongChiTietThayDoiID` | `INT` PK IDENTITY | ID primary key của table HopDongChiTietThayDoi |
| `HopDongChiTietREF` | `INT` NN | ID foreign từ table HopDongChiTiet (HopDongChiTietID) |
| `HopDongFK` | `INT` NN | ID Foreign từ table HopDong (HopDongID) |
| `HopDongThayDoiREF` | `INT` NN | ID Foreign key từ table HopDongThayDoi (HopDongThayDoiID) |
| `NhanHang` | `NVARCHAR(500)` nullable | Tên nhãn hàng |
| `DmNhomNganhREF` | `NVARCHAR(250)` nullable | ID của table DmNhomNganh |
| `TenNhomNganh` | `NVARCHAR(1000)` nullable | Tên nhóm ngành |
| `DmLoaiREF` | `INT` nullable | ID từ DmHinhThucQuangCao (DmHinhThucQuangCaoID) |
| `TenLoai` | `NVARCHAR(250)` nullable | Tên hình thức quảng cáo |
| `DmNhomWebsiteREF` | `NVARCHAR(200)` nullable | ID từ table DmNhomWebsite |
| `TenNhomWebsite` | `NVARCHAR(100)` nullable | Tên nhóm website |
| `DmWebsiteREF` | `INT` nullable | ID  foreign key từ table DmWebiste |
| `TenWebsite` | `NVARCHAR(100)` nullable | Tên website |
| `DmSanPhamREF` | `INT` nullable | ID foreign key từ table DmSanPham (DmSanphamID) |
| `TenSanPham` | `NVARCHAR(100)` nullable | Tên sản phẩm |
| `DmLoaiBannerREF` | `INT` nullable | ID từ table DmLoaiBanner |
| `TenLoaiBanner` | `NVARCHAR(250)` nullable | Tên loại banner từ DmLoaiBanner |
| `DmChuyenMucREF` | `INT` nullable | ID từ table DmChuyenMuc |
| `TenChuyenMuc` | `NVARCHAR(500)` nullable | Tên chuyên mục từ table DmChuyenMuc |
| `DmViTriREF` | `INT` nullable | ID từ table DmViTri |
| `TenViTri` | `NVARCHAR(500)` nullable | Tên vị trí từ table DmViTri |
| `ThoiGian` | `NVARCHAR(50)` nullable |  |
| `SoLuong` | `INT` nullable | Số lượng |
| `DonViTinh` | `NVARCHAR(50)` nullable | Đơn vị tính |
| `DonGia` | `FLOAT` nullable | Đơn giá |
| `ChietKhau` | `FLOAT` nullable | Chiết khấu |
| `GiamGia` | `FLOAT` nullable |  |
| `TiLeTuVan` | `FLOAT` nullable |  |
| `KhuyenMai` | `NVARCHAR(350)` nullable |  |
| `IsKhuyenMai` | `INT` nullable | = 1 là phân bổ khuyến mại với chiết khấu = 100%, = 0 phân bổ không phải khuyến mại với chiết khấu <> 100% |
| `ChiPhiTuVan` | `FLOAT` nullable |  |
| `ThanhTien` | `FLOAT` nullable | Thành tiền phân bổ sau chiết khấu |
| `GhiChu` | `NVARCHAR(1000)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csHopDongChiTietThayDoi` | `HopDongChiTietThayDoiID` | PRIMARY KEY |
| `HopDong_IDX` | `HopDongChiTietREF, HopDongFK` | BTREE |
