# Stored Procedure: `sp_TC_ThayDoiSoLuong_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-23 17:58:41.320000
- **Ngày sửa cuối**: 2018-11-14 15:33:14.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@CONTENT_LOG` | `nvarchar(1000)` | No |
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_TC_ThayDoiSoLuong_Mobile] 
-- Add the parameters for the stored procedure here
    @NgayThucHien DATETIME ,
    @HopDongREF INT ,
    @DmSanPhamID INT ,
    @HopDongChiTietREF INT ,
    @CONTENT_LOG NVARCHAR(500) ,
    @DmBannerID INT --Banner thay doi thong tin 
AS
    BEGIN
        DECLARE @MinDate DATETIME ,@MaxDate DATETIME,
            @SoLuongLechTreoHa BIGINT ,
            @SoLuongThucChayDuocTinh BIGINT
	
        DECLARE @SoLuongThucChay BIGINT ,
            @SoLuongHopDong BIGINT ,
            @TTChenhLechDuocTinh FLOAT ,
            @SoLuongChenhLechDuocTinh INT
	
        DECLARE @count_HDCT INT ,
            @DonGiaTheoDonViTinh FLOAT ,
            @TTThucChaySauChietKhau FLOAT ,
            @GiaTriThayDoi FLOAT ,
            @TongTienThucChay FLOAT ,
            @TongTienHopDong BIGINT ,
            @IsHDFinish INT ,
            @TongSLThucChay INT,
			@SoHopDong NVARCHAR(200)
	
		SET @SoHopDong = ''
        SET @TongTienHopDong = 0
        SET @IsHDFinish = 0
        SET @count_HDCT = 0
        SET @SoLuongLechTreoHa = 0
        SET @SoLuongThucChayDuocTinh = 0
        SET @SoLuongThucChay = 0
        SET @SoLuongHopDong = 0
        SET @DonGiaTheoDonViTinh = 0
        SET @TTThucChaySauChietKhau = 0
        SET @GiaTriThayDoi = 0
        SET @TTChenhLechDuocTinh = 0
        SET @TongTienThucChay = 0
        SET @TongSLThucChay = 0

        BEGIN

			SELECT @SoHopDong = hd.SoHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongREF
		
			--------DOI TRU CHO HDCT
			INSERT  INTO ThucChayDaTinh
                            SELECT  NEWID() ,
                                    tcdt.HopDongID ,
                                    tcdt.SoHopDong ,
                                    tcdt.DmMaHopDongREF ,
                                    tcdt.TenMaHopDong ,
                                    tcdt.NgayDanhSoHopDong ,
                                    tcdt.NgayKyHopDong ,
                                    tcdt.NhanHopDong ,
                                    tcdt.NgayNhanBanFax ,
                                    tcdt.NgayNhanHopDongBanCung ,
                                    tcdt.NgayChuyenHopDongChoKeToan ,
                                    tcdt.So ,
                                    tcdt.Thang ,
                                    tcdt.Nam ,
                                    tcdt.GiaTriHopDong ,
                                    tcdt.CongNo ,
                                    tcdt.HopDongChiTietREF ,
                                    tcdt.DangSuDung ,
                                    tcdt.IsGiayPhep ,
                                    tcdt.TrangThaiHopDong ,
                                    tcdt.IsBanCung ,
                                    tcdt.DmPhongBanREF ,
                                    tcdt.TenPhongBan ,
                                    tcdt.DmBoPhanREF ,
                                    tcdt.TenBoPhan ,
                                    tcdt.DmNhomLamViecREF ,
                                    tcdt.TenNhomLamViec ,
                                    tcdt.DmDiaDiemLamViecREF ,
                                    tcdt.TenDiaDiemLamViec ,
                                    tcdt.SysNhanVienREF ,
                                    tcdt.TenDangNhap ,
                                    tcdt.TenNhanVien ,
                                    tcdt.TenKhachHang ,
                                    tcdt.NhanHang ,
                                    tcdt.DmNhomNganhREF ,
                                    tcdt.TenNhomNganh ,
                                    tcdt.DmHinhThucQuangCao ,
                                    tcdt.TenHinhThucQuangCao ,
                                    tcdt.DmSanPhamREF ,
                                    tcdt.TenSanPham ,
                                    tcdt.DmNhomWebsiteREF ,
                                    tcdt.TenNhomWebsite ,
                                    tcdt.DmChuyenMucREF ,
                                    tcdt.TenChuyenMuc ,
                                    tcdt.DmLoaiBannerREF ,
                                    tcdt.TenLoaiBanner ,
                                    tcdt.DmViTriREF ,
                                    tcdt.TenViTri ,
                                    '' [DotChayHopDong] ,
                                    0 [SoLuongDotChayHD] ,
                                    '' [DotChayBooking] ,
                                    0 [SoLuongDotChayBooking] ,
                                    tcdt.SoLuong ,
                                    tcdt.DonViTinh ,
                                    tcdt.DonGia ,
                                    tcdt.DonGiaTheoDonVi ,
                                    tcdt.ChietKhau ,
                                    tcdt.GiamGia ,
                                    tcdt.ThanhTien ,
                                    tcdt.TiLeTuVan ,
                                    tcdt.ChiPhiTuVan ,
                                    tcdt.IsKhuyenMai ,
                                    tcdt.KhuyenMai ,
                                    tcdt.DmBannerREF ,
                                    tcdt.DmChienDichREF ,
                                    tcdt.DmWebsiteREF ,
                                    tcdt.TenWebsite ,
                                    0 AS TongViewThucChay ,
                                    0 AS TongClickThucChay ,
                                    0 AS TongSoBaiViet ,
                                    0 AS SoLuongThucChay ,
                                    @NgayThucHien AS NgayThucHien ,
                                    -SUM([ThanhTienSauTrietKhauThucChay]
                                         + [GiaTriThayDoi]) AS GiaTriThayDoi ,
                                    0 AS ThanhTienThucChayTruocTrietKhau ,
                                    0 AS GiaTriTrietKhauThucChay ,
                                    0 AS ThanhTienSauTrietKhauThucChay ,
                                    0 AS GiaTriHoaHongThucChay ,
                                    0 AS ThanhTienThucThu ,
                                    0 AS ThanhTienKM ,
                                    0 AS SoLuongThucChayKM ,
                                    -SUM(tcdt.SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa ,
                                    -SUM(tcdt.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa ,
                                    GETDATE() ,
                                    GETDATE() ,
                                    0 IsPheDuyet ,
                                    '' PheDuyetBy ,
                                    GETDATE() ,
                                    -SUM([SoLuongThucChay] + [SoLuongThayDoi]) AS SoLuongThayDoi ,
                                    -SUM(ISNULL([SoLuongThucChayKM], 0)
                                         + ISNULL([SoLuongKMThayDoi], 0)) AS SoLuongKMThayDoi ,
                                    -SUM([ThanhTienKM] + [GiaTriKMThayDoi]) AS GiaTriKMThayDoi ,
                                    @CONTENT_LOG + ' sp_TC_ThayDoiSoLuong_Mobile' GhiChu
                            FROM    dbo.ThucChayDaTinh tcdt
                            WHERE   tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                    AND tcdt.NgayThucHien < @NgayThucHien
                                    AND tcdt.DmSanPhamREF = @DmSanPhamID
									--AND tcdt.DmBannerREF = @DmBannerID
                            GROUP BY [HopDongID] ,
                                    [SoHopDong] ,
                                    [DmMaHopDongREF] ,
                                    [TenMaHopDong] ,
                                    [NgayDanhSoHopDong] ,
                                    [NgayKyHopDong] ,
                                    [NhanHopDong] ,
                                    [NgayNhanBanFax] ,
                                    [NgayNhanHopDongBanCung] ,
                                    [NgayChuyenHopDongChoKeToan] ,
                                    [So] ,
                                    [Thang] ,
                                    [Nam] ,
                                    [GiaTriHopDong] ,
                                    [CongNo] ,
                                    [HopDongChiTietREF] ,
                                    [DangSuDung] ,
                                    [IsGiayPhep] ,
                                    [TrangThaiHopDong] ,
                                    [IsBanCung] ,
                                    [DmPhongBanREF] ,
                                    [TenPhongBan] ,
                                    [DmBoPhanREF] ,
                                    [TenBoPhan] ,
                                    [DmNhomLamViecREF] ,
                                    [TenNhomLamViec] ,
                                    [DmDiaDiemLamViecREF] ,
                                    [TenDiaDiemLamViec] ,
                                    [SysNhanVienREF] ,
                                    [TenDangNhap] ,
                                    [TenNhanVien] ,
                                    [TenKhachHang] ,
                                    [NhanHang] ,
                                    [DmNhomNganhREF] ,
                                    [TenNhomNganh] ,
                                    [DmHinhThucQuangCao] ,
                                    [TenHinhThucQuangCao] ,
                                    [DmSanPhamREF] ,
                                    [TenSanPham] ,
                                    [DmNhomWebsiteREF] ,
                                    [TenNhomWebsite] ,
                                    [DmChuyenMucREF] ,
                                    [TenChuyenMuc] ,
                                    [DmLoaiBannerREF] ,
                                    [TenLoaiBanner] ,
                                    [DmViTriREF] ,
                                    [TenViTri] ,
                                    [SoLuong] ,
                                    [DonViTinh] ,
                                    [DonGia] ,
                                    [DonGiaTheoDonVi] ,
                                    [ChietKhau] ,
                                    [GiamGia] ,
                                    [ThanhTien] ,
                                    [TiLeTuVan] ,
                                    [ChiPhiTuVan] ,
                                    [IsKhuyenMai] ,
                                    [KhuyenMai] ,
                                    [DmBannerREF] ,
                                    [DmChienDichREF] ,
                                    [DmWebsiteREF] ,
                                    [TenWebsite]
			--tcdt.NgayThucHien

			-- Tinh lai
			exec [dbo].[sp_TC_ExcUpdateGTTDThucChayDaTinh_Mobile] @HopDongChiTietREF, @SoHopDong, @DmBannerID, @NgayThucHien

			----------------------------------

			--- Log
            INSERT  INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
                        SELECT  NEWID() ,
                                D.HopDongID ,
	                            --Thong tin ve ma so 
                                D.SoHopDong ,
                                A.HopDongChiTietREF ,
                                C.DmSanPhamREF AS DmSanPhamREF ,
                                A.DmWebsiteREF ,
                                @NgayThucHien NgayThucHien ,
                                ISNULL(A.GiaTriThayDoi, 0) AS GiaTriThayDoi ,
                                0 AS GiaSauCK1 ,
                                0 Soluong1 ,
                                0 AS GiaSauCK2 ,
                                0 Soluong2 ,
                                @CONTENT_LOG ,
                                N'Thay đổi hợp đồng' ,
                                'Mobile' ,
                                'ThucChay' ,
                                GETDATE() ,
                                'ThucChay' ,
                                GETDATE() ,
                                0 ,
                                0 ,
                                0
                        FROM    ( SELECT    tcdt.HopDongChiTietREF ,
                                            tcdt.DmWebsiteREF ,
                                            tcdt.TenWebsite ,
                                            0 GiaTriThayDoi
                                    FROM      dbo.ThucChayDaTinh tcdt
                                    WHERE     tcdt.HopDongChiTietREF = @HopDongChiTietREF
                                            AND ( tcdt.GiaTriThayDoi <> 0 OR tcdt.ThanhTienSauTrietKhauThucChay <> 0 )
                                            AND tcdt.DmBannerREF = @DmBannerID
                                    GROUP BY  tcdt.HopDongChiTietREF ,
                                            tcdt.DmWebsiteREF ,
                                            tcdt.TenWebsite
                                ) A
                                INNER JOIN dbo.HopDongChiTiet C ON C.HopDongChiTietID = A.HopDongChiTietREF
                                INNER JOIN dbo.HopDong D ON D.HopDongID = C.HopDongFK
                                INNER JOIN dbo.DmWebsite E ON E.DmWebsiteID = C.DmWebsiteREF
                        WHERE   D.TrangThaiHopDong <> 3
                                AND C.DeletedStatus = 0
                                AND C.DmSanPhamREF IN ( 342 )

		
        END

    END


```
