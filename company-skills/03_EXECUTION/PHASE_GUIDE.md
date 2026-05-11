# Phase 3 — Execution: Hướng dẫn vận hành

> **Đặc thù:** Phase 3 là **BIMODAL** — 1 phase setup (one-time) + 1 loop per Work Package (lặp).
>
> **Tham khảo:**
> - [phase-3-orchestrator/SKILL.md](phase-3-orchestrator/SKILL.md)
> - [phase-3-orchestrator/references/runbook.md](phase-3-orchestrator/references/runbook.md)

---

## 1. Mục tiêu Phase 3

**Build cái Phase 2 đã plan**, dùng AI tier routing để optimize cost.

**Output Phase 3:**
- `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md` (one-time)
- `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` (one-time)
- `docs/03_EXECUTION/work-packages/decomposed/<WP-ID>_tasks.md` (per WP)
- **Code thực sự** trong `src/` (sản phẩm cuối cùng)

---

## 2. Skills trong Phase 3

| # | Skill | Vai trò | Khi chạy |
|---|-------|---------|-----------|
| 1 | `ai-operator-protocol` | Quy tắc + workflow vận hành AI | One-time, đầu Phase 3 |
| 2 | `multi-tier-ai-routing` | Chính sách tier (T1/T2/T3/Human) | One-time, sau skill 1 |
| 3 | `work-package-decomposer` | Chia 1 WP thành micro-tasks | Lặp, mỗi WP |

**Orchestrator:** [`phase-3-execution-orchestrator`](phase-3-orchestrator/) — coordinate Sub-pipeline A (setup) + Sub-pipeline B (per WP loop).

---

## 3. Hai sub-pipeline

### 3.1 Sub-pipeline A — Setup (chạy 1 lần)

```
Pre-flight (Phase 2 done?)
    ↓
Step 1: ai-operator-protocol → AI_OPERATOR_GUIDE.md
    ↓
Step 2: multi-tier-ai-routing → AI_AGENT_TASK_DISTRIBUTION.md
    ↓
Phase 3 infrastructure ready
```

**Prompt mẫu:**
```
Chạy phase-3-execution-orchestrator Sub-pipeline A.
Project complexity: medium (~80K LOC target).
AI budget: $30K total Phase 3.
Mode A Supervised.
```

### 3.2 Sub-pipeline B — WP execution loop (lặp per WP)

```
Per WP-X.Y:
    ↓
Pre-flight (deps done?)
    ↓
Step 2: work-package-decomposer → tasks file
    ↓
Operator review tasks → approve
    ↓
AI executor: dispatch tasks per dependency order
    ↓
AI reviewer: verify (independent session)
    ↓
Operator: final review + commit
    ↓
Update PROGRESS.md
```

**Prompt mẫu (mỗi WP):**
```
Chạy phase-3-execution-orchestrator Sub-pipeline B cho WP-0.E.
Mode A Supervised.
Đợi tôi review trước khi dispatch tasks.
```

---

## 4. Hai cách vận hành

### 4.1 Cách A — Chạy từng skill riêng

Dùng khi:
- Update tier policy giữa chừng (chỉ multi-tier-ai-routing)
- Decompose 1 WP đặc biệt với guidance riêng (chỉ work-package-decomposer)
- Adjust operator protocol sau bài học từ WP đầu

### 4.2 Cách B — Chạy qua orchestrator (khuyến nghị)

Dùng khi:
- Setup Phase 3 lần đầu
- Mỗi WP của project (lặp đi lặp lại)
- Đảm bảo cấu trúc reviewer + verify

---

## 5. 4 Tier routing — chi tiết

| Tier | Model class | Use cases | % task target | Cost relative |
|------|-------------|-----------|----------------|---------------|
| **T1 Simple** | Haiku-class | Boilerplate, scaffolding, format | 60-70% | 1× |
| **T2 Mid** | Sonnet-class | Logic implementation, refactor | 20-30% | 5× |
| **T3 Strong** | Opus-class | Architecture, complex algorithm, security | 5-15% | 25× |
| **Human** | Người | ADR change, prod deploy, billing/auth/legal | <5% | (operator time) |

**Cost saving:** ~88% so với all-Tier-3.

**Cảnh báo:** Nếu T3 actual >30% → policy sai HOẶC dự án phức tạp hơn ước tính → re-calibrate.

---

## 6. WP execution flow chi tiết

```
1. Operator: "Run Phase 3 Sub-B for WP-X.Y"
2. Orchestrator pre-flight:
   - Deps done? (PROGRESS.md check)
   - WP spec valid?
   - Cost budget remaining?
3. work-package-decomposer:
   - Reads WP spec
   - Reads AI_OPERATOR_GUIDE + AI_AGENT_TASK_DISTRIBUTION
   - Output: 10-20 micro-tasks với tier assignment + verify command
4. Operator review tasks file:
   - Tier assignment đúng?
   - Verify commands đầy đủ?
   - Adjust nếu cần
   - Approve dispatch
5. Executor (per task, dependency order):
   - Read task prompt
   - Generate code change
   - Run verify command
   - If pass: mark done
   - If fail: retry per AI_OPERATOR_GUIDE rules; escalate if 2nd fail
6. Reviewer (separate session):
   - Re-run all verify commands
   - Check existing tests still pass
   - Flag anomalies
   - Recommend: APPROVE / FIX / ROLLBACK
7. Operator final review:
   - Diff inspection
   - Commit per convention
   - Update PROGRESS.md WP row
```

---

## 7. Quality gate per WP

