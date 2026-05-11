# Stored Procedure: `AdminMappingUserOTP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-10 16:52:54.840000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-06
-- Description:	Mapping user
-- =============================================
CREATE PROCEDURE [dbo].[AdminMappingUserOTP] 
	-- Add the parameters for the stored procedure here
	@TenDangNhap NVARCHAR(50)
AS
BEGIN
	DECLARE @NhanSuSoYeuLyLichREF INT
	DECLARE @OxUserREF INT
	DECLARE @Mobile NVARCHAR(50)
	DECLARE @ShortName NVARCHAR(50)	
	
	DECLARE @TableTemp TABLE (
		TenDangNhap NVARCHAR(50),
		NhanSuSoYeuLyLichREF INT,
		OxUserREF INT,
		Mobile NVARCHAR(50),
		ShortName NVARCHAR(50)
	)
	
	IF @TenDangNhap <> ''
	BEGIN
		INSERT INTO @TableTemp(TenDangNhap, NhanSuSoYeuLyLichREF,OxUserREF, Mobile, ShortName)
					(
						SELECT A.TenDangNhap, A.NhanSuSoYeuLyLichREF,A.OxUserREF, A.Mobile, A.TenVietTat
						FROM BookingUserFull A
						WHERE A.TenDangNhap = @TenDangNhap
					)
		
	END
	ELSE
	BEGIN
		INSERT INTO @TableTemp(TenDangNhap, NhanSuSoYeuLyLichREF,OxUserREF, Mobile, ShortName)
					(
						SELECT A.TenDangNhap, A.NhanSuSoYeuLyLichREF,A.OxUserREF, A.Mobile, A.TenVietTat
						FROM BookingUserFull A
					)
	END
	
	DECLARE UserCursor CURSOR FOR
	SELECT TenDangNhap FROM @TableTemp
	
	OPEN UserCursor
	
	DECLARE @CurrentUsername NVARCHAR(50)
	FETCH NEXT FROM UserCursor INTO @CurrentUsername
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @NhanSuSoYeuLyLichREF = (SELECT NhanSuSoYeuLyLichREF FROM @TableTemp WHERE TenDangNhap = @CurrentUsername)
		SET @OxUserREF = (SELECT OxUserREF FROM @TableTemp WHERE TenDangNhap = @CurrentUsername)
		SET @Mobile = (SELECT Mobile FROM @TableTemp WHERE TenDangNhap = @CurrentUsername)
		SET @ShortName = (SELECT ShortName FROM @TableTemp WHERE TenDangNhap = @CurrentUsername)
		
		UPDATE AdminUser
		SET
			NhanSuSoYeuLyLichREF = @NhanSuSoYeuLyLichREF,
			OxUserREF = @OxUserREF,
			Mobile = @Mobile,
			ShortName = @ShortName
		WHERE Username = @CurrentUsername
		
		FETCH NEXT FROM UserCursor INTO @CurrentUsername;
	END
	
	CLOSE UserCursor
	DEALLOCATE UserCursor

	SELECT * FROM AdminUser 
END

```
