# Stored Procedure: `ThucChay_HopDongChiTietAndBannerCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-25 14:51:58.677000
- **Ngày sửa cuối**: 2017-06-05 10:55:38.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DenNgay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--exec ThucChay_HopDongChiTietAndBannerCPD  '2017-03-01'
CREATE PROCEDURE [dbo].[ThucChay_HopDongChiTietAndBannerCPD] @DenNgay DATETIME
AS
    BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
        DECLARE @ThucChayHopDongChiTietID INT ,
            @DmBannerREF NVARCHAR(4000) ,
            @HopDongChiTietREF INT ,
            @HopDongREF INT ,
            @BookingREF INT ,
            @BannerID NVARCHAR(50)
        DECLARE @CreatedBy NVARCHAR(50) ,
            @LastModifiedBy NVARCHAR(50) ,
            @DaThucHienUpdateTile TINYINT ,
            @DeletedStatus INT
        DECLARE @ThoiGianBatDau DATETIME ,
            @ThoiGianKetThuc DATETIME ,
            @CreatedAt DATETIME ,
            @LastModifiedAt DATETIME
        SET @DaThucHienUpdateTile = 1

        DELETE  FROM ThucChayHopDongChiTietAndBannerCPD
        WHERE   CONVERT(DATE, LastModifiedAt) >= @DenNgay

        DECLARE Record_Cursor CURSOR
        FOR
            SELECT  ThucChayHopDongChiTietID ,
                    DmBannerREF ,
                    HopDongREF ,
                    HopDongChiTietREF ,
                    BookingREF ,
                    ThoiGianBatDau ,
                    ThoiGianKetThuc ,
                    CreatedBy ,
                    CreatedAt ,
                    LastModifiedBy ,
                    LastModifiedAt ,
                    tc.DeletedStatus
            FROM    dbo.ThucChayHopDongChiTiet tc
            WHERE   HopDongChiTietREF > 0
                    AND HopDongREF > 0
                    AND DmBannerREF IS NOT NULL
                    AND DmBannerREF <> ''
                    AND ( CASE WHEN tc.LastModifiedAt >= tc.CreatedAt
                               THEN CONVERT(DATE, tc.LastModifiedAt)
                               ELSE CONVERT(DATE, tc.CreatedAt)
                          END ) >= CONVERT(DATE, @DenNgay)
                    AND tc.HopDongChiTietREF IN (
                    SELECT  hdct.HopDongChiTietID
                    FROM    HopDongChiTiet hdct
                    WHERE   hdct.DmSanPhamREF IN ( 140, 228, 564, 549 )
                            AND hdct.DeletedStatus = 0 )
	--AND tc.HopDongChiTietREF = 501512
        OPEN Record_Cursor

-- Perform the first fetch.
        FETCH NEXT FROM Record_Cursor INTO @ThucChayHopDongChiTietID,
            @DmBannerREF, @HopDongREF, @HopDongChiTietREF, @BookingREF,
            @ThoiGianBatDau, @ThoiGianKetThuc, @CreatedBy, @CreatedAt,
            @LastModifiedBy, @LastModifiedAt, @DeletedStatus
		
        WHILE @@FETCH_STATUS = 0
            BEGIN
		
                PRINT @HopDongREF
                PRINT @DmBannerREF
	
                DECLARE Record_Cursor1 CURSOR
                FOR
                    SELECT  dbo.FormatString(item)
                    FROM    dbo.ArrayToTable(dbo.Array(@DmBannerREF, ','))
                OPEN Record_Cursor1
                FETCH NEXT FROM Record_Cursor1 INTO @BannerID
                WHILE @@FETCH_STATUS = 0
                    BEGIN
		--Delete khi ton tai ThucChayHopDongChiTietID
                        DELETE  FROM ThucChayHopDongChiTietAndBannerCPD
                        WHERE   ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
                                AND DmBannerID = @BannerID
                                AND BookingREF = @BookingREF
                                AND HopDongChiTietREF = @HopDongChiTietREF
                        PRINT @BannerID
		--Insert thuc chay ThucChayHopDongChiTietID	
                        INSERT  INTO dbo.ThucChayHopDongChiTietAndBannerCPD
                                ( ThucChayHopDongChiTietID ,
                                  DmBannerID ,
                                  HopDongChiTietREF ,
                                  HopDongREF ,
                                  BookingREF ,
                                  ThoiGianBatDau ,
                                  ThoiGianKetThuc ,
                                  CreatedBy ,
                                  CreatedAt ,
                                  LastModifiedBy ,
                                  LastModifiedAt ,
                                  DeletedStatus
		                        )
                                SELECT  @ThucChayHopDongChiTietID ,
                                        @BannerID ,
                                        @HopDongChiTietREF ,
                                        @HopDongREF ,
                                        @BookingREF ,
                                        @ThoiGianBatDau ,
                                        @ThoiGianKetThuc ,
                                        @CreatedBy ,
                                        @CreatedAt ,
                                        @LastModifiedBy ,
                                        @LastModifiedAt ,
                                        @DeletedStatus
                        FETCH NEXT FROM Record_Cursor1 INTO @BannerID
                    END
                CLOSE Record_Cursor1
                DEALLOCATE Record_Cursor1
	
                FETCH NEXT FROM Record_Cursor INTO @ThucChayHopDongChiTietID,
                    @DmBannerREF, @HopDongREF, @HopDongChiTietREF, @BookingREF,
                    @ThoiGianBatDau, @ThoiGianKetThuc, @CreatedBy, @CreatedAt,
                    @LastModifiedBy, @LastModifiedAt, @DeletedStatus
            END

        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor

        PRINT  '1'



    END

--EXEC [dbo].[ThucChay_HopDongChiTietAndBannerCPD] '2014-01-01'

--SELECT COUNT(*) FROM ThucChayHopDongChiTietAndBannerCPD

```
