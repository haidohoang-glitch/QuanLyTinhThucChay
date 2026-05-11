# Function: `FormatStringWebsiteList`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-06 13:49:44.177000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@DonViTinh` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[FormatStringWebsiteList] 
(
	@DonViTinh nvarchar(4000)
)
RETURNS nvarchar(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(4000)
	BEGIN
		SET @Result = 
		CASE @DonViTinh
			 WHEN N'afamily.vn' THEN N'Afamily'
			 WHEN N'autopro.com.vn' THEN N'Autopro'
			 WHEN N'cafef.vn' THEN N'Cafef'
			 WHEN N'dantri.com.vn' THEN N'Dân trí'
			 WHEN N'gamek.vn' THEN N'GameK'
			 WHEN N'genk.vn' THEN N'GenK'
			 WHEN N'giadinh.net.vn' THEN N'Gia Đình Net'
			 WHEN N'kenh14.vn' THEN N'Kênh 14'
			 WHEN N'phapluattp.vn' THEN N'Pháp luật TP'
			 WHEN N'soha.vn' THEN N'Soha'
			 WHEN N'suckhoedoisong.vn' THEN N'Sức khỏe đời sống'
			 WHEN N'vneconomy.vn' THEN N'Vneconomy'
			 ELSE @DonViTinh
		END		
	END

	RETURN @Result

END

```
