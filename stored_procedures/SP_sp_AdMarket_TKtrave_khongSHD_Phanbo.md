# Stored Procedure: `sp_AdMarket_TKtrave_khongSHD_Phanbo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-14 15:27:41.177000
- **Ngày sửa cuối**: 2025-10-24 16:27:56.910000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NamTu` | `int(4)` | No |
| `@DmSanPhamRef` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE dbo.sp_AdMarket_TKtrave_khongSHD_Phanbo
(
    @NamTu INT = 2020,
    @DmSanPhamRef INT = 585
)
AS
BEGIN
    SET NOCOUNT ON;

    WITH A AS (
        SELECT
            p.[user_id], p.username,p.contract_number,
            SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_view))  AS tong_view,
            SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_click)) AS tong_click,
            SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_money)) AS tong_tien
        FROM ThucChayAdmarket_PhanBo AS p
        WHERE NULLIF(LTRIM(RTRIM(p.contract_number)), '') IS NULL
			  OR UPPER(LTRIM(RTRIM(p.contract_number))) = N'BLANK'
        GROUP BY  p.[user_id],p.username,contract_number
		HAVING SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_money)) > 0
    ),
    C AS (
        SELECT 
			hd.NgayDanhSoHopDong,
            hd.SoHopDong,
            hdct.HopDongChiTietID,
            hdct.SoLuong,
            hdct.DonGia,
            hdct.ChietKhau,
            hdct.ThanhTien,
            hdct.TK_AdMarketID,
            hdct.TK_AdMarket
        FROM dbo.HopDongChiTiet AS hdct
        JOIN dbo.HopDong AS hd ON hd.HopDongID = hdct.HopDongFK
        WHERE hdct.DeletedStatus = 0
		  AND ( ROUND(ISNULL(hdct.SoLuong,0),0) <> 0 OR ROUND(ISNULL(hdct.DonGia,0),0) <> 0)
          AND hd.TrangThaiHopDong NOT IN (0,3)		  
          AND hdct.DmLoaiREF IN (26, 5010, 5038, 5000) -- HTQC Performance
          AND hdct.DmSanPhamREF = @DmSanPhamRef
          AND hd.Nam >= @NamTu
    ),
    D AS (
        SELECT 
            d.HopDongChiTietREF,
            SUM(ISNULL(d.ThanhTienSauTrietKhauThucChay,0) + ISNULL(d.GiaTriThayDoi,0)) AS TongThucChay
        FROM dbo.ThucChayDaTinhAdmarket AS d
		WHERE  d.DmHinhThucQuangCao IN (26, 5010, 5038, 5000) -- HTQC Performance
        GROUP BY d.HopDongChiTietREF
    )
    SELECT
          C.TK_AdMarketID,
		  C.TK_AdMarket,
		  A.contract_number AS SoHopDong_SP,
		  --A.username                  AS TK_AdMarket_SP,
		  dbo.FormatNumber(A.tong_view) AS tong_view_SP,
		  dbo.FormatNumber(A.tong_click) AS tong_click_SP,
		  dbo.FormatNumber(A.tong_tien) AS tong_tien_SP,
		   C.SoHopDong,
		  C.HopDongChiTietID,
		  C.SoLuong,
		  dbo.FormatNumber(C.DonGia) AS DonGia,
		  C.ChietKhau,
		  dbo.FormatNumber(C.ThanhTien)                 AS ThanhTien_HDky,
		  dbo.FormatNumber(ISNULL(D.TongThucChay,0))   AS ThanhTien_ThucChay,
		  dbo.FormatNumber((C.ThanhTien - ISNULL(D.TongThucChay,0))) AS TienTC_thieu_HDKy,
        CASE 
            WHEN D.TongThucChay IS NULL THEN N'Phân bổ chưa có thực chạy'
            WHEN C.ThanhTien - ISNULL(D.TongThucChay,0) < 0 THEN N'Phân bổ vượt thực chạy so với HĐ ký'
            WHEN C.ThanhTien - ISNULL(D.TongThucChay,0) > 0 THEN N'Phân bổ chưa đủ thực chạy so với HĐ ký'
            ELSE N'Khớp thực chạy và HĐ ký'
        END AS Ghichu
    FROM C
    LEFT JOIN D ON D.HopDongChiTietREF = C.HopDongChiTietID
    JOIN A ON a.user_id = c.TK_AdMarketID --LTRIM(RTRIM(A.username)) = LTRIM(RTRIM(C.TK_AdMarket))
    WHERE ROUND((C.ThanhTien - ISNULL(D.TongThucChay,0)),0) > 1000
    ORDER BY C.TK_AdMarket, c.NgayDanhSoHopDong DESC,C.SoHopDong DESC;
END

```
