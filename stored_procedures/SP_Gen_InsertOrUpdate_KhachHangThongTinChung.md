# Stored Procedure: `Gen_InsertOrUpdate_KhachHangThongTinChung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-26 16:35:46.230000
- **Ngày sửa cuối**: 2017-06-13 10:17:17.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangThongTinChungID` | `bigint(8)` | No |
| `@TenKhachHang` | `nvarchar(400)` | No |
| `@TenVietTat` | `nvarchar(400)` | No |
| `@TenTiengAnh` | `nvarchar(400)` | No |
| `@MaKhachHang` | `bigint(8)` | No |
| `@TenHinhThucKhachHang` | `nvarchar(400)` | No |
| `@DmHinhThucKhachHangREF` | `int(4)` | No |
| `@MaHinhThucKhachHang` | `nvarchar(400)` | No |
| `@DmLoaiKhachHang` | `int(4)` | No |
| `@TenLoaiKhachHang` | `nvarchar(400)` | No |
| `@MaSoThue` | `nvarchar(400)` | No |
| `@MaSoDangKyKinhDoanh` | `nvarchar(400)` | No |
| `@SoCMND` | `nvarchar(400)` | No |
| `@NgayCap` | `datetime(8)` | No |
| `@NoiCap` | `nvarchar(400)` | No |
| `@DiaChiKhachHang` | `nvarchar(400)` | No |
| `@SoDienThoai` | `nvarchar(400)` | No |
| `@SoDienThoai2` | `nvarchar(400)` | No |
| `@SoDienThoai3` | `nvarchar(400)` | No |
| `@Mobile` | `nvarchar(400)` | No |
| `@SoFax` | `nvarchar(400)` | No |
| `@Email` | `nvarchar(400)` | No |
| `@Email2` | `nvarchar(400)` | No |
| `@SoTaiKhoan` | `nvarchar(400)` | No |
| `@MoTaiNganHang` | `nvarchar(400)` | No |
| `@NgaySinh_NgayThanhLapCty` | `datetime(8)` | No |
| `@WebsiteCty` | `nvarchar(400)` | No |
| `@LinhVucKinhDoanh` | `nvarchar(400)` | No |
| `@KhachHangThongTinChungREF` | `int(4)` | No |
| `@KhachHangThuocCapThu` | `int(4)` | No |
| `@TenNguoiDaiDien` | `nvarchar(400)` | No |
| `@GioiTinhNguoiDaiDien` | `nvarchar(400)` | No |
| `@DmChuVuREF` | `int(4)` | No |
| `@ChucVu` | `nvarchar(400)` | No |
| `@SoDienThoaiNguoiDaiDien` | `nvarchar(400)` | No |
| `@ThongTinKhac` | `nvarchar(400)` | No |
| `@TenFileDiKem` | `nvarchar(400)` | No |
| `@UrlTaiLieu` | `nvarchar(400)` | No |
| `@MoTaTaiLieuDiKem` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CoMaSoThueYN` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@quanhuyen` | `int(4)` | No |
| `@tinh_thanhpho` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_KhachHangThongTinChung] 	
@KhachHangThongTinChungID bigint ,	
@TenKhachHang nvarchar (200) ,	
@TenVietTat nvarchar (200) ,	
@TenTiengAnh nvarchar (200) ,	
@MaKhachHang bigint ,	
@TenHinhThucKhachHang nvarchar (200) ,	
@DmHinhThucKhachHangREF int ,	
@MaHinhThucKhachHang nvarchar (200) ,	
@DmLoaiKhachHang int ,	
@TenLoaiKhachHang nvarchar (200) ,	
@MaSoThue nvarchar (200) ,	
@MaSoDangKyKinhDoanh nvarchar (200) ,	
@SoCMND nvarchar (200) ,	
@NgayCap datetime ,	
@NoiCap nvarchar (200) ,	
@DiaChiKhachHang nvarchar (200) ,	
@SoDienThoai nvarchar (200) ,	
@SoDienThoai2 nvarchar (200) ,	
@SoDienThoai3 nvarchar (200) ,	
@Mobile nvarchar (200) ,	
@SoFax nvarchar (200) ,	
@Email nvarchar (200) ,	
@Email2 nvarchar (200) ,	
@SoTaiKhoan nvarchar (200) ,	
@MoTaiNganHang nvarchar (200) ,	
@NgaySinh_NgayThanhLapCty datetime ,	
@WebsiteCty nvarchar (200) ,	
@LinhVucKinhDoanh nvarchar (200) ,	
@KhachHangThongTinChungREF int ,	
@KhachHangThuocCapThu int ,	
@TenNguoiDaiDien nvarchar (200) ,	
@GioiTinhNguoiDaiDien nvarchar (200) ,	
@DmChuVuREF int ,	
@ChucVu nvarchar (200) ,	
@SoDienThoaiNguoiDaiDien nvarchar (200) ,	
@ThongTinKhac nvarchar (200) ,	
@TenFileDiKem nvarchar (200) ,	
@UrlTaiLieu nvarchar (200) ,	
@MoTaTaiLieuDiKem nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CoMaSoThueYN int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int ,	
@quanhuyen int ,	
@tinh_thanhpho int 	
As 	
BEGIN
	SET @CreatedAt = ISNULL(@CreatedAt,'1900-01-01')
    if(exists(select * from [KhachHangThongTinChung] where [KhachHangThongTinChungID] = @KhachHangThongTinChungID))	
	UPDATE [dbo].[KhachHangThongTinChung] SET 	
	[TenKhachHang] = @TenKhachHang,	
	[TenVietTat] = @TenVietTat,	
	[TenTiengAnh] = @TenTiengAnh,	
	[MaKhachHang] = @MaKhachHang,	
	[TenHinhThucKhachHang] = @TenHinhThucKhachHang,	
	[DmHinhThucKhachHangREF] = @DmHinhThucKhachHangREF,	
	[MaHinhThucKhachHang] = @MaHinhThucKhachHang,	
	[DmLoaiKhachHang] = @DmLoaiKhachHang,	
	[TenLoaiKhachHang] = @TenLoaiKhachHang,	
	[MaSoThue] = @MaSoThue,	
	[MaSoDangKyKinhDoanh] = @MaSoDangKyKinhDoanh,	
	[SoCMND] = @SoCMND,	
	[NgayCap] = @NgayCap,	
	[NoiCap] = @NoiCap,	
	[DiaChiKhachHang] = @DiaChiKhachHang,	
	[SoDienThoai] = @SoDienThoai,	
	[SoDienThoai2] = @SoDienThoai2,	
	[SoDienThoai3] = @SoDienThoai3,	
	[Mobile] = @Mobile,	
	[SoFax] = @SoFax,	
	[Email] = @Email,	
	[Email2] = @Email2,	
	[SoTaiKhoan] = @SoTaiKhoan,	
	[MoTaiNganHang] = @MoTaiNganHang,	
	[NgaySinh_NgayThanhLapCty] = @NgaySinh_NgayThanhLapCty,	
	[WebsiteCty] = @WebsiteCty,	
	[LinhVucKinhDoanh] = @LinhVucKinhDoanh,	
	[KhachHangThongTinChungREF] = @KhachHangThongTinChungREF,	
	[KhachHangThuocCapThu] = @KhachHangThuocCapThu,	
	[TenNguoiDaiDien] = @TenNguoiDaiDien,	
	[GioiTinhNguoiDaiDien] = @GioiTinhNguoiDaiDien,	
	[DmChuVuREF] = @DmChuVuREF,	
	[ChucVu] = @ChucVu,	
	[SoDienThoaiNguoiDaiDien] = @SoDienThoaiNguoiDaiDien,	
	[ThongTinKhac] = @ThongTinKhac,	
	[TenFileDiKem] = @TenFileDiKem,	
	[UrlTaiLieu] = @UrlTaiLieu,	
	[MoTaTaiLieuDiKem] = @MoTaTaiLieuDiKem,	
	[GhiChu] = @GhiChu,	
	[CoMaSoThueYN] = @CoMaSoThueYN,	
	[CreatedBy] = @CreatedBy,	
	[CreatedAt] = @CreatedAt,	
	[LastModifiedBy] = @LastModifiedBy,	
	[LastModifiedAt] = @LastModifiedAt,	
	[DeletedStatus] = @DeletedStatus,	
	[PrintStatus] = @PrintStatus,	
	[RecordStatus] = @RecordStatus,	
	[quanhuyen] = @quanhuyen,	
	[tinh_thanhpho] = @tinh_thanhpho where [KhachHangThongTinChungID] = @KhachHangThongTinChungID	
	else 	
	INSERT INTO [dbo].[KhachHangThongTinChung] (	
	[KhachHangThongTinChungID],	
	[TenKhachHang],	
	[TenVietTat],	
	[TenTiengAnh],	
	[MaKhachHang],	
	[TenHinhThucKhachHang],	
	[DmHinhThucKhachHangREF],	
	[MaHinhThucKhachHang],	
	[DmLoaiKhachHang],	
	[TenLoaiKhachHang],	
	[MaSoThue],	
	[MaSoDangKyKinhDoanh],	
	[SoCMND],	
	[NgayCap],	
	[NoiCap],	
	[DiaChiKhachHang],	
	[SoDienThoai],	
	[SoDienThoai2],	
	[SoDienThoai3],	
	[Mobile],	
	[SoFax],	
	[Email],	
	[Email2],	
	[SoTaiKhoan],	
	[MoTaiNganHang],	
	[NgaySinh_NgayThanhLapCty],	
	[WebsiteCty],	
	[LinhVucKinhDoanh],	
	[KhachHangThongTinChungREF],	
	[KhachHangThuocCapThu],	
	[TenNguoiDaiDien],	
	[GioiTinhNguoiDaiDien],	
	[DmChuVuREF],	
	[ChucVu],	
	[SoDienThoaiNguoiDaiDien],	
	[ThongTinKhac],	
	[TenFileDiKem],	
	[UrlTaiLieu],	
	[MoTaTaiLieuDiKem],	
	[GhiChu],	
	[CoMaSoThueYN],	
	[CreatedBy],	
	[CreatedAt],	
	[LastModifiedBy],	
	[LastModifiedAt],	
	[DeletedStatus],	
	[PrintStatus],	
	[RecordStatus],	
	[quanhuyen],	
	[tinh_thanhpho])	
	Values 	
	(	
	@KhachHangThongTinChungID,	
	@TenKhachHang,	
	@TenVietTat,	
	@TenTiengAnh,	
	@MaKhachHang,	
	@TenHinhThucKhachHang,	
	@DmHinhThucKhachHangREF,	
	@MaHinhThucKhachHang,	
	@DmLoaiKhachHang,	
	@TenLoaiKhachHang,	
	@MaSoThue,	
	@MaSoDangKyKinhDoanh,	
	@SoCMND,	
	@NgayCap,	
	@NoiCap,	
	@DiaChiKhachHang,	
	@SoDienThoai,	
	@SoDienThoai2,	
	@SoDienThoai3,	
	@Mobile,	
	@SoFax,	
	@Email,	
	@Email2,	
	@SoTaiKhoan,	
	@MoTaiNganHang,	
	@NgaySinh_NgayThanhLapCty,	
	@WebsiteCty,	
	@LinhVucKinhDoanh,	
	@KhachHangThongTinChungREF,	
	@KhachHangThuocCapThu,	
	@TenNguoiDaiDien,	
	@GioiTinhNguoiDaiDien,	
	@DmChuVuREF,	
	@ChucVu,	
	@SoDienThoaiNguoiDaiDien,	
	@ThongTinKhac,	
	@TenFileDiKem,	
	@UrlTaiLieu,	
	@MoTaTaiLieuDiKem,	
	@GhiChu,	
	@CoMaSoThueYN,	
	@CreatedBy,	
	@CreatedAt,	
	@LastModifiedBy,	
	@LastModifiedAt,	
	@DeletedStatus,	
	@PrintStatus,	
	@RecordStatus,	
	@quanhuyen,	
	@tinh_thanhpho)
END

```
