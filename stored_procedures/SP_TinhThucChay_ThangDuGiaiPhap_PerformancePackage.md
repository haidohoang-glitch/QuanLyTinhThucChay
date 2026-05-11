# Stored Procedure: `TinhThucChay_ThangDuGiaiPhap_PerformancePackage`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-10-24 15:33:21.807000
- **Ngày sửa cuối**: 2022-10-24 15:33:21.807000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[TinhThucChay_ThangDuGiaiPhap_PerformancePackage]
    -- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    SELECT 'ThucTreo_ThucChayDaTinh';
    -- check tính đúng bảng TCDT
    SELECT A.shd,
           A.HopDongID,
           A.HopDongChiTietREF,
           A.TenHTQC,
           A.DmSanPhamREF,
           A.TenSanPham,
           A.TenViTri,
           A.RecordStatus,
           dbo.FormatNumber(A.ThanhTien) ThanhTien,
           dbo.FormatNumber(A.tt) tt,
           (A.ThanhTien - A.tt) lechTTTT,
           B.SoHopDong,
           B.HopDongID,
           B.HopDongChiTietREF,
           B.DmSanPhamREF,
           dbo.FormatNumber(B.ThanhTienThucChay) ThanhTienThucChay,
           dbo.FormatNumber(A.tt - B.ThanhTienThucChay) LechTT_TC
    FROM
    (
        SELECT hd.SoHopDong shd,
               tchdctp.HopDongID,
               tchdctp.HopDongChiTietREF,
               hdct.TenLoai TenHTQC,
               hdct.DmSanPhamREF,
               hdct.TenSanPham,
               tchdctp.DmViTriREF,
               tchdctp.TenViTri,
               hdct.ThanhTien,
               tchdctp.LastModifiedAt,
               tchdctp.RecordStatus,
               SUM(tchdctp.SoTienThayDoi) tt
        FROM dbo.ThucChay_PerformanceBase_ThayDoi tchdctp
            INNER JOIN HopDongChiTiet hdct
                ON tchdctp.HopDongChiTietREF = hdct.HopDongChiTietID
            INNER JOIN HopDong hd
                ON hd.HopDongID = tchdctp.HopDongID
        WHERE tchdctp.DeletedStatus = 0
              AND tchdctp.LoaiGhiNhan = 1
              AND hdct.DeletedStatus <> 1
              AND TrangThaiHopDong <> 3
              AND hdct.ThanhTien <> 0
              AND CONVERT(DATE, tchdctp.LastModifiedAt) = @NgayThucHien
        GROUP BY hd.SoHopDong,
                 tchdctp.HopDongID,
                 tchdctp.HopDongChiTietREF,
                 hdct.TenLoai,
                 hdct.DmSanPhamREF,
                 hdct.TenSanPham,
                 tchdctp.DmViTriREF,
                 tchdctp.TenViTri,
                 hdct.ThanhTien,
                 tchdctp.LastModifiedAt,
                 tchdctp.RecordStatus
    ) A
        FULL OUTER JOIN
        (
            SELECT SoHopDong,
                   HopDongID,
                   HopDongChiTietREF,
                   tcdt.DmSanPhamREF,
                   tcdt.DmViTriREF,
                   SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ThanhTienThucChay
            FROM ThucChayDaTinh tcdt
            WHERE NgayThucHien = @NgayThucHien
                  AND tcdt.HopDongChiTietREF IN
                      (
                          SELECT HopDongChiTietREF
                          FROM ThucChay_PerformanceBase_ThayDoi
                          WHERE DeletedStatus = 0
                                AND LoaiGhiNhan = 1
                                AND CONVERT(DATE, LastModifiedAt) = @NgayThucHien
                      )
            GROUP BY SoHopDong,
                     HopDongID,
                     HopDongChiTietREF,
                     tcdt.DmSanPhamREF,
                     tcdt.DmViTriREF
        ) B
            ON A.HopDongChiTietREF = B.HopDongChiTietREF
    WHERE 1 = 1;

    SELECT 'ThucTreo_ThucChayDaTinhAdmarket';
    -- check tính đúng bảng TCDTAdmarket
    SELECT A.shd,
           A.HopDongID,
           A.HopDongChiTietREF,
           A.TenHTQC,
           A.DmSanPhamREF,
           A.TenSanPham,
           A.TenViTri,
           dbo.FormatNumber(A.ThanhTien) ThanhTien,
           dbo.FormatNumber(A.tt) tt,
           (A.ThanhTien - A.tt) lechTTTT,
           B.SoHopDong,
           B.HopDongID,
           B.HopDongChiTietREF,
           B.DmSanPhamREF,
           dbo.FormatNumber(B.ThanhTienThucChay_MN) ThanhTienThucChay_MN,
           dbo.FormatNumber(A.tt - B.ThanhTienThucChay_MN) LechTT_TCMN
    FROM
    (
        SELECT hd.SoHopDong shd,
               tchdctp.HopDongID,
               tchdctp.HopDongChiTietREF,
               hdct.TenLoai TenHTQC,
               hdct.DmSanPhamREF,
               hdct.TenSanPham,
               tchdctp.DmViTriREF,
               tchdctp.TenViTri,
               hdct.ThanhTien,
               tchdctp.LastModifiedAt,
               SUM(tchdctp.SoTienThayDoi) tt
        FROM dbo.ThucChay_PerformanceBase_ThayDoi tchdctp
            INNER JOIN HopDongChiTiet hdct
                ON tchdctp.HopDongChiTietREF = hdct.HopDongChiTietID
            INNER JOIN HopDong hd
                ON hd.HopDongID = tchdctp.HopDongID
        WHERE tchdctp.DeletedStatus = 0
              AND tchdctp.DmSanPhamREF IN ( 144, 585, 628 )
              AND tchdctp.LoaiGhiNhan = 1
              AND hdct.DeletedStatus <> 1
              AND TrangThaiHopDong <> 3
              AND hdct.ThanhTien <> 0
              AND CONVERT(DATE, tchdctp.LastModifiedAt) = @NgayThucHien
        GROUP BY hd.SoHopDong,
                 tchdctp.HopDongID,
                 tchdctp.HopDongChiTietREF,
                 hdct.TenLoai,
                 hdct.DmSanPhamREF,
                 hdct.TenSanPham,
                 tchdctp.DmViTriREF,
                 tchdctp.TenViTri,
                 hdct.ThanhTien,
                 tchdctp.LastModifiedAt
    ) A
        FULL OUTER JOIN
        (
            SELECT SoHopDong,
                   tcdt.HopDongID,
                   HopDongChiTietREF,
                   tcdt.DmSanPhamREF,
                   tcdt.DmViTriREF,
                   SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienThucChay_MN
            FROM dbo.ThucChayDaTinhAdmarket tcdt
            WHERE NgayThucHien = @NgayThucHien
                  AND tcdt.HopDongChiTietREF IN
                      (
                          SELECT HopDongChiTietREF
                          FROM ThucChay_PerformanceBase_ThayDoi
                          WHERE DeletedStatus = 0
                                AND tcdt.DmSanPhamREF IN ( 144, 585, 628 )
                                AND LoaiGhiNhan = 1
                                AND CONVERT(DATE, LastModifiedAt) = @NgayThucHien
                      )
            GROUP BY SoHopDong,
                     tcdt.HopDongID,
                     HopDongChiTietREF,
                     tcdt.DmSanPhamREF,
                     tcdt.DmViTriREF
        ) B
            ON A.HopDongChiTietREF = B.HopDongChiTietREF
    WHERE 1 = 1;
    SELECT 'ThucTreo_ThucChayDaTinh_MuaNgoai';
    -- check tính đúng bảng TCDTAdmarket
    SELECT A.shd,
           A.HopDongID,
           A.HopDongChiTietREF,
           A.TenHTQC,
           A.DmSanPhamREF,
           A.TenSanPham,
           A.TenViTri,
           dbo.FormatNumber(A.ThanhTien) ThanhTien,
           dbo.FormatNumber(A.tt) tt,
           (A.ThanhTien - A.tt) lechTTTT,
           A.RecordStatus,
           B.SoHopDong,
           B.HopDongREF,
           B.HopDongChiTietREF,
           B.DmSanPhamREF,
           dbo.FormatNumber(B.ThanhTienThucChay_MN) ThanhTienThucChay_MN,
           dbo.FormatNumber(A.tt - B.ThanhTienThucChay_MN) LechTT_TCMN
    FROM
    (
        SELECT hd.SoHopDong shd,
               tchdctp.HopDongID,
               tchdctp.HopDongChiTietREF,
               hdct.TenLoai TenHTQC,
               hdct.DmSanPhamREF,
               hdct.TenSanPham,
               tchdctp.DmViTriREF,
               tchdctp.TenViTri,
               hdct.ThanhTien,
               tchdctp.RecordStatus,
               tchdctp.LastModifiedAt,
               SUM(tchdctp.SoTienThayDoi) tt
        FROM dbo.ThucChay_PerformanceBase_ThayDoi tchdctp
            INNER JOIN HopDongChiTiet hdct
                ON tchdctp.HopDongChiTietREF = hdct.HopDongChiTietID
            INNER JOIN HopDong hd
                ON hd.HopDongID = tchdctp.HopDongID
        WHERE tchdctp.DeletedStatus = 0
              AND tchdctp.LoaiGhiNhan = 1
              AND hdct.DeletedStatus <> 1
              AND TrangThaiHopDong <> 3
              AND hdct.ThanhTien <> 0
              AND CONVERT(DATE, tchdctp.LastModifiedAt) = @NgayThucHien
        GROUP BY hd.SoHopDong,
                 tchdctp.HopDongID,
                 tchdctp.HopDongChiTietREF,
                 hdct.TenLoai,
                 hdct.DmSanPhamREF,
                 hdct.TenSanPham,
                 tchdctp.DmViTriREF,
                 tchdctp.TenViTri,
                 tchdctp.RecordStatus,
                 hdct.ThanhTien,
                 tchdctp.LastModifiedAt
    ) A
        FULL OUTER JOIN
        (
            SELECT SoHopDong,
                   tcdt.HopDongREF,
                   HopDongChiTietREF,
                   tcdt.DmSanPhamREF,
                   tcdt.DmViTriREF,
                   SUM(tcdt.ThanhTienLaiThucChaySauCK + tcdt.GiaTriThayDoiLaiSauCK) ThanhTienThucChay_MN
            FROM dbo.ThucChayDaTinh_MuaNgoai tcdt
            WHERE NgayThucHien = @NgayThucHien
                  AND tcdt.HopDongChiTietREF IN
                      (
                          SELECT HopDongChiTietREF
                          FROM ThucChay_PerformanceBase_ThayDoi
                          WHERE DeletedStatus = 0
                                AND LoaiGhiNhan = 1
                                AND CONVERT(DATE, LastModifiedAt) = @NgayThucHien
                      )
            GROUP BY SoHopDong,
                     tcdt.HopDongREF,
                     HopDongChiTietREF,
                     tcdt.DmSanPhamREF,
                     tcdt.DmViTriREF
        ) B
            ON A.HopDongChiTietREF = B.HopDongChiTietREF
    WHERE 1 = 1;
-- Insert statements for procedure here
END;

```
