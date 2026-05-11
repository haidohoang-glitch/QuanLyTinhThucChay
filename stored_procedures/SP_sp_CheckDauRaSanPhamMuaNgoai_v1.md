# Stored Procedure: `sp_CheckDauRaSanPhamMuaNgoai_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-09 15:43:11.410000
- **Ngày sửa cuối**: 2017-09-22 09:56:22.063000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayDanhSo` | `datetime(8)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--sp_CheckDauRaSanPhamMuaNgoai_v1 '2016-01-01','2017-08-16','2017-08-16'
CREATE PROCEDURE [dbo].[sp_CheckDauRaSanPhamMuaNgoai_v1]
    @NgayDanhSo DATETIME ,
    @NgayBatDau DATETIME ,
    @NgayKetThuc DATETIME
AS
    BEGIN
	-- Xác định những hợp đồng mua ngoài chốt trong khoảng thời gian chọn và kiểm tra thực chạy đã đúng chưa
        SELECT  *
        INTO    #KetQua
        FROM    ( SELECT    CONTRACT_ID HopDongID ,
                            CONTRACT_DETAIL_ID HopDongChiTietREF ,
                            PRODUCT_ID DmSanPhamREF ,
                            mn.ThanhTien ThanhTienThucChayTT ,
                            ISNULL(SUM(ThanhTienSauTrietKhauThucChay
                                       + tcdt.GiaTriThayDoi), 0) ThanhTienThucChay
                  FROM      dbo.ThucChayDaTinh tcdt
                            RIGHT JOIN ( SELECT tcmn.CONTRACT_ID ,
                                                CONTRACT_DETAIL_ID ,
                                                tcmn.PRODUCT_ID ,
                                                hdct.ThanhTien
                                         FROM   dbo.ThucChayMuaNgoaiChot tcmn
                                                INNER JOIN dbo.HopDong hd ON hd.HopDongID = tcmn.CONTRACT_ID
                                                INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcmn.CONTRACT_DETAIL_ID
                                         WHERE  CONVERT(DATE, LAST_MODIFIED_AT) BETWEEN @NgayBatDau
                                                              AND
                                                              @NgayKetThuc
                                                AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                                                AND ( hdct.DmLoaiREF = 13
                                                      OR hdct.DmLoaiBannerREF = 18
                                                    )
                                       ) mn ON tcdt.HopDongChiTietREF = mn.CONTRACT_DETAIL_ID
                  GROUP BY  CONTRACT_ID ,
                            CONTRACT_DETAIL_ID ,
                            PRODUCT_ID ,
                            mn.ThanhTien
                  HAVING    ABS(mn.ThanhTien
                                - ISNULL(SUM(ThanhTienSauTrietKhauThucChay
                                             + tcdt.GiaTriThayDoi), 0)) > 10
                  UNION ALL 
	-- Đối với hợp đồng chưa có trong bảng chốt
                  SELECT    mn.HopDongFK HopDongID ,
                            mn.HopDongChiTietID HopDongChiTietREF ,
                            mn.DmSanPhamREF ,
                            mn.ThanhTienThucChayMuaNgoaiTruocCK/1.1 ThanhTienThucChayTT ,
                            ISNULL(SUM(ThanhTienSauTrietKhauThucChay
                                       + tcdt.GiaTriThayDoi), 0) ThanhTienThucChay
                  FROM      dbo.ThucChayDaTinh tcdt
                            RIGHT JOIN ( SELECT hdct.*
                                         FROM   dbo.HopDong hd
                                                INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongFK = hd.HopDongID
                                         WHERE  CONVERT(DATE, hdct.LastModifiedAt) BETWEEN @NgayBatDau
                                                              AND
                                                              @NgayKetThuc
                                                AND hd.NgayDanhSoHopDong >= @NgayDanhSo
                                                AND ( hdct.DmLoaiREF = 13
                                                      OR hdct.DmLoaiBannerREF = 18
                                                    )
                                       ) mn ON tcdt.HopDongChiTietREF = mn.HopDongChiTietID
                  WHERE     tcdt.HopDongChiTietREF NOT IN (
                            SELECT DISTINCT
                                    CONTRACT_DETAIL_ID
                            FROM    dbo.ThucChayMuaNgoaiChot )
                  GROUP BY  mn.HopDongFK ,
                            mn.HopDongChiTietID ,
                            mn.DmSanPhamREF ,
                            mn.ThanhTienThucChayMuaNgoaiTruocCK ,
                            mn.ThanhTien
                  HAVING    ABS(mn.ThanhTienThucChayMuaNgoaiTruocCK/1.1
                                - ISNULL(SUM(ThanhTienSauTrietKhauThucChay
                                             + tcdt.GiaTriThayDoi), 0)) > 10
                            OR mn.ThanhTienThucChayMuaNgoaiTruocCK/1.1 > mn.ThanhTien
                ) A;
       

        INSERT  INTO dbo.KiemSoatDauRaThucChay_ChiTiet
                ( NgayThucHien ,
                  DotChayBooking ,
                  HopDongID ,
                  SoHopDong ,
                  HopDongChiTietREF ,
                  DmSanPhamREF ,
                  TenSanPham ,
                  DmHinhThucQuangCaoREF ,
                  ThongTinThucTreo ,
                  ThongTinThucChay ,
                  IDLoi ,
                  TenLoiChiTiet ,
                  SPXuLyLoi ,
                  TrangThaiXuLy ,
                  CreatedAt
                )
                SELECT  A.NgayThucHien ,
                        0 DotChayBooking ,
                        A.HopDongID ,
                        A.SoHopDong ,
                        A.HopDongChiTietREF ,
                        A.DmSanPhamREF ,
                        A.TenSanPham ,
                        A.HinhThucQuangCao ,
                        dbo.FormatNumber(A.ThanhTienThucChayTT) ThanhTienThucChayTT ,
                        dbo.FormatNumber(A.ThanhTienThucChay) ThanhTienThucChay ,
                        A.IDLoi ,
                        B.TenLoiChiTiet ,
                        B.SPXuLy ,
                        0 TrangThaiXuLy ,
                        GETDATE()
                FROM    ( SELECT    @NgayKetThuc NgayThucHien ,
                                    A.HopDongID ,
                                    hd.SoHopDong ,
                                    A.HopDongChiTietREF ,
                                    A.DmSanPhamREF ,
                                    hdct.TenSanPham ,
                                    hdct.DmLoaiREF HinhThucQuangCao ,
                                    A.ThanhTienThucChayTT ,
                                    A.ThanhTienThucChay ,
                                    6 IDLoi
                          FROM      #KetQua A
                                    INNER JOIN dbo.HopDong hd ON A.HopDongID = hd.HopDongID
                                    INNER JOIN dbo.HopDongChiTiet hdct ON A.HopDongChiTietREF = hdct.HopDongChiTietID
                        ) A
                        INNER JOIN KiemSoatThucChay_DanhSachLoi B ON A.IDLoi = B.ID;


    END;


--SELECT * FROM dbo.Check_ThongTinDauRaSanPham
```
