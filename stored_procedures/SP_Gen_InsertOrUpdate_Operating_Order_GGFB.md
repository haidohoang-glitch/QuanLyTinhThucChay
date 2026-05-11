# Stored Procedure: `Gen_InsertOrUpdate_Operating_Order_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-07 15:59:17.413000
- **Ngày sửa cuối**: 2025-11-03 17:39:26.860000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_Operating_Order_GGFB] 	
AS	
BEGIN

DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''
, @NgayThucHienNow DATETIME = GETDATE()

	SET @server_id =
		(SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id)

	SET @database= 
		(SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'GGFB' ORDER BY id)
	SET @NgayThucHien = 
		ISNULL((
			SELECT MAX([LastModificationTime])   
			FROM   dbo.[ADS_Operating_Order]  
		),'1900-01-01')

	SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)

	--SET @NgayThucHien = '2025-10-25'

	CREATE TABLE #ADS_Operating_Order(
		[Id] [int]  NOT NULL,
		[Code] [nvarchar](100) NULL,                -- mã vận hành
		[Contract_Id] [int] NULL,
		[Contract_Number] [varchar](100) NULL,
		[Submitting_Number] [nvarchar](500) NULL,   -- số tờ trình
		[Contract_Detail_Id] [int] NULL,   
		[Product_Id] [int] NULL,
		[Brand_id] [int] NULL,
		[Money_Turnover] [money] NULL,              -- giá trị bán
		[From_Date] [datetime] NULL,                
		[To_Date] [datetime] NULL,
		[Campaign_Type] [int] NULL,                 -- loại chiến lược, hình thức chạy
		[KPI] [decimal](18, 4) NULL,                -- KPI
		[Team] [nvarchar](100) NULL,                     -- team vận hành
		[SetupBy] [nvarchar](100) NULL,                    -- người chạy quảng cáo
		[Start_Time] [datetime] NULL,               -- ngày bắt đầu
		[Receive_Time] [datetime] NULL,             -- ngày tiếp nhận
		[ReceivedBy] [nvarchar](100) NULL,                 -- người tiếp nhận
		[Units] [nvarchar](200) NULL,                    -- đơn vị
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
		  ,[DmWebsiteREF]) '

		  SET @SQL +=
	'
	SELECT [Id]
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
				   FROM ' + @server_id + '.' + @database + '.dbo.[D_Teams] t
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
		  ,[website_id]   
	FROM ' + @server_id + '.' + @database + '.[dbo].[Operating_Order] od
	WHERE od.[LastModificationTime] >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '
	 + ' AND od.[LastModificationTime]< ' + @daunhay + convert(nvarchar(23),@NgayThucHienNow,121)+ @daunhay+' ' 
	
	PRINT @SQL
	EXEC(@SQL)

	UPDATE t 
	SET    t.[Status_Record] = 1
	FROM  #ADS_Operating_Order t 
	LEFT JOIN dbo.ADS_Operating_Order dc ON t.Id = dc.id
	WHERE dc.Id is not null

	-- Update nhung row da ton ton                                      
	UPDATE D
	SET
			[Id] =  S.[Id],
			[Code] =   S.[Code] ,
			[Contract_Id] =  S.[Contract_Id],
			[Contract_Number] =  S.[Contract_Number],
			[Submitting_Number] = S.[Submitting_Number],
			[Contract_Detail_Id] =  S.[Contract_Detail_Id],
			[Product_Id] =  S.[Product_Id],
			[Brand_id] =  S.[Brand_id],
			[Money_Turnover] =  S.[Money_Turnover],
			[From_Date] = S.[From_Date],
			[To_Date] =  S.[To_Date],
			[Campaign_Type] =  S.[Campaign_Type],
			[KPI] =  S.[KPI],
			[Team] =  S.[Team],
			[SetupBy] =  S.[SetupBy],
			[Start_Time] = S.[Start_Time] ,
			[Receive_Time] =  S.[Receive_Time],
			[ReceivedBy] =  S.[ReceivedBy],
			[Units] = S.[Units] ,
			[ProfitRate] = S.[ProfitRate] ,
			[Note] = S.[Note],
			[Status] =  S.[Status],
			[CreationTime] =  S.[CreationTime],
			[CreatedBy] = S.[CreatedBy],
			[LastModificationTime] = S.[LastModificationTime],
			[LastModifiedBy] = S.[LastModifiedBy],
			[IsDeleted] = S.[IsDeleted],
			[Deletedby] = S.[Deletedby],
			[DeletionTime] =  S.[DeletionTime],
			[DmWebsiteREF] = S.[DmWebsiteREF]
	FROM  [dbo].[ADS_Operating_Order] D
	LEFT JOIN #ADS_Operating_Order S ON D.ID = S.ID 
	WHERE S.[Status_record] =1

	-- insert row chưa có
	INSERT INTO [dbo].[ADS_Operating_Order]
           ([Id]
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
		   ,[DmWebsiteREF]
     FROM #ADS_Operating_Order
	 WHERE Status_record = 0
	 
	 DROP TABLE #ADS_Operating_Order

END

```
