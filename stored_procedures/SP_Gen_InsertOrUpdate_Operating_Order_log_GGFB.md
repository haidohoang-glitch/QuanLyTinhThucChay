# Stored Procedure: `Gen_InsertOrUpdate_Operating_Order_log_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-25 10:13:59.070000
- **Ngày sửa cuối**: 2025-10-24 09:47:13.490000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_Operating_Order_log_GGFB] 	
AS	
BEGIN

DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''
	SET @NgayThucHien = 
		ISNULL((
			SELECT MAX([LastModificationTime])   
			FROM   dbo.[ADS_Operating_Order_log]  
		),'1900-01-01')

	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id),'')

	SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)

	--SET @NgayThucHien = '2025-10-25'

	CREATE TABLE #ADS_Operating_Order(
		[Id] [int]  NOT NULL,
		[Code] [nvarchar](500) NULL,                -- mã vận hành
		[Contract_Id] [int] NULL,
		[Contract_Number] [varchar](1000) NULL,
		[Submitting_Number] [nvarchar](500) NULL,   -- số tờ trình
		[Contract_Detail_Id] [int] NULL,   
		[Product_Id] [int] NULL,
		[Brand_id] [int] NULL,
		[Money_Turnover] [money] NULL,              -- giá trị bán
		[From_Date] [datetime] NULL,                
		[To_Date] [datetime] NULL,
		[Campaign_Type] [int] NULL,                 -- loại chiến lược, hình thức chạy
		[KPI] [decimal](18, 4) NULL,                -- KPI
		[Team] [nvarchar](500) NULL,                     -- team vận hành
		[SetupBy] [nvarchar](100) NULL,                    -- người chạy quảng cáo
		[Start_Time] [datetime] NULL,               -- ngày bắt đầu
		[Receive_Time] [datetime] NULL,             -- ngày tiếp nhận
		[ReceivedBy] [nvarchar](100) NULL,                 -- người tiếp nhận
		[Units] [nvarchar](500) NULL,                    -- đơn vị
		[ProfitRate] [decimal](18, 4) NULL,         -- tỉ lệ lợi nhuận
		[Note] [nvarchar](2000) NULL,
		[Status] [int] NULL,                        -- trạng thái xử lý
		[CreationTime] [datetime2](7) NULL,
		[CreatedBy] [nvarchar](100) NULL,
		[LastModificationTime] [datetime2](7) NULL,
		[LastModifiedBy] [nvarchar](100) NULL,
		[IsDeleted] [smallint] NOT NULL,
		[Deletedby] [nvarchar](100) NULL,
		[DeletionTime] [datetime2](7) NULL,
		[Status_Record] int not null,
		[DmWebsiteREF] INT NULL
	)

	SET @SQL =
	'INSERT INTO #ADS_Operating_Order
	(      [Id]
		  ,[Code]
		  ,[Contract_Id]
		  ,[Contract_Number]
		  ,[Submitting_Number]
		  ,[Contract_Detail_Id]
		  ,[Product_Id]
		  ,[Brand_id]
		  ,[Money_Turnover]
		  ,[From_Date]
		  ,[To_Date]
		  ,[Campaign_Type]
		  ,[KPI]
		  ,[Team]
		  ,[SetupBy]
		  ,[Start_Time]
		  ,[Receive_Time]
		  ,[ReceivedBy]
		  ,[Units]
		  ,[ProfitRate]
		  ,[Note]
		  ,[Status]
		  ,[CreationTime]
		  ,[CreatedBy]
		  ,[LastModificationTime]
		  ,[LastModifiedBy]
		  ,[IsDeleted]
		  ,[Deletedby]
		  ,[DeletionTime]
		  ,[Status_Record]
		  ,[DmWebsiteREF] ) '

	SET @SQL +=
	'SELECT [Id]
		  ,[Code]
		  ,[Contract_Id]
		  ,[Contract_Number]
		  ,[Submitting_Number]
		  ,[Contract_Detail_Id]
		  ,[Product_Id]
		  ,[Brand_id]
		  ,[Money_Turnover]
		  ,[From_Date]
		  ,[To_Date]
		  ,[Campaign_Type]
		  ,[KPI]
		  ,Team = isnull((select TOP (1) t.[Name]
				   from ' + @server_id + '.' + @database + '.dbo.[D_Teams] t
				   where t.id = od.D_team_id order by t.id),'''')
		  ,[Setup_User] =    isnull((select top (1) u.[Name]
							  from ' + @server_id + '.' + @database + '.dbo.AbpUsers u
							  where u.id = od.[Setup_User_Id] order by u.id),'''')
		  ,[Start_Date]
		  ,[Receive_Date]
		  ,[Receive_User] =  isnull((select top (1) u.[Name]
							  from ' + @server_id + '.' + @database + '.dbo.AbpUsers u
							  where u.id = od.[Receive_User_id] order by u.id),'''')
		  ,[Units]   =       isnull((select top (1) u.[Unit_Name]
							  from ' + @server_id + '.' + @database + '.dbo.D_Units u
							  where u.id = od.[D_Units_Id] order by u.id),'''')
		  ,[ProfitRate]
		  ,[Note]
		  ,[Status]
		  ,[CreationTime]
		  ,[CreatorUser] =  isnull((select top (1) u.[Name]
							   from ' + @server_id + '.' + @database + '.dbo.AbpUsers u
							   where u.id = od.[CreatorUserId] order by u.id),'''')
		  ,[LastModificationTime]
		  ,[LastModifierUser] = isnull((select top(1) u.[Name]
								   from ' + @server_id + '.' + @database + '.dbo.AbpUsers u
								   where u.id = od.[LastModifierUserId] order by u.id),'''')
		  ,[IsDeleted]
		  ,[DeleterUser] =        isnull((select top (1) u.[Name]
								   from ' + @server_id + '.' + @database + '.dbo.AbpUsers u
								   where u.id = od.[DeleterUserId] order by u.id),'''')
		  ,[DeletionTime]
		  ,0    
		  ,website_id 
	FROM ' + @server_id + '.' + @database + '.[dbo].[Operating_Order] od
	WHERE od.[LastModificationTime] >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '

	--PRINT @SQL
	EXEC(@SQL)


	UPDATE t 
	SET    t.DmWebsiteREF = 265
	FROM  #ADS_Operating_Order t 
	WHERE (t.DmWebsiteREF is null) or (t.DmWebsiteREF = 0)

	--XAC DINH TRANG THAI CUA RECORD
	UPDATE t 
	SET    t.[Status_Record] = 1
	FROM  #ADS_Operating_Order t 
	LEFT JOIN dbo.ADS_Operating_Order_Log dc ON t.Id = dc.ADS_Operating_Order_Id
	AND t.LastModificationTime = dc.LastModificationTime
	WHERE dc.Id is not null

	
	-- insert row chưa có
	INSERT INTO [dbo].[ADS_Operating_Order_Log]
           ([ADS_Operating_Order_Id]
           ,[Code]
           ,[Contract_Id]
           ,[Contract_Number]
           ,[Submitting_Number]
           ,[Contract_Detail_Id]
           ,[Product_Id]
           ,[Brand_id]
           ,[Money_Turnover]
           ,[From_Date]
           ,[To_Date]
           ,[Campaign_Type]
           ,[KPI]
           ,[Team]
           ,[SetupBy]
           ,[Start_Time]
           ,[Receive_Time]
           ,[ReceivedBy]
           ,[Units]
           ,[ProfitRate]
           ,[Note]
           ,[Status]
           ,[CreationTime]
           ,[CreatedBy]
           ,[LastModificationTime]
           ,[LastModifiedBy]
           ,[IsDeleted]
           ,[Deletedby]
           ,[DeletionTime]
		   ,[Log_time]
		   ,[DmWebsiteREF])
     SELECT 
            [Id]
           ,[Code]
           ,[Contract_Id]
           ,[Contract_Number]
           ,[Submitting_Number]
           ,[Contract_Detail_Id]
           ,[Product_Id]
           ,[Brand_id]
           ,[Money_Turnover]
           ,[From_Date]
           ,[To_Date]
           ,[Campaign_Type]
           ,[KPI]
           ,[Team]
           ,[SetupBy]
           ,[Start_Time]
           ,[Receive_Time]
           ,[ReceivedBy]
           ,[Units]
           ,[ProfitRate]
           ,[Note]
           ,[Status]
           ,[CreationTime]
           ,[CreatedBy]
           ,[LastModificationTime]
           ,[LastModifiedBy]
           ,[IsDeleted]
           ,[Deletedby]
           ,[DeletionTime]
		   ,GETDATE()
		   ,[DmWebsiteREF]
     FROM #ADS_Operating_Order
	 WHERE Status_record = 0
	 
	 DROP TABLE #ADS_Operating_Order

END

```
