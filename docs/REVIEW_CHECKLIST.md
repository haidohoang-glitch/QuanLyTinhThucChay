# 📋 Checklist Review Tài liệu — Hệ thống QuanLyTinhThucChay

> **Mục đích:** Đối chiếu tính chính xác của tài liệu với nghiệp vụ thực tế và logic tính toán của hệ thống.
> **Kết quả mong muốn:** Tài liệu đủ chất lượng để xây dựng AI Skill/Agent phục vụ 3 tình huống:
> 1. 🆕 **Thêm mới** nghiệp vụ tính sản phẩm
> 2. ✏️ **Chỉnh sửa** cách tính sản phẩm hiện tại
> 3. 💬 **Trả lời câu hỏi** của đội Kiểm soát về logic tính toán

**Cách dùng checklist:**
- `[ ]` Chưa review
- `[/]` Đang review
- `[x]` Đã xác nhận đúng
- `[!]` Phát hiện sai lệch / cần bổ sung

---

## 🔴 NHÓM 1 — Công thức tính & Logic lõi (PHẢI review trước)
> Ảnh hưởng trực tiếp đến tính chính xác của số liệu tài chính

### Tài liệu 1.1 — Logic nghiệp vụ chi tiết
#### A. Điều kiện nhận diện sản phẩm (Filters)
- [x] **CPD:** Xác nhận danh sách `DmSanPhamID IN (140, 228, 241, 564, 549, 5082)` còn đầy đủ và chính xác? Có SP nào mới thêm/xóa? *(Đã xác nhận đúng)*
- [x] **CPD Loại trừ:** Điều kiện `NOT (DmHinhThucQuangCao IN (42, 13) OR DmLoaiBannerREF = 18)` có còn đúng? *(Đã xác nhận đúng)*
- [x] **PR:** `DmSanPhamREF IN (141, 245, 250, 637, 305)` — xác nhận danh sách SP *(Đã xác nhận đúng)*
- [ ] **Chi phí:** Điều kiện dựa vào `CauHinhNhomTinhDoanhSoThucChay` (`NhomTinhDoanhSoThucChay = 1`) — xác nhận mapping
- [x] **CPM:** `NhomTinhDoanhSoThucChay = 2` — xác nhận mapping *(Đã xác nhận đúng)*
- [x] **Mobile:** `DmSanPhamREF = 342` — xác nhận duy nhất 1 sản phẩm? *(Đã xác nhận đúng)*
- [ ] **Admatic:** `DmHinhThucQuangCao = 42` — xác nhận điều kiện
- [x] **GG-FB:** `DotChayHopDong = 'ThanhTien_GGFB'` — xác nhận giá trị literal đúng không? *(Đã xác nhận đúng)*

#### B. Công thức tính mới (New Calculation Formulas)

**CPD Đợt chạy (Loại A):**
- [x] Công thức `TT = (SL_danhso × DG_danhso / songaydotchay_danhso) × (1 - CK_danhso%)` — xác nhận đúng
  > 💡 **Mapping chi tiết nguồn dữ liệu:**
  > - `SL_danhso`: Cột `SoLuong` trong bảng `HopDongChiTiet`.
  > - `DG_danhso`: Cột `DonGia` trong bảng `HopDongChiTiet`.
  > - `songaydotchay_danhso` (SoLuongDotChayHD): Tổng số ngày trong lịch phân bổ đợt chạy (`SUM(DATEDIFF(day, ThoiGianBatDau, ThoiGianKetThuc) + 1)` trong bảng `DotChayHopDongChiTiet` tương ứng với `HopDongChiTietID`).
  > - `CK_danhso%`: Cột `ChietKhau` trong bảng `HopDongChiTiet`.
- [x] `Soluongchay_moingaytreo = 1` — xác nhận không phụ thuộc số lượng thực treo? *(Đã xác nhận đúng)*
- [x] `Donvitinh = ngày` — xác nhận đơn vị *(Đã xác nhận đúng)*

