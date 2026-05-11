# Stored Procedure: `OtpSetting_Save`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-26 10:46:13.503000
- **Ngày sửa cuối**: 2014-11-26 10:46:13.503000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |
| `@FullName` | `nvarchar(400)` | No |
| `@Email` | `nvarchar(400)` | No |
| `@Mobile` | `nvarchar(100)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[OtpSetting_Save] 
	@NhanSuSoYeuLyLichID	INT,
	@FullName				NVARCHAR(200),
	@Email					NVARCHAR(200),
	@Mobile					NVARCHAR(50),
	@CreatedBy				NVARCHAR(50),
	@RecordStatus			INT
AS
BEGIN	
	IF EXISTS (SELECT NhanSuSoYeuLyLichID FROM OtpSetting WHERE NhanSuSoYeuLyLichID = @NhanSuSoYeuLyLichID)
		BEGIN
			UPDATE OtpSetting
			SET								
				FullName				= @FullName,
				Email					= @Email,
				Mobile					= @Mobile,
				CreatedBy				= @CreatedBy,
				CreatedAt				= GETDATE(),
				LastModifiedBy			= @CreatedBy,
				LastModifiedAt			= GETDATE(),				
				RecordStatus			= @RecordStatus
			WHERE NhanSuSoYeuLyLichID	= @NhanSuSoYeuLyLichID
		END
	ELSE	
		BEGIN
			INSERT INTO OtpSetting
			(				
				NhanSuSoYeuLyLichID,
				FullName,
				Email,
				Mobile,
				CreatedBy,
				CreatedAt,
				LastModifiedBy,
				LastModifiedAt,
				DeletedStatus,
				PrintStatus,
				RecordStatus
			)
			VALUES
			(
				@NhanSuSoYeuLyLichID,
				@FullName,
				@Email,
				@Mobile,
				@CreatedBy,
				GETDATE(),
				@CreatedBy,
				GETDATE(),
				0,
				0,
				@RecordStatus
			)
		END		
END

```
