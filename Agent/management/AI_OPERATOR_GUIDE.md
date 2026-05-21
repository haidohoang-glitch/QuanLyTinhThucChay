# AI_OPERATOR_GUIDE — Hệ thống Tính Thực Chạy

> **Skill:** `ai-operator-protocol` | **Trạng thái:** 🟢 Complete
> **Ngày tạo:** 2026-05-12 | **Phiên bản:** v1.0

---

## 1. Quy tắc Bắt buộc (Mandatory Rules)

Trước khi trả lời BẤT KỲ câu hỏi nào về hệ thống, AI agent PHẢI:

1. **Đọc `context/00_MASTER_INDEX.md`** — Master nav cho toàn bộ context
2. **Xác định loại câu hỏi** theo bảng Routing ở Section 2
3. **Đọc file tương ứng** trước khi trả lời
4. **KHÔNG suy luận logic nghiệp vụ từ tên SP** — luôn đối chiếu với tài liệu

> ⚠️ **Quy tắc tuyệt đối:** Nếu không tìm thấy thông tin trong tài liệu, trả lời: *"Thông tin này chưa được tài liệu hóa — cần xác nhận với developer/BA"*. KHÔNG đoán.

---

## 2. Routing theo Loại Câu hỏi

### 2.1 Bảng routing chính

| Loại câu hỏi | File ưu tiên đọc (theo thứ tự) | Model tier |
|--------------|-------------------------------|-----------|
| **Tổng quan hệ thống là gì?** | `context/00_MASTER_INDEX.md` → `docs/01_DISCOVERY/BUSINESS_CONTEXT.md` | T1 |
| **Job X làm gì? Gồm những bước nào?** | `context/04_JOB_DESC.md` → `context/01_JOBS_AND_STEPS.md` → `jobs/[JobName].md` | T1-T2 |
| **SP X hoạt động ra sao?** | `stored_procedures/SP_[name].md` → `stored_procedures/FLOW_*.md` | T2 |
| **Luồng tính toán của nhóm SP [Y]?** | `docs/Logic_nghiepvu_tinh_thucchay.md` (hàng tương ứng) → `stored_procedures/FLOW_*.md` | T2 |
| **Schema bảng [Z]?** | `tables/[TableName].md` → `context/05_TABLE_DESC.md` → `context/06_DATA_ARCHITECTURE.md` | T1 |
| **Doanh số tính sai cho nhóm SP [X]?** | `docs/Logic_nghiepvu_tinh_thucchay.md` → `stored_procedures/FLOW_*.md` → `stored_procedures/SP_*.md` | T3 |
| **Tại sao Job fail?** | `docs/04_MAINTENANCE/runbooks/INCIDENT_JOB_FAILURE.md` → `context/01_JOBS_AND_STEPS.md` | T2 |
| **Quy tắc nghiệp vụ cho nhóm CPD/PR/Mobile/...?** | `docs/00_REQUIREMENTS/SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md` | T2 |
| **Kiến trúc tổng thể?** | `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` → `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` | T1-T2 |
| **Mối quan hệ giữa các bảng?** | `relations.md` → `context/06_DATA_ARCHITECTURE.md` | T1 |

### 2.2 Câu hỏi debug nâng cao

Khi được hỏi về **lỗi tính sai doanh số**, thực hiện theo quy trình:

```
Bước 1: Xác định nhóm sản phẩm bị ảnh hưởng
         → Đọc context/02_DM_SANPHAM.md để map DmSanPhamID

Bước 2: Xác định Job + SP xử lý nhóm đó
         → Đọc context/04_JOB_DESC.md + jobs/[JobName].md

Bước 3: Đọc logic nghiệp vụ kỳ vọng
         → Đọc docs/Logic_nghiepvu_tinh_thucchay.md (hàng tương ứng)

Bước 4: So sánh logic SP với logic kỳ vọng
         → Đọc stored_procedures/SP_[name].md

Bước 5: Kiểm tra runbook
         → Đọc docs/04_MAINTENANCE/runbooks/INCIDENT_WRONG_REVENUE.md
```

---

## 3. Context Loading Strategy (Chiến lược nạp context)

### 3.1 Khi cần trả lời câu hỏi cụ thể về 1 Job

```
LOAD (tối thiểu):
  context/04_JOB_DESC.md                    ← tổng quan job
  context/01_JOBS_AND_STEPS.md (phần job đó) ← steps chi tiết
  jobs/[JobName].md                          ← data flow diagram

LOAD (nếu cần đi sâu):
  stored_procedures/SP_*.md (các SP trong job đó)
  stored_procedures/FLOW_*.md
```

### 3.2 Khi cần trả lời về logic nghiệp vụ nhóm SP

```
LOAD (tối thiểu):
  docs/Logic_nghiepvu_tinh_thucchay.md (hàng nhóm SP tương ứng)
  docs/00_REQUIREMENTS/SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md (module tương ứng)

LOAD (nếu cần đi sâu):
  context/INPUT_LOGIC_TINH_MOI.md     ← logic tính mới
  context/INPUT_LOGIC_TINH_THAYDOI.md ← logic tính thay đổi
```

