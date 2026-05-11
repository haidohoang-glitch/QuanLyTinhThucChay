# Stored Procedure: `Sp_Check_SoLuongLechBanGhiTrenHopDongAttachFile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-22 17:35:32.240000
- **Ngày sửa cuối**: 2017-03-11 09:45:44.280000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_SoLuongLechBanGhiTrenHopDongAttachFile '',''
CREATE PROCEDURE [dbo].[Sp_Check_SoLuongLechBanGhiTrenHopDongAttachFile]
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
        CREATE TABLE #Temp
            (
              ID INT ,
              LastModifiedAt DATETIME
            )
        DECLARE @SQL NVARCHAR(MAX) 
	
        SET @SQL = 'select A.id,CAST(IFNULL(LastModifiedAt,IFNULL(CreatedAt,''''2010-01-01'''')) AS DATETIME) AS LastModifiedAt from hdcn_attachfiles A
					WHERE CAST(IFNULL(LastModifiedAt,IFNULL(CreatedAt,''''2010-01-01'''')) AS DATETIME) between '''''
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
                        N'Hợp đồng AttachFile' DoiTuong ,
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
                                    SELECT  HopDongAttachFileID
                                    FROM    dbo.HopDongAttachFile
                                    WHERE   LastModifiedAt BETWEEN @FromDate AND @LastSynTime )
                          UNION ALL
                          SELECT    N'Thiếu bản ghi trên MySQL' ,
                                    15 IDLoai ,
                                    HopDongAttachFileID ,
                                    LastModifiedAt
                          FROM      dbo.HopDongAttachFile
                          WHERE     LastModifiedAt BETWEEN @FromDate AND @LastSynTime
                                    AND HopDongAttachFileID NOT IN ( SELECT
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
