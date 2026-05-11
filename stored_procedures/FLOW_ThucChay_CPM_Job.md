# Phân tích Luồng nghiệp vụ: `ThucChay_CPM_Job`

## 1. Sơ đồ Call Graph (Mermaid)

```mermaid
graph TD
    ThucChay_CPM_Job[ThucChay_CPM_Job]:::rootNode
    ThucChay_CPM_Job -->|Level 1| CauHinhNhomTinhDoanhSoThucChay
    ThucChay_CPM_Job -->|Level 1| ThucChay_CPM_Update_HopDongChiTietAndBanner
    ThucChay_CPM_Job -->|Level 1| ThucChay_CPMDonViBai
    ThucChay_CPM_Job -->|Level 1| ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| ThucChay_NativeAds_Update_HopDongChiTietAndBanner
    ThucChay_CPM_Job -->|Level 1| ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh
    ThucChay_CPM_Job -->|Level 1| thucchaydatinh
    ThucChay_CPM_Update_HopDongChiTietAndBanner -->|Level 2| CheckDonViTinhHinhThucCPDAndNotCPD
    ThucChay_CPM_Update_HopDongChiTietAndBanner -->|Level 2| HopDong
    ThucChay_CPM_Update_HopDongChiTietAndBanner -->|Level 2| HopDongChiTiet
    ThucChay_CPM_Update_HopDongChiTietAndBanner -->|Level 2| tchdctab
    ThucChay_CPM_Update_HopDongChiTietAndBanner -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_CPM_Update_HopDongChiTietAndBanner -->|Level 2| ThucChayHopDongChiTietAndBanner
    ThucChay_CPMDonViBai -->|Level 2| dm
    ThucChay_CPMDonViBai -->|Level 2| GetDmWebsiteReportingdbIDByDmWebsiteID
    ThucChay_CPMDonViBai -->|Level 2| GetWebsiteLinkByDmWebsiteID
    ThucChay_CPMDonViBai -->|Level 2| HopDong
    ThucChay_CPMDonViBai -->|Level 2| HopDongChiTiet
    ThucChay_CPMDonViBai -->|Level 2| HopDongChiTietLog
    ThucChay_CPMDonViBai -->|Level 2| tchdct
    ThucChay_CPMDonViBai -->|Level 2| thucchaydatinh
    ThucChay_CPMDonViBai -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_CPMDonViBai -->|Level 2| ThucChayHopDongChiTietLog
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| DataType_Thucchay_CPMDonViGoi_DmTinhMoi
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| dm
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| DmThongTinHopDongBanInventory
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| temp
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_Native_Ads
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| thucchaydatinh
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner_Native_Ads
    ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayTrueView
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| DataType_Thucchay_CPMDonViGoi_DmTinhlai
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| dm
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| DmThongTinHopDongBanInventory
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| GhiNhanThanhLy
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDongChiTietLog
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| temp
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_Native_Ads
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| thucchaydatinh
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner_Native_Ads
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietLog
    ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayTrueView
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| CauHinhNhomTinhDoanhSoThucChay
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| CheckDonViTinhHinhThucCPDAndNotCPD
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| DataType_Thucchay_CPMthuan_DmTinhMoi
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| dm
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| temp
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| thucchay
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_CPM_Insert_ThucChayDaTinh
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayDaTinh
    ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| CauHinhNhomTinhDoanhSoThucChay
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| CheckDonViTinhHinhThucCPDAndNotCPD
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| DataType_Thucchay_CPMthuan_DmTinhlai
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| dm
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| GetProductIDByTypeProduct
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| GetProductNameByTypeProduct
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDongChiTietLog
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| temp
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| thucchay
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_CheckSanPhamBoxAppSelfServing
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayDaTinh
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| DataType_Thucchay_CPMthuan_DmTinhMoi
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| dm
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| temp
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| thucchay
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_CPV_Insert_ThucChayDaTinh
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| thucchayCPV
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| thucchaydatinh
    ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| DataType_Thucchay_NativeAds_DmTinhMoi
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| dm
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| DmThongTinHopDongBanInventory
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| temp
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_Native_Ads
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_NativeAds_Insert_ThucChayDaTinh
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| thucchaydatinh
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner_Native_Ads
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| DataType_Thucchay_NativeAds_DmTinhlai
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| dm
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| DmThongTinHopDongBanInventory
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| GhiNhanThanhLy
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDongChiTietLog
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| temp
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_Native_Ads
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| thucchaydatinh
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner_Native_Ads
    ThucChay_NativeAds_Update_HopDongChiTietAndBanner -->|Level 2| HopDong
    ThucChay_NativeAds_Update_HopDongChiTietAndBanner -->|Level 2| HopDongChiTiet
    ThucChay_NativeAds_Update_HopDongChiTietAndBanner -->|Level 2| tchdctab
    ThucChay_NativeAds_Update_HopDongChiTietAndBanner -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_NativeAds_Update_HopDongChiTietAndBanner -->|Level 2| ThucChayHopDongChiTietAndBanner_Native_Ads
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| DataType_Thucchay_CPMthuan_DmTinhMoi
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| dm
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| temp
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChay_TrueView_Insert_ThucChayDaTinh
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| thucchaydatinh
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner
    ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh -->|Level 2| ThucChayTrueView
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| DataType_Thucchay_CPMthuan_DmTinhlai
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| dm
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| GetProductIDByTypeProduct
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| GetProductNameByTypeProduct
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDong
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDongChiTiet
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| HopDongChiTietLog
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| temp
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChay_TrueView_DoiTruTinhLai_ThucChayDaTinh
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| thucchaydatinh
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTiet
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayHopDongChiTietAndBanner
    ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh -->|Level 2| ThucChayTrueView
    CheckDonViTinhHinhThucCPDAndNotCPD -->|Level 3| FormatStringUpper
    GetDmWebsiteReportingdbIDByDmWebsiteID -->|Level 3| WebsiteMapping_HDCN_Reporting
    GetWebsiteLinkByDmWebsiteID -->|Level 3| WebsiteMapping_HDCN_Reporting
    ThucChay_CPM_Insert_ThucChayDaTinh -->|Level 3| DataType_Thucchay_CPMthuan_DmTinhMoi
    ThucChay_CPM_Insert_ThucChayDaTinh -->|Level 3| GetProductIDByTypeProduct
    ThucChay_CPM_Insert_ThucChayDaTinh -->|Level 3| GetProductNameByTypeProduct
    ThucChay_CPM_Insert_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_CPM_Insert_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_CPM_Insert_ThucChayDaTinh -->|Level 3| ThucChay_GetDonViTinhNotCPD_v2
    ThucChay_CPM_Insert_ThucChayDaTinh -->|Level 3| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_CPM_Insert_ThucChayDaTinh -->|Level 3| ThucChayDaTinh
    ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| DataType_Thucchay_CPMDonViGoi_DmTinhlai
    ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| DmSanPham
    ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| thucchaydatinh
    ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh -->|Level 3| DataType_Thucchay_CPMDonViGoi_DmTinhMoi
    ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh -->|Level 3| DmSanPham
    ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh -->|Level 3| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh -->|Level 3| thucchaydatinh
    ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| DataType_Thucchay_CPMthuan_DmTinhlai
    ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| ThucChay_GetDonViTinhNotCPD_v2
    ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| ThucChayDaTinh
    ThucChay_CPV_Insert_ThucChayDaTinh -->|Level 3| DataType_Thucchay_CPMthuan_DmTinhMoi
    ThucChay_CPV_Insert_ThucChayDaTinh -->|Level 3| GetProductIDByTypeProduct
    ThucChay_CPV_Insert_ThucChayDaTinh -->|Level 3| GetProductNameByTypeProduct
    ThucChay_CPV_Insert_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_CPV_Insert_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_CPV_Insert_ThucChayDaTinh -->|Level 3| ThucChay_GetDonViTinhNotCPD_v2
    ThucChay_CPV_Insert_ThucChayDaTinh -->|Level 3| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_CPV_Insert_ThucChayDaTinh -->|Level 3| thucchaydatinh
    ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| DataType_Thucchay_NativeAds_DmTinhlai
    ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| thucchaydatinh
    ThucChay_NativeAds_Insert_ThucChayDaTinh -->|Level 3| DataType_Thucchay_NativeAds_DmTinhMoi
    ThucChay_NativeAds_Insert_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_NativeAds_Insert_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_NativeAds_Insert_ThucChayDaTinh -->|Level 3| ThucChay_GetDonViTinhNotCPD_v2
    ThucChay_NativeAds_Insert_ThucChayDaTinh -->|Level 3| thucchaydatinh
    ThucChay_TrueView_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| DataType_Thucchay_CPMthuan_DmTinhlai
    ThucChay_TrueView_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_TrueView_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_TrueView_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| ThucChay_GetDonViTinhNotCPD_v2
    ThucChay_TrueView_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_TrueView_DoiTruTinhLai_ThucChayDaTinh -->|Level 3| thucchaydatinh
    ThucChay_TrueView_Insert_ThucChayDaTinh -->|Level 3| DataType_Thucchay_CPMthuan_DmTinhMoi
    ThucChay_TrueView_Insert_ThucChayDaTinh -->|Level 3| GetProductIDByTypeProduct
    ThucChay_TrueView_Insert_ThucChayDaTinh -->|Level 3| GetProductNameByTypeProduct
    ThucChay_TrueView_Insert_ThucChayDaTinh -->|Level 3| HopDong
    ThucChay_TrueView_Insert_ThucChayDaTinh -->|Level 3| HopDongChiTiet
    ThucChay_TrueView_Insert_ThucChayDaTinh -->|Level 3| ThucChay_GetDonViTinhNotCPD_v2
    ThucChay_TrueView_Insert_ThucChayDaTinh -->|Level 3| ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD
    ThucChay_TrueView_Insert_ThucChayDaTinh -->|Level 3| thucchaydatinh

    classDef rootNode fill:#f9f,stroke:#333,stroke-width:4px;
```

