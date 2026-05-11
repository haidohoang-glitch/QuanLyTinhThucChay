# Stored Procedure: `sp_CheckDauRaSanPhamMuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-10 14:47:08.767000
- **Ngày sửa cuối**: 2017-05-10 14:47:19.540000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_CheckDauRaSanPhamMuaNgoai
    @NgayThucHien DATETIME = '2017-03-27 00:00:00.000'
AS
    BEGIN
        DELETE  FROM dbo.Check_ThongTinDauRaSanPham
        WHERE   IDLyDo = 27
                AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
        SELECT DISTINCT
                tcdt.HopDongID ,
                tcdt.HopDongChiTietREF
        INTO    #DsHopDongMuaNgoai
        FROM    ThucChayDaTinh tcdt
        WHERE   1 = 1
                AND tcdt.NgayThucHien = @NgayThucHien
                AND ( tcdt.DmHinhThucQuangCao = 13
                      OR tcdt.DmLoaiBannerREF = 18
                    )
                AND tcdt.TrangThaiHopDong <> 3
        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  HopDongID ,
                  HopDongChiTietID ,
                  SoHopDong ,
                  DmSanPhamREF ,
                  ThanhTienHD ,
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
                        A.HopDongChiTietID ,
                        A.SoHopDong ,
                        A.DmSanPhamREF ,
                        A.ThanhTienTuTinh ,
                        A.DsThucChay ,
                        A.ThanhTienTuTinh ,
                        A.GiaTriLech ,
                        A.ID_LyDo ,
                        B.TenLoiChiTiet ,
                        0 TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        GETDATE()
                FROM    ( SELECT    @NgayThucHien NgayThucHien ,
                                    ISNULL(A.HopDongFK, B.HopDongID) HopDongID ,
                                    ISNULL(A.HopDongChiTietID,
                                           A.HopDongChiTietID) HopDongChiTietID ,
                                    ISNULL(A.SoHopDong, B.SoHopDong) SoHopDong ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                                    ISNULL(A.ThanhTien, 0) ThanhTienTuTinh ,
                                    ISNULL(B.DsThucChay, 0) DsThucChay ,
                                    ISNULL(A.ThanhTien, 0)
                                    - ISNULL(B.DsThucChay, 0) GiaTriLech ,
                                    27 ID_LyDo
                          FROM      ( SELECT    hdct.HopDongFK ,
                                                hd.SoHopDong ,
                                                hdct.HopDongChiTietID ,
                                                hdct.DmSanPhamREF ,
                                                hdct.ThanhTien
                                      FROM      dbo.HopDongChiTiet hdct
                                                INNER JOIN #DsHopDongMuaNgoai mn ON hdct.HopDongChiTietID = mn.HopDongChiTietREF
                                                              AND hdct.HopDongFK = mn.HopDongID
                                                INNER JOIN dbo.HopDong hd ON hd.HopDongID = mn.HopDongID
                                    ) A
                                    FULL JOIN ( SELECT  tcdt.HopDongID ,
                                                        tcdt.SoHopDong ,
                                                        tcdt.HopDongChiTietREF ,
                                                        tcdt.DmSanPhamREF ,
                                                        SUM(tcdt.ThanhTienSauTrietKhauThucChay
                                                            + tcdt.GiaTriThayDoi) DsThucChay
                                                FROM    dbo.ThucChayDaTinh tcdt
                                                        INNER JOIN #DsHopDongMuaNgoai mn ON tcdt.HopDongChiTietREF = mn.HopDongChiTietREF
                                                              AND tcdt.HopDongID = mn.HopDongID
                                                GROUP BY tcdt.HopDongID ,
                                                        tcdt.HopDongChiTietREF ,
                                                        tcdt.DmSanPhamREF ,
                                                        tcdt.SoHopDong
                                              ) B ON B.DmSanPhamREF = A.DmSanPhamREF
                                                     AND A.HopDongChiTietID = B.HopDongChiTietREF
                                                     AND A.HopDongFK = B.HopDongID
                          WHERE     ROUND(ISNULL(B.DsThucChay, 0)
                                          - ISNULL(ThanhTien, 0), -1) <> 0
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.ID_LyDo = B.ID
		--SELECT * FROM dbo.HopDongChiTiet WHERE HopDongFK=44598
        DROP TABLE #DsHopDongMuaNgoai
    END


--SELECT * FROM dbo.Check_ThongTinDauRaSanPham
```
