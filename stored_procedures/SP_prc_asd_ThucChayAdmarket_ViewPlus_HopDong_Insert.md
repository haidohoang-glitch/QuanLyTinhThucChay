# Stored Procedure: `prc_asd_ThucChayAdmarket_ViewPlus_HopDong_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-10 10:48:45.557000
- **Ngày sửa cuối**: 2017-05-10 14:13:32.590000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@data` | `TBT_ThucChayAdmarket_ViewPlus_HopDong` | No |
| `@ngayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Bangdv
-- Create date: 
-- Description:	
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_ThucChayAdmarket_ViewPlus_HopDong_Insert] 
	-- Add the parameters for the stored procedure here
    @data TBT_ThucChayAdmarket_ViewPlus_HopDong READONLY ,
    @ngayThucHien DATETIME ,
    @DmSanPhamREF NVARCHAR(100)
AS
    BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
        SET NOCOUNT ON;

        BEGIN TRANSACTION t1;

        BEGIN TRY
            --DELETE  FROM dbo.ThucChayAdmarket_ViewPlus_HopDong
            --WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, @ngayThucHien)
            --        AND DmSanPhamREF = @DmSanPhamREF;

            INSERT  INTO ThucChayAdmarket_ViewPlus_HopDong
                    ( [user_id] ,
                      [username] ,
                      [isnoibo] ,
                      [contract_number] ,
                      [tt_click] ,
                      [tt_view] ,
                      [money] ,
                      [promotion] ,
                      [domain_name] ,
                      [domain_tt_click] ,
                      [domain_tt_view] ,
                      [domain_money] ,
                      [domain_promotion] ,
                      [campaign_id] ,
                      [DmSanPhamREF] ,
                      [TenSanPham] ,
                      [NgayThucHien] ,
                      [createdBy] ,
                      [createdAt]
			        )
                    SELECT  [user_id] ,
                            [username] ,
                            [isnoibo] ,
                            [contract_number] ,
                            [tt_click] ,
                            [tt_view] ,
                            [money] ,
                            [promotion] ,
                            [domain_name] ,
                            [domain_tt_click] ,
                            [domain_tt_view] ,
                            [domain_money] ,
                            [domain_promotion] ,
                            [campaign_id] ,
                            [DmSanPhamREF] ,
                            [TenSanPham] ,
                            [NgayThucHien] ,
                            [createdBy] ,
                            GETDATE()
                    FROM    @data;

            COMMIT TRANSACTION t1;
        END TRY
        BEGIN CATCH
            ROLLBACK TRANSACTION t1;
        END CATCH;
	
    END;

```