## 2. Chi tiết Biến Đầu Vào (Parameters)

### `CauHinhNhomTinhDoanhSoThucChay`
*(Không có tham số)*

### `CheckDonViTinhHinhThucCPDAndNotCPD`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `int(4)` | Có |
| `@DonViTinhREF` | `int(4)` | Không |
| `@DonViTinh` | `nvarchar(100)` | Không |

### `DataType_Thucchay_CPMDonViGoi_DmTinhMoi`
*(Không có tham số)*

### `DataType_Thucchay_CPMDonViGoi_DmTinhlai`
*(Không có tham số)*

### `DataType_Thucchay_CPMthuan_DmTinhMoi`
*(Không có tham số)*

### `DataType_Thucchay_CPMthuan_DmTinhlai`
*(Không có tham số)*

### `DataType_Thucchay_NativeAds_DmTinhMoi`
*(Không có tham số)*

### `DataType_Thucchay_NativeAds_DmTinhlai`
*(Không có tham số)*

### `DmSanPham`
*(Không có tham số)*

### `DmThongTinHopDongBanInventory`
*(Không có tham số)*

### `FormatStringUpper`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `nvarchar(100)` | Có |
| `@TenField` | `nvarchar(100)` | Không |

### `GetDmWebsiteReportingdbIDByDmWebsiteID`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `int(4)` | Có |
| `@DmWebsiteID` | `int(4)` | Không |

