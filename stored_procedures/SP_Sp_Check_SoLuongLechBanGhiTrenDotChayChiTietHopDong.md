# Stored Procedure: `Sp_Check_SoLuongLechBanGhiTrenDotChayChiTietHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-22 15:55:08.380000
- **Ngày sửa cuối**: 2017-03-11 09:44:01.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_SoLuongLechBanGhiTrenDotChayChiTietHopDong '',''
CREATE PROCEDURE [dbo].[Sp_Check_SoLuongLechBanGhiTrenDotChayChiTietHopDong]
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
        CREATE TABLE #Temp_DotChay
            (
              DotChayID INT ,
              LastModifiedAt DATETIME
            )
        DECLARE @SQL NVARCHAR(MAX) 
	
        SET @SQL = 'select A.id,CAST(IF (LastModifiedAt = ''''0000-00-00'''' OR LastModifiedAt = ''''0001-01-01'''' OR LastModifiedAt IS NULL,IFNULL(CreatedAt, ''''2010-01-01''''),LastModifiedAt) AS DATETIME) AS LastModifiedAt from hdcn_DotChay_ChiTiet A
					WHERE CAST(IF (LastModifiedAt = ''''0000-00-00'''' OR LastModifiedAt = ''''0001-01-01'''' OR LastModifiedAt IS NULL,IFNULL(CreatedAt, ''''2010-01-01''''),LastModifiedAt) AS DATETIME) between '''''
            + CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
            + CONVERT(NVARCHAR(20), @LastSynTime, 120) + ''''';'
        SET @SQL = '
					SELECT * FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #Temp_DotChay
                EXECUTE ( @SQL
                       )
        INSERT  INTO CheckThongTinDauVao
                SELECT  N'Thiếu bản ghi' NhomVanDe ,
                        N'Đợt chạy chi tiết hợp đồng chi tiết' DoiTuong ,
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
                                    SELECT  DotChayChiTietHopDongChiTietID
                                    FROM    dbo.DotChayChiTietHopDongChiTiet
                                    WHERE   LastModifiedAt BETWEEN @FromDate AND @LastSynTime )
                          UNION ALL
                          SELECT    N'Thiếu bản ghi trên MySQL' ,
                                    15 IDLoai ,
                                    DotChayChiTietHopDongChiTietID ,
                                    LastModifiedAt
                          FROM      dbo.DotChayChiTietHopDongChiTiet
                          WHERE     LastModifiedAt BETWEEN @FromDate AND @LastSynTime
                                    AND DotChayChiTietHopDongChiTietID NOT IN (
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
