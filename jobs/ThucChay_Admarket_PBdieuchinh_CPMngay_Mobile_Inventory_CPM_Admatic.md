# Job: ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic

## Thông Tin Cơ Bản
| Thuộc tính | Giá trị |
|---|---|
| Job Name | ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic |
| Database | ABM_Data_ThucChay |
| Hệ thống | Tính toán thực chạy |

## Các Bước (Steps)
| Step ID | Step Name | Command | Tác dụng |
|---|---|---|---|
| 1 | Job_TinhThucChay_Admarket | `--Điều chuyển job tính thưc chay từ ngày 11/03/2025 EXEC dbo.job_prc_asd_calc_admarket_PhanBo` | Gọi SP |
| 2 | Job_PerformanceBase_DieuChinhGiaTri | `--Điều chuyển job tinh cho admarket dieu chinh 11/03/2025 EXEC dbo.prc_asd_calc_admarket_UpdateValue_With_HopDong` | Gọi SP |
| 3 | job_TinhThucChay_CPM_With_DonViTinh_Ngay | `--Dieu chuyen job CPM don vi ngày 11/03/2025 EXEC dbo.ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs` | Gọi SP |
| 4 | Job_TinhThucChaySanPham_Mobile | `--SP chạy chạy cho job tinh mobile theo phuong phap cu --EXEC dbo.ThucChay_TinhMobile_BySQLJobs  -- SP tinh mobile theo phuong phap moi 11/02/2025 --dieu chuyen 11/03/2025 EXEC  [dbo].[ThucChay_Mobile_Job]` | Gọi SP |
| 5 | job_TinhThucChay_Inventory | `--Dieu chuyen job 11/03/2025 EXEC dbo.ThucChay_job_TinhthucchayInventory` | Gọi SP |
| 6 | ThucChay_CPM | `--Job tinh CPM chua toi uu --EXEC [dbo].[ThucChay_TinhCPM_BySQLJobs]  --job tinh CPM da toi uu 07/03/2025 EXEC  [dbo].[ThucChay_CPM_Job]` | Gọi SP |
| 7 | TinhThucChay_Admatic | `-- Job chay theo phuong phap cu chua toi uu --EXEC [dbo].[Job_ThucChay_Admatic_NhieuSanPham]  --Job thuc chay da toi uu 10/03/2025 EXEC  [dbo].[ThucChay_Admatic_Job]` | Gọi SP |
| 8 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] ThucChay_Admatic_CPM" -smtpBody "Job loi ThucChay_Admatic_CPM"` | Chạy Script |

