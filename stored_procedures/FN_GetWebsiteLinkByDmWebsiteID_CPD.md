# Function: `GetWebsiteLinkByDmWebsiteID_CPD`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2020-12-16 15:39:16.660000
- **Ngày sửa cuối**: 2020-12-16 15:39:21.007000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(400)` | Yes |
| `@DmWebsiteID` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[GetWebsiteLinkByDmWebsiteID_CPD]
(
	@DmWebsiteID INT,
	@TenWebsite NVARCHAR(50)
)
RETURNS NVARCHAR(200)
AS
BEGIN
	DECLARE @DomainName NVARCHAR(200)
	--voi nhom san pham CPD thi tu ngay 16/11/2020 ben bo phan CPD yeu cau ghi nhan tu dantri.com.vn -> dtri.com.vn
	IF(@DmWebsiteID = 119) -- 119 dantri.com.vn	56
		SET @DomainName = N'dtri.com.vn' --5186 dtri.com.vn	310317
	ELSE
	IF (@DmWebsiteID = 5100) --5100	m.dantri.com.vn	3146
		SET @DomainName = N'm.dtri.com.vn' -- 5185	m.dtri.com.vn	310318
	ELSE
	BEGIN
		SET @DomainName =  (SELECT WebsiteLink FROM dbo.WebsiteMapping_HDCN_Reporting 
				WHERE DmWebsiteID = @DmWebsiteID)
	END

	SET @DomainName = ISNULL(@DomainName,@TenWebsite)
	
	RETURN @DomainName

END

```
