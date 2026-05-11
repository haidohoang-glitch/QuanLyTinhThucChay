# Stored Procedure: `Gen_InsertOrUpdate_PMS_QuanLyThucChay_Account`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-11-10 15:42:54.010000
- **Ngày sửa cuối**: 2021-10-27 16:53:11.320000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_PMS_QuanLyThucChay_Account]
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_PMS_QuanLyThucChay_Account]
As 	
BEGIN
    DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''
	SET @NgayThucHien = 
	ISNULL((
			SELECT MAX(dchdct.LastmodificationTime)
			FROM   DBO.PMS_QuanLyThucChay_Account dchdct
		),'2010-01-01')

	SET @server_id =
	(SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCCHAY_ACCOUNT' ORDER BY id)

	SET @database= 
	(SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCCHAY_ACCOUNT' ORDER BY id)

	set @NgayThucHien = DATEADD(day,-1,@NgayThucHien)

	PRINT @NgayThucHien


CREATE TABLE #PMS_QuanLyThucChay_Account(
	[Id] [int] NOT NULL,
	[B_QuanLyThucChayREF] [int] NULL,
	[D_NhanSuREF] [int] NULL,
	[CreationTime] [datetime2](7) NULL,
	[CreatorUserId] [bigint] NULL,
	[LastModificationTime] [datetime2](7) NULL,
	[LastModifierUserId] [bigint] NULL,
	[IsDeleted] [bit] NOT NULL,
	[RecordStatus] smallint
)

SET @SQL =
	'INSERT INTO #PMS_QuanLyThucChay_Account
           ([Id]
           ,[B_QuanLyThucChayREF]
           ,[D_NhanSuREF]
           ,[CreationTime]
           ,[CreatorUserId]
           ,[LastModificationTime]
           ,[LastModifierUserId]
           ,[IsDeleted]
		   ,[RecordStatus]) '
SET @SQL += 
	'SELECT [Id]
		,[B_QuanLyThucChayREF]
		,[D_NhanSuREF]
		,[CreationTime]
		,[CreatorUserId]
		,[LastModificationTime]
		,[LastModifierUserId]
		,[IsDeleted]
		,0 [RecordStatus]
	FROM  ' + @server_id + '.' + @database + '.dbo.B_QuanLyThucChay_Account
	where [LastModificationTime] >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '

	--PRINT @SQL
	EXEC(@SQL)

	-- Set trang thai = 1 doi voi nhung truong hop sua chua 
	UPDATE t
	SET t.[RecordStatus] = 1
	FROM  #PMS_QuanLyThucChay_Account t 
	INNER JOIN dbo.PMS_QuanLyThucChay_Account  dc
	ON t.Id = dc.id
	WHERE 1=1

	-- UPDATE GIA TRI CHO NHUNG BAN GHI DA TON TAI  
	UPDATE dc
	   SET dc.[B_QuanLyThucChayREF] = t.B_QuanLyThucChayREF
		  ,dc.[D_NhanSuREF] = t.D_NhanSuREF
		  ,dc.[CreationTime] = t.CreationTime
		  ,dc.[CreatorUserId] = t.CreatorUserId
		  ,dc.[LastModificationTime] = t.LastModificationTime
		  ,dc.[LastModifierUserId] = t.LastModifierUserId
		  ,dc.[IsDeleted] = t.IsDeleted
	FROM  #PMS_QuanLyThucChay_Account t 
	INNER JOIN dbo.PMS_QuanLyThucChay_Account  dc ON t.Id = dc.id
	WHERE t.[RecordStatus] = 1

	-- INSERT ROW CHUA TON TAI
	INSERT INTO [dbo].[PMS_QuanLyThucChay_Account]
           ([Id]
           ,[B_QuanLyThucChayREF]
           ,[D_NhanSuREF]
           ,[CreationTime]
           ,[CreatorUserId]
           ,[LastModificationTime]
           ,[LastModifierUserId]
           ,[IsDeleted])

	SELECT [Id]
		,[B_QuanLyThucChayREF]
		,[D_NhanSuREF]
		,[CreationTime]
		,[CreatorUserId]
		,[LastModificationTime]
		,[LastModifierUserId]
		,[IsDeleted]
	FROM #PMS_QuanLyThucChay_Account
	WHERE [RecordStatus] = 0

END



```
