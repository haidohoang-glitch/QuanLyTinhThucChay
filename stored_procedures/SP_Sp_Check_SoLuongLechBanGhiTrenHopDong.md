# Stored Procedure: `Sp_Check_SoLuongLechBanGhiTrenHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-21 11:44:44.297000
- **Ngày sửa cuối**: 2017-03-11 10:05:47.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_SoLuongLechBanGhiTrenHopDong '2017-01-01','2017-03-07'
CREATE PROCEDURE [dbo].[Sp_Check_SoLuongLechBanGhiTrenHopDong]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN
       
        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.HopDong
                              )

        IF @NgayKetThuc = ''
            SET @LastSynTime = GETDATE()
        ELSE
            SET @LastSynTime = @NgayKetThuc
        IF @NgayBatDau = ''
            SET @FromDate = DATEADD(DD, -2, @LastSynTime)
        ELSE
            SET @FromDate = @NgayBatDau
        CREATE TABLE #Temp_HopDongMySQL
            (
              HopDongID INT ,
              LastModified DATETIME
            )
        CREATE TABLE #Temp_HDNew
            (
              HopDongID INT ,
              LastModified DATETIME
            )
        DECLARE @SQL NVARCHAR(MAX) 
	
        SET @SQL = 'select id,LastModifyAt from hdcn_hd where CONVERT(LastModifyAt,DATE) between '''''
            + CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
            + CONVERT(NVARCHAR(20), @LastSynTime, 120) + '''''
					and trangthai <>0
					;'
        SET @SQL = '
					SELECT * FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #Temp_HopDongMySQL
                EXECUTE ( @SQL
                       )
		
        SET @SQL = 'select id,LastModifyAt from hdcn_hd where CONVERT(LastModifyAt,DATE) > '''''
            + CONVERT(NVARCHAR(20), @LastSynTime, 120) + '''''
					and trangthai <>0
					;'
        SET @SQL = '
					SELECT * FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        INSERT  INTO #Temp_HDNew
                EXECUTE ( @SQL
                       )

        CREATE TABLE #HopDongSQL
            (
              HopDongID INT ,
              LastModifiedAt DATETIME
            )
        INSERT  INTO #HopDongSQL
                SELECT  HopDongID ,
                        LastModifiedAt
                FROM    dbo.HopDong
                WHERE   CONVERT(DATE, LastModifiedAt) >= @FromDate

        INSERT  INTO CheckThongTinDauVao
                SELECT  N'Thiếu bản ghi' NhomVanDe ,
                        N'Hợp đồng' DoiTuong ,
                        A.HopDongID ,
                        '' DuLieuTrenSQL ,
                        '' DuLieuTrenMySQL ,
                        A.ThongTinLech LoaiVanDe ,
                        CONVERT(NVARCHAR(100), GETDATE(), 113) ThoiGianLog ,
                        0 TrangThaiXuLy ,
                        A.IDLoai
                FROM    ( SELECT    N'Thiếu bản ghi trên SQL' ThongTinLech ,
                                    16 IDLoai ,
                                    HopDongID ,
                                    LastModified NgaySua
                          FROM      #Temp_HopDongMySQL
                          WHERE     HopDongID NOT IN ( SELECT HopDongID
                                                       FROM   #HopDongSQL )
                          UNION ALL
                          SELECT    N'Thiếu bản ghi trên MySQL' ,
                                    15 IDLoai ,
                                    HopDongID ,
                                    LastModifiedAt
                          FROM      #HopDongSQL
                          WHERE     HopDongID NOT IN (
                                    SELECT  HopDongID
                                    FROM    #Temp_HopDongMySQL
                                    UNION ALL
                                    SELECT  HopDongID
                                    FROM    #Temp_HDNew )
												  -- AND CONVERT(DATE,LastModifiedAt) BETWEEN @NgayBatDau AND @LastSynTime
                        ) A
       -- WHERE   A.NgaySua <= @MaxTimeSynInHD
    END
```
