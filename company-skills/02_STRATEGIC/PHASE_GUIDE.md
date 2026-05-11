# Phase 2 — Strategic: Hướng dẫn vận hành

> **Đặc thù:** Phase này có **2 cổng phê duyệt CỨNG** — stakeholder approval (G1) + tech lead approval (G2). KHÔNG có Mode Express.
>
> **Tham khảo:**
> - [phase-2-orchestrator/SKILL.md](phase-2-orchestrator/SKILL.md)
> - [phase-2-orchestrator/references/runbook.md](phase-2-orchestrator/references/runbook.md)

---

## 1. Mục tiêu Phase 2

Convert Requirements (Phase 0) thành **kế hoạch thực thi đã được approve**:
- **Quyết định** (CÓ làm hay KHÔNG, làm phạm vi nào, ngân sách bao nhiêu)
- **Thiết kế** (kiến trúc nào, technology stack nào, ADR nào)
- **Kế hoạch** (phase, work package, dependency, timeline, owner)

**Output cuối Phase 2:**
- `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md`
- `docs/02_STRATEGIC/_decisions/G1_approval_<DATE>.md` (stakeholder approval artifact)
- `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` (with ADRs)
- `docs/02_STRATEGIC/_decisions/G2_approval_<DATE>.md` (tech lead approval artifact)
- `docs/02_STRATEGIC/MASTER_PLAN.md`
- `docs/03_EXECUTION/work-packages/PHASE_*.md`

---

## 2. Skills trong Phase 2

| # | Skill | Vai trò | Sau bước này |
|---|-------|---------|--------------|
| 1 | `feasibility-assessment` | 3 scenarios + ROI + recommendation | ✋ G1 — Stakeholder approval |
| 2 | `tech-solution-design` | Architecture + ADRs | ✋ G2 — Tech lead approval |
| 3 | `implementation-planning` | Master plan + WPs | (không gate — Phase 3 begins) |

**Orchestrator:** [`phase-2-strategic-orchestrator`](phase-2-orchestrator/) — coordinate với hard gates BẮT BUỘC.

---

## 3. Hai cách vận hành

### 3.1 Cách A — Chạy từng skill riêng

Dùng khi:
- Exploratory (chỉ feasibility, chưa cam kết vào Phase 2 đầy đủ)
- Re-design without scope change (chỉ tech-solution-design)
- Replanning approved work (chỉ implementation-planning)

**Prompt mẫu (chỉ feasibility):**
```
Chạy skill feasibility-assessment cho project Atrium.
Question: "Should we rewrite or refactor?"
Mode A 3-scenario.
Output: docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md.
KHÔNG tự chọn scenario — chỉ recommendation.
Sau khi xong, dừng lại để stakeholder review.
```

### 3.2 Cách B — Chạy cả cụm qua orchestrator (khuyến nghị)

Dùng khi:
- Phase 0 + Phase 1 (legacy) đã complete
- Project ready commit budget/timeline
- Stakeholder + tech lead available cho 2 cổng

**Prompt mẫu:**
```
Chạy phase-2-strategic-orchestrator cho project Pegasus.
Stakeholder approver: CEO (Anh A).
Tech lead approver: CTO (Chị B).
Pre-flight: verify Phase 0 + Phase 1 complete.
Sau Step 1 → pause + chờ G1.
Sau Step 2 → pause + chờ G2.
Sau Step 3 → final review.
```

---

## 4. CỔNG G1 — Stakeholder Approval (chi tiết)

### 4.1 Trước cổng

Step 1 (`feasibility-assessment`) sản xuất FEASIBILITY_ASSESSMENT.md với:
- 3 scenarios (Full / Partial / Minimum) + Do nothing baseline
- Mỗi scenario: cost, benefit, risk, timeline, ROI
- Operator's recommendation (KHÔNG phải decision)

### 4.2 Tại cổng

