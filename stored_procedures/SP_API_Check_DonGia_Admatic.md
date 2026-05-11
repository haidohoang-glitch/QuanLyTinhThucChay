# Stored Procedure: `API_Check_DonGia_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-06-28 11:33:46.050000
- **Ngày sửa cuối**: 2018-06-28 11:35:56.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |
| `@Product_id` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [dbo].[API_Check_DonGia_Admatic] 544620, 8
CREATE PROCEDURE [dbo].[API_Check_DonGia_Admatic]
	-- Add the parameters for the stored procedure here
	@DmBannerID INT,
	@Product_id INT
AS
    BEGIN

            SELECT  bannerid
                  , core_bannerid
                  , product_id
                  , price
                  , bid_type
                  , NgayThucHien
            FROM    dbo.AdmaticDonGiaBanner_API
			WHERE CONVERT(INT,core_bannerid) = @DmBannerID
			AND product_id = @Product_id
			GROUP BY  bannerid
                  , core_bannerid
                  , product_id
                  , price
                  , bid_type
                  , NgayThucHien
			UNION 
            SELECT  bannerid
                  , core_bannerid
                  , product_id
                  , price
                  , bid_type
                  , NgayThucHien
            FROM    dbo.AdmaticDonGiaBanner_API_2
			WHERE CONVERT(INT,core_bannerid) = @DmBannerID
			AND product_id = @Product_id
			GROUP BY  bannerid
                  , core_bannerid
                  , product_id
                  , price
                  , bid_type
                  , NgayThucHien
    END



```
