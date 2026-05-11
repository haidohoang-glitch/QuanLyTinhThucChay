# Stored Procedure: `sp_AppKetQuaVanHanh_Nguon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:45:47.030000
- **Ngày sửa cuối**: 2026-03-06 16:45:47.030000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE sp_AppKetQuaVanHanh_Nguon
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Chi tiết
    SELECT 
           Id,
           HopDongBanRef,
           PhanBoRef,
           PbSoLuong,
           dbo.FormatNumber(pbDonGia)        AS pbDonGia,
           dbo.FormatNumber(PbChietKhau)     AS PbChietKhau,
           dbo.FormatNumber(PbThanhTien)     AS PbThanhTien,
           TcSoLuong,
           dbo.FormatNumber(TcDonGia)        AS TcDonGia,
           dbo.FormatNumber(TcThanhTien)     AS TcThanhTien,
           dbo.FormatNumber(DonGia)          AS DonGia,
           ChietKhau,
           dbo.FormatNumber(ThanhTien)       AS ThanhTien,
	       CASE 
                WHEN TrangThai = 1 THEN N'1: Mới (k tính)'
	            WHEN TrangThai = 2 THEN N'2: Gửi duyệt (gửi leader duyệt)(k tính)'
	            WHEN TrangThai = 3 THEN N'3: Duyệt KQVH (leader duyệt)'
		        WHEN TrangThai = 4 THEN N'4: Từ chối duyệt KQVH (k tính)'
		        WHEN TrangThai = 5 THEN N'5: Gửi duyệt TT: Gửi kế toán duyệt TT'
		        WHEN TrangThai = 6 THEN N'6: Duyệt TT: Kế toán duyệt TT'
		        WHEN TrangThai = 7 THEN N'7: Từ chối duyệt TT'
		        WHEN TrangThai = 8 THEN N'8: Gửi review TT'
	            ELSE N'' 
           END AS TrangThai,
           IsDeleted,
           CreationTime,
	       CreatorUserId,
           LastModificationTime,
	       LastModifierUserId
    FROM ASDAG2.AbpZeroDb_SanPham_CreatorContent.dbo.AppKetQuaVanHanh
    WHERE PhanBoRef = @HopDongChiTietID

    UNION ALL

    -- Tổng
    SELECT
           NULL AS Id,
           NULL AS HopDongBanRef,
           NULL AS PhanBoRef,
           SUM(PbSoLuong) AS PbSoLuong,
           NULL AS pbDonGia,
           NULL AS PbChietKhau,
           dbo.FormatNumber(SUM(PbThanhTien)) AS PbThanhTien,
           SUM(TcSoLuong) AS TcSoLuong,
           NULL AS TcDonGia,
           dbo.FormatNumber(SUM(TcThanhTien)) AS TcThanhTien,
           NULL AS DonGia,
           NULL AS ChietKhau,
           dbo.FormatNumber(SUM(ThanhTien)) AS ThanhTien,
	       N'TỔNG' AS TrangThai,
           0 AS IsDeleted,
           NULL AS CreationTime,
	       NULL AS CreatorUserId,
           NULL AS LastModificationTime,
	       NULL AS LastModifierUserId
    FROM ASDAG2.AbpZeroDb_SanPham_CreatorContent.dbo.AppKetQuaVanHanh
    WHERE PhanBoRef = @HopDongChiTietID;

END

```
