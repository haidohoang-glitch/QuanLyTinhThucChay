# Stored Procedure: `Gen_InsertOrUpdate_ThongTinTienVe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:18:29.583000
- **Ngày sửa cuối**: 2017-06-26 09:45:10.983000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinTienVeID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@IsPhieuThu` | `int(4)` | No |
| `@PhieuThuLinkNapTien` | `nvarchar(400)` | No |
| `@GiaTri` | `float(8)` | No |
| `@TaiKhoanKhachHang` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@GiaTriDatCoc` | `float(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinTienVe] 	
@ThongTinTienVeID int ,	
@HopDongREF int ,	
@NgayThanhToan datetime ,	
@IsPhieuThu int ,	
@PhieuThuLinkNapTien nvarchar (200) ,	
@GiaTri float ,	
@TaiKhoanKhachHang nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@RecordStatus int ,	
@PrintStatus int ,	
@GiaTriDatCoc float 	
As 	
if(exists(select * from [ThongTinTienVe] where [ThongTinTienVeID] = @ThongTinTienVeID))	
UPDATE [dbo].[ThongTinTienVe] SET 	
[HopDongREF] = @HopDongREF,	
[NgayThanhToan] = @NgayThanhToan,	
[IsPhieuThu] = @IsPhieuThu,	
[PhieuThuLinkNapTien] = @PhieuThuLinkNapTien,	
[GiaTri] = @GiaTri,	
[TaiKhoanKhachHang] = @TaiKhoanKhachHang,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[Deleted] = @DeletedStatus,	
[DeletedStatus] = @DeletedStatus,	
[RecordStatus] = @RecordStatus,	
[PrintStatus] = @PrintStatus,	
[GiaTriDatCoc] = @GiaTriDatCoc where [ThongTinTienVeID] = @ThongTinTienVeID	
else 	
INSERT INTO [dbo].[ThongTinTienVe] (	
[ThongTinTienVeID],	
[HopDongREF],	
[NgayThanhToan],	
[IsPhieuThu],	
[PhieuThuLinkNapTien],	
[GiaTri],	
[TaiKhoanKhachHang],	
[GhiChu],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[Deleted],	
[DeletedStatus],
[RecordStatus],	
[PrintStatus],	
[GiaTriDatCoc])	
Values 	
(	
@ThongTinTienVeID,	
@HopDongREF,	
@NgayThanhToan,	
@IsPhieuThu,	
@PhieuThuLinkNapTien,	
@GiaTri,	
@TaiKhoanKhachHang,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@DeletedStatus,	
@RecordStatus,	
@PrintStatus,	
@GiaTriDatCoc)
```
