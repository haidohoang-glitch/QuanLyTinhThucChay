# Stored Procedure: `Sp_Check_SoLuongLechBanGhiTrenDotChayHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-22 15:11:13.520000
- **Ngày sửa cuối**: 2017-03-11 09:44:46.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_SoLuongLechBanGhiTrenDotChayHopDong '2017-01-01',''
CREATE PROCEDURE [dbo].[Sp_Check_SoLuongLechBanGhiTrenDotChayHopDong]
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
        CREATE TABLE #Temp_DotChay
            (
              DotChayID INT ,
              LastModifiedAt DATETIME
            )
        DECLARE @SQL NVARCHAR(MAX) 
	
        SET @SQL = 'select A.id,IFNULL(A.LastModifiedAt,A.CreatedAt)LastModifiedAt  from hdcn_dotchay A
					WHERE IFNULL(A.LastModifiedAt,A.CreatedAt) between '''''
            + CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
            + CONVERT(NVARCHAR(20), @LastSynTime, 120) + '''''
					;'
        SET @SQL = '
					SELECT * FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #Temp_DotChay
                EXECUTE ( @SQL
                       )
        INSERT  INTO CheckThongTinDauVao
                SELECT  N'Thiếu bản ghi' NhomVanDe ,
                        N'Đợt chạy hợp đồng chi tiết' DoiTuong ,
                        A.DotChayID ,
                        '' DuLieuTrenSQL ,
                        '' DuLieuTrenMySQL ,
                        A.ThongTinLech LoaiVanDe ,
                        CONVERT(NVARCHAR(100), GETDATE(), 113) ThoiGianLog ,
                        0 TrangThaiXuLy ,
                        A.IDLoai
                FROM    ( SELECT    N'Thiếu bản ghi trên SQL' ThongTinLech ,
                                    16 IDLoai ,
                                    DotChayID ,
                                    LastModifiedAt NgaySua
                          FROM      #Temp_DotChay
                          WHERE     DotChayID NOT IN (
                                    SELECT  DotChayHopDongChiTietID
                                    FROM    dbo.DotChayHopDongChiTiet
                                    WHERE   LastModifiedAt BETWEEN @FromDate AND @LastSynTime )
                          UNION ALL
                          SELECT    N'Thiếu bản ghi trên MySQL' ,
                                    15 ,
                                    DotChayHopDongChiTietID ,
                                    LastModifiedAt
                          FROM      dbo.DotChayHopDongChiTiet
                          WHERE     LastModifiedAt BETWEEN @FromDate AND @LastSynTime
                                    AND DotChayHopDongChiTietID NOT IN (
                                    SELECT  DotChayID
                                    FROM    #Temp_DotChay )
                                    AND DeletedStatus = 0
                        ) A
                WHERE   A.NgaySua <= @MaxTimeSynInHD
		--SELECT @MaxTimeSynInHD
        DROP TABLE #Temp_DotChay
    END
	--Sp_Check_SoLuongLechBanGhiTrenHopDongChiTiet '2017-01-01','2017-02-22'
```
