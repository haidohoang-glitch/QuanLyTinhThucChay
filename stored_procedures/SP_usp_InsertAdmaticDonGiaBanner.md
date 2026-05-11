# Stored Procedure: `usp_InsertAdmaticDonGiaBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-12 11:46:57.850000
- **Ngày sửa cuối**: 2017-09-11 11:15:49.600000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@bannerid` | `int(4)` | No |
| `@product_id` | `int(4)` | No |
| `@core_bannerid` | `int(4)` | No |
| `@price` | `int(4)` | No |
| `@bid_type` | `int(4)` | No |
| `@BannerDateCreated` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[usp_InsertAdmaticDonGiaBanner]	7213,--@bannerid INT,
	11,--@product_id int,
	517190,--@core_bannerid INT,
	3300,--@price INT,
	1,--@bid_type INT,
	'2017-05-11 00:00:00.000' --@BannerDateCreated DATETIME
	EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] @bannerid
*/
CREATE PROCEDURE [dbo].[usp_InsertAdmaticDonGiaBanner]
(
	@bannerid INT,
	@product_id int,
	@core_bannerid INT,
	@price INT,
	@bid_type INT,
	@BannerDateCreated DATETIME
)
AS
BEGIN
	INSERT INTO [dbo].[AdmaticDonGiaBanner_Log]
			   ([AdmaticBannerID]
			   ,[AdmaticProductID]
			   ,[DmBannerID]
			   ,[DonGiaBanner_VAT]
			   ,[LoaiDonGiaTheoDVT]
			   ,[BannerDateCreate]
			   ,[CreatedAt]
			   ,[CreatedBy]
			   ,[LastModifiedAt]
			   ,[LastModifiedBy]
			   ,[RecordStatus]
			   ,[DeletedStatus])
		 VALUES
			   (@bannerid
			   ,@product_id
			   ,@core_bannerid
			   ,@price
			   ,@bid_type
			   ,@BannerDateCreated
			   ,GETDATE() 
			   ,'Services'
			   ,GETDATE()
			   ,'Services'
			   ,0 
			   ,0 )


	IF EXISTS(SELECT [AdmaticBannerID]
          FROM dbo.[AdmaticDonGiaBanner]  
         WHERE 1=1
		 AND [AdmaticProductID] = @product_id
		 AND [DmBannerID] = @core_bannerid)
	BEGIN
		PRINT 'Update'
		UPDATE [dbo].[AdmaticDonGiaBanner]
		   SET [AdmaticBannerID] = @bannerid
			  ,[AdmaticProductID] = @product_id
			  ,[DmBannerID] = @core_bannerid
			  ,[DonGiaBanner_VAT] = @price
			  ,[LoaiDonGiaTheoDVT] = @bid_type
			  ,[BannerDateCreate] = @BannerDateCreated
			  ,[LastModifiedAt] = GETDATE()
			  ,[LastModifiedBy] = 'Services'
		 WHERE [AdmaticBannerID] = @bannerid
		 AND [AdmaticProductID] = @product_id
		 AND [DmBannerID] = @core_bannerid

		 EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] @core_bannerid
	END
	ELSE
	BEGIN
		INSERT INTO [dbo].[AdmaticDonGiaBanner]
				   ([AdmaticBannerID]
				   ,[AdmaticProductID]
				   ,[DmBannerID]
				   ,[DonGiaBanner_VAT]
				   ,[LoaiDonGiaTheoDVT]
				   ,[BannerDateCreate]
				   ,[CreatedAt]
				   ,[CreatedBy]
				   ,[LastModifiedAt]
				   ,[LastModifiedBy]
				   ,[RecordStatus]
				   ,[DeletedStatus])
			 VALUES
				   (@bannerid
				   ,@product_id
				   ,@core_bannerid
				   ,@price
				   ,@bid_type
				   ,@BannerDateCreated
				   ,GETDATE()
				   ,'Services'
				   ,GETDATE()
				   ,'Services'
				   ,0
				   ,0)
			EXEC [dbo].[ThucChay_UpdateGia_From_AdmaticDonGiaBanner_To_TCBanner_Admatic] @core_bannerid
		END
	
END


```
