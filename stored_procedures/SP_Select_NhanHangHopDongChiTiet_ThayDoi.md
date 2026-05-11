# Stored Procedure: `Select_NhanHangHopDongChiTiet_ThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-18 15:19:30.090000
- **Ngày sửa cuối**: 2018-06-06 11:48:22.433000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================================================
-- Author:		hungtruongviet
-- Create date: 18/5/2018
-- Description:	show nhãn hàng đánh số từ sai lệch của phần bổ DB : ABM và CONTRACT
-- ==============================================================================

CREATE PROCEDURE [dbo].[Select_NhanHangHopDongChiTiet_ThayDoi]

AS
BEGIN
Select 
					[HopDongChiTietID]
	,				[DanhSachNhanHangREF_ABM]
	,				[DanhSachNhanHang_CONTRACT]
	,				N'Nhãn hàng đánh số trên ABM và CONTRACT sai lệch'
					[Warring]
From dbo.[KiemTraNhanHangThayDoi]
Where [HopDongChiTietID] <> '505885'
END
```
