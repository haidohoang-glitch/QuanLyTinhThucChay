# Stored Procedure: `sp_KSTC_CheckTCDTGhiNhanTheoNhanHang_ChiPhi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-04-15 10:46:09.017000
- **Ngày sửa cuối**: 2024-12-06 16:54:24.273000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Linhvtt>
-- Create date: <2024-04-15>
-- Description:	<Description,,>
CREATE PROCEDURE  [dbo].[sp_KSTC_CheckTCDTGhiNhanTheoNhanHang_ChiPhi]
	-- Add the parameters for the stored procedure here
	 @NgayThucHien DATE
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT TCDT.SoHopDong,
       TCDT.HopDongID,
       TCDT.HopDongChiTietREF,
       TCDT.TenSanPham,
       TT.DmSanPhamREF,
       TT.DmNhanHangREF,
       dbo.FormatNumber(TT.ThanhtienTreo) ThanhtienTreo,
       dbo.FormatNumber(TCDT.ThanhTienTC) ThanhTienTC,
       dbo.FormatNumber(SUM(TCDT.ThanhTienTC - TT.ThanhtienTreo)) AS chenhlechTCnhanhang
FROM
(
SELECT ttcp.HopDongREF,
ttcp.HopDongChiTietREF,
ttcp.DmSanPhamREF,
SUM(ttcp.ThanhTien)ThanhtienTreo,
ttcp.DmNhanHangREF,
ttcp.NhanHang
FROM dbo.ThucChayHopDongChiTiet ttcp
 INNER JOIN dbo.HopDong hd
 ON hd.HopDongID=ttcp.HopDongREF
 WHERE SUBSTRING(hd.SoHopDong, LEN(hd.SoHopDong) - 1, 2) >= 24 -- lấy các hđ >=2024 do 2024 mới xử lý vấn đề về ghi nhận nhãn hàng 
          AND CONVERT(DATE, ttcp.LastModifiedAt) <= @NgayThucHien
          AND ttcp.DeletedStatus = 0
		   AND ttcp.DmSanPhamREF NOT IN ( 140,549)
		   AND ttcp.TrangThaiTreo=2-- Trạng thái được tính thực chạy 06/12 linh vtt
		   AND ttcp.DmSanPhamREF<> 5182 -- box thông tin bên CPD kiểm soát 
    GROUP BY ttcp.HopDongREF,
ttcp.HopDongChiTietREF,
ttcp.DmNhanHangREF,
ttcp.NhanHang,
ttcp.DmSanPhamREF
) TT
    INNER JOIN
    -- thực chạy đã tính 
    (
        SELECT tcdt.SoHopDong,
               tcdt.HopDongID,
               tcdt.HopDongChiTietREF,
               tcdt.DmSanPhamREF,
               tcdt.TenSanPham,
               tcdt.NhanHang,
               SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhTienTC
        FROM dbo.ThucChayDaTinh tcdt
            INNER JOIN dbo.HopDong hd
                ON tcdt.HopDongID = hd.HopDongID
        WHERE tcdt.NgayThucHien <= @NgayThucHien
              AND SUBSTRING(tcdt.SoHopDong, LEN(tcdt.SoHopDong) - 1, 2) >= 24 -- lấy các hđ >=2024 do 2024 mới xử lý vấn đề về ghi nhận nhãn hàng 
              AND tcdt.SoHopDong <> N'-'
              AND tcdt.SoHopDong <> N'NB'
			  AND tcdt.DmSanPhamREF<>5182 -- SP Box tài trợ thông tin CPD ks 
        GROUP BY tcdt.SoHopDong,
                 tcdt.HopDongChiTietREF,
                 tcdt.DmSanPhamREF,
                 tcdt.TenSanPham,
                 tcdt.NhanHang,
                 tcdt.HopDongID
    ) TCDT
        ON TT.HopDongChiTietREF = TCDT.HopDongChiTietREF
           AND TCDT.DmSanPhamREF = TT.DmSanPhamREF
           AND TT.DmNhanHangREF = TCDT.NhanHang
WHERE --SUBSTRING(TCDT.SoHopDong, LEN(TCDT.SoHopDong) - 1, 2) >= 23-- lấy các hđ >=2023
    TCDT.ThanhTienTC - TT.ThanhtienTreo <> 0
GROUP BY TCDT.SoHopDong,
       TCDT.HopDongID,
       TCDT.HopDongChiTietREF,
       TCDT.TenSanPham,
       TT.DmSanPhamREF,
       TT.DmNhanHangREF,
	   dbo.FormatNumber(TT.ThanhtienTreo),
	   dbo.FormatNumber(TCDT.ThanhTienTC);
END

```
