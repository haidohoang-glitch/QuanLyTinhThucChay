# Giá trị vận hành — Bộ Skills vs Chỉ có `docs/`

> **Mục đích:** Trả lời câu hỏi *"Có bộ skills khác gì với chỉ có folder `docs/`?"* — để stakeholder, investor, hoặc team mới hiểu ROI một cách cụ thể.
>
> **Đọc trong:** 5-10 phút.
>
> **Tham khảo bổ sung:**
> - [GETTING_STARTED.md](GETTING_STARTED.md) — overview + cách dùng
> - [WORKFLOW_GUIDE.md](WORKFLOW_GUIDE.md) — chi tiết vận hành
> - [INDEX.md](INDEX.md) — bản đồ 19 skills

---

## 1. Tóm tắt 1 câu

- **Chỉ có `docs/`:** Tài liệu là **bản ghi tĩnh** — viết ra rồi để đó, người đọc tự xoay xở, mỗi dự án 1 kiểu.
- **Có skills + `docs/`:** Tài liệu là **output của process có thể chạy lại** — có quality gate, refresh được, replicate cho 60 dự án bằng cùng 1 phương pháp.

---

## 2. So sánh theo 10 tình huống thực tế

| Tình huống | Chỉ có `docs/` (TRƯỚC) | Có skills + `docs/` (SAU) |
|------------|--------------------------|----------------------------|
| **Onboarding nhân viên mới** | Tự đọc 200 trang, hỏi senior 50 câu, mất 1-2 tuần làm quen format từng dự án | Đọc INDEX → GETTING_STARTED → biết section X ở module Y trên mọi dự án. 1-2 ngày. |
| **Khởi động dự án mới** | Bắt đầu từ blank file, copy template từ dự án cũ (đôi khi đã sai), 4-8 tuần ra bộ docs đầu tiên | Pipeline Pre-P0 → P0 → P1 → P2: 5 tuần ra audit-grade docs. AI làm 70-80% draft, người review/quyết định. |
| **Stakeholder pivot giữa chừng** | Tự đi gặp lại từng người, viết lại từng doc thủ công, dễ sót | Re-run `project-context-ingestion` → CONTEXT_PACK mới → re-run skill downstream theo dependency. Auto-detect inconsistency. |
| **Audit / SOC2 / ISO** | Mỗi audit chuẩn bị bespoke 2-4 tuần, team bị gián đoạn | Audit-grade output có sẵn. ~0 chuẩn bị. Auditor học format 1 lần, áp dụng cho mọi project. |
| **Doc-vs-code drift sau 6 tháng** | Chỉ phát hiện khi có người phàn nàn / có sự cố — thường quá muộn | `documentation-sync` chạy hàng tháng → drift surface trước khi tích lũy thành nợ |
| **Thêm 1 feature mới** | Mỗi dev viết spec theo style riêng, chất lượng nhảy cóc, không link tới SRS gốc | `feature-extension-planning` ép format chuẩn, FR mới cite tới SRS, breaking change buộc ADR mới |
| **Senior engineer rời đi** | Tribal knowledge đi theo người. 3-6 tháng đào hố lại | Methodology lưu trong skills, không trong đầu người. Người mới chạy skill → ra cùng output. |
| **AI agent execution** | Mỗi project setup AI riêng, prompt riêng, cost không kiểm soát | `ai-operator-protocol` + `multi-tier-ai-routing` áp cho mọi project. ~88% cost saving so với all-Tier-3. |
| **Sự cố production 2h sáng** | On-call mò mẫm, log vô cấu trúc, MTTR dài | Runbook có sẵn từ `incident-response-playbook` cho từng failure mode đã biết. Step-by-step commands. |
| **Cải tiến cross-project** | Cải tiến ở project A không lan sang B, C, D... | Update skill 1 lần → áp 60 project. Skill v2 → version bump → tất cả hưởng lợi. |

---

## 3. Ba ví dụ kể nhanh

### Ví dụ 1 — Project Pegasus (logistics rewrite)

Pre-Phase 0 phát hiện CEO muốn rewrite, CTO muốn refactor.

- **Trước có skills:** Phát hiện ở Phase 2 sau 2 tháng đầu tư, lãng phí ~$200K rework.
- **Sau có skills:** `project-context-ingestion` surface contradiction trước Phase 0, dừng lại 1 cuộc họp, tiết kiệm tháng work.

### Ví dụ 2 — Audit hằng năm

Công ty có 60 project. Auditor đến 1 lần/năm.

- **Trước:** Team chuẩn bị 60 × 2 tuần = **120 tuần-người (~2.5 năm-người)** chỉ riêng audit prep.
- **Sau:** Docs đã audit-grade thường xuyên, audit prep 60 × 1 ngày = **60 ngày-người (~3 tháng-người)**.

### Ví dụ 3 — Senior leaves

Tech lead rời, mang theo hiểu biết về kiến trúc 3 dự án.

- **Trước:** 3-6 tháng dev mới hiểu lại; quyết định cũ đôi khi bị đảo ngược do không ai nhớ tại sao.
- **Sau:** ADR trong `tech-solution-design` ghi WHY, BUSINESS_CONTEXT có invariants, runbook xử lý sự cố. Người mới ramp 1-2 tuần.

---

## 4. Lợi ích định lượng (ước tính)

Cho 60 project trong 1 năm:

