# Stored Procedure: `Gen_InsertOrUpdate_DmLoaiHopDongNoiBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-06 10:42:42.690000
- **Ngày sửa cuối**: 2025-10-06 10:52:27.257000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmLoaiHopDongNoiBo]

AS
BEGIN
	DECLARE @MaxLogTime DATETIME
	DECLARE @SQL NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''

	SET @MaxLogTime =
	ISNULL((
			SELECT max(LastModifiedAt)
			FROM   dbo.DmLoaiHopDongNoiBo  dchdct
			),'2010-01-01')
	
	SET @server_id =
	ISNULL((SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'ABM_DATA_RELEASE' ORDER BY id),'')

	SET @database= 
	ISNULL((SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'ABM_DATA_RELEASE' ORDER BY id),'')

	--SET @MaxLogTime = DATEADD(HOUR,-8,@MaxLogTime)
	--PRINT @NgayThucHien


	CREATE TABLE #DmLoaiHopDongNoiBo(
		[DmLoaiHopDongNoiBoID] [int] NOT NULL,
		[TenLoaiHopDongNoiBo] [nvarchar](100) NULL,
		[MaLoaiHopDong] [nvarchar](50) NULL,
		[DmLoaiHopDongREF] [int] NULL,
		[ThoiGiaBatDauHieuLuc] [date] NULL,
		[ThoiGianKetThucHieuLuc] [date] NULL,
		[CreateAt] [datetime] NOT NULL,
		[CreatedBy] [nvarchar](100) NOT NULL,
		[LastModifiedBy] [nvarchar](100) NOT NULL,
		[LastModifiedAt] [datetime] NOT NULL,
		[DeletedStatus] [int] NOT NULL,
		[PrintStatus] [int] NOT NULL,
		[RecordStatus] [int] NOT NULL,
		status_record INT
		)
	


	SET @SQL =
	'INSERT INTO #DmLoaiHopDongNoiBo '
	SET @SQL +=
	'SELECT	 
		  [DmLoaiHopDongNoiBoID]
		  ,[TenLoaiHopDongNoiBo]
		  ,[MaLoaiHopDong]
		  ,[DmLoaiHopDongREF]
		  ,[ThoiGiaBatDauHieuLuc]
		  ,[ThoiGianKetThucHieuLuc]
		  ,[CreateAt]
		  ,[CreatedBy]
		  ,[LastModifiedBy]
		  ,[LastModifiedAt]
		  ,[DeletedStatus]
		  ,[PrintStatus]
		  ,[RecordStatus]
		  ,0 AS status_record
	FROM   ' + @server_id + '.' + @database + '.dbo.DmLoaiHopDongNoiBo ctdl
	WHERE  ctdl.LastModifiedAt > ' + @daunhay + convert(nvarchar(23),@MaxLogTime,121)+ @daunhay+' '

	--PRINT @SQL
	EXEC(@SQL)

	--UPDATE TRANG THAI
	UPDATE L
	SET L.status_record = 1
	FROM #DmLoaiHopDongNoiBo L 
	INNER JOIN dbo.DmLoaiHopDongNoiBo h on L.DmLoaiHopDongNoiBoID = h.DmLoaiHopDongNoiBoID
	
	--UPDATE RECORD
	UPDATE h
	   SET h.[TenLoaiHopDongNoiBo] = L.TenLoaiHopDongNoiBo
		  ,h.[MaLoaiHopDong] = L.MaLoaiHopDong
		  ,h.[DmLoaiHopDongREF] = L.DmLoaiHopDongREF
		  ,h.[ThoiGiaBatDauHieuLuc] = L.ThoiGiaBatDauHieuLuc
		  ,h.[ThoiGianKetThucHieuLuc] = L.ThoiGianKetThucHieuLuc
		  ,h.[LastModifiedBy] = L.LastModifiedBy
		  ,h.[LastModifiedAt] = L.LastModifiedAt
		  ,h.[DeletedStatus] = L.DeletedStatus
		  ,h.[RecordStatus] = L.RecordStatus
	FROM #DmLoaiHopDongNoiBo L 
	INNER JOIN dbo.DmLoaiHopDongNoiBo h on L.DmLoaiHopDongNoiBoID = h.DmLoaiHopDongNoiBoID
	WHERE L.status_record = 1



	--INSERT INTO
	INSERT INTO [dbo].[DmLoaiHopDongNoiBo]
			   ([DmLoaiHopDongNoiBoID]
			   ,[TenLoaiHopDongNoiBo]
			   ,[MaLoaiHopDong]
			   ,[DmLoaiHopDongREF]
			   ,[ThoiGiaBatDauHieuLuc]
			   ,[ThoiGianKetThucHieuLuc]
			   ,[CreateAt]
			   ,[CreatedBy]
			   ,[LastModifiedBy]
			   ,[LastModifiedAt]
			   ,[DeletedStatus]
			   ,[PrintStatus]
			   ,[RecordStatus])
	SELECT [DmLoaiHopDongNoiBoID]
		  ,[TenLoaiHopDongNoiBo]
		  ,[MaLoaiHopDong]
		  ,[DmLoaiHopDongREF]
		  ,[ThoiGiaBatDauHieuLuc]
		  ,[ThoiGianKetThucHieuLuc]
		  ,[CreateAt]
		  ,[CreatedBy]
		  ,[LastModifiedBy]
		  ,[LastModifiedAt]
		  ,[DeletedStatus]
		  ,[PrintStatus]
		  ,[RecordStatus]
	  FROM #DmLoaiHopDongNoiBo
	  WHERE status_record = 0

	DROP TABLE #DmLoaiHopDongNoiBo

END

```
