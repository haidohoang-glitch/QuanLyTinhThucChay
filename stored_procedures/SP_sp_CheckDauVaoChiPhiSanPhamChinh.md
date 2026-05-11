# Stored Procedure: `sp_CheckDauVaoChiPhiSanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-17 14:47:08.473000
- **Ngày sửa cuối**: 2017-10-04 09:48:57.110000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_CheckDauVaoChiPhiSanPhamChinh]
    @NgayDanhSo DATETIME = '2015-01-01',
	@FromDate DATETIME = NULL,
	@ToDate DATETIME = NULL
AS
    BEGIN
        DELETE  FROM dbo.Check_DuLieuDauVaoSanPham
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, GETDATE())
                AND IDLyDo IN ( 29, 30 )
        INSERT  INTO dbo.Check_DuLieuDauVaoSanPham
                ( NgayThucHien ,
                  HopDongREF ,
                  SoHopDong ,
                  HopDongChiTietREF ,
                  DmSanPhamREF ,
                  DmDonViTinhREF ,
                  DonViTinh ,
                  SoLuongTrenHD ,
                  SoLuongTrenThucTreo ,
                  DmHinhThucQuangCaoREF_HD ,
                  DmHinhThucQuangCaoREF_TT ,
                  IDLyDo ,
                  LyDo ,
                  TrangThaiXuLy ,
                  IDLoai ,
                  TenLoai ,
                  GhiChu 
                )
                SELECT  A.* ,
                        B.TenLoiChiTiet ,
                        0 TrangThaiXuLy ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        '' GhiChu
                FROM    ( SELECT    GETDATE() NgayThucHien ,
                                    A.HopDongID ,
                                    A.SoHopDong ,
                                    A.HopDongChiTietID ,
                                    A.DmSanPhamREF ,
                                    A.DonViTinhREF ,
                                    A.DonViTinh ,
                                    A.SoLuong ,
                                    ISNULL(B.SLThucTreo, 0) SLThucTreo ,
                                    A.DmLoaiREF DmHinhThucQuangCaoREF_HD ,
                                    ISNULL(B.DmLoaiREF, 0) DmHinhThucQuangCaoREF_TT ,
                                    CASE WHEN ISNULL(B.SLThucTreo, 0) = 0
                                         THEN 29
                                         ELSE 30
                                    END IDLyDo
                          FROM      ( SELECT    hd.HopDongID ,
                                                hd.SoHopDong ,
                                                pb.HopDongChiTietID ,
                                                pb.DmSanPhamREF ,
                                                pb.TenSanPham ,
                                                pb.DmLoaiREF ,
                                                pb.TenLoai ,
                                                pb.DmLoaiBannerREF ,
                                                pb.TenLoaiBanner ,
                                                pb.SoLuong ,
                                                pb.DonViTinhREF ,
                                                pb.DonViTinh
                                      FROM      dbo.HopDong hd
                                                INNER JOIN dbo.HopDongChiTiet pb ON hd.HopDongID = pb.HopDongFK
                                      WHERE     pb.DmLoaiBannerREF = 17
                                                AND pb.DmLoaiREF NOT IN ( 29,
                                                              28, 30, 33, 31,
                                                              32, 22, 34, 10,
                                                              13, 14, 26 )
                                                AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                                                AND hd.TrangThaiHopDong <> 3
                                                AND pb.DmSanPhamREF NOT IN (
                                                423, 306 )
                                                AND hd.DeletedStatus = 0
                                                AND pb.DeletedStatus = 0
                                    ) A
                                    LEFT JOIN ( SELECT  hd.HopDongID ,
                                                        hd.SoHopDong ,
                                                        tchdct.HopDongChiTietREF ,
                                                        tchdct.DmSanPhamREF ,
                                                        tchdct.TenSanPham ,
                                                        hdct.DmLoaiREF ,
                                                        hdct.TenLoai ,
                                                        hdct.DmLoaiBannerREF ,
                                                        hdct.TenLoaiBanner ,
                                                        COUNT(DISTINCT tchdct.ThucChayHopDongChiTietID) SLThucTreo ,
                                                        hdct.DonViTinhREF ,
                                                        hdct.DonViTinh
                                                FROM    dbo.ThucChayHopDongChiTiet tchdct
                                                        INNER JOIN dbo.HopDong hd ON hd.HopDongID = tchdct.HopDongREF
                                                        INNER JOIN dbo.HopDongChiTiet hdct ON tchdct.HopDongREF = hdct.HopDongFK
                                                              AND hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
                                                WHERE   hdct.DmLoaiBannerREF = 17
                                                        AND hdct.DmLoaiREF NOT IN (
                                                        29, 28, 30, 33, 31, 32,
                                                        22, 34, 10, 13, 14, 26 )
                                                        AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                                                        AND hd.TrangThaiHopDong <> 3
                                                        AND hdct.DmSanPhamREF NOT IN (
                                                        423, 306 )
                                                        AND hd.DeletedStatus = 0
                                                        AND hdct.DeletedStatus = 0
                                                        AND tchdct.DeletedStatus = 0
                                                GROUP BY hd.HopDongID ,
                                                        hd.SoHopDong ,
                                                        tchdct.HopDongChiTietREF ,
                                                        tchdct.DmSanPhamREF ,
                                                        tchdct.TenSanPham ,
                                                        hdct.DmLoaiREF ,
                                                        hdct.TenLoai ,
                                                        hdct.DmLoaiBannerREF ,
                                                        hdct.TenLoaiBanner ,
                                                        hdct.DonViTinhREF ,
                                                        hdct.DonViTinh
                                              ) B ON B.HopDongID = A.HopDongID
                                                     AND A.HopDongChiTietID = B.HopDongChiTietREF
                        ) A
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu B ON A.IDLyDo = B.ID
                WHERE   A.SoLuong <> A.SLThucTreo
    END

--		SELECT * FROM dbo.ThucChayHopDongChiTiet WHERE HopDongChiTietREF=78676
--SELECT  *
--FROM    dbo.HopDongChiTiet
--WHERE   HopDongChiTietID = 78676

--SELECT * FROM dbo.DmHinhThucQuangCao WHERE DmHinhThucQuangCaoID IN 
```