**CPD Không đợt chạy (Loại B):**
- [x] Công thức `TT = (SL_danhso × DG_danhso / tongsongaytreo) × (1 - CK_danhso%)` — xác nhận đúng
  > 💡 **Mapping chi tiết nguồn dữ liệu:**
  > - `SL_danhso`: Cột `SoLuong` trong bảng `HopDongChiTiet`.
  > - `DG_danhso`: Cột `DonGia` trong bảng `HopDongChiTiet`.
  > - `tongsongaytreo` (SoLuongDotChayBooking): Tổng số ngày treo lịch sử của dòng treo có trạng thái duyệt (`SUM(DATEDIFF(day, ThoiGianBatDau, ThoiGianKetThuc) + 1)` trong bảng `ThucChayHopDongChiTiet` tương ứng với `HopDongChiTietREF`).
  > - `CK_danhso%`: Cột `ChietKhau` trong bảng `HopDongChiTiet`.
- [x] `tongsongaytreo` tính như thế nào? Tổng tất cả ngày treo lịch sử hay chỉ trong kỳ? *(Đã xác nhận đúng: Tổng tất cả ngày treo lịch sử của các dòng treo được duyệt)*

**CPD Đơn vị gói (Loại C):**
- [x] `TT = SL_danhso × DG_danhso × (1 - CK%)` — xác nhận ghi nhận **full 100%** ngay lần đầu có treo? *(Đã xác nhận đúng)*
- [x] Nếu có nhiều ngày treo, hành xử thế nào? Chỉ ghi nhận 1 lần? *(Xác nhận: **Chỉ ghi nhận 01 lần**)*

**PR:**
- [x] `TT = SLtreo × Giatientreo × (1 - CKtreo%)` — xác nhận đơn giá lấy từ dòng treo (không phải đánh số)? *(Đã xác nhận đúng)*

**Chi phí:**
- [x] `TT = SoLuongTreo × DonGiaTreo × (1 - CK%)` — xác nhận đúng *(Đã xác nhận đúng)*
- [x] Cơ chế **anti-overcap**: nếu `TT_datinh + TT_treo > GiaTriPhanBo` thì phần dôi bị loại bỏ — xác nhận logic này?
  > 🔍 **Kết quả check Stored Procedure (`[dbo].[ThucChay_ChiPhiKhac]`):**
  > - Cơ chế anti-overcap sử dụng `CTE_Recursive` để tính lũy kế số tiền sau chiết khấu (`TichLuyThanhTienSauCK`).
  > - **Khác biệt cốt lõi:** Nếu dòng treo hiện tại làm tổng lũy kế vượt quá phân bổ (`ThanhTienSauCKDaTinh + ThanhTienSauCKTreo > ThanhTienSauCKPhanBo`), hệ thống sẽ **bỏ qua hoàn toàn dòng đó** (ghi nhận bằng `0` và không tính mới hoặc đối trừ sang `ThucChayDaTinh`), chứ **không tính một phần** (không partial-fill) để vừa khít phân bổ.
  > - Đối với **CPM** (ví dụ `[dbo].[ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh]`), hệ thống **tính một phần** vừa đủ phần còn thiếu để đạt 100% phân bổ, phần dôi ra được ghi nhận vào cột `SoLuongThucChayLechTreoHa` (Lệch treo hạ).
- [x] Khi `IsKhuyenMai = 1` hoặc `CK = 100`: giá trị chuyển thành 0, ghi vào `SoLuongThucChayKM` — xác nhận?
  > 📝 **Xác nhận từ nghiệp vụ:**
  > - Nếu giá trị/tiền thì ghi nhận vào cột `ThanhTienKM` (đối với CPD và Chi phí).
  > - Nếu số lượng thì ghi nhận vào cột `SoLuongThucChayKM`.

**Mua Ngoài và GG-FB (3 chỉ số):**
- [ ] `ThanhTienBan = ThanhTien_KQVH × (1 - CK_danhso%)` — xác nhận
- [ ] `ThanhTienMua` lấy từ đâu? (GG-FB: `ADS_Operating_Result`, Mua Ngoài: `ThucChayMuaNgoaiChiTiet`)
- [ ] `ThanhTienLai = ThanhTienBan - ThanhTienMua` — xác nhận

