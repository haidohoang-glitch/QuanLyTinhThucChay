# Stored Procedure: `Gen_InsertOrUpdate_ThongTinHoTroThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-14 18:18:21.880000
- **Ngày sửa cuối**: 2016-03-14 18:18:21.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinHoTroThanhToanID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@ThongTinHanThanhToanHoaDonREF` | `int(4)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@NgayHoTroThanhToan` | `datetime(8)` | No |
| `@NgayCanThanhToan` | `datetime(8)` | No |
| `@GiaTriHoTroThanhToan` | `int(4)` | No |
| `@LaThauChi` | `int(4)` | No |
| `@NgayTienVe` | `datetime(8)` | No |
| `@GiaTriTienThucVe` | `int(4)` | No |
| `@TuoiNo` | `int(4)` | No |
| `@TrangThai` | `int(4)` | No |
| `@UserName_NguoiHoTro` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinHoTroThanhToan] 	
@ThongTinHoTroThanhToanID int ,	
@HopDongREF int ,	
@SoHopDong nvarchar (200) ,	
@ThongTinHanThanhToanHoaDonREF int ,	
@NgayThanhToan datetime ,	
@NgayHoTroThanhToan datetime ,	
@NgayCanThanhToan datetime ,	
@GiaTriHoTroThanhToan int ,	
@LaThauChi int ,	
@NgayTienVe datetime ,	
@GiaTriTienThucVe int ,	
@TuoiNo int ,	
@TrangThai int ,	
@UserName_NguoiHoTro nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedAt datetime ,	
@CreatedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@DeletedStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [ThongTinHoTroThanhToan] where [ThongTinHoTroThanhToanID] = @ThongTinHoTroThanhToanID))	
UPDATE [dbo].[ThongTinHoTroThanhToan] SET 	
[HopDongREF] = @HopDongREF,	
[SoHopDong] = @SoHopDong,	
[ThongTinHanThanhToanHoaDonREF] = @ThongTinHanThanhToanHoaDonREF,	
[NgayThanhToan] = @NgayThanhToan,	
[NgayHoTroThanhToan] = @NgayHoTroThanhToan,	
[NgayCanThanhToan] = @NgayCanThanhToan,	
[GiaTriHoTroThanhToan] = @GiaTriHoTroThanhToan,	
[LaThauChi] = @LaThauChi,	
[NgayTienVe] = @NgayTienVe,	
[GiaTriTienThucVe] = @GiaTriTienThucVe,	
[TuoiNo] = @TuoiNo,	
[TrangThai] = @TrangThai,	
[UserName_NguoiHoTro] = @UserName_NguoiHoTro,	
[GhiChu] = @GhiChu,	
[CreatedAt] = @CreatedAt,	
[CreatedBy] = @CreatedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[DeletedStatus] = @DeletedStatus,	
[RecordStatus] = @RecordStatus where [ThongTinHoTroThanhToanID] = @ThongTinHoTroThanhToanID	
else 	
INSERT INTO [dbo].[ThongTinHoTroThanhToan] (	
[ThongTinHoTroThanhToanID],	
[HopDongREF],	
[SoHopDong],	
[ThongTinHanThanhToanHoaDonREF],	
[NgayThanhToan],	
[NgayHoTroThanhToan],	
[NgayCanThanhToan],	
[GiaTriHoTroThanhToan],	
[LaThauChi],	
[NgayTienVe],	
[GiaTriTienThucVe],	
[TuoiNo],	
[TrangThai],	
[UserName_NguoiHoTro],	
[GhiChu],	
[CreatedAt],	
[CreatedBy],	
[LastModifiedAt],	
[LastModifiedBy],	
[DeletedStatus],	
[RecordStatus])	
Values 	
(	
@ThongTinHoTroThanhToanID,	
@HopDongREF,	
@SoHopDong,	
@ThongTinHanThanhToanHoaDonREF,	
@NgayThanhToan,	
@NgayHoTroThanhToan,	
@NgayCanThanhToan,	
@GiaTriHoTroThanhToan,	
@LaThauChi,	
@NgayTienVe,	
@GiaTriTienThucVe,	
@TuoiNo,	
@TrangThai,	
@UserName_NguoiHoTro,	
@GhiChu,	
@CreatedAt,	
@CreatedBy,	
@LastModifiedAt,	
@LastModifiedBy,	
@DeletedStatus,	
@RecordStatus)
```
