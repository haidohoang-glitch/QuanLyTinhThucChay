# Job: ThucChay_CPD_Chiphi_PR

## Thông Tin Cơ Bản
| Thuộc tính | Giá trị |
|---|---|
| Job Name | ThucChay_CPD_Chiphi_PR |
| Database | ABM_Data_ThucChay |
| Hệ thống | Tính toán thực chạy |

## Các Bước (Steps)
| Step ID | Step Name | Command | Tác dụng |
|---|---|---|---|
| 1 | Job_TinhThucChay_CPD | `EXEC [dbo].[ThucChay_CPD_Job]` | Gọi SP |
| 2 | Job_TinhThucChay_ChiPhiKhac | `--EXEC dbo.ThucChay_TinhChiPhiKhac_ByJobs --Truoc toi uu --job sau toi uu 06/02/2025 EXEC [dbo].[ThucChay_ChiPhi_Job]` | Gọi SP |
| 3 | Job_TinhThucChay_PR | `--job tinh thuc chay pr theo phuong phap cu --EXEC dbo. ThucChay_TinhPR_BySQLJobs  -- job PR duoc toi u theo phuong phap moi 20/03/2025 EXEC [dbo].[ThucChay_PR_Job]` | Gọi SP |
| 4 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] ThucChay_CPD_Chiphi_PR_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory" -smtpBody "Job loi ThucChay_CPD_Chiphi_PR_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory"` | Chạy Script |

## Data Flow (Luồng Dữ Liệu)
```mermaid
graph TD
    Job_ThucChay_CPD_Chiphi_PR[Job: ThucChay_CPD_Chiphi_PR]
    Job_ThucChay_CPD_Chiphi_PR --> SP_dbo_ThucChay_CPD_Job(SP: dbo.ThucChay_CPD_Job)
    SP_dbo_ThucChay_CPD_Job --> Ent_ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh[(Table: ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh)]
    SP_dbo_ThucChay_CPD_Job --> Ent_ThucChay_CPDdonvigoi_PhatSinhThucChay_ThucChayDaTinh[(Table: ThucChay_CPDdonvigoi_PhatSinhThucChay_ThucChayDaTinh)]
    SP_dbo_ThucChay_CPD_Job --> Ent_ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh[(Table: ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh)]
    SP_dbo_ThucChay_CPD_Job --> Ent_ThucChay_CPDdotchay_PhatSinhThucChay_ThucChayDaTinh[(Table: ThucChay_CPDdotchay_PhatSinhThucChay_ThucChayDaTinh)]
    SP_dbo_ThucChay_CPD_Job --> Ent_ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh[(Table: ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh)]
    SP_dbo_ThucChay_CPD_Job --> Ent_ThucChay_CPDkhongdotchay_PhatSinhThucChay_ThucChayDaTinh[(Table: ThucChay_CPDkhongdotchay_PhatSinhThucChay_ThucChayDaTinh)]
    Job_ThucChay_CPD_Chiphi_PR --> SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs(SP: dbo.ThucChay_TinhChiPhiKhac_ByJobs)
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_CauHinhNhomTinhDoanhSoThucChay[(Table: CauHinhNhomTinhDoanhSoThucChay)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_prc_asd_CheckGTTDChiPhi_With_HopDong_ThangDuGP[(Table: prc_asd_CheckGTTDChiPhi_With_HopDong_ThangDuGP)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_sp_TC_InsertThucChayDaTinh_ChiPhi_SanPhamChinh[(Table: sp_TC_InsertThucChayDaTinh_ChiPhi_SanPhamChinh)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_sp_TC_InsertThucChayDaTinh_ChiPhiKhac[(Table: sp_TC_InsertThucChayDaTinh_ChiPhiKhac)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_sp_TC_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh[(Table: sp_TC_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_sp_TC_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh[(Table: sp_TC_UpdateGiaTriThayDoi_ThucChay_GiaiPhapCongNghe_SanPhamChinh)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhiKhac)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_sp_ThucChay_ExcInsertThucChayDaTinh_CreatorContent[(Table: sp_ThucChay_ExcInsertThucChayDaTinh_CreatorContent)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_ThucChayDaTinh[(Table: ThucChayDaTinh)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_ThucChayDaTinh_CheckKetQuaVanHanhThayDoi_CreatorContent[(Table: ThucChayDaTinh_CheckKetQuaVanHanhThayDoi_CreatorContent)]
    SP_dbo_ThucChay_TinhChiPhiKhac_ByJobs --> Ent_ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_CreatorContent[(Table: ThucChayDaTinh_CheckVaUpdateGiaTriThayDoi_CreatorContent)]
    Job_ThucChay_CPD_Chiphi_PR --> SP_dbo_dbo(SP: dbo.dbo)
```