#### C. Logic tính thay đổi (Change/Offset Logic)
- [ ] TH thay đổi thông tin đánh số (SL, DG, CK) → thay đổi `TTthucchaysauCK_denngaytinh` — xác nhận chiều đối trừ
- [ ] TH thay đổi thuộc tính (sohopdong, nhanvienID...) → đối trừ và ghi bản ghi thuộc tính mới — xác nhận
- [ ] TH xóa phân bổ → đối trừ toàn bộ về 0 — xác nhận
- [ ] TH thay đổi thông tin treo (SLtreo) → cập nhật các trường `_denngaytinh` — xác nhận
- [ ] Công thức đối trừ: `GiaTriThayDoi = After − Before` — xác nhận hướng tính

---

### Tài liệu 1.2 — [M3-M8_FUNCTIONAL_REQUIREMENTS.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/00_REQUIREMENTS/SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md)
*Tài liệu SRS đã hệ thống hóa lại — kiểm tra xem có mất thông tin hay không*

#### A. Nhóm CPD (Mục 3.1)
- [x] 3 loại A/B/C có khớp với Logic_nghiepvu không? *(Đã xác nhận đúng)*
- [x] Tên bảng nguồn `HopDongChiTiet`, `DotChayHopDongChiTiet`, `ThucChayHopDongChiTiet` — xác nhận đúng? *(Đã xác nhận đúng)*
- [x] Tên Stored Procedure `[dbo].[ThucChay_CPD_Job]` — xác nhận tên đúng trong DB? *(Đã xác nhận đúng)*

#### B. Nhóm PR (Mục 3.2)
- [ ] Bảng nguồn `ThucChayHopDongChiTietPR` — khác với CPD, xác nhận đây là bảng đúng?
- [ ] Không dùng đơn giá từ HopDongChiTiet, mà dùng `Giatientreo` từ dòng treo — xác nhận?

#### C. Nhóm Chi Phí (Mục 3.3)
- [ ] Loại trừ HDBAN_INVENTORY và Vị trí `100093, 100478` — xác nhận 2 vị trí ID này còn đúng?
- [ ] Cơ chế anti-overcap có được mô tả đủ trong tài liệu SRS?

#### D. Nhóm CPM - 8 Loại con (Mục 3.4)
- [ ] Xác nhận đủ 8 loại CPM là gì? (Tài liệu chỉ ghi "8 loại" nhưng không liệt kê đủ tên)
- [ ] CPM đơn vị ngày: `TT = DonGia × TiLeBannerSiteHDCT × (1 - CK%)` — xác nhận công thức?

#### E. Nhóm Admatic (Mục 3.5)
- [ ] `TiLeThucChay = TiLeThucChayHDCTSoVoiBanner / 100` — xác nhận tên cột chính xác trong DB?
- [ ] `TT = (TT_SauCK_ChuaVAT_VanHanh × TiLeThucChay) × (1 - CK%)` — xác nhận có nhân (1 - CK%) không hay bỏ qua CK ở bước này?

#### F. Nhóm Mobile (Mục 3.6)
- [ ] Công thức CTE Recursive: `IIF(TichLuyCu + PhatSinhMoi >= GiaTriPhanBo, GiaTriPhanBo - TichLuyCu, PhatSinhMoi)` — xác nhận đây là logic chốt chặn đúng không?
- [ ] Khi `TichLuyCu >= GiaTriPhanBo`: ghi 0 hay không ghi? — cần xác nhận rõ

#### G. Nhóm Admarket (Mục 3.7)
- [ ] Giá trị lấy từ `TT = ThanhTienThucChay_VanHanh` — xác nhận tên cột trong `ThucChayAdmarket_PhanBo`?
- [ ] Performance Base là gì? Tài liệu chưa giải thích rõ cơ chế tính

