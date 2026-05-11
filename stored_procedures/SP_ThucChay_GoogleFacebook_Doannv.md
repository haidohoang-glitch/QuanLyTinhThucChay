# Stored Procedure: `ThucChay_GoogleFacebook_Doannv`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-16 14:53:29.570000
- **Ngày sửa cuối**: 2020-09-08 17:04:04.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChay_GoogleFacebook_Doannv] '2020-09-07'
CREATE PROCEDURE [dbo].[ThucChay_GoogleFacebook_Doannv]
	-- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME
AS
    BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
        SET NOCOUNT ON;
        DECLARE @check INT 
        DECLARE @SoHopDong NVARCHAR(50) ,
            @DmSanPhamREF NVARCHAR(50) ,
            @SoLuongThucChay INT ,
            @ThanhTienThucChay FLOAT ,
            @DonViTinh NVARCHAR(50) ,
            @DmLoaiBannerREF INT ,
            @NhanHopDong NVARCHAR(500)
    -- Insert statements for procedure here
        DECLARE db_cursor CURSOR
        FOR
            SELECT  tcg.SoHopDong ,
                    tcg.DmSanPhamREF ,
                    tcg.DonViTinh ,
                    tcg.SoLuongThucChay ,
                    tcg.ThanhTienThucChay ,
                    tcg.DmLoaiBannerREF ,
                    tcg.NhanHopDong
            FROM    ThucChayGGFBInput tcg
            WHERE   CONVERT(DATE, tcg.NgayThucHien) = CONVERT(DATE, @NgayThucHien)
					--AND tcg.SoHopDong = 'QC7241018'

        OPEN db_cursor   
        FETCH NEXT FROM db_cursor INTO @SoHopDong, @DmSanPhamREF, @DonViTinh,
            @SoLuongThucChay, @ThanhTienThucChay, @DmLoaiBannerREF,
            @NhanHopDong

        WHILE @@FETCH_STATUS = 0
            BEGIN   
                PRINT ( @SoHopDong )
                PRINT ( @DmSanPhamREF )
                PRINT ( @DonViTinh )
                PRINT ( @DmLoaiBannerREF )
                SET @check = ( SELECT   dbo.fn_CheckTienGoogleFacebook_Doannv(@SoHopDong,
                                                              @DmSanPhamREF,
                                                              @NgayThucHien,
                                                              @DmLoaiBannerREF,
                                                              @DonViTinh)
                             )	  
                PRINT ( @SoHopDong )
                PRINT ( @DmSanPhamREF )
                PRINT ( @DonViTinh )
                PRINT ( @DmLoaiBannerREF )
                PRINT ( @check )
                IF ( @check = 1 )
                    EXEC [dbo].[ThucChay_GoogleFacebookInsert_Doannv] @NgayThucHien,
                        @SoHopDong, @DmSanPhamREF, @SoLuongThucChay,
                        @ThanhTienThucChay, @DonViTinh, @DmLoaiBannerREF,
                        @NhanHopDong
                IF ( @check = 2 )
                    EXEC [dbo].[ThucChay_GoogleFacebookInsertGTTD_Doannv] @NgayThucHien,
                        @SoHopDong, @DmSanPhamREF, @SoLuongThucChay,
                        @ThanhTienThucChay, @DonViTinh, @DmLoaiBannerREF,
                        @NhanHopDong
                IF ( @check = 3 )
                    EXEC [dbo].[ThucChay_GoogleFacebookInsertGTTD3_Doannv] @NgayThucHien,
                        @SoHopDong, @DmSanPhamREF, @SoLuongThucChay,
                        @ThanhTienThucChay, @DonViTinh, @DmLoaiBannerREF,
                        @NhanHopDong
                IF ( @check = 4 )
                    EXEC [dbo].[ThucChay_GoogleFacebookInsertGTTD4_Doannv] @NgayThucHien,
                        @SoHopDong, @DmSanPhamREF, @SoLuongThucChay,
                        @ThanhTienThucChay, @DonViTinh, @DmLoaiBannerREF,
                        @NhanHopDong
                FETCH NEXT FROM db_cursor INTO @SoHopDong, @DmSanPhamREF,
                    @DonViTinh, @SoLuongThucChay, @ThanhTienThucChay,
                    @DmLoaiBannerREF, @NhanHopDong
            END   

        CLOSE db_cursor   
        DEALLOCATE db_cursor
    END


--SELECT * FROM HopDongChiTiet hdct WHERE hdct.HopDongFK= 34882

```
