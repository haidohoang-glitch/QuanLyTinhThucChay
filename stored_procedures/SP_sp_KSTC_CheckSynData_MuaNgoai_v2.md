# Stored Procedure: `sp_KSTC_CheckSynData_MuaNgoai_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-10-29 14:05:22.420000
- **Ngày sửa cuối**: 2025-12-04 10:47:01.300000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[sp_KSTC_CheckSynData_MuaNgoai_v2]
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @Today DATE = CAST(GETDATE() AS DATE);

    ----------------------------------------------------------------------
    -- 1. DỰ TOÁN MUA – NGUỒN & ĐÍCH & CHI TIẾT LỆCH
    ----------------------------------------------------------------------

    -- Nguồn: B_DuToan_Chitiet_HopDong + B_DuToan_ChiTiet + contract_details
    SELECT 
          ct.Contract_Id
        , b.PhanBoId
        , ct.Product_id
        , a.Id
        , a.DonGiaMua          -- giá mua nguồn
        , a.SoLuongMua         -- SL mua nguồn
        , a.ChietKhauMua
        , a.PhaiTraNhaCungCap
        , a.ThanhTienSauCK
        , a.IsDeleted
        , a.LastModificationTime
        , ct.Last_Modified_At
    INTO #DuToanNguon
    FROM [asdag2].PMS.dbo.B_DuToan_Chitiet_HopDong a
    INNER JOIN [asdag2].PMS.dbo.B_DuToan_ChiTiet b 
            ON a.B_DuToan_ChiTiet_REF = b.Id
    LEFT JOIN [asdag2].contract.dbo.contract_details ct 
            ON ct.Id = b.PhanBoId
    WHERE 
        a.IsDeleted = 0
        AND ct.Deleted_Status = 0
        AND ct.Contract_id NOT IN (
                SELECT Id 
                FROM [asdag2].contract.dbo.contracts 
                WHERE [Status] = 3
            )
        AND b.PhanBoId IN (
                SELECT PhanBoID 
                FROM [asdag2].PMS.dbo.B_QuanLyThucChay 
                WHERE IsDeleted = 0
            )
        AND (
                ct.PRODUCT_FORMALITY_ID = 13 
             OR EXISTS (
                    SELECT 1 
                    FROM [asdag2].CONTRACT.dbo.CONTRACT_DETAIL_PRODUCT_PROPERTIES x
                    WHERE x.PRODUCT_CONFIG_PROPERTY_ID = 5 
                      AND x.[VALUE] = 18
                      AND x.DELETED_STATUS = 0
                      AND x.CONTRACT_DETAIL_ID = ct.ID
                )
            );

    -- Đích: HopDongChiTiet_MuaNgoai + HopDongChiTiet
    -- 🔧 Đổi tên DonGiaMua, SoLuongMua để không trùng với nguồn
    SELECT 
          b.HopDongFK
        , mn.HopDongChiTietID
        , b.DmSanPhamREF
        , mn.DonGiaMua    AS DonGiaMua_Dich
        , mn.SoLuongMua   AS SoLuongMua_Dich
        , mn.ThanhTienSauCKMua
        , mn.ThanhTienBanSauCK
        , mn.ThanhTienLaiSauCK
    INTO #DuToanDich
    FROM dbo.HopDongChiTiet_MuaNgoai mn
    LEFT JOIN dbo.HopDongChiTiet b 
           ON mn.HopDongChiTietID = b.HopDongChiTietID
    WHERE 
        mn.DeletedStatus = 0
        AND b.DeletedStatus = 0
        AND mn.HopDongChiTietID NOT IN 
            (529886,532414,549887,634898,682448,692930,723055)
        AND (b.DmLoaiREF = 13 OR b.DmLoaiBannerREF = 18)
        AND b.HopDongFK NOT IN (
                SELECT HopDongID 
                FROM dbo.HopDong 
                WHERE TrangThaiHopDong = 3
            )
        AND b.HopDongChiTietID IN (
                SELECT HopDongChiTietREF 
                FROM dbo.ThucChayMuaNgoaiChiTiet 
                WHERE DeletedStatus = 0
            );

    -- Chi tiết lệch Dự toán
    SELECT 
          N'Mua ngoài' AS CheckSynData
        , 'DuToanMua'  AS Loai
        , Nguon.*
        , Dich.*
        , CAST(ISNULL(Nguon.LastModificationTime, Nguon.Last_Modified_At) AS DATE) AS NgayThayDoi
    INTO #DuToanChiTiet
    FROM #DuToanNguon Nguon
    FULL OUTER JOIN #DuToanDich Dich
         ON Nguon.PhanBoId = Dich.HopDongChiTietID
    WHERE 
        Nguon.PhanBoId IS NULL
        OR Dich.HopDongChiTietID IS NULL;

    -- 🔹 Result set 1: chi tiết Dự toán (KHÔNG CÓ CỘT TỔNG)
    SELECT 
          CheckSynData
        , Loai
        , Contract_Id
        , PhanBoId
        , Product_id
        , Id
        , DonGiaMua              -- nguồn
        , SoLuongMua             -- nguồn
        , ChietKhauMua
        , PhaiTraNhaCungCap
        , ThanhTienSauCK
        , IsDeleted
        , LastModificationTime
        , Last_Modified_At
        , HopDongFK
        , HopDongChiTietID
        , DmSanPhamREF
        , DonGiaMua_Dich         -- đích
        , SoLuongMua_Dich        -- đích
        , ThanhTienSauCKMua
        , ThanhTienBanSauCK
        , ThanhTienLaiSauCK
        , NgayThayDoi            -- có thể bỏ nếu không cần xem
    FROM #DuToanChiTiet;



    ----------------------------------------------------------------------
    -- 2. THỰC CHẠY MUA – NGUỒN & ĐÍCH & CHI TIẾT LỆCH
    ----------------------------------------------------------------------

    -- Nguồn: B_QuanLyThucChay
    SELECT 
          a.Id
        , a.HopDongID
        , a.PhanBoId
        , a.ChietKhauMua
        , a.SoLuongChay
        , a.DonGia
        , a.D_DonViTinhREF
        , a.ThanhTien
        , a.IsDeleted
        , a.TrangThai
        , a.CreationTime
        , a.LastModificationTime
    INTO #ThucChayNguon
    FROM [asdag2].pms.dbo.B_QuanLyThucChay a
    LEFT JOIN [asdag2].contract.dbo.contracts ct 
           ON a.HopDongID = ct.Id
    WHERE 
        ct.Status <> 3
        AND a.LastModificationTime >= '2020-01-01'
        AND a.PhanBoId NOT IN (575154,575112);

    -- Đích: ThucChayMuaNgoaiChiTiet + HopDongChiTiet + HopDong
    SELECT  
          tc.ThucChayMuaNgoaiChiTietID
        , tc.HopDongREF
        , tc.HopDongChiTietREF
        , dtb.DmSanPhamREF
        , tc.ChietKhauMuaNgoai
        , tc.SoLuongThucChay
        , tc.ThanhTienMuaNgoaiTruocCK
        , tc.DeletedStatus
        , tc.[Status] AS TrangThaiDuyet
        , tc.LastModifiedAt
    INTO #ThucChayDich
    FROM dbo.ThucChayMuaNgoaiChiTiet tc 
    LEFT JOIN dbo.HopDongChiTiet dtb 
           ON tc.HopDongChiTietREF = dtb.HopDongChiTietID 
          AND dtb.DeletedStatus = 0 
          AND (dtb.DmLoaiREF = 13 OR dtb.DmLoaiBannerREF = 18)
    LEFT JOIN dbo.HopDong hd 
           ON hd.HopDongID = tc.HopDongREF 
    WHERE 
        hd.TrangThaiHopDong <> 3
        AND tc.LastModifiedAt >= '2020-01-01'
        AND tc.HopDongChiTietREF NOT IN (575154,575112);

    -- Chi tiết lệch Thực chạy
    SELECT 
          N'Mua ngoài' AS CheckSynData
        , 'ThucChayMua' AS Loai
        , A.Id
        , B.ThucChayMuaNgoaiChiTietID AS IdDich
        , A.HopDongID
        , B.HopDongREF
        , A.PhanBoId
        , B.HopDongChiTietREF
        , B.DmSanPhamREF
        , A.ChietKhauMua
        , B.ChietKhauMuaNgoai
        , A.SoLuongChay
        , B.SoLuongThucChay
        , A.ThanhTien
        , B.ThanhTienMuaNgoaiTruocCK
        , (A.ThanhTien - B.ThanhTienMuaNgoaiTruocCK) AS LechTien
        , A.TrangThai
        , B.TrangThaiDuyet
        , A.IsDeleted
        , B.DeletedStatus
        , A.CreationTime
        , A.LastModificationTime
        , B.LastModifiedAt
        , CAST(ISNULL(A.LastModificationTime, B.LastModifiedAt) AS DATE) AS NgayThayDoi
    INTO #ThucChayChiTiet
    FROM #ThucChayNguon A
    FULL OUTER JOIN #ThucChayDich B
         ON A.Id = B.ThucChayMuaNgoaiChiTietID
    WHERE 
        NOT (A.IsDeleted = 1 AND B.DeletedStatus = 1)
        AND (
               A.HopDongID <> B.HopDongREF OR A.HopDongID IS NULL OR B.HopDongREF IS NULL
            OR A.PhanBoId <> B.HopDongChiTietREF OR A.PhanBoId IS NULL OR B.HopDongChiTietREF IS NULL
            OR A.TrangThai <> B.TrangThaiDuyet OR A.TrangThai IS NULL OR B.TrangThaiDuyet IS NULL
            OR ABS(ISNULL(A.ThanhTien,0) - ISNULL(B.ThanhTienMuaNgoaiTruocCK,0)) > 5
            OR A.IsDeleted <> B.DeletedStatus
        );

    -- 🔹 Result set 2: chi tiết Thực chạy
    SELECT 
          CheckSynData
        , Loai
        , Id
        , IdDich
        , HopDongID
        , HopDongREF
        , PhanBoId
        , HopDongChiTietREF
        , DmSanPhamREF
        , ChietKhauMua
        , ChietKhauMuaNgoai
        , SoLuongChay
        , SoLuongThucChay
        , ThanhTien
        , ThanhTienMuaNgoaiTruocCK
        , LechTien
        , TrangThai
        , TrangThaiDuyet
        , IsDeleted
        , DeletedStatus
        , CreationTime
        , LastModificationTime
        , LastModifiedAt
        , NgayThayDoi
    FROM #ThucChayChiTiet
    ORDER BY ISNULL(LastModificationTime, LastModifiedAt) DESC;



    ----------------------------------------------------------------------
    -- 3. KHỐI TỔNG – RIÊNG 1 RESULT SET
    ----------------------------------------------------------------------
    SELECT 
          'DuToanMua' AS Loai
        , (SELECT COUNT(*) FROM #DuToanNguon)     AS SoLuongNguon
        , (SELECT COUNT(*) FROM #DuToanDich)      AS SoLuongDich
        , (SELECT COUNT(*) FROM #DuToanChiTiet)   AS SoLuongLech
        , (SELECT COUNT(*) FROM #DuToanChiTiet 
           WHERE NgayThayDoi = @Today)           AS SoLuongLechHomNay

    UNION ALL

    SELECT 
          'ThucChayMua' AS Loai
        , (SELECT COUNT(*) FROM #ThucChayNguon)   AS SoLuongNguon
        , (SELECT COUNT(*) FROM #ThucChayDich)    AS SoLuongDich
        , (SELECT COUNT(*) FROM #ThucChayChiTiet) AS SoLuongLech
        , (SELECT COUNT(*) FROM #ThucChayChiTiet 
           WHERE NgayThayDoi = @Today)           AS SoLuongLechHomNay;



    ----------------------------------------------------------------------
    -- DỌN TEMP TABLE
    ----------------------------------------------------------------------
    DROP TABLE #DuToanNguon;
    DROP TABLE #DuToanDich;
    DROP TABLE #DuToanChiTiet;
    DROP TABLE #ThucChayNguon;
    DROP TABLE #ThucChayDich;
    DROP TABLE #ThucChayChiTiet;

END

```
