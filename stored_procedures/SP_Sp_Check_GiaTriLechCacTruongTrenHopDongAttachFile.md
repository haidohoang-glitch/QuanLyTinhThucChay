# Stored Procedure: `Sp_Check_GiaTriLechCacTruongTrenHopDongAttachFile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-23 09:47:37.133000
- **Ngày sửa cuối**: 2017-03-11 09:42:00.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--[Sp_Check_GiaTriLechCacTruongTrenHopDongAttachFile] '',''
CREATE PROCEDURE [dbo].[Sp_Check_GiaTriLechCacTruongTrenHopDongAttachFile]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.HopDongAttachFile
                              )

        IF @NgayKetThuc = ''
            SET @LastSynTime = GETDATE()
        ELSE
            SET @LastSynTime = @NgayKetThuc
        IF @NgayBatDau = ''
            SET @FromDate = DATEADD(DD, -2, @LastSynTime)
        ELSE
            SET @FromDate = @NgayBatDau
      
		
		
        CREATE TABLE #HopDongTemp
            (	id INT,
				hd_id INT,
				filetypeID INT,
				fileName NVARCHAR(max),
				LastModifiedAt DATETIME
            )

        DECLARE @SQL NVARCHAR(MAX) 
		
        SET @SQL = 'select id,
					hd_id,
					filetypeID,
					fileName,
					LastModifiedAt
					from hdcn_attachfiles A 
					WHERE CAST(IF (A.LastModifiedAt = ''''0000-00-00'''' OR A.LastModifiedAt = ''''0001-01-01'''' OR A.LastModifiedAt IS NULL,IFNULL(A.CreatedAt, ''''2010-01-01''''),A.LastModifiedAt) AS DATE) between '''''
					+ CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
					+ CONVERT(NVARCHAR(20), @LastSynTime, 120) + ''''';'
        SET @SQL = 'SELECT * FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #HopDongTemp
                EXECUTE ( @SQL
                       )
					   --SELECT * FROM #HopDongTemp
		DECLARE @TotalRows INT
		DECLARE @x INT
		DECLARE @ColumnSQL NVARCHAR(500)
		DECLARE @ColumnMySQL NVARCHAR(500)
		DECLARE @DoiTuong NVARCHAR(500)
		SET @TotalRows  = (SELECT Max(STT) FROM ColumnCheckValue WHERE DoiTuong=N'Hợp đồng AttachFile')
		SET @x=(SELECT MIN(STT) FROM ColumnCheckValue WHERE DoiTuong=N'Hợp đồng AttachFile')
		WHILE @x<=@TotalRows
		BEGIN
			SELECT @ColumnSQL = ColumnSQL FROM ColumnCheckValue A WHERE STT=@x AND DoiTuong=N'Hợp đồng AttachFile'
			SELECT @ColumnMySQL = ColumnMySQL FROM ColumnCheckValue A WHERE STT=@x AND DoiTuong=N'Hợp đồng AttachFile'
			SELECT @DoiTuong = DoiTuong FROM ColumnCheckValue WHERE STT=@x AND DoiTuong=N'Hợp đồng AttachFile'
			SET @SQL = '
			SELECT  '''+@ColumnSQL+''' [Column], 
					N'''+@DoiTuong+''' DoiTuong, 
					B.HopDongAttachFileID,
					B.'+@ColumnSQL+' DulieuSQL,
					A.'+@ColumnMySQL+' DulieuMySQL,
					''Lech du lieu'' LoaiVanDe,
					'''+CONVERT(NVARCHAR(100),GETDATE(),113)+''' ThoiGianLog,
					0 TrangThaiXuLy,
					14 IDLoai
			FROM    #HopDongTemp A FULL JOIN
			(
			SELECT  *
			FROM    dbo.HopDongAttachFile
			WHERE   CONVERT(DATE,LastModifiedAt) BETWEEN  '''+CONVERT(NVARCHAR(100),@FromDate,113)+''' AND '''+CONVERT(NVARCHAR(100), @LastSynTime ,113)+'''
			) B ON A.id=B.HopDongAttachFileID
			WHERE 1=1 
			AND B.'+@ColumnSQL+'<> A.'+@ColumnMySQL+'
			AND a.LastModifiedAt <='''+CONVERT(NVARCHAR(50),@MaxTimeSynInHD,113)+''''
			PRINT @SQL
			INSERT INTO CheckThongTinDauVao
			EXECUTE(@SQL)
			SET @x = @x+1
		END
		
    END
	--[Sp_Check_GiaTriLechCacTruongTrenDotChayHopDong] '',''

```