Operator phải:
1. **Schedule meeting** với stakeholder (CEO/CFO/board) — typically 30-60 min
2. **Present FEASIBILITY** — đi qua 4 scenarios; trả lời câu hỏi
3. **Document approval** với 1 trong các format:
   - Email với "Approve scenario [X]" rõ ràng
   - Meeting minutes ghi rõ approval
   - Decision note có chữ ký
4. **Save artifact** vào `docs/02_STRATEGIC/_decisions/G1_approval_<DATE>.md`

### 4.3 Format G1 approval artifact

```markdown
# G1 — Phase 2 Feasibility Approval

**Date:** YYYY-MM-DD
**Approver:** [NAME], [ROLE]
**Approval method:** [Email / Meeting / Signed note]

## Approved scenario
[FULL / PARTIAL / MINIMUM] — $X over T months

## Approval source
[paste email content / link to meeting minutes / scan signed doc]

## Conditions (if any)
- [list conditions]

## Reference
- FEASIBILITY_ASSESSMENT.md version: <git-hash>
```

### 4.4 Sau cổng

Orchestrator verify file tồn tại trước Step 2. Nếu thiếu → REFUSE start.

---

## 5. CỔNG G2 — Tech Lead Approval (chi tiết)

### 5.1 Trước cổng

Step 2 (`tech-solution-design`) sản xuất TECH_SOLUTION_DESIGN.md với:
- ≥3 candidates per major architectural decision
- Decision matrix
- N ADRs (Context / Decision / Alternatives Considered / Consequences)

### 5.2 Tại cổng

Tech Lead/CTO review từng ADR:
- **Approve all** → Step 3
- **Approve with modifications** → operator update ADRs, re-present (no full re-run unless major)
- **Reject** → re-run Step 2 với new constraints

### 5.3 Format G2 approval artifact

```markdown
# G2 — Phase 2 Architecture Approval

**Date:** YYYY-MM-DD
**Approver:** [NAME], [ROLE]

## ADRs reviewed
- ADR-001: [title] — APPROVED
- ADR-002: [title] — APPROVED with modification (see below)
- ADR-003: [title] — REJECTED, see notes
...

## Modifications required
- ADR-002: [description of modification]

## Reference
- TECH_SOLUTION_DESIGN.md version: <git-hash>
```

---

## 6. Tại sao Phase 2 KHÔNG có Mode Express

Phase 2 outputs cam kết:
- Ngân sách
- Timeline
- Architecture
- Implementation phases

Sai = lãng phí tháng. 1 tuần qua G1+G2 là cheap insurance. Không skip.

---

## 7. Quality gate cuối Phase 2

- [ ] G1 approval artifact tồn tại + reference rõ scenario
- [ ] G2 approval artifact tồn tại + reference rõ ADRs
- [ ] FEASIBILITY có Do nothing baseline
- [ ] TECH_SOLUTION_DESIGN ADRs đầy đủ 4 sections
- [ ] MASTER_PLAN timeline ≤ approved timeline
- [ ] MASTER_PLAN budget ≤ approved budget
- [ ] WP count reasonable (10-30 cho dự án trung bình)
- [ ] No WP >2 weeks effort (decompose thêm)
- [ ] Critical FRs (Must) all covered trong WPs

---

## 8. Cadence vận hành

| Cadence | Hoạt động |
|---------|-----------|
| **Lần đầu** | Run orchestrator full pipeline (typically 1-2 weeks elapsed) |
| **Mid-project pivot** | Re-run from Step 1 (re-feasibility với new constraints) |
| **Architecture review** | Re-run Step 2 only (chỉ tech-solution-design) |
| **Replanning sprint** | Re-run Step 3 only (chỉ implementation-planning) |
| **Hàng năm** | Phase 2 strategy review — approved scenario có còn đúng không? |

---

## 9. Common pitfalls

### 9.1 Auto-pipeline qua G1/G2

**Hậu quả:** Decision không có ownership. Stakeholder sau hối hận, blame operator.

