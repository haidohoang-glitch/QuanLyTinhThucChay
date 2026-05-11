# Stored Procedure: `nhung_Dutoanban_Muangoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:44:40.990000
- **Ngày sửa cuối**: 2026-03-06 17:44:40.990000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_Dutoanban_Muangoai]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

SELECT 'DuToanBan Đích'[DuToan],
Id
,MaDuToan
,SoHopDong
,HopDongId
,D_KhachHangREF
,D_NhanHangREF
,dbo.FormatNumber(TongGiaTriHopDong) TongGiaTriHopDong
,dbo.FormatNumber(TongGiaTriMuaNgoai) TongGiaTriHopDong
,dbo.FormatNumber(TongGiaTriDaDuToan) TongGiaTriHopDong
,TrangThai
,NguoiLap
,TypeDuyet
,LyDo
,NguoiDuyet
,NgayDuyet
,CreationTime
,CreatorUserId
,LastModificationTime
,LastModifierUserId
FROM [ASDAG2].PMS.dbo.B_DuToan 
WHERE ID = (select distinct B_DuToanREF from [ASDAG2].PMS.dbo.B_DuToan_ChiTiet WHERE phanboid = @HopDongChiTietID and IsDeleted = 0) 
AND IsDeleted = 0-- du toan ban


END 

```
