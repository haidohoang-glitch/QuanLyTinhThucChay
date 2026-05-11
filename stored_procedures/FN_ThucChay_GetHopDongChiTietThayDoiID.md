# Function: `ThucChay_GetHopDongChiTietThayDoiID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-07 12:37:59.073000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.013000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetHopDongChiTietThayDoiID]
(	
	@NgayThucHien datetime,
	@HopDongChiTietID int
)
RETURNS int

AS
BEGIN
	
	DECLARE @ID INT
	SET @ID =
		(				
							SELECT Top 1 A.ID
							FROM dbo.HopDongChiTietAllTemp A
							INNER JOIN dbo.HopDong B ON A.HopDongFK = B.HopDongID
							WHERE 
							A.DeletedStatus <> 1 AND 
							B.DeletedStatus <> 1 AND
							[HopDongChiTietID] = @HopDongChiTietID AND
							NgayThayDoi <= @NgayThucHien 
							Order by NgayThayDoi Desc
		)

	
	return @ID
End

```
