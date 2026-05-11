# Stored Procedure: `Gen_InsertOrUpdate_KhachHangThongTinChungLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-26 16:35:46.010000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangThongTinChungREF` | `bigint(8)` | No |
| `@TenKhachHang` | `nvarchar(400)` | No |
| `@TenVietTat` | `nvarchar(400)` | No |
| `@TenTiengAnh` | `nvarchar(400)` | No |
| `@MaKhachHang` | `bigint(8)` | No |
| `@TenHinhThucKhachHang` | `nvarchar(400)` | No |
| `@DmHinhThucKhachHangREF` | `int(4)` | No |
| `@MaHinhThucKhachHang` | `nvarchar(400)` | No |
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
| `@KhachHangThongTinChungREF1` | `int(4)` | No |
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
| `@ThoiGianLog` | `datetime(8)` | No |
| `@NguoiLog` | `nvarchar(400)` | No |
| `@LoaiLog` | `int(4)` | No |
| `@CoMaSoThueYN` | `int(4)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_KhachHangThongTinChungLog]
	@KhachHangThongTinChungREF BIGINT ,
	@TenKhachHang NVARCHAR(200) ,
	@TenVietTat NVARCHAR(200) ,
	@TenTiengAnh NVARCHAR(200) ,
	@MaKhachHang BIGINT ,
	@TenHinhThucKhachHang NVARCHAR(200) ,
	@DmHinhThucKhachHangREF INT ,
	@MaHinhThucKhachHang NVARCHAR(200) ,
	@MaSoThue NVARCHAR(200) ,
	@MaSoDangKyKinhDoanh NVARCHAR(200) ,
	@SoCMND NVARCHAR(200) ,
	@NgayCap DATETIME ,
	@NoiCap NVARCHAR(200) ,
	@DiaChiKhachHang NVARCHAR(200) ,
	@SoDienThoai NVARCHAR(200) ,
	@SoDienThoai2 NVARCHAR(200) ,
	@SoDienThoai3 NVARCHAR(200) ,
	@Mobile NVARCHAR(200) ,
	@SoFax NVARCHAR(200) ,
	@Email NVARCHAR(200) ,
	@Email2 NVARCHAR(200) ,
	@SoTaiKhoan NVARCHAR(200) ,
	@MoTaiNganHang NVARCHAR(200) ,
	@NgaySinh_NgayThanhLapCty DATETIME ,
	@WebsiteCty NVARCHAR(200) ,
	@LinhVucKinhDoanh NVARCHAR(200) ,
	@KhachHangThongTinChungREF1 INT ,
	@KhachHangThuocCapThu INT ,
	@TenNguoiDaiDien NVARCHAR(200) ,
	@GioiTinhNguoiDaiDien NVARCHAR(200) ,
	@DmChuVuREF INT ,
	@ChucVu NVARCHAR(200) ,
	@SoDienThoaiNguoiDaiDien NVARCHAR(200) ,
	@ThongTinKhac NVARCHAR(200) ,
	@TenFileDiKem NVARCHAR(200) ,
	@UrlTaiLieu NVARCHAR(200) ,
	@MoTaTaiLieuDiKem NVARCHAR(200) ,
	@GhiChu NVARCHAR(200) ,
	@ThoiGianLog DATETIME ,
	@NguoiLog NVARCHAR(200) ,
	@LoaiLog INT ,
	@CoMaSoThueYN INT ,
	@CreatedAt DATETIME ,
	@CreatedBy NVARCHAR(200) ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT
AS
BEGIN
	DECLARE @IsExist INT
	SET @IsExist = (
	        SELECT COUNT(khttcl.DmHinhThucKhachHangREF)
	        FROM   KhachHangThongTinChungLog khttcl
	        WHERE  khttcl.KhachHangThongTinChungREF = @KhachHangThongTinChungREF
	               AND khttcl.ThoiGianLog = @ThoiGianLog
	    )
	
	IF (@IsExist = 0)
	BEGIN
	    INSERT INTO [dbo].[KhachHangThongTinChungLog]
	      (
	        [KhachHangThongTinChungREF],
	        [TenKhachHang],
	        [TenVietTat],
	        [TenTiengAnh],
	        [MaKhachHang],
	        [TenHinhThucKhachHang],
	        [DmHinhThucKhachHangREF],
	        [MaHinhThucKhachHang],
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
	        [KhachHangThongTinChungREF1],
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
	        [ThoiGianLog],
	        [NguoiLog],
	        [LoaiLog],
	        [CoMaSoThueYN],
	        [CreatedAt],
	        [CreatedBy],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus]
	      )
	    VALUES
	      (
	        @KhachHangThongTinChungREF,
	        @TenKhachHang,
	        @TenVietTat,
	        @TenTiengAnh,
	        @MaKhachHang,
	        @TenHinhThucKhachHang,
	        @DmHinhThucKhachHangREF,
	        @MaHinhThucKhachHang,
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
	        @KhachHangThongTinChungREF1,
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
	        @ThoiGianLog,
	        @NguoiLog,
	        @LoaiLog,
	        @CoMaSoThueYN,
	        @CreatedAt,
	        @CreatedBy,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )
	END
END

```
