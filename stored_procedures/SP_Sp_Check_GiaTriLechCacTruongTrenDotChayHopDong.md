# Stored Procedure: `Sp_Check_GiaTriLechCacTruongTrenDotChayHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-22 15:35:41.867000
- **Ngày sửa cuối**: 2017-03-11 09:41:26.250000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--[Sp_Check_GiaTriLechCacTruongTrenDotChayHopDong] '',''
CREATE PROCEDURE [dbo].[Sp_Check_GiaTriLechCacTruongTrenDotChayHopDong]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.DotChayHopDongChiTiet
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
				hd_id INT	,
				phanbosite_id INT	,
				tungay	DATETIME,
				dengay	DATETIME,
				booking_id	NVARCHAR(1000),
				LastModifiedAt DATETIME
            )

        DECLARE @SQL NVARCHAR(MAX) 
		
        SET @SQL = 'select * FROM hdcn_dotchay where CONVERT(IFNULL(LastModifiedAt,CreatedAt),DATE) between '''''
            + CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
            + CONVERT(NVARCHAR(20), @LastSynTime, 120) + ''''';'
        SET @SQL = '
					SELECT id,
					hd_id	,
					phanbosite_id	,
					tungay	,
					dengay	,
					booking_id,
					ISNULL(LastModifiedAt,CreatedAt) LastModifiedAt 
					FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #HopDongTemp
                EXECUTE ( @SQL
                       )
		DECLARE @TotalRows INT
		DECLARE @x INT
		DECLARE @ColumnSQL NVARCHAR(500)
		DECLARE @ColumnMySQL NVARCHAR(500)
		DECLARE @DoiTuong NVARCHAR(500)
		SET @TotalRows  = (SELECT Max(STT) FROM ColumnCheckValue WHERE DoiTuong=N'Đợt chạy hợp đồng chi tiết')
		SET @x=(SELECT MIN(STT) FROM ColumnCheckValue WHERE DoiTuong=N'Đợt chạy hợp đồng chi tiết')
		WHILE @x<=@TotalRows
		BEGIN
			SELECT @ColumnSQL = ColumnSQL FROM ColumnCheckValue A WHERE STT=@x AND DoiTuong=N'Đợt chạy hợp đồng chi tiết'
			SELECT @ColumnMySQL = ColumnMySQL FROM ColumnCheckValue A WHERE STT=@x AND DoiTuong=N'Đợt chạy hợp đồng chi tiết'
			SELECT @DoiTuong = DoiTuong FROM ColumnCheckValue WHERE STT=@x AND DoiTuong=N'Đợt chạy hợp đồng chi tiết'
			SET @SQL = '
			SELECT  '''+@ColumnSQL+''' [Column], 
					N'''+@DoiTuong+''' DoiTuong, 
					B.DotChayHopDongChiTietID,
					B.'+@ColumnSQL+' DulieuSQL,
					A.'+@ColumnMySQL+' DulieuMySQL,
					''Lech du lieu'' LoaiVanDe,
					'''+CONVERT(NVARCHAR(100),GETDATE(),113)+''' ThoiGianLog,
					0 TrangThaiXuLy,
					14 IDLoai
			FROM    #HopDongTemp A FULL JOIN
			(
			SELECT  *
			FROM    dbo.DotChayHopDongChiTiet
			WHERE   CONVERT(DATE,LastModifiedAt) BETWEEN  '''+CONVERT(NVARCHAR(100),@FromDate,113)+''' AND '''+CONVERT(NVARCHAR(100), @LastSynTime ,113)+'''
			) B ON A.id=B.DotChayHopDongChiTietID
			WHERE 1=1 
			AND B.'+@ColumnSQL+'<> A.'+@ColumnMySQL+'
			AND a.LastModifiedAt <='''+CONVERT(NVARCHAR(50),@MaxTimeSynInHD,113)+''''
			INSERT INTO CheckThongTinDauVao
			EXECUTE(@SQL)
			SET @x = @x+1
		END
		
    END
	--[Sp_Check_GiaTriLechCacTruongTrenDotChayHopDong] '',''

```
