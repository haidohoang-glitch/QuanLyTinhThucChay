# Stored Procedure: `Check_DauRaSanPhamPerformentBase`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-07 15:37:23.517000
- **Ngày sửa cuối**: 2017-06-07 16:16:49.720000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE Check_DauRaSanPhamPerformentBase
    @NgayThucHien DATETIME = '2017-05-31'
AS
    BEGIN
        


        DELETE  FROM dbo.Check_ThongTinDauRaSanPham
        WHERE   IDLoai = 8
                AND IDLyDo IN ( 45, 46 )
                AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
-- Lấy danh sách cách user trả về đúng dữ liệu trong ngày

        SELECT DISTINCT
                A.NgayThucHien ,
                A.username ,
                A.DmSanPhamREF ,
                A.DmViTriREF
        INTO    #ThucChayOk
        FROM    ( SELECT    NgayThucHien ,
                            username ,
                            DmSanPhamREF ,
                            DmViTriREF ,
                            CONVERT(FLOAT, tt_click) tt_click ,
                            CONVERT(FLOAT, tt_view) tt_view ,
                            CONVERT(FLOAT, money) money ,
                            CONVERT(FLOAT, promotion) promotion ,
                            SUM(CONVERT(FLOAT, domain_tt_click)) domain_tt_click ,
                            SUM(CONVERT(FLOAT, domain_tt_view)) domain_tt_view ,
                            SUM(CONVERT(FLOAT, domain_tt_money)) domain_tt_money ,
                            SUM(CONVERT(FLOAT, domain_tt_promotion)) domain_tt_promotion
                  FROM      ThucChayAdmarket_ADX_CPC_HopDong
                  WHERE     NgayThucHien = @NgayThucHien
                  GROUP BY  username ,
                            DmSanPhamREF ,
                            tt_click ,
                            tt_view ,
                            money ,
                            promotion ,
                            NgayThucHien ,
                            DmViTriREF
                  UNION ALL
                  SELECT    NgayThucHien ,
                            username ,
                            DmSanPhamREF ,
                            0 DmViTri ,
                            CONVERT(FLOAT, tt_click) tt_click ,
                            CONVERT(FLOAT, tt_view) tt_view ,
                            CONVERT(FLOAT, money) money ,
                            CONVERT(FLOAT, promotion) promotion ,
                            SUM(CONVERT(FLOAT, domain_tt_click)) domain_tt_click ,
                            SUM(CONVERT(FLOAT, domain_tt_view)) domain_tt_view ,
                            SUM(CONVERT(FLOAT, domain_money)) domain_tt_money ,
                            SUM(CONVERT(FLOAT, domain_promotion)) domain_tt_promotion
                  FROM      ThucChayAdmarket_ViewPlus_HopDong
                  WHERE     NgayThucHien = @NgayThucHien
                  GROUP BY  username ,
                            DmSanPhamREF ,
                            tt_click ,
                            tt_view ,
                            money ,
                            promotion ,
                            NgayThucHien
                ) A
        WHERE   NOT ( A.tt_click <> A.domain_tt_click
                      OR A.tt_view <> A.domain_tt_view
                      OR A.money <> A.domain_tt_money
                      OR A.promotion <> A.domain_tt_promotion
                    ) 

-- Lấy theo chiều chi tiết domain với các tài khoản trả về đúng dữ liệu
        SELECT  A.*
        INTO    #ThucChayTrongNgay
        FROM    ( SELECT    NgayThucHien ,
                            username ,
                            contract_number ,
                            DmSanPhamREF ,
                            DmViTriREF ,
                            domain_name ,
                            SUM(CONVERT(FLOAT, domain_tt_click)) domain_tt_click ,
                            SUM(CONVERT(FLOAT, domain_tt_view)) domain_tt_view ,
                            SUM(CONVERT(FLOAT, domain_tt_money)) domain_tt_money ,
                            SUM(CONVERT(FLOAT, domain_tt_promotion)) domain_tt_promotion
                  FROM      ThucChayAdmarket_ADX_CPC_HopDong
                  WHERE     NgayThucHien = @NgayThucHien
                  GROUP BY  username ,
                            DmSanPhamREF ,
                            NgayThucHien ,
                            domain_name ,
                            contract_number ,
                            DmViTriREF
                  UNION ALL
                  SELECT    NgayThucHien ,
                            username ,
                            contract_number ,
                            DmSanPhamREF ,
                            0 DmViTriREF ,
                            domain_name ,
                            SUM(CONVERT(FLOAT, domain_tt_click)) domain_tt_click ,
                            SUM(CONVERT(FLOAT, domain_tt_view)) domain_tt_view ,
                            SUM(CONVERT(FLOAT, domain_money)) domain_tt_money ,
                            SUM(CONVERT(FLOAT, domain_promotion)) domain_tt_promotion
                  FROM      ThucChayAdmarket_ViewPlus_HopDong
                  WHERE     NgayThucHien = @NgayThucHien
                  GROUP BY  username ,
                            DmSanPhamREF ,
                            NgayThucHien ,
                            domain_name ,
                            contract_number
                ) A
                INNER JOIN #ThucChayOk B ON A.NgayThucHien = B.NgayThucHien
                                            AND A.username = B.username
                                            AND A.DmSanPhamREF = B.DmSanPhamREF
                                            AND A.DmViTriREF = B.DmViTriREF