#### H. Nhóm GG-FB (Mục 3.8)
- [ ] `DotChayHopDong = N'ThanhTien_GGFB'` — chữ `N` prefix (Unicode) có quan trọng cho filter?
- [ ] MKT Fee tính như thế nào? Tài liệu chỉ liệt kê step 2 mà chưa có công thức

#### I. Nhóm Inventory (Mục 3.9)
- [ ] `ThanhTienThucChay = ThanhTienPhanBo` — xác nhận ghi nhận full toàn bộ giá trị phân bổ ngay khi có treo?
- [ ] Điều kiện `HopDongChiTietRef IN DmHopDongBanInventory` — xác nhận tên bảng/view?

#### J. Nhóm Mua Ngoài (Mục 3.10)
- [ ] Xác nhận bảng nguồn: `HopDongChiTiet_MuaNgoai` và `ThucChayMuaNgoaiChiTiet` — đúng không?

---

## 🟠 NHÓM 2 — Quy tắc nghiệp vụ chung & Vận hành
> Ảnh hưởng đến tính nhất quán của toàn hệ thống

### Tài liệu 2.1 — [BUSINESS_CONTEXT.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/01_DISCOVERY/BUSINESS_CONTEXT.md)

#### A. Mục 4 — Bảng 11 Nhóm Sản phẩm
- [ ] Xác nhận đủ 11 nhóm SP (CPD đợt chạy, CPD không đợt, CPD gói, PR, Chi phí, Admarket, CPM, Mobile, Admatic, Mua Ngoài, GG-Facebook)?
- [ ] **Lưu ý:** Inventory và Performance Base được xếp là "loại con" — có phải tách ra thành nhóm riêng không?
- [ ] Creator Content có phải là nhóm SP độc lập? Hiện đang xếp vào "Chi phí" — xác nhận?

#### B. Mục 6.1 — Quy tắc chung
- [ ] **BR-001** (`DeletedStatus = 1` → đối trừ về 0): Xác nhận đây là xóa HĐ hay xóa HĐCT?
- [ ] **BR-002** (làm tròn 2 chữ số thập phân): Kiểu làm tròn nào? ROUND() hay CAST? Làm tròn trước hay sau khi cộng dồn?
- [ ] **BR-003** (1 banner chỉ gắn 1 SP 1 thời điểm): Áp dụng cho CPM, Admatic, Mobile — xác nhận Admatic đúng không?
- [ ] **BR-004** (không vượt giá trị phân bổ): Nhóm nào được phép vượt theo cấu hình (`NhomTinhDoanhSoThucChay_ChoPhepVuotGiaTri`)?
- [ ] **BR-005** (Đối trừ = After − Before): Có trường hợp nào Đối trừ = Before − After không?

#### C. Mục 6.3 — Quy tắc thay đổi & đối trừ
- [ ] **BR-C-04**: CDC bắt thay đổi từ bảng nào? Xác nhận danh sách bảng được CDC monitor?
- [ ] Các bảng `*ThayDoi`, `*Log` — hiện có bảng nào đang thiếu audit trail?

#### D. Mục 7 — Workflows
- [ ] Giờ chạy `01:00 / 07:xx / 08:00` — xác nhận giờ chính xác của từng job?
- [ ] 4 Calc Jobs chạy **song song** hay **tuần tự**? Tài liệu ghi "SONG SONG / TUẦN TỰ" — cần xác nhận rõ
- [ ] Sau tính mới xong, `job_TinhLaiThucChay` chạy khi nào? Cùng lúc hay sau đó?

---

## 🟡 NHÓM 3 — Ánh xạ Kỹ thuật & Luồng Dữ liệu
> Quan trọng để đảm bảo tài liệu trỏ đúng code thực tế

