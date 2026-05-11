# Stored Procedure: `OtpSetting_Get_By_NhanSuSoYeuLyLichId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-26 10:46:13.483000
- **Ngày sửa cuối**: 2014-11-26 10:46:13.483000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuSoYeuLyLichId` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[OtpSetting_Get_By_NhanSuSoYeuLyLichId] 
	@NhanSuSoYeuLyLichId INT
AS
BEGIN
	SELECT NhanSuSoYeuLyLichID, FullName, Email, Mobile, RecordStatus FROM OtpSetting
	WHERE NhanSuSoYeuLyLichID = @NhanSuSoYeuLyLichId
END

```