### `GetProductIDByTypeProduct`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `int(4)` | Có |
| `@TypeProduct` | `int(4)` | Không |

### `GetProductNameByTypeProduct`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `nvarchar(100)` | Có |
| `@TypeProduct` | `int(4)` | Không |

### `GetWebsiteLinkByDmWebsiteID`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `nvarchar(400)` | Có |
| `@DmWebsiteID` | `int(4)` | Không |
| `@TenWebsite` | `nvarchar(100)` | Không |

### `GhiNhanThanhLy`
*(Không có tham số)*

### `HopDong`
*(Không có tham số)*

### `HopDongChiTiet`
*(Không có tham số)*

### `HopDongChiTietLog`
*(Không có tham số)*

### `ThucChay`
*(Không có tham số)*

### `ThucChayDaTinh`
*(Không có tham số)*

### `ThucChayHopDongChiTiet`
*(Không có tham số)*

### `ThucChayHopDongChiTietAndBanner`
*(Không có tham số)*

### `ThucChayHopDongChiTietAndBanner_Native_Ads`
*(Không có tham số)*

### `ThucChayHopDongChiTietLog`
*(Không có tham số)*

### `ThucChayTrueView`
*(Không có tham số)*

### `ThucChay_CPMDonViBai`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayCheckThayDoi` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_CPMDonViGoi_DmTinhlai` | `DataType_Thucchay_CPMDonViGoi_DmTinhlai` | Không |

