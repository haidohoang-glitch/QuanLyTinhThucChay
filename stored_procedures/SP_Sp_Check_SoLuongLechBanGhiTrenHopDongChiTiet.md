# Stored Procedure: `Sp_Check_SoLuongLechBanGhiTrenHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-22 11:02:35.573000
- **Ngày sửa cuối**: 2017-03-11 11:05:00.703000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_SoLuongLechBanGhiTrenHopDongChiTiet '2017-03-10','2017-03-10'
CREATE PROCEDURE [dbo].[Sp_Check_SoLuongLechBanGhiTrenHopDongChiTiet]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.HopDongChiTiet
                              )

        IF @NgayKetThuc = ''
            SET @LastSynTime = GETDATE()
        ELSE
            SET @LastSynTime = @NgayKetThuc
        IF @NgayBatDau = ''
            SET @FromDate = DATEADD(DD, -2, @LastSynTime)
        ELSE
            SET @FromDate = @NgayBatDau
        CREATE TABLE #Temp_HopDong
            (
              HopDongChiTietID INT ,
              LastModified DATETIME
            )
        DECLARE @SQL NVARCHAR(MAX) 
	
        SET @SQL = 'select A.id,A.LastModifiedAt from hdcn_phanbosite A inner join hdcn_hd B on B.id=A.hd_id  
					where CONVERT(A.LastModifiedAt,DATE) between '''''
            + CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
            + CONVERT(NVARCHAR(20), @LastSynTime, 120) + '''''
					;'
        SET @SQL = '
					SELECT * FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #Temp_HopDong
                EXECUTE ( @SQL
                       )
        INSERT  INTO CheckThongTinDauVao
                SELECT  N'Thiếu bản ghi' NhomVanDe ,
                        N'Hợp đồng chi tiết' DoiTuong ,
                        A.HopDongChiTietID ,
                        '' DuLieuTrenSQL ,
                        '' DuLieuTrenMySQL ,
                        A.ThongTinLech LoaiVanDe ,
                        CONVERT(NVARCHAR(100), GETDATE(), 113) ThoiGianLog ,
                        0 TrangThaiXuLy ,
                        A.IDLoai
                FROM    ( SELECT    N'Thiếu bản ghi trên SQL' ThongTinLech ,
                                    16 IDLoai ,
                                    HopDongChiTietID ,
                                    LastModified NgaySua
                          FROM      #Temp_HopDong
                          WHERE     HopDongChiTietID NOT IN (
                                    SELECT  HopDongChiTietID
                                    FROM    dbo.HopDongChiTiet
                                    WHERE   LastModifiedAt BETWEEN @FromDate AND @LastSynTime )
                          UNION ALL
                          SELECT    N'Thiếu bản ghi trên MySQL' ,
                                    15 IDLoai ,
                                    HopDongChiTietID ,
                                    LastModifiedAt
                          FROM      dbo.HopDongChiTiet
                          WHERE     LastModifiedAt BETWEEN @FromDate AND @LastSynTime
                                    AND HopDongChiTietID NOT IN ( SELECT
                                                              HopDongChiTietID
                                                              FROM
                                                              #Temp_HopDong )
                                    AND DeletedStatus = 0
                        ) A
                WHERE   A.NgaySua <= @MaxTimeSynInHD
		--SELECT @MaxTimeSynInHD
        DROP TABLE #Temp_HopDong
    END
	--Sp_Check_SoLuongLechBanGhiTrenHopDongChiTiet '2017-01-01','2017-02-22'
```
