# Stored Procedure: `Sp_Check_SoLuongLechBanGhiTrenThongTinTienVe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-23 11:07:48.040000
- **Ngày sửa cuối**: 2017-03-11 09:47:15.633000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_SoLuongLechBanGhiTrenThongTinTienVe '2016',''
CREATE PROCEDURE [dbo].[Sp_Check_SoLuongLechBanGhiTrenThongTinTienVe]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.ThongTinTienVe
                              )

        IF @NgayKetThuc = ''
            SET @LastSynTime = GETDATE()
        ELSE
            SET @LastSynTime = @NgayKetThuc
        IF @NgayBatDau = ''
            SET @FromDate = DATEADD(DD, -2, @LastSynTime)
        ELSE
            SET @FromDate = @NgayBatDau
        CREATE TABLE #Temp
            (
              ID INT ,
              LastModifiedAt DATETIME
            )
        DECLARE @SQL NVARCHAR(MAX) 
	
        SET @SQL = 'select A.id,CAST(IFNULL(LogTime,''''2010-01-01'''') AS DATETIME) AS LastModifiedAt from hdcn_congno A
					WHERE 1=1 AND  ((`ngaythanhtoan` <> ''''0000-00-00'''') AND (`ngaythanhtoan` <> ''''0001-01-01'''')) AND CAST(IFNULL(LogTime,''''2010-01-01'''') AS DATETIME) between '''''
            + CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
            + CONVERT(NVARCHAR(20), @LastSynTime, 120) + ''''';'
        SET @SQL = '
					SELECT * FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #Temp
                EXECUTE ( @SQL
                       )
        INSERT  INTO CheckThongTinDauVao
                SELECT  N'Thiếu bản ghi' NhomVanDe ,
                        N'Thông tin tiền về' DoiTuong ,
                        A.ID ,
                        '' DuLieuTrenSQL ,
                        '' DuLieuTrenMySQL ,
                        A.ThongTinLech LoaiVanDe ,
                        CONVERT(NVARCHAR(100), GETDATE(), 113) ThoiGianLog ,
                        0 TrangThaiXuLy ,
                        A.IDLoai
                FROM    ( SELECT    N'Thiếu bản ghi trên SQL' ThongTinLech ,
                                    16 IDLoai ,
                                    ID ,
                                    LastModifiedAt NgaySua
                          FROM      #Temp
                          WHERE     ID NOT IN (
                                    SELECT  ThongTinTienVeID
                                    FROM    dbo.ThongTinTienVe
                                    WHERE   LastModifiedAt BETWEEN @FromDate AND @LastSynTime )
                          UNION ALL
                          SELECT    N'Thiếu bản ghi trên MySQL' ,
                                    15 IDLoai ,
                                    ThongTinTienVeID ,
                                    LastModifiedAt
                          FROM      dbo.ThongTinTienVe
                          WHERE     LastModifiedAt BETWEEN @FromDate AND @LastSynTime
                                    AND ThongTinTienVeID NOT IN ( SELECT
                                                              ID
                                                              FROM
                                                              #Temp )
                                    AND DeletedStatus = 0
                        ) A
                WHERE   A.NgaySua <= @MaxTimeSynInHD
		--SELECT @MaxTimeSynInHD
        DROP TABLE #Temp
    END
	--Sp_Check_SoLuongLechBanGhiTrenHopDongChiTiet '2017-01-01','2017-02-22'
```
