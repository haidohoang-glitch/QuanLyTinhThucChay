# Stored Procedure: `ThucChay_GoogleFacebook_HuyPhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-04 15:23:03.040000
- **Ngày sửa cuối**: 2017-10-09 14:24:47.713000

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
--EXEC [dbo].[ThucChay_GoogleFacebook_TinhLai] '2016-03-18'
CREATE PROCEDURE [dbo].[ThucChay_GoogleFacebook_HuyPhanBo]
    @NgayThucHien DATETIME
AS
    BEGIN
	
	----- Truong hop xoa phan bo

		DECLARE @SoLuongPhanBo INT
		DECLARE @ThanhTienPhanBo FLOAT
		DECLARE @HopDongChiTietID INT

        DECLARE icursor CURSOR
        FOR
            SELECT  HopDongChiTietID
            FROM    dbo.HopDongChiTiet
            WHERE   CONVERT(DATE, LastModifiedAt) = @NgayThucHien
                    AND DeletedStatus = 1
                    AND TenSanPham IN ( N'Google Ads', N'Facebook Ads',
                                        N'Chi phí quản lý' )
                    AND DmLoaiREF <> 13

        OPEN icursor  

        FETCH NEXT FROM icursor   
			INTO @HopDongChiTietID

        WHILE @@FETCH_STATUS = 0
            BEGIN  
                DECLARE @SHD NVARCHAR(50)

                SET @SHD = ( SELECT TOP 1
                                    HD.SoHopDong
                             FROM   dbo.HopDongChiTiet CT
                                    INNER JOIN dbo.HopDong HD ON CT.HopDongFK = HD.HopDongID
                             WHERE  HopDongChiTietID = @HopDongChiTietID
                           )

		-- Doi tru    
                INSERT  INTO dbo.ThucChayDaTinh
                        SELECT  NEWID() ,
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
                                -SoLuongThucChay ,
                                @NgayThucHien ,
                                -GiaTriThayDoi ,
                                ThanhTienThucChayTruocTrietKhau ,
                                GiaTriTrietKhauThucChay ,
                                -ThanhTienSauTrietKhauThucChay ,
                                GiaTriHoaHongThucChay ,
                                -ThanhTienThucThu ,
                                -ThanhTienKM ,
                                -SoLuongThucChayKM ,
                                SoLuongThucChayLechTreoHa ,
                                ThanhTienLechTreoHa ,
                                GETDATE() ,
                                GETDATE() ,
                                IsPheDuyet ,
                                PheDuyetBy ,
                                PheDuyetAt ,
                                -SoLuongThayDoi ,
                                -SoLuongKMThayDoi ,
                                -GiaTriKMThayDoi ,
                                N'Doi tru xoa phan bo'
                        FROM    dbo.ThucChayDaTinh
                        WHERE   HopDongChiTietREF = @HopDongChiTietID
                                AND TenSanPham IN ( N'Google Ads',
                                                    N'Facebook Ads',
                                                    N'Chi phí quản lý' ) 

		-- Tinh lai
                EXEC ThucChay_GoogleFacebook_TinhLai @NgayThucHien, @SHD
	 
                FETCH NEXT FROM icursor   
					INTO @HopDongChiTietID 
            END   
        CLOSE icursor;  
        DEALLOCATE icursor;  

    END


```
