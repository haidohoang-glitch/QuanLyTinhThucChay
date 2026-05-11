# 04 — Danh mục Job (Job_desc)

> **Ghi chú**: `job_type_name = 0` (Job lấy dữ liệu / Sync), `job_type_name = 1` (Job tính toán thực chạy)

| Tên Job | Loại Job | Ý nghĩa / Mô tả chi tiết |
|---------|----------|--------------------------|
| `Job_DoDuLieuTuAPI` | 0 (Sync Data) | Job lấy thông tin thực chạy để tính cho nhóm sản phẩm: Admatic, CPM thuần, CPV, CPR, Trueview, Mobile, Native_Ads/On Image, CPM đơn vị bài, CPM đơn vị gói, CPM đơn vị ngày |
| `Job_GetInfo_ThucChay_GGFB` | 0 (Sync Data) | lấy thông tin thực chạy để tính cho nhóm sản phẩm: GGFB - theo thực tế phát sinh, GGFB - theo sản lượng chốt |
| `Job_GetInforThucTreo_PR` | 0 (Sync Data) | Lấy thông tin thực treo để tính thực chạy cho nhóm sản phẩm : PR |
| `Job_GetInforThucTreo_ThucChayMuaNgoai_GGFB_FromHDCN` | 0 (Sync Data) | Lấy thông tin thực treo, mua ngoai để phục vụ cho đữ liệu đầu vào tính |
| `job_InsertBanner_Branding_thanhtien_admatic` | 0 (Sync Data) | Xác định banner là của Admatic treo bên Branding để tính tiền và đổ vào table thucchaythanhtien_admatic |
| `job_Syn_DataLogFrom_CauHinhNhomTinh_LoaiHD_ToolContract_ADS` | 0 (Sync Data) | job syn du lieu tu tool contract de phuc vu viec tinh du lieu thuc chay, va du lieu log cua cac table trong tool nhập GGFB (ADS) va cap nhap thong tin Loai_Treo = 3 (chi phi) tu DmSanPham sang table CauHinhNhomTinhDoanhSoThucChay và DmLoaiHopDongNoiBo |
| `job_Syn_DataLogFrom_ToolContract_ADS` | 0 (Sync Data) | job syn du lieu log table nghiệp vụ tu tool contract de phuc vu viec tinh du lieu thuc chay, va du lieu log cua cac table trong tool nhập GGFB (ADS) |
| `ThucChay_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory_CPM_Admatic` | 1 (Calc Data) | Tinh thực chạy cho các nhóm: Inventory, Admatic, CPM thuần, CPV, CPR, Trueview, Mobile, Native_Ads/On Image, CPM đơn vị bài, CPM đơn vị gói, CPM đơn vị ngày, Admarket, Admarket điều chỉnh giá trị |
| `ThucChay_CPD_Chiphi_PR` | 1 (Calc Data) | Tính thực chạy cho các nhóm sản phẩm: CPD đợt chạy, CPD không đợt chạy, CPD đơn vị gói, PR, Chi phí khác, Chi phí sản phẩm chính |
| `ThucChay_GoogleFacebook_MktFee` | 1 (Calc Data) | Tính thực chạy cho nhóm: GGFB - theo thực tế phát sinh, GGFB - theo sản lượng chốt, sản phẩm Marketing fee |
| `ThucChay_MuaNgoai` | 1 (Calc Data) | Tính thực chạy cho nhóm sản phẩm Mua ngoài |