| Hoạt động | Trước (giờ-người/năm) | Sau (giờ-người/năm) | Tiết kiệm |
|-----------|------------------------|----------------------|-----------|
| Onboarding (30 người mới/năm) | 30 × 60h = 1,800h | 30 × 8h = 240h | **1,560h** |
| Audit prep (60 project/năm) | 60 × 80h = 4,800h | 60 × 8h = 480h | **4,320h** |
| Doc maintenance (hàng tháng) | 60 × 12 × 4h = 2,880h | 60 × 12 × 1h = 720h | **2,160h** |
| Khởi động project mới (~10/năm) | 10 × 200h = 2,000h | 10 × 80h = 800h | **1,200h** |
| Sự cố MTTR (~30/năm) | 30 × 6h = 180h | 30 × 2h = 60h | **120h** |
| **TỔNG** | **~11,660h** | **~2,300h** | **~9,360h ≈ 5 năm-người** |

> Số ước tính, không phải benchmark thực — minh họa magnitude. Cost xây skills 1 lần được amortize cực nhanh khi vận hành 60+ project.

---

## 5. Hiệu ứng compounding — cái quan trọng nhất

4 lợi ích chỉ xuất hiện **sau 6-12 tháng** dùng skills, không thấy ngay:

### 5.1 Cross-project learning loop

Skill v1 → vài project chạy → tìm thấy weakness → skill v2 → tất cả project upgrade theo. Không có skills, mỗi project tự học một mình, kinh nghiệm không lan tỏa.

### 5.2 AI agents trở nên "professional"

Cùng 1 AI có thể vận hành 60 project chuẩn enterprise. Không có skills, AI là intern bị throw vô project mỗi lần phải instruct lại từ đầu.

### 5.3 Quality floor thay vì quality average

Skills có `references/checklist.md` = quality minimum bắt buộc. Không có skills, junior viết docs kém, senior không có bandwidth review hết, doc kém leak ra ngoài và tích lũy.

### 5.4 Decision archaeology

2 năm sau, hỏi "tại sao chọn AWS?" → mở ADR là biết. Không có ADR, decisions trở thành folklore — *"Tôi nghĩ là Anh A quyết hồi 2024 nhưng không nhớ tại sao"*.

---

## 6. Tradeoffs (trung thực)

Skills không miễn phí. Cần chấp nhận:

| Cost | Mức độ |
|------|--------|
| **Setup ban đầu** | ~1 tuần đào tạo 1 person/team về skills |
| **AI compute** | Skills khuyến khích AI execution → cần budget API calls (đã optimize qua tier routing) |
| **Discipline** | Stakeholder phải tôn trọng cổng G1/G2/G3 — AI không pipeline qua được (đây là feature, không phải bug) |
| **Skill maintenance** | Quý 1 lần review skill suite. Outdated skill tệ hơn không có. |
| **Vẫn cần chuyên môn nghiệp vụ** | Skill cho khuôn — content cần expert. Đặc biệt: chiến lược, đàm phán stakeholders đối kháng, regulatory deep-dive. |

---

## 7. Khi nào skills KHÔNG mang lại lợi ích đáng kể

Để cân bằng — nếu các điều kiện sau đều đúng, ROI thấp:

- Công ty có **<5 project**, mỗi project **<3 tháng** → overhead lớn hơn benefit
- Team rất ổn định, **không có thay đổi người trong 5+ năm** → tribal knowledge OK
- **Không có audit/compliance** → không cần audit-grade docs
- Mỗi project đặc thù 100%, **không reuse được pattern** → standardization vô nghĩa

Công ty có 60+ project = không rơi vào nhóm này. Skills xứng đáng đầu tư.

---

## 8. Tổng kết — metaphor

**Trước (chỉ `docs/`):**
Mỗi project là 1 đảo. Tài liệu phụ thuộc người viết. Knowledge phụ thuộc người ở. Cải tiến không lan tỏa.

**Sau (skills + `docs/`):**
Tài liệu là sản phẩm của hệ thống. Hệ thống thuộc về công ty, không phải cá nhân. Cải tiến áp lên toàn bộ portfolio. AI vận hành được ở chuẩn enterprise.

> **Metaphor:**
> *Trước:* Mỗi project có 1 đầu bếp riêng, công thức riêng, khách quen mất 1 tháng nhớ menu.
>
> *Sau:* Cả chuỗi 60 nhà hàng dùng 1 cookbook. Đầu bếp luân chuyển dễ. Khách đến nhà hàng nào cũng tìm được món quen. Cookbook nâng cấp → cả chuỗi nâng theo.

---

## 9. Kết luận hành động

Bộ skills đã build xong:
- **19 skills** organized theo 5 phase + cross-cutting
- **100+ files**, ~18.7k dòng methodology
- **3 tầng tài liệu**: INDEX → GETTING_STARTED → WORKFLOW_GUIDE
- Pipeline đã verify (Pre-P0 → P0 → P1 → P2 → P3 → P4)

**Việc còn lại** là vận hành thực tế:
1. Pilot với 1-2 project trong 4-6 tuần để verify ROI giả định
2. Đào tạo 1 cohort nhân sự (5-10 người) làm "skill-fluent operators"
3. Triển khai rollout cho project tiếp theo (legacy audit hoặc greenfield)
4. Quý 1 lần review skill suite, cập nhật theo feedback

Sau 6-12 tháng, hiệu ứng compounding bắt đầu bộc lộ — và ở thời điểm đó, công ty sẽ có **methodology asset** thay vì **document collection**.

---

*Skills là phương tiện. Mục đích là: vận hành 60 dự án với chất lượng đồng đều, chi phí thấp, knowledge không bị thất thoát khi người đến/đi.*
