# Stored Procedure: `ThucChay_DoDuLieuDonGiaAdmatic_job`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-23 15:23:24.063000
- **Ngày sửa cuối**: 2020-09-16 09:38:28.737000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [ThucChay_TinhPR_BySQLJobs]
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuDonGiaAdmatic_job]
	-- Add the parameters for the stored procedure here
AS
    BEGIN
	

        DECLARE @ID INT = 0
        DECLARE @JobID INT
        DECLARE @NgayThucHien DATETIME = NULL

        DECLARE @bannerid INT
          , @product_id INT
          , @core_bannerid INT
          , @price FLOAT
          , @bid_type INT
          , @BannerDateCreated DATETIME

		
		--------------
		-- Nguon 1

        DECLARE icursor CURSOR
        FOR
            SELECT  bannerid
                  , core_bannerid
                  , product_id
                  , convert(float,price)
                  , bid_type
                  , NgayThucHien
            FROM    dbo.AdmaticDonGiaBanner_API
            WHERE   NgayThucHien = CONVERT(DATE, GETDATE())
		
        OPEN icursor  
		
        FETCH NEXT FROM icursor   
		INTO @bannerid, @core_bannerid, @product_id, @price, @bid_type, @BannerDateCreated
		
        WHILE @@FETCH_STATUS = 0
            BEGIN  
                IF EXISTS ( SELECT  [AdmaticBannerID]
                            FROM    dbo.[AdmaticDonGiaBanner]
                            WHERE   1 = 1
                                    AND [AdmaticProductID] = @product_id
                                    AND [DmBannerID] = @core_bannerid )
                    BEGIN
                        PRINT 'Update'
                        UPDATE  [dbo].[AdmaticDonGiaBanner]
                        SET     [AdmaticBannerID] = @bannerid
                              , [AdmaticProductID] = @product_id
                              , [DmBannerID] = @core_bannerid
                              , [DonGiaBanner_VAT] = @price
                              , [LoaiDonGiaTheoDVT] = @bid_type
                              , [BannerDateCreate] = @BannerDateCreated
                              , [LastModifiedAt] = GETDATE()
                              , [LastModifiedBy] = 'Services'
                        WHERE   [AdmaticBannerID] = @bannerid
                                AND [AdmaticProductID] = @product_id
                                AND [DmBannerID] = @core_bannerid

                        EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] @core_bannerid
                    END
                ELSE
                    BEGIN
                        INSERT  INTO [dbo].[AdmaticDonGiaBanner]
                                ( [AdmaticBannerID]
                                , [AdmaticProductID]
                                , [DmBannerID]
                                , [DonGiaBanner_VAT]
                                , [LoaiDonGiaTheoDVT]
                                , [BannerDateCreate]
                                , [CreatedAt]
                                , [CreatedBy]
                                , [LastModifiedAt]
                                , [LastModifiedBy]
                                , [RecordStatus]
                                , [DeletedStatus]
                                )
                        VALUES  ( @bannerid
                                , @product_id
                                , @core_bannerid
                                , @price
                                , @bid_type
                                , @BannerDateCreated
                                , GETDATE()
                                , 'Services'
                                , GETDATE()
                                , 'Services'
                                , 0
                                , 0
                                )
                        EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] @core_bannerid
                    END
			 
                FETCH NEXT FROM icursor   
		    INTO @bannerid, @core_bannerid, @product_id, @price, @bid_type, @BannerDateCreated 
            END   
        CLOSE icursor;  
        DEALLOCATE icursor;  



		--------------
		-- Nguon 2

		DECLARE icursor2 CURSOR
        FOR
            SELECT  bannerid
                  , core_bannerid
                  , product_id
                  , price
                  , bid_type
                  , NgayThucHien
            FROM    dbo.AdmaticDonGiaBanner_API_2
            WHERE   NgayThucHien = CONVERT(DATE, GETDATE())
		
        OPEN icursor2  
		
        FETCH NEXT FROM icursor2   
		INTO @bannerid, @core_bannerid, @product_id, @price, @bid_type, @BannerDateCreated
		
        WHILE @@FETCH_STATUS = 0
            BEGIN  
                IF EXISTS ( SELECT  [AdmaticBannerID]
                            FROM    dbo.[AdmaticDonGiaBanner]
                            WHERE   1 = 1
                                    AND [AdmaticProductID] = @product_id
                                    AND [DmBannerID] = @core_bannerid )
                    BEGIN
                        PRINT 'Update'
                        UPDATE  [dbo].[AdmaticDonGiaBanner]
                        SET     [AdmaticBannerID] = @bannerid
                              , [AdmaticProductID] = @product_id
                              , [DmBannerID] = @core_bannerid
                              , [DonGiaBanner_VAT] = @price
                              , [LoaiDonGiaTheoDVT] = @bid_type
                              , [BannerDateCreate] = @BannerDateCreated
                              , [LastModifiedAt] = GETDATE()
                              , [LastModifiedBy] = 'Services'
                        WHERE   [AdmaticBannerID] = @bannerid
                                AND [AdmaticProductID] = @product_id
                                AND [DmBannerID] = @core_bannerid

                        EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] @core_bannerid
                    END
                ELSE
                    BEGIN
                        INSERT  INTO [dbo].[AdmaticDonGiaBanner]
                                ( [AdmaticBannerID]
                                , [AdmaticProductID]
                                , [DmBannerID]
                                , [DonGiaBanner_VAT]
                                , [LoaiDonGiaTheoDVT]
                                , [BannerDateCreate]
                                , [CreatedAt]
                                , [CreatedBy]
                                , [LastModifiedAt]
                                , [LastModifiedBy]
                                , [RecordStatus]
                                , [DeletedStatus]
                                )
                        VALUES  ( @bannerid
                                , @product_id
                                , @core_bannerid
                                , @price
                                , @bid_type
                                , @BannerDateCreated
                                , GETDATE()
                                , 'Services'
                                , GETDATE()
                                , 'Services'
                                , 0
                                , 0
                                )
                        EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] @core_bannerid
                    END
			 
                FETCH NEXT FROM icursor2   
		    INTO @bannerid, @core_bannerid, @product_id, @price, @bid_type, @BannerDateCreated 
            END   
        CLOSE icursor2;  
        DEALLOCATE icursor2; 

	--CAP NHAT DMSANPHAM
	UPDATE  dbo.AdmaticDonGiaBanner_API
	SET DmSanPhamREF = ISNULL(([dbo].[GetProductIDByTypeProduct]
	(
		product_id
	)),product_id)
	, TenSanPham =  ISNULL(([dbo].[GetProductNameByTypeProduct]
	(
		product_id
	)),'')
	where dmsanphamref IS NULL

	UPDATE  dbo.AdmaticDonGiaBanner_API_2
	SET DmSanPhamREF = ISNULL(([dbo].[GetProductIDByTypeProduct]
	(
		product_id
	)),product_id)
	, TenSanPham =  ISNULL(([dbo].[GetProductNameByTypeProduct]
	(
		product_id
	)),'')
	where dmsanphamref IS NULL
    END



```
