# Stored Procedure: `CheckThucChayVuotHopDong_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-08 10:27:27.470000
- **Ngày sửa cuối**: 2025-12-05 11:15:05.257000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiCheck` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC CheckThucChayVuotHopDong_v2 '2018-08-06',3
--b1. tao bang contract, lay du lieu cac hd tu nam 2015
--EXEC CheckThucChayVuotHopDong_TableHopDong

--b2. tao bang thucchaydatinh, lay du lieu cac hd tu nam 2015
--EXEC CheckThucChayVuotHopDong_TableTCDT '2020-11-31','2020-07-31'

--b3. Check vuot
--EXEC CheckThucChayVuotHopDong_v2 '2020-11-24', 3

CREATE PROCEDURE [dbo].[CheckThucChayVuotHopDong_v2]
    @NgayThucHien DATETIME,
    @LoaiCheck INT --1: Theo San pham,	                
-- 2: theo san pham, phan bo và HTQC
-- 4: HopDong,SanPham,HinhThucQuangcao
--141: PR
--42: Admatic
AS
BEGIN
    SET NOCOUNT ON;  -- thêm, không ảnh hưởng logic

    -------------list hợp đồng ký Branding - nhiều sản phẩm
    DECLARE @table_733 TABLE
    (
        Sohopdong NVARCHAR(100),
        Hopdongchitietid INT
    );
    INSERT INTO @table_733
    (
        Sohopdong,
        Hopdongchitietid
    )
    SELECT SoHopDong,
           HopDongChiTietID
    FROM KS_ThucChay_HopDong
    WHERE DmLoaiREF = 5001
          AND DmSanPhamREF = 733;


    ------------------------------


    IF @LoaiCheck = 1
    BEGIN
        --------------Check all hop dong -----------------
        /*
SELECT A.*, B.*, A.ThanhTien -B.ThanhTienThucChay FROM (
SELECT SoHopDong,
HopDongID,
SUM(ThanhTien)ThanhTien,
SUM(ThanhTienKhuyenMai)ThanhTienKhuyenMai
FROM KS_ThucChay_HopDong  where Nam >=2017
GROUP BY SoHopDong,
HopDongID
)A
FULL OUTER JOIN 
(
SELECT SoHopDong,
Nam,
HopDongID,
SUM(ThanhTienThucChay)ThanhTienThucChay ,
SUM(ThanhTienThucChayKM)ThanhTienThucChayKM
FROM KS_ThucChay_TCDT where Nam >=2017
GROUP BY 
SoHopDong,
Nam,
HopDongID
)B
ON A.HopDongID = B.HopDongID
WHERE A.ThanhTien - B.ThanhTienThucChay  <-10
ORDER BY  A.HopDongID desc
*/
        --------------Check theo hop dong va san pham không gồm mua ngoài -----------------

        SELECT A.*,
               B.*,
               dbo.FormatNumber(A.ThanhTien - B.ThanhTienThucChay)
        FROM
        (
            SELECT SoHopDong,
                   HopDongID,				
                   DmSanPhamREF,
                   b.TenSanPham,
                   SUM(ThanhTien) ThanhTien,
                   SUM(ThanhTienKhuyenMai) ThanhTienKhuyenMai,
                   MAX(a.LastModifiedAt) LastModifiedAt
            FROM KS_ThucChay_HopDong a
                LEFT JOIN dbo.DmSanPham b
                    ON a.DmSanPhamREF = b.DmSanPhamID
            WHERE DmLoaiREF <> 42
                  AND NOT (
                              a.DmLoaiREF = 13
                              OR a.DmLoaiBannerREF = 18
                          )
                  AND YEAR(a.LastModifiedAt) >= 2021
                  AND a.SoHopDong NOT IN
                      (
                          SELECT Sohopdong FROM @table_733
                      )
            GROUP BY SoHopDong,
                     Nam,
                     TrangThaiHopDong,
                     HopDongID,				
                     DmSanPhamREF,
                     b.TenSanPham
        ) A
            FULL OUTER JOIN
            (
                SELECT a.SoHopDong,
                       a.Nam,
                       a.HopDongID,					
                       DmSanPhamREF,
                       b.TenSanPham,
                       SUM(a.ThanhTienThucChay) ThanhTienThucChay,
                       SUM(a.ThanhTienThucChayKM) ThanhTienThucChayKM
                FROM KS_ThucChay_TCDT a
                    INNER JOIN HopDong hd
                        ON a.HopDongID = hd.HopDongID
                    LEFT JOIN dbo.DmSanPham b
                        ON a.DmSanPhamREF = b.DmSanPhamID
                WHERE DmHinhThucQuangCao <> 42
                      AND NOT (
                                  a.DmHinhThucQuangCao = 13
                                  OR a.DmLoaiBannerREF = 18
                              )
                      AND a.Nam >= 2017
                      AND YEAR(hd.LastModifiedAt) >= 2021
                      AND a.SoHopDong NOT IN
                          (
                              SELECT Sohopdong FROM @table_733
                          )
                GROUP BY a.SoHopDong,
                         a.Nam,
                         a.HopDongID,						
                         DmSanPhamREF,
                         b.TenSanPham
                HAVING ROUND(SUM(a.ThanhTienThucChay), 0) <> 0
            ) B
                ON A.HopDongID = B.HopDongID
                   AND A.DmSanPhamREF = B.DmSanPhamREF
        WHERE 1 = 1
              AND
              (
                  NOT (
                          A.ThanhTien = 0
                          AND B.ThanhTienThucChay = 0
                      )
                  AND NOT (
                              A.ThanhTien <> 0
                              AND B.ThanhTienThucChay IS NULL
                          )
                  AND NOT (A.ThanhTien = B.ThanhTienThucChay)
                  AND A.ThanhTien - B.ThanhTienThucChay < -10
              )
              OR
              (
                  A.DmSanPhamREF IS NULL
                  OR A.HopDongID IS NULL
              )
        ORDER BY A.LastModifiedAt DESC;
    END;

    ELSE IF @LoaiCheck = 2
    ---------------Check vuot theo phan bo, sanpham, HTQC-----------
    BEGIN
        SELECT A.*,
               B.*,
                dbo.FormatNumber(A.ThanhTien - B.ThanhTienThucChay)
        FROM
        (
            SELECT SoHopDong,
                   HopDongID,
                   HopDongChiTietID,
                   DmLoaiREF,
                   a.DmLoaiBannerREF,
                   DmSanPhamREF,
                   b.TenSanPham,
                   SUM(ThanhTien) ThanhTien,
                   SUM(ThanhTienKhuyenMai) ThanhTienKhuyenMai,
                   a.LastModifiedAt
            FROM KS_ThucChay_HopDong a
                LEFT JOIN dbo.DmSanPham b
                    ON a.DmSanPhamREF = b.DmSanPhamID
            WHERE DmSanPhamREF NOT IN ( 141, 637, 305 )
                  AND NOT (
                              a.DmLoaiREF = 13
                              OR a.DmLoaiBannerREF = 18
                          )
                  AND DmLoaiREF <> 42
                  AND Nam >= 2017
                  AND a.HopDongChiTietID NOT IN
                      (
                          SELECT Hopdongchitietid FROM @table_733
                      )
                  AND a.HopDongChiTietID NOT IN ( 515063, 504682, 504068 ) -- hợp đồng năm cũ không xử lý
            GROUP BY SoHopDong,
                     HopDongID,
                     HopDongChiTietID,
                     DmLoaiREF,
                     a.DmLoaiBannerREF,
                     DmSanPhamREF,
                     b.TenSanPham,
                     a.LastModifiedAt
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       HopDongChiTietID,
                       DmHinhThucQuangCao,
                       a.DmLoaiBannerREF,
                       DmSanPhamREF,
                       b.TenSanPham,
                       SUM(ThanhTienThucChay) ThanhTienThucChay,
                       SUM(ThanhTienThucChayKM) ThanhTienThucChayKM
                FROM KS_ThucChay_TCDT a
                    LEFT JOIN dbo.DmSanPham b
                        ON a.DmSanPhamREF = b.DmSanPhamID
                WHERE DmSanPhamREF NOT IN ( 141, 637, 305 )
                      AND NOT (
                                  a.DmHinhThucQuangCao = 13
                                  OR a.DmLoaiBannerREF = 18
                              )
                      AND DmHinhThucQuangCao <> 42
                      AND Nam >= 2017
                      AND a.HopDongChiTietID NOT IN
                          (
                              SELECT Hopdongchitietid FROM @table_733
                          )
                      AND a.HopDongChiTietID NOT IN ( 515063, 504682, 504068 ) -- hợp đồng năm cũ không xử lý
                GROUP BY SoHopDong,
                         HopDongID,
                         HopDongChiTietID,
                         DmHinhThucQuangCao,
                         a.DmLoaiBannerREF,
                         DmSanPhamREF,
                         b.TenSanPham
                HAVING ROUND(SUM(ThanhTienThucChay), 0) <> 0
            ) B
                ON A.HopDongID = B.HopDongID
                   AND A.HopDongChiTietID = B.HopDongChiTietID
                   AND A.DmSanPhamREF = B.DmSanPhamREF
                   AND A.DmLoaiREF = B.DmHinhThucQuangCao
        --AND A.DmLoaiBannerREF = B.DmLoaiBannerREF
        WHERE 1 = 1 --A.ThanhTien - B.ThanhTienThucChay  <-10
			AND A.HopDongChiTietID NOT IN (549698,572639) --duongnt - 09-06-2023 - bỏ qua phân bổ vượt cũ từ 2020 
              AND
              (
                  NOT (
                          A.ThanhTien = 0
                          AND B.ThanhTienThucChay = 0
                      )
                  AND NOT (
                              A.ThanhTien <> 0
                              AND B.ThanhTienThucChay IS NULL
                          )
                  AND NOT (A.ThanhTien = B.ThanhTienThucChay)
                  AND A.ThanhTien - B.ThanhTienThucChay < -10
              )
              OR A.DmSanPhamREF IS NULL
              OR A.HopDongID IS NULL
              OR A.DmLoaiREF IS NULL
              OR A.HopDongChiTietID IS NULL
              OR A.HopDongID IS NULL
              OR A.DmLoaiBannerREF IS NULL
        --OR B.DmSanPhamREF IS NULL OR B.HopDongID IS NULL or B.DmHinhThucQuangCao is null or B.HopDongChiTietID is null or B.HopDongID is null or B.DmLoaiBannerREF is null
        ORDER BY A.LastModifiedAt DESC,
                 A.DmSanPhamREF,
                 A.DmLoaiBannerREF,
                 A.HopDongID DESC;
    END;
    --------------Check vuot  Mua ngoài -----------------
    ELSE IF @LoaiCheck = 13
    BEGIN

        SELECT A.*,
               B.*,
              dbo.FormatNumber( A.ThanhTien - B.ThanhTienThucChay)
        FROM
        (
            SELECT SoHopDong,
                   HopDongID,
                   HopDongChiTietID,
                   DmSanPhamREF,
                   b.TenSanPham,
                   SUM(ThanhTien) ThanhTien,
                   SUM(ThanhTienKhuyenMai) ThanhTienKhuyenMai,
                   a.LastModifiedAt
            FROM KS_ThucChay_HopDong a
                LEFT JOIN dbo.DmSanPham b
                    ON a.DmSanPhamREF = b.DmSanPhamID
            WHERE (
                      DmLoaiREF = 13
                      OR DmLoaiBannerREF = 18
                  )
            --AND a.HopDongChiTietID = 544923
            GROUP BY SoHopDong,
                     HopDongID,
                     HopDongChiTietID,
                     DmSanPhamREF,
                     TenSanPham,
                     a.LastModifiedAt
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       HopDongChiTietID,
                       DmSanPhamREF,
                       b.TenSanPham,
                       SUM(SoLuongThucChay) SoLuongThucChay,
                       SUM(ThanhTienThucChay) ThanhTienThucChay,
                       SUM(ThanhTienThucChayKM) ThanhTienThucChayKM
                FROM KS_ThucChay_TCDT a
                    LEFT JOIN dbo.DmSanPham b
                        ON a.DmSanPhamREF = b.DmSanPhamID
                WHERE (
                          DmHinhThucQuangCao = 13
                          OR DmLoaiBannerREF = 18
                      )
                      AND a.Nam >= 2017
                --AND a.HopDongChiTietID = 544923
                GROUP BY SoHopDong,
                         HopDongID,
                         HopDongChiTietID,
                         DmSanPhamREF,
                         TenSanPham
                HAVING ROUND(SUM(ThanhTienThucChay), 0) <> 0
            ) B
                ON A.HopDongID = B.HopDongID
                   AND A.HopDongChiTietID = B.HopDongChiTietID
                   AND A.DmSanPhamREF = B.DmSanPhamREF
        WHERE ((ISNULL(A.ThanhTien, 0) - ISNULL(B.ThanhTienThucChay, 0) < -13)
              OR
              (
                  A.DmSanPhamREF IS NULL
                  OR A.HopDongChiTietID IS NULL
              ))
			AND A.SoHopDong NOT IN (N'QC1971218',N'QC7321217') ----duongnt - 09-06-2023 bỏ qua 4 row hđ cũ: QC1971218;QC7321217
        ORDER BY A.LastModifiedAt DESC;
    END;
    --------------Check vuot  PR, Tuyen bai, Adpage -----------------
    ELSE IF @LoaiCheck = 141
    BEGIN
        SELECT A.*,
               B.*,
              dbo.FormatNumber( A.ThanhTien - B.ThanhTienThucChay)
        FROM
        (
            SELECT SoHopDong,
                   HopDongID,
                   DmSanPhamREF,
                   SUM(ThanhTien) ThanhTien,
                   SUM(ThanhTienKhuyenMai) ThanhTienKhuyenMai,
                   MAX(LastModifiedAt) LastModifiedAt
            FROM KS_ThucChay_HopDong
            WHERE DmSanPhamREF IN ( 141, 637, 305 )
                  AND NOT (
                              DmLoaiREF = 13
                              OR DmLoaiBannerREF = 18
                          )
            GROUP BY SoHopDong,
                     HopDongID,
                     DmSanPhamREF
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       DmSanPhamREF,
                       SUM(SoLuongThucChay) SoLuongThucChay,
                       SUM(ThanhTienThucChay) ThanhTienThucChay,
                       SUM(ThanhTienThucChayKM) ThanhTienThucChayKM
                FROM KS_ThucChay_TCDT
                WHERE DmSanPhamREF IN ( 141, 637, 305 )
                      AND NOT (
                                  DmHinhThucQuangCao = 13
                                  OR DmLoaiBannerREF = 18
                              )
                GROUP BY SoHopDong,
                         HopDongID,
                         DmSanPhamREF
            ) B
                ON A.HopDongID = B.HopDongID
                   AND A.DmSanPhamREF = B.DmSanPhamREF
        WHERE A.ThanhTien - B.ThanhTienThucChay < -5
		AND A.SoHopDong NOT IN (N'QC0470317',N'DT1981216') --duongnt - 09-06-2023 bỏ qua hợp đồng cũ
        ORDER BY A.LastModifiedAt DESC,
                 A.DmSanPhamREF,
                 A.HopDongID DESC;
    END;

    --------------Check vuot  PR, Tuyen bai, Adpage theo phan bo -----------------
    ELSE IF @LoaiCheck = 1412
    BEGIN
        SELECT A.*,
               B.*,
             dbo.FormatNumber( A.ThanhTien - B.ThanhTienThucChay)
        FROM
        (
            SELECT SoHopDong,
                   HopDongID,
                   HopDongChiTietID,
                   DmSanPhamREF,
                   SUM(ThanhTien) ThanhTien,
                   SUM(ThanhTienKhuyenMai) ThanhTienKhuyenMai,
                   LastModifiedAt
            FROM KS_ThucChay_HopDong
            WHERE DmSanPhamREF IN ( 141, 637, 305 )
                  AND NOT (
                              DmLoaiBannerREF = 18
                              OR DmLoaiREF = 13
                          )
                  AND Nam >= 2020
            GROUP BY SoHopDong,
                     HopDongID,
                     HopDongChiTietID,
                     DmSanPhamREF,
                     LastModifiedAt
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       HopDongChiTietID,
                       DmSanPhamREF,
                       SUM(SoLuongThucChay) SoLuongThucChay,
                       SUM(ThanhTienThucChay) ThanhTienThucChay,
                       SUM(ThanhTienThucChayKM) ThanhTienThucChayKM
                FROM KS_ThucChay_TCDT
                WHERE DmSanPhamREF IN ( 141, 637, 305 )
                      AND NOT (
                                  DmLoaiBannerREF = 18
                                  OR DmHinhThucQuangCao = 13
                              )
                      AND Nam >= 2020
                GROUP BY SoHopDong,
                         HopDongID,
                         HopDongChiTietID,
                         DmSanPhamREF
            ) B
                ON A.HopDongID = B.HopDongID
                   AND A.HopDongChiTietID = B.HopDongChiTietID
                   AND A.DmSanPhamREF = B.DmSanPhamREF
        WHERE A.ThanhTien - B.ThanhTienThucChay < -10
        ORDER BY A.LastModifiedAt DESC,
                 A.DmSanPhamREF,
                 A.HopDongID;
    END;
    --------------Check vuot  admatic -----------------
    ELSE IF @LoaiCheck = 42
    BEGIN

        SELECT A.*,
               B.*,
              dbo.FormatNumber( A.ThanhTien - B.ThanhTienThucChay)
        FROM
        (
            SELECT SoHopDong,
                   HopDongID,
                   tc.HopDongChiTietID,
                   hdct.LastModifiedAt,
                   SUM(tc.ThanhTien) ThanhTien,
                   SUM(tc.ThanhTienKhuyenMai) ThanhTienKhuyenMai
            FROM KS_ThucChay_HopDong tc
                INNER JOIN HopDongChiTiet hdct
                    ON tc.HopDongChiTietID = hdct.HopDongChiTietID
            WHERE tc.DmLoaiREF = 42
                  AND NOT (
                              tc.DmLoaiREF = 13
                              OR tc.DmLoaiBannerREF = 18
                          )
                  AND YEAR(hdct.LastModifiedAt) >= 2021
                  AND hdct.HopDongChiTietID NOT IN ( 558428 ) --- lệch ít, hợp đồng năm cũ không xử lý
            GROUP BY SoHopDong,
                     tc.HopDongID,
                     tc.HopDongChiTietID,
                     tc.DmSanPhamREF,
                     hdct.LastModifiedAt
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       HopDongChiTietID,
                       DmHinhThucQuangCao,
                       SUM(SoLuongThucChay) SoLuongThucChay,
                       SUM(ThanhTienThucChay) ThanhTienThucChay,
                       SUM(ThanhTienThucChayKM) ThanhTienThucChayKM
                FROM KS_ThucChay_TCDT
                WHERE DmHinhThucQuangCao = 42
                      AND NOT (
                                  DmHinhThucQuangCao = 13
                                  OR DmLoaiBannerREF = 18
                              )
                      AND HopDongChiTietID NOT IN ( 558428 ) --- lệch ít, hợp đồng năm cũ không xử lý
                GROUP BY SoHopDong,
                         HopDongID,
                         HopDongChiTietID,
                         DmHinhThucQuangCao
            ) B
                ON A.HopDongID = B.HopDongID
                   AND A.HopDongChiTietID = B.HopDongChiTietID
        WHERE A.ThanhTien - B.ThanhTienThucChay < -10
        ORDER BY A.LastModifiedAt DESC;
    END;

    -------------Check branding - nhiều sản phẩm

    ELSE IF @LoaiCheck = 733
    BEGIN
        SELECT A.*,
               B.*,
              dbo.FormatNumber( A.ThanhTien - B.ThanhTienThucChay)
        FROM
        (
            SELECT SoHopDong,
                   HopDongID,
                   tc.HopDongChiTietID,
                   hdct.LastModifiedAt,
                   SUM(tc.ThanhTien) ThanhTien,
                   SUM(tc.ThanhTienKhuyenMai) ThanhTienKhuyenMai
            FROM KS_ThucChay_HopDong tc
                INNER JOIN HopDongChiTiet hdct
                    ON tc.HopDongChiTietID = hdct.HopDongChiTietID
            WHERE tc.HopDongChiTietID IN
                  (
                      SELECT Hopdongchitietid FROM @table_733
                  )
            GROUP BY SoHopDong,
                     tc.HopDongID,
                     tc.HopDongChiTietID,
                     tc.DmSanPhamREF,
                     hdct.LastModifiedAt
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongID,
                       HopDongChiTietID,
                       DmHinhThucQuangCao,
                       SUM(SoLuongThucChay) SoLuongThucChay,
                       SUM(ThanhTienThucChay) ThanhTienThucChay,
                       SUM(ThanhTienThucChayKM) ThanhTienThucChayKM
                FROM KS_ThucChay_TCDT
                WHERE HopDongChiTietID IN
                      (
                          SELECT Hopdongchitietid FROM @table_733
                      )
                GROUP BY SoHopDong,
                         HopDongID,
                         HopDongChiTietID,
                         DmHinhThucQuangCao
            ) B
                ON A.HopDongID = B.HopDongID
                   AND A.HopDongChiTietID = B.HopDongChiTietID
        WHERE A.ThanhTien - B.ThanhTienThucChay < -10
        ORDER BY A.LastModifiedAt DESC;
    END;
    --------------Check inventory -----------------
    ELSE IF @LoaiCheck = 3
    BEGIN
        SELECT A.*,
               B.*,
               (ISNULL(A.ThanhTien, 0) - ISNULL(B.tttc, 0)) [LechTT-TC]
        FROM
        (
            SELECT hd.TrangThaiHopDong,
                   hd.SoHopDong,
                   hdct.HopDongChiTietID,
                   hdct.DmSanPhamREF,
                   hdct.DeletedStatus,

                   -- ✅ CỘT MỚI: phân bổ này đã treo ở ThucChayHopDongChiTiet hay chưa
                   CASE 
                       WHEN EXISTS (
                            SELECT 1
                            FROM ThucChayHopDongChiTiet t
                            WHERE t.HopDongChiTietREF = hdct.HopDongChiTietID
                              AND t.DeletedStatus = 0     -- chỉ tính bản ghi còn hiệu lực
                       ) THEN 1
                       ELSE 0
                   END AS CoTreo,

                   (CASE                      	
                        WHEN hdct.DeletedStatus = 1 THEN
                            0
                        WHEN hd.TrangThaiHopDong = 3 THEN
                            0
                        WHEN hdct.DeletedStatus = 0 THEN
                            hdct.ThanhTien
                        WHEN hd.TrangThaiHopDong IN ( 1, 2 ) THEN
                            hdct.ThanhTien
                    END
                   ) ThanhTien
            FROM DmThongTinHopDongBanInventory hdI
                INNER JOIN HopDongChiTiet hdct
                    INNER JOIN HopDong hd
                        ON hdct.HopDongFK = HopDongID
                    ON hdI.HopDongChiTietREF = hdct.HopDongChiTietID
                       AND RIGHT(hdI.SoHopDong, 2) >= '20'
                       AND hdI.HopDongChiTietREF NOT IN ( 599379, 596942 )
                       --and hd.sohopdong ='QC8380319'
                       AND hdct.DmSanPhamREF <> 733
        --and hdct.DeletedStatus = 1
        ) A
            FULL OUTER JOIN
            (
                SELECT SoHopDong,
                       HopDongChiTietID,
                       DmSanPhamREF,
                       SUM(ThanhTienThucChay) AS tttc
                FROM KS_ThucChay_TCDT_Inventory
                WHERE 1 = 1
                      AND Nam >= 2020
                      --and SoHopDong = 'QC8380319'
                      --and DmSanPhamREF <> 733
					   AND HopDongChiTietID IN
                          (
                              SELECT HopDongChiTietREF
                              FROM DmThongTinHopDongBanInventory
                              WHERE DmSanPhamREF <> 733
                          )
                      AND HopDongChiTietID NOT IN ( 599379, 596942, 591259, 610723, 610769 )					 
                GROUP BY SoHopDong,
                         HopDongChiTietID,
                         DmSanPhamREF
                HAVING ROUND(SUM(ThanhTienThucChay), 0) <> 0
            ) B
                ON A.HopDongChiTietID = B.HopDongChiTietID
                   AND (A.DmSanPhamREF = B.DmSanPhamREF)
        WHERE 1 = 1
              AND
              (
                  A.HopDongChiTietID IS NULL
                  OR B.HopDongChiTietID IS NULL
                  OR A.DmSanPhamREF IS NULL
                  OR B.DmSanPhamREF IS NULL
                  OR ABS(A.ThanhTien - ISNULL(B.tttc, 0)) > 10
              )
              AND NOT (
                          A.ThanhTien = 0
                          AND B.tttc IS NULL
                      )
              AND A.CoTreo = 1       -- 🔴 CHỈ LẤY NHỮNG PHÂN BỔ ĐÃ TREO
        ORDER BY A.HopDongChiTietID;

       -------------------nhieu san pham-----------------
		SELECT 
			   'NhieuSanPham' AS Loai,
			   A.TrangThaiHopDong,
			   A.SoHopDong,
			   A.HopDongChiTietID,
			   A.DmSanPhamREF,          -- đây là mã 733 ở HopDongChiTiet (gói nhiều sản phẩm)
			   A.DeletedStatus,
			   A.ThanhTien,             -- tiền trên hợp đồng (733)
			   B.tttc,                  -- TỔNG tiền thực chạy (gộp 342 + 598 + ... nếu có)
			   (ISNULL(A.ThanhTien, 0) - ISNULL(B.tttc, 0)) AS [LechTT-TC]
		FROM
		(
			SELECT hd.TrangThaiHopDong,
				   hd.SoHopDong,
				   hdct.HopDongChiTietID,
				   hdct.DmSanPhamREF,
				   hdct.DeletedStatus,
				   (CASE
						WHEN hdct.DeletedStatus = 1 THEN 0
						WHEN hd.TrangThaiHopDong = 3 THEN 0
						WHEN hdct.DeletedStatus = 0 THEN hdct.ThanhTien
						WHEN hd.TrangThaiHopDong IN (1, 2) THEN hdct.ThanhTien
					END
				   ) AS ThanhTien
			FROM DmThongTinHopDongBanInventory hdI
				INNER JOIN HopDongChiTiet hdct
					INNER JOIN HopDong hd
						ON hdct.HopDongFK = hd.HopDongID
					ON hdI.HopDongChiTietREF = hdct.HopDongChiTietID
					   --and right(hdI.SoHopDong,2) >='20'
					   AND hdI.HopDongChiTietREF NOT IN (599379, 596942)
					   --and hdct.HopDongChiTietID =610769
					   AND hdct.DmSanPhamREF = 733         -- NHIỀU SẢN PHẨM
			--and hdct.DeletedStatus = 1
		) A
		FULL OUTER JOIN
		(
			-- B: gộp tất cả sản phẩm con (342, 598, ...) về 1 dòng / HopDongChiTietID
			SELECT 
				   SoHopDong,
				   HopDongChiTietID,
				   SUM(ThanhTienThucChay) AS tttc
			FROM KS_ThucChay_TCDT_Inventory
			WHERE 1 = 1
				  --AND Nam >= 2020
				  --and SoHopDong = 'QC9631220'
				  AND HopDongChiTietID IN
					  (
						  SELECT HopDongChiTietREF
						  FROM DmThongTinHopDongBanInventory
						  WHERE DmSanPhamREF = 733   -- các phân bổ nhiều sản phẩm
					  )
				  AND HopDongChiTietID NOT IN (599379, 596942)
			GROUP BY SoHopDong,
					 HopDongChiTietID
			HAVING ROUND(SUM(ThanhTienThucChay), 0) <> 0
		) B
			ON A.HopDongChiTietID = B.HopDongChiTietID
		WHERE 1 = 1
			  AND
			  (
				  A.HopDongChiTietID IS NULL
				  OR B.HopDongChiTietID IS NULL
				  OR ABS(ISNULL(A.ThanhTien, 0) - ISNULL(B.tttc, 0)) > 10
			  )
			  AND NOT (
						  ISNULL(A.ThanhTien, 0) = 0
						  AND B.tttc IS NULL
					  )
		ORDER BY A.HopDongChiTietID;
    END;

    ELSE IF @LoaiCheck = 32
    BEGIN

        SELECT a.*,
               b.*
        FROM
        (
            SELECT hd.SoHopDong,
                   hd.HopDongID,
                   hdct.HopDongChiTietID,
                   hdct.DmSanPhamREF,
                   tt.DmSanPhamREF DmSanPhamREF_tt,
                   hdct.ThanhTien,
                   tt.DmHinhThucQuangCaoREF,
                   MIN(tt.CreatedAt) CreatedAt,
                   MAX(tt.LastModifiedAt) LastModifiedAt
            FROM HopDongChiTiet hdct
                INNER JOIN HopDong hd
                    ON hd.HopDongID = hdct.HopDongFK
                INNER JOIN ThucChayHopDongChiTiet tt
                    ON hdct.HopDongChiTietID = tt.HopDongChiTietREF
            WHERE hdct.DmLoaiNenTangREF = 9
                  AND hdct.DeletedStatus = 0
                  AND tt.DeletedStatus = 0
                  AND tt.CreatedAt >= '2021-04-08'
            GROUP BY hd.SoHopDong,
                     hdct.HopDongChiTietID,
                     hdct.ThanhTien,
                     tt.DmHinhThucQuangCaoREF,
                     hd.HopDongID,
                     hdct.DmSanPhamREF,
                     tt.DmSanPhamREF
        ) a
            LEFT JOIN
            (
                SELECT hd.SoHopDong,
                       hdct.HopDongChiTietID,
                       SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) SoLuong,
                       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThucChay --, tcdt.NgayThucHien 
                FROM HopDongChiTiet hdct
                    INNER JOIN HopDong hd
                        ON hd.HopDongID = hdct.HopDongFK
                    INNER JOIN ThucChayDaTinh tcdt
                        ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
                WHERE hdct.DmLoaiNenTangREF = 9
                GROUP BY hd.SoHopDong,
                         hdct.HopDongChiTietID --,tcdt.NgayThucHien 
            ) b
                ON a.HopDongChiTietID = b.HopDongChiTietID
        WHERE (
                  a.HopDongChiTietID IS NULL
                  OR b.HopDongChiTietID IS NULL
              )
              OR (a.ThanhTien <> b.ThucChay);
    END;


END;

--select * from KS_ThucChay_TCDT_Inventory where HopDongChiTietID = 610769
--update DmThongTinHopDongBanInventory set DmSanPhamREF = 240 where HopDongChiTietREF = 581274



```
