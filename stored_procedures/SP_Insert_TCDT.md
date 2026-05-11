# Stored Procedure: `Insert_TCDT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-15 14:09:11.907000
- **Ngày sửa cuối**: 2020-05-15 16:38:27.103000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Nhan` | `int(4)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@ThucChayDaTinhID` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
/*
EXEC Insert_TCDT 
@HopDongID int, 
@HopDongChiTietID int, 
@DmSanPhamREF int,
@ThucChayDaTinhID ='',
@NgayThucHien ='2020-05-14',
@Nhan
@GhiChu =N'XuLy_ThucChay_TInhLai_Mkt_admatic'

*/
CREATE proc [dbo].[Insert_TCDT] 
@HopDongID int, @HopDongChiTietID int, @DmSanPhamREF int, @Nhan int, @GiaTriThayDoi float,
 @ThucChayDaTinhID nvarchar(50),
 @NgayThucHien datetime,
 @GhiChu nvarchar(200)
 as
 begin
insert into thucchaydatinh 
SELECT newid()[ThucChayDaTinhID]
      ,[HopDongID]
      ,[SoHopDong]
      ,[DmMaHopDongREF]
      ,[TenMaHopDong]
      ,[NgayDanhSoHopDong]
      ,[NgayKyHopDong]
      ,[NhanHopDong]
      ,[NgayNhanBanFax]
      ,[NgayNhanHopDongBanCung]
      ,[NgayChuyenHopDongChoKeToan]
      ,[So]
      ,[Thang]
      ,[Nam]
      ,[GiaTriHopDong]
      ,[CongNo]
      ,[HopDongChiTietREF]
      ,[DangSuDung]
      ,[IsGiayPhep]
      ,[TrangThaiHopDong]
      ,[IsBanCung]
      ,[DmPhongBanREF]
      ,[TenPhongBan]
      ,[DmBoPhanREF]
      ,[TenBoPhan]
      ,[DmNhomLamViecREF]
      ,[TenNhomLamViec]
      ,[DmDiaDiemLamViecREF]
      ,[TenDiaDiemLamViec]
      ,[SysNhanVienREF]
      ,[TenDangNhap]
      ,[TenNhanVien]
      ,[TenKhachHang]
      ,@Nhan[NhanHang]
      ,[DmNhomNganhREF]
      ,[TenNhomNganh]
      ,[DmHinhThucQuangCao]
      ,[TenHinhThucQuangCao]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmNhomWebsiteREF]
      ,[TenNhomWebsite]
      ,[DmChuyenMucREF]
      ,[TenChuyenMuc]
      ,[DmLoaiBannerREF]
      ,[TenLoaiBanner]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[DotChayHopDong]
      ,[SoLuongDotChayHD]
      ,[DotChayBooking]
      ,[SoLuongDotChayBooking]
      ,[SoLuong]
      ,[DonViTinh]
      ,[DonGia]
      ,[DonGiaTheoDonVi]
      ,[ChietKhau]
      ,[GiamGia]
      ,[ThanhTien]
      ,[TiLeTuVan]
      ,[ChiPhiTuVan]
      ,[IsKhuyenMai]
      ,[KhuyenMai]
      ,[DmBannerREF]
      ,[DmChienDichREF]
      ,[DmWebsiteREF]
      ,[TenWebsite]
      ,0[TongViewThucChay]
      ,0[TongClickThucChay]
      ,0[TongSoBaiViet]
      ,0[SoLuongThucChay]
      ,@NgayThucHien [NgayThucHien]
      ,@GiaTriThayDoi [GiaTriThayDoi]
      ,0[ThanhTienThucChayTruocTrietKhau]
      ,0[GiaTriTrietKhauThucChay]
      ,0[ThanhTienSauTrietKhauThucChay]
      ,0[GiaTriHoaHongThucChay]
      ,0[ThanhTienThucThu]
      ,0[ThanhTienKM]
      ,0[SoLuongThucChayKM]
      ,0[SoLuongThucChayLechTreoHa]
      ,0[ThanhTienLechTreoHa]
      ,getdate()[CreatedAt]
      ,getdate()[LastModifiedAt]
      ,[IsPheDuyet]
      ,[PheDuyetBy]
      ,[PheDuyetAt]
      ,-([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
      ,[SoLuongKMThayDoi]
      ,[GiaTriKMThayDoi]
      ,@GhiChu [GhiChu]
 FROM [dbo].[ThucChayDaTinh] where ThucChayDaTinhID  = @ThucChayDaTinhID
 and HopDongID =@HopDongID 
 and HopDongChiTietREF =@HopDongChiTietID
 and DmSanPhamREF =@DmSanPhamREF 
 and DmSanPhamREF = 817 and DmHinhThucQuangCao = 42
 End

```
