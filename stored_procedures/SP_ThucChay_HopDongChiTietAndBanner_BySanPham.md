# Stored Procedure: `ThucChay_HopDongChiTietAndBanner_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:17.493000
- **Ngày sửa cuối**: 2017-09-18 15:04:30.383000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DenNgay` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_HopDongChiTietAndBanner_BySanPham]
    @DenNgay DATETIME ,
    @DmSanPhamREF INT
AS
    BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
        DECLARE @ThucChayHopDongChiTietID INT ,
            @DmBannerREF NVARCHAR(4000) ,
            @HopDongChiTietREF INT ,
            @HopDongREF INT ,
            @BookingREF INT ,
            @DsNhanHangREF NVARCHAR(200) ,
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
        SET @DsNhanHangREF = ''

        DELETE  FROM ThucChayHopDongChiTietAndBanner
        WHERE   CONVERT(DATE, LastModifiedAt) >= @DenNgay
                AND HopDongChiTietREF IN (
                SELECT  hdct.HopDongChiTietID
                FROM    HopDongChiTiet hdct
                WHERE   hdct.DmSanPhamREF = @DmSanPhamREF )

        DECLARE Record_Cursor CURSOR
        FOR
            SELECT  ThucChayHopDongChiTietID ,
                    DmBannerREF ,
                    HopDongREF ,
                    HopDongChiTietREF ,
                    BookingREF ,
                    tc.DmNhanHangREF ,
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
					AND tc.DeletedStatus = 0
                    AND DmBannerREF IS NOT NULL
                    AND DmBannerREF <> ''
                    AND ( CASE WHEN tc.LastModifiedAt >= tc.CreatedAt
                               THEN CONVERT(DATE, tc.LastModifiedAt)
                               ELSE CONVERT(DATE, tc.CreatedAt)
                          END ) >= CONVERT(DATE, @DenNgay)
                    AND tc.DmSanPhamREF = @DmSanPhamREF
					AND HopDongChiTietREF NOT IN (
                    SELECT  HopDongChiTietID
                    FROM    dbo.HopDongChiTiet
                    WHERE   ( TenLoaiNenTang LIKE '%Retargeting%'
                              OR DmLoaiBannerREF = 17
                              OR DmLoaiNenTangREF = 8
                            )
                            AND DeletedStatus <> 1 )
        OPEN Record_Cursor

-- Perform the first fetch.
        FETCH NEXT FROM Record_Cursor INTO @ThucChayHopDongChiTietID,
            @DmBannerREF, @HopDongREF, @HopDongChiTietREF, @BookingREF,
            @DsNhanHangREF, @ThoiGianBatDau, @ThoiGianKetThuc, @CreatedBy,
            @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus
		
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
		--DELETE FROM ThucChayHopDongChiTietAndBanner
		--WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
		
                        IF ( EXISTS ( SELECT    tchdctab.ThucChayHopDongChiTietID
                                      FROM      ThucChayHopDongChiTietAndBanner tchdctab
                                      WHERE     tchdctab.HopDongREF = @HopDongREF
                                                AND tchdctab.HopDongChiTietREF = @HopDongChiTietREF
                                                AND tchdctab.DmBannerID = @DmBannerREF
                                                AND tchdctab.DeletedStatus = 0 ) )
                            BEGIN
                                UPDATE  ThucChayHopDongChiTietAndBanner
                                SET     ThoiGianBatDau = @ThoiGianBatDau ,
                                        ThoiGianKetThuc = @ThoiGianKetThuc ,
                                        CreatedBy = @CreatedBy ,
                                        CreatedAt = @CreatedAt ,
                                        LastModifiedBy = @LastModifiedBy ,
                                        LastModifiedAt = @LastModifiedAt ,
                                        DeletedStatus = @DeletedStatus ,
                                        DsNhanHangREF = @DsNhanHangREF
                                WHERE   HopDongREF = @HopDongREF
                                        AND HopDongChiTietREF = @HopDongChiTietREF
                                        AND DmBannerID = @DmBannerREF
                                        AND DeletedStatus = 0
                            END
                        ELSE
                            BEGIN
                                PRINT @BannerID
				--Insert thuc chay ThucChayHopDongChiTietID	
                                INSERT  INTO dbo.ThucChayHopDongChiTietAndBanner
                                        ( ThucChayHopDongChiTietID ,
                                          DmBannerID ,
                                          HopDongChiTietREF ,
                                          HopDongREF ,
                                          BookingREF ,
                                          ThoiGianBatDau ,
                                          ThoiGianKetThuc ,
                                          TiLeThucChayHDCTSoVoiBanner ,
                                          DaThucHienUpdateTiLe ,
                                          CreatedBy ,
                                          CreatedAt ,
                                          LastModifiedBy ,
                                          LastModifiedAt ,
                                          DeletedStatus ,
                                          DsNhanHangREF
				                        )
                                        SELECT  @ThucChayHopDongChiTietID ,
                                                @BannerID ,
                                                @HopDongChiTietREF ,
                                                @HopDongREF ,
                                                @BookingREF ,
                                                @ThoiGianBatDau ,
                                                @ThoiGianKetThuc ,
                                                0 ,
                                                0 ,
                                                @CreatedBy ,
                                                @CreatedAt ,
                                                @LastModifiedBy ,
                                                @LastModifiedAt ,
                                                @DeletedStatus ,
                                                @DsNhanHangREF
                            END
                        FETCH NEXT FROM Record_Cursor1 INTO @BannerID
                    END
                CLOSE Record_Cursor1
                DEALLOCATE Record_Cursor1
	
                FETCH NEXT FROM Record_Cursor INTO @ThucChayHopDongChiTietID,
                    @DmBannerREF, @HopDongREF, @HopDongChiTietREF, @BookingREF,
                    @DsNhanHangREF, @ThoiGianBatDau, @ThoiGianKetThuc,
                    @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt,
                    @DeletedStatus
            END

        CLOSE Record_Cursor
        DEALLOCATE Record_Cursor

        SELECT  '1'



    END

--EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] '2014-09-22'

--SELECT COUNT(*) FROM ThucChayHopDongChiTietAndBanner

```
