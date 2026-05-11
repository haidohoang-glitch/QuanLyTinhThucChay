# Stored Procedure: `sp_KSTC_CheckTCDT_ThucTreoChiPhi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-07-31 15:13:03.327000
- **Ngày sửa cuối**: 2024-12-06 16:22:39.783000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC sp_KSTC_CheckTCDT_ThucTreoChiPhi '2021-06-02',817
--817
--0: all không bao gồm ggfb
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_ThucTreoChiPhi]
    -- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME,
    @DmSanPhamREF INT
AS
BEGIN
    EXEC CheckThucChayVuotHopDong_TableTCDT @NgayThucHien, @NgayThucHien;
    IF @DmSanPhamREF = 817
    BEGIN
        SELECT A.*,
               (A.ThanhTien - A.tt) LechTTTT,
               B.*
        FROM
        (
            SELECT hd.SoHopDong shd,
                   tchdctp.HopDongREF,
                   tchdctp.HopDongChiTietREF,
                   hdct.TenLoai TenHTQC,
                   hdct.DmSanPhamREF,
                   hdct.TenSanPham,
                   hdct.ThanhTien,
                   SUM(tchdctp.SoLuongThucTreo * tchdctp.DonGia * (1 - tchdctp.ChietKhau / 100)) tt
            FROM ThucChayHopDongChiTiet tchdctp
                INNER JOIN HopDongChiTiet hdct
                    ON tchdctp.HopDongChiTietREF = hdct.HopDongChiTietID --and 	tchdctp.DmSanPhamREF = hdct.DmSanPhamREF						
                INNER JOIN HopDong hd
                    ON hd.HopDongID = tchdctp.HopDongREF
            WHERE 1 = 1
                  AND HopDongChiTietREF NOT IN ( 557703 --hd 2019, k xử lý nữa, thiếu 200vnd)
								
                                               )
				  AND tchdctp.TrangThaiTreo=2 -- trạng thái được tính tc ngày 20241206
                  AND tchdctp.DeletedStatus <> 1
                  AND hdct.DeletedStatus <> 1
                  AND NOT (
                              hdct.DmLoaiREF = 13
                              OR hdct.DmLoaiBannerREF = 18
                          )
                  AND TrangThaiHopDong <> 3
                  --AND Nam =@Nam
                  AND Nam >= 2018
                  AND hdct.ThanhTien <> 0
                  AND hdct.DmSanPhamREF = 817
                  AND CONVERT(DATE, tchdctp.LastModifiedAt) <= @NgayThucHien
                  AND NOT EXISTS
            (
                SELECT TOP (1)
                       HopDongChiTietREF
                FROM DmThongTinHopDongBanInventory inv
                WHERE inv.HopDongChiTietREF = hdct.HopDongChiTietID
                ORDER BY inv.HopDongChiTietREF
            )
            --and isnull(hdct.DmLoaiNenTangREF,0) <> 9--khong xet case inventory
            GROUP BY hd.SoHopDong,
                     tchdctp.HopDongREF,
                     tchdctp.HopDongChiTietREF,
                     hdct.TenLoai,
                     hdct.DmSanPhamREF,
                     hdct.TenSanPham,
                     hdct.ThanhTien
            HAVING SUM(tchdctp.SoLuongThucTreo * tchdctp.DonGia * (1 - tchdctp.ChietKhau / 100)) <> 0
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       tcdt.HopDongChiTietID,
                       tcdt.DmSanPhamREF,
                       SUM(tcdt.ThanhTienThucChay) ThanhTienThucChay
                FROM KS_ThucChay_TCDT tcdt
                    LEFT JOIN HopDongChiTiet hdct
                        ON tcdt.HopDongChiTietID = hdct.HopDongChiTietID
                --left join ThucChayHopDongChiTiet tc on tcdt.HopDongChiTietID = tc.HopDongChiTietREF
                WHERE 1 = 1
                      AND tcdt.HopDongChiTietID NOT IN ( 557703,557233 --hd 2019, k xử lý nữa, thiếu 200vnd
						
                                                       )
                      AND Nam >= 2018
                      --and isnull(hdct.DmLoaiNenTangREF,0) <> 9--khong xet case inventory
                      AND NOT (
                                  DmHinhThucQuangCao = 13
                                  OR tcdt.DmLoaiBannerREF = 18
                              )
                      AND tcdt.DmSanPhamREF = 817
                      AND NOT EXISTS
                (
                    SELECT TOP (1)
                           HopDongChiTietREF
                    FROM DmThongTinHopDongBanInventory inv
                    WHERE inv.HopDongChiTietREF = tcdt.HopDongChiTietID
                    ORDER BY inv.HopDongChiTietREF
                )
                GROUP BY SoHopDong,
                         HopDongID,
                         tcdt.HopDongChiTietID,
                         tcdt.DmSanPhamREF
                HAVING ROUND(SUM(tcdt.ThanhTienThucChay), 0) <> 0
            ) B
                ON A.HopDongChiTietREF = B.HopDongChiTietID
                   AND A.DmSanPhamREF = B.DmSanPhamREF
        WHERE NOT (
                      (
                          ROUND(A.tt, 0) >= ROUND(A.ThanhTien, 0)
                          AND ROUND(A.ThanhTien, 0) = ROUND(B.ThanhTienThucChay, 0)
                      )
                      OR
                      (
                          ROUND(A.tt, 0) < ROUND(A.ThanhTien, 0)
                          AND ROUND(A.tt, 0) = ROUND(B.ThanhTienThucChay, 0)
                      )
                  )
              OR A.HopDongChiTietREF IS NULL
              OR B.HopDongChiTietID IS NULL
              OR A.DmSanPhamREF IS NULL
              OR B.DmSanPhamREF IS NULL
        ORDER BY A.HopDongREF DESC;

    END;
    ELSE IF @DmSanPhamREF = 0
    BEGIN
        PRINT 'chiphi';
        SELECT A.shd,
               A.HopDongREF,
               A.HopDongChiTietREF,
               A.TenHTQC,
               A.DmSanPhamREF,
               A.TenSanPham,		
               dbo.FormatNumber(A.ThanhTien) ThanhTien,
               dbo.FormatNumber(A.tt) tt,
               (A.ThanhTien - A.tt) lechTTTT,
               B.SoHopDong TCDT_SoHopDong,
               B.HopDongID TCDT_HopdongID,
               B.HopDongChiTietREF TCDT_HopDongChiTietREF,
               B.DmSanPhamREF TCDT_DmSanPhamREF,		
               dbo.FormatNumber(B.ThanhTienThucChay) ThanhTienThucChayDT
        FROM
        (
            SELECT hd.SoHopDong shd,
                   tchdctp.HopDongREF,
                   tchdctp.HopDongChiTietREF,
                   hdct.TenLoai TenHTQC,
                   hdct.DmSanPhamREF,
                   hdct.TenSanPham,				   
                   hdct.ThanhTien,
                   (SUM(tchdctp.SoLuongThucTreo * tchdctp.DonGia * (1 - tchdctp.ChietKhau / 100))) tt
            FROM ThucChayHopDongChiTiet tchdctp
                INNER JOIN HopDongChiTiet hdct
                    ON tchdctp.HopDongChiTietREF = hdct.HopDongChiTietID --and 	tchdctp.DmSanPhamREF = hdct.DmSanPhamREF						
                INNER JOIN HopDong hd
                    ON hd.HopDongID = tchdctp.HopDongREF
            WHERE 1 = 1
                  AND tchdctp.HopDongChiTietREF NOT IN ( 574648,538235,557233 -- pbo từ 2018, k check nữa
														,689901 -- hđ thặng dư giải pháp đã đủ TC
														,660869,654498,654499,654500--hd Ceator content vượt có CF 
														,687215-- thang du giai phap du TC
														,550963-- cf đủ thực chạy 
                                                       )
				   AND tchdctp.TrangThaiTreo=2 -- Trạng thái được tính thực chạy 
                  AND tchdctp.DeletedStatus <> 1
                  AND hdct.DeletedStatus <> 1
                  AND NOT (
                              hdct.DmLoaiREF = 13
                              OR hdct.DmLoaiBannerREF = 18
                          )
                  AND TrangThaiHopDong <> 3
                  AND Nam >= 2018
                  AND hdct.ThanhTien <> 0
                  --AND ( hdct.DmSanPhamREF NOT IN (141,140,585,549,240,339,370,342,613,144,375,628,598,228,381,241,228,385,733,735,564,720,722,680,821,637,305,5133,5056,5007,5005,817) OR ( hdct.DmSanPhamREF = 5082 AND hdct.DmLoaiREF= 5 ) )
                  AND hdct.DmSanPhamREF NOT IN ( 141, 140, 585, 549, 240, 339, 370, 342, 613, 144, 375, 628, 598, 228,
                                                 381, 241, 228, 385, 733, 735, 564, 720, 722, 680, 821, 637, 305, 5133,
                                                 5056, 5007, 5005, 817, 5082, 5312, 5268
                                               )
                  AND NOT (
                              hdct.DmSanPhamREF = 5082
                              AND hdct.DmLoaiREF = 5
                          )
                  AND NOT (
                              hdct.DmSanPhamREF IN ( 423, 306,5188 )
                              OR hdct.DmViTriREF IN ( 100093, 100478,100774 )
                          )
                  AND CONVERT(DATE, tchdctp.LastModifiedAt) <= @NgayThucHien
                  AND NOT EXISTS
            (
                SELECT TOP (1)
                       HopDongChiTietREF
                FROM DmThongTinHopDongBanInventory inv
                WHERE inv.HopDongChiTietREF = hdct.HopDongChiTietID
                ORDER BY inv.HopDongChiTietREF
            )
            GROUP BY hd.SoHopDong,
                     tchdctp.HopDongREF,
                     tchdctp.HopDongChiTietREF,
                     hdct.TenLoai,
                     hdct.DmSanPhamREF,
                     hdct.TenSanPham,		
                     hdct.ThanhTien
            HAVING SUM(tchdctp.SoLuongThucTreo * tchdctp.DonGia * (1 - tchdctp.ChietKhau / 100)) <> 0
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       HopDongChiTietREF,
                       tcdt.DmSanPhamREF,			
                       SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) ThanhTienThucChay
                FROM ThucChayDaTinh tcdt
                WHERE 1 = 1
                      AND tcdt.HopDongChiTietREF NOT IN ( 574648, 538235,557233 -- pbo từ 2018, k check nữa
					  	                                 ,660869,654498,654499,654500--hd Ceator content vượt có CF 
														 ,687215-- thang du giai phap du TC
														 ,550963-- cf đủ thực chạy 
                                                        )
                      AND Nam >= 2018
                      AND NgayThucHien <= @NgayThucHien
                      AND NOT (
                                  DmHinhThucQuangCao = 13
                                  OR DmLoaiBannerREF = 18
                              )
                      AND tcdt.DmSanPhamREF NOT IN ( 141, 140, 585, 549, 240, 339, 370, 342, 613, 144, 375, 628, 598,
                                                     228, 381, 241, 228, 385, 733, 735, 564, 720, 722, 680, 821, 637,
                                                     305, 5133, 5056, 5007, 5005, 817, 5082, 5312, 5268
                                                   )
                      --AND (tcdt.DmSanPhamREF NOT IN (141,140,585,549,240,339,370,342,613,144,375,628,598,228,381,241,228,385,733,735,564,720,722,680,821,637,305,5133,5056,5007,5005,817) OR (tcdt.DmSanPhamREF=5082 AND tcdt.DmHinhThucQuangCao= 5 ))
                      AND NOT (
                                  tcdt.DmSanPhamREF = 5082
                                  AND tcdt.DmHinhThucQuangCao = 5
                              )
                      AND tcdt.DmChienDichREF <> 3 --dấu hiệu ghi nhận thặng dư giải pháp team Performance, không ghi nhận theo hình thức chi phí
                      AND NOT (
                                  tcdt.DmSanPhamREF IN ( 423, 306,5188 )
                                  OR tcdt.DmViTriREF IN ( 100093, 100478,100774 )
                              )
                      AND DotChayHopDong NOT IN ( 'ThanhTien_GGFB', 'ThanhTien_GGFB_Chot' )
                      AND SUBSTRING(DotChayHopDong, 10, 1) <> ':'
                      AND NOT EXISTS
                (
                    SELECT TOP (1)
                           HopDongChiTietREF
                    FROM DmThongTinHopDongBanInventory inv
                    WHERE inv.HopDongChiTietREF = tcdt.HopDongChiTietREF
                    ORDER BY inv.HopDongChiTietREF
                )
                GROUP BY SoHopDong,
                         HopDongID,
                         HopDongChiTietREF,
                         tcdt.DmSanPhamREF		
                HAVING ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) <> 0
            ) B
                ON A.HopDongChiTietREF = B.HopDongChiTietREF
                   AND A.DmSanPhamREF = B.DmSanPhamREF
        WHERE NOT (
                      (
                          ROUND(A.tt, 0) >= ROUND(A.ThanhTien, 0)
                          AND ROUND(A.ThanhTien, 0) = ROUND(B.ThanhTienThucChay, 0)
                      )
                      OR
                      (
                          ROUND(A.tt, 0) < ROUND(A.ThanhTien, 0)
                          AND ROUND(A.tt, 0) = ROUND(B.ThanhTienThucChay, 0)
                      )
                  )
              OR A.HopDongChiTietREF IS NULL
              OR B.HopDongChiTietREF IS NULL
              OR A.DmSanPhamREF IS NULL
              OR B.DmSanPhamREF IS NULL
        ORDER BY A.HopDongREF DESC;
    END;

END;



```
