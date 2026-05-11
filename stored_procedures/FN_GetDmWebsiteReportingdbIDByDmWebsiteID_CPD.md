# Function: `GetDmWebsiteReportingdbIDByDmWebsiteID_CPD`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2020-12-16 15:26:10.767000
- **Ngày sửa cuối**: 2020-12-16 15:36:09.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DmWebsiteID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDmWebsiteReportingdbIDByDmWebsiteID_CPD]
(
	@DmWebsiteID INT
)
RETURNS int
AS
BEGIN
	DECLARE @ID INT

	--voi nhom san pham CPD thi tu ngay 16/11/2020 ben bo phan CPD yeu cau ghi nhan tu dantri.com.vn -> dtri.com.vn
	IF(@DmWebsiteID = 119) -- 119 dantri.com.vn	56
		SET @ID = 310317 --5186 dtri.com.vn	310317
	ELSE
	IF (@DmWebsiteID = 5100) --5100	m.dantri.com.vn	3146
		SET @ID = 310318 -- 5185	m.dtri.com.vn	310318
	ELSE
	BEGIN
		SET @ID =  (SELECT DmWebsiteReportingdbID FROM dbo.WebsiteMapping_HDCN_Reporting 
			WHERE DmWebsiteID = @DmWebsiteID)
	
	END

	SET @ID = ISNULL(@ID,@DmWebsiteID)

	RETURN @ID

END



```
