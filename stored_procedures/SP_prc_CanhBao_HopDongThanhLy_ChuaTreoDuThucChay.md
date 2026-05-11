# Stored Procedure: `prc_CanhBao_HopDongThanhLy_ChuaTreoDuThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-11-28 11:46:02.613000
- **Ngày sửa cuối**: 2025-11-28 11:46:02.613000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DateCanhBao` | `date(3)` | No |
| `@Type` | `tinyint(1)` | No |

## Definition (Source Code)

```sql

CREATE PROC dbo.prc_CanhBao_HopDongThanhLy_ChuaTreoDuThucChay
(
    @DateCanhBao DATE = NULL,      -- Ngày muốn chạy cảnh báo
    @Type        TINYINT = NULL    -- 1: cảnh báo ngày thanh lý; 2: sau 15 ngày; NULL: cả 2
)
AS
BEGIN
    SET NOCOUNT ON;

    IF @DateCanhBao IS NULL
        SET @DateCanhBao = CONVERT(DATE, GETDATE());

    ;WITH HopDong AS (
        SELECT  
                c.[ID], 
                c.CONTRACT_NUMBER,
                c.STAFF_ID,
                c.ACCOUNT_MANAGER,
                dt.ID AS PhanBoId
        FROM ASDAG2.CONTRACT.dbo.CONTRACTS c WITH (NOLOCK)
        JOIN ASDAG2.CONTRACT.dbo.CONTRACT_DETAILS dt WITH (NOLOCK) 
              ON dt.CONTRACT_ID = c.ID AND dt.DELETED_STATUS = 0
        WHERE c.DELETED_STATUS = 0 
          AND c.CONTRACT_PREFIX_CODE_ID NOT IN (136, 693)
          AND NOT EXISTS (
                SELECT 1
                FROM ASDAG2.ABM_Data_Release.dbo.DmLoaiHopDongNoiBo n
                WHERE n.DmLoaiHopDongREF = c.CONTRACT_PREFIX_CODE_ID
                  AND GETDATE() BETWEEN n.ThoiGiaBatDauHieuLuc 
                                     AND n.ThoiGianKetThucHieuLuc
          )
          AND c.STATUS NOT IN (0,3)
          AND dt.MONEY_REAL_RUNING <> 3
          AND dt.QUANTITY > 0
          AND dt.PRICE > 0
          AND dt.PERCENT_DISCOUNT_TOTAL <> 100
          AND dt.IS_REAL_RUNING <> 3
    ),
    PhanBo AS (
        SELECT  
                h.ID AS HopDongId,
                h.CONTRACT_NUMBER,
                h.PhanBoId,
                h.STAFF_ID,
                h.ACCOUNT_MANAGER,
                d.PRODUCT_FORMALITY_ID,
                d.PRODUCT_ID,
                d.PRICE,
                d.QUANTITY,
                d.PERCENT_DISCOUNT_TOTAL,
                d.PRICE * d.QUANTITY * (100 - d.PERCENT_DISCOUNT_TOTAL) / 100.0 AS MONEY_REVENUE, 
                d.MONEY_REAL_RUNING,
                d.IS_REAL_RUNING
        FROM HopDong h
        JOIN ASDAG2.CONTRACT.dbo.CONTRACT_DETAILS d WITH (NOLOCK)
              ON d.ID = h.PhanBoId AND d.DELETED_STATUS = 0
    ),
    ChungTuThanhLy AS (
        SELECT  
                a.ID AS HopDongId,
                MAX(b.DATE_CREATE_DOCUMENT) AS NgayThanhLy
        FROM (SELECT DISTINCT ID FROM HopDong) a
        JOIN ASDAG2.CONTRACT.dbo.DOCUMENT_ATTACHS b WITH (NOLOCK)
              ON b.CONTRACT_ID = a.ID AND b.DELETED_STATUS = 0
        JOIN ASDAG2.CONTRACT.dbo.DOCUMENT_TYPES c WITH (NOLOCK)
              ON c.ID = b.DOCUMENT_TYPE_ID AND c.NAME LIKE N'%thanh lý%'
        GROUP BY a.ID
    ),
    DieuKien AS (
        SELECT  
                p.*,
                ctl.NgayThanhLy
        FROM PhanBo p
        LEFT JOIN ChungTuThanhLy ctl 
               ON ctl.HopDongId = p.HopDongId
        WHERE p.MONEY_REVENUE > 0
          AND ctl.HopDongId IS NOT NULL
          AND (p.MONEY_REVENUE - p.MONEY_REAL_RUNING) > 1000
    ),
    CanhBao AS (
        SELECT  
                d.*,
                DATEDIFF(DAY, d.NgayThanhLy, @DateCanhBao) AS SoNgaySauThanhLy
        FROM DieuKien d
    )
    SELECT         
           cb.CONTRACT_NUMBER                              AS SoHopDong,
           cb.HopDongId,
           cb.PhanBoId,
           htqc.NAME                                       AS TenHinhThucQuangCao,
           sp.NAME                                         AS TenSanPham,

           FORMAT(cb.MONEY_REVENUE, 'N0')                  AS ThanhTienHopDong,
           FORMAT(cb.MONEY_REAL_RUNING, 'N0')              AS TongTienTreo_ThucChay,
           FORMAT(cb.MONEY_REVENUE - cb.MONEY_REAL_RUNING, 'N0')
                                                            AS GiaTriCanTreoBoSung,

           cb.NgayThanhLy,
           cb.SoNgaySauThanhLy,

           -- Type theo @Type
           CASE 
               WHEN cb.SoNgaySauThanhLy = 0  THEN 1
               WHEN cb.SoNgaySauThanhLy = 15 THEN 2
           END AS TypeID,

           CASE 
               WHEN cb.SoNgaySauThanhLy = 0 THEN 
                    N'Cảnh báo hợp đồng thanh lý chưa treo đủ giá trị thực chạy'
               WHEN cb.SoNgaySauThanhLy = 15 THEN 
                    N'Cảnh báo hợp đồng thanh lý chưa treo đủ giá trị thực chạy sau 15 ngày'
           END AS TypeName,

           acc.EMAIL_OFFICIAL + ';' + sale.EMAIL_OFFICIAL AS [To],
           sale.EMAIL_OFFICIAL                             AS [Cc],

           sale.FULL_NAME                                  AS AccountPhuTrach,
           sale.EMAIL_OFFICIAL                             AS EmailAccountPhuTrach,

           acc.FULL_NAME                                   AS AccountTong,
           acc.EMAIL_OFFICIAL                              AS EmailAccountTong,

           sale.EMAIL_OFFICIAL                             AS EmailNhanVienKinhDoanh
      
    FROM CanhBao cb
    LEFT JOIN ASDAG2.CONTRACT.dbo.PRODUCT_FORMALITY htqc WITH (NOLOCK) 
           ON htqc.ID = cb.PRODUCT_FORMALITY_ID
    LEFT JOIN ASDAG2.CONTRACT.dbo.PRODUCTS sp WITH (NOLOCK)
           ON sp.ID = cb.PRODUCT_ID
    LEFT JOIN ASDAG2.HRM.dbo.EMPLOYEES sale WITH (NOLOCK)
           ON sale.ID = cb.STAFF_ID
    LEFT JOIN ASDAG2.HRM.dbo.EMPLOYEES acc WITH (NOLOCK)
           ON acc.ID = cb.ACCOUNT_MANAGER
    WHERE cb.NgayThanhLy IS NOT NULL
      AND (
            (@Type IS NULL AND cb.SoNgaySauThanhLy IN (0,15))  -- không truyền type thì lấy cả 2
         OR (@Type = 1    AND cb.SoNgaySauThanhLy = 0)
         OR (@Type = 2    AND cb.SoNgaySauThanhLy = 15)
      );

END

```
