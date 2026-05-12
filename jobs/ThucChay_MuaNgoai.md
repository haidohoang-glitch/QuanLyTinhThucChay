# Job: ThucChay_MuaNgoai

## Thông Tin Cơ Bản
| Thuộc tính | Giá trị |
|---|---|
| Job Name | ThucChay_MuaNgoai |
| Database | ABM_Data_ThucChay |
| Hệ thống | Tính toán thực chạy |

## Các Bước (Steps)
| Step ID | Step Name | Command | Tác dụng |
|---|---|---|---|
| 1 | EXEC_ThucChay_TinhMuaNgoai | `EXEC dbo.ThucChay_TinhMuaNgoai_BySQLJobs` | Gọi SP |
| 2 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] ThucChay_MuaNgoai" -smtpBody "Job loi ThucChay_MuaNgoai"` | Chạy Script |

## Data Flow (Luồng Dữ Liệu)
```mermaid
graph TD
    Job_ThucChay_MuaNgoai[Job: ThucChay_MuaNgoai]
    Job_ThucChay_MuaNgoai --> SP_dbo_ThucChay_TinhMuaNgoai_BySQLJobs(SP: dbo.ThucChay_TinhMuaNgoai_BySQLJobs)
    SP_dbo_ThucChay_TinhMuaNgoai_BySQLJobs --> Ent_ThucChayDaTinh[(Table: ThucChayDaTinh)]
    SP_dbo_ThucChay_TinhMuaNgoai_BySQLJobs --> Ent_ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet[(Table: ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet)]
    SP_dbo_ThucChay_TinhMuaNgoai_BySQLJobs --> Ent_ThucChayDaTinh_MuaNgoai_SendThucChayDaTinhAdmarket[(Table: ThucChayDaTinh_MuaNgoai_SendThucChayDaTinhAdmarket)]
    SP_dbo_ThucChay_TinhMuaNgoai_BySQLJobs --> Ent_ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet[(Table: ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet)]
```
