# Stored Procedure: `sp_TC_CheckHopDongXoaPhanBo_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-23 17:56:21.900000
- **Ngày sửa cuối**: 2024-12-06 09:01:14.233000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@BannerType` | `int(4)` | No |
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_TC_CheckHopDongXoaPhanBo_Mobile] 
	-- Add the parameters for the stored procedure here
    @HopDongREF INT ,
    @SoHopDong NVARCHAR(50) ,
    @DmSanPhamREF INT ,
    @HopDongChiTietID INT ,
    @NgayThucHien DATETIME ,
    @BannerType INT ,
    @DmBannerID INT--,
	--@ProductUnitName NVARCHAR(50)
AS
    BEGIN
	-- Declare the return variable here
        DECLARE @DonGiaBF INT ,
            @CONTENT_DETAIL_LOG NVARCHAR(MAX) ,
            @CONTENT_LOG NVARCHAR(MAX) ,
            @NGUON_LOG NVARCHAR(MAX) ,
            @DmWebsiteREF INT ,
            @TenWebsite NVARCHAR(50) ,
            @IsKhuyenMai INT ,
            @SoLuongThucChayByWebiste INT ,
            @GiaTriThayDoi INT ,
            @NgayThayDoiLast DATETIME ,
            @CountHDTD INT;

        SET @CONTENT_DETAIL_LOG = '';
        SET @CONTENT_LOG = '';	        
        SET @NGUON_LOG = '';
        SET @IsKhuyenMai = ( SELECT TOP 1
                                    IsKhuyenMai
                             FROM   ThucChayDaTinh tcdtm
                             WHERE  tcdtm.HopDongChiTietREF = @HopDongChiTietID
                                    AND tcdtm.DmSanPhamREF = @DmSanPhamREF
                                    AND tcdtm.DmViTriREF = @BannerType
                                    AND tcdtm.DmBannerREF = @DmBannerID
                             ORDER BY tcdtm.NgayThucHien DESC
                           );
	        
        BEGIN
		--TINH DONGIACHENHLECH 
--		SET @DonGiaChenhLech = @DonGia*(100-@ChietKhau)/100 - @DonGiaLienKeTruoc*(100-@ChietKhauBF)/100
		
            DECLARE Record_Cursor_TCDT_Mobile CURSOR
            FOR
                SELECT DISTINCT
                        tcdt.DmWebsiteREF ,
                        tcdt.TenWebsite
                FROM    ThucChayDaTinh tcdt
                WHERE   tcdt.SoHopDong = @SoHopDong
                        AND tcdt.HopDongChiTietREF = @HopDongChiTietID
                        AND tcdt.DmSanPhamREF = @DmSanPhamREF
                        AND tcdt.DmBannerREF = @DmBannerID
		--AND tcdt.DmViTriREF = @BannerType
		
            OPEN Record_Cursor_TCDT_Mobile
		-- Perform the first fetch.
            FETCH NEXT FROM Record_Cursor_TCDT_Mobile INTO @DmWebsiteREF, @TenWebsite
			
            WHILE @@FETCH_STATUS = 0
                BEGIN
				--UPDATE GIA TRI THAY DOI CHO TUNG WEBSITE
                    SET @CONTENT_DETAIL_LOG = ''	
                    SET @SoLuongThucChayByWebiste = 0
                    SET @GiaTriThayDoi = 0
				--GET THONG TIN THƯC CHAY THEO WEBSITE
                    SET @NgayThayDoiLast = ( SELECT MAX(tcdt.NgayThucHien)
                                             FROM   ThucChayDaTinh tcdt
                                             WHERE  ( CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien )
                                                    AND tcdt.SoHopDong = @SoHopDong
                                                    AND tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                    AND tcdt.DmSanPhamREF = @DmSanPhamREF
                                                    AND tcdt.SoLuongThucChay <> 0
                                                    AND tcdt.GiaTriThayDoi <> 0
                                                    AND tcdt.DmBannerREF = @DmBannerID
					--AND tcdt.DmViTriREF = @BannerType
                                           )
                    IF ( @NgayThayDoiLast IS NULL )
                        BEGIN
                            SET @NgayThayDoiLast = ( SELECT MIN(tcdt.NgayThucHien)
                                                     FROM   ThucChayDaTinh tcdt
                                                     WHERE  ( CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien )
                                                            AND tcdt.SoHopDong = @SoHopDong
                                                            AND tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                            AND tcdt.DmSanPhamREF = @DmSanPhamREF
                                                            AND tcdt.SoLuongThucChay <> 0
                                                            AND tcdt.DmBannerREF = @DmBannerID
						--AND tcdt.DmViTriREF = @BannerType
                                                   )
                            SET @NgayThayDoiLast = DATEADD(d, -1,
                                                           @NgayThayDoiLast)
                        END 
				
                    SELECT  @GiaTriThayDoi = -( CASE WHEN @IsKhuyenMai = 0
                                                     THEN SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,
                                                              0)
                                                              + ISNULL(tcdt.GiaTriThayDoi,
                                                              0))
                                                     ELSE SUM(ISNULL(tcdt.ThanhTienKM,
                                                              0)
                                                              + ISNULL(tcdt.GiaTriKMThayDoi,
                                                              0))
                                                END )
                    FROM    ThucChayDaTinh tcdt
                    WHERE   ( ( CONVERT(DATE, tcdt.NgayThucHien) > @NgayThayDoiLast )
                              AND ( CONVERT(DATE, tcdt.NgayThucHien) <= @NgayThucHien )
                            )
                            AND tcdt.SoHopDong = @SoHopDong
                            AND tcdt.HopDongChiTietREF = @HopDongChiTietID
                            AND tcdt.DmSanPhamREF = @DmSanPhamREF
                            AND tcdt.DmWebsiteREF = @DmWebsiteREF
                            AND tcdt.SoLuongThucChay <> 0
                            AND tcdt.DmBannerREF = @DmBannerID
					--AND tcdt.DmViTriREF = @BannerType
				
				
                    SET @CONTENT_DETAIL_LOG = N'Giá trị thay đổi:'
                        + CONVERT(NVARCHAR(30), CONVERT(BIGINT, @GiaTriThayDoi))
                        + '; Website:' + @TenWebsite 

                    SET @CountHDTD = ( SELECT   COUNT(*)
                                       FROM     ThucChayDaTinh tcdt
                                       WHERE    tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
                                                AND tcdt.SoHopDong = @SoHopDong
                                                AND tcdt.HopDongChiTietREF = @HopDongChiTietID
                                                AND tcdt.DmSanPhamREF = @DmSanPhamREF
                                                AND tcdt.DmWebsiteREF = @DmWebsiteREF
                                                AND tcdt.DmBannerREF = @DmBannerID
					--AND tcdt.DmViTriREF = @BannerType
                                     )		
                    IF ( @CountHDTD <> 0 )
					--UPDATE GIA TRI THAY DOI
                        UPDATE  ThucChayDaTinh
                        SET     GiaTriThayDoi = ( CASE WHEN @IsKhuyenMai = 0
                                                       THEN @GiaTriThayDoi
                                                       ELSE 0
                                                  END ) ,
                                GiaTriKMThayDoi = ( CASE WHEN @IsKhuyenMai = 1
                                                         THEN @GiaTriThayDoi
                                                         ELSE 0
                                                    END ) ,
                                LastModifiedAt = GETDATE()
                        WHERE   HopDongID = @HopDongREF
                                AND DmSanPhamREF = @DmSanPhamREF
                                AND DmWebsiteREF = @DmWebsiteREF
                                AND HopDongChiTietREF = @HopDongChiTietID
                                AND CONVERT(DATE, NgayThucHien) = @NgayThucHien
                                AND DmBannerREF = @DmBannerID
					--AND DmViTriREF = @BannerType
				
						--GHI LOG VIEC THAY DOI
                    INSERT  INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
                            ( [ThuChay_LogNNTinhGiaTriThayDoiID] ,
                              [HopDongREF] ,
                              [SoHopDong] ,
                              [HopDongChiTietREF] ,
                              [DmSanPhamREF] ,
                              [DmWebsiteREF] ,
                              [NgayThucHien] ,
                              [GiaTriThayDoi] ,
                              [GiaSauCK1] ,
                              [Soluong1] ,
                              [GiaSauCK2] ,
                              [Soluong2] ,
                              [NoiDungLog] ,
                              [NguonLog] ,
                              [GhiChu] ,
                              [CreatedBy] ,
                              [CreatedAt] ,
                              [LastModifiedBy] ,
                              [LastModifiedAt] ,
                              [DeletedStatus] ,
                              [PrintStatus] ,
                              [RecordStatus]
						    )
                    VALUES  ( NEWID() ,
                              @HopDongREF ,
                              @SoHopDong ,
                              @HopDongChiTietID ,
                              @DmSanPhamREF ,
                              @DmWebsiteREF ,
                              @NgayThucHien ,
                              @GiaTriThayDoi ,
                              0 ,--@DonGiaHienTai,
                              0 ,--@SoLuongHT,
                              @DonGiaBF ,
                              0 ,--@SoLuongHT,
                              @CONTENT_LOG ,
                              @NGUON_LOG ,
                              'Mobile' ,
                              'ThucChay' ,
                              GETDATE() ,
                              'ThucChay' ,
                              GETDATE() ,
                              0 ,
                              0 ,
                              0
						    )

                    EXEC sp_TC_InsertGiaTriThayDoi_Mobile @HopDongChiTietID,
                        @NgayThucHien, @GiaTriThayDoi, @DmWebsiteREF,
                        @TenWebsite, @BannerType, @DmBannerID--, @ProductUnitName			
                END
				
            FETCH NEXT FROM Record_Cursor_TCDT_Mobile INTO @DmWebsiteREF, @TenWebsite					 
        END
    END

```
