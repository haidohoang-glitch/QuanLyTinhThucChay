# Phase 1 — Discovery: Hướng dẫn vận hành

> **Áp dụng:** CHỈ legacy projects (đã có code). Greenfield bỏ qua phase này.
>
> **Tham khảo:**
> - [phase-1-orchestrator/SKILL.md](phase-1-orchestrator/SKILL.md) — orchestrator skill
> - [phase-1-orchestrator/references/runbook.md](phase-1-orchestrator/references/runbook.md) — worked examples

---

## 1. Mục tiêu Phase 1

Hiểu rõ **codebase đang tồn tại** trước khi viết SRS reverse-engineer. Sản xuất 4 bản đồ:
- Bản đồ **kỹ thuật** (CODEBASE_MAP)
- Bản đồ **dữ liệu** (DATA_ARCHITECTURE)
- Bản đồ **nghiệp vụ** (BUSINESS_CONTEXT)
- Bản đồ **nợ kỹ thuật** (TECH_DEBT_AUDIT)

**Output cuối Phase 1:**
- `docs/01_DISCOVERY/CODEBASE_MAP.md`
- `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`
- `docs/01_DISCOVERY/BUSINESS_CONTEXT.md`
- `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md`

---

## 2. Skills trong Phase 1

| # | Skill | Vai trò | Bắt buộc? |
|---|-------|---------|-----------|
| 1 | `codebase-discovery` | Bản đồ kỹ thuật (entry, modules, deps) | Bắt buộc; chạy trước |
| 2 | `data-architecture-audit` | Bản đồ dữ liệu (schema, PII, governance) | Bắt buộc |
| 3 | `business-context-capture` | Bản đồ nghiệp vụ (actors, rules, workflows) | Bắt buộc |
| 4 | `tech-debt-audit` | Liệt kê nợ + rủi ro | Bắt buộc; chạy cuối |

**Orchestrator:** [`phase-1-discovery-orchestrator`](phase-1-orchestrator/) — coordinate tuần tự HOẶC parallel.

---

## 3. Hai cách vận hành

### 3.1 Cách A — Chạy từng skill riêng

Dùng khi:
- Chỉ refresh 1 doc (vd: chỉ data architecture sau khi thêm DB)
- Debug cụ thể 1 skill
- Selective audit

**Prompt mẫu:**
```
Chạy skill data-architecture-audit cho project Helix.
Inputs: codebase + DB migrations + cloud config + docs/01_DISCOVERY/CODEBASE_MAP.md.
Output: overwrite docs/01_DISCOVERY/DATA_ARCHITECTURE.md (archive prior).
Focus: PII, retention, encryption, governance.
```

### 3.2 Cách B — Chạy cả cụm qua orchestrator

Dùng khi:
- Onboarding legacy lần đầu (4 docs cần đầy đủ)
- Refresh tất cả sau major refactor
- Audit prep
- Trước khi chạy `srs-reverse-engineer`

**Prompt mẫu (Mode A Sequential):**
```
Chạy phase-1-discovery-orchestrator cho project Helix.
Mode A Supervised Sequential.
Codebase ở src/. CONTEXT_PACK ở docs/00_REQUIREMENTS/.
Pause sau mỗi step để tôi review.
```

**Prompt mẫu (Mode B Parallel — nhanh hơn):**
```
Chạy phase-1-discovery-orchestrator Mode B Parallel.
Step 1 (codebase-discovery) chạy trước.
Sau Step 1: Step 2+3 chạy parallel (2 AI sessions khác nhau).
Sau Step 2+3: Step 4 chạy.
Pause cuối Phase để tôi review tổng thể.
```

---

## 4. Thứ tự dependency (quan trọng)

```
Step 1: codebase-discovery
        ↓
        ├─→ Step 2: data-architecture-audit ─┐
        └─→ Step 3: business-context-capture ─┤
                                              ↓
                                           Step 4: tech-debt-audit
```

**Lý do thứ tự:**
- Step 1 trước: tất cả skills sau cần bản đồ kỹ thuật
- Step 2+3 có thể parallel: không phụ thuộc lẫn nhau
- Step 4 sau cùng: tech debt cần view holistic từ 1+2+3

---

## 5. Quality gate cuối Phase 1

- [ ] CODEBASE_MAP có coverage statement honest (% read trực tiếp vs sample)
- [ ] DATA_ARCHITECTURE PII section explicit (không "có PII đâu đó")
- [ ] BUSINESS_CONTEXT Section 7 invariants non-empty
- [ ] BUSINESS_CONTEXT Section 9 Open Questions có code-vs-stakeholder mismatches (nếu có CONTEXT_PACK)
- [ ] TECH_DEBT severity calibrated (Critical ≤ 10 cho dự án trung bình)
- [ ] Phase report generated

---

## 6. Cadence vận hành

