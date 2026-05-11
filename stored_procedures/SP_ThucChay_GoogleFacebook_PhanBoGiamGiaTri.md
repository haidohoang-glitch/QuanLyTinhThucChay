# Stored Procedure: `ThucChay_GoogleFacebook_PhanBoGiamGiaTri`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-04 15:26:11.427000
- **Ngày sửa cuối**: 2020-05-21 17:00:36.610000

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
--EXEC [dbo].[ThucChay_GoogleFacebook_PhanBoGiamGiaTri] '2016-03-18'
CREATE PROCEDURE [dbo].[ThucChay_GoogleFacebook_PhanBoGiamGiaTri]
    @NgayThucHien DATETIME
AS
    BEGIN
	
        DECLARE @SoLuongPhanBo INT
        DECLARE @ThanhTienPhanBo FLOAT
        DECLARE @HopDongChiTietID INT

		----- Truong hop gia tri hop dong giam

        DECLARE icursor CURSOR
        FOR
            SELECT  HopDongChiTietID ,
                    SoLuong ,
                    ThanhTien
            FROM    dbo.HopDongChiTiet
            WHERE   CONVERT(DATE, LastModifiedAt) = @NgayThucHien
                    AND TenSanPham IN ( N'Google Ads', N'Facebook Ads',
                                        N'Chi phí quản lý' )
                    AND NOT ( DmLoaiREF = 13 or DmLoaiBannerREF = 18)
                    AND DeletedStatus = 0
					--AND HopDongFK = 504747

        OPEN icursor  

        FETCH NEXT FROM icursor   
			INTO @HopDongChiTietID, @SoLuongPhanBo, @ThanhTienPhanBo

        WHILE @@FETCH_STATUS = 0
            BEGIN  
    
                DECLARE @ThanhTien_Bf FLOAT
                DECLARE @SoLuongThayDoi INT
                DECLARE @GiaTriThayDoi FLOAT
                DECLARE @SoLuongDaTinh INT
                DECLARE @ThanhTienDaTinh FLOAT

                SELECT TOP (1)
                        @ThanhTien_Bf = ThanhTien
                FROM    dbo.ThucChayDaTinh
                WHERE   HopDongChiTietREF = @HopDongChiTietID
                        AND TenSanPham IN ( N'Google Ads', N'Facebook Ads',
                                            N'Chi phí quản lý' )
                ORDER BY CreatedAt DESC

                SELECT  @SoLuongDaTinh = ISNULL(SUM(SoLuongThucChay
                                                    + SoLuongThayDoi), 0) ,
                        @ThanhTienDaTinh = ISNULL(SUM(ThanhTienSauTrietKhauThucChay
                                                      + GiaTriThayDoi), 0)
                FROM    dbo.ThucChayDaTinh
                WHERE   HopDongChiTietREF = @HopDongChiTietID
                        AND TenSanPham IN ( N'Google Ads', N'Facebook Ads',
                                            N'Chi phí quản lý' ) 


                IF @ThanhTien_Bf IS NOT NULL
                    BEGIN
                        IF @ThanhTienPhanBo < @ThanhTien_Bf
                            BEGIN
                                DECLARE @SHD NVARCHAR(50)

                                SET @SHD = ( SELECT TOP 1
                                                    HD.SoHopDong
                                             FROM   dbo.HopDongChiTiet CT
                                                    INNER JOIN dbo.HopDong HD ON CT.HopDongFK = HD.HopDongID
                                             WHERE  HopDongChiTietID = @HopDongChiTietID
                                           )


                                SET @SoLuongThayDoi = -( @SoLuongDaTinh
                                                         - @SoLuongPhanBo )
                                SET @GiaTriThayDoi = -( @ThanhTienDaTinh
                                                        - @ThanhTienPhanBo )

                                INSERT  INTO dbo.ThucChayDaTinh
                                        SELECT TOP 1
                                                NEWID() ,
                                                HopDongID ,
                                                SoHopDong ,
                                                DmMaHopDongREF ,
                                                TenMaHopDong ,
                                                NgayDanhSoHopDong ,
                                                NgayKyHopDong ,
                                                NhanHopDong ,
                                                NgayNhanBanFax ,
                                                NgayNhanHopDongBanCung ,
                                                NgayChuyenHopDongChoKeToan ,
                                                So ,
                                                Thang ,
                                                Nam ,
                                                GiaTriHopDong ,
                                                CongNo ,
                                                HopDongChiTietREF ,
                                                DangSuDung ,
                                                IsGiayPhep ,
                                                TrangThaiHopDong ,
                                                IsBanCung ,
                                                DmPhongBanREF ,
                                                TenPhongBan ,
                                                DmBoPhanREF ,
                                                TenBoPhan ,
                                                DmNhomLamViecREF ,
                                                TenNhomLamViec ,
                                                DmDiaDiemLamViecREF ,
                                                TenDiaDiemLamViec ,
                                                SysNhanVienREF ,
                                                TenDangNhap ,
                                                TenNhanVien ,
                                                TenKhachHang ,
                                                NhanHang ,
                                                DmNhomNganhREF ,
                                                TenNhomNganh ,
                                                DmHinhThucQuangCao ,
                                                TenHinhThucQuangCao ,
                                                DmSanPhamREF ,
                                                TenSanPham ,
                                                DmNhomWebsiteREF ,
                                                TenNhomWebsite ,
                                                DmChuyenMucREF ,
                                                TenChuyenMuc ,
                                                DmLoaiBannerREF ,
                                                TenLoaiBanner ,
                                                DmViTriREF ,
                                                TenViTri ,
                                                DotChayHopDong ,
                                                SoLuongDotChayHD ,
                                                DotChayBooking ,
                                                SoLuongDotChayBooking ,
                                                SoLuong ,
                                                DonViTinh ,
                                                DonGia ,
                                                DonGiaTheoDonVi ,
                                                ChietKhau ,
                                                GiamGia ,
                                                ThanhTien ,
                                                TiLeTuVan ,
                                                ChiPhiTuVan ,
                                                IsKhuyenMai ,
                                                KhuyenMai ,
                                                DmBannerREF ,
                                                DmChienDichREF ,
                                                DmWebsiteREF ,
                                                TenWebsite ,
                                                TongViewThucChay ,
                                                TongClickThucChay ,
                                                TongSoBaiViet ,
                                                0 ,
                                                @NgayThucHien ,
                                                @GiaTriThayDoi ,
                                                ThanhTienThucChayTruocTrietKhau ,
                                                GiaTriTrietKhauThucChay ,
                                                0 ,
                                                GiaTriHoaHongThucChay ,
                                                0 ,
                                                0 ,
                                                0 ,
                                                0 ,
                                                0 ,
                                                GETDATE() ,
                                                GETDATE() ,
                                                IsPheDuyet ,
                                                PheDuyetBy ,
                                                PheDuyetAt ,
                                                @SoLuongThayDoi ,
                                                0 ,
                                                0 ,
                                                N'Doi tru gia tri PB giam'
                                        FROM    dbo.ThucChayDaTinh
                                        WHERE   HopDongChiTietREF = @HopDongChiTietID
                                        ORDER BY NgayThucHien DESC


				-- Tinh lai
                                EXEC ThucChay_GoogleFacebook_TinhLai @NgayThucHien,
                                    @SHD
                            END
                    END
                
	 
                FETCH NEXT FROM icursor   
					INTO @HopDongChiTietID, @SoLuongPhanBo, @ThanhTienPhanBo 
            END   
        CLOSE icursor;  
        DEALLOCATE icursor;  


    END


```