### Tài liệu 3.1 — [M10_TRACEABILITY.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/00_REQUIREMENTS/SRS_VI/M10_TRACEABILITY.md)
- [ ] **FR-GL-01** → SP `*GhiNhanThayDoi_ThucChayDaTinh`: Tên SP đúng không? Có phải là prefix của nhiều SP?
- [x] **FR-CPD-01/04**: SP `[dbo].[ThucChay_CPD_Job]` — xác nhận tên đầy đủ và đúng schema? *(Đã xác nhận đúng)*
- [ ] **FR-CP-01/03**: Chi phí có 3 loại con (ChiPhiKhac + Creator Content) — Ma trận có bao gồm đủ?
- [ ] **FR-CPM-01/03**: CPM và Admatic gộp chung — cần tách ra cho rõ ràng?
- [ ] Mục 10.2 — Sync Traceability: `Job_GetInforThucTreo_ThucChayMuaNgoai...` — tên đầy đủ là gì? (tên hiện tại bị cắt)

### Tài liệu 3.2 — [DATA_ARCHITECTURE.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/01_DISCOVERY/DATA_ARCHITECTURE.md)

#### A. Mục 3 — Bảng ThucChayDaTinh (Bảng đích chính)
- [ ] Xác nhận các cột hiện tại đủ không: `LoaiXuLy`, `GhiChu`, `IsKhuyenMai`? (Runbook có nhắc đến nhưng architecture không liệt kê)
- [ ] Cột `ThanhTienKhuyenMai` vs `ThanhTienKM` — tên chính xác trong DB là gì?
- [ ] Cột `NgayTinhThucChay` vs `NgayThucHien` — tài liệu dùng 2 tên khác nhau, cái nào đúng?

#### B. Mục 5 — Data Flow
- [ ] Luồng ghi nhận cho Admatic có dùng bảng `ThucChayDaTinhAdmarket` — tài liệu có ghi nhưng mapping chưa thể hiện rõ điều kiện nào ghi vào bảng phụ này?
- [ ] Creator Content → bảng đích nào? (Codebase Map ghi cả `ThucChayDaTinh` lẫn `ThucChayDaTinh_MuaNgoai`)

#### C. Mục 4 — Virtual Foreign Keys
- [ ] `ThucChayDaTinhAdmarket.ThucChayDaTinhREF` → `ThucChayDaTinh` là quan hệ 1:1 — xác nhận đúng không?
- [ ] `ThucChayDaTinh_MuaNgoai.ThucChayDaTinhREF` — xác nhận tên cột đúng?

### Tài liệu 3.3 — [CODEBASE_MAP.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/01_DISCOVERY/CODEBASE_MAP.md)
- [ ] Mục 4.1 — Job_GetInforThucTreo Step 2: `ThucTreoHopDongChiTietTrinhDuyet_ThucTreo` — tên bảng đích có đúng không?
- [ ] Step 5-10 của Job sync ghi là `[COMMENT - có job riêng]` — đây là gì? Cần bổ sung?
- [ ] OQ-03: `job_TinhLaiThucChay` và `KiemSoat_ThucChayDaTinh` có trong scope không? Nếu có cần bổ sung vào tài liệu

---

## 🟢 NHÓM 4 — Rủi ro & Runbook Vận hành
> Đảm bảo tài liệu phản ánh đúng quy trình xử lý sự cố thực tế

### Tài liệu 4.1 — [TECH_DEBT_AUDIT.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/01_DISCOVERY/TECH_DEBT_AUDIT.md)
- [ ] **TD-002** (Hardcode ID): Ngoài `DmSanPhamID`, còn hardcode gì nữa (ngưỡng %, ngày cụ thể...)?
- [ ] **TD-003** (Race Condition): Hiện tại đã có cơ chế kiểm tra dependency chưa? Hay vẫn phụ thuộc lịch schedule?
- [ ] **TD-006** (Linked Server): Có SLA cụ thể nào cho việc phục hồi khi Linked Server chết không?
- [ ] Mục 4 — Punch List: Các hành động TD-004, TD-005 chưa có trong danh sách — có cần ưu tiên không?

