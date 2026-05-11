# Stored Procedure: `Sp_Check_SoLuongLechBanGhiTrenThongTinHoaDon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-23 11:04:10.027000
- **Ngày sửa cuối**: 2017-03-11 09:46:53.350000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_SoLuongLechBanGhiTrenThongTinHoaDon '2015-01-01',''
CREATE PROCEDURE [dbo].[Sp_Check_SoLuongLechBanGhiTrenThongTinHoaDon]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.ThongTinHoaDon
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
					WHERE 1=1 AND  ((`ngayxuat` <> ''''0000-00-00'''') AND (`ngayxuat` <> ''''0001-01-01'''')) AND CAST(IFNULL(LogTime,''''2010-01-01'''') AS DATETIME) between '''''
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
                        N'Thông tin hóa đơn' DoiTuong ,
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
                                    SELECT  ThongTinHoaDonID
                                    FROM    dbo.ThongTinHoaDon
                                    WHERE   LastModifiedAt BETWEEN @FromDate AND @LastSynTime )
                          UNION ALL
                          SELECT    N'Thiếu bản ghi trên MySQL' ,
                                    15 IDLoai ,
                                    ThongTinHoaDonID ,
                                    LastModifiedAt
                          FROM      dbo.ThongTinHoaDon
                          WHERE     LastModifiedAt BETWEEN @FromDate AND @LastSynTime
                                    AND ThongTinHoaDonID NOT IN ( SELECT
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
