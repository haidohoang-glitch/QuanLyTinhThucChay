# Stored Procedure: `Gen_InsertOrUpdate_Operating_Result_Log_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-31 10:35:40.830000
- **Ngày sửa cuối**: 2025-10-24 14:06:25.257000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
[dbo].[Gen_InsertOrUpdate_Operating_Result_Log_GGFB]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_Operating_Result_Log_GGFB] 	
AS	
BEGIN

DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''
	SET @NgayThucHien = 
		ISNULL((
			SELECT MAX([LastModificationTime])   
			FROM   dbo.[ADS_Operating_Result_Log]  
		),'1900-01-01')

	DECLARE	@NgayThucHienNow DATETIME = CONVERT(DATE,GETDATE())--getdate() -- CONVERT(DATE,GETDATE())
	SET @NgayThucHien = 
		ISNULL((
			SELECT MAX([LastModificationTime])   
			FROM   dbo.[ADS_Operating_Result]  
		),'1900-01-01')


	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id),'')
	SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)

--	SET @NgayThucHien = '2025-10-24'
--set @NgayThucHienNow = '2025-10-25'
	CREATE TABLE #ADS_Operating_Result(
		[Id] [int]  NOT NULL,
		[Product Id] int NULL,
		[Product Name] nvarchar(50) NULL,
		[Operating_Order_Id] [int] NULL,
		[AdAccount_Name] [nvarchar](500) NULL,   -- tên tài khoản chạy
		[AdAccount_Id] [nvarchar](500) NULL,  
		[Campaign_Id] [nvarchar](500) NULL,   -- tên chiến dịch
		[Campaign_Name] [nvarchar](500) NULL,
		[Exchange_Rate_Id] [int] NULL,     -- tỉ giá
		[Exchange_Rate] [decimal](18, 4) NULL,
		[Start_Date] [datetime] NULL,
		[Result_Type] [nvarchar](100) NULL,    -- loại kết quả 
		[Result] [decimal](18, 4) NULL, 
		[Reach] [decimal](18, 4) NULL,
		[Impression] [decimal](18, 4) NULL,
		[Amoun_Spent] [decimal](18, 4) NULL,
		[Frequency] [decimal](18, 4) NULL,
		[CPC] [decimal](18, 4) NULL,
		[CTR] [decimal](18, 4) NULL,
		[Cost_Per_Result] [decimal](18, 4) NULL,
		[Clicks] [decimal](18, 4) NULL,
		[CPM] [decimal](18, 4) NULL,
		[Cost_Per_Thousand_People_Reached] [decimal](18, 4) NULL,
		[Page_Likes] [decimal](18, 4) NULL,
		[Post_Engagement] [decimal](18, 4) NULL,
		[Cost_Per_Page_Like] [decimal](18, 4) NULL,
		[Cost_Per_Post_Engagement] [decimal](18, 4) NULL,
		[Leads] [decimal](18, 4) NULL,
		[Total_Money_VND] [decimal](18, 4) NULL,
		[Sell_Money_VND] [decimal](18, 4) NULL,
		[View] [decimal](18, 4) NULL,
		[Conversions] [decimal](18, 4) NULL,
		[CPV] [decimal](18, 4) NULL,
		[CreationTime] [datetime2](7) NULL,
		[Age] [nvarchar](100) NULL,
		[Sex] [int] NULL,
		[Regions] [nvarchar](100) NULL,
		[CreatedBy] nvarchar(100) NULL,
		[LastModificationTime] [datetime2](7) NULL,
		[LastModifiedBy] nvarchar(100) NULL,
		[IsDeleted] [smallint] NOT NULL,
		[DeletedBy] nvarchar(100) NULL,
		[DeletionTime] [datetime2](7) NULL,
		[Date_result] [date] NULL ,
		[Status Record] [smallint] not null
		)

	SET @SQL =
	'INSERT INTO #ADS_Operating_Result
	(      [Id]
		  ,[Product Id]
		  ,[Product Name]
		  ,[Operating_Order_Id]
		  ,[AdAccount_Name]
		  ,[AdAccount_Id]
		  ,[Campaign_Id]
		  ,[Campaign_Name]
		  ,[Exchange_Rate_Id]
		  ,[Exchange_Rate]
		  ,[Start_Date]
		  ,[Result_Type]
		  ,[Result]
		  ,[Reach]
		  ,[Impression]
		  ,[Amoun_Spent]
		  ,[Frequency]
		  ,[CPC]
		  ,[CTR]
		  ,[Cost_Per_Result]
		  ,[Clicks]
		  ,[CPM]
		  ,[Cost_Per_Thousand_People_Reached]
		  ,[Page_Likes]
		  ,[Post_Engagement]
		  ,[Cost_Per_Page_Like]
		  ,[Cost_Per_Post_Engagement]
		  ,[Leads]
		  ,[Total_Money_VND]
		  ,[Sell_Money_VND]
		  ,[View]
		  ,[Conversions]
		  ,[CPV]
		  ,[CreationTime]
		  ,[Age]
		  ,[Sex]
		  ,[Regions]
		  ,[CreatedBy]
		  ,[LastModificationTime]
		  ,[LastModifiedBy]
		  ,[IsDeleted]
		  ,[DeletedBy]
		  ,[DeletionTime]
		  ,[Date_result]
		  ,[Status Record]) '

	SET @SQL +=
	'SELECT [Id]
		  ,isnull(D_Products_Id,0)
		  ,'''' as [Product Name] 
		  ,[Operating_Order_Id]
		  ,[AdAccount_Name]
		  ,[AdAccount_Id]
		  ,[Campaign_Id]
		  ,[Campaign_Name]
		  ,isnull([D_Exchange_Rate_Id] ,0) AS [D_Exchange_Rate_Id]
		  ,isnull([Exchange_Rate],0) AS [Exchange_Rate]
		  ,[Start_Date]
		  ,isnull([Result_Type],0) AS [Result_Type]
		  ,isnull([Result],0) AS [Result]
		  ,ISNULL([Reach],0) AS [Reach]
		  ,ISNULL([Impression],0) AS [Impression]
		  ,ISNULL([Amoun_Spent],0) AS [Amoun_Spent]
		  ,ISNULL([Frequency],0) AS [Frequency]
		  ,ISNULL([CPC],0) AS [CPC]
		  ,ISNULL([CTR],0) AS [CTR]
		  ,ISNULL([Cost_Per_Result],0) AS [Cost_Per_Result]
		  ,ISNULL([Clicks],0) AS [Clicks]
		  ,ISNULL([CPM],0) AS [CPM]
		  ,ISNULL([Cost_Per_Thousand_People_Reached],0) AS [Cost_Per_Thousand_People_Reached]
		  ,ISNULL([Page_Likes],0) AS [Page_Likes]
		  ,ISNULL([Post_Engagement],0) AS [Post_Engagement]
		  ,ISNULL([Cost_Per_Page_Like],0) AS [Cost_Per_Page_Like]
		  ,ISNULL([Cost_Per_Post_Engagement],0) AS [Cost_Per_Post_Engagement]
		  ,ISNULL([Leads],0) AS [Leads]
		  ,ISNULL([Total_Money_VND],0) AS [Total_Money_VND]
		  ,ISNULL([Sell_Money_VND],0) AS [Sell_Money_VND]
		  ,ISNULL([View],0) AS [View]
		  ,ISNULL([Conversions],0) AS [Conversions]
		  ,ISNULL([CPV],0) AS [CPV]
		  ,[CreationTime]
		  ,[Age]
		  ,[Sex]
		  ,[Regions]
		  ,[CreatedBy] = isnull((SELECT TOP (1) [UserName]
			              FROM ' + @server_id + '.' + @database + '.[dbo].[AbpUsers] u 
						  WHERE odr.[CreatorUserId] = u.[Id]  ORDER BY u.id
						  ),'''')
		  ,[LastModificationTime]
		  ,[LastModifiedBy] =  isnull((SELECT TOP (1) [UserName]
			              FROM ' + @server_id + '.' + @database + '.[dbo].[AbpUsers] u 
						  WHERE odr.[LastModifierUserId] = u.[Id]  ORDER BY u.id
						  ),'''')
		  ,isnull([IsDeleted],0)
		  ,[DeletedBy] = isnull((SELECT TOP (1) [UserName]
						  FROM ' + @server_id + '.' + @database + '.[dbo].[AbpUsers] u 
						  WHERE odr.[DeleterUserId] = u.[Id] ORDER BY u.id
						  ),'''')
		  ,[DeletionTime]
		  ,[Date_result]
		  ,0
	  FROM ' + @server_id + '.' + @database + '.[dbo].[Operating_Result] odr
	  WHERE odr.[LastModificationTime] >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '
	   + ' AND odr.[LastModificationTime]< ' + @daunhay + convert(nvarchar(23),@NgayThucHienNow,121)+ @daunhay+' ' 
	--PRINT @SQL
	EXEC(@SQL)
	--XAC DINH TRANG THAI RECORD
	UPDATE t 
	SET    t.[Status Record] = 1
	FROM  #ADS_Operating_Result t 
	LEFT JOIN dbo.ADS_Operating_Result_log odr  ON t.Id = odr.ADS_Operating_Result_Id
	AND t.LastModificationTime = odr.LastModificationTime
	WHERE odr.id is not null


	-- insert row chưa có
	INSERT INTO [dbo].[ADS_Operating_Result_Log]
           (ADS_Operating_Result_Id
		  ,[Product Id]
		  ,[Product Name]
		  ,[Operating_Order_Id]
		  ,[AdAccount_Name]
		  ,[AdAccount_Id]
		  ,[Campaign_Id]
		  ,[Campaign_Name]
		  ,[Exchange_Rate_Id]
		  ,[Exchange_Rate]
		  ,[Start_Date]
		  ,[Result_Type]
		  ,[Result]
		  ,[Reach]
		  ,[Impression]
		  ,[Amoun_Spent]
		  ,[Frequency]
		  ,[CPC]
		  ,[CTR]
		  ,[Cost_Per_Result]
		  ,[Clicks]
		  ,[CPM]
		  ,[Cost_Per_Thousand_People_Reached]
		  ,[Page_Likes]
		  ,[Post_Engagement]
		  ,[Cost_Per_Page_Like]
		  ,[Cost_Per_Post_Engagement]
		  ,[Leads]
		  ,[Total_Money_VND]
		  ,[Sell_Money_VND]
		  ,[View]
		  ,[Conversions]
		  ,[CPV]
		  ,[CreationTime]
		  ,[Age]
		  ,[Sex]
		  ,[Regions]
		  ,[CreatedBy]
		  ,[LastModificationTime]
		  ,[LastModifiedBy]
		  ,[IsDeleted]
		  ,[DeletedBy]
		  ,[DeletionTime]
		  ,[Date_result]
		  ,[Log_time])
     SELECT 
		   Id
		  ,[Product Id]
		  ,[Product Name]
		  ,[Operating_Order_Id]
		  ,[AdAccount_Name]
		  ,[AdAccount_Id]
		  ,[Campaign_Id]
		  ,[Campaign_Name]
		  ,[Exchange_Rate_Id]
		  ,[Exchange_Rate]
		  ,[Start_Date]
		  ,[Result_Type]
		  ,[Result]
		  ,[Reach]
		  ,[Impression]
		  ,[Amoun_Spent]
		  ,[Frequency]
		  ,[CPC]
		  ,[CTR]
		  ,[Cost_Per_Result]
		  ,[Clicks]
		  ,[CPM]
		  ,[Cost_Per_Thousand_People_Reached]
		  ,[Page_Likes]
		  ,[Post_Engagement]
		  ,[Cost_Per_Page_Like]
		  ,[Cost_Per_Post_Engagement]
		  ,[Leads]
		  ,[Total_Money_VND]
		  ,[Sell_Money_VND]
		  ,[View]
		  ,[Conversions]
		  ,[CPV]
		  ,[CreationTime]
		  ,[Age]
		  ,[Sex]
		  ,[Regions]
		  ,[CreatedBy]
		  ,[LastModificationTime]
		  ,[LastModifiedBy]
		  ,[IsDeleted]
		  ,[DeletedBy]
		  ,[DeletionTime]
		  ,[Date_result]
		  ,GETDATE()
     FROM #ADS_Operating_Result
	 WHERE [Status Record] = 0
	 
	 DROP TABLE #ADS_Operating_Result

END

```
