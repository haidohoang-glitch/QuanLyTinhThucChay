# Stored Procedure: `sp_CheckDauRaSanPhamPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-09 14:20:41.570000
- **Ngày sửa cuối**: 2017-05-25 09:42:07.570000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--SELECT * FROM dbo.ThucChayHopDongChiTietPR WHERE HopDongREF=500758
--sp_CheckDauRaSanPhamPR '2017-05-23'
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamPR]
    @NgayThucHien DATETIME
AS
    BEGIN
        DELETE  FROM dbo.Check_ThongTinDauRaSanPham
        WHERE   IDLyDo = 26
                AND CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
        SELECT  pr.HopDongREF ,
                hd.SoHopDong ,
                pr.DmSanPhamREF ,
                pr.DmNhanHangREF ,
                pr.DmHinhThucQuangCaoREF ,
                pr.DmWebsiteREF ,
                pr.ChietKhau ,
                pr.GiaTien ,
                pr.ThoiGianBatDau ,
                pr.CreatedAt ,
                pr.LastModifiedAt
        INTO    #HDPhatSinhThucChay
        FROM    dbo.ThucChayHopDongChiTietPR pr
                INNER JOIN dbo.HopDong hd ON hd.HopDongID = pr.HopDongREF
        WHERE   CONVERT(DATE, pr.LastModifiedAt) = @NgayThucHien
                AND DmSanPhamREF IN ( 141, 637, 305 )
                AND hd.DeletedStatus = 0
                AND pr.DeletedStatus = 0
                AND hd.TrangThaiHopDong <> 3
		--AND pr.HopDongREF=501281

        SELECT  pr.HopDongREF ,
                hd.SoHopDong ,
                pr.DmSanPhamREF ,
                pr.DmHinhThucQuangCaoREF ,
                ISNULL(map.DmWebsiteReportingdbID, pr.DmWebsiteREF) DmWebsiteREF ,
                pr.TenWebsite ,
                pr.ChietKhau ,
                SUM(CONVERT(FLOAT, GiaTien * SoLuong) * ( 100 - ChietKhau )
                    / 100) ThanhTien
        INTO    #TempThucTreoPR
        FROM    dbo.ThucChayHopDongChiTietPR pr
                INNER JOIN ( SELECT DISTINCT
                                    HopDongREF
                             FROM   #HDPhatSinhThucChay
                           ) hdps ON hdps.HopDongREF = pr.HopDongREF
                INNER JOIN dbo.HopDong hd ON hd.HopDongID = pr.HopDongREF
                LEFT JOIN WebsiteMapping_HDCN_Reporting map ON pr.DmWebsiteREF = map.DmWebsiteID
        WHERE   DmSanPhamREF IN ( 141, 637, 305 )
                AND pr.DmHinhThucQuangCaoREF NOT IN ( 13, 42 )
                AND hd.DeletedStatus = 0
                AND pr.DeletedStatus = 0
                AND hd.TrangThaiHopDong <> 3
                AND CONVERT(DATE, pr.CreatedAt) <= @NgayThucHien
        --AND hd.HopDongID = 500758
