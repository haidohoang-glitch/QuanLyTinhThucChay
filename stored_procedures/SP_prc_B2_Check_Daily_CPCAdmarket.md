# Stored Procedure: `prc_B2_Check_Daily_CPCAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-04-29 14:41:59.170000
- **Ngày sửa cuối**: 2022-04-29 14:41:59.170000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

CREATE PROC prc_B2_Check_Daily_CPCAdmarket
	@NgayThucHien DATETIME = NULL
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT A.HopDongID,
           A.SoHopDong,
           ISNULL(ROUND((A.tc - B.money), 2), NULL) AS Lech,
           hd.TrangThaiHopDong,
           B.username,
           A.TK_AdMarket
    FROM
    (
        SELECT tcdt.HopDongID,
               tcdt.SoHopDong,
               hdct.TK_AdMarket,
               SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) tc
        FROM ThucChayDaTinhAdmarket tcdt
            INNER JOIN HopDongChiTiet hdct
                ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
        WHERE NgayThucHien = @NgayThucHien
              AND tcdt.DmSanPhamREF = 144
              AND tcdt.DmViTriREF = 0
              AND tcdt.SoHopDong <> '-'
        GROUP BY tcdt.SoHopDong,
                 hdct.TK_AdMarket,
                 tcdt.HopDongID
    ) A
        FULL OUTER JOIN
        (
            SELECT contract_number,
                   username,
                   ISNULL(SUM(CONVERT(FLOAT, domain_tt_money)) / 1.08, 0) AS money
            FROM ThucChayAdmarket_ADX_CPC_HopDong
            WHERE NgayThucHien = @NgayThucHien
                  AND DmSanPhamREF = 144
                  AND DmViTriREF = 0
                  AND isnoibo = 0
            GROUP BY contract_number,
                     username
        ) B
            ON A.SoHopDong = B.contract_number
               AND A.TK_AdMarket = B.username
        INNER JOIN HopDong hd
            ON hd.SoHopDong = A.SoHopDong
    WHERE ISNULL(ROUND((A.tc - B.money), 2), 9999) <> 0
    ORDER BY A.SoHopDong;

END;









```
