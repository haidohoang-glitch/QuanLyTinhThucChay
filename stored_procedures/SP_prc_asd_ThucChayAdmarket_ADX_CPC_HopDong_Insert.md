# Stored Procedure: `prc_asd_ThucChayAdmarket_ADX_CPC_HopDong_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-10 10:48:59.587000
- **Ngày sửa cuối**: 2017-05-10 14:13:34.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@data` | `TBT_ThucChayAdmarket_ADX_CPC_HopDong` | No |
| `@ngayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Bangdv
-- Create date: 
-- Description:	
-- =============================================
CREATE PROCEDURE prc_asd_ThucChayAdmarket_ADX_CPC_HopDong_Insert 
	-- Add the parameters for the stored procedure here
    @data TBT_ThucChayAdmarket_ADX_CPC_HopDong READONLY ,
    @ngayThucHien DATETIME ,
    @DmSanPhamREF NVARCHAR(100)
AS
    BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
        SET NOCOUNT ON;

    -- Insert statements for procedure here

        BEGIN TRANSACTION t1;

        BEGIN TRY
		

            --DELETE  FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong
            --WHERE   CONVERT(DATE, NgayThucHien) = CONVERT(DATE, @ngayThucHien)
            --        AND DmSanPhamREF = @DmSanPhamREF;

            INSERT  INTO ThucChayAdmarket_ADX_CPC_HopDong
                    ( [user_id] ,
                      [username] ,
                      [isnoibo] ,
                      [tt_click] ,
                      [tt_view] ,
                      [money] ,
                      [promotion] ,
                      [contract_number] ,
                      [domain_name] ,
                      [domain_tt_click] ,
                      [domain_tt_view] ,
                      [domain_tt_money] ,
                      [domain_tt_promotion] ,
                      [campaign_id] ,
                      [DmSanPhamREF] ,
                      [TenSanPham] ,
                      [NgayThucHien] ,
                      [createdBy] ,
                      [createdAt] ,
                      [DmViTriREF] ,
                      [TenViTri]
			        )
                    SELECT  [user_id] ,
                            [username] ,
                            [isnoibo] ,
                            [tt_click] ,
                            [tt_view] ,
                            [money] ,
                            [promotion] ,
                            [contract_number] ,
                            [domain_name] ,
                            [domain_tt_click] ,
                            [domain_tt_view] ,
                            [domain_tt_money] ,
                            [domain_tt_promotion] ,
                            [campaign_id] ,
                            [DmSanPhamREF] ,
                            [TenSanPham] ,
                            [NgayThucHien] ,
                            [createdBy] ,
                            GETDATE() ,
                            [DmViTriREF] ,
                            [TenViTri]
                    FROM    @data;

            COMMIT TRANSACTION t1;
        END TRY
        BEGIN CATCH
            ROLLBACK TRANSACTION t1;
        END CATCH;
	
    END;
```
