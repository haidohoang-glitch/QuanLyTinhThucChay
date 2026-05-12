# AI_AGENT_TASK_DISTRIBUTION — Hệ thống Tính Thực Chạy

> **Skill:** `multi-tier-ai-routing` | **Trạng thái:** 🟢 Complete
> **Ngày tạo:** 2026-05-12 | **Phiên bản:** v1.0

---

## 1. Tier Definitions (Định nghĩa tier cho dự án này)

| Tier | Mục đích | Model khuyến nghị | Cost ratio |
|------|----------|-------------------|-----------|
| **T3 Strong** | Phân tích logic nghiệp vụ phức tạp, debug SP multi-step, viết SRS, ADRs | Claude Opus 4.7 / GPT-5 o-series | 25× |
| **T2 Mid** | Gen tài liệu từ data có sẵn, đọc SP, tổng hợp structured, runbook template | Claude Sonnet 4.6 / Gemini 2.x Pro | 5× |
| **T1 Simple** | Chạy scripts, format Markdown, cập nhật links, gen boilerplate, query lookup | Claude Haiku 4.5 / Gemini 2.x Flash | 1× |
| **Human** | Approve ADRs, phê duyệt chốt số, quyết định fix TD-001, deploy production | — | Operator time |

---

## 2. Task Routing Matrix

### 2.1 Documentation Tasks

| Task | Tier | Model | Lý do |
|------|------|-------|-------|
| Đọc tổng quan hệ thống, trả lời câu hỏi đơn giản | T1 | Haiku 4.5 | Chỉ tra cứu tài liệu |
| Gen `CODEBASE_MAP.md` từ data đã có | T2 | Sonnet 4.6 | Tổng hợp structured data |
| Gen `DATA_ARCHITECTURE.md` từ relations + tables/ | T2 | Sonnet 4.6 | Structured extraction |
| Cập nhật `INDEX.md`, format links | T1 | Haiku 4.5 | Format-only |
| Viết `BUSINESS_CONTEXT.md` (logic nghiệp vụ) | T3 | Opus 4.7 | Domain sâu, nhiều nuance |
| Reverse-engineer SRS từ SP code | T3 | Opus 4.7 | Long context + cross-reference |
| Viết ADRs cho kiến trúc | T3 | Opus 4.7 | Judgment + alternatives |
| Gen runbook từ template | T2 | Sonnet 4.6 | Template-based + domain input |
| Tạo `DOC_SYNC_REPORT.md` | T1-T2 | Haiku → Sonnet | Pattern matching |

### 2.2 Development & Debugging Tasks

| Task | Tier | Model | Lý do |
|------|------|-------|-------|
| Chạy `generate_*.py` scripts | T1 | Haiku 4.5 | Execute only |
| Đọc schema bảng đơn lẻ | T1 | Haiku 4.5 | Lookup |
| Debug Job fail (xem log, identify step) | T2 | Sonnet 4.6 | Structured analysis |
| Debug doanh số sai — trace 1 SP | T2 | Sonnet 4.6 | Code reading |
| Debug doanh số sai — trace multi-SP (offset chain) | T3 | Opus 4.7 | Multi-SP analysis + judgment |
| Viết SP mới cho case đặc thù (fix nhỏ) | T2 | Sonnet 4.6 | Code gen với context rõ |
| Thiết kế SP mới phức tạp (logic mới) | T3 | Opus 4.7 | Architecture + business rules |
| Audit orphan records (WP-B02) | T2 | Sonnet 4.6 | Query + analysis |
| Thiết kế FK migration plan (WP-B04) | T3 | Opus 4.7 | Risk + dependency analysis |

### 2.3 Operations & Maintenance Tasks

| Task | Tier | Model | Lý do |
|------|------|-------|-------|
| Xử lý sự cố theo runbook (triage) | T2 | Sonnet 4.6 | Structured + judgment |
| Post-incident review (bài học) | T3 | Opus 4.7 | Insights + lessons learned |
| Monthly doc-sync check | T1-T2 | Haiku → Sonnet | Pattern match code-vs-doc |
| Quarterly consistency review | T2 | Sonnet 4.6 | Cross-doc analysis |
| Feature extension planning (SP mới cho nhóm SP mới) | T2 | Sonnet 4.6 | Mini-spec |