### `ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayPhatSinh_Tu` | `date(3)` | Không |
| `@NgayPhatSinh_Den` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayCheckThayDoi` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_CPMDonViGoi_DmTinhMoi` | `DataType_Thucchay_CPMDonViGoi_DmTinhMoi` | Không |

### `ThucChay_CPM_Insert_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_CPMthuan_DmTinhMoi` | `DataType_Thucchay_CPMthuan_DmTinhMoi` | Không |

### `ThucChay_CPM_Job`
*(Không có tham số)*

### `ThucChay_CPM_Update_HopDongChiTietAndBanner`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayCheckThayDoi` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |

### `ThucChay_CPMthuan_DoiTruTinhLai_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_CPMthuan_DmTinhlai` | `DataType_Thucchay_CPMthuan_DmTinhlai` | Không |

### `ThucChay_CPMthuan_GhiNhanPhatSinh_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayPhatSinh_Tu` | `date(3)` | Không |
| `@NgayPhatSinh_Den` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_CPMthuan_GhiNhanThayDoi_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayCheckThayDoi` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_CPV_GhiNhanPhatSinh_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayPhatSinh_Tu` | `date(3)` | Không |
| `@NgayPhatSinh_Den` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_CPV_Insert_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_CPV_DmTinhMoi` | `DataType_Thucchay_CPMthuan_DmTinhMoi` | Không |

### `ThucChay_CheckSanPhamBoxAppSelfServing`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `int(4)` | Có |
| `@DmSanPhamID` | `int(4)` | Không |
| `@TenBanner` | `nvarchar(100)` | Không |

### `ThucChay_GetDonViTinhNotCPD_v2`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `nvarchar(100)` | Có |
| `@DonViTinh` | `nvarchar(100)` | Không |
| `@TenLoai` | `nvarchar(100)` | Không |

### `ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `(Return)` | `float(8)` | Có |
| `@DonViTinh` | `nvarchar(100)` | Không |

### `ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_NativeAds_DmTinhlai` | `DataType_Thucchay_NativeAds_DmTinhlai` | Không |

### `ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayPhatSinh_Tu` | `date(3)` | Không |
| `@NgayPhatSinh_Den` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayCheckThayDoi` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_NativeAds_Insert_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_NativeAds_DmTinhMoi` | `DataType_Thucchay_NativeAds_DmTinhMoi` | Không |

### `ThucChay_NativeAds_Update_HopDongChiTietAndBanner`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayCheckThayDoi` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |

### `ThucChay_Native_Ads`
*(Không có tham số)*

### `ThucChay_TrueView_DoiTruTinhLai_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_TrueView_DmTinhlai` | `DataType_Thucchay_CPMthuan_DmTinhlai` | Không |

### `ThucChay_TrueView_GhiNhanPhatSinh_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayPhatSinh_Tu` | `date(3)` | Không |
| `@NgayPhatSinh_Den` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_TrueView_GhiNhanThayDoi_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@NgayGhiNhan` | `date(3)` | Không |
| `@NgayCheckThayDoi` | `date(3)` | Không |
| `@NgayDanhSoGioiHan` | `date(3)` | Không |
| `@SoHopDong` | `nvarchar(100)` | Không |
| `@HopDongChiTietID` | `int(4)` | Không |

### `ThucChay_TrueView_Insert_ThucChayDaTinh`
| Tên tham số | Kiểu dữ liệu | Output |
|-------------|--------------|--------|
| `@Thucchay_TrueView_DmTinhMoi` | `DataType_Thucchay_CPMthuan_DmTinhMoi` | Không |

### `WebsiteMapping_HDCN_Reporting`
*(Không có tham số)*

### `dm`
*(Không có tham số)*

### `tchdct`
*(Không có tham số)*

### `tchdctab`
*(Không có tham số)*

### `temp`
*(Không có tham số)*

### `thucchay`
*(Không có tham số)*

### `thucchayCPV`
*(Không có tham số)*

### `thucchaydatinh`
*(Không có tham số)*

