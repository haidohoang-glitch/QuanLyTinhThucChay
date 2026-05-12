# Job: job_TinhLaiThucChay

## Thông Tin Cơ Bản
| Thuộc tính | Giá trị |
|---|---|
| Job Name | job_TinhLaiThucChay |
| Database | ABM_Data_ThucChay |
| Hệ thống | Tính toán thực chạy |

## Các Bước (Steps)
| Step ID | Step Name | Command | Tác dụng |
|---|---|---|---|
| 1 | exec sql | `exec job_ThucChayDaTinh_ReInsertByHopDong` | Gọi SP |
| 2 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] job_TinhLaiThucChay" -smtpBody "Job loi job_TinhLaiThucChay"` | Chạy Script |

## Data Flow (Luồng Dữ Liệu)
```mermaid
graph TD
    Job_job_TinhLaiThucChay[Job: job_TinhLaiThucChay]
    Job_job_TinhLaiThucChay --> SP_dbo_job_ThucChayDaTinh_ReInsertByHopDong(SP: dbo.job_ThucChayDaTinh_ReInsertByHopDong)
    SP_dbo_job_ThucChayDaTinh_ReInsertByHopDong --> Ent_sp_TC_UpdateGiaTriThayDoi_HDHuy[(Table: sp_TC_UpdateGiaTriThayDoi_HDHuy)]
    SP_dbo_job_ThucChayDaTinh_ReInsertByHopDong --> Ent_sp_ThucChayDaTinh_ReInsertByHopDong[(Table: sp_ThucChayDaTinh_ReInsertByHopDong)]
    SP_dbo_job_ThucChayDaTinh_ReInsertByHopDong --> Ent_sp_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi[(Table: sp_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi)]
```
