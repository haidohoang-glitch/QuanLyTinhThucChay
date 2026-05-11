# Stored Procedure: `sp_TC_CheckHopDongCoThayDoi_CPM_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-18 16:18:55.613000
- **Ngày sửa cuối**: 2017-09-18 16:18:55.613000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_CheckHopDongCoThayDoi_CPM] 26325,'SH020614',370,59116,'2014-06-12'

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongCoThayDoi_CPM_BySanPham] 
	-- Add the parameters for the stored procedure here
    @HopDongREF INT ,
    @SoHopDong NVARCHAR(50) ,
    @DmSanPhamREF INT ,
    @HopDongChiTietID INT ,
    @NgayThucHien DATETIME
AS
    BEGIN
	-- Declare the return variable here
        DECLARE @ChietKhauBF FLOAT ,
            @ChietKhau FLOAT ,
            @DonGiaBF FLOAT ,
            @DonGia FLOAT ,
            @HopDongChiTietThayDoiGia INT ,
            @HopDongChiTietThayDoiCK INT
        DECLARE @DotChayHopDongChiTietThayDoi INT ,
            @NgayThayDoiMax DATETIME ,
            @SoLuongHD INT ,
            @SoLuongHDBF INT
        DECLARE @SoNgayDotChayThayDoi INT ,
            @DmWebsiteREF INT ,
            @TenWebsite NVARCHAR(100) ,
            @SoLuongHT INT ,
            @TiLeThuChaySite FLOAT
	
        DECLARE @CONTENT_LOG NVARCHAR(MAX) ,
            @NGUON_LOG NVARCHAR(500) ,
            @CONTENT_DETAIL_LOG NVARCHAR(MAX)
        DECLARE @CountHDTD INT ,
            @GiaTriThayDoi FLOAT ,
            @SoLuongThucChayByWebiste INT ,
            @TongSLThucChayByWebsite BIGINT ,
            @GiaTriThayDoi_HDTD_SL FLOAT
        DECLARE @DonGiaChenhLech FLOAT ,
            @DonGiaLienKeTruoc FLOAT ,
            @SoLuongThucChay FLOAT
        DECLARE @DonGiaHienTai FLOAT ,
            @TenSanPham NVARCHAR(50) ,
            @NgayThayDoiLast DATETIME
        DECLARE @count_HDCT INT
	

        SET @SoNgayDotChayThayDoi = 0
        SET @SoLuongThucChayByWebiste = 0
        SET @CountHDTD = 0
        SET @CONTENT_LOG = ''
        SET @NGUON_LOG = ''
        SET @DotChayHopDongChiTietThayDoi = 0
        SET @HopDongChiTietThayDoiGia = 0
        SET @HopDongChiTietThayDoiCK = 0
        SET @SoLuongHD = 0
        SET @SoLuongHDBF = 0
        SET @TiLeThuChaySite = 0
        SET @TongSLThucChayByWebsite = 0
        SET @GiaTriThayDoi_HDTD_SL = 0
	--GET DONGIA VA CHIETKHAU HIEN TAI
        SET @NgayThayDoiMax = ( SELECT  CONVERT(DATE, MAX(B.NgayThayDoi))
                                FROM    dbo.HopDongChiTietThayDoi A
                                        INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
                                WHERE   A.DeletedStatus <> 1
                                        AND B.DeletedStatus <> 1
                                        AND A.HopDongChiTietREF = @HopDongChiTietID
                              )
        SET @NgayThayDoiMax = ISNULL(@NgayThayDoiMax, @NgayThucHien)
        IF ( @NgayThucHien >= @NgayThayDoiMax )
            BEGIN
                SELECT TOP 1
                        @DonGia = hdct.DonGia
                        / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh) ,
                        @ChietKhau = hdct.ChietKhau ,
                        @SoLuongHD = hdct.SoLuong
                        * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh) ,
                        @TenSanPham = hdct.TenSanPham
                FROM    dbo.HopDongChiTiet hdct
                WHERE   hdct.DeletedStatus <> 1
                        AND hdct.HopDongChiTietID = @HopDongChiTietID 
            END
        ELSE
            BEGIN
                SET @NgayThayDoiMax = ( SELECT TOP 1
                                                CONVERT(DATE, B.NgayThayDoi)
                                        FROM    dbo.HopDongChiTietThayDoi A
                                                INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
                                        WHERE   A.DeletedStatus <> 1
                                                AND B.DeletedStatus <> 1
                                                AND A.HopDongChiTietREF = @HopDongChiTietID
                                                AND CONVERT(DATE, B.NgayThayDoi) >= @NgayThucHien
                                        ORDER BY B.NgayThayDoi ASC
                                      )	
		
                SELECT TOP 1
                        @DonGia = A.DonGia
                        / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(A.DonViTinh) ,
                        @ChietKhau = A.ChietKhau ,
                        @SoLuongHD = A.SoLuong
                        * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(A.DonViTinh) ,
                        @TenSanPham = A.TenSanPham
                FROM    dbo.HopDongChiTietThayDoi A
                        INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
                WHERE   A.DeletedStatus <> 1
                        AND B.DeletedStatus <> 1
                        AND A.HopDongChiTietREF <> 0
                        AND A.HopDongChiTietREF = @HopDongChiTietID
                        AND CONVERT(DATE, B.NgayThayDoi) = @NgayThayDoiMax
                ORDER BY A.HopDongChiTietThayDoiID DESC

            END
        SET @DonGia = ISNULL(@DonGia, 0)
        SET @ChietKhau = ISNULL(@ChietKhau, 0)
        SET @SoLuongHD = ISNULL(@SoLuongHD, 0)
	--GET DONGIA VA CHIETKHAU TRUOC NGAY HIEN TAI
        SELECT TOP 1
                @DonGiaLienKeTruoc = ISNULL(tcdt.DonGiaTheoDonVi, 0) ,
                @ChietKhauBF = ISNULL(tcdt.ChietKhau, 0) ,
                @SoLuongHDBF = ISNULL(tcdt.SoLuong, 0)
        FROM    ThucChayDaTinh tcdt
        WHERE   CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
                AND tcdt.HopDongID = @HopDongREF
                AND tcdt.DmSanPhamREF = tcdt.DmSanPhamREF
                AND dbo.FormatString(tcdt.HopDongChiTietREF) = @HopDongChiTietID
        ORDER BY tcdt.NgayThucHien DESC

        SET @DonGiaLienKeTruoc = ISNULL(@DonGiaLienKeTruoc, 0)
        SET @ChietKhauBF = ISNULL(@ChietKhauBF, 0)
        SET @SoLuongHDBF = ISNULL(@SoLuongHDBF, 0)
	--TINH SO LUONG THUC CHAY
        SET @SoLuongThucChay = ( SELECT ISNULL(SUM(tcdt.SoLuongThucChay), 0)
                                        + SUM(ISNULL(tcdt.SoLuongThayDoi, 0))
                                 FROM   ThucChayDaTinh tcdt
                                 WHERE  CONVERT(DATE, tcdt.NgayThucHien) <= @NgayThucHien
                                        AND tcdt.HopDongID = @HopDongREF
                                        AND tcdt.DmSanPhamREF = tcdt.DmSanPhamREF
                                        AND dbo.FormatString(tcdt.HopDongChiTietREF) = @HopDongChiTietID
                               )
        SET @SoLuongThucChay = ISNULL(@SoLuongThucChay, 0)
	--NEU CO THAY DOI VE GIA
        IF ( @DonGia <> @DonGiaBF )
            BEGIN
                SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi giá:'
                    + CONVERT(NVARCHAR(30), @DonGiaBF) + '->'
                    + CONVERT(NVARCHAR(30), @DonGia) + ');'
                SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi:'
                    + CONVERT(NVARCHAR(50), @HopDongChiTietThayDoiGia)	
            END
	--NEU CO THAY DOI VE CHIET KHAU
        IF ( @ChietKhau <> @ChietKhauBF )
            BEGIN
                SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi chiết khấu:'
                    + CONVERT(NVARCHAR(30), @ChietKhauBF) + '->'
                    + CONVERT(NVARCHAR(30), @ChietKhau) + ');'
                SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi: '
                    + CONVERT(NVARCHAR(30), @HopDongChiTietThayDoiCK)
            END
	--TRUONG HOP HD THAY DOI SO LUONG(SOLUONG HIEN TAI NHO HON SO LUONG BAN DAU
	--TRUONG HOP SO LUONG HD HIEN TAI > SO LUONG HD TRUOC DO CHUA LAM DC

        IF ( ( ( @SoLuongHD != @SoLuongHDBF )
               OR ( @ChietKhau <> @ChietKhauBF )
               OR ( @DonGia <> @DonGiaBF )
             )
             AND ( @SoLuongThucChay > 0 )
           )
            BEGIN
                SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi số lượng:'
                    + CONVERT(NVARCHAR(30), @SoLuongHDBF) + '->'
                    + CONVERT(NVARCHAR(30), @SoLuongHD) + ');'
                SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi: '
                    + CONVERT(NVARCHAR(30), @HopDongChiTietThayDoiCK)
		--XAC DINH PHUONG PHAP TINH THUC CHAY
                SELECT  @count_HDCT = COUNT(tcdt.HopDongChiTietREF)
                FROM    ThucChayDaTinh tcdt
                WHERE   tcdt.HopDongChiTietREF = 0
                        AND tcdt.DmSanPhamREF = @DmSanPhamREF
                        AND tcdt.HopDongID = @HopDongREF
                IF ( @count_HDCT = 0 )
                    BEGIN
                        PRINT 'Tinh theo pp thuc treo'
                        EXEC [sp_TC_UpdateGiaTriTDTCCPMThucTreoByNgayLog_BySanPham] @NgayThucHien,
                            @HopDongREF, @DmSanPhamREF, @HopDongChiTietID,
                            @CONTENT_LOG	
                    END					
                ELSE
                    BEGIN
                        PRINT 'Tinh theo pp san pham'
                        EXEC [sp_TC_UpdateGiaTriTDTCCPMSanPhamByNgayLog_BySanPham] @NgayThucHien,
                            @HopDongREF, @DmSanPhamREF, @CONTENT_LOG 
                    END
            END
        ELSE
            BEGIN
                PRINT 'HD Khong thay doi so luong'
            END
	
	
    END

```
