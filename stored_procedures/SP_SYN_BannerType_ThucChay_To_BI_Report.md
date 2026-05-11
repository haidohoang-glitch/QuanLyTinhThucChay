# Stored Procedure: `SYN_BannerType_ThucChay_To_BI_Report`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-09 10:59:37.437000
- **Ngày sửa cuối**: 2020-09-22 15:40:25.473000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		hungtruongviet
-- Create date: 9/8/2018
-- Description:	Đẩy thông tin loại banner từ ABM sang BI
-- =============================================
CREATE PROCEDURE [dbo].[SYN_BannerType_ThucChay_To_BI_Report]
AS
BEGIN
    SET NOCOUNT ON;
    --INSERT
    INSERT INTO [192.168.23.150].[BI_Report].[dbo].[DM_BANNER_TYPE_NAME_PRODUCT]
    (
        ID,
        BANNER_TYPE_NAME,
        PRODUCT_ID
    )

    SELECT ID,
           BANNER_TYPE_NAME,
           PRODUCT_ID
    FROM [dbo].[DM_BANNER_TYPE_NAME_PRODUCT]
    WHERE DELETED_STATUS = 0
	EXCEPT
	SELECT ID,
           BANNER_TYPE_NAME,
           PRODUCT_ID
    FROM [192.168.23.150].[BI_Report].[dbo].[DM_BANNER_TYPE_NAME_PRODUCT]

END;

```
