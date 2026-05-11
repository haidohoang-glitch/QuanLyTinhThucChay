# Stored Procedure: `prc_asd_ThucTreo_PR_Update_ContractDetailInfo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-27 10:47:38.600000
- **Ngày sửa cuối**: 2019-05-27 10:47:38.600000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Hungnv
-- Create date: 
-- Description:	
-- =============================================

CREATE PROCEDURE [dbo].[prc_asd_ThucTreo_PR_Update_ContractDetailInfo]
-- Add the parameters for the stored procedure here
@NgayThucHien DATETIME = NULL
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    -- Insert statements for procedure here
    DECLARE @ContractDetailTemp TABLE
    (
        [PhanBoID]           INT   NOT NULL,
        [SanPhamID]          INT   NULL,
        [HinhThucQuangCaoID] INT   NULL,
        [ChietKhau]          FLOAT NULL
    );

    -- =============================================

    DECLARE @executionDate DATE = CONVERT(DATE, ISNULL(@NgayThucHien, GETDATE()));
    DECLARE @currentDate DATETIME = GETDATE();

    -- =============================================

    INSERT INTO @ContractDetailTemp
    (
        [PhanBoID],
        [SanPhamID],
        [HinhThucQuangCaoID],
        [ChietKhau]
    )
    SELECT [ID],
           [PRODUCT_ID],
           [PRODUCT_FORMALITY_ID],
           [PERCENT_DISCOUNT_TOTAL]
    FROM   [CONTRACT].[dbo].[CONTRACT_DETAILS] AS [CD]
    WHERE  CONVERT(DATE, [LAST_MODIFIED_AT]) = @executionDate
    AND    [CREATED_AT] <> [LAST_MODIFIED_AT]
    AND    EXISTS (
        SELECT 1
        FROM   [dbo].[ThucTreo_PR]
        WHERE  [Deleted_Status] = 0
        AND    [Contract_Detail_Id] = [CD].[ID]
    );

    -- =============================================

    UPDATE     [TT_PR]
    SET        [TT_PR].[Product_Formality_Id] = [PB].[HinhThucQuangCaoID],
               [TT_PR].[Product_Id] = [PB].[SanPhamID],
               [TT_PR].[ChietKhau] = [PB].[ChietKhau],
               [TT_PR].[Last_Modified_At] = @currentDate
    FROM       [dbo].[ThucTreo_PR] AS [TT_PR]
    INNER JOIN @ContractDetailTemp AS [PB]
            ON [TT_PR].[Contract_Detail_Id] = [PB].[PhanBoID];



END;

```
