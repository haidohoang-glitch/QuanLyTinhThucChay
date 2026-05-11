# Stored Procedure: `Gen_InsertOrUpdate_ThongTinNguoiDungResetPassWord`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:07.740000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.700000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinNguoiDungResetPassWordID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichREF` | `bigint(8)` | No |
| `@TenNhanSu` | `nvarchar(400)` | No |
| `@UserName` | `nvarchar(400)` | No |
| `@PassWords` | `nvarchar(400)` | No |
| `@ActiveYN` | `int(4)` | No |
| `@IsCoHieuLucYN` | `int(4)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinNguoiDungResetPassWord] 	
@ThongTinNguoiDungResetPassWordID int ,	
@NhanSuSoYeuLyLichREF bigint ,	
@TenNhanSu nvarchar (200) ,	
@UserName nvarchar (200) ,	
@PassWords nvarchar (200) ,	
@ActiveYN int ,	
@IsCoHieuLucYN int ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [ThongTinNguoiDungResetPassWord] where [ThongTinNguoiDungResetPassWordID] = @ThongTinNguoiDungResetPassWordID))	
UPDATE [dbo].[ThongTinNguoiDungResetPassWord] SET 	
[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,	
[TenNhanSu] = @TenNhanSu,	
[UserName] = @UserName,	
[PassWords] = @PassWords,	
[ActiveYN] = @ActiveYN,	
[IsCoHieuLucYN] = @IsCoHieuLucYN,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [ThongTinNguoiDungResetPassWordID] = @ThongTinNguoiDungResetPassWordID	
else 	
INSERT INTO [dbo].[ThongTinNguoiDungResetPassWord] (	
[ThongTinNguoiDungResetPassWordID],	
[NhanSuSoYeuLyLichREF],	
[TenNhanSu],	
[UserName],	
[PassWords],	
[ActiveYN],	
[IsCoHieuLucYN],	
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
@ThongTinNguoiDungResetPassWordID,	
@NhanSuSoYeuLyLichREF,	
@TenNhanSu,	
@UserName,	
@PassWords,	
@ActiveYN,	
@IsCoHieuLucYN,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
