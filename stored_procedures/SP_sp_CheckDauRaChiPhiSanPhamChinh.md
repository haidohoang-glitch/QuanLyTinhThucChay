# Stored Procedure: `sp_CheckDauRaChiPhiSanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-17 17:04:52.900000
- **Ngày sửa cuối**: 2017-05-18 11:41:12.170000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_CheckDauRaChiPhiSanPhamChinh]
    @NgayThucHien DATETIME = '2017-05-11'
AS
    BEGIN
        DELETE  FROM dbo.Check_ThongTinDauRaSanPham
        WHERE   CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
                AND IDLyDo IN ( 31, 32 )
        SELECT  DISTINCT
                hd.HopDongID ,
                tchdct.HopDongChiTietREF
        INTO    #HDPhatSinh1
        FROM    dbo.ThucChayHopDongChiTiet tchdct
                INNER JOIN dbo.HopDong hd ON hd.HopDongID = tchdct.HopDongREF
                INNER JOIN dbo.HopDongChiTiet hdct ON tchdct.HopDongREF = hdct.HopDongFK
                                                      AND hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
        WHERE   hdct.DmLoaiBannerREF = 17
                AND hdct.DmLoaiREF NOT IN ( 29, 28, 30, 33, 31, 32, 22, 34, 10,
                                            13, 14, 26 )
                AND CONVERT(DATE, tchdct.LastModifiedAt) = @NgayThucHien
                AND hd.TrangThaiHopDong <> 3
                AND hdct.DmSanPhamREF NOT IN ( 423, 306 )
                AND hd.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
                AND tchdct.DeletedStatus = 0

        SELECT  hd.HopDongID ,
                hd.SoHopDong ,
                tchdct.HopDongChiTietREF ,
                tchdct.DmSanPhamREF ,
                tchdct.TenSanPham ,
                hdct.DmLoaiREF ,
                hdct.TenLoai ,
                hdct.DmLoaiBannerREF ,
                hdct.TenLoaiBanner ,
                COUNT(DISTINCT tchdct.ThucChayHopDongChiTietID) SLThucTreo ,
                hdct.DonViTinh ,
                hdct.DonGia * COUNT(DISTINCT tchdct.ThucChayHopDongChiTietID)
                * ( 1 - hdct.ChietKhau / 100 ) ThanhTien
        INTO    #HDThucTreo
        FROM    dbo.ThucChayHopDongChiTiet tchdct
                INNER JOIN #HDPhatSinh1 hdps ON hdps.HopDongChiTietREF = tchdct.HopDongChiTietREF
                                                AND hdps.HopDongID = tchdct.HopDongREF
                INNER JOIN dbo.HopDong hd ON hd.HopDongID = tchdct.HopDongREF
                INNER JOIN dbo.HopDongChiTiet hdct ON tchdct.HopDongREF = hdct.HopDongFK
                                                      AND hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
        WHERE   hdct.DmLoaiBannerREF = 17
                AND hdct.DmLoaiREF NOT IN ( 29, 28, 30, 33, 31, 32, 22, 34, 10,
                                            13, 14, 26 )
                AND CONVERT(DATE, tchdct.LastModifiedAt) <= @NgayThucHien
                AND hd.TrangThaiHopDong <> 3
                AND hdct.DmSanPhamREF NOT IN ( 423, 306 )
                AND hd.DeletedStatus = 0
                AND hdct.DeletedStatus = 0
                AND tchdct.DeletedStatus = 0
		--AND hdct.HopDongChiTietID=91498