| Cadence | Hoạt động |
|---------|-----------|
| **Onboarding** | Run orchestrator full Phase 1 |
| **Sau major refactor** | Re-run affected skills (Mode D Selective) |
| **Hàng quý** | Spot-check via `documentation-sync` — detect Phase 1 drift |
| **Hàng năm** | Full Phase 1 refresh (re-run orchestrator) |
| **Trước rewrite** | Phase 1 mới nhất là baseline cho "as-is" SRS |

---

## 7. Common pitfalls

### 7.1 Bỏ qua Phase 1 vì "vào SRS luôn cho nhanh"

**Hậu quả:** `srs-reverse-engineer` sẽ ABORT vì thiếu BUSINESS_CONTEXT. Phải quay lại Phase 1.

**Tránh:** Đi đúng thứ tự. Phase 1 trước, Phase 0 sau (cho legacy).

### 7.2 CODEBASE_MAP coverage thấp (< 50%)

**Hậu quả:** Downstream skills inherit blind spots. BUSINESS_CONTEXT thiếu use cases. TECH_DEBT bỏ sót critical findings.

**Tránh:** Target ≥70% coverage. Nếu không đạt, log honest + flag là gap.

### 7.3 Tech debt all-Critical

**Hậu quả:** Operator panic, stakeholder hoảng, không biết bắt đầu từ đâu.

**Tránh:** Force calibration: max 10 Critical. Critical = causes outage OR blocks revenue OR fails audit. Phần còn lại High/Medium/Low.

### 7.4 BUSINESS_CONTEXT mô tả code thay vì business

**Hậu quả:** Output bị overlap với CODEBASE_MAP, không add value.

**Tránh:** Domain language only — "user can transfer funds" KHÔNG phải "POST /api/transfers calls TransferService".

### 7.5 Skip BUSINESS_CONTEXT invariants

**Hậu quả:** Mất phần quý nhất của doc. Sau này phát hiện bug "không nhất quán" mà không có invariant để check.

**Tránh:** Cố tìm invariants. DB constraints, comments "phải luôn đúng", trigger functions enforce rules — đó là invariants.

---

## 8. Hand-off ra Phase 0/2

### Phase 1 → Phase 0 (legacy SRS)

| Output | Vai trò trong Phase 0 |
|--------|------------------------|
| CODEBASE_MAP | M2.1 (product perspective), M2.4 (operating environment) |
| DATA_ARCHITECTURE | M2.5 (constraints), seeds M9 NFR security/privacy |
| BUSINESS_CONTEXT | M2-M8 phần lớn lấy từ đây |
| TECH_DEBT | M2.7 (assumptions), M10 (open issues) |

### Phase 1 → Phase 2 (feasibility)

| Output | Vai trò |
|--------|---------|
| TECH_DEBT | Cost-of-inaction baseline (Do nothing scenario) |
| DATA_ARCHITECTURE | Migration cost projection |
| CODEBASE_MAP | Effort estimation context |
| BUSINESS_CONTEXT | Value at risk if system fails |

---

## 9. Time + cost (ước tính)

Cho legacy ~80K LOC, 4 functional domains:

| Mode | AI work | Operator | Elapsed | Cost |
|------|---------|----------|---------|------|
| A Sequential | 9-10 hr | 2-3 hr | 2-3 ngày | ~$25-40 |
| B Parallel | 7-8 hr | 2-3 hr | 1-2 ngày | ~$22-35 |
| C Express | 5-7 hr | 1 hr | 1 ngày | ~$18-28 |
| D Selective (1 skill) | 1-3 hr | 30 min | <1 ngày | ~$5-10 |

---

## 10. FAQ Phase 1

**Q: Codebase có 5 microservices, có cần chạy Phase 1 cho từng cái?**
→ Có, mỗi microservice nên có CODEBASE_MAP riêng (ở subfolder), và 1 BUSINESS_CONTEXT chung tổng hợp. Hoặc 1 docs/ chung với section per service. Tùy size.

**Q: DB không truy cập được production, làm sao audit?**
→ Dùng migration files + ORM models làm proxy. Mark "Schema based on migrations; runtime data not verified" trong DATA_ARCHITECTURE. Schedule follow-up.

**Q: BUSINESS_CONTEXT có nên bao gồm tính năng đã deprecated trong code?**
→ Có, nhưng đánh dấu "(deprecated, used by N% users per analytics)". Đó là context, không phải spec.

**Q: TECH_DEBT_AUDIT có nên estimate cost-to-fix bằng tiền?**
→ Yes, nhưng range thay vì single number ($50-80K thay vì $65K). Honest về uncertainty.

**Q: Mode B Parallel có an toàn không?**
→ Có nếu Step 2+3 chạy trên 2 AI sessions độc lập. Cảnh báo: review parallel outputs cùng lúc khó hơn — dành thêm time cho operator review nếu chọn Mode B.
