# Stored Procedure: `sp_CheckDauRaSanPhamCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-03 16:02:45.050000
- **Ngày sửa cuối**: 2017-05-17 17:36:47.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayCheck` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamCPD]
    @NgayCheck DATETIME = '2017-05-15'
AS
    BEGIN
	DELETE FROM dbo.Check_ThongTinDauRaSanPham WHERE IDLoai=1 AND IDLyDo IN (24,25) AND CONVERT(DATE,CreatedAt) = CONVERT(DATE,GETDATE())
        SELECT  HopDongREF ,
                HopDongChiTietREF ,
                A.DmSanPhamREF ,
                SUM(DATEDIFF(DD, @NgayCheck, @NgayCheck) + 1) SLThucChay
        INTO    #ThucChayHDCT
        FROM    ( SELECT DISTINCT
                            HopDongREF ,
                            HopDongChiTietREF ,
                            DmSanPhamREF ,
                            BookingREF ,
                            ThoiGianBatDau ,
                            ThoiGianKetThuc
                  FROM      dbo.ThucChayHopDongChiTiet
                  WHERE     @NgayCheck BETWEEN ThoiGianBatDau
                                       AND     ThoiGianKetThuc
                            AND DmSanPhamREF IN ( 140, 228, 564, 549 )
                            AND DeletedStatus = 0
                ) A
        GROUP BY HopDongREF ,
                HopDongChiTietREF ,
                A.DmSanPhamREF

        SELECT  HopDongREF ,
                SoHopDong ,
                HopDongChiTietREF ,
                DmSanPhamREF ,
                TenSanPham ,
                DmWebsiteREF ,
                TenWebsite ,
                ThanhTien ,
                SUM(DATEDIFF(DD, ThoiGianBatDau, ThoiGianKetThuc) + 1) SLNgayChay ,
                ThanhTien / SUM(DATEDIFF(DD, ThoiGianBatDau, ThoiGianKetThuc)
                                + 1) DonGiaTheoNgay
        INTO    #DonGiaThucChay
        FROM    ( SELECT DISTINCT
                            HopDongREF ,
                            hd.SoHopDong ,
                            HopDongChiTietREF ,
                            dchdct.BookingREF ,
                            hd.DmSanPhamREF ,
                            hd.TenSanPham ,
                            hd.DmWebsiteREF ,
                            hd.TenWebsite ,
                            dchdct.ThoiGianBatDau ,
                            dchdct.ThoiGianKetThuc ,
                            hd.ThanhTien
                  FROM      dbo.DotChayHopDongChiTiet dchdct
                            INNER JOIN ( SELECT hd.HopDongID ,
                                                hd.SoHopDong ,
                                                hdct.HopDongChiTietID ,
                                                hdct.DmSanPhamREF ,
                                                hdct.TenSanPham ,
                                                hdct.DmWebsiteREF ,
                                                hdct.TenWebsite ,
                                                hdct.ThanhTien
                                         FROM   dbo.HopDong hd
                                                INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
                                                INNER JOIN ( SELECT DISTINCT
                                                              HopDongREF
                                                             FROM
                                                              #ThucChayHDCT
                                                           ) tchdct ON hd.HopDongID = tchdct.HopDongREF
                                         WHERE  hd.DeletedStatus = 0
                                                AND hdct.DeletedStatus = 0
                                                AND hd.TrangThaiHopDong <> 3
                                                AND hdct.DmSanPhamREF IN ( 140,
                                                              228, 564, 549 )
                                       ) hd ON dchdct.HopDongREF = hd.HopDongID
                                               AND dchdct.HopDongChiTietREF = hd.HopDongChiTietID
                  WHERE     1 = 1
                            AND dchdct.DeletedStatus = 0
                ) A
        GROUP BY HopDongREF ,
                SoHopDong ,
                HopDongChiTietREF ,
                DmSanPhamREF ,
                ThanhTien ,
                TenSanPham ,
                DmWebsiteREF ,
                TenWebsite 
        SELECT  ISNULL(A.NgayThucHien, B.NgayThucHien) NgayThucHien ,
                ISNULL(A.HopDongREF, B.HopDongID) HopDongREF ,
                ISNULL(A.SoHopDong, B.SoHopDong) SoHopDong ,
                ISNULL(A.HopDongChiTietREF, B.HopDongChiTietREF) HopDongChiTietREF ,
                ISNULL(A.DmSanPhamREF, B.DmSanPhamREF) DmSanPhamREF ,
                ISNULL(A.TenSanPham, B.TenSanPham) TenSanPham ,
                ISNULL(B.DmWebsiteREF, 0) DmWebsiteREF_TC ,
                ISNULL(A.DmWebsiteREF, 0) DmWebsiteREF_HD ,
                ISNULL(B.TenWebsite, '') TenWebsite_TC ,
                ISNULL(A.TenWebsite, '') TenWebsite_HD ,
        --ISNULL(A.TenWebsite, B.TenWebsite) TenWebsite ,
                ISNULL(A.SLThucChay, 0) SLThucChayTuTinh ,
                ISNULL(B.SoLuongThucChay, 0) SLThucChayDaTinh ,
                ISNULL(A.SLThucChay, 0) - ISNULL(B.SoLuongThucChay, 0) SLLech ,
                ISNULL(A.ThanhTienThucChayTheoNgay, 0) ThanhTienTuTinh ,
                ISNULL(B.ThanhTienSauTrietKhauThucChay, 0) ThanhTienDaTinh ,
                ROUND(ISNULL(A.ThanhTienThucChayTheoNgay, 0)
                      - ISNULL(B.ThanhTienSauTrietKhauThucChay, 0), 0) ThanhTienLech ,
                ISNULL(B.IsPhatSinhThayDoi, 0) IsPhatSinhThayDoi
        INTO    #DanhSachHopDongLech
        FROM    ( SELECT    @NgayCheck NgayThucHien ,
                            A.HopDongREF ,
                            B.SoHopDong ,
                            A.HopDongChiTietREF ,
                            B.DmSanPhamREF ,
                            TenSanPham ,
                            DmWebsiteREF ,
                            TenWebsite ,
                            ISNULL(B.SLNgayChay, 0) TongSoLuongNgayChay ,
                            A.SLThucChay ,
                            ISNULL(B.DonGiaTheoNgay, 0) * A.SLThucChay ThanhTienThucChayTheoNgay
                  FROM      #ThucChayHDCT A
                            LEFT JOIN #DonGiaThucChay B ON B.HopDongChiTietREF = A.HopDongChiTietREF
                                                           AND B.HopDongREF = A.HopDongREF
                  WHERE     1 = 1
                ) A
                FULL JOIN ( SELECT  NgayThucHien ,
                                    HopDongID ,
                                    SoHopDong ,
                                    HopDongChiTietREF ,
                                    DmSanPhamREF ,
                                    TenSanPham ,
                                    DmWebsiteREF ,
                                    TenWebsite ,
                                    SoLuongThucChay ,
                                    ThanhTienSauTrietKhauThucChay ,
                                    CASE WHEN ABS(ROUND(GiaTriThayDoi, -1) - 0) < 1
                                         THEN 0
                                         ELSE 1
                                    END IsPhatSinhThayDoi
                            FROM    dbo.ThucChayDaTinh
                            WHERE   NgayThucHien = @NgayCheck
                                    AND DmSanPhamREF IN ( 140, 228, 564, 549 )
                          ) B ON B.HopDongChiTietREF = A.HopDongChiTietREF
                                 AND A.HopDongREF = B.HopDongID
                                 AND A.DmSanPhamREF = B.DmSanPhamREF
------------ Check các hợp đồng không phát sinh giá trị thay đổi



------------------- Hợp đồng phát sinh giá trị thay đổi
---------- Check lại các hợp đồng phát sinh giá trị thay đổi với all thời gian chạy
        SELECT  @NgayCheck NgayThucHien ,
                ISNULL(B.HopDongREF, A.HopDongID) HopDongID ,
                ISNULL(A.SoHopDong, B.SoHopDong) SoHopDong ,
                ISNULL(B.HopDongChiTietREF, A.HopDongChiTietREF) HopDongChiTietREF ,
                ISNULL(B.DmSanPhamREF, A.DmSanPhamREF) DmSanPhamREF ,
                ISNULL(A.TenSanPham, B.TenSanPham) TenSanPham ,
                ISNULL(A.DmWebsiteREF, 0) DmWebsiteREF_TC ,
                ISNULL(B.DmWebsiteREF, 0) DmWebsiteREF_HD ,
                ISNULL(A.TenWebsite, '') TenWebsite_TC ,
                ISNULL(B.TenWebsite, '') TenWebsite_HD ,
        --ISNULL(A.TenWebsite, B.TenWebsite) TenWebsite ,
                ISNULL(B.SLThucChay, 0) SLThucChayTuTinh ,
                ISNULL(A.SLThucChay, 0) SLThucChayDaTinh ,
                ROUND(ISNULL(B.SLThucChay, 0) - ISNULL(A.SLThucChay, 0), 0) SLLech ,
                ISNULL(B.TongThucChay, 0) DSThucChayTuTinh ,
                ISNULL(A.DSThucChay, 0) DSThucChayDaTinh ,
                ROUND(ISNULL(B.TongThucChay, 0) - ISNULL(A.DSThucChay, 0), 0) ThanhTienLech ,
                1 IsPhatSinhThayDoi
        INTO    #DsHopDongThayDoi
        FROM    ( SELECT    HopDongID ,
                            tcdt.SoHopDong ,
                            tcdt.HopDongChiTietREF ,
                            tcdt.DmSanPhamREF ,
                            tcdt.TenSanPham ,
                            tcdt.DmWebsiteREF ,
                            tcdt.TenWebsite ,
                            SUM(SoLuongThucChay + tcdt.SoLuongThayDoi) SLThucChay ,
                            SUM(ThanhTienSauTrietKhauThucChay
                                + tcdt.GiaTriThayDoi) DSThucChay
                  FROM      dbo.ThucChayDaTinh tcdt
                            INNER JOIN ( SELECT DISTINCT
                                                HopDongChiTietREF ,
                                                MAX(IsPhatSinhThayDoi) IsPhatSinhThayDoi
                                         FROM   #DanhSachHopDongLech
                                         GROUP BY HopDongChiTietREF
                                       ) ds ON ds.HopDongChiTietREF = tcdt.HopDongChiTietREF
                  WHERE     NgayThucHien <= @NgayCheck
                            AND DmSanPhamREF IN ( 140, 228, 564, 549 )
                            AND IsPhatSinhThayDoi <> 0
        --AND tcdt.HopDongID = 44264
GROUP BY                    HopDongID ,
                            tcdt.SoHopDong ,
                            tcdt.HopDongChiTietREF ,
                            tcdt.DmSanPhamREF ,
                            tcdt.TenSanPham ,
                            tcdt.DmWebsiteREF ,
                            tcdt.TenWebsite
                ) A
                FULL JOIN ( SELECT  A.HopDongREF ,
                                    dgtc.SoHopDong ,
                                    A.HopDongChiTietREF ,
                                    A.DmSanPhamREF ,
                                    dgtc.TenSanPham ,
                                    dgtc.DmWebsiteREF ,
                                    dgtc.TenWebsite ,
                                    SUM(DATEDIFF(DD, ThoiGianBatDau,
                                                 ThoiGianKetThuc) + 1) SLThucChay ,
                                    dgtc.DonGiaTheoNgay ,
                                    SUM(DATEDIFF(DD, ThoiGianBatDau,
                                                 ThoiGianKetThuc) + 1)
                                    * dgtc.DonGiaTheoNgay TongThucChay
                            FROM    ( SELECT DISTINCT
                                                tchdct.HopDongREF ,
                                                tchdct.HopDongChiTietREF ,
                                                tchdct.DmSanPhamREF ,
                                                BookingREF ,
                                                ThoiGianBatDau ,
                                                CASE WHEN ThoiGianKetThuc >= @NgayCheck
                                                     THEN @NgayCheck
                                                     ELSE tchdct.ThoiGianKetThuc
                                                END ThoiGianKetThuc
                                      FROM      dbo.ThucChayHopDongChiTiet tchdct
                                                INNER JOIN ( SELECT DISTINCT
                                                              HopDongChiTietREF ,
                                                              MAX(IsPhatSinhThayDoi) IsPhatSinhThayDoi
                                                             FROM
                                                              #DanhSachHopDongLech
                                                             GROUP BY HopDongChiTietREF
                                                           ) tcdt ON tcdt.HopDongChiTietREF = tchdct.HopDongChiTietREF
                                      WHERE     1 = 1
                                                AND tchdct.DmSanPhamREF IN (
                                                140, 228, 564, 549 )
                                                AND tchdct.DeletedStatus = 0
                                                AND IsPhatSinhThayDoi <> 0
                                                AND tchdct.ThoiGianBatDau <= @NgayCheck
                                    ) A
                                    INNER JOIN #DonGiaThucChay dgtc ON A.HopDongREF = dgtc.HopDongREF
                                                              AND dgtc.HopDongChiTietREF = A.HopDongChiTietREF
                            GROUP BY A.HopDongREF ,
                                    A.HopDongChiTietREF ,
                                    A.DmSanPhamREF ,
                                    dgtc.TenSanPham ,
                                    dgtc.DmWebsiteREF ,
                                    dgtc.TenWebsite ,
                                    dgtc.DonGiaTheoNgay ,
                                    dgtc.SoHopDong
                          ) B ON B.DmSanPhamREF = A.DmSanPhamREF
                                 AND B.HopDongChiTietREF = A.HopDongChiTietREF
                                 AND B.HopDongREF = A.HopDongID
        WHERE   ROUND(ISNULL(A.SLThucChay, 0) - ISNULL(B.SLThucChay, 0), 0) <> 0
                OR ROUND(ISNULL(A.DSThucChay, 0) - ISNULL(B.TongThucChay, 0),
                         0) <> 0 
        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  HopDongID ,
                  SoHopDong ,
                  HopDongChiTietID ,
                  DmSanPhamREF ,
                  TenSanPham ,
                  DmWebsiteREF_HD ,
                  TenWebsite_HD ,
                  DmWebsiteREF_TC ,
                  TenWebsite_TC ,
                  SLChayTuTinh ,
                  SLThucChay ,
                  GiaTriLech ,
                  TienThucChayTuTinh ,
                  ThanhTienThucChay ,
                  IDLyDo ,
                  LyDo ,
                  IDLoai ,
                  TenLoai ,
                  TrangThaiXuLy ,
				  CreatedAt
                )
                SELECT  A.NgayThucHien ,
                        A.HopDongREF ,
                        A.SoHopDong ,
                        A.HopDongChiTietREF ,
                        A.DmSanPhamREF ,
                        A.TenSanPham ,
                        A.DmWebsiteREF_HD ,
                        A.TenWebsite_HD ,
                        A.DmWebsiteREF_TC ,
                        A.TenWebsite_TC ,
                        A.SLThucChayTuTinh ,
                        A.SLThucChayDaTinh ,
                        A.SLLech ,
                        A.ThanhTienTuTinh ,
                        A.ThanhTienDaTinh ,
                        CASE WHEN A.SLLech <> 0 THEN 24
                             WHEN A.ThanhTienLech <> 0 THEN 25
                        END IDLyDo ,
                        B.TenLoiChiTiet ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        0 TrangThaiXuLy,
						GETDATE()
                FROM    ( SELECT    *
                          FROM      #DanhSachHopDongLech
                          WHERE     ( ThanhTienLech <> 0
                                      OR SLLech <> 0
                                    )
                                    AND IsPhatSinhThayDoi <> 1
                          UNION ALL
                          SELECT    *
                          FROM      #DsHopDongThayDoi
                        ) A
                        INNER JOIN dbo.DmLoiKhiCheckDuLieu B ON CASE
                                                              WHEN A.SLLech <> 0
                                                              THEN 24
                                                              WHEN A.ThanhTienLech <> 0
                                                              THEN 25
                                                              END = B.ID
                WHERE   A.SLLech <> 0
        INSERT  INTO dbo.Check_ThongTinDauRaSanPham
                ( NgayThucHien ,
                  HopDongID ,
                  SoHopDong ,
                  HopDongChiTietID ,
                  DmSanPhamREF ,
                  TenSanPham ,
                  DmWebsiteREF_HD ,
                  TenWebsite_HD ,
                  DmWebsiteREF_TC ,
                  TenWebsite_TC ,
                  SLChayTuTinh ,
                  SLThucChay ,
                  TienThucChayTuTinh ,
                  ThanhTienThucChay ,
                  GiaTriLech ,
                  IDLyDo ,
                  LyDo ,
                  IDLoai ,
                  TenLoai ,
                  TrangThaiXuLy ,
				  CreatedAt
                )
                SELECT  A.NgayThucHien ,
                        A.HopDongREF ,
                        A.SoHopDong ,
                        A.HopDongChiTietREF ,
                        A.DmSanPhamREF ,
                        A.TenSanPham ,
                        A.DmWebsiteREF_HD ,
                        A.TenWebsite_HD ,
                        A.DmWebsiteREF_TC ,
                        A.TenWebsite_TC ,
                        A.SLThucChayTuTinh ,
                        A.SLThucChayDaTinh ,
                        A.ThanhTienTuTinh ,
                        A.ThanhTienDaTinh ,
                        A.ThanhTienLech ,
                        CASE WHEN A.SLLech <> 0 THEN 24
                             WHEN A.ThanhTienLech <> 0 THEN 25
                        END IDLyDo ,
                        B.TenLoiChiTiet ,
                        B.ID_Loai ,
                        B.TenLoai ,
                        0 TrangThaiXuLy,
						GETDATE()
                FROM    ( SELECT    *
                          FROM      #DanhSachHopDongLech
                          WHERE     ( ThanhTienLech <> 0
                                      OR SLLech <> 0
                                    )
                                    AND IsPhatSinhThayDoi <> 1
                          UNION ALL
                          SELECT    *
                          FROM      #DsHopDongThayDoi
                        ) A
                        INNER JOIN dbo.DmLoiKhiCheckDuLieu B ON CASE
                                                              WHEN A.SLLech <> 0
                                                              THEN 24
                                                              WHEN A.ThanhTienLech <> 0
                                                              THEN 25
                                                              END = B.ID
                WHERE   A.ThanhTienLech <> 0

      
    END 
	--sp_CheckDauRaSanPhamCPD
```
