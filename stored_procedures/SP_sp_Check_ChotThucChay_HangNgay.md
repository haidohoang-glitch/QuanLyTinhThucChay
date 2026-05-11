# Stored Procedure: `sp_Check_ChotThucChay_HangNgay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-18 14:27:53.283000
- **Ngày sửa cuối**: 2025-09-19 08:51:48

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
--EXEC [dbo].[sp_Check_ChotThucChay_HangNgay]
-- =============================================
CREATE PROCEDURE  [dbo].[sp_Check_ChotThucChay_HangNgay]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	-- 🗓️ Lấy ngày chạy thực tế mới nhất
DECLARE @NgayThucHien NVARCHAR(50);
SET @NgayThucHien = (
    SELECT CONVERT(DATE, MAX(ACTUAL_RUN_DATE))
    FROM [ASDAG2].contract.dbo.CONTRACT_INFO_DATE_RUNNING_REAL
);

-- 📊 So sánh dữ liệu TCDT vs MONEY_REAL_RUNNING
SELECT 
    @NgayThucHien AS [ThucChayChotDenNgay],
    TC.SoHopDong,
    TC.HopdongID,
    TC.HopDongChiTietID,
    TC.tc,
    TC.NgayThucHien,
    -- B.ID, B.CONTRACT_ID, B.PRODUCT_ID,
    B.MONEY_REAL_RUNING,
    B.DATE_REAL_RUNING,
    B.Deleted_Status,
    (TC.tc - B.MONEY_REAL_RUNING) AS Lech
FROM (
    -- ✅ Tổng hợp dữ liệu thực chạy từ KS_ThucChay_TCDT
    SELECT 
        A.SoHopDong,
        A.HopDongID,
        A.HopDongChiTietID,
        ROUND(SUM(A.tc), 0) AS tc,
        MAX(A.NgayThucHien) AS NgayThucHien
    FROM (
        SELECT 
            SoHopDong,
            HopdongID,
            HopDongChiTietID,
            SUM(ThanhTienThucChay) AS tc,
            MAX(NgayThucHien) AS NgayThucHien
        FROM KS_ThucChay_TCDT
        WHERE 
            NgayThucHien <= @NgayThucHien
          --  AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18) không rõ sao lại không cảnh báo mua ngoài --> 18/09/2025 duongnt 
            AND HopDongChiTietID NOT IN (
                0, 45890, 52942, 52943, 53039, 50351,
                52567, 44268, 46921, 46922, 20240,
                48674, 44004, 42278, 33453
            ) -- các phân bổ từ 2014 trở về trước, không check nữa
        GROUP BY 
            SoHopDong, HopdongID, HopDongChiTietID
    ) A
    GROUP BY 
        A.SoHopDong, A.HopDongChiTietID, A.HopdongID, A.HopDongChiTietID
) TC

-- 🧩 Join với bảng contract_details đã ghi nhận thực chạy
LEFT JOIN (
    SELECT 
		c.CONTRACT_NUMBER,
        ct.ID,
        CONTRACT_ID,
        MONEY_REAL_RUNING,
        DATE_REAL_RUNING,
        ct.PRODUCT_ID,
        ct.Deleted_Status
    FROM [ASDAG2].contract.dbo.contract_details ct
	LEFT JOIN [ASDAG2].contract.dbo.CONTRACTS c
	ON c.ID = ct.CONTRACT_ID
    WHERE 
        ct.ID NOT IN (52942, 52943, 53039)
		--AND ct.ID='760348'
		--không rõ sao lại không cảnh báo mua ngoài --> 18/09/2025 duongnt 
        --AND NOT (
        --    PRODUCT_FORMALITY_ID = 13
        --    OR EXISTS (
        --        SELECT 1
        --        FROM [ASDAG2].CONTRACT.dbo.CONTRACT_DETAIL_PRODUCT_PROPERTIES a
        --        WHERE 
        --            a.PRODUCT_CONFIG_PROPERTY_ID = 5
        --            AND a.VALUE = 18
        --            AND a.DELETED_STATUS = 0
        --            AND a.CONTRACT_DETAIL_ID = ct.ID
        --    )
        --)
) B
    ON TC.HopDongChiTietID = B.ID
    AND TC.HopDongID = B.CONTRACT_ID
	AND TC.SoHopDong = B.CONTRACT_NUMBER

-- ⚠️ Chỉ lấy các phân bổ có chênh lệch > 100 và lọc đúng phân bổ cần xem
WHERE 
    ABS(ISNULL(TC.tc, 0) - ISNULL(B.MONEY_REAL_RUNING, 0)) > 100
    --AND TC.HopDongChiTietID = '760348'
	AND YEAR(TC.NgayThucHien) >= 2025

ORDER BY TC.NgayThucHien DESC;

END

```
