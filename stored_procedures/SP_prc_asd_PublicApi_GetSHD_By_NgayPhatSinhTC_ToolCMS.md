# Stored Procedure: `prc_asd_PublicApi_GetSHD_By_NgayPhatSinhTC_ToolCMS`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-27 10:47:38.713000
- **Ngày sửa cuối**: 2019-05-27 10:47:38.713000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayPhatSinhThucChay` | `date(3)` | No |
| `@WebsiteID` | `int(4)` | No |

## Definition (Source Code)

```sql


-- =============================================
-- Author:		Hungnv
-- Create date: 
-- Description:	
-- =============================================
-- EXECUTE [dbo].[prc_asd_PublicApi_GetSHD_By_NgayPhatSinhTC_ToolCMS] '2015-05-01'
CREATE PROCEDURE [dbo].[prc_asd_PublicApi_GetSHD_By_NgayPhatSinhTC_ToolCMS]
-- Add the parameters for the stored procedure here
@NgayPhatSinhThucChay DATE = NULL,
@WebsiteID            INT  = NULL
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- ==========================================================================================

    DECLARE @ngayPhatSinhTC DATETIME = @NgayPhatSinhThucChay,
            @websiteIdLocal INT      = ISNULL(@WebsiteID, 0);

    -- ==========================================================================================

    SELECT DISTINCT
           [PB].[SoHopDong],
           [PB].[NhanVienID]
    FROM   [dbo].[V_HopDong_PhanBo] AS [PB]
    WHERE  EXISTS ( -- ============ Phat sinh thuc chay ==========
        SELECT 1
        FROM   [dbo].[V_HopDong_PhanBo_NhanHang_DoMain_ThucChay]
        WHERE  [HopDongID] = [PB].[HopDongID]
        AND    [NgayThucHien] = @ngayPhatSinhTC
    )
    AND    EXISTS ( -- ============ La thuc treo PR & Tim theo WebsiteID ==========
        SELECT 1
        FROM   [dbo].[ThucTreo_PR] AS [TT_PR]
        WHERE  [TT_PR].[Deleted_Status] = 0
        AND    [TT_PR].[Contract_Detail_Id] = [PB].[PhanBoID]
        AND    (
                 @websiteIdLocal = 0
              OR [TT_PR].[Website_id] = @websiteIdLocal
        )
    )
    AND    [PB].[SanPhamID] IN (141, 637, 305)
    AND    [PB].[HinhThucQuangCaoID] <> 13
    AND    [PB].[LoaiBanner] <> 18;

END;

```
