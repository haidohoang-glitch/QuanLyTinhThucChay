# Stored Procedure: `ReThucChayAdmarketUsers_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-18 09:47:25.563000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.327000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-09-18
-- Description:	Insert thuc chay cua nhung tai khoan co ngay phat sinh phan bo sau ngay du lieu thuc chay tra ve
-- =============================================
CREATE PROCEDURE [dbo].[ReThucChayAdmarketUsers_Insert]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    --INSERT INTO ReThucChayAdmarketUsers
    SELECT 
		NEWID()
		,[username]
		,[DmSanPhamREF]
		,[TenSanPham]
		,[Domain]
		,[ttc]
		,[ttv]
		,[money]
		,[pro]
		,[IsNoiBo]
		,[NgayThucHien]
		,[CreatedAt]
		,[CreatedBy]
		,[LastModifedAt]
		,[LastModifiedBy]
		,[userid]
		,CASE A.DmSanPhamREF
			WHEN 337 THEN N'VIEW'
			ELSE N'CLICK'
		END AS DonViTinh
    FROM ThucChayAdmarketUsers A
    WHERE 
		A.NgayThucHien = @NgayThucHien
END

```
