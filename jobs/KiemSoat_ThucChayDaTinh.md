# Job: KiemSoat_ThucChayDaTinh

## Thông Tin Cơ Bản
| Thuộc tính | Giá trị |
|---|---|
| Job Name | KiemSoat_ThucChayDaTinh |
| Database | ABM_Data_ThucChay |
| Hệ thống | Tính toán thực chạy |

## Các Bước (Steps)
| Step ID | Step Name | Command | Tác dụng |
|---|---|---|---|
| 1 | KiemSoat_ThucChayDaTinh_website_nhieuhon1ID | `EXEC dbo.KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID` | Gọi SP |
| 2 | KiemSoat_DataThucChay_ThayDoi_Mobile | `EXEC [dbo].[KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay]  @TypeProduct = 1010` | Gọi SP |

## Data Flow (Luồng Dữ Liệu)
```mermaid
graph TD
    Job_KiemSoat_ThucChayDaTinh[Job: KiemSoat_ThucChayDaTinh]
    Job_KiemSoat_ThucChayDaTinh --> SP_dbo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID(SP: dbo.KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID)
    SP_dbo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID --> Ent_KiemSoat_ThucChayDaTinh_Website[(Table: KiemSoat_ThucChayDaTinh_Website)]
    SP_dbo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID --> Ent_KiemSoat_ThucChayDaTinh_Website[(Table: KiemSoat_ThucChayDaTinh_Website)]
    SP_dbo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID --> Ent_KS_ThucChay_TCDT_Website[(Table: KS_ThucChay_TCDT_Website)]
    SP_dbo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID --> Ent_KS_ThucChay_TCDT_Website[(Table: KS_ThucChay_TCDT_Website)]
    SP_dbo_KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID --> Ent_ThucChayDaTinh[(Table: ThucChayDaTinh)]
    Job_KiemSoat_ThucChayDaTinh --> SP_dbo_KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay(SP: dbo.KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay)
    SP_dbo_KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay --> Ent_DataThucChay[(Table: DataThucChay)]
    SP_dbo_KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay --> Ent_DataThucChay_2[(Table: DataThucChay_2)]
    SP_dbo_KiemSoat_DataThucChay_ThayDoi_KhiTinhThucChay --> Ent_KiemSoat_DataThucChay_ThayDoi[(Table: KiemSoat_DataThucChay_ThayDoi)]
```
