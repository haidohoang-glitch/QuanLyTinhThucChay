# Stored Procedure: `Check_DauVaoSanPhamPerformentBase`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-01 16:27:07.547000
- **Ngày sửa cuối**: 2017-11-04 09:10:51.670000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Check_DauVaoSanPhamPerformentBase]
    @NgayThucHien DATETIME = '2017-11-02'
AS
    BEGIN
        DELETE  FROM dbo.Check_DuLieuDauVaoSanPham
        WHERE   IDLoai = 8
                AND CONVERT(DATE, GETDATE()) = CONVERT(DATE, CreatedAt)
        SELECT  *
        INTO    #ThucChay_HopDong
        FROM    ( 
-- Check bảng trả về theo hợp đồng
                  SELECT    NgayThucHien ,
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

        SELECT  *
        INTO    #ThucChay_NhanHang
        FROM    ( SELECT    NgayThucHien ,
                            username ,
                            DmSanPhamREF ,
                            CASE WHEN TenSanPham = 'adx' THEN 1
                                 WHEN TenSanPham = 'mobx' THEN 2
                                 WHEN TenSanPham = 'ecomx' THEN 3
                                 ELSE 0
                            END DmViTriREF ,
                            SUM(CONVERT(FLOAT, total_click)) total_click ,
                            SUM(CONVERT(FLOAT, total_view)) total_view ,
                            SUM(CONVERT(FLOAT, money)) money ,
                            SUM(CONVERT(FLOAT, promotion)) promotion
                  FROM      ThucChayAdmarket_ADX_CPC_NhanHang
                  WHERE     NgayThucHien = @NgayThucHien
                  GROUP BY  username ,
                            DmSanPhamREF ,
                            NgayThucHien ,
                            CASE WHEN TenSanPham = 'adx' THEN 1
                                 WHEN TenSanPham = 'mobx' THEN 2
                                 WHEN TenSanPham = 'ecomx' THEN 3
                                 ELSE 0
                            END
                  UNION ALL
                  SELECT    NgayThucHien ,
                            username ,
                            DmSanPhamREF ,
                            0 DmVitri ,
                            SUM(CONVERT(FLOAT, tt_click)) total_click ,
                            SUM(CONVERT(FLOAT, tt_view)) total_view ,
                            SUM(CONVERT(FLOAT, money)) money ,
                            SUM(CONVERT(FLOAT, promotion)) promotion
                  FROM      dbo.ThucChayAdmarket_ViewPlus_NhanHang
                  WHERE     NgayThucHien = @NgayThucHien
                  GROUP BY  username ,
                            DmSanPhamREF ,
                            NgayThucHien
                ) A

        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  UserName ,
                  DmSanPhamREF ,
                  DmViTriREF ,
                  TongClick ,
                  TongView ,
                  TongTien ,
                  TongKhuyenMai ,
                  TongClickTheoDomain ,
                  TongViewTheoDomain ,
                  TongTienTheoDomain ,
                  TongKhuyenMaiTheoDomain ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  CreatedAt
				 )
                SELECT  A.NgayThucHien ,
                        A.username ,
                        A.DmSanPhamREF ,
                        A.DmViTriREF ,
                        A.tt_click ,
                        A.tt_view ,
                        A.money ,
                        A.promotion ,
                        A.domain_tt_click ,
                        A.domain_tt_view ,
                        A.domain_tt_money ,
                        A.domain_tt_promotion ,
                        A.ID_LyDo ,
                        B.TenLoiChiTiet ,
                        0 TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        GETDATE()
                FROM    ( SELECT    * ,
                                    CASE WHEN A.tt_click <> A.domain_tt_click
                                         THEN 38
                                         WHEN A.tt_view <> A.domain_tt_view
                                         THEN 37
                                         WHEN A.money <> A.domain_tt_money
                                         THEN 39
                                         WHEN A.promotion <> A.domain_tt_promotion
                                         THEN 40
                                    END ID_LyDo
                          FROM      #ThucChay_HopDong A
                          WHERE     A.tt_click <> A.domain_tt_click
                                    OR A.tt_view <> A.domain_tt_view
                                    OR A.money <> A.domain_tt_money
                                    OR A.promotion <> A.domain_tt_promotion
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.ID_LyDo = B.ID

        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  UserName ,
                  DmSanPhamREF ,
                  DmViTriREF ,
                  TongClick ,
                  TongView ,
                  TongTien ,
                  TongKhuyenMai ,
                  TongClick_NhanHang ,
                  TongView_NhanHang ,
                  TongMoney_NhanHang ,
                  TongKhuyenMai_NhanHang ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  CreatedAt
				 )
                SELECT  A.NgayThucHien ,
                        A.username ,
                        A.DmSanPhamREF ,
                        A.DmViTriREF ,
                        A.tt_click ,
                        A.tt_view ,
                        A.money ,
                        A.promotion ,
                        A.total_click ,
                        A.total_view ,
                        A.total_money ,
                        A.total_promotion ,
                        A.ID_LyDo ,
                        B.TenLoiChiTiet ,
                        0 TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        GETDATE()
                FROM    ( SELECT    ISNULL(A.NgayThucHien, B.NgayThucHien) NgayThucHien ,
                                    ISNULL(A.username, B.username) username ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                                    ISNULL(A.DmViTriREF, B.DmViTriREF) DmViTriREF ,
                                    ISNULL(tt_click, 0) tt_click ,
                                    ISNULL(tt_view, 0) tt_view ,
                                    ISNULL(A.money, 0) money ,
                                    ISNULL(A.promotion, 0) promotion ,
                                    ISNULL(total_click, 0) total_click ,
                                    ISNULL(total_view, 0) total_view ,
                                    ISNULL(B.money, 0) total_money ,
                                    ISNULL(B.promotion, 0) total_promotion ,
                                    CASE WHEN ISNULL(tt_click, 0) <> ISNULL(total_click,
                                                              0) THEN 41
                                         WHEN ISNULL(tt_view, 0) <> ISNULL(total_view,
                                                              0) THEN 42
                                         WHEN ISNULL(A.money, 0) <> ISNULL(B.money,
                                                              0) THEN 43
                                         WHEN ISNULL(A.promotion, 0) <> ISNULL(B.promotion,
                                                              0) THEN 44
                                    END ID_LyDo
                          FROM      ( SELECT    NgayThucHien ,
                                                username ,
                                                DmSanPhamREF ,
                                                DmViTriREF ,
                                                SUM(tt_click) tt_click ,
                                                SUM(tt_view) tt_view ,
                                                SUM(money) money ,
                                                SUM(promotion) promotion
                                      FROM      #ThucChay_HopDong
                                      GROUP BY  NgayThucHien ,
                                                username ,
                                                DmSanPhamREF ,
                                                DmViTriREF
                                    ) A
                                    FULL JOIN #ThucChay_NhanHang B ON A.NgayThucHien = B.NgayThucHien
                                                              AND A.username = B.username
                                                              AND A.DmSanPhamREF = B.DmSanPhamREF
                                                              AND A.DmViTriREF = B.DmViTriREF
                          WHERE     ISNULL(tt_click, 0) <> ISNULL(total_click,
                                                              0)
                                    OR ISNULL(tt_view, 0) <> ISNULL(total_view,
                                                              0)
                                    OR ISNULL(A.money, 0) <> ISNULL(B.money, 0)
                                    OR ISNULL(A.promotion, 0) <> ISNULL(B.promotion,
                                                              0)
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.ID_LyDo = B.ID
				
				
--SELECT  *
--FROM    dbo.Check_DuLieuDauVaoSanPham
    END
	
```
