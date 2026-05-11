# Stored Procedure: `Sp_Check_GiaTriLechCacTruongTrenThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-23 14:53:13.060000
- **Ngày sửa cuối**: 2017-03-11 09:42:54.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--[Sp_Check_GiaTriLechCacTruongTrenThucTreo] '',''
CREATE PROCEDURE [dbo].[Sp_Check_GiaTriLechCacTruongTrenThucTreo]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.ThucChayHopDongChiTiet
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
            (
              id INT ,
              hd_id INT ,
              phanbosite_id INT ,
              abm_nhanhang_id NVARCHAR(1000) ,
              thoigianketthuc DATETIME ,
              LastModifiedAt DATETIME
            )

        DECLARE @SQL NVARCHAR(MAX) 
		
        SET @SQL = 'select A.id,
					hd_id,
					phanbosite_id,
					abm_nhanhang_id,
					CAST(IF (A.thoigianketthuc = ''''0000-00-00'''' OR A.thoigianketthuc =''''0001-01-01'''' OR A.thoigianketthuc IS NULL,''''2010-01-01'''', A.thoigianketthuc) AS DATETIME) ThoiGianKetThuc,
					CAST(IF (A.modifieddate = ''''0000-00-00'''' OR A.modifieddate =''''0001-01-01'''' OR A.modifieddate IS NULL,IFNULL(A.CreatedDate, ''''2010-01-01''''), A.modifieddate) AS DATETIME) AS LastModifiedAt 
					from hdcn_thucchay A
					WHERE 1=1 AND  CAST(IF (A.modifieddate = ''''0000-00-00'''' OR A.modifieddate =''''0001-01-01'''' OR A.modifieddate IS NULL,IFNULL(A.CreatedDate, ''''2010-01-01''''), A.modifieddate) AS DATE) between '''''
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
        SET @TotalRows = ( SELECT   MAX(STT)
                           FROM     ColumnCheckValue
                           WHERE    DoiTuong = N'Thông tin thực treo'
                         )
        SET @x = ( SELECT   MIN(STT)
                   FROM     ColumnCheckValue
                   WHERE    DoiTuong = N'Thông tin thực treo'
                 )
        WHILE @x <= @TotalRows
            BEGIN
                SELECT  @ColumnSQL = ColumnSQL
                FROM    ColumnCheckValue A
                WHERE   STT = @x
                        AND DoiTuong = N'Thông tin thực treo'
                SELECT  @ColumnMySQL = ColumnMySQL
                FROM    ColumnCheckValue A
                WHERE   STT = @x
                        AND DoiTuong = N'Thông tin thực treo'
                SELECT  @DoiTuong = DoiTuong
                FROM    ColumnCheckValue
                WHERE   STT = @x
                        AND DoiTuong = N'Thông tin thực treo'
                SET @SQL = '
			SELECT  ''' + @ColumnSQL + ''' [Column], 
					N''' + @DoiTuong + ''' DoiTuong, 
					B.ThucChayHopDongChiTietID,
					B.' + @ColumnSQL + ' DulieuSQL,
					A.' + @ColumnMySQL + ' DulieuMySQL,
					''Lech du lieu'' LoaiVanDe,
					''' + CONVERT(NVARCHAR(100), GETDATE(), 113)
                    + ''' ThoiGianLog,
					0 TrangThaiXuLy,
					14 IDLoai
			FROM    #HopDongTemp A FULL JOIN
			(
			SELECT  *
			FROM    dbo.ThucChayHopDongChiTiet
			WHERE   CONVERT(DATE,LastModifiedAt) BETWEEN  '''
                    + CONVERT(NVARCHAR(100), @FromDate, 113) + ''' AND '''
                    + CONVERT(NVARCHAR(100), @LastSynTime, 113) + '''
			) B ON A.id=B.ThucChayHopDongChiTietID
			WHERE 1=1 
			AND B.' + @ColumnSQL + '<> A.' + @ColumnMySQL + '
			AND a.LastModifiedAt <=''' + CONVERT(NVARCHAR(50), @MaxTimeSynInHD, 113)
                    + ''''
                PRINT @SQL
                INSERT  INTO CheckThongTinDauVao
                EXECUTE ( @SQL
                )
                SET @x = @x + 1
            END
		
    END
	--[Sp_Check_GiaTriLechCacTruongTrenDotChayHopDong] '',''

```
