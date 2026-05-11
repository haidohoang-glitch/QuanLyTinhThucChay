# Stored Procedure: `sp_KSTC_CheckTCDT_LaiMuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-06 14:47:14.170000
- **Ngày sửa cuối**: 2022-12-30 17:53:57.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec sp_KSTC_CheckTCDT_LaiMuaNgoai '2020-09-28'
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_LaiMuaNgoai]
    -- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME
AS
BEGIN
    SELECT tc.*
    FROM
    (
        SELECT A.*,
               B.*
        FROM
        (
            SELECT CONVERT(DATE, tcmn.NgayChot) NgayChot,
                   hd.HopDongID,
                   hd.SoHopDong,
                   hd.DmMaHopDongREF,
                   hd.NgayDanhSoHopDong,
                   hd.TrangThaiHopDong,
                   hd.SysNhanVienREF,
                   hd.TenDangNhap,
                   hd.DmPhongBanREF,
                   hd.DmBoPhanREF,
                   hd.DmNhomLamViecREF,
                   hd.DmDiaDiemLamViecREF,
                   hd.DmKhachHangREF,
                   hdct.HopDongChiTietID,
                   hdct.DanhSachNhanHangREF,
                   hdct.DmNhomNganhREF,
                   hdct.DmLoaiREF,
                   hdct.DmSanPhamREF,
                   hdct.DmChuyenMucREF,
                   hdct.DmLoaiBannerREF,
                   hdct.DmViTriREF,
                   hdct.SoLuong,
                   hdct.DonViTinhREF,
                   hdct.DonGia,
                   hdct.ChietKhau,
                   hdct.ThanhTien,
                   hdct.IsKhuyenMai,
                   hdct.KhuyenMai,
                   hdct.DmWebsiteREF,
                   hdct.TenWebsite,
                   hdctmn.ThanhTienSauCKMua,
                   hdctmn.ThanhTienLaiSauCK,
                   tcmn.ThucChayMuaNgoaiChiTietID,
                   tcmn.ChietKhauMuaNgoai,
                   tcmn.TuNgay,
                   tcmn.DenNgay,
                   tcmn.DmDonViTinhREF,
                   tcmn.SoLuongThucChay,
                   tcmn.ThanhTienThucChayBanSauCK,
                   tcmn.ThanhTienLaiThucChaySauCK,
                   ISNULL((tcmn.ThanhTienMuaNgoaiTruocCK * (100 - tcmn.ChietKhauMuaNgoai) / 100), 0) AS TongThanhTienThucChayMuaSauCK,
                   (CASE
                        WHEN tcmn.SoLuongThucChay <> 0 THEN
                            ISNULL((tcmn.ThanhTienMuaNgoaiTruocCK / tcmn.SoLuongThucChay), 0)
                        ELSE
                            -999999
                    END
                   ) AS DonGiaTheoDonViTinhTC
            --,tcmn. [ThanhTienLaiThucChayKM]
            --,[SoLuongThucChayKM]
            --,[SoLuongThucChayLechTreoHa]
            --,[ThanhTienLechTreoHa]
            --,[GiaTriThayDoiLaiSauCK]
            --,[SoLuongThayDoi]
            --,[SoLuongKMThayDoi]
            --,[GiaTriKMLaiThayDoi]		
            FROM ThucChayMuaNgoaiChiTiet tcmn
                INNER JOIN HopDongChiTiet_MuaNgoai hdctmn
                    ON tcmn.HopDongChiTietREF = hdctmn.HopDongChiTietID
                INNER JOIN HopDongChiTiet hdct
                    ON hdctmn.HopDongChiTietID = hdct.HopDongChiTietID
                INNER JOIN HopDong hd
                    ON hdct.HopDongFK = hd.HopDongID
            WHERE 1 = 1
                  AND hdct.DeletedStatus = 0
                  AND tcmn.DeletedStatus = 0
                  AND hdctmn.DeletedStatus = 0
                  AND tcmn.DeletedStatus = 0
                  AND tcmn.TrangThaiTinhThucChay = 1
                  AND
                  (
                      hdct.DmLoaiREF = 13
                      OR hdct.DmLoaiBannerREF = 18
                  )
                  AND HopDongREF NOT IN
                      (
                          SELECT HopDongID FROM HopDong WHERE TrangThaiHopDong = 3
                      )
                  AND CONVERT(DATE, NgayChot)
                  BETWEEN '2013-01-01' AND @NgayThucHien
                  AND tcmn.HopDongChiTietREF NOT IN
                      (
                          SELECT HopDongChiTietID FROM MuaNgoaiChot_TinhBoSung_2016
                      )
				AND hdct.DmSanPhamREF <> 5184 --sp creatorcontent
        --and HopDongChiTietREF =578571 and ThucChayMuaNgoaiChiTietID = 23580
        ) A
            FULL OUTER JOIN
            (
                SELECT [NgayThucHien],
                       [HopDongREF],
                       [HopDongChiTietREF],
                       [DmSanPhamREF] DmSanPhamREF_tcdtmn,
                       [SoHopDong] SoHopDong_tcdtmn,
                       [DmMaHopDongREF] DmMaHopDongREF_tcdtmn,
                       [NgayDanhSoHopDong] NgayDanhSoHopDong_tcdtmn,
                       [TrangThaiHopDong] TrangThaiHopDong_tcdtmn,
                       [DmNhanVienREF] DmNhanVienREF_tcdtmn,
                       [TenDangNhap] TenDangNhap_tcdtmn,
                       [DmPhongBanREF] DmPhongBanREF_tcdtmn,
                       [DmBoPhanREF] DmBoPhanREF_tcdtmn,
                       [DmNhomLamViecREF] DmNhomLamViecREF_tcdtmn,
                       [DmDiaDiemLamViecREF] DmDiaDiemLamViecREF_tcdtmn,
                       [DmKhachHangREF] DmKhachHangREF_tcdtmn,
                       [LstDmNhanHangREF] LstDmNhanHangREF_tcdtmn,
                       [LstDmNhomNganhREF] LstDmNhomNganhREF_tcdtmn,
                       [DmHinhThucQuangCaoREF] DmHinhThucQuangCaoREF_tcdtmn,
                       [DmChuyenMucREF] DmChuyenMucREF_tcdtmn,
                       [DmLoaiBannerREF] DmLoaiBannerREF_tcdtmn,
                       [DmViTriREF] DmViTriREF_tcdtmn,
                       [SoLuong] SoLuong_tcdtmn,
                       [DonViTinhREF] DonViTinhREF_tcdtmn,
                       [DonGia] DonGia_tcdtmn,
                       [ChietKhau] ChietKhau_tcdtmn,
                       [IsKhuyenMai] IsKhuyenMai_tcdtmn,
                       [KhuyenMai] KhuyenMai_tcdtmn,
                       [ThucChayMuaNgoaiChiTietREF] ThucChayMuaNgoaiChiTietREF,
                       [TongTienDuToanMuaSauCK] TongTienDuToanMuaSauCK_tcdtmn,
                       [TongTienDuToanLaiMuaSauCK] TongTienDuToanLaiMuaSauCK_tcdtmn,
                       [ChietKhauMua] ChietKhauMua_tcdtmn,
                       [DmBannerREF] DmBannerREF_tcdtmn,
                       [DmChienDichREF] DmChienDichREF_tcdtmn,
                       [DmWebsiteREF] DmWebsiteREF_tcdtmn,
                       [TenWebsite] TenWebsite_tcdtmn,
                       [NgayBatDau] NgayBatDau_tcdtmn,
                       [NgayKetThuc] NgayKetThuc_tcdtmn,
                       [DonViTinhThucChay] DonViTinhThucChay_tcdtmn,
                       [DonGiaTheoDonViTinhTC] DonGiaTheoDonViTinhTC_tcdtmn,
                       [TongViewClickThucChay] TongViewClickThucChay_tcdtmn,
                       [TongSoBaiVietChiPhiThucChay] TongSoBaiVietChiPhiThucChay_tcdtmn,
                       [SoLuongThucChay] SoLuongThucChay_tcdtmn,
                       [TongThanhTienThucChayBanSauCK] TongThanhTienThucChayBanSauCK_tcdtmn,
                       [TongThanhTienThucChayMuaSauCK] TongThanhTienThucChayMuaSauCK_tcdtmn,
                       [ThanhTienLaiThucChaySauCK] ThanhTienLaiThucChaySauCK_tcdtmn,
                       [ThanhTienLaiThucChayKM] ThanhTienLaiThucChayKM_tcdtmn,
                       [SoLuongThucChayKM] SoLuongThucChayKM_tcdtmn,
                       [SoLuongThucChayLechTreoHa] SoLuongThucChayLechTreoHa_tcdtmn,
                       [ThanhTienLechTreoHa] ThanhTienLechTreoHa_tcdtmn,
                       [GiaTriThayDoiLaiSauCK] GiaTriThayDoiLaiSauCK_tcdtmn,
                       [SoLuongThayDoi] SoLuongThayDoi_tcdtmn,
                       [SoLuongKMThayDoi] SoLuongKMThayDoi_tcdtmn,
                       [GiaTriKMLaiThayDoi] GiaTriKMLaiThayDoi_tcdtmn,
                       [GhiChu] GhiChu_tcdtmn,
                       [CreatedAt] CreatedAt_tcdtmn,
                       [LastModifiedAt] LastModifiedAt_tcdtmn
                FROM ThucChayDaTinh_MuaNgoai tcdt
                --where HopDongChiTietREF = 578571 and ThucChayMuaNgoaiChiTietREF = 23580
                WHERE DmChienDichREF = 0
                      AND tcdt.DmSanPhamREF <> 5184 --sp creatorcontent
            ) B
                ON A.ThucChayMuaNgoaiChiTietID = B.ThucChayMuaNgoaiChiTietREF
        WHERE 1 = 1 AND A.DmSanPhamREF <>5184
              AND NOT (
                          A.SoHopDong = B.SoHopDong_tcdtmn
                          OR A.DmMaHopDongREF = B.DmMaHopDongREF_tcdtmn
                          OR A.NgayDanhSoHopDong = B.NgayDanhSoHopDong_tcdtmn
                          OR A.TrangThaiHopDong = B.TrangThaiHopDong_tcdtmn
                          OR A.SysNhanVienREF = B.DmNhanVienREF_tcdtmn
                          OR A.TenDangNhap = B.TenDangNhap_tcdtmn
                          OR A.DmPhongBanREF = B.DmPhongBanREF_tcdtmn
                          OR A.DmBoPhanREF = B.DmBoPhanREF_tcdtmn
                          OR A.DmNhomLamViecREF = B.DmNhomLamViecREF_tcdtmn
                          OR A.DmDiaDiemLamViecREF = B.DmDiaDiemLamViecREF_tcdtmn
                          OR A.DmKhachHangREF = B.DmKhachHangREF_tcdtmn
                          OR A.HopDongChiTietID = B.HopDongChiTietREF
                          OR A.DanhSachNhanHangREF = B.LstDmNhanHangREF_tcdtmn
                          OR A.DmLoaiREF = B.DmHinhThucQuangCaoREF_tcdtmn
                          OR A.DmSanPhamREF = B.DmSanPhamREF_tcdtmn
                          OR A.DmChuyenMucREF = B.DmChuyenMucREF_tcdtmn
                          OR A.DmLoaiBannerREF = B.DmLoaiBannerREF_tcdtmn
                          OR A.DmViTriREF = B.DmViTriREF_tcdtmn
                          OR A.SoLuong = B.SoLuong_tcdtmn
                          OR A.DonViTinhREF = B.DonViTinhREF_tcdtmn
                          OR A.DonGia = B.DonGia_tcdtmn
                          OR A.ChietKhau = B.ChietKhau_tcdtmn
                          --OR A.ThanhTien = B.ThanhTien_tcdtmn
                          OR A.IsKhuyenMai = B.IsKhuyenMai_tcdtmn
                          OR A.KhuyenMai = B.KhuyenMai_tcdtmn
                          --OR A.DmWebsiteREF = B.DmWebsiteREF
                          OR A.TenWebsite = B.TenWebsite_tcdtmn
                          OR A.ThanhTienSauCKMua = B.TongThanhTienThucChayMuaSauCK_tcdtmn
                          OR A.ThanhTienLaiSauCK = B.TongTienDuToanLaiMuaSauCK_tcdtmn
                          OR A.ThucChayMuaNgoaiChiTietID = B.ThucChayMuaNgoaiChiTietREF
                          OR A.ChietKhauMuaNgoai = B.ChietKhauMua_tcdtmn
                          OR CONVERT(DATE, A.NgayChot) = B.NgayThucHien
                          --OR A.TuNgay = B.NgayBatDau
                          --OR A.DenNgay=B.NgayKetThuc
                          OR A.DmDonViTinhREF = B.DonViTinhThucChay_tcdtmn
                          OR A.SoLuongThucChay = B.SoLuongThucChay_tcdtmn
                          OR A.ThanhTienThucChayBanSauCK = B.TongThanhTienThucChayBanSauCK_tcdtmn
                          OR A.ThanhTienLaiThucChaySauCK = B.ThanhTienLaiThucChaySauCK_tcdtmn
                          OR A.TongThanhTienThucChayMuaSauCK = B.TongThanhTienThucChayMuaSauCK_tcdtmn
                          OR A.DonGiaTheoDonViTinhTC = B.DonGiaTheoDonViTinhTC_tcdtmn
                      )
              OR A.SoHopDong IS NULL
              OR B.SoHopDong_tcdtmn IS NULL
    ) tc
    WHERE NOT (
                  tc.NgayChot IS NULL
                  AND tc.NgayThucHien < @NgayThucHien
              );
    --order by B.NgayThucHien desc


    ---Kiem tra website
    -- select * from WebsiteMapping_HDCN_Reporting where WebsiteLink = 'ictnews.vn'
    SELECT A.DmWebsiteREF,
           A.TenWebsite,
           B.*
    FROM
    (
        SELECT tcmn.ThucChayMuaNgoaiChiTietID,
               hdct.DmWebsiteREF,
               hdct.TenWebsite
        FROM ThucChayMuaNgoaiChiTiet tcmn
            INNER JOIN HopDongChiTiet_MuaNgoai hdctmn
                ON tcmn.HopDongChiTietREF = hdctmn.HopDongChiTietID
            INNER JOIN HopDongChiTiet hdct
                ON hdctmn.HopDongChiTietID = hdct.HopDongChiTietID
            INNER JOIN HopDong hd
                ON hdct.HopDongFK = hd.HopDongID
        WHERE 1 = 1
              AND hdct.DeletedStatus = 0
              AND tcmn.DeletedStatus = 0
              AND hdctmn.DeletedStatus = 0
              AND tcmn.DeletedStatus = 0
              AND tcmn.TrangThaiTinhThucChay = 1
              AND
              (
                  hdct.DmLoaiREF = 13
                  OR hdct.DmLoaiBannerREF = 18
              )
			  AND hdct.DmSanPhamREF <>5184
    ) A
        LEFT JOIN
        (
            SELECT [ThucChayMuaNgoaiChiTietREF],
                   [DmWebsiteREF],
                   [TenWebsite],
                   web.DmWebsiteID,
                   web.DmWebsiteReportingdbID,
                   web.WebsiteLink,
                   NgayThucHien,
				   tcdt.DmSanPhamREF
            FROM ThucChayDaTinh_MuaNgoai tcdt
                INNER JOIN WebsiteMapping_HDCN_Reporting web
                    ON tcdt.TenWebsite = web.WebsiteLink
            WHERE NgayThucHien = @NgayThucHien
                  AND DmChienDichREF = 0
        ) B
            ON A.ThucChayMuaNgoaiChiTietID = B.ThucChayMuaNgoaiChiTietREF
    WHERE 1 = 1
          AND NOT A.DmWebsiteREF = B.DmWebsiteID
		   AND B.DmSanPhamREF <> 5184;
END;

```