### 3.3 Danh sách nhóm SP → Module SRS

| Nhóm SP | Module SRS | Section trong Logic_nghiepvu |
|---------|-----------|--------------------------|
| CPD đợt chạy / không đợt / đơn vị gói | M3 | STT 1.0 |
| PR | M3 | STT 2.0 |
| Inventory | M3 | STT 3.0 |
| Chi phí (khác + SP chính) | M3 | STT 4.0 |
| Admarket | M3/M4 | STT 5.0 |
| Admatic | M3/M4 | STT 6.0 |
| Mua ngoài | M3/M4 | STT 7.0 |
| CPM (thuần, CPV, CPR, Trueview, Native, DVBài, DVGói, DVNgày) | M3 | STT 8.0 |
| Mobile | M3 | STT 9.0 (CTE Recursive) |
| GGFB (thực tế + sản lượng chốt) | M3 | STT 10+ |
| Marketing Fee | M3 | STT 11+ |

---

## 4. Escalation Rules

### 4.1 Khi nào tự xử lý được

| Tình huống | Action |
|------------|--------|
| Câu hỏi về tổng quan, flow, schema | Trả lời từ tài liệu — không escalate |
| Debug logic: lỗi nhỏ, rõ nguyên nhân | Cung cấp analysis + query kiểm tra |
| Câu hỏi về lịch sử thay đổi SP | Kiểm tra header SP (Tác giả, ngày sửa) |

### 4.2 Khi nào cần escalate → Developer

| Tình huống | Mức độ | Người nhận |
|------------|--------|-----------|
| Job fail và runbook không xử lý được | 🔴 Urgent | Developer on-call |
| Dữ liệu doanh số sai > 5% so với kỳ vọng | 🔴 Urgent | Developer + BA Kiểm soát |
| Cần viết SP mới để fix case đặc thù | 🟡 Normal | Developer |
| Phát hiện orphan records bất thường | 🟡 Normal | Developer + DBA |

### 4.3 Khi nào cần escalate → Business Analyst / Đội Kiểm soát

| Tình huống | Mức độ |
|------------|--------|
| Logic nghiệp vụ mơ hồ, tài liệu mâu thuẫn | 🟡 Normal |
| Case thực chạy chưa có trong `Logic_nghiepvu_tinh_thucchay.md` | 🟡 Normal |
| Câu hỏi về chốt số cuối tháng, đẩy Release | 🟡 Normal |

### 4.4 Khi nào cần escalate → Tech Lead / DBA

| Tình huống | Mức độ |
|------------|--------|
| Nghi ngờ race condition giữa các Job | 🔴 Urgent |
| Phát hiện data corruption (NULL không mong muốn, âm không được phép) | 🔴 Urgent |
| Cần thay đổi kiến trúc hoặc thêm index | 🟡 Normal |

---

## 5. Checklist Trước khi Trả lời

```
□ 1. Đã đọc context/00_MASTER_INDEX.md?
□ 2. Đã xác định đúng file cần đọc theo bảng routing?
□ 3. Câu trả lời có cite nguồn tài liệu cụ thể không?
□ 4. Có thông tin nào đoán mò (không có trong tài liệu) không?
   → Nếu có: đánh dấu rõ [CHƯA TÀI LIỆU HÓA — cần xác nhận]
□ 5. Nếu là câu hỏi debug: đã đi qua 5 bước ở Section 2.2?
```

---

## 6. Quick Reference — Mapping quan trọng

### Tên Job → File tài liệu

| Tên Job | File jobs/ |
|---------|-----------|
| `ThucChay_CPD_Chiphi_PR` | `jobs/ThucChay_CPD_Chiphi_PR.md` |
| `ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic` | `jobs/ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic.md` |
| `ThucChay_GoogleFacebook_MktFee` | `jobs/ThucChay_GoogleFacebook_MktFee.md` |
| `ThucChay_MuaNgoai` | `jobs/ThucChay_MuaNgoai.md` |
| `Job_GetInfo_ThucChay_GGFB` | `jobs/Job_GetInfo_ThucChay_GGFB.md` |
| `Job_GetInforThucTreo_PR` | `jobs/Job_GetInforThucTreo_PR.md` |
| `Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN` | `jobs/Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN.md` |
| `KiemSoat_ThucChayDaTinh` | `jobs/KiemSoat_ThucChayDaTinh.md` |
| `job_TinhLaiThucChay` | `jobs/job_TinhLaiThucChay.md` |

### Bảng đích quan trọng

| Bảng | Lớp | Mục đích |
|------|-----|---------|
| `ThucChayDaTinh` | L3 Output | Kết quả thực chạy chính (CPD, PR, CPM, Mobile, Chi phí, GGFB, MuaNgoai) |
| `ThucChayDaTinhAdmarket` | L3 Output | Kết quả thực chạy Admarket theo chiều hợp đồng |
| `ThucChayHopDongChiTiet` | L2 Normalized | Log vận hành chi tiết từng phân bổ |
| `HopDongChiTiet` | L2 | Phân bổ hợp đồng (đánh số) |
| `HopDong` | L2 | Hợp đồng gốc |
