# 01 — Danh sách Jobs & Steps

> Tổng số Jobs liên quan: **13**

---
## Job: `Job_GetInfo_ThucChay_GGFB`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: Job lay thong tin thuc chay cua GGFB

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | Job_InsertOrUpdate_Operating_Order_GGFB | `EXEC Gen_InsertOrUpdate_Operating_Order_GGFB` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 2 | Job_InsertOrUpdate_Operating_Result_GGFB | `EXEC Gen_InsertOrUpdate_Operating_Result_GGFB` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 3 | Job_InsertOrUpdate_Operating_Result_Map_Order_GGFB | `EXEC Gen_InsertOrUpdate_Operating_Result_Map_Order_GGFB` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 4 | Job_InsertOrUpdate_Operating_Result_Quantity_GGFB | `EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_Quantity_GGFB]` | ABM_Data_ThucChay | Quit (Success) | Quit (Failure) |

---
## Job: `Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: Job get thong tin thuc treo tu ban hdcn ve tinh thuc chay

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | job_GetInforThucTreoBranding_From_ThucTreo_SQLServer | `--EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_New]  EXEC [Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreo]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 2 | job_getInfor_ThucTreoTrinhDuyet_ThucTreoChiPhi_From_ThucTreo | `EXEC [dbo].[Gen_InsertOrUpdate_ThucTreoHopDongChiTietTrinhDuyet_ThucTreo_fromSQLServer]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 3 | Job_get_Infor_hdcn_thucchay_muangoai | `EXEC [dbo].[Gen_InsertOrUpdate_HopDongChiTiet_MuaNgoai_New_v1]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 4 | job_Update_ChietKhau_IsKhuyenMai_HopDongChiTiet | `EXEC [dbo].[ThucChay_Update_ChietKhau_IsKhuyenMai_HopDongChiTiet]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 5 | Bojob_job_get_ThuctreoPR_from_ThucTreo_SQLServer | `--EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_ThucTreo]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 6 | Job_Get_ThucTreo_ChiPhi_SQLServer | `---EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreoChiPhi]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 7 | job_InsertOfUpdate_Operating_Order_GGFB | `--haidh comment vi co job rieng chay luc 1h sang --EXEC Gen_InsertOrUpdate_Operating_Order_GGFB` | ABM_Data_ThucChay | Go to next step | Go to step |
| 8 | job_InsertOrUpdate_Operating_Result_GGFB | `--haidh comment vi co job rieng chay luc 1h sang --EXEC Gen_InsertOrUpdate_Operating_Result_GGFB` | ABM_Data_ThucChay | Go to next step | Go to step |
| 9 | Job_InsertOrUpdate_Operating_Result_Map_Order_GGFB | `--haidh comment vi co job rieng chay luc 1h sang --EXEC Gen_InsertOrUpdate_Operating_Result_Map_Order_GGFB` | ABM_Data_ThucChay | Go to next step | Go to step |
| 10 | Job_InsertOrUpdate_Operating_Result_Quantity_GGFB | `--haidh comment vi co job rieng chay luc 1h sang --EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_Quantity_GGFB]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 11 | job_PMS_QuanLyThucChay_Account | `EXEC [dbo].[Gen_InsertOrUpdate_PMS_QuanLyThucChay_Account]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 12 | job get thuc treo chi phi log | `EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreoChiPhi_Log]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 13 | job_Get_AppKetQuaVanHanh_CreatorContent | `EXEC [Gen_InsertOrUpdate_AppKetQuaVanHanh_CreatorContent]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 14 | job_Get_AppKetQuaVanHanhHistory_CreatorContent | `EXEC [dbo].[Gen_InsertOrUpdate_AppKetQuaVanHanhHistory_CreatorContent]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 15 | job get ThucChayHopDongChiTiet_ThucTreo_Log | `EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreo_Log]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 16 | Job_Insert_Update_HopDongChiTietAndBanner_CPM | `--exec [dbo].[Job_Insert_Update_HopDongChiTietAndBanner_CPM] --THEM HAM CHAY CHO ADMATIC exec [dbo].[Job_Insert_Update_HopDongChiTietAndBanner_CPM_Admatic]` | ABM_Data_ThucChay | Quit (Success) | Go to step |
| 17 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -smtpSubject "[Canh bao job loi] Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN" -smtpBody "Job loi Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN"` | msdb | Quit (Success) | Quit (Failure) |

---
## Job: `Job_InsertAndUpdate_ThucChayHopDongChiTietAndBanner_Admatic`
- **Trạng thái**: ❌ Đã tắt
- **Mô tả**: Thuc hien tinh du lieu cho table ThucChayHopDongChiTietAndBanner_Admatic

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | Job_InsertAndUpdateThucChayHopDongChiTiet_Admatic | `EXEC [Job_InsertAndUpdate_HopDongChiTietAndBanner_Admatic]` | ABM_Data_ThucChay | Quit (Success) | Go to step |
| 2 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -smtpSubject "[Canh bao job loi] Job_InsertAndUpdate_ThucChayHopDongChiTietAndBanner_Admatic" -smtpBody "Job loi Job_InsertAndUpdate_ThucChayHopDongChiTietAndBanner_Admatic"` | msdb | Quit (Success) | Quit (Failure) |