---

## 3. Cost Projection

### 3.1 Phase A — Documentation (Đã hoàn thành)

| WP | Task | Tier | Est. tokens | Est. cost |
|----|------|------|-------------|-----------|
| WP-A01 | AI Operator Guide | T2 | 8K | ~$0.04 |
| WP-A02 | AI Task Distribution | T2 | 6K | ~$0.03 |
| WP-A03–A05 | 3 Runbooks | T2 | 15K | ~$0.08 |
| WP-A06 | DOC_SYNC_REPORT | T1 | 3K | ~$0.005 |
| WP-A07 | INDEX refresh | T1 | 2K | ~$0.003 |
| **Tổng Phase A** | | **T1+T2** | **~34K** | **~$0.16** |

*(Lưu ý: con số trên là ước tính với Sonnet 4.6 pricing ~$3/1M input tokens)*

### 3.2 Phase B — Tech Debt Resolution

| WP | Task | Tier | Est. cost |
|----|------|------|-----------|
| WP-B01 | Add TRY-CATCH vào ~11 SPs | T2 | ~$0.10 |
| WP-B02 | Audit orphan records script | T2 | ~$0.05 |
| WP-B03 | Data cleanup analysis | T2-T3 | ~$0.20 |
| WP-B04 | FK Design review | T3 | ~$0.50 |
| WP-B05 | FK Implementation (rolling) | T3 + Human review | ~$1.00 |
| **Tổng Phase B** | | **T2+T3** | **~$1.85** |

### 3.3 Phase C — Monitoring

| WP | Task | Tier | Est. cost |
|----|------|------|-----------|
| WP-C01 | Dashboard view design | T2 | ~$0.10 |
| WP-C02 | Anomaly detection SP | T3 | ~$0.30 |
| WP-C03 | Run history table + logging | T2 | ~$0.10 |
| WP-C04 | SLA monitoring alert | T2 | ~$0.10 |
| **Tổng Phase C** | | **T2+T3** | **~$0.60** |

### 3.4 Ongoing Operations (Hàng năm)

| Activity | Frequency | Tier | Est. cost/year |
|----------|-----------|------|---------------|
| Monthly doc-sync | 12×/năm | T1 | ~$0.06 |
| Quarterly consistency review | 4×/năm | T2 | ~$0.12 |
| Per-incident triage | ~30×/năm | T2 | ~$0.45 |
| Per-incident post-review | ~10×/năm | T3 | ~$0.50 |
| Feature extension planning | ~5×/năm | T2 | ~$0.20 |
| **Tổng/năm** | | | **~$1.33/năm** |

---

## 4. Fallback Policy

| Primary | Fallback 1 | Fallback 2 | Quality impact |
|---------|-----------|-----------|----------------|
| Claude Opus 4.7 | GPT-5 o-series | Gemini 2.x Pro | ~10-15% |
| Claude Sonnet 4.6 | GPT-5 mini | Gemini 2.x Pro | ~5-10% |
| Claude Haiku 4.5 | GPT-5 nano | Gemini 2.x Flash | ~5% |

**Quy tắc fallback:** Khi dùng fallback, ghi note `[fallback: vendor X]` vào commit/document. Khi primary online lại, review các output critical (T3 tier).

---

## 5. Anti-patterns cần tránh

| Anti-pattern | Tác hại |
|-------------|---------|
| ❌ Dùng T3 cho tất cả task | Tốn cost 25× không cần thiết |
| ❌ Dùng T1 cho debug multi-SP phức tạp | Output thiếu nuance, bỏ sót edge case |
| ❌ AI tự chạy job lại production mà không có Human review | Nguy cơ tính trùng/sai doanh số |
| ❌ AI sửa SP production mà không có test plan | Có thể break logic offset |

---

## 6. Ghi chú & Caveats

- **Vietnamese language:** Claude và GPT-5 xử lý tiếng Việt tốt nhất — ưu tiên cho output tiếng Việt
- **Long context (Logic_nghiepvu_tinh_thucchay.md ~260KB):** Gemini 2.x Pro (1M context) có thể load toàn bộ trong 1 pass — phù hợp cho analysis toàn diện
- **Cost projection** là ước tính, phụ thuộc model pricing cập nhật hàng quý
