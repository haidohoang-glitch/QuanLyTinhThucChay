# Stored Procedure: `Gen_InsertOrUpdate_KhachhangThongTinTaiKhoan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-26 16:39:36.870000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.207000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangThongTinTaiKhoanID` | `bigint(8)` | No |
| `@KhachHangThongTinChungREF` | `bigint(8)` | No |
| `@SoTaiKhoan` | `nvarchar(400)` | No |
| `@NganHangREF` | `int(4)` | No |
| `@TenNganHang` | `nvarchar(400)` | No |
| `@MoTaiChiNhanh` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_KhachhangThongTinTaiKhoan] 	
@KhachHangThongTinTaiKhoanID bigint ,	
@KhachHangThongTinChungREF bigint ,	
@SoTaiKhoan nvarchar (200) ,	
@NganHangREF int ,	
@TenNganHang nvarchar (200) ,	
@MoTaiChiNhanh nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [KhachhangThongTinTaiKhoan] where [KhachhangThongTinTaiKhoanID] = @KhachhangThongTinTaiKhoanID))	
UPDATE [dbo].[KhachhangThongTinTaiKhoan] SET 	
[KhachHangThongTinChungREF] = @KhachHangThongTinChungREF,	
[SoTaiKhoan] = @SoTaiKhoan,	
[NganHangREF] = @NganHangREF,	
[TenNganHang] = @TenNganHang,	
[MoTaiChiNhanh] = @MoTaiChiNhanh,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [KhachhangThongTinTaiKhoanID] = @KhachhangThongTinTaiKhoanID	
else 	
INSERT INTO [dbo].[KhachhangThongTinTaiKhoan] (	
[KhachHangThongTinTaiKhoanID],	
[KhachHangThongTinChungREF],	
[SoTaiKhoan],	
[NganHangREF],	
[TenNganHang],	
[MoTaiChiNhanh],	
[GhiChu],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@KhachHangThongTinTaiKhoanID,	
@KhachHangThongTinChungREF,	
@SoTaiKhoan,	
@NganHangREF,	
@TenNganHang,	
@MoTaiChiNhanh,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