---
## Job: `Job_KiemTraTrangThai_JobTinhThucChay`
- **Trạng thái**: ❌ Đã tắt
- **Mô tả**: No description available.

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | Job_KiemTraTrangThai_JobTinhThucChay | `EXEC dbo.prc_ProcessCheckingJobTinhThucChay_ThucChayAg` | AbpZeroDb_QuanLyThucChay | Quit (Success) | Quit (Failure) |

---
## Job: `Job_XuLy_ThucChay_TamTinh`
- **Trạng thái**: ❌ Đã tắt
- **Mô tả**: Job xy ly du lieu thuc chay tam tinh de show len domain fake

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | job_xuly_fake_DongBoDuLieu_ABM_Data_Relase | `exec DongBoDuLieu_Fake_All` | ABM_Data_ThucChay | Go to next step | Quit (Success) |
| 2 | job_xuly_fake_TinhThucChayDaTinhBySanPham | `EXEC TinhThucChayDaTinhBySanPham` | ABM_Data_Release | Go to next step | Quit (Failure) |
| 3 | job_xuly_fake_XuLyDuLieuThucChay_ReportingDB | `exec Rpt_XuLyDuLieuThucChay_ReportingDB` | Reporting_Data | Quit (Success) | Quit (Success) |

---
## Job: `KiemSoat_ThucChayDaTinh`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: Job thuc hien kiem tra thông tin du lieu thuc chay sau khi tinh

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | KiemSoat_ThucChayDaTinh_website_nhieuhon1ID | `EXEC dbo.KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID` | ABM_Data_ThucChay | Go to next step | Quit (Failure) |
| 2 | KiemSoat_DataThucChay_ThayDoi_Mobile | `EXEC [dbo].[KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay]  @TypeProduct = 1010` | ABM_Data_ThucChay | Quit (Success) | Quit (Failure) |

---
## Job: `ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: Tinh thuc chay admatic

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | Job_TinhThucChay_Admarket | `--Điều chuyển job tính thưc chay từ ngày 11/03/2025 EXEC dbo.job_prc_asd_calc_admarket_PhanBo` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 2 | Job_PerformanceBase_DieuChinhGiaTri | `--Điều chuyển job tinh cho admarket dieu chinh 11/03/2025 EXEC dbo.prc_asd_calc_admarket_UpdateValue_With_HopDong` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 3 | job_TinhThucChay_CPM_With_DonViTinh_Ngay | `--Dieu chuyen job CPM don vi ngày 11/03/2025 EXEC dbo.ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 4 | Job_TinhThucChaySanPham_Mobile | `--SP chạy chạy cho job tinh mobile theo phuong phap cu --EXEC dbo.ThucChay_TinhMobile_BySQLJobs  -- SP tinh mobile theo phuong phap moi 11/02/2025 --dieu chuyen 11/03/2025 EXEC  [dbo].[ThucChay_Mobile_Job]` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 5 | job_TinhThucChay_Inventory | `--Dieu chuyen job 11/03/2025 EXEC dbo.ThucChay_job_TinhthucchayInventory` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 6 | ThucChay_CPM | `--Job tinh CPM chua toi uu --EXEC [dbo].[ThucChay_TinhCPM_BySQLJobs]  --job tinh CPM da toi uu 07/03/2025 EXEC  [dbo].[ThucChay_CPM_Job]` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 7 | TinhThucChay_Admatic | `-- Job chay theo phuong phap cu chua toi uu --EXEC [dbo].[Job_ThucChay_Admatic_NhieuSanPham]  --Job thuc chay da toi uu 10/03/2025 EXEC  [dbo].[ThucChay_Admatic_Job]` | ABM_Data_ThucChay | Quit (Success) | Go to step |
| 8 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] ThucChay_Admatic_CPM" -smtpBody "Job loi ThucChay_Admatic_CPM"` | msdb | Quit (Success) | Quit (Failure) |

