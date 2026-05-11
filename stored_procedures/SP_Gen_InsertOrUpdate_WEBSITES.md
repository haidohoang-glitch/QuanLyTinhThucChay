# Stored Procedure: `Gen_InsertOrUpdate_WEBSITES`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-19 11:22:15.260000
- **Ngày sửa cuối**: 2022-06-06 17:05:11.557000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_WEBSITES]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_WEBSITES]
As 	
BEGIN
    DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(3500)
	,@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''

	SET @NgayThucHien = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   DBO.DMWEBSITE dchdct
		),'2010-01-01')

	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'CONTRACT' ORDER BY id),'')

	set @NgayThucHien = DATEADD(day,-1,@NgayThucHien)


CREATE TABLE #DmWebsite(
	[DmWebsiteID] [int] NOT NULL,
	[TenWebsite] [nvarchar](200) NULL,
	[WebsiteLink] [nvarchar](255) NULL,
	[GhiChu] [nvarchar](4000) NULL,
	[Code] [nvarchar](200) NULL,
	[DmGroupTypeREF] [int] NULL,
	[IsThuongMaiDienTu] [int] NULL,
	[CreatedBy] [nvarchar](50) NOT NULL,
	[CreatedAt] [datetime] NOT NULL,
	[LastModifiedBy] [nvarchar](50) NOT NULL,
	[LastModifiedAt] [datetime] NOT NULL,
	[DeletedStatus] [int] NOT NULL,
	[PrintStatus] [int] NOT NULL,
	[RecordStatus] [int] NOT NULL,
	[DomainWebsite] [nvarchar](200) NULL,
	[Status_record] int)

	SET @SQL =
	'INSERT INTO #DmWebsite
           ([DmWebsiteID]
           ,[TenWebsite]
           ,[WebsiteLink]
           ,[GhiChu]
           ,[Code]
           ,[DmGroupTypeREF]
           ,[IsThuongMaiDienTu]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
           ,[DeletedStatus]
           ,[PrintStatus]
           ,[RecordStatus]
           ,[DomainWebsite]
		   ,[Status_record])  SELECT [ID]
      ,[NAME]
      ,[DOMAIN]
	  , '''' AS GHICHU
	  , '''' AS CODE
	  , 0 AS DMGROUPTYPEREF
	  , 0 AS IsThuongMaiDienTu
	  ,[CREATED_BY]
      ,[CREATED_AT]
      ,[LAST_MODIFIED_BY]
      ,[LAST_MODIFIED_AT]
	  ,[DELETED_STATUS]
	  , 0 as [PrintStatus]
      ,[RECORD_STATUS]
	  ,[DOMAIN]
	  , 0 AS Status_Record
	  FROM	 ' + @server_id + '.' + @database + '.dbo.WEBSITES D
	  WHERE D.[LAST_MODIFIED_AT] >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '

	  --print len(@sql)
	  EXEC(@SQL)	


	  --print @SQL
	  --CAP NHAP TRANG THAI BAN GHI
	  UPDATE W
	  SET W.Status_record = 1 
	  FROM #DmWebsite W INNER JOIN
	  DmWebsite DW ON W.DmWebsiteID = DW.DmWebsiteID

	  select * from  #DmWebsite

	 --UPDATE THONG TIN
		UPDATE DW
	   SET DW.[TenWebsite] = W.TenWebsite
		  ,DW.[WebsiteLink] = W.[WebsiteLink]
		  ,DW.[LastModifiedBy] = W.[LastModifiedBy]
		  ,DW.[LastModifiedAt] = W.[LastModifiedAt]
		  ,DW.[DeletedStatus] = W.[DeletedStatus]
		  ,DW.[DomainWebsite] = W.[DomainWebsite]
	  FROM #DmWebsite W INNER JOIN
	  DBO.DmWebsite DW ON W.DmWebsiteID = DW.DmWebsiteID
	  WHERE W.Status_record = 1

	  ---INSERT THONG TIN
	  INSERT INTO DBO.DMWEBSITE
           ([DmWebsiteID]
           ,[TenWebsite]
           ,[WebsiteLink]
           ,[GhiChu]
           ,[Code]
           ,[DmGroupTypeREF]
           ,[IsThuongMaiDienTu]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
           ,[DeletedStatus]
           ,[PrintStatus]
           ,[RecordStatus]
           ,[DomainWebsite] )

		   SELECT [DmWebsiteID]
           ,[TenWebsite]
           ,[WebsiteLink]
           ,[GhiChu]
           ,[Code]
           ,[DmGroupTypeREF]
           ,[IsThuongMaiDienTu]
           ,[CreatedBy]
           ,[CreatedAt]
           ,[LastModifiedBy]
           ,[LastModifiedAt]
           ,[DeletedStatus]
           ,[PrintStatus]
           ,[RecordStatus]
           ,[DomainWebsite] FROM #DmWebsite W
		   WHERE W.Status_record = 0

		DROP TABLE #DmWebsite
END



```