### Tài liệu 4.2 — [INCIDENT_WRONG_REVENUE.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/04_MAINTENANCE/runbooks/INCIDENT_WRONG_REVENUE.md)
- [ ] Bảng công thức tại Bước 2 (mục "Bảng tra công thức kỳ vọng"): có khớp với tài liệu Logic_nghiepvu không? (Hiện thiếu Admarket, GG-FB, Inventory, Mua Ngoài)
- [ ] Query Bước 2: cột `LoaiXuLy`, `GhiChu` trong SELECT — xác nhận tồn tại trong `ThucChayDaTinh`?
- [ ] Bước 3: Query kiểm tra dữ liệu nguồn chỉ cho nhóm CPD — cần bổ sung query cho PR, CPM, GG-FB?
- [ ] SP `job_ThucChayDaTinh_ReInsertByHopDong` tại Bước 4 — xác nhận tên SP đúng không?
- [ ] Phần "Phòng tránh": Alert khi doanh số lệch > 15% — có WP-C02 ghi là "Chưa có" — đây đã được xây dựng chưa?

### Tài liệu 4.3 — [INCIDENT_JOB_FAILURE.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/04_MAINTENANCE/runbooks/INCIDENT_JOB_FAILURE.md)
- [ ] Quy trình xử lý khi Job lỗi có bao gồm bước kiểm tra xem Job đã tính một phần chưa?
- [ ] Hướng dẫn rollback khi Job Calc chạy 50% rồi lỗi — có hay chưa?

### Tài liệu 4.4 — [INCIDENT_DATA_SYNC_FAIL.md](file:///d:/QuanLyTinhThucChay/QuanLyTinhThucChay/docs/04_MAINTENANCE/runbooks/INCIDENT_DATA_SYNC_FAIL.md)
- [ ] Có hướng dẫn khi Linked Server đến HDCN đứt — nên bỏ qua tính hay đợi?
- [ ] Khi sync thất bại, dữ liệu cũ vẫn còn trong staging — tính trên dữ liệu cũ hay skip?

---

## 📊 Tổng kết Review

| Nhóm | Số điểm cần review | Trọng số | Trạng thái |
|---|---|---|---|
| 1 - Core Logic (1.1 + 1.2) | ~35 điểm | ⭐⭐⭐⭐⭐ Critical | `[ ]` Chưa bắt đầu |
| 2 - Business Rules (2.1) | ~12 điểm | ⭐⭐⭐⭐ High | `[ ]` Chưa bắt đầu |
| 3 - Traceability (3.1–3.3) | ~15 điểm | ⭐⭐⭐ Medium | `[ ]` Chưa bắt đầu |
| 4 - Runbooks (4.1–4.4) | ~12 điểm | ⭐⭐ Standard | `[ ]` Chưa bắt đầu |

---

## 🤖 Tiêu chí "Đủ điều kiện" cho AI Agent

Sau khi review xong, tài liệu đạt chất lượng để xây dựng AI Agent khi đáp ứng:

### Cho Agent "Thêm nghiệp vụ tính sản phẩm mới"
- [ ] Tất cả điều kiện nhận diện sản phẩm (filter logic) đã được xác nhận chính xác
- [ ] Bảng cấu hình `CauHinhNhomTinhDoanhSoThucChay` được document đủ các cột và ý nghĩa
- [ ] Template SP mẫu cho "Tính mới" và "Tính thay đổi" được mô tả trong tài liệu

### Cho Agent "Chỉnh sửa cách tính sản phẩm"
- [ ] Mapping rõ: Nhóm SP → Job → Step → SP cụ thể (không có gap)
- [ ] Tài liệu CODEBASE_MAP đã bổ sung đầy đủ các SP còn thiếu (`job_TinhLaiThucChay`...)
- [ ] Luồng đối trừ (offset) được document đủ cho cả 11 nhóm SP

### Cho Agent "Trả lời câu hỏi Kiểm soát"
- [ ] Tất cả công thức tính đã được xác nhận và có ví dụ số cụ thể
- [ ] Runbook INCIDENT_WRONG_REVENUE có bảng tra công thức đủ 11 nhóm SP
- [ ] Các câu hỏi Open Questions trong tài liệu đã được trả lời hết

---

*Checklist này được tạo tự động từ cấu trúc tài liệu hiện tại ngày 2026-05-20*
