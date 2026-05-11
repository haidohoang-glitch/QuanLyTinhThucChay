# Stored Procedure: `sp_CheckDauRaChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-18 11:44:23.513000
- **Ngày sửa cuối**: 2017-05-18 11:44:43.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_CheckDauRaChiPhiKhac]
    @NgayThucHien DATETIME = '2017-05-15'
AS
    BEGIN

        DELETE  FROM dbo.Check_ThongTinDauRaSanPham
        WHERE   CONVERT(DATE, CreatedAt) = CONVERT(DATE, GETDATE())
                AND IDLyDo IN ( 33, 34 )
        SELECT DISTINCT
                hd.HopDongID ,
                tchdct.HopDongChiTietREF
        INTO    #HDPhatSinh1
        FROM    dbo.ThucChayHopDongChiTiet tchdct
                INNER JOIN dbo.HopDong hd ON hd.HopDongID = tchdct.HopDongREF
                INNER JOIN dbo.HopDongChiTiet hdct ON tchdct.HopDongREF = hdct.HopDongFK
                                                      AND hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
        WHERE   1 = 1
		--hdct.DmLoaiBannerREF = 17
        --AND hdct.DmLoaiREF NOT IN ( 29, 28, 30, 33, 31, 32, 22, 34, 10, 13, 14,
        --                            26 )
                AND CONVERT(DATE, tchdct.LastModifiedAt) = @NgayThucHien
                AND hd.TrangThaiHopDong <> 3
                AND hdct.DmSanPhamREF IN ( 242-- Luot up							
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

        SELECT  hd.HopDongID ,
                hd.SoHopDong ,
                tchdct.HopDongChiTietREF ,
                tchdct.DmSanPhamREF ,
                tchdct.TenSanPham ,
                hdct.DmLoaiREF ,
                hdct.TenLoai ,
                hdct.DmLoaiBannerREF ,
                hdct.TenLoaiBanner ,
                COUNT(tchdct.ThucChayHopDongChiTietID) SLThucTreo ,
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
        WHERE   1 = 1
		--hdct.DmLoaiBannerREF = 17
        --AND hdct.DmLoaiREF NOT IN ( 29, 28, 30, 33, 31, 32, 22, 34, 10, 13, 14,
        --                            26 )
        --AND CONVERT(DATE, tchdct.LastModifiedAt) = @NgayThucHien
                AND hd.TrangThaiHopDong <> 3
                AND hdct.DmSanPhamREF IN ( 242-- Luot up							
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
                INNER JOIN #HDPhatSinh1 hd ON hd.HopDongChiTietREF = tcdt.HopDongChiTietREF
                                              AND hd.HopDongID = tcdt.HopDongID
        WHERE   1 = 1
		--tcdt.DmLoaiBannerREF = 17
        --AND DmHinhThucQuangCao NOT IN ( 29, 28, 30, 33, 31, 32, 22, 34, 10, 13,
        --                                14, 26 )
                AND tcdt.DmSanPhamREF IN ( 242-- Luot up							
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
                                    34 ID_LyDo
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
                                    ISNULL(A.ThanhTien, 0)
                                    - ISNULL(B.DsThucChay, 0) SLLech ,
                                    33 ID_LyDo
                          FROM      #HDThucTreo A
                                    FULL JOIN #HDThucChay B ON A.HopDongID = B.HopDongID
                                                              AND B.HopDongChiTietREF = A.HopDongChiTietREF
                          WHERE     ISNULL(B.DsThucChay, 0) <> ISNULL(A.ThanhTien,
                                                              0)
                        ) M
                        LEFT JOIN dbo.DmLoiKhiCheckDuLieu N ON M.ID_LyDo = N.ID
    END 
```