Trước khi mark WP complete:
- [ ] All micro-tasks verified (verify commands pass)
- [ ] WP-level test suite passes
- [ ] No regressions (existing tests pass)
- [ ] Reviewer signed-off
- [ ] Operator commit per convention
- [ ] PROGRESS.md WP row updated

---

## 8. Quality gate Phase 3 overall

- [ ] Sub-A: AI_OPERATOR_GUIDE + AI_AGENT_TASK_DISTRIBUTION generated, tech lead approved
- [ ] Cost actual vs Sub-A projection trong ±20%
- [ ] Tier mix actual matches policy (T1 60-70% / T2 20-30% / T3 5-15% / Human <5%)
- [ ] All MASTER_PLAN WPs done với từng WP gate pass
- [ ] No WP stuck >2 tuần (re-decompose nếu có)
- [ ] PROGRESS.md show all WPs ✅

---

## 9. Cadence vận hành

| Cadence | Hoạt động |
|---------|-----------|
| **Đầu Phase 3** | Sub-A setup (1 ngày) |
| **Per WP** | Sub-B loop (1-2 tuần per WP, tùy size) |
| **Mỗi 5 WPs** | Audit cost actual vs projection; calibrate tier policy nếu cần |
| **Mỗi WP retrospective** | Update SKILL examples.md với patterns học được |
| **Sub-A refresh** | Khi phát hiện hard rule cần thêm/sửa |

---

## 10. Common pitfalls

### 10.1 Skip Sub-A vì "AI execute được rồi cần gì protocol"

**Hậu quả:** AI không có hard rules → vi phạm convention, commit không proper, gọi prod API trong dev.

**Tránh:** Sub-A bắt buộc. Mất 3 hr nhưng save weeks downstream.

### 10.2 Mode C Auto-WP từ Day 1

**Hậu quả:** Operator không build trust với system. Sai sót đầu tiên cũng auto-merge.

**Tránh:** Run 5+ WPs supervised trước khi enable Mode C. Ngay cả Mode C, operator vẫn review trước commit.

### 10.3 Decomposer output dispatch không review

**Hậu quả:** Tier sai → cost overrun. Verify command thiếu → task "done" không thực sự done.

**Tránh:** Operator review tasks file BẮT BUỘC trước dispatch. 5-10 min, save hours.

### 10.4 Reviewer = same session as executor

**Hậu quả:** Cùng AI vừa làm vừa review = tự chấm bài. Bias.

**Tránh:** Reviewer phải là session khác. Format prompt: "Review WP-X output. Bạn KHÔNG phải executor — đánh giá độc lập."

### 10.5 WP marked complete dù verify chưa pass

**Hậu quả:** Lỗi tích lũy. Phase 3 cuối phát hiện 50 things broken.

**Tránh:** Verify pass = mandatory. Nếu verify command fail, task chưa done, dù code "looks good".

### 10.6 Aggregate per-WP commits thành 1 PR lớn

**Hậu quả:** Không rollback được per-WP. Code review nightmare.

**Tránh:** Mỗi WP = 1 commit (hoặc 1 PR). Granularity matter.

### 10.7 Cost overrun tiếp tục chạy không re-calibrate

**Hậu quả:** Phase 3 tiêu nguyên budget khi chỉ làm 50% WPs.

**Tránh:** Audit cost mỗi 5 WPs. Nếu actual >120% projection: stop, calibrate, update Sub-A docs, resume.

---

## 11. Hand-off ra Phase 4

Khi tất cả WPs done:

1. **Pre-deploy gate G3** (out of scope orchestrator):
   - Operator + ops team approve go-live
   - Final integration test
   - Rollback plan ready
2. **Production deploy**
3. **Phase 4 starts:**
   - Run `phase-4-maintenance-orchestrator` Mode A Setup
   - Tạo runbooks cho mọi failure mode
   - Schedule monthly/quarterly maintenance

---

## 12. Time + cost (ước tính)

| Mode | Cost | Operator time | AI work | Elapsed |
|------|------|----------------|---------|---------|
| Sub-A (setup) | $0 (skills only) | 3 hr | 2.5 hr | 1 ngày |
| Sub-B all-supervised (18 WPs) | ~$25-40 | ~30 hr | ~50 hr | 6-8 tuần |
| Sub-B mixed (3 supervised + auto) | ~$25-35 | ~20 hr | ~40 hr | 4-6 tuần |

Cost variable nhất: reviewer flag rate + operator rework.

---

## 13. FAQ Phase 3

**Q: WP đầu tiên estimate sai (1 ngày → 3 ngày)?**
→ Học bài: estimation skill cải thiện sau 5-10 WPs. Update MASTER_PLAN nếu pattern systematic.

**Q: AI executor stuck infinitive loop trên 1 task?**
→ Per AI_OPERATOR_GUIDE: retry 1 lần, escalate human. Operator inspect, có thể re-decompose.

**Q: Reviewer flag false positive?**
→ Operator override + document reasoning trong commit. Pattern tracking: nếu reviewer luôn false-positive ở X, update reviewer prompt.

**Q: Có thể chạy 2 WPs parallel không?**
→ Có nếu independent (no dependency). Cẩn thận: 2 PRs cùng touch 1 file = merge conflict.

**Q: Cost tier ratio actual khác policy nhiều?**
→ Re-calibrate policy. AI_AGENT_TASK_DISTRIBUTION.md là living doc.

**Q: Vendor outage (Anthropic down)?**
→ Per fallback policy: switch alt vendor. Quality drop expected; flag commits affected. Re-review khi primary back nếu critical.

**Q: Hard rule mới phát sinh giữa Phase 3?**
→ Update AI_OPERATOR_GUIDE (Sub-A refresh). Audit prior commits có vi phạm rule mới không. Document.