**Tránh:** Orchestrator REFUSE start Step 2/3 nếu thiếu approval artifact. KHÔNG bypass.

### 9.2 Operator approve giùm stakeholder

**Hậu quả:** Operator không có authority quyết budget. Audit reject.

**Tránh:** Approval rights = stakeholder. Operator chỉ facilitate.

### 9.3 Stakeholder reject all scenarios → operator pick one closest

**Hậu quả:** Built thing stakeholder không muốn.

**Tránh:** Re-run Step 1 với new constraints (loop). KHÔNG skip.

### 9.4 ADR thiếu Alternatives Considered

**Hậu quả:** Decision không phải design — là mệnh lệnh. 6 tháng sau không ai nhớ tại sao.

**Tránh:** Mỗi ADR ≥3 alternatives + lý do reject từng cái.

### 9.5 MASTER_PLAN timeline > approved timeline

**Hậu quả:** Stakeholder phát hiện sau khi đã commit, project crash.

**Tránh:** Quality gate check timeline match. Nếu không fit, loop về G1.

### 9.6 WP quá lớn (>2 weeks)

**Hậu quả:** Decomposer ở Phase 3 sẽ struggle. AI executor mất context.

**Tránh:** Mỗi WP ≤ 2 weeks. Decompose thêm nếu lớn hơn.

### 9.7 Skip Do nothing baseline

**Hậu quả:** Stakeholder không thấy cost-of-inaction → undervalue project.

**Tránh:** Do nothing scenario BẮT BUỘC trong feasibility.

---

## 10. Hand-off ra Phase 3

| Output | Vai trò trong Phase 3 |
|--------|------------------------|
| MASTER_PLAN | Roadmap tổng thể, critical path |
| PHASE_*.md WPs | Input cho `work-package-decomposer` |
| TECH_SOLUTION_DESIGN | Architecture context cho AI executor |
| ADRs | Constraint khi AI implement (vd: vendor lock = AWS) |
| FEASIBILITY approved scenario | Budget ceiling cho Phase 3 cost |

---

## 11. Time + cost (ước tính)

| Pipeline | AI work | Human time | Elapsed | Cost |
|----------|---------|-------------|---------|------|
| First run, 1 iteration | 10-12 hr | 4 hr operator + 2 hr stakeholder + 2 hr tech lead | 1 tuần | ~$30-50 |
| Với G1 re-loop | 14-18 hr | 6 hr operator + 4 hr stakeholder | 2 tuần | ~$45-70 |
| Refresh (Phase 0 đổi) | 6-8 hr | 2-3 hr | 3-5 ngày | ~$20-35 |

Phase 2 là phase chậm nhất — đó là feature, không phải bug.

---

## 12. FAQ Phase 2

**Q: Stakeholder không có thời gian cho 60-min meeting cho G1?**
→ Cấp Section 1 Executive Summary của FEASIBILITY (1 trang). 10-min meeting tối thiểu. Nếu vẫn không có 10 phút → eskalate; project pending.

**Q: Tech lead không khoái ADR format, muốn free-form design doc?**
→ Có thể (Mode B Honor company template). Document quyết định format trong skill output. Nhưng "Alternatives Considered" + "Consequences" sections vẫn bắt buộc dù format gì.

**Q: Có thể có nhiều stakeholder approver (CEO + CFO + customer rep)?**
→ Có. Approval artifact phải bao gồm signature của tất cả. Mất time hơn nhưng safer.

**Q: WP count 50+ — quá nhiều không?**
→ Yes, over-decomposed. Thường 10-30 cho medium project. Gộp các WP nhỏ lại.

**Q: Stakeholder approve scenario A, sau đó đổi ý qua scenario B mà chưa go-live?**
→ Re-loop: re-run Step 1 với new framing → new G1 approval → cascade Step 2+3.

**Q: G1 approval rồi nhưng phát hiện feasibility numbers sai (budget mistake $50K)?**
→ Re-run Step 1 với corrected numbers → new approval (G1 phải re-approve nếu impact material).
