# Stored Procedure: `BaoCaoSPvuotHD_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-02-27 15:48:34.147000
- **Ngày sửa cuối**: 2026-03-02 14:57:24.623000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Nam` | `int(4)` | No |
| `@HopDongChiTietID` | `bigint(8)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[BaoCaoSPvuotHD_GGFB]
(
    @Nam INT = 2025,
    @HopDongChiTietID BIGINT = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    -- Xóa dữ liệu cũ của riêng GGFB
    DELETE FROM dbo.BaoCaoSPvuotHD
    WHERE NguonSP = 'GGFB';

    INSERT INTO dbo.BaoCaoSPvuotHD
    (
        NgayDanhso,
        SoHopDong,
        HopDongID,
        HopDongChiTietID,
        DmLoaiREF,
        htqc,
        DmSanPhamREF,
        TenSanPham,
        TenLoaiBanner,
        DmViTriREF,
        TenViTri,
        SoLuong,
        DonViTinh,
        DonGia,
        ChietKhau,
        ThanhTien,
        SoLuong_SP,
        ThucChayBanSP,
        Lech,
        TyLeVuot,
        CreatedDate,
        NguonSP
    )
    SELECT 
        CONVERT(DATE, C.CreatedAt),
        C.SoHopDong,
        C.HopDongID,
        C.HopDongChiTietID,
        C.DmLoaiREF,
        C.TenLoai,
        C.DmSanPhamREF,
        C.TenSanPham,
        C.TenLoaiBanner,
        C.DmViTriREF,
        C.TenViTri,
        C.SoLuong,
        C.DonViTinh,
        C.DonGia,
        C.ChietKhau,
        C.ThanhTien,
        ISNULL(D.SoLuong_SP,0),
        ISNULL(D.ThucChayBanSP,0),
        ISNULL(D.ThucChayBanSP,0) - C.ThanhTien,
        Round(CASE 
            WHEN C.ThanhTien = 0 THEN 0
            ELSE (ISNULL(D.ThucChayBanSP,0) - C.ThanhTien) * 100.0 / C.ThanhTien
        END,2),
        GETDATE(),
        'GGFB'

    FROM (
        SELECT 
            hd.CreatedAt,
            hd.SoHopDong,
            hd.HopDongID,
            hdct.HopDongChiTietID,
            hdct.DmSanPhamREF,
            hdct.DmLoaiREF,
            hdct.TenSanPham,
            hdct.SoLuong,
            hdct.DonViTinh,
            hdct.DmViTriREF,
            hdct.TenViTri,
            hdct.DonGia,
            hdct.ChietKhau,
            CASE 
                WHEN hdct.ChietKhau = 100 
                THEN hdct.SoLuong * hdct.DonGia 
                ELSE hdct.ThanhTien 
            END AS ThanhTien,
            hdct.TenLoai,
            hdct.TenLoaiBanner
        FROM dbo.HopDongChiTiet hdct 
        INNER JOIN dbo.HopDong hd
            ON hd.HopDongID = hdct.HopDongFK
        WHERE 
            hdct.DmLoaiREF <> 42 
            AND hdct.DmLoaiNenTangREF <> 9
            AND hd.DeletedStatus = 0
            AND hdct.DeletedStatus = 0
            AND hd.TrangThaiHopDong NOT IN (0,3)
            AND hd.Nam >= @Nam
            AND (
                    hdct.DmSanPhamREF IN (306,423,5188)  
                    OR hdct.DmViTriREF IN (100093,100478,100774)
                )
            AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
    ) C
    LEFT JOIN (	
        SELECT 
            A.Contract_Detail_Id,
            SUM(ISNULL(A.SoLuongThucChay,0)) AS SoLuong_SP,
            SUM(ISNULL(A.ThucChayBan,0)) AS ThucChayBanSP
        FROM (	
            SELECT  
                o.Contract_Detail_Id,															
                SUM(ISNULL(m.Result,0)) SoLuongThucChay,															
                SUM(ISNULL(m.Sell_Money_VND,0)) ThucChayBan
            FROM [asdag2].ADS.dbo.Operating_Result_Map_Order m															
            INNER JOIN [asdag2].ADS.dbo.Operating_Order o 
                ON o.Id = m.Operating_Order_Id															
            WHERE 
                m.IsDeleted = 0														 
                AND m.Sell_Money_VND <> 0		
            GROUP BY o.Contract_Detail_Id	

            UNION ALL															

            SELECT  
                o.Contract_Detail_Id,
                -1,
                SUM(ISNULL(q.TotalMoney,0))
            FROM ADS_Operating_Order o															
            INNER JOIN ADS_Operating_Result_Quantity q 
                ON o.Id = q.Operating_Order_Id															
            WHERE q.IsDeleted = 0				
            GROUP BY o.Contract_Detail_Id
        ) A 
        GROUP BY A.Contract_Detail_Id
    ) D 
        ON C.HopDongChiTietID = D.Contract_Detail_Id

    WHERE 
        ROUND(ISNULL(D.ThucChayBanSP,0) - C.ThanhTien,0) > 1000

END

```
