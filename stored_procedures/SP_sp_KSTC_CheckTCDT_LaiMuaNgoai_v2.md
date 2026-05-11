# Stored Procedure: `sp_KSTC_CheckTCDT_LaiMuaNgoai_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-06 15:17:08.707000
- **Ngày sửa cuối**: 2022-12-30 17:07:59.257000

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
--EXEC sp_KSTC_CheckTCDT_LaiMuaNgoai_v2 '2021-05-29'
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_LaiMuaNgoai_v2]
    -- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    ---------------check dữ liệu lãi mua ngoài-----------
    SELECT TT.*,
           B.*
    FROM
    (
        SELECT A.*
        FROM
        (
            SELECT dbo.GetSoHopDongByID(c.HopDongFK) SHD,
                   c.HopDongFK,
                   a.HopDongChiTietID,
                   c.DmSanPhamREF,
                   b.ThucChayMuaNgoaiChiTietID,
                   b.LastModifiedAt LastModifiedAt_TCM,
                   c.TenLoai,
                   c.TenSanPham,
                   c.TenWebsite,
                   c.TenLoaiBanner,
                   c.SoLuong,
                   c.DonViTinh,
                   c.DonGia,
                   dbo.FormatNumber(c.ThanhTien) DuToanBan,
                   dbo.FormatNumber(a.ThanhTienSauCKMua) DuToanMua,
                   b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100 ThucChayMua,
                   (b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100) + ThanhTienLaiSauCK
                   * ((b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100)) / a.ThanhTienSauCKMua tctt,
                   --(CASE
                   --     WHEN a.ThanhTienSauCKMua <> 0 THEN
                   --         b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100
                   --         * (c.ThanhTien - a.ThanhTienSauCKMua) / a.ThanhTienSauCKMua
                   --     ELSE
                   --         b.ThanhTienLaiThucChaySauCK -- -999999999
                   -- END
                   --) LaiTT
				   b.ThanhTienLaiThucChaySauCK LaiTT
            FROM HopDongChiTiet_MuaNgoai a --
                INNER JOIN ThucChayMuaNgoaiChiTiet b
                    ON a.HopDongChiTietID = b.HopDongChiTietREF
                       AND b.DeletedStatus = 0
                INNER JOIN HopDongChiTiet c
                    ON a.HopDongChiTietID = c.HopDongChiTietID
                INNER JOIN HopDong hd
                    ON HopDongID = b.HopDongREF
            WHERE 1 = 1
                  AND a.DeletedStatus = 0
                  AND
                  (
                      DmLoaiREF = 13
                      OR DmLoaiBannerREF = 18
                  )
                  AND c.DeletedStatus = 0
                  AND a.ThanhTienSauCKMua <> 0
                  AND c.HopDongFK NOT IN ( 1001985 ) --hd test
                  AND HopDongChiTietREF NOT IN
                      (
                          SELECT HopDongChiTietID FROM MuaNgoaiChot_TinhBoSung_2016
                      )
                  AND HopDongChiTietREF IN
                      (
                          SELECT HopDongChiTietREF
                          FROM ThucChayDaTinh tdct
                          WHERE YEAR(tdct.NgayThucHien) >= 2021
                                AND
                                (
                                    tdct.DmLoaiBannerREF = 18
                                    OR tdct.DmHinhThucQuangCao = 42
                                )
                      )
                  AND TrangThaiHopDong <> 3
                  AND b.Status IN ( 2, 1, 4 )
                  AND CONVERT(DATE, b.LastModifiedAt) <= @NgayThucHien
        ) A
    ) TT
        FULL OUTER JOIN
        (
            SELECT SoHopDong,
                   HopDongREF,
                   HopDongChiTietREF,
                   --DmSanPhamREF,
                   ThucChayMuaNgoaiChiTietREF,
                   ROUND(SUM(TongThanhTienThucChayBanSauCK), 0) BanCK,
                   ROUND(SUM(ThanhTienLaiThucChaySauCK + GiaTriThayDoiLaiSauCK), 0) LaiThucChay
            FROM ThucChayDaTinh_MuaNgoai
            WHERE 1 = 1
                  AND TrangThaiHopDong <> 3
                  AND HopDongChiTietREF IN
                      (
                          SELECT HopDongChiTietREF
                          FROM ThucChayDaTinh
                          WHERE YEAR(NgayThucHien) >= 2021
                                AND
                                (
                                    DmLoaiBannerREF = 18
                                    OR DmHinhThucQuangCao = 42
                                )
                      )
                  AND HopDongChiTietREF NOT IN ( 580018, 605804, 605805, 535431 --hd cũ done thực chạy rồi
                                               )
                  AND DmChienDichREF = 0
            GROUP BY SoHopDong,
                     HopDongREF,
                     HopDongChiTietREF,
                     --DmSanPhamREF,
                     ThucChayMuaNgoaiChiTietREF
        ) B
            ON TT.HopDongChiTietID = B.HopDongChiTietREF              AND TT.ThucChayMuaNgoaiChiTietID = B.ThucChayMuaNgoaiChiTietREF
			JOIN ASDAG2.PMS.dbo.B_QuanLyThucChay C ON c.PhanBoId=b.HopDongChiTietREF
    WHERE 1 = 1
          AND B.HopDongChiTietREF NOT IN ( 535431 ) --hd cũ done thực chạy rồi  
          AND
          (
              TT.HopDongFK IS NULL
              OR B.HopDongREF IS NULL
              OR TT.HopDongChiTietID IS NULL
              OR B.HopDongChiTietREF IS NULL
              OR TT.ThucChayMuaNgoaiChiTietID IS NULL
              OR B.ThucChayMuaNgoaiChiTietREF IS NULL
              OR ABS(ISNULL(TT.LaiTT, 0) - ISNULL(B.LaiThucChay, 0)) > 1000
          )
          AND NOT (
                      TT.HopDongFK IS NULL
                      AND B.LaiThucChay = 0
                  )
		AND CONVERT(DATE,C.LastModificationTime) < CONVERT(DATE,GETDATE())
    ORDER BY TT.HopDongFK DESC;

END;

```
