# Stored Procedure: `sp_CheckDauVaoChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-18 11:54:18.040000
- **Ngày sửa cuối**: 2017-10-04 09:48:16.130000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_CheckDauVaoChiPhiKhac]
    @NgayDanhSo DATETIME = '2015-01-01',
	@FromDate DATETIME = NULL,
	@ToDate DATETIME = NULL
AS
    BEGIN
        DELETE  FROM dbo.Check_DuLieuDauVaoSanPham
        WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, GETDATE())
                AND IDLyDo IN ( 35, 36 )
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
                                         THEN 36
                                         ELSE 35
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
                                      WHERE     1 = 1
                                                AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                                                AND hd.TrangThaiHopDong <> 3
                                                AND pb.DmSanPhamREF IN ( 242-- Luot up							
						--NHOM SP Chi phí--	
							, 251--Thiết kế, quản lý
							, 252--Hosting
							, 253--Chi phi khac
							, 535--Chi phí quản lý campaign
							, 537--Chi phí viết bài
							, 538--Chi phí thiết kế
							, 539--Chi phí dựng clip
							, 540--Chi phí sáng tạo
							, 541--Chi phí giải thưởng cuộc thi/ Contest
							, 542--Chi phí xây dưng microsite/ tab
							, 555--Chi phí trài trợ
							, 556--Hiệu đính
							, 557--Chèn Clip
							, 558--Chi phí viết bài
							, 559--Chi phí quay clip
							, 560--Chi phí sản xuất
							, 561-- Chi phí khảo sát thị trường online
							, 635-- Quản trị fanpage
							, 563-- Forum Seeding
							, 631-- facebook seeding
							, 651-- đăng tin fanpage
							, 629 )
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
                                                WHERE   1 = 1
                                                        AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                                                        AND hd.TrangThaiHopDong <> 3
                                                        AND hdct.DmSanPhamREF IN (
                                                        242-- Luot up							
						--NHOM SP Chi phí--	
							, 251--Thiết kế, quản lý
							, 252--Hosting
							, 253--Chi phi khac
							, 535--Chi phí quản lý campaign
							, 537--Chi phí viết bài
							, 538--Chi phí thiết kế
							, 539--Chi phí dựng clip
							, 540--Chi phí sáng tạo
							, 541--Chi phí giải thưởng cuộc thi/ Contest
							, 542--Chi phí xây dưng microsite/ tab
							, 555--Chi phí trài trợ
							, 556--Hiệu đính
							, 557--Chèn Clip
							, 558--Chi phí viết bài
							, 559--Chi phí quay clip
							, 560--Chi phí sản xuất
							, 561-- Chi phí khảo sát thị trường online
							, 635-- Quản trị fanpage
							, 563-- Forum Seeding
							, 631-- facebook seeding
							, 651-- đăng tin fanpage
							, 629 )
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
