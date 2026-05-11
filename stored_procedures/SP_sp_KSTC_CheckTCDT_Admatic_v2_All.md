# Stored Procedure: `sp_KSTC_CheckTCDT_Admatic_v2_All`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-09-25 16:53:41.243000
- **Ngày sửa cuối**: 2023-09-04 16:36:16.843000

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
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_Admatic_v2_All]
    -- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Insert statements for procedure here
    SELECT c.HopDongID,
           c.SoHopDong,
           c.[ThoiGianSuaHopDong],
           c.HopDongChiTietREF,
           dbo.FormatNumber(c.ThanhTienThucChaySauCK_ChuaVAT) ThanhTienThucChaySauCK_ChuaVAT,
           dbo.FormatNumber(c.ThanhTienThucChayKM) ThanhTienThucChayKM,
           c.SoHopDong_TCDT,
           c.HopDongChiTietREF_TCDT,
           dbo.FormatNumber(c.tcdt) tcdt,
           dbo.FormatNumber(c.tcdtkm) tcdtkm,
           c.IsKhuyenMai,
           dbo.FormatNumber(c.ThanhTienHD) ThanhTienHD,
           dbo.FormatNumber(c.mm) mm,
           dbo.FormatNumber(c.[LECH Da tinh - mm]) [LECH Da tinh - mm]
    FROM
    (
        SELECT TC.HopDongID,
               TC.SoHopDong,
               TC.[ThoiGianSuaHopDong],
               TC.HopDongChiTietREF,
               TC.ThanhTienThucChaySauCK_ChuaVAT,
               TC.ThanhTienThucChayKM,
               TCDT.SoHopDong SoHopDong_TCDT,
               TCDT.HopDongChiTietREF HopDongChiTietREF_TCDT,
               TCDT.tcdt,
               TCDT.tcdtkm,
               TCDT.IsKhuyenMai,
               TCDT.ThanhTienHD,
               ROUND(   (CASE
                             WHEN TCDT.IsKhuyenMai = 0 THEN
                        (CASE
                             WHEN ISNULL(TC.ThanhTienThucChaySauCK_ChuaVAT, 0) < ISNULL(TCDT.ThanhTienHD, 0) THEN
                                 ISNULL(ThanhTienThucChaySauCK_ChuaVAT, 0)
                             ELSE
                                 TCDT.ThanhTienHD
                         END
                        )
                             WHEN TCDT.IsKhuyenMai = 1 THEN
                        (CASE
                             WHEN ISNULL(TC.ThanhTienThucChayKM, 0) < ISNULL(TCDT.ThanhTienHD, 0) THEN
                                 ISNULL(ThanhTienThucChayKM, 0)
                             ELSE
                                 TCDT.ThanhTienHD
                         END
                        )
                         END
                        ),
                        0
                    ) mm,
               ROUND(
                        (CASE
                             WHEN TCDT.IsKhuyenMai = 0 THEN
                                 TCDT.tcdt
                                 - (CASE
                                        WHEN ISNULL(TC.ThanhTienThucChaySauCK_ChuaVAT, 0) < ISNULL(TCDT.ThanhTienHD, 0) THEN
                                            ISNULL(ThanhTienThucChaySauCK_ChuaVAT, 0)
                                        ELSE
                                            TCDT.ThanhTienHD
                                    END
                                   )
                             WHEN TCDT.IsKhuyenMai = 1 THEN
                                 TCDT.tcdtkm
                                 - (CASE
                                        WHEN ISNULL(TC.ThanhTienThucChayKM, 0) < ISNULL(TCDT.ThanhTienHD, 0) THEN
                                            ISNULL(ThanhTienThucChayKM, 0)
                                        ELSE
                                            TCDT.ThanhTienHD
                                    END
                                   )
                         END
                        ),
                        0
                    ) [LECH Da tinh - mm]
        FROM
        (
            SELECT hd.HopDongID,
                   tc.SoHopDong,
                   hd.LastModifiedAt [ThoiGianSuaHopDong],
                   HopDongChiTietREF, --tt.DmBannerREF,
                   SUM(ThanhTienThucChaySauCK_ChuaVAT) ThanhTienThucChaySauCK_ChuaVAT,
                   SUM(ThanhTienThucChayKM) ThanhTienThucChayKM
            --,tt.DmBannerREF
            FROM ThucChay_ThanhTien_Admatic tc
                LEFT JOIN HopDong hd
                    ON tc.SoHopDong = hd.SoHopDong
                LEFT JOIN
                (
                    SELECT DISTINCT
                           DmBannerREF,
                           HopDongChiTietREF,
                           DmSanPhamREF
                    FROM ThucChayHopDongChiTiet
                    WHERE 1 = 1
                          AND DmHinhThucQuangCaoREF = 42
                          AND HopDongChiTietREF NOT IN ( 0, -1 )
                          AND DeletedStatus = 0
                ) tt
                    ON tt.DmBannerREF = CONVERT(NVARCHAR(50), tc.DmBannerID)
                       AND tt.HopDongChiTietREF NOT IN (   596562, 601959, 601833, 601456, --pbo đã chạy xong
                                                           596942, 604294,                 -- hd chạy programmatic ghi nhận qua mail
                                                           619385,                         -- pbo đặc biệt, 1 banner gán vào 2 pbo
                                                           592062, 599473,                 -- pbo chạy banner lõi
                                                           591037, 591038, 591039          --hd không ps thực chạy 2021
                                                       )
            WHERE 1 = 1
                  AND TypeProduct NOT IN ( -3, 1 )
                  --AND tc.NgayThucHien = ''
                  AND tc.SoHopDong NOT IN ( 'HD DEMO', 'TEST BILLBOARD', 'HD_TEST' )
                  AND NgayDanhSoHopDong >= '2020-07-20'
                  AND NgayThucHien <= @NgayThucHien
                  --and tc.DmBannerID = 619151
                  --and tt.HopDongChiTietREF = 619151
                  AND
                  (
                      tc.DmSanPhamREF = tt.DmSanPhamREF
                      OR tt.DmSanPhamREF = 733
                  )
                  AND tt.HopDongChiTietREF NOT IN
                      (
                          SELECT HopDongChiTietID
                          FROM HopDongChiTiet
                          WHERE DmLoaiNenTangREF = 9
                                AND DeletedStatus = 0
                      ) --khong check hd admatic programmatic
            --and DmSanPhamREF = 342
            --and NgayThucHien between @FromDate and @ToDate
            GROUP BY hd.HopDongID,
                     tc.SoHopDong,
                     NgayDanhSoHopDong,
                     tt.HopDongChiTietREF,
                     hd.LastModifiedAt --,tt.DmBannerREF
        ) TC
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongChiTietREF,
                       ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) tcdt,
                       SUM(ThanhTienKM + GiaTriKMThayDoi) tcdtkm,
                       hdct.IsKhuyenMai,
                       (CASE
                            WHEN hdct.IsKhuyenMai = 1 THEN
                                SUM(DISTINCT hdct.DonGia * hdct.SoLuong)
                            ELSE
                                hdct.ThanhTien
                        END
                       ) ThanhTienHD
                FROM ThucChayDaTinh tcdt
                    INNER JOIN HopDongChiTiet hdct
                        ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID 
								AND hdct.DonViTinhREF NOT IN (7,84) --Duongnt Thêm đk không tính kiểm tra đơn vị bài. Tách bước KTra Bài riêng
                WHERE 1 = 1
                      --and tcdt.DmBannerREF = 77578
                      AND tcdt.DmHinhThucQuangCao = 42
                      AND tcdt.DmSanPhamREF NOT IN ( 817, 560, 140,253,535 )
                      AND tcdt.HopDongChiTietREF NOT IN (   592604, 592606,        --hd treo tay
                                                            596562, 601831, 601832, 595650, 598615, 595994, 590510,
                                                            596005, 595126, 600839, 601640, 595499, 591302, 591318,
                                                            591519, 600215, 599472, 596825, 601959, 601833,
                                                            601456,                --pbo đã chạy xong
                                                            619385,                -- pbo đặc biệt, 1 banner gán vào 2 pbo
                                                            596942, 604294,        -- hd chạy programmatic ghi nhận qua mail
                                                            592062, 599473,        -- pbo chạy banner lõi
                                                            591037, 591038, 591039 --hd không ps thực chạy 2021
                                                        )
                      --and not (tcdt.DmSanPhamREF in (821,5133) and len(tcdt.DmBannerREF)=6)
                      AND NgayDanhSoHopDong >= '2020-07-20'
                      AND NgayThucHien <= @NgayThucHien
                      AND DotChayBooking <> 'HDBAN_INVENTORY'
                      AND DmLoaiNenTangREF <> 9 --khong check hd admatic programmatic
                --and HopDongChiTietREF =618239
                --and SoHopDong ='QC5180720' and DmSanPhamREF = 342
                --and NgayThucHien between @FromDate and @ToDate
                GROUP BY SoHopDong,
                         NgayDanhSoHopDong,
                         tcdt.HopDongChiTietREF,
                         hdct.ThanhTien,
                         hdct.IsKhuyenMai
            ) TCDT
                ON TC.SoHopDong = TCDT.SoHopDong
                   AND TC.HopDongChiTietREF = TCDT.HopDongChiTietREF
        WHERE 1 = 1
    -- isnull(TC.ThanhTienThucChayKM ,0) <> isnull(TCDT.tcdtkm,0)
    --or isnull(round(TCDT.tcdt - (case when isnull(TC.ThanhTienThucChaySauCK_ChuaVAT,0) < isnull(TCDT.ThanhTienHD,0) then isnull(ThanhTienThucChaySauCK_ChuaVAT,0) else  TCDT.ThanhTienHD end),0),0) <> 0
    ) c
    WHERE ABS(c.[LECH Da tinh - mm]) > 10
    ORDER BY c.[ThoiGianSuaHopDong] DESC; --, TC.HopDongChiTietREF
END;

```
