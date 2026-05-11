# Stored Procedure: `Sp_Check_SoLuongLechBanGhiTrenThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-23 11:37:31.723000
- **Ngày sửa cuối**: 2017-03-11 09:47:37.103000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_SoLuongLechBanGhiTrenThucTreo '2016-01-01',''
CREATE PROCEDURE [dbo].[Sp_Check_SoLuongLechBanGhiTrenThucTreo]
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
        CREATE TABLE #Temp
            (
              ID INT ,
              LastModifiedAt DATETIME
            )
        DECLARE @SQL NVARCHAR(MAX) 
	
        SET @SQL = 'select A.id,CAST(IF (A.modifieddate = ''''0000-00-00'''' OR A.modifieddate = ''''0001-01-01'''' OR A.modifieddate IS NULL,IFNULL(A.CreatedDate, ''''2010-01-01''''), A.modifieddate) AS DATETIME) AS LastModifiedAt from hdcn_thucchay A
					WHERE 1=1 AND  CAST(IF (A.modifieddate = ''''0000-00-00'''' OR A.modifieddate = ''''0001-01-01'''' OR A.modifieddate IS NULL,IFNULL(A.CreatedDate, ''''2010-01-01''''), A.modifieddate) AS DATETIME) between '''''
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
                        N'Thông tin thực treo' DoiTuong ,
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
                                    SELECT  ThucChayHopDongChiTietID
                                    FROM    dbo.ThucChayHopDongChiTiet
                                    WHERE   LastModifiedAt BETWEEN @FromDate AND @LastSynTime )
                          UNION ALL
                          SELECT    N'Thiếu bản ghi trên MySQL' ,
                                    15 IDLoai ,
                                    ThucChayHopDongChiTietID ,
                                    LastModifiedAt
                          FROM      dbo.ThucChayHopDongChiTiet
                          WHERE     LastModifiedAt BETWEEN @FromDate AND @LastSynTime
                                    AND ThucChayHopDongChiTietID NOT IN (
                                    SELECT  ID
                                    FROM    #Temp )
                                    AND DeletedStatus = 0
                        ) A
                WHERE   A.NgaySua <= @MaxTimeSynInHD
		--SELECT @MaxTimeSynInHD
        DROP TABLE #Temp
    END
	--Sp_Check_SoLuongLechBanGhiTrenHopDongChiTiet '2017-01-01','2017-02-22'
```