---
## Job: `ThucChay_CPD_Chiphi_PR`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: Nhóm 1: 
CPD, Chiphikhac, PR, Admarket, 
PB dieuchinhgia, CPM ngay, Mobile, Inventory

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | Job_TinhThucChay_CPD | `EXEC [dbo].[ThucChay_CPD_Job]` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 2 | Job_TinhThucChay_ChiPhiKhac | `--EXEC dbo.ThucChay_TinhChiPhiKhac_ByJobs --Truoc toi uu --job sau toi uu 06/02/2025 EXEC [dbo].[ThucChay_ChiPhi_Job]` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 3 | Job_TinhThucChay_PR | `--job tinh thuc chay pr theo phuong phap cu --EXEC dbo. ThucChay_TinhPR_BySQLJobs  -- job PR duoc toi u theo phuong phap moi 20/03/2025 EXEC [dbo].[ThucChay_PR_Job]` | ABM_Data_ThucChay | Quit (Success) | Go to next step |
| 4 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] ThucChay_CPD_Chiphi_PR_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory" -smtpBody "Job loi ThucChay_CPD_Chiphi_PR_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory"` | msdb | Quit (Success) | Quit (Failure) |

---
## Job: `ThucChay_GoogleFacebook_MktFee`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: Tinh thuc chay cho 02 nhom san pham GoogleFacebook va Marketing fee

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | EXEC [dbo].[ThucChay_GGFB_Job] | `--EXEC dbo.ThucChay_TinhGoogleFacebook_BySQLJobs -- job toi uu trien ngay 20250324 EXEC [dbo].[ThucChay_GGFB_Job]` | ABM_Data_ThucChay | Go to next step | Go to step |
| 2 | Job Marketing fee | `EXEC [dbo].[ThucChay_MKT_FEE_Job]` | ABM_Data_ThucChay | Quit (Success) | Quit (Failure) |
| 3 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] ThucChay_GoogleFacebook" -smtpBody "Job loi ThucChay_GoogleFacebook"` | msdb | Quit (Success) | Quit (Failure) |

---
## Job: `ThucChay_MuaNgoai`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: No description available.

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | EXEC_ThucChay_TinhMuaNgoai | `EXEC dbo.ThucChay_TinhMuaNgoai_BySQLJobs` | ABM_Data_ThucChay | Quit (Success) | Go to step |
| 2 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] ThucChay_MuaNgoai" -smtpBody "Job loi ThucChay_MuaNgoai"` | msdb | Quit (Success) | Quit (Failure) |

---
## Job: `cdc.ABM_Data_ThucChay_capture`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: CDC Log Scan Job

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | Starting Change Data Capture Collection Agent | `RAISERROR(22801, 10, -1)` | ABM_Data_ThucChay | Go to next step | Go to next step |
| 2 | Change Data Capture Collection Agent | `sys.sp_MScdc_capture_job` | ABM_Data_ThucChay | Quit (Success) | Quit (Failure) |

---
## Job: `cdc.ABM_Data_ThucChay_cleanup`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: CDC Cleanup Job

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | Change Data Capture Cleanup Agent | `sys.sp_MScdc_cleanup_job` | ABM_Data_ThucChay | Quit (Success) | Quit (Failure) |

---
## Job: `job_TinhLaiThucChay`
- **Trạng thái**: ✅ Đang bật
- **Mô tả**: No description available.

| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |
|------|----------|----------------------|----------|----------------|--------------|
| 1 | exec sql | `exec job_ThucChayDaTinh_ReInsertByHopDong` | ABM_Data_ThucChay | Quit (Success) | Go to step |
| 2 | Canh_Bao_job_chay_FAILURE | `D:\script\send_mail.ps1 -Subject "[Canh bao job loi] job_TinhLaiThucChay" -smtpBody "Job loi job_TinhLaiThucChay"` | msdb | Quit (Success) | Quit (Failure) |