## Data Flow (Luồng Dữ Liệu)
```mermaid
graph TD
    Job_ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic[Job: ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic]
    Job_ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic --> SP_dbo_job_prc_asd_calc_admarket_PhanBo(SP: dbo.job_prc_asd_calc_admarket_PhanBo)
    SP_dbo_job_prc_asd_calc_admarket_PhanBo --> Ent_prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_PhanBo[(Table: prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_PhanBo)]
    SP_dbo_job_prc_asd_calc_admarket_PhanBo --> Ent_prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong_PhanBo[(Table: prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong_PhanBo)]
    SP_dbo_job_prc_asd_calc_admarket_PhanBo --> Ent_prc_asd_tinhthucchay_sanphamadmarket_PhanBo[(Table: prc_asd_tinhthucchay_sanphamadmarket_PhanBo)]
    SP_dbo_job_prc_asd_calc_admarket_PhanBo --> Ent_prc_insert_thucchaydatinh_admarket_PhanBo[(Table: prc_insert_thucchaydatinh_admarket_PhanBo)]
    SP_dbo_job_prc_asd_calc_admarket_PhanBo --> Ent_ThucChayDaTinhAdmarket_InsertThucChayNoContract_PhanBo[(Table: ThucChayDaTinhAdmarket_InsertThucChayNoContract_PhanBo)]
    Job_ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic --> SP_dbo_prc_asd_calc_admarket_UpdateValue_With_HopDong(SP: dbo.prc_asd_calc_admarket_UpdateValue_With_HopDong)
    SP_dbo_prc_asd_calc_admarket_UpdateValue_With_HopDong --> Ent_ADX_Job_UpdateStatusThayDoiThucChay[(Table: ADX_Job_UpdateStatusThayDoiThucChay)]
    SP_dbo_prc_asd_calc_admarket_UpdateValue_With_HopDong --> Ent_prc_asd_DeletedThucChay_Admarket_With_HopDong_MKT_FEE[(Table: prc_asd_DeletedThucChay_Admarket_With_HopDong_MKT_FEE)]
    SP_dbo_prc_asd_calc_admarket_UpdateValue_With_HopDong --> Ent_prc_asd_TinhThucChay_Admarket_With_HopDong_NgayDauThang_ThangDuGP[(Table: prc_asd_TinhThucChay_Admarket_With_HopDong_NgayDauThang_ThangDuGP)]
    SP_dbo_prc_asd_calc_admarket_UpdateValue_With_HopDong --> Ent_prc_asd_TinhThucChay_Admarket_With_HopDong_ThangDuGP[(Table: prc_asd_TinhThucChay_Admarket_With_HopDong_ThangDuGP)]
    SP_dbo_prc_asd_calc_admarket_UpdateValue_With_HopDong --> Ent_prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong[(Table: prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong)]
    Job_ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic --> SP_dbo_ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs(SP: dbo.ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs)
    SP_dbo_ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_With_DonViTinh_Ngay[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_With_DonViTinh_Ngay)]
    SP_dbo_ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site[(Table: ThucChay_ExcInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site)]
    SP_dbo_ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs --> Ent_ThucChay_HopDongChiTietAndBanner[(Table: ThucChay_HopDongChiTietAndBanner)]
    SP_dbo_ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs --> Ent_ThucChay_UpdateHopDongChiTietAndBannerCPM_With_DonViTinh_Ngay[(Table: ThucChay_UpdateHopDongChiTietAndBannerCPM_With_DonViTinh_Ngay)]
    Job_ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic --> SP_dbo_ThucChay_TinhMobile_BySQLJobs(SP: dbo.ThucChay_TinhMobile_BySQLJobs)
    SP_dbo_ThucChay_TinhMobile_BySQLJobs --> Ent_HopDongChiTiet[(Table: HopDongChiTiet)]
    SP_dbo_ThucChay_TinhMobile_BySQLJobs --> Ent_sp_TC_ExcInsertThucChayDaTinh_Mobile[(Table: sp_TC_ExcInsertThucChayDaTinh_Mobile)]
    SP_dbo_ThucChay_TinhMobile_BySQLJobs --> Ent_ThucChayDaTinh[(Table: ThucChayDaTinh)]
    Job_ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic --> SP_dbo_ThucChay_job_TinhthucchayInventory(SP: dbo.ThucChay_job_TinhthucchayInventory)
    SP_dbo_ThucChay_job_TinhthucchayInventory --> Ent_ThucChay_ExecThucChayDaTinh_HopDongInventory[(Table: ThucChay_ExecThucChayDaTinh_HopDongInventory)]
    SP_dbo_ThucChay_job_TinhthucchayInventory --> Ent_ThucChay_ExecThucChayDaTinh_HopDongInventory_AdmaticProgrammatic[(Table: ThucChay_ExecThucChayDaTinh_HopDongInventory_AdmaticProgrammatic)]
    SP_dbo_ThucChay_job_TinhthucchayInventory --> Ent_ThucChay_Update_GTTD_ThucChayDaTinh_HopDongInventory[(Table: ThucChay_Update_GTTD_ThucChayDaTinh_HopDongInventory)]
    Job_ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic --> SP_dbo_ThucChay_TinhCPM_BySQLJobs(SP: dbo.ThucChay_TinhCPM_BySQLJobs)
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_CauHinhNhomTinhDoanhSoThucChay[(Table: CauHinhNhomTinhDoanhSoThucChay)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_HopDongChiTiet[(Table: HopDongChiTiet)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai_ThucTreo[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai_ThucTreo)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi_v2[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi_v2)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_Native_Ads[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_Native_Ads)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_TRUEVIEW[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_TRUEVIEW)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinh[(Table: ThucChay_ExcInsertThucChayDaTinh)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinh_CPM_Native_Ads[(Table: ThucChay_ExcInsertThucChayDaTinh_CPM_Native_Ads)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinh_CPR[(Table: ThucChay_ExcInsertThucChayDaTinh_CPR)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR[(Table: ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinh_DonViBai[(Table: ThucChay_ExcInsertThucChayDaTinh_DonViBai)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinh_DonViBai_ThucTreo[(Table: ThucChay_ExcInsertThucChayDaTinh_DonViBai_ThucTreo)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinh_DonViGoi_V2[(Table: ThucChay_ExcInsertThucChayDaTinh_DonViGoi_V2)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinhCPV[(Table: ThucChay_ExcInsertThucChayDaTinhCPV)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_ExcInsertThucChayDaTinhTrueView[(Table: ThucChay_ExcInsertThucChayDaTinhTrueView)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_HopDongChiTietAndBanner[(Table: ThucChay_HopDongChiTietAndBanner)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChay_UpdateHopDongChiTietAndBanner[(Table: ThucChay_UpdateHopDongChiTietAndBanner)]
    SP_dbo_ThucChay_TinhCPM_BySQLJobs --> Ent_ThucChayDaTinh[(Table: ThucChayDaTinh)]
    Job_ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic --> SP_dbo_Job_ThucChay_Admatic_NhieuSanPham(SP: dbo.Job_ThucChay_Admatic_NhieuSanPham)
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_HopDongChiTiet[(Table: HopDongChiTiet)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_sp_TC_UpdateGiaTriThayDoi_ThucTreoThayDoi_ThanhTien_Admatic[(Table: sp_TC_UpdateGiaTriThayDoi_ThucTreoThayDoi_ThanhTien_Admatic)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai_Admatic_ThucTreo[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai_Admatic_ThucTreo)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ThanhTien_Admatic[(Table: sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ThanhTien_Admatic)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham[(Table: ThucChay_Check_NhanHangThayDoi_Admatic_NhieuSanPham)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_ThucChay_ExcInsertThucChayDaTinh_DonViBai_Admatic_ThucTreo[(Table: ThucChay_ExcInsertThucChayDaTinh_DonViBai_Admatic_ThucTreo)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_ThucChay_ExcInsertThucChayDaTinh_ThanhTien_Admatic[(Table: ThucChay_ExcInsertThucChayDaTinh_ThanhTien_Admatic)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic[(Table: ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_ThucChay_InsertThucChayDaTinhAdmarket_Adx_ThanhTien_Admatic[(Table: ThucChay_InsertThucChayDaTinhAdmarket_Adx_ThanhTien_Admatic)]
    SP_dbo_Job_ThucChay_Admatic_NhieuSanPham --> Ent_ThucChayDaTinh[(Table: ThucChayDaTinh)]
```
