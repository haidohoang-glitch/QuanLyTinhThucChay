# Incident Response Playbook — Hệ thống Tính Thực Chạy

> **Skill:** `incident-response-playbook` | **Trạng thái:** 🔴 Cần user cung cấp thông tin
>
> Playbook xử lý sự cố cho hệ thống production.

---

## Danh sách Runbooks

<!-- ⚠️ Mỗi incident type sẽ có 1 file INCIDENT_*.md riêng -->

| File | Sự cố | Trạng thái |
|------|-------|------------|
| INCIDENT_JOB_FAILURE.md | Job chạy fail | 🔴 Cần user input |
| INCIDENT_WRONG_REVENUE.md | Doanh số tính sai | 🔴 Cần user input |
| INCIDENT_DATA_SYNC_FAIL.md | Đồng bộ dữ liệu thất bại | 🔴 Cần user input |

---

## Template Runbook

```markdown
# INCIDENT: [Tên sự cố]

## Triệu chứng
- _(mô tả)_

## Nguyên nhân thường gặp
1. _(nguyên nhân 1)_
2. _(nguyên nhân 2)_

## Quy trình xử lý
### Bước 1: Xác nhận
### Bước 2: Triage
### Bước 3: Fix
### Bước 4: Verify

## Escalation
- _(khi nào escalate)_
```