GROUP BY        pr.HopDongREF ,
                hd.SoHopDong ,
                pr.DmSanPhamREF ,
                pr.DmHinhThucQuangCaoREF ,
                pr.ChietKhau ,
                pr.TenWebsite ,
                ISNULL(map.DmWebsiteReportingdbID, pr.DmWebsiteREF) 
       



        SELECT  tcdt.HopDongID ,
                tcdt.SoHopDong ,
                tcdt.DmSanPhamREF ,
                tcdt.DmHinhThucQuangCao DmHinhThucQuangCaoREF ,
                tcdt.DmWebsiteREF ,
                tcdt.TenWebsite ,
                tcdt.ChietKhau ,
                SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) DsThucChay
        INTO    #TempThucChayPR
        FROM    dbo.ThucChayDaTinh tcdt
                INNER JOIN ( SELECT DISTINCT
                                    HopDongREF
                             FROM   #HDPhatSinhThucChay
                           ) hd ON hd.HopDongREF = tcdt.HopDongID
        WHERE   DmSanPhamREF IN ( 141, 637, 305 )
                AND ( tcdt.DmHinhThucQuangCao NOT IN ( 13, 42 )
                      OR tcdt.DmLoaiBannerREF <> 18
                    )
                AND tcdt.TrangThaiHopDong <> 3
                AND tcdt.NgayThucHien <= @NgayThucHien
        GROUP BY tcdt.HopDongID ,
                tcdt.DmSanPhamREF ,
                tcdt.DmHinhThucQuangCao ,
                tcdt.DmWebsiteREF ,
                tcdt.ChietKhau ,
                tcdt.TenWebsite ,
                tcdt.SoHopDong 


        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  HopDongID ,
                  SoHopDong ,
                  DmSanPhamREF ,
                  DmWebsiteREF_HD ,
                  TenWebsite_HD ,
                  DmWebsiteREF_TC ,
                  TenWebsite_TC ,
                  ThanhTienThucChay ,
                  TienThucChayTuTinh ,
                  GiaTriLech ,
                  GhiChu ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  CreatedAt ,
                  DmHinhThucQuangCaoREF
                )
                SELECT  NgayThucHien ,
                        HopDongREF ,
                        SoHopDong ,
                        DmSanPhamREF ,
                        DmWebsiteREF_HD ,
                        TenWebsite_HD ,
                        DmWebsiteREF_TC ,
                        TenWebsite_TC ,
                        DsThucChay ,
                        ThanhTien ,
                        GiaTriLech ,
                        '' ,
                        IDLyDo ,
                        TenLoiChiTiet ,
                        0 ,
                        ID_Loai ,
                        TenLoai ,
                        GETDATE() ,
                        DmHinhThucQuangCaoREF
                FROM    ( SELECT    @NgayThucHien NgayThucHien ,
                                    ISNULL(A.HopDongREF, B.HopDongID) HopDongREF ,
                                    ISNULL(A.SoHopDong, B.SoHopDong) SoHopDong ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                                    ISNULL(A.DmWebsiteREF, 0) DmWebsiteREF_HD ,
                                    ISNULL(A.TenWebsite, '') TenWebsite_HD ,
                                    ISNULL(B.DmWebsiteREF, 0) DmWebsiteREF_TC ,
                                    ISNULL(B.TenWebsite, '') TenWebsite_TC ,
                                    ISNULL(B.DsThucChay, 0) DsThucChay ,
                                    ISNULL(A.ThanhTien, 0) ThanhTien ,
                                    ISNULL(B.DsThucChay, 0)
                                    - ISNULL(A.ThanhTien, 0) GiaTriLech ,
                                    ISNULL(A.DmHinhThucQuangCaoREF,
                                           B.DmHinhThucQuangCaoREF) DmHinhThucQuangCaoREF ,
                                    26 IDLyDo
                          FROM      ( SELECT    t.HopDongREF ,
                                                t.SoHopDong ,
                                                t.DmSanPhamREF ,
                                                t.DmHinhThucQuangCaoREF ,
                                                t.DmWebsiteREF ,
                                                t.TenWebsite ,
                                                SUM(t.ThanhTien) ThanhTien
                                      FROM      #TempThucTreoPR t
                                      GROUP BY  t.HopDongREF ,
                                                t.SoHopDong ,
                                                t.DmSanPhamREF ,
                                                t.DmHinhThucQuangCaoREF ,
                                                t.DmWebsiteREF ,
                                                t.TenWebsite
                                    ) A
                                    FULL JOIN ( SELECT  t.HopDongID ,
                                                        t.SoHopDong ,
                                                        t.DmSanPhamREF ,
                                                        t.DmHinhThucQuangCaoREF ,
                                                        t.DmWebsiteREF ,
                                                        t.TenWebsite ,
                                                        SUM(t.DsThucChay) DsThucChay
                                                FROM    #TempThucChayPR t
                                                GROUP BY t.HopDongID ,
                                                        t.SoHopDong ,
                                                        t.DmSanPhamREF ,
                                                        t.DmHinhThucQuangCaoREF ,
                                                        t.DmWebsiteREF ,
                                                        t.TenWebsite
                                              ) B ON B.DmWebsiteREF = A.DmWebsiteREF
                                                     AND A.HopDongREF = B.HopDongID
                                                     AND B.DmSanPhamREF = A.DmSanPhamREF
                                                     AND A.DmHinhThucQuangCaoREF = B.DmHinhThucQuangCaoREF
                          WHERE     ( ISNULL(A.ThanhTien, 0) <> ISNULL(B.DsThucChay,
                                                              0) )
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID

    END
--SELECT * FROM dbo.Check_ThongTinDauRaSanPham
```
