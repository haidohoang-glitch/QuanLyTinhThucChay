# Stored Procedure: `ThucChaySelfServingUsers_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-17 11:20:49.433000
- **Ngày sửa cuối**: 2015-03-11 18:49:35.147000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-07-17
-- Description:	Insert du lieu thuc chay dung chung cho cac san pham tinh theo phuong phap SelfServing
-- =============================================
--
-- EXEC dbo.ThucChaySelfServingUsers_Insert '2014-09-08', '2014-09-08'

CREATE PROCEDURE [dbo].[ThucChaySelfServingUsers_Insert] 
	-- Add the parameters for the stored procedure here
	@StartDate	DATETIME,
	@EndDate	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Delete du lieu truoc khi insert neu da ton tai
    --DELETE FROM ThucChaySelfServingUsers WHERE NgayThucHien BETWEEN @StartDate AND @EndDate;
    TRUNCATE TABLE ThucChaySelfServingUsers;
    
    -- Insert du lieu ThucChayAdmarketUser
    INSERT INTO ThucChaySelfServingUsers
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
		,1 DmViTriREF
		,'' TenViTri
    FROM ThucChayAdmarketUsers A
    WHERE 
		A.NgayThucHien BETWEEN @StartDate AND @EndDate;
		
	-- Insert du lieu ThucChayAdXUser
	INSERT INTO ThucChaySelfServingUsers
    SELECT 
		NEWID()
		,[username]
		,[DmSanPhamREF]
		,[TenSanPham]
		,[Domain]
		,SUM([ttc]) [ttc]
		,SUM([ttv]) [ttv]
		,SUM([money]) [money]
		,SUM([pro]) [pro]
		,[IsNoiBo]
		,[NgayThucHien]
		,MAX([CreatedAt]) [CreatedAt]
		,[CreatedBy]
		,MAX([LastModifedAt]) [LastModifedAt]
		,[LastModifiedBy]
		,[userid]
		,CASE A.DonViTinh
			WHEN 'View' THEN N'VIEW'
			WHEN 'CPC' THEN N'CLICK'
		END AS DonViTinh
		,DmViTriREF
		,TenViTri
    FROM ThucChayAdXForUsers A
    WHERE 
		A.NgayThucHien BETWEEN @StartDate AND @EndDate
		AND A.DmSanPhamREF = 585
		--AND A.username = 'adamkhoo'
    GROUP BY
		[username]
		,[DmSanPhamREF]
		,[TenSanPham]
		,[Domain]
		,[userid]
		,[IsNoiBo]
		,A.DonViTinh
		,A.NgayThucHien
		,[CreatedBy]
		,[LastModifiedBy]
		,DmViTriREF
		,TenViTri
END

```
