# Stored Procedure: `Gen_InsertOrUpdate_DmDonViTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:39.080000
- **Ngày sửa cuối**: 2025-10-01 16:19:45.073000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmDonViTinhID` | `bigint(8)` | No |
| `@MaDonViTinh` | `nvarchar(400)` | No |
| `@TenDonViTinh` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `bigint(8)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmDonViTinh] 	
	@DmDonViTinhID bigint ,	
	@MaDonViTinh nvarchar (200) ,	
	@TenDonViTinh nvarchar (200) ,	
	@GhiChu nvarchar (200) ,	
	@CreatedBy nvarchar (200) ,	
	@CreatedAt datetime ,	
	@LastModifiedBy nvarchar (200) ,	
	@LastModifiedAt datetime ,	
	@DeletedStatus bigint ,	
	@PrintStatus int ,	
	@RecordStatus int 	
As 	
begin
		if(exists(select * from [DmDonViTinh] where [DmDonViTinhID] = @DmDonViTinhID))	
			UPDATE [dbo].[DmDonViTinh] SET 	
			[MaDonViTinh] = @MaDonViTinh,	
			[TenDonViTinh] = @TenDonViTinh,	
			[GhiChu] = @GhiChu,	
			[CreatedBy] = @CreatedBy,	
			[CreatedAt] = @CreatedAt,	
			[LastModifiedBy] = @LastModifiedBy,	
			[LastModifiedAt] = @LastModifiedAt,	
			[DeletedStatus] = @DeletedStatus,	
			[PrintStatus] = @PrintStatus,	
			[RecordStatus] = @RecordStatus where [DmDonViTinhID] = @DmDonViTinhID	
		else 	
			INSERT INTO [dbo].[DmDonViTinh] (	
			[DmDonViTinhID],	
			[MaDonViTinh],	
			[TenDonViTinh],	
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
			@DmDonViTinhID,	
			@MaDonViTinh,	
			@TenDonViTinh,	
			@GhiChu,	
			@CreatedBy,	
			@CreatedAt,	
			@LastModifiedBy,	
			@LastModifiedAt,	
			@DeletedStatus,	
			@PrintStatus,	
			@RecordStatus)

end
```
