# Stored Procedure: `Sp_Check_GiaTriLechCacTruongTrenDotChayChiTietHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-22 17:19:22.173000
- **Ngày sửa cuối**: 2017-03-11 09:40:46.017000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--[Sp_Check_GiaTriLechCacTruongTrenDotChayChiTietHopDong] '',''
CREATE PROCEDURE [dbo].[Sp_Check_GiaTriLechCacTruongTrenDotChayChiTietHopDong]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.DotChayChiTietHopDongChiTiet
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
				DotChayID INT	,
				BookingID INT	,
				tungay	DATETIME,
				dengay	DATETIME,
				SoLuong	NVARCHAR(1000),
				LastModifiedAt DATETIME
            )

        DECLARE @SQL NVARCHAR(MAX) 
		
        SET @SQL = 'select A.*,B.tungay,B.dengay from hdcn_DotChay_ChiTiet A INNER JOIN hdcn_dotchay B On A.DotChayID=B.id
					WHERE CAST(IF (A.LastModifiedAt = ''''0000-00-00'''' OR A.LastModifiedAt = ''''0001-01-01'''' OR A.LastModifiedAt IS NULL,IFNULL(A.CreatedAt, ''''2010-01-01''''),A.LastModifiedAt) AS DATE) between '''''
					+ CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
					+ CONVERT(NVARCHAR(20), @LastSynTime, 120) + ''''';'
        SET @SQL = '
					SELECT id,
					DotChayID,
					BookingID,
					Tungay,
					Dengay,
					SoLuong,
					ISNULL(LastModifiedAt,CreatedAt) LastModifiedAt 
					FROM OPENQUERY(MySQL,''' + @SQL + ''') 
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
		SET @TotalRows  = (SELECT Max(STT) FROM ColumnCheckValue WHERE DoiTuong=N'Đợt chạy chi tiết hợp đồng chi tiết')
		SET @x=(SELECT MIN(STT) FROM ColumnCheckValue WHERE DoiTuong=N'Đợt chạy chi tiết hợp đồng chi tiết')
		WHILE @x<=@TotalRows
		BEGIN
			SELECT @ColumnSQL = ColumnSQL FROM ColumnCheckValue A WHERE STT=@x AND DoiTuong=N'Đợt chạy chi tiết hợp đồng chi tiết'
			SELECT @ColumnMySQL = ColumnMySQL FROM ColumnCheckValue A WHERE STT=@x AND DoiTuong=N'Đợt chạy chi tiết hợp đồng chi tiết'
			SELECT @DoiTuong = DoiTuong FROM ColumnCheckValue WHERE STT=@x AND DoiTuong=N'Đợt chạy chi tiết hợp đồng chi tiết'
			SET @SQL = '
			SELECT  '''+@ColumnSQL+''' [Column], 
					N'''+@DoiTuong+''' DoiTuong, 
					B.DotChayChiTietHopDongChiTietID,
					B.'+@ColumnSQL+' DulieuSQL,
					A.'+@ColumnMySQL+' DulieuMySQL,
					''Lech du lieu'' LoaiVanDe,
					'''+CONVERT(NVARCHAR(100),GETDATE(),113)+''' ThoiGianLog,
					0 TrangThaiXuLy,
					14 IDLoai
			FROM    #HopDongTemp A FULL JOIN
			(
			SELECT  *
			FROM    dbo.DotChayChiTietHopDongChiTiet
			WHERE   CONVERT(DATE,LastModifiedAt) BETWEEN  '''+CONVERT(NVARCHAR(100),@FromDate,113)+''' AND '''+CONVERT(NVARCHAR(100), @LastSynTime ,113)+'''
			) B ON A.id=B.DotChayChiTietHopDongChiTietID
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
