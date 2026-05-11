# Stored Procedure: `TCDT_CheckTCTD_Dutoan0`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-03-27 14:32:37.347000
- **Ngày sửa cuối**: 2024-03-27 14:32:37.347000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Ngaythuchien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[TCDT_CheckTCTD_Dutoan0] @Ngaythuchien DATETIME
AS
BEGIN
    IF @Ngaythuchien IS NULL
        SET @Ngaythuchien = CONVERT(DATE, GETDATE());
    SELECT *
    FROM
    (
        SELECT c.HopDongREF,
               c.HopDongChiTietREF,
               SUM(c.ThanhTienThucChayBanSauCK) ThanhTienThucChayBanSauCK
        FROM dbo.ThucChayMuaNgoaiChiTiet c
        WHERE c.HopDongChiTietREF IN
              (
                  SELECT B.PhanBoId
                  FROM [ASDAG2].PMS.dbo.B_DuToan_ChiTiet_HopDong A
                      INNER JOIN [ASDAG2].PMS.dbo.B_DuToan_ChiTiet B
                          ON A.B_DuToan_ChiTiet_REF = B.Id
                  WHERE A.ThanhTienSauCK = 0
                        AND A.LastModificationTime >= @Ngaythuchien
                        AND B.PhanBoId IS NOT NULL
              )
              AND c.Status IN ( 1, 2, 4 )
              AND c.DeletedStatus = 0
        --AND c.HopDongChiTietREF=715795
        GROUP BY c.HopDongREF,
                 c.HopDongChiTietREF
    --ORDER BY c.HopDongChiTietREF DESC)
    ) L
        INNER JOIN
        (
            SELECT a.SoHopDong,
                   a.HopDongChiTietREF,
                   a.DmSanPhamREF,
                   a.TenSanPham,
                   a.TenHinhThucQuangCao,
                   (SUM(a.ThanhTienSauTrietKhauThucChay + a.GiaTriThayDoi)) AS tc
            FROM dbo.ThucChayDaTinh a
            WHERE HopDongChiTietREF IN
                  (
                      SELECT B.PhanBoId
                      FROM [ASDAG2].PMS.dbo.B_DuToan_ChiTiet_HopDong c
                          INNER JOIN [ASDAG2].PMS.dbo.B_DuToan_ChiTiet B
                              ON c.B_DuToan_ChiTiet_REF = B.Id
                      WHERE c.ThanhTienSauCK = 0
                            AND c.LastModificationTime >= @Ngaythuchien
                            AND B.PhanBoId IS NOT NULL
                  )
            GROUP BY a.SoHopDong,
                     a.HopDongChiTietREF,
                     a.DmSanPhamREF,
                     a.TenSanPham,
                     a.TenHinhThucQuangCao
        --ORDER BY a.HopDongChiTietREF DESC
        ) T
            ON T.HopDongChiTietREF = L.HopDongChiTietREF
    WHERE ROUND(L.ThanhTienThucChayBanSauCK - T.tc, 0) <> 0;
END;

```
