# Stored Procedure: `BC_HopDongChuaTreoChiPhi_PRSolution_TCDT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-30 08:54:14.143000
- **Ngày sửa cuối**: 2025-10-30 08:58:46.967000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--PR Solution	Chi phí sản xuất
--Hạng mục Đặng tin đã chạy xong, hạng mục chi phí sản xuất chưa chạy xong.

CREATE PROCEDURE dbo.BC_HopDongChuaTreoChiPhi_PRSolution_TCDT 
    @ToDate DATETIME = NULL
AS
BEGIN
    SET NOCOUNT ON; 

    -- Lấy @ToDate mặc định
    IF @ToDate IS NULL
    BEGIN
        SELECT @ToDate = MAX(NgayThucHien)
        FROM dbo.KS_ThucChay_TCDT;
    END

    /* 0) Tổng thực chạy theo @ToDate */
    IF OBJECT_ID('tempdb..#ThucChay_HD') IS NOT NULL DROP TABLE #ThucChay_HD;
    CREATE TABLE #ThucChay_HD (
        HopDongID          INT            NOT NULL,
        HopDongChiTietID   INT            NOT NULL,
        ThucChay           DECIMAL(19,2)  NOT NULL,
        CONSTRAINT PK_ThucChay_HD PRIMARY KEY (HopDongID, HopDongChiTietID)
    );

    INSERT INTO #ThucChay_HD (HopDongID, HopDongChiTietID, ThucChay)
    SELECT  t.HopDongID,
            t.HopDongChiTietID,
            SUM(CAST(ISNULL(t.ThanhTienThucChayKM,0) AS DECIMAL(19,2)))
          + SUM(CAST(ISNULL(t.ThanhTienThucChay,  0) AS DECIMAL(19,2))) AS ThucChay
    FROM dbo.KS_ThucChay_TCDT t
    WHERE t.NgayThucHien <= @ToDate
    GROUP BY t.HopDongID, t.HopDongChiTietID;

    /* 1) Phân bổ CHI PHÍ () */
    IF OBJECT_ID('tempdb..#PB_CP') IS NOT NULL DROP TABLE #PB_CP;
    CREATE TABLE #PB_CP (
        SoHopDong              NVARCHAR(50),
        HopDongID              INT            NOT NULL,
        PhanBoID               INT            NOT NULL,
        HinhThucQuangCaoID     INT            NULL,
        TenHinhThucQuangCao    NVARCHAR(255)  NULL,
        TenSanPham             NVARCHAR(255)  NULL,
        LoaiBanner             NVARCHAR(255)  NULL,
        NhanHang               NVARCHAR(255)  NULL,   -- 🆕 thêm cột NhanHang
        SoLuong                DECIMAL(19,2)  NULL,
        DonGia                 DECIMAL(19,2)  NULL,
        ChietKhau              DECIMAL(19,2)  NULL,
        ThanhTienPhanBoCP      DECIMAL(19,2)  NOT NULL,  -- tiền phân bổ CP (đã áp dụng IIF)
        CONSTRAINT PK_PB_CP PRIMARY KEY (HopDongID, PhanBoID)
    );

    INSERT INTO #PB_CP
    (
        SoHopDong, HopDongID, PhanBoID, HinhThucQuangCaoID, TenHinhThucQuangCao,
        TenSanPham, LoaiBanner, NhanHang,  -- 🆕 đưa NhanHang vào đúng vị trí
        SoLuong, DonGia, ChietKhau, ThanhTienPhanBoCP
    )
    SELECT  hd.SoHopDong,
            hd.HopDongID,
            hdct.HopDongChiTietID,
            hdct.DmLoaiREF,
            hdct.TenLoai,
            hdct.TenSanPham,
            hdct.TenLoaiBanner,
            hdct.NhanHang,  -- ⚠️ nếu là REF thì JOIN dim lấy tên
            CAST(hdct.SoLuong   AS DECIMAL(19,2)),
            CAST(hdct.DonGia    AS DECIMAL(19,2)),
            CAST(hdct.ChietKhau AS DECIMAL(19,2)),
            CAST(
                IIF(hdct.ChietKhau = 100,
                    hdct.SoLuong * hdct.DonGia,
                    hdct.ThanhTien)
            AS DECIMAL(19,2)) AS ThanhTienPhanBoCP
    FROM dbo.HopDong hd
    JOIN dbo.HopDongChiTiet hdct
      ON hd.HopDongID = hdct.HopDongFK AND hdct.DeletedStatus = 0
    WHERE hd.TrangThaiHopDong NOT IN (0,3)	
      AND hdct.DmLoaiREF =34		--PR Solution
	  AND hdct.DmSanPhamREF =560  -- Chi phí sản xuất  
	  AND  CAST(
                IIF(hdct.ChietKhau = 100,
                    hdct.SoLuong * hdct.DonGia,
                    hdct.ThanhTien)
            AS DECIMAL(19,2)) <> 0
     	

    -- Lưu ý: LIKE '%chi phí%' không SARGable; cân nhắc thêm cột phân loại persisted hoặc full-text nếu muốn tăng tốc.

    /* 2) Phân bổ SẢN PHẨM CHÍNH (Performance base, loại bỏ chi phí) */
    IF OBJECT_ID('tempdb..#PB_SPChinh') IS NOT NULL DROP TABLE #PB_SPChinh;
    CREATE TABLE #PB_SPChinh (
        SoHopDong                   NVARCHAR(50),
        HopDongID                   INT            NOT NULL,
        PhanBoID                    INT            NOT NULL,
        ThanhTienPhanBoSPChinh      DECIMAL(19,2)  NOT NULL,
        CONSTRAINT PK_PB_SPChinh PRIMARY KEY (HopDongID, PhanBoID)
    );

    INSERT INTO #PB_SPChinh (SoHopDong, HopDongID, PhanBoID, ThanhTienPhanBoSPChinh)
    SELECT  hd.SoHopDong,
            hd.HopDongID,
            hdct.HopDongChiTietID,
            --CAST(
            --    IIF(hdct.ChietKhau = 100,
            --        hdct.SoLuong * hdct.DonGia,
            --        hdct.ThanhTien)
            --AS DECIMAL(19,2)) AS ThanhTienPhanBoSPChinh
            CAST(hdct.ThanhTien AS DECIMAL(19,2)) AS ThanhTienPhanBoSPChinh
    FROM dbo.HopDong hd
    JOIN dbo.HopDongChiTiet hdct
      ON hd.HopDongID = hdct.HopDongFK
    WHERE hd.TrangThaiHopDong NOT IN (0,3)
      AND hdct.DmLoaiREF =34		--PR Solution	  
      AND hdct.DmSanPhamREF IN (141,305,637) ;

    /* 3) Tổng hợp SP CHÍNH theo hợp đồng */
    IF OBJECT_ID('tempdb..#Agg_SPChinh') IS NOT NULL DROP TABLE #Agg_SPChinh;
    CREATE TABLE #Agg_SPChinh (
        SoHopDong               NVARCHAR(50),
        HopDongID               INT            NOT NULL PRIMARY KEY,
        TongTienSPChinh         DECIMAL(19,2)  NOT NULL,
        TongThucChaySPChinh     DECIMAL(19,2)  NOT NULL,
        TC_Thieu_SPChinh        DECIMAL(19,2)  NOT NULL
    );

    INSERT INTO #Agg_SPChinh (SoHopDong, HopDongID, TongTienSPChinh, TongThucChaySPChinh, TC_Thieu_SPChinh)
    SELECT  sp.SoHopDong,
            sp.HopDongID,
            SUM(sp.ThanhTienPhanBoSPChinh)                          AS TongTienSPChinh,
            SUM(ISNULL(tc.ThucChay,0))                              AS TongThucChaySPChinh,
            SUM(sp.ThanhTienPhanBoSPChinh) - SUM(ISNULL(tc.ThucChay,0)) AS TC_Thieu_SPChinh
    FROM #PB_SPChinh sp
    LEFT JOIN #ThucChay_HD tc
      ON sp.HopDongID = tc.HopDongID
     AND sp.PhanBoID  = tc.HopDongChiTietID
    GROUP BY sp.HopDongID, sp.SoHopDong;

    /* 4) Tổng hợp CHI PHÍ theo phân bổ */
    IF OBJECT_ID('tempdb..#Agg_CP') IS NOT NULL DROP TABLE #Agg_CP;
    CREATE TABLE #Agg_CP (
        SoHopDong               NVARCHAR(50),
        HopDongID               INT            NOT NULL,
        PhanBoID                INT            NOT NULL,
        TenHinhThucQuangCao     NVARCHAR(255)  NULL,
        TenSanPham              NVARCHAR(255)  NULL,
        NhanHang                NVARCHAR(255)  NULL,  -- 🆕 mang NhanHang theo
        ChietKhau               DECIMAL(19,2)  NULL,
        TienPhanBoCP            DECIMAL(19,2)  NOT NULL,
        ThucChayPB_ChiPhi       DECIMAL(19,2)  NOT NULL,
        TC_Thieu_SPChiPhi       DECIMAL(19,2)  NOT NULL,
        CONSTRAINT PK_Agg_CP PRIMARY KEY (HopDongID, PhanBoID)
    );

    INSERT INTO #Agg_CP
    (
        SoHopDong, HopDongID, PhanBoID, TenHinhThucQuangCao, TenSanPham,
        NhanHang,  -- 🆕
        ChietKhau, TienPhanBoCP, ThucChayPB_ChiPhi, TC_Thieu_SPChiPhi
    )
    SELECT  cp.SoHopDong,
            cp.HopDongID,
            cp.PhanBoID,
            cp.TenHinhThucQuangCao,
            cp.TenSanPham,
            cp.NhanHang,   -- 🆕
            cp.ChietKhau,
            cp.ThanhTienPhanBoCP                              AS TienPhanBoCP,
            SUM(ISNULL(tc.ThucChay,0))                        AS ThucChayPB_ChiPhi,
            cp.ThanhTienPhanBoCP - SUM(ISNULL(tc.ThucChay,0)) AS TC_Thieu_SPChiPhi
    FROM #PB_CP cp
    LEFT JOIN #ThucChay_HD tc
      ON cp.HopDongID = tc.HopDongID
     AND cp.PhanBoID  = tc.HopDongChiTietID
    GROUP BY cp.SoHopDong, cp.HopDongID, cp.PhanBoID, cp.TenHinhThucQuangCao,
             cp.TenSanPham, cp.NhanHang, cp.ChietKhau, cp.ThanhTienPhanBoCP;

    /* 5) Kết quả + cột format số (N0, vi-VN) */
           SELECT
            N'Chưa treo CP' AS CanhBao,
            cp.SoHopDong,
            cp.HopDongID,
            cp.PhanBoID,
            cp.TenHinhThucQuangCao,
            cp.TenSanPham,
            cp.NhanHang,  -- 🆕 hiển thị
            -- cp.ChietKhau,  -- (raw) giữ lại nếu cần dùng số thập phân gốc
            FORMAT(CAST(cp.ChietKhau AS INT), 'N0', 'vi-VN') AS ChietKhau,  -- ✅ bỏ .00
   --         cp.TienPhanBoCP,
   --         cp.ThucChayPB_ChiPhi,
   --         cp.TC_Thieu_SPChiPhi,
   --         sp.TongTienSPChinh,
   --         sp.TongThucChaySPChinh,			
   --         sp.TC_Thieu_SPChinh,
            -- Format hiển thị
            FORMAT(cp.TienPhanBoCP,       'N0', 'vi-VN') AS TienPhanBoCP,
            FORMAT(cp.ThucChayPB_ChiPhi,  'N0', 'vi-VN') AS ThucChayPB_ChiPhi,
            FORMAT(cp.TC_Thieu_SPChiPhi,  'N0', 'vi-VN') AS TC_Thieu_SPChiPhi,
            FORMAT( (sp.TongThucChaySPChinh / NULLIF(sp.TongTienSPChinh,0))*100,'N0', 'vi-VN') AS [TyLe%_TC_SPChinh],
            FORMAT(sp.TongTienSPChinh,    'N0', 'vi-VN') AS TongTienSPChinh,
            FORMAT(sp.TongThucChaySPChinh,'N0', 'vi-VN') AS TongThucChaySPChinh,
            FORMAT(sp.TC_Thieu_SPChinh,   'N0', 'vi-VN') AS TC_Thieu_SPChinh
        FROM #Agg_CP cp
        JOIN #Agg_SPChinh sp
          ON sp.HopDongID = cp.HopDongID
        WHERE sp.TC_Thieu_SPChinh <= 1000      -- coi như đã chạy ~100% SP chính          
		   AND cp.TC_Thieu_SPChiPhi >  1000  -- CP còn thiếu đáng kể
        ORDER BY cp.HopDongID DESC, cp.TC_Thieu_SPChiPhi DESC
        OPTION (RECOMPILE);
   

    -- Cleanup
    DROP TABLE IF EXISTS #Agg_CP, #Agg_SPChinh, #PB_SPChinh, #PB_CP, #ThucChay_HD;
END

```
