# Stored Procedure: `Gen_InsertOrUpdate_NhanSuSoYeuLyLichLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:37:37.487000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.033000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichLogID` | `bigint(8)` | No |
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |
| `@MaNhanSu` | `nvarchar(400)` | No |
| `@HoVaTen` | `nvarchar(400)` | No |
| `@BiDanh` | `nvarchar(400)` | No |
| `@NgaySinh` | `datetime(8)` | No |
| `@NoiSinh` | `nvarchar(400)` | No |
| `@GioiTinh` | `int(4)` | No |
| `@SoCMTND` | `nvarchar(400)` | No |
| `@NoiCap` | `nvarchar(400)` | No |
| `@NgayCap` | `datetime(8)` | No |
| `@HoKhauThuongTru` | `nvarchar(400)` | No |
| `@DiaChiThuongTru` | `nvarchar(400)` | No |
| `@DiaChiLienHe` | `nvarchar(400)` | No |
| `@DanToc` | `nvarchar(400)` | No |
| `@TonGiao` | `nvarchar(400)` | No |
| `@TrinhDoVanHoa` | `nvarchar(400)` | No |
| `@TrinhDoNgoaiNgu` | `nvarchar(400)` | No |
| `@QuaTrinhBanThan` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Email` | `nvarchar(400)` | No |
| `@EmailCaNhan` | `nvarchar(400)` | No |
| `@Mobile` | `nvarchar(400)` | No |
| `@DienThoai1` | `nvarchar(400)` | No |
| `@DienThoai2` | `nvarchar(400)` | No |
| `@Code` | `bigint(8)` | No |
| `@NgayBatDauLamViec` | `datetime(8)` | No |
| `@NgayNghiViec` | `datetime(8)` | No |
| `@ImageFIleName` | `nvarchar(400)` | No |
| `@ImageFIleNameEncode` | `nvarchar(400)` | No |
| `@MaSoThue` | `nvarchar(400)` | No |
| `@IsNhanSuYN` | `int(4)` | No |
| `@BanMem` | `nvarchar(400)` | No |
| `@ThoiGianLog` | `datetime(8)` | No |
| `@NguoiLog` | `nvarchar(400)` | No |
| `@LoaiLog` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuSoYeuLyLichLog] 	
@NhanSuSoYeuLyLichLogID bigint ,	
@NhanSuSoYeuLyLichID int ,	
@MaNhanSu nvarchar (200) ,	
@HoVaTen nvarchar (200) ,	
@BiDanh nvarchar (200) ,	
@NgaySinh datetime ,	
@NoiSinh nvarchar (200) ,	
@GioiTinh int ,	
@SoCMTND nvarchar (200) ,	
@NoiCap nvarchar (200) ,	
@NgayCap datetime ,	
@HoKhauThuongTru nvarchar (200) ,	
@DiaChiThuongTru nvarchar (200) ,	
@DiaChiLienHe nvarchar (200) ,	
@DanToc nvarchar (200) ,	
@TonGiao nvarchar (200) ,	
@TrinhDoVanHoa nvarchar (200) ,	
@TrinhDoNgoaiNgu nvarchar (200) ,	
@QuaTrinhBanThan nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@Email nvarchar (200) ,	
@EmailCaNhan nvarchar (200) ,	
@Mobile nvarchar (200) ,	
@DienThoai1 nvarchar (200) ,	
@DienThoai2 nvarchar (200) ,	
@Code bigint ,	
@NgayBatDauLamViec datetime ,	
@NgayNghiViec datetime ,	
@ImageFIleName nvarchar (200) ,	
@ImageFIleNameEncode nvarchar (200) ,	
@MaSoThue nvarchar (200) ,	
@IsNhanSuYN int ,	
@BanMem nvarchar (200) ,	
@ThoiGianLog datetime ,	
@NguoiLog nvarchar (200) ,	
@LoaiLog int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [NhanSuSoYeuLyLichLog] where [NhanSuSoYeuLyLichLogID] = @NhanSuSoYeuLyLichLogID))	
UPDATE [dbo].[NhanSuSoYeuLyLichLog] SET 	
[NhanSuSoYeuLyLichID] = @NhanSuSoYeuLyLichID,	
[MaNhanSu] = @MaNhanSu,	
[HoVaTen] = @HoVaTen,	
[BiDanh] = @BiDanh,	
[NgaySinh] = @NgaySinh,	
[NoiSinh] = @NoiSinh,	
[GioiTinh] = @GioiTinh,	
[SoCMTND] = @SoCMTND,	
[NoiCap] = @NoiCap,	
[NgayCap] = @NgayCap,	
[HoKhauThuongTru] = @HoKhauThuongTru,	
[DiaChiThuongTru] = @DiaChiThuongTru,	
[DiaChiLienHe] = @DiaChiLienHe,	
[DanToc] = @DanToc,	
[TonGiao] = @TonGiao,	
[TrinhDoVanHoa] = @TrinhDoVanHoa,	
[TrinhDoNgoaiNgu] = @TrinhDoNgoaiNgu,	
[QuaTrinhBanThan] = @QuaTrinhBanThan,	
[GhiChu] = @GhiChu,	
[Email] = @Email,	
[EmailCaNhan] = @EmailCaNhan,	
[Mobile] = @Mobile,	
[DienThoai1] = @DienThoai1,	
[DienThoai2] = @DienThoai2,	
[Code] = @Code,	
[NgayBatDauLamViec] = @NgayBatDauLamViec,	
[NgayNghiViec] = @NgayNghiViec,	
[ImageFIleName] = @ImageFIleName,	
[ImageFIleNameEncode] = @ImageFIleNameEncode,	
[MaSoThue] = @MaSoThue,	
[IsNhanSuYN] = @IsNhanSuYN,	
[BanMem] = @BanMem,	
[ThoiGianLog] = @ThoiGianLog,	
[NguoiLog] = @NguoiLog,	
[LoaiLog] = @LoaiLog,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [NhanSuSoYeuLyLichLogID] = @NhanSuSoYeuLyLichLogID	
else 	
INSERT INTO [dbo].[NhanSuSoYeuLyLichLog] (	
[NhanSuSoYeuLyLichLogID],	
[NhanSuSoYeuLyLichID],	
[MaNhanSu],	
[HoVaTen],	
[BiDanh],	
[NgaySinh],	
[NoiSinh],	
[GioiTinh],	
[SoCMTND],	
[NoiCap],	
[NgayCap],	
[HoKhauThuongTru],	
[DiaChiThuongTru],	
[DiaChiLienHe],	
[DanToc],	
[TonGiao],	
[TrinhDoVanHoa],	
[TrinhDoNgoaiNgu],	
[QuaTrinhBanThan],	
[GhiChu],	
[Email],	
[EmailCaNhan],	
[Mobile],	
[DienThoai1],	
[DienThoai2],	
[Code],	
[NgayBatDauLamViec],	
[NgayNghiViec],	
[ImageFIleName],	
[ImageFIleNameEncode],	
[MaSoThue],	
[IsNhanSuYN],	
[BanMem],	
[ThoiGianLog],	
[NguoiLog],	
[LoaiLog],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@NhanSuSoYeuLyLichLogID,	
@NhanSuSoYeuLyLichID,	
@MaNhanSu,	
@HoVaTen,	
@BiDanh,	
@NgaySinh,	
@NoiSinh,	
@GioiTinh,	
@SoCMTND,	
@NoiCap,	
@NgayCap,	
@HoKhauThuongTru,	
@DiaChiThuongTru,	
@DiaChiLienHe,	
@DanToc,	
@TonGiao,	
@TrinhDoVanHoa,	
@TrinhDoNgoaiNgu,	
@QuaTrinhBanThan,	
@GhiChu,	
@Email,	
@EmailCaNhan,	
@Mobile,	
@DienThoai1,	
@DienThoai2,	
@Code,	
@NgayBatDauLamViec,	
@NgayNghiViec,	
@ImageFIleName,	
@ImageFIleNameEncode,	
@MaSoThue,	
@IsNhanSuYN,	
@BanMem,	
@ThoiGianLog,	
@NguoiLog,	
@LoaiLog,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
