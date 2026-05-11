# Stored Procedure: `sp_KSTC_CheckTCDT_ThucChayBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-06 14:51:49.130000
- **Ngày sửa cuối**: 2024-07-08 14:38:29.070000

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
--sp_KSTC_CheckTCDT_ThucChayBan '2022-11-29'

CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_ThucChayBan]
    -- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Insert statements for procedure here
    -----cách check mới, all dữ liệu----
    SELECT tc.*
    FROM
    (
        SELECT TT.*,
               B.*,
               (TT.ThucChayBan - ISNULL(B.tc, 0)) TinhThieu,
               (TT.DuToanBan - B.tc) lechPboThucchay
        FROM
        (
            SELECT A.SHD,
                   A.HopDongFK,
                   A.HopDongChiTietID,
                   A.DmSanPhamREF,
                   A.TenLoai,
                   A.TenSanPham,
                   A.TenWebsite,
                   A.TenLoaiBanner,
                   A.SoLuong,
                   A.DonViTinh,
                   A.DonGia,
                   A.DuToanBan,
                   A.DuToanMua,
                   A.ChietKhau,
                   SUM(A.ThucChayMua) ThucChayMua,
                   ROUND(SUM(A.ThucChayBan), 0) AS ThucChayBan,
                   MAX(A.dtmua) AS NgaySua_DuToan,
                   MAX(A.tcmua) AS NgaySua_ThucChay,
                   MAX(A.dtban) AS NgaySua_HopDongBan
            FROM
            (
                SELECT dbo.GetSoHopDongByID(c.HopDongFK) SHD,
                       c.HopDongFK,
                       a.HopDongChiTietID,
                       c.DmSanPhamREF,
                       b.ThucChayMuaNgoaiChiTietID,
                       c.TenLoai,
                       c.TenSanPham,
                       c.TenWebsite,
                       c.TenLoaiBanner,
                       c.SoLuong,
                       c.DonViTinh,
                       c.DonGia,
                       c.ThanhTien DuToanBan,
                       a.ThanhTienSauCKMua DuToanMua,
                       (CASE
                            WHEN
                            (
                                b.Status IN ( 2, 1, 4 )
                                AND b.CreatedAt >= '2020-05-14'
                            ) THEN
                                b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100
                            WHEN (b.CreatedAt < '2020-05-14') THEN
                                b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100
                            ELSE
                                0
                        END
                       ) ThucChayMua,
                       (CASE
                            WHEN a.ThanhTienSauCKMua = 0 THEN
                       (b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100 + b.ThanhTienLaiThucChaySauCK)
                            --WHEN (B.ThanhTienLaiThucChaySauCK =0 AND ((b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai)/100) = a.ThanhTienSauCKMua ) THEN  a.ThanhTienBanSauCK
                            ELSE
                                CASE
                                    WHEN
                                    (
                                        b.Status IN ( 2, 1, 4 )
                                        AND b.CreatedAt >= '2020-05-14'
                                    ) THEN
                       (b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100) + ThanhTienLaiSauCK
                       * ((b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100)) / a.ThanhTienSauCKMua
                                    WHEN (b.CreatedAt < '2020-05-14') THEN
                       (b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100) + ThanhTienLaiSauCK
                       * ((b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100)) / a.ThanhTienSauCKMua
                                END
                        END
                       ) ThucChayBan,
                       a.LastModifiedAt dtmua,
                       b.LastModifiedAt tcmua,
                       c.LastModifiedAt dtban,
                       c.ChietKhau
                FROM HopDongChiTiet_MuaNgoai a --
                    LEFT JOIN ThucChayMuaNgoaiChiTiet b
                        ON a.HopDongChiTietID = b.HopDongChiTietREF
                           AND b.DeletedStatus = 0
                    LEFT JOIN HopDongChiTiet c
                        ON a.HopDongChiTietID = c.HopDongChiTietID
                           AND c.ChietKhau <> 100
                WHERE 1 = 1
                      AND a.DeletedStatus = 0
                      AND
                      (
                          DmLoaiREF = 13
                          OR DmLoaiBannerREF = 18
                      )
                      AND c.DeletedStatus = 0
                      AND c.HopDongFK IN
                          (
                              SELECT HopDongID FROM HopDong WHERE Nam >= 2017
                          )
                      --AND a.ThanhTienSauCKMua  <> 0
                      AND c.HopDongFK NOT IN ( 1001985 ) --hd test
                      AND a.HopDongChiTietID NOT IN (   574017, 572588, 571173, 568666, 563326, 561708, 561704, 552486,
                                                        514202, 514203,520039,520042,
                                                        514196,                                --hdct cũ tcb vuot nhung ghi nhan = pbo
                                                        599839, 589270, 588520, 586494, 510863, --th đặc biệt: mua = 0
														542198-- hđ đã xư lý vượt 2018
                                                    )
                      AND CONVERT(DATE, b.NgayChot) <= @NgayThucHien
            ) A
            GROUP BY A.SHD,
                     A.HopDongFK,
                     A.HopDongChiTietID,
                     A.DmSanPhamREF,
                     A.TenLoai,
                     A.TenSanPham,
                     A.TenWebsite,
                     A.TenLoaiBanner,
                     A.SoLuong,
                     A.DonViTinh,
                     A.DonGia,
                     A.DuToanBan,
                     A.DuToanMua,
                     A.ChietKhau
        ) TT
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       HopDongChiTietREF,
                       DmSanPhamREF DmSanPhamREF_tcdt,
                       ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) AS tc
                --, SUM(ThanhTienKM) AS ThucChay_KM
                FROM dbo.ThucChayDaTinh
                WHERE (
                          DmLoaiBannerREF = 18
                          OR DmHinhThucQuangCao = 13
                      )
                      AND TrangThaiHopDong <> 3
                      AND Nam >= 2017
                      AND DmChienDichREF = 0
                      AND HopDongChiTietREF NOT IN (   574017, 572588, 571173, 568666, 563326, 561708, 561704, 552486,
                                                       514202, 514203,520039,520042, 514196,                        --hdct cũ tcb vuot nhung ghi nhan = pbo
                                                       505417, 539812, 536491, 550445, 529886, 599839, --th đặc biệt: mua = 0
													   542198-- hđ đã xư lý vượt 2018
                                                   )
                GROUP BY SoHopDong,
                         HopDongID,
                         HopDongChiTietREF,
                         DmSanPhamREF
                HAVING ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) <> 0
            ) B
                ON TT.HopDongChiTietID = B.HopDongChiTietREF
        WHERE 1 = 1
              AND ABS(ISNULL(TT.ThucChayBan, 0) - ISNULL(B.tc, 0)) > 1000
              AND
              (
                  YEAR(TT.NgaySua_DuToan) >= 2020
                  OR YEAR(TT.NgaySua_ThucChay) >= 2020
                  OR YEAR(TT.NgaySua_HopDongBan) >= 2020
              )
              OR TT.HopDongFK IS NULL
    ) tc
    ORDER BY tc.HopDongFK DESC;

END;




```