-- Lấy danh sách những hợp đồng chạy admarket

        SELECT DISTINCT
                hd.SoHopDong ,
                hdct.DmSanPhamREF ,
                hdct.TK_AdMarket
        INTO    #HopDongChayAdmarket
        FROM    dbo.HopDong hd
                INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
        WHERE   hdct.DmSanPhamREF IN ( 144, 585, 628 )
                AND hd.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
                AND hd.TrangThaiHopDong <> 3
                AND hd.DmMaHopDongREF NOT IN ( 136, 310, 345, 533 )
                AND hd.NgayDanhSoHopDong >= '2015-01-01'


        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  DmSanPhamREF ,
                  TenSanPham ,
                  TenWebsite_TC ,
                  ThanhTienThucChay ,
                  TienThucChayTuTinh ,
                  GiaTriLech ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  CreatedAt 
                )
                SELECT  A.NgayThucHien ,
                        A.DmSanPhamREF ,
                        TenSanPham ,
                        A.TenWebsite ,
                        A.ThucChayDaTinh ,
                        A.ThucChayTuTinh ,
                        ThanhTienLech ,
                        A.ID_LyDo ,
                        B.TenLoiChiTiet ,
                        A.TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        GETDATE()
                FROM    ( SELECT    ISNULL(B.NgayThucHien, A.NgayThucHien) NgayThucHien ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                                    ISNULL(domain_name, B.TenWebsite) TenWebsite ,
                                    ISNULL(domain_tt_money, 0) ThucChayTuTinh ,
                                    ISNULL(B.ThanhTienSauTrietKhauThucChay, 0) ThucChayDaTinh ,
                                    ISNULL(domain_tt_money, 0)
                                    - ISNULL(B.ThanhTienSauTrietKhauThucChay,
                                             0) ThanhTienLech ,
                                    45 ID_LyDo ,
                                    0 TrangThaiXuLy
                          FROM      ( SELECT    NgayThucHien ,
                                                DmSanPhamREF ,
                                                domain_name ,
                                                SUM(CONVERT(FLOAT, domain_tt_money)) domain_tt_money
                                      FROM      #ThucChayTrongNgay A
--WHERE   DmSanPhamREF = 144
GROUP BY                                        NgayThucHien ,
                                                DmSanPhamREF ,
                                                domain_name
                                      HAVING    SUM(domain_tt_money) <> 0
                                    ) A
                                    FULL JOIN ( SELECT  tcdt.NgayThucHien ,
                                                        tcdt.DmSanPhamREF ,
                                                        tcdt.TenWebsite ,
                                                        SUM(tcdt.ThanhTienSauTrietKhauThucChay)
                                                        * 1.1 ThanhTienSauTrietKhauThucChay
                                                FROM    dbo.ThucChayDaTinh tcdt
                                                WHERE   tcdt.DmSanPhamREF IN (
                                                        144, 585, 628 )
                                                        AND DmMaHopDongREF NOT IN (
                                                        136, 310, 345, 533 )
                                                        AND NgayThucHien = @NgayThucHien
        --AND tcdt.DmSanPhamREF = 144
GROUP BY                                                tcdt.NgayThucHien ,
                                                        tcdt.DmSanPhamREF ,
                                                        tcdt.TenSanPham ,
                                                        tcdt.TenWebsite
                                                HAVING  SUM(tcdt.ThanhTienSauTrietKhauThucChay) <> 0
                                              ) B ON A.NgayThucHien = B.NgayThucHien
                                                     AND A.DmSanPhamREF = B.DmSanPhamREF
                                                     AND domain_name = B.TenWebsite
                          WHERE     ABS(ISNULL(domain_tt_money, 0)
                                        - ISNULL(B.ThanhTienSauTrietKhauThucChay,
                                                 0)) > 10
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.ID_LyDo = B.ID
                        LEFT JOIN dbo.DmSanPham dms ON A.DmSanPhamREF = dms.DmSanPhamID


        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  username ,
                  HopDongID ,
                  SoHopDong ,
                  DmSanPhamREF ,
                  TenSanPham ,
                  ThanhTienThucChay ,
                  TienThucChayTuTinh ,
                  GiaTriLech ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  CreatedAt 
						
                )
                SELECT  A.NgayThucHien ,
                        A.username ,
                        ISNULL(hd.HopDongID, 0) HopDongID ,
                        A.SoHopDong ,
                        A.DmSanPhamREF ,
                        TenSanPham ,
                        A.ThucChayDaTinh ,
                        A.ThanhTienTuTinh ,
                        A.ThanhTienLech ,
                        A.ID_LyDo ,
                        B.TenLoiChiTiet ,
                        A.TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        GETDATE()
                FROM    ( SELECT    ISNULL(A.NgayThucHien, B.NgayThucHien) NgayThucHien ,
                                    ISNULL(A.username, B.TK_AdMarket) username ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                                    ISNULL(A.contract_number, B.SoHopDong) SoHopDong ,
                                    ISNULL(A.ThanhTienTuTinh, 0) ThanhTienTuTinh ,
                                    ISNULL(B.ThanhTienSauTrietKhauThucChay, 0) ThucChayDaTinh ,
                                    ISNULL(A.ThanhTienTuTinh, 0)
                                    - ISNULL(B.ThanhTienSauTrietKhauThucChay,
                                             0) ThanhTienLech ,
                                    46 ID_LyDo ,
                                    0 TrangThaiXuLy
                          FROM      ( SELECT    NgayThucHien ,
                                                username ,
                                                contract_number ,
                                                DmSanPhamREF ,
                                                SUM(domain_tt_money) ThanhTienTuTinh
                                      FROM      #ThucChayTrongNgay
                                      WHERE     contract_number <> ''
                                      GROUP BY  NgayThucHien ,
                                                username ,
                                                contract_number ,
                                                DmSanPhamREF
                                      HAVING    SUM(domain_tt_money) <> 0
                                      UNION
                                      SELECT    NgayThucHien ,
                                                '' username ,
                                                '-' contract_number ,
                                                DmSanPhamREF ,
                                                SUM(domain_tt_money) ThanhTienTuTinh
                                      FROM      #ThucChayTrongNgay
                                      WHERE     contract_number <> ''
                                      GROUP BY  NgayThucHien ,
                                                DmSanPhamREF
                                      HAVING    SUM(domain_tt_money) <> 0
                                    ) A
                                    FULL JOIN ( SELECT  tcdt.NgayThucHien ,
                                                        ISNULL(hd.TK_AdMarket,
                                                              '') TK_AdMarket ,
                                                        tcdt.DmSanPhamREF ,
                                                        tcdt.SoHopDong ,
                                                        SUM(CASE
                                                              WHEN tcdt.SoHopDong = '-'
                                                              THEN tcdt.GiaTriThayDoi
                                                              ELSE tcdt.ThanhTienSauTrietKhauThucChay
                                                            END) * 1.1 ThanhTienSauTrietKhauThucChay
                                                FROM    dbo.ThucChayDaTinhAdmarket tcdt
                                                        LEFT JOIN #HopDongChayAdmarket hd ON hd.DmSanPhamREF = tcdt.DmSanPhamREF
                                                              AND hd.SoHopDong = tcdt.SoHopDong
                                                WHERE   tcdt.DmSanPhamREF IN (
                                                        144, 585, 628 )
                                                        AND DmMaHopDongREF NOT IN (
                                                        136, 310, 345, 533 )
                                                        AND NgayThucHien = @NgayThucHien
        --AND tcdt.ThucChayDaTinhID = '86D00404-4589-45F7-890A-77DA25915B7A'
                                                GROUP BY tcdt.NgayThucHien ,
                                                        hd.TK_AdMarket ,
                                                        tcdt.DmSanPhamREF ,
                                                        tcdt.SoHopDong
                                                HAVING  SUM(CASE
                                                              WHEN tcdt.SoHopDong = '-'
                                                              THEN tcdt.GiaTriThayDoi
                                                              ELSE tcdt.ThanhTienSauTrietKhauThucChay
                                                            END) <> 0
                                              ) B ON B.DmSanPhamREF = A.DmSanPhamREF
                                                     AND B.NgayThucHien = A.NgayThucHien
                                                     AND A.contract_number = B.SoHopDong
                          WHERE     ABS(ISNULL(A.ThanhTienTuTinh, 0)
                                        - ISNULL(B.ThanhTienSauTrietKhauThucChay,
                                                 0)) > 10
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.ID_LyDo = B.ID
                        LEFT JOIN dbo.DmSanPham dms ON A.DmSanPhamREF = dms.DmSanPhamID
                        LEFT JOIN dbo.HopDong hd ON A.SoHopDong = hd.SoHopDong

       
   


     
    END

--EXEC	Check_DauRaSanPhamPerformentBase
```
