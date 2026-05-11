# Stored Procedure: `ThucChaySelfServingUsers_InsertByAccountAndProduct`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:03.233000
- **Ngày sửa cuối**: 2015-06-10 16:07:03.233000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@ngayThucHien` | `datetime(8)` | No |
| `@account` | `nvarchar(100)` | No |
| `@sanPhamId` | `int(4)` | No |
| `@dmViTriREF` | `int(4)` | No |
| `@tenViTri` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-07-17
-- Description:	Insert du lieu thuc chay dung chung cho cac san pham tinh theo phuong phap SelfServing
-- =============================================
--
/*
	EXEC dbo.ThucChaySelfServingUsers_InsertByAccountAndProduct 
		'2015-01-01', 
		'2015-01-01',
		'2015-01-01',
		'doduyduc',
		144,
		1,
		''
*/

CREATE PROCEDURE [dbo].[ThucChaySelfServingUsers_InsertByAccountAndProduct] 
	-- Add the parameters for the stored procedure here
	@StartDate		DATETIME,
	@EndDate		DATETIME,
	@ngayThucHien	DATETIME,
	@account		NVARCHAR(50),
	@sanPhamId		INT,
	@dmViTriREF		INT,
	@tenViTri		NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Delete du lieu truoc khi insert neu da ton tai
    --DELETE FROM ThucChaySelfServingUsers WHERE NgayThucHien BETWEEN @StartDate AND @EndDate;
    TRUNCATE TABLE ThucChaySelfServingUsers;
    
	IF @sanPhamId = 585
	BEGIN
		-- Insert du lieu ThucChayAdXUser
		INSERT INTO ThucChaySelfServingUsers
		SELECT 
			NEWID()
			,[username]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[Domain]
			,SUM(CAST([ttc] AS BIGINT)) [ttc]
			,0 AS [ttv]
			--,SUM(CAST([ttv] AS BIGINT)) [ttv]
			,SUM([money]) [money]
			,SUM([pro]) [pro]
			,[IsNoiBo]
			--,@ngayThucHien [NgayThucHien]
			,@ngayThucHien [NgayThucHien]
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
			AND A.DmSanPhamREF = @sanPhamId
			AND A.username = @account
		GROUP BY
			[username]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[Domain]
			,[userid]
			,[IsNoiBo]
			,A.DonViTinh
			,[CreatedBy]
			,[LastModifiedBy]
			,DmViTriREF
			,TenViTri
	END
	ELSE
	BEGIn
		-- Insert du lieu ThucChayAdmarketUser
		INSERT INTO ThucChaySelfServingUsers
		SELECT 
			NEWID()
			,[username]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[Domain]
			,SUM(CAST([ttc] AS BIGINT)) [ttc]
			,0 AS [ttv]
			--,SUM(CAST([ttv] AS BIGINT)) [ttv]
			,SUM([money]) [money]
			,SUM([pro]) [pro]
			,[IsNoiBo]
			,@ngayThucHien [NgayThucHien]
			,GETDATE() [CreatedAt]
			,[CreatedBy]
			,GETDATE() [LastModifedAt]
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
			A.NgayThucHien BETWEEN @StartDate AND @EndDate
			AND A.username = @account
			AND A.DmSanPhamREF = @sanPhamId
		GROUP BY
			[username]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[Domain]
			,[userid]
			,[IsNoiBo]
			,[CreatedBy]
			,[LastModifiedBy]
	END	
	
END

```
