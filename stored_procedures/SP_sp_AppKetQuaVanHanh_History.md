# Stored Procedure: `sp_AppKetQuaVanHanh_History`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:48:02.630000
- **Ngày sửa cuối**: 2026-03-06 16:48:02.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE sp_AppKetQuaVanHanh_History
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Chi tiết
   SELECT Id
,HopDongBanRef AS HopdongID
,PhanBoRef AS PhanBo
,PbSoLuong 
,dbo.FormatNumber(pbDonGia) AS pbDonGia
,PbChietKhau
,dbo.FormatNumber(PbThanhTien) AS PbThanhTien
,NgayThucHien
,TcDonViTinh
,TcSoLuong
,dbo.FormatNumber(TcDonGia) AS TcDonGia
,dbo.FormatNumber(TcThanhTien) AS TcThanhTien
,AppHopDongKolRef
,AppHopDongKolRef
,VAT
,CASE
            WHEN TrangThai = 1 THEN N'1: Mới (k tính)'
	        WHEN TrangThai = 2 THEN N'2: Gửi duyệt (gửi leader duyệt)(k tính)'
		    WHEN TrangThai = 3 THEN N'3: Duyệt KQVH (leader duyệt)'
		    WHEN TrangThai = 4 THEN N'4: Từ chối duyệt KQVH (k tính)'
		    WHEN TrangThai = 5 THEN N'5: Gửi duyệt TT: Gửi kế toán duyệt TT'
		    WHEN TrangThai = 6 THEN N'6: Duyệt TT: Kế toán duyệt TT'
		    WHEN TrangThai = 7 THEN N'7: Từ chối duyệt TT'
		    WHEN TrangThai = 8 THEN N'8: Gửi review TT'
	        ELSE N''
       END AS TrangThai
,Version
,VAT
,CreationTime
,CreatorUserName
,LastModificationTime
,LastModifierUserName
,NgayDuyet
,NguoiDuyet
FROM ASDAG2.AbpZeroDb_SanPham_CreatorContent.dbo.AppKetQuaVanHanhHistory 
WHERE PhanBoRef =@HopDongChiTietID
AND IsDeleted = 0
ORDER BY LastModificationTime DESC


END

```
