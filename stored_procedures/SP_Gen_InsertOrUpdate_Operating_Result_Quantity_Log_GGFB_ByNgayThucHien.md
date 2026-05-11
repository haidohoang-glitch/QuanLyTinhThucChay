# Stored Procedure: `Gen_InsertOrUpdate_Operating_Result_Quantity_Log_GGFB_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-24 16:23:29.850000
- **Ngày sửa cuối**: 2025-10-24 16:23:34.623000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_Quantity_Log_GGFB]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_Operating_Result_Quantity_Log_GGFB_ByNgayThucHien] 	
	@FromDate DATETIME,
	@ToDate DATETIME
AS	
BEGIN

DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''
, @NgayThucHienNow DATETIME = CONVERT(DATE,GETDATE())--getdate() -- CONVERT(DATE,GETDATE())


	SET @server_id =
		ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id),'')

	SET @database= 
		ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id),'')

	SET @NgayThucHien = @FromDate 
	SET @NgayThucHienNow =  @ToDate

	CREATE TABLE #ADS_Operating_Result_Quantity(
		[Id] [int] NOT NULL,
		[D_Products_Id] [int] NULL,
		[Operating_Order_Id] [int] NULL,
		[Quantity] [decimal](18, 4) NULL,
		[UnitPrice] [decimal](18, 4) NULL,
		[TotalMoney] [decimal](18, 4) NULL,
		[FromDate] [date] NULL,
		[ToDate] [date] NULL,
		[UserConfirm] [bigint] NULL,
		[DateConfirm] [datetime2](7) NULL,
		[Status] [int] NULL,
		[CreatorUserId] [nvarchar](50) NULL,
		[CreationTime] [datetime] NULL,
		[LastModificationTime] [datetime] NULL,
		[LastModifierUserId] [nvarchar](50) NULL,
		[IsDeleted] [smallint] NOT NULL,
		[DeleterUserId] [nvarchar](50) NULL,
		[DeletionTime] [datetime] NULL,
		[IsCalc_Result_Quantity] [smallint] NULL,
		[status_record] [smallint] null
	)

	SET @SQL =
	'INSERT INTO #ADS_Operating_Result_Quantity
			   ([Id]
			   ,[D_Products_Id]
			   ,[Operating_Order_Id]
			   ,[Quantity]
			   ,[UnitPrice]
			   ,[TotalMoney]
			   ,[FromDate]
			   ,[ToDate]
			   ,[UserConfirm]
			   ,[DateConfirm]
			   ,[Status]
			   ,[CreatorUserId]
			   ,[CreationTime]
			   ,[LastModificationTime]
			   ,[LastModifierUserId]
			   ,[IsDeleted]
			   ,[DeleterUserId]
			   ,[DeletionTime]
			   ,[IsCalc_Result_Quantity]
			   ,[status_record]) '
    
	SET @SQL +=
	'SELECT [Id]
		  ,[D_Products_Id]
		  ,[Operating_Order_Id]
		  ,[Quantity]
		  ,[UnitPrice]
		  ,[TotalMoney]
		  ,[FromDate]
		  ,[ToDate]
		  ,[UserConfirm]
		  ,[DateConfirm]
		  ,[Status]
		  ,[CreatorUserId] =  ISNULL((select top (1) u.[Name]
								   from ' + @server_id + '.' + @database + '.dbo.AbpUsers u
								   where u.id = od.[CreatorUserId] order by u.id),'''')
		  ,[CreationTime]
		  ,[LastModificationTime]
		  ,[LastModifierUserId]  =  ISNULL((select top (1) u.[Name]
								   from ' + @server_id + '.' + @database + '.dbo.AbpUsers u
								   where u.id = od.[LastModifierUserId] order by u.id),'''')
		  ,[IsDeleted]
		  ,[DeleterUserId] = ISNULL((select top (1) u.[Name]
								   from ' + @server_id + '.' + @database + '.dbo.AbpUsers u
								   where u.id = od.[DeleterUserId] order by u.id),'''')
		  ,[DeletionTime]
		  ,[IsCalc_Result_Quantity] = 0
		  , 0 as status_record
	  FROM ' + @server_id + '.' + @database + '.[dbo].[Operating_Result_Quantity] od
	  WHERE od.[LastModificationTime] >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '
	  + ' AND od.[LastModificationTime] < ' + @daunhay + convert(nvarchar(23),@NgayThucHienNow,121)+ @daunhay+' ' 	
	--PRINT @SQL
	EXEC(@SQL)

	--XAC DINH TRANG THAI RECORD
	UPDATE t 
	SET    t.[status_record] = 1
	FROM  #ADS_Operating_Result_Quantity t 
	LEFT JOIN dbo.ADS_Operating_Result_Quantity_log dc ON t.Id = dc.ADS_Operating_Result_Quantity_Id
	AND t.LastModificationTime = dc.LastModificationTime
	WHERE dc.Id is not null


	-- insert row chưa có
	INSERT INTO [dbo].[ADS_Operating_Result_Quantity_log]
			   ([ADS_Operating_Result_Quantity_Id]
			   ,[D_Products_Id]
			   ,[Operating_Order_Id]
			   ,[Quantity]
			   ,[UnitPrice]
			   ,[TotalMoney]
			   ,[FromDate]
			   ,[ToDate]
			   ,[UserConfirm]
			   ,[DateConfirm]
			   ,[Status]
			   ,[CreatorUserId]
			   ,[CreationTime]
			   ,[LastModificationTime]
			   ,[LastModifierUserId]
			   ,[IsDeleted]
			   ,[DeleterUserId]
			   ,[DeletionTime]
			   ,[IsCalc_Result_Quantity]
			   ,[Log_time])

	SELECT [Id]
		  ,[D_Products_Id]
		  ,[Operating_Order_Id]
		  ,[Quantity]
		  ,[UnitPrice]
		  ,[TotalMoney]
		  ,[FromDate]
		  ,[ToDate]
		  ,[UserConfirm]
		  ,[DateConfirm]
		  ,[Status]
		  ,[CreatorUserId]
		  ,[CreationTime]
		  ,[LastModificationTime]
		  ,[LastModifierUserId]
		  ,[IsDeleted]
		  ,[DeleterUserId]
		  ,[DeletionTime]
		  ,[IsCalc_Result_Quantity]
		  ,GETDATE()
	  FROM #ADS_Operating_Result_Quantity
		WHERE [Status_record] = 0

	 DROP TABLE #ADS_Operating_Result_Quantity
END

```
