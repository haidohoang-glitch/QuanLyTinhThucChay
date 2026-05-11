# Stored Procedure: `prc_asd_ThucTreo_GetByThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-02-14 08:24:06.800000
- **Ngày sửa cuối**: 2025-04-11 08:25:14.470000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@JsonThucChay` | `nvarchar` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		Haidv
-- Create date: @Create Date,,>
-- Description:	@Description,,>
-- =============================================
-- [prc_asd_ThucTreo_GetByContractId] 1049192
CREATE PROCEDURE [dbo].[prc_asd_ThucTreo_GetByThucChay]
	-- Add the parameters for the stored procedure here
	--DECLARE
	@JsonThucChay NVARCHAR(MAX)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
    SET NOCOUNT ON;

	-- Kết thúc lệnh trước với chấm phẩy

	;SELECT
    ThucTreoID,
    ContractNumber,
    HinhThucQuangCaoID,
    SanPhamID,
    DonViTinhID,
    DonGia,
    SoLuong,
    ChietKhau,
    BannerId,
    HinhThucQuangCaoID_PB,
    SanPhamID_PB,
    DonViTinhID_PB,
    DonGia_PB,
    SoLuong_PB,
    ChietKhau_PB,
    BannerId_PB
	INTO #templParsedJson
	FROM OPENJSON(@JsonThucChay) -- Giả sử @JsonData là biến chứa chuỗi JSON
	WITH (
		ThucTreoID INT '$.ThucTreoID',
		ContractNumber NVARCHAR(50) '$.ContractNumber',
		HinhThucQuangCaoID INT '$.HinhThucQuangCaoID',
		SanPhamID INT '$.SanPhamID',
		DonViTinhID INT '$.DonViTinhID',
		DonGia DECIMAL(18, 6) '$.DonGia',
		SoLuong INT '$.SoLuong',
		ChietKhau DECIMAL(18, 6) '$.ChietKhau',
		BannerId INT '$.BannerId',
		HinhThucQuangCaoID_PB INT '$.HinhThucQuangCaoID_PB',
		SanPhamID_PB INT '$.SanPhamID_PB',
		DonViTinhID_PB INT '$.DonViTinhID_PB',
		DonGia_PB DECIMAL(18, 6) '$.DonGia_PB',
		SoLuong_PB INT '$.SoLuong_PB',
		ChietKhau_PB DECIMAL(18, 6) '$.ChietKhau_PB',
		BannerId_PB INT '$.BannerId_PB'
	);



	SELECT
    ct.ThucTreoId,
    CASE
        WHEN ct.SanPhamID_PB IN (821, 5133) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN SUM(ISNULL(a.SoLuongThucChay, 0))
        WHEN ct.SanPhamID_PB IN (598) AND ct.BannerId_PB IN (9198) AND ct.DonViTinhID_PB = 7 THEN ct.SoLuong
        WHEN ct.SanPhamID_PB IN (339, 240, 370, 598, 735, 613, 680, 5056, 342) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN
            CASE
                WHEN ct.DonViTinhID_PB = 1 THEN SUM(ISNULL(b.TongViewThucChay, 0))
                WHEN ct.DonViTinhID_PB IN (27, 2) THEN SUM(ISNULL(b.TongClickThucChay, 0))
                WHEN ct.DonViTinhID_PB = 32 THEN SUM(ISNULL(trueview.True_View, 0))
                ELSE 0
            END
        WHEN ct.SanPhamID_PB IN (733) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN
            CASE
                WHEN ct.DonViTinhID = 1 THEN SUM(ISNULL(b.TongViewThucChay, 0))
                WHEN ct.DonViTinhID IN (27, 2) THEN SUM(ISNULL(b.TongClickThucChay, 0))
                WHEN ct.DonViTinhID = 32 THEN SUM(ISNULL(trueview.True_View, 0))
                WHEN ct.SanPhamID IN (821, 5133) THEN SUM(ISNULL(a.SoLuongThucChay, 0))
                ELSE 0
            END
        WHEN ct.HinhThucQuangCaoID_PB IN (42) THEN
            CASE
                WHEN ct.DonViTinhID_PB = 7 AND ct.SanPhamID = 305 THEN ct.SoLuong
                WHEN ct.DonViTinhID_PB = 84 AND ct.SanPhamID = 5312 THEN ct.SoLuong
                WHEN ct.DonViTinhID_PB = 7 AND ct.SanPhamID = 5312 THEN ct.SoLuong
                WHEN ct.BannerId >= 500000 THEN SUM(ISNULL(d.SoLuongThucChay, 0))
                ELSE SUM(ISNULL(d.SoLuongThucChay, 0))
            END
        ELSE 0
    END AS SoLuongChay,
    CASE
        WHEN ct.SanPhamID_PB IN (821, 5133) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN ct.DonGia
        WHEN ct.SanPhamID_PB IN (598) AND ct.BannerId_PB IN (9198) AND ct.DonViTinhID_PB = 7 THEN ct.DonGia
        WHEN ct.SanPhamID_PB IN (339, 240, 370, 598, 735, 613, 680, 5056, 342) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN ct.DonGia
        WHEN ct.SanPhamID_PB IN (733) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN ct.DonGia
        WHEN ct.HinhThucQuangCaoID_PB IN (42) THEN
            CASE
                WHEN ct.DonViTinhID_PB = 7 AND ct.SanPhamID = 305 THEN ct.DonGia
                WHEN ct.DonViTinhID_PB = 84 AND ct.SanPhamID = 5312 THEN ct.DonGia
                WHEN ct.DonViTinhID_PB = 7 AND ct.SanPhamID = 5312 THEN ct.DonGia
                ELSE SUM(ISNULL(banner.DonGiaBanner_VAT, 0))
            END
        ELSE 0
    END AS DonGiaTheoBanner,
    CASE
        WHEN ct.SanPhamID_PB IN (821, 5133) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN SUM(ISNULL(a.ThanhTienThucChaySauCK, 0))
        WHEN ct.SanPhamID_PB IN (598) AND ct.BannerId_PB IN (9198) AND ct.DonViTinhID_PB = 7 THEN ct.SoLuong * ct.DonGia * (1 - ct.ChietKhau_PB / 100)
        WHEN ct.SanPhamID_PB IN (339, 240, 370, 598, 735, 613, 680, 5056, 342) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN
            (CASE
                WHEN ct.DonViTinhID_PB = 1 THEN SUM(ISNULL(b.TongViewThucChay, 0))
                WHEN ct.DonViTinhID_PB IN (27, 2) THEN SUM(ISNULL(b.TongClickThucChay, 0)) * 1000
                WHEN ct.DonViTinhID_PB = 32 THEN SUM(ISNULL(trueview.True_View, 0))
                ELSE 0
            END) * (ct.DonGia / 1000) * (100 - ct.ChietKhau_PB) / 100
        WHEN ct.SanPhamID_PB IN (733) AND ct.HinhThucQuangCaoID_PB NOT IN (42) THEN
            (CASE
                WHEN ct.DonViTinhID = 1 THEN SUM(ISNULL(b.TongViewThucChay, 0))
                WHEN ct.DonViTinhID = 27 THEN SUM(ISNULL(b.TongClickThucChay, 0))
                WHEN ct.DonViTinhID = 32 THEN SUM(ISNULL(trueview.True_View, 0))
                WHEN ct.SanPhamID IN (821, 5133) THEN SUM(ISNULL(a.SoLuongThucChay, 0))
                ELSE 0
            END) * ct.DonGia * (100 - ct.ChietKhau_PB) / 100
        WHEN ct.HinhThucQuangCaoID_PB IN (42) THEN
            CASE
                WHEN ct.DonViTinhID_PB = 7 AND ct.SanPhamID = 305 THEN ct.SoLuong * ct.DonGia * (1 - ct.ChietKhau_PB / 100)
                WHEN ct.DonViTinhID_PB = 84 AND ct.SanPhamID = 5312 THEN ct.SoLuong * ct.DonGia * (1 - ct.ChietKhau_PB / 100)
                WHEN ct.DonViTinhID_PB = 7 AND ct.SanPhamID = 5312 THEN ct.SoLuong * ct.DonGia * (1 - ct.ChietKhau_PB / 100)
                ELSE SUM(ISNULL(d.ThanhTienThucChaySauCK_ChuaVAT, 0)) * (100 - ct.ChietKhau_PB) / 100
            END
        ELSE 0
    END AS ThanhTienTheoBanneer
FROM #templParsedJson ct
LEFT JOIN (
    SELECT
        x.DmBannerID,
        x.SoHopDong,
        SUM(ISNULL(x.ThanhTienThucChaySauCK, 0)) AS ThanhTienThucChaySauCK,
        SUM(ISNULL(x.SoLuongThucChay, 0)) AS SoLuongThucChay
    FROM #templParsedJson y
    JOIN dbo.Thucchay_native_ads x
        ON y.BannerId_PB = x.DmBannerID
        AND y.ContractNumber = x.SoHopDong
        AND x.DeletedStatus = 0
    WHERE
        y.SanPhamID_PB IN (821, 5133, 733)
        AND Y.HinhThucQuangCaoID_PB NOT IN (42)
    GROUP BY
        x.DmBannerID,
        x.SoHopDong
) a ON ct.BannerId = a.DmBannerID
    AND ct.ContractNumber = a.SoHopDong

LEFT JOIN (
    SELECT
        x.DmBannerREF,
        x.SoHopDong,
        SUM(ISNULL(x.TongViewThucChay, 0)) AS TongViewThucChay,
        SUM(ISNULL(x.TongClickThucChay, 0)) AS TongClickThucChay
    FROM #templParsedJson y
    JOIN dbo.ThucChay x
        ON y.BannerId = x.DmBannerREF
        AND y.ContractNumber = x.SoHopDong
        AND x.DeletedStatus = 0
    WHERE
        y.SanPhamID_PB IN (339, 240, 370, 598, 735, 613, 680, 5056, 342, 733)
        AND Y.HinhThucQuangCaoID_PB NOT IN (42)
    GROUP BY
        x.DmBannerREF,
        x.SoHopDong
) b ON ct.BannerId = b.DmBannerREF
    AND ct.ContractNumber = b.SoHopDong

LEFT JOIN (
    SELECT
        x.bannerid,
        x.SoHopDong,
        SUM(ISNULL(x.True_View, 0)) AS True_View
    FROM #templParsedJson y
    JOIN dbo.ThucChayTrueView x
        ON y.BannerId = x.bannerid
        AND y.ContractNumber = x.SoHopDong
        AND x.DeletedStatus = 0
    WHERE
        y.SanPhamID_PB IN (339, 240, 370, 598, 735, 613, 680, 5056, 342, 733)
        AND Y.HinhThucQuangCaoID_PB NOT IN (42)
    GROUP BY
        x.bannerid,
        x.SoHopDong
) trueview ON ct.BannerId = trueview.bannerid
    AND ct.ContractNumber = trueview.SoHopDong

LEFT JOIN (
    SELECT
        x.DmBannerID,
        x.SoHopDong,
        SUM(ISNULL(x.ThanhTienThucChaySauCK_ChuaVAT, 0)) AS ThanhTienThucChaySauCK_ChuaVAT,
        SUM(ISNULL(x.SoLuongThucChay, 0)) AS SoLuongThucChay
    FROM #templParsedJson y
    JOIN dbo.ThucChay_ThanhTien_Admatic x
        ON y.BannerId = x.DmBannerID
        AND y.ContractNumber = x.SoHopDong
        AND x.DmBannerID < 500000
        AND x.DeletedStatus = 0
    WHERE
        y.HinhThucQuangCaoID IN (42)
        AND y.SanPhamID NOT IN (140, 549)
    GROUP BY
        x.DmBannerID,
        x.SoHopDong
) d ON ct.BannerId = d.DmBannerID
    AND ct.ContractNumber = d.SoHopDong

LEFT JOIN (
    SELECT
        x.DmBannerID,
        SUM(ISNULL(x.DonGiaBanner_VAT, 0)) AS DonGiaBanner_VAT
    FROM #templParsedJson y
    JOIN dbo.AdmaticDonGiaBanner x
        ON y.BannerId = x.DmBannerID
        AND x.DeletedStatus = 0
    WHERE
        y.BannerId >= 500000
    GROUP BY
        x.DmBannerID
) banner ON ct.BannerId = banner.DmBannerID
GROUP BY
    ct.ThucTreoId,
    ct.HinhThucQuangCaoID_PB,
    ct.SanPhamID_PB,
    ct.BannerId,
	ct.BannerId_PB,
    ct.DonViTinhID,
    ct.DonViTinhID_PB,
    ct.SanPhamID,
    ct.SoLuong,
    ct.DonGia,
    ct.ChietKhau_PB;

END

```