GROUP BY        hd.HopDongID ,
                hd.SoHopDong ,
                tchdct.HopDongChiTietREF ,
                tchdct.DmSanPhamREF ,
                tchdct.TenSanPham ,
                hdct.DmLoaiREF ,
                hdct.TenLoai ,
                hdct.DmLoaiBannerREF ,
                hdct.TenLoaiBanner ,
                hdct.DonViTinh ,
                hdct.DonGia ,
                hdct.ChietKhau

        SELECT  tcdt.HopDongID ,
                tcdt.SoHopDong ,
                tcdt.HopDongChiTietREF ,
                tcdt.DmSanPhamREF ,
                tcdt.TenSanPham ,
                DmHinhThucQuangCao ,
                TenHinhThucQuangCao ,
                tcdt.DmLoaiBannerREF ,
                tcdt.TenLoaiBanner ,
                tcdt.DonViTinh ,
                SUM(SoLuongThucChay + SoLuongThayDoi) SLThucChay ,
                SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) DsThucChay
        INTO    #HDThucChay
        FROM    dbo.ThucChayDaTinh tcdt
                INNER JOIN #HDPhatSinh1 hdps ON hdps.HopDongChiTietREF = tcdt.HopDongChiTietREF
                                                AND hdps.HopDongID = tcdt.HopDongID
        WHERE   tcdt.DmLoaiBannerREF = 17
                AND DmHinhThucQuangCao NOT IN ( 29, 28, 30, 33, 31, 32, 22, 34,
                                                10, 13, 14, 26 )
                AND tcdt.DmSanPhamREF NOT IN ( 423, 306 )
                AND TrangThaiHopDong <> 3
                AND tcdt.NgayThucHien <= @NgayThucHien
        GROUP BY tcdt.HopDongID ,
                tcdt.SoHopDong ,
                tcdt.HopDongChiTietREF ,
                tcdt.DmSanPhamREF ,
                tcdt.TenSanPham ,
                DmHinhThucQuangCao ,
                TenHinhThucQuangCao ,
                tcdt.DmLoaiBannerREF ,
                tcdt.TenLoaiBanner ,
                tcdt.DonViTinh

        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  HopDongID ,
                  SoHopDong ,
                  HopDongChiTietID ,
                  DmSanPhamREF ,
                  TenSanPham ,
                  DonViTinh ,
                  DmHinhThucQuangCaoREF ,
                  ThanhTienHD ,
                  SoLuongHD ,
                  SLThucTreo ,
                  SLThucChay ,
                  SLChayTuTinh ,
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
                SELECT  M.NgayThucHien ,
                        M.HopDongID ,
                        M.SoHopDong ,
                        M.HopDongChiTietREF ,
                        M.DmSanPhamREF ,
                        M.TenSanPham ,
                        M.DonViTinh ,
                        M.DmHinhThucQuangCaoREF ,
                        M.ThanhTienTuTinh ,
                        M.SLTuTinh ,
                        M.SLTuTinh ,
                        M.SLThucChay ,
                        M.SLTuTinh ,
                        M.DsThucChay ,
                        M.ThanhTienTuTinh ,
                        M.GiaTriLech ,
                        M.ID_LyDo ,
                        N.TenLoiChiTiet ,
                        0 TrangThaiXuLy ,
                        N.ID_Loai ,
                        N.TenLoai ,
                        GETDATE() CreatedAt
                FROM    ( SELECT    @NgayThucHien NgayThucHien ,
                                    ISNULL(A.HopDongID, B.HopDongID) HopDongID ,
                                    ISNULL(A.SoHopDong, B.SoHopDong) SoHopDong ,
                                    ISNULL(A.HopDongChiTietREF,
                                           B.HopDongChiTietREF) HopDongChiTietREF ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                                    ISNULL(A.TenSanPham, B.TenSanPham) TenSanPham ,
                                    ISNULL(A.DmLoaiREF, B.DmHinhThucQuangCao) DmHinhThucQuangCaoREF ,
                                    ISNULL(A.DonViTinh, B.DonViTinh) DonViTinh ,
                                    ISNULL(A.SLThucTreo, 0) SLTuTinh ,
                                    ISNULL(B.SLThucChay, 0) SLThucChay ,
                                    ISNULL(A.ThanhTien, 0) ThanhTienTuTinh ,
                                    ISNULL(B.DsThucChay, 0) DsThucChay ,
                                    ISNULL(A.SLThucTreo, 0)
                                    - ISNULL(B.SLThucChay, 0) GiaTriLech ,
                                    31 ID_LyDo
                          FROM      #HDThucTreo A
                                    FULL JOIN #HDThucChay B ON A.HopDongID = B.HopDongID
                                                              AND B.HopDongChiTietREF = A.HopDongChiTietREF
                          WHERE     ISNULL(B.SLThucChay, 0) <> ISNULL(A.SLThucTreo,
                                                              0)
                          UNION ALL
                          SELECT    @NgayThucHien NgayThucHien ,
                                    ISNULL(A.HopDongID, B.HopDongID) HopDongID ,
                                    ISNULL(A.SoHopDong, B.SoHopDong) SoHopDong ,
                                    ISNULL(A.HopDongChiTietREF,
                                           B.HopDongChiTietREF) HopDongChiTietREF ,
                                    ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                                    ISNULL(A.TenSanPham, B.TenSanPham) TenSanPham ,
                                    ISNULL(A.DmLoaiREF, B.DmHinhThucQuangCao) DmHinhThucQuangCaoREF ,
                                    ISNULL(A.DonViTinh, B.DonViTinh) DonViTinh ,
                                    ISNULL(A.SLThucTreo, 0) SLTuTinh ,
                                    ISNULL(B.SLThucChay, 0) SLThucChay ,
                                    ISNULL(A.ThanhTien, 0) ThanhTienTuTinh ,
                                    ISNULL(B.DsThucChay, 0) DsThucChay ,
                                    ISNULL(A.SLThucTreo, 0)
                                    - ISNULL(B.SLThucChay, 0) SLLech ,
                                    32 ID_LyDo
                          FROM      #HDThucTreo A
                                    FULL JOIN #HDThucChay B ON A.HopDongID = B.HopDongID
                                                              AND B.HopDongChiTietREF = A.HopDongChiTietREF
                          WHERE     ISNULL(B.DsThucChay, 0) <> ISNULL(A.ThanhTien,
                                                              0)
                        ) M
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu N ON M.ID_LyDo = N.ID
        
    END
--SELECT  *
--FROM    dbo.Check_ThongTinDauRaSanPham
```
