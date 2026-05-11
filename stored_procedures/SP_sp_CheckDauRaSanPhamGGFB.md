# Stored Procedure: `sp_CheckDauRaSanPhamGGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-12 10:24:57.653000
- **Ngày sửa cuối**: 2017-05-12 10:40:36.667000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_CheckDauRaSanPhamGGFB '2017-04-19'
CREATE PROCEDURE sp_CheckDauRaSanPhamGGFB
    @NgayThucHien DATETIME
AS
    BEGIN
        DELETE  FROM dbo.Check_ThongTinDauRaSanPham
        WHERE   IDLyDo = 28
                AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
        IF @NgayThucHien IS NULL
            SET @NgayThucHien = ( SELECT    MAX(NgayThucHien)
                                  FROM      dbo.ThucChayGGFBInput
                                )
 
        SELECT  hd.HopDongID ,
                tcg.SoHopDong ,
                sp.DmSanPhamID ,
                SUM(tcg.ThanhTienThucChay) ThanhTienThucTreo
        INTO    #ThucChayGGFB
        FROM    ThucChayGGFBInput tcg
                INNER JOIN dbo.HopDong hd ON hd.SoHopDong = tcg.SoHopDong
                LEFT JOIN dbo.DmSanPham sp ON tcg.DmSanPhamREF = sp.TenSanPham
        WHERE   tcg.NgayThucHien = @NgayThucHien
        GROUP BY hd.HopDongID ,
                tcg.SoHopDong ,
                sp.DmSanPhamID
        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  HopDongID ,
                  SoHopDong ,
                  DmSanPhamREF ,
                  TenSanPham ,
                  DmWebsiteREF_HD ,
                  TenWebsite_HD ,
                  DmWebsiteREF_TC ,
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
                        A.HopDongID ,
                        A.SoHopDong ,
                        A.DmSanPhamID ,
                        '' TenSanPham ,
                        A.DmWebsiteREF_HD ,
                        A.TenWebsite_HD ,
                        A.DmWebsiteREF ,
                        A.TenWebsite ,
                        A.ThanhTienThucChay ,
                        A.ThucChayTuTinh ,
                        A.GiaTriLech ,
                        B.ID ,
                        B.TenLoiChiTiet ,
                        A.TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        A.CreatedAt
                FROM    ( SELECT    @NgayThucHien NgayThucHien ,
                                    ISNULL(A.HopDongID, B.HopDongID) HopDongID ,
                                    ISNULL(A.SoHopDong, B.SoHopDong) SoHopDong ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamID) DmSanPhamID ,
                                    A.DmWebsiteREF DmWebsiteREF ,
                                    A.TenWebsite TenWebsite ,
                                    0 DmWebsiteREF_HD ,
                                    '' TenWebsite_HD ,
                                    ISNULL(A.ThanhTienThucChay, 0) ThanhTienThucChay ,
                                    ISNULL(B.ThanhTienThucTreo, 0) ThucChayTuTinh ,
                                    ISNULL(A.ThanhTienThucChay, 0)
                                    - ISNULL(B.ThanhTienThucTreo, 0) GiaTriLech ,
                                    28 IDLyDo ,
                                    0 TrangThaiXuLy ,
                                    GETDATE() CreatedAt
                          FROM      ( SELECT    tcdt.HopDongID ,
                                                tcdt.SoHopDong ,
                                                tcdt.DmSanPhamREF ,
                                                tcdt.DmWebsiteREF ,
                                                tcdt.TenWebsite ,
                                                SUM(tcdt.ThanhTienSauTrietKhauThucChay
                                                    + tcdt.GiaTriThayDoi) ThanhTienThucChay
                                      FROM      ThucChayDaTinh tcdt
                                                INNER JOIN #ThucChayGGFB gg ON gg.HopDongID = tcdt.HopDongID
                                                              AND gg.DmSanPhamID = tcdt.DmSanPhamREF
                                      WHERE     tcdt.DmSanPhamREF IN ( 423,
                                                              306, 535, 251 )
                                                AND tcdt.TrangThaiHopDong <> 3
                                                AND NOT ( tcdt.DmHinhThucQuangCao = 13
                                                          OR tcdt.DmLoaiBannerREF = 18
                                                        )
                                                AND tcdt.NgayThucHien <= @NgayThucHien
                                      GROUP BY  tcdt.HopDongID ,
                                                tcdt.SoHopDong ,
                                                tcdt.DmSanPhamREF ,
                                                tcdt.DmWebsiteREF ,
                                                tcdt.TenWebsite
                                    ) A
                                    FULL JOIN #ThucChayGGFB B ON B.HopDongID = A.HopDongID
                                                              AND B.DmSanPhamID = A.DmSanPhamREF
                          WHERE     NOT ( ISNULL(A.ThanhTienThucChay, 0) = 0
                                          AND ISNULL(B.ThanhTienThucTreo, 0) = 0
                                        )
                                    AND ISNULL(A.ThanhTienThucChay, 0) <> ISNULL(B.ThanhTienThucTreo,
                                                              0)
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
        DROP TABLE #ThucChayGGFB
    END

```
