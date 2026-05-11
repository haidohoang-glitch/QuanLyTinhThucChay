# Stored Procedure: `Gen_InsertOrUpdate_AdminPermisionHDCN`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 10:00:56.337000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.467000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminPermisionHDCNID` | `int(4)` | No |
| `@ThoiGianDangNhap` | `datetime(8)` | No |
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |
| `@AdminGroupId` | `int(4)` | No |
| `@SalerID` | `bigint(8)` | No |
| `@KhoaNguoiDung` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `bigint(8)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_AdminPermisionHDCN] 	
@AdminPermisionHDCNID int ,	
@ThoiGianDangNhap datetime ,	
@NhanSuSoYeuLyLichID int ,	
@AdminGroupId int ,	
@SalerID bigint ,	
@KhoaNguoiDung int ,	
@TenDangNhap nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [AdminPermisionHDCN] where [AdminPermisionHDCNID] = @AdminPermisionHDCNID))	
UPDATE [dbo].[AdminPermisionHDCN] SET 	
[ThoiGianDangNhap] = @ThoiGianDangNhap,	
[NhanSuSoYeuLyLichID] = @NhanSuSoYeuLyLichID,	
[AdminGroupId] = @AdminGroupId,	
[SalerID] = @SalerID,	
[KhoaNguoiDung] = @KhoaNguoiDung,	
[TenDangNhap] = @TenDangNhap,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [AdminPermisionHDCNID] = @AdminPermisionHDCNID	
else 	
INSERT INTO [dbo].[AdminPermisionHDCN] (	
[AdminPermisionHDCNID],	
[ThoiGianDangNhap],	
[NhanSuSoYeuLyLichID],	
[AdminGroupId],	
[SalerID],	
[KhoaNguoiDung],	
[TenDangNhap],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@AdminPermisionHDCNID,	
@ThoiGianDangNhap,	
@NhanSuSoYeuLyLichID,	
@AdminGroupId,	
@SalerID,	
@KhoaNguoiDung,	
@TenDangNhap,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
