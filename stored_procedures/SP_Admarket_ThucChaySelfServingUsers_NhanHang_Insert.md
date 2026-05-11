# Stored Procedure: `Admarket_ThucChaySelfServingUsers_NhanHang_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-11 09:58:24.830000
- **Ngày sửa cuối**: 2016-03-25 10:54:36.037000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 2016-07-17
-- Description:	Insert du lieu thuc chay dung chung cho cac san pham tinh theo phuong phap SelfServing

    	
CREATE PROCEDURE [dbo].[Admarket_ThucChaySelfServingUsers_NhanHang_Insert] 
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
    TRUNCATE TABLE ThucChaySelfServingUsers_NhanHang;
    
    DECLARE @TableTeam TABLE 
    	(
	[ThucChayAdmarketUserID] [uniqueidentifier],
	[username] [nvarchar](50) ,
	[DmSanPhamREF] [int] ,
	[TenSanPham] [nvarchar](50) ,
	[Domain] [nvarchar](200) ,
	[ttc] [int] ,
	[ttv] [int] ,
	[money] [float] ,
	[pro] [float] ,
	[IsNoiBo] [int] ,
	[NgayThucHien] [datetime] ,
	[CreatedAt] [datetime] ,
	[CreatedBy] [nvarchar](50) ,
	[LastModifedAt] [datetime] ,
	[LastModifiedBy] [nvarchar](50) ,
	[userid] [int] ,
	[DmNhanHangREF] [int] ,
	[TenNhanHang] [nvarchar](500),
	DmViTriREF INT  )
	
	INSERT INTO @TableTeam 
	SELECT [ThucChayAdmarketUserID] ,
	[username]  ,
	[DmSanPhamREF]  ,
	[TenSanPham]  ,
	[Domain] ,
	[ttc] [int] ,
	[ttv] [int] ,
	[money] [float] ,
	[pro] [float] ,
	[IsNoiBo] [int] ,
	[NgayThucHien]  ,
	[CreatedAt]  ,
	[CreatedBy]  ,
	[LastModifedAt]  ,
	[LastModifiedBy]  ,
	[userid]  ,
	[DmNhanHangREF]  ,
	[TenNhanHang] ,
	CASE WHEN DmSanPhamREF IN  (144,628) THEN 1
		 WHEN DmSanPhamREF = 585 AND TenSanPham = 'adx' THEN 1
		 WHEN DmSanPhamREF = 585 AND TenSanPham = 'mobx' THEN 2
		 WHEN DmSanPhamREF = 585 AND TenSanPham = 'ecomx' THEN 3
		 ELSE 1 END DmViTriREF
	FROM ThucChayAdmarketUser_NhanHang WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
	
    -- Insert du lieu ThucChayAdmarketUser
    INSERT INTO ThucChaySelfServingUsers_NhanHang
    SELECT NEWID()
      ,[username]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[Domain]
      ,SUM([ttc])
      ,SUM([ttv])
      ,SUM([money])
      ,SUM([pro])
      ,[IsNoiBo]
      ,[NgayThucHien]
      ,[CreatedAt]
      ,[CreatedBy]
      ,[LastModifedAt]
      ,[LastModifiedBy]
      ,[userid]
      ,[DonViTinh]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[DmNhanHangREF]
      ,[TenNhanHang]
    FROM
    (
    SELECT 
		 [username]
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
		, DmViTriREF
		,'' TenViTri
		,A.DmNhanHangREF
		,A.TenNhanHang
    FROM @TableTeam A
    WHERE 
		A.NgayThucHien BETWEEN @StartDate AND @EndDate
		AND A.IsNoiBo = 0
		--AND A.username = 'tienganh123';
	UNION ALL
	SELECT 
       [username]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[Domain]
      ,[ttc]
      ,[ttv]
      ,[money]
      ,[pro]
      ,[IsNoiBo]
      ,@StartDate
      ,[CreatedAt]
      ,[CreatedBy]
      ,[LastModifedAt]
      ,[LastModifiedBy]
      ,[userid]
      ,CASE DmSanPhamREF
			WHEN 337 THEN N'VIEW'
			ELSE N'CLICK'
		END AS DonViTinh
		,CASE WHEN TenSanPham = 'viewplus' OR TenSanPham  = 'cpc' THEN 1
			  WHEN TenSanPham = 'mobx' THEN 2
			  WHEN TenSanPham = 'ecomx' THEN 3
			  ELSE 1 END AS DmViTriREF
		,'' TenViTri
      ,[DmNhanHangREF]
      ,[TenNhanHang]
	FROM [dbo].ThucChayAdmarketUser_NhanHang_Online WHERE Domain <> N'DAHUY'
	UNION ALL
	-- Phần còn thiếu so với chiều user
	SELECT 
	username,
	DmSanPhamREF,
	TenSanPham,
	Domain,
	ttc,
	ttv,
	[money] - ISNULL((SELECT SUM([money]) FROM @TableTeam t WHERE t.username = tuser.username AND t.DmSanPhamREF = tuser.DmSanPhamREF AND t.DmViTriREF=tuser.DmViTriREF   AND NgayThucHien = @StartDate),0),
	pro,
	IsNoiBo,
	@StartDate
	,[CreatedAt]
    ,[CreatedBy]
    ,[LastModifedAt]
    ,[LastModifiedBy]
    ,[userid]
    ,DonViTinh
    ,DmViTriREF
    ,TenViTri
    ,0 [DmNhanHangREF]
    ,'' [TenNhanHang]
	FROM ThucChaySelfServingUsers tuser WHERE 1=1 
	AND tuser.IsNoiBo = 0
	AND tuser.username NOT LIKE '%soha%'
	AND tuser.NgayThucHien BETWEEN @StartDate AND @EndDate
	AND [money] - ISNULL((SELECT SUM([money]) FROM @TableTeam t WHERE t.username = tuser.username AND t.DmSanPhamREF = tuser.DmSanPhamREF AND t.DmViTriREF=tuser.DmViTriREF   AND NgayThucHien = @StartDate),0) > 0
	UNION ALL
	-- Phần còn thiếu so với chiều user
	SELECT 
	username,
	DmSanPhamREF,
	TenSanPham,
	Domain,
	ttc,
	ttv,
	[money] + pro - ISNULL((SELECT SUM([money] + pro ) FROM @TableTeam t WHERE t.username = tuser.username AND t.DmSanPhamREF = tuser.DmSanPhamREF AND t.DmViTriREF=tuser.DmViTriREF    AND NgayThucHien = @StartDate),0),
	0,
	IsNoiBo,
	@StartDate
	,[CreatedAt]
    ,[CreatedBy]
    ,[LastModifedAt]
    ,[LastModifiedBy]
    ,[userid]
    ,DonViTinh
    ,DmViTriREF
    ,TenViTri
    ,0 [DmNhanHangREF]
    ,'' [TenNhanHang]
	FROM ThucChaySelfServingUsers tuser WHERE 1=1 
	AND tuser.IsNoiBo = 1
	AND tuser.NgayThucHien BETWEEN @StartDate AND @EndDate
	AND [money] + pro - ISNULL((SELECT SUM([money] + pro ) FROM @TableTeam t WHERE t.username = tuser.username AND t.DmSanPhamREF = tuser.DmSanPhamREF AND t.DmViTriREF=tuser.DmViTriREF  AND NgayThucHien = @StartDate),0) > 0
    ) B GROUP BY [username]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[Domain]
      ,[IsNoiBo]
      ,[NgayThucHien]
      ,[CreatedAt]
      ,[CreatedBy]
      ,[LastModifedAt]
      ,[LastModifiedBy]
      ,[userid]
      ,[DonViTinh]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[DmNhanHangREF]
      ,[TenNhanHang]
	
	
	  UPDATE  [dbo].ThucChayAdmarketUser_NhanHang_Online SET Domain = N'DAHUY'
END


```
