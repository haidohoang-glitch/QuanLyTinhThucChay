# Job: ThucChay_CPD_Chiphi_PR

## Thông Tin Cơ Bản
| Thuộc tính | Giá trị |
|---|---|
| Job Name | ThucChay_CPD_Chiphi_PR |
| Database | ABM_Data_ThucChay |
| Hệ thống | Tính toán thực chạy |

## Các Bước (Steps) Liên Quan CPD
| Step ID | Step Name | Command | Tác dụng |
|---|---|---|---|
| 1 | Job_TinhThucChay_CPD | `EXEC [dbo].[ThucChay_CPD_Job]` | Gọi SP điều phối chính để tính doanh số cho nhóm CPD |

## Data Flow (Luồng Dữ Liệu)
```mermaid
graph TD
    A[Job: ThucChay_CPD_Chiphi_PR] --> B(SP: ThucChay_CPD_Job)
    B --> C{Phase 1: Tính Mới}
    B --> D{Phase 2: Thay Đổi}
    
    C --> C1[SP: CPDdotchay_PhatSinh...]
    C --> C2[SP: CPDkhongdotchay_PhatSinh...]
    C --> C3[SP: CPDdonvigoi_PhatSinh...]
    
    D --> D1[SP: CPDdotchay_GhiNhanThayDoi...]
    D --> D2[SP: CPDkhongdotchay_GhiNhanThayDoi...]
    D --> D3[SP: CPDdonvigoi_GhiNhanThayDoi...]
    
    C1 --> E[(Table: ThucChayDaTinh)]
    C2 --> E
    C3 --> E
    D1 --> E
    D2 --> E
    D3 --> E
```
