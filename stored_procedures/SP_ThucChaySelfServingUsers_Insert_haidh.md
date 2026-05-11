# Stored Procedure: `ThucChaySelfServingUsers_Insert_haidh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:03.277000
- **Ngày sửa cuối**: 2015-07-21 16:34:39.377000

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
--B1. EXEC dbo.[ThucChaySelfServingUsers_Insert_haidh] '2015-06-16', '2015-06-16'
--SELECT * FROM ThucChaySelfServingUsers tcssu WHERE tcssu.username = 'datxanh_mienbac2'
--B2.DELETE FROM ThucChaySelfServingUsers WHERE username <> 'datxanh_mienbac2'
--B3. Xoa Du lieu bang online theo tk, san pham, ngay
--SELECT * FROM ThucChayAdmarketOnline tcao WHERE tcao.TaiKhoan = 'datxanh_mienbac2' AND tcao.NgayThucHien = '2015-06-16' AND tcao.DmSanPhamREF = 144
--DELETE FROM ThucChayAdmarketOnline WHERE TaiKhoan = 'datxanh_mienbac2' AND NgayThucHien = '2015-06-16' AND DmSanPhamREF = 144
--B4. Xoa bang ThucChayDaTinhAdmarket theo tk, ngay, sp
/*
SELECT * FROM ThucChayDaTinhAdmarket tcdta WHERE tcdta.NgayThucHien =  '2015-06-16' AND tcdta.DmSanPhamREF = 144
AND tcdta.HopDongChiTietREF IN (SELECT HopDongChiTietID
                                FROM HopDong hd INNER JOIN HopDongChiTiet hdct 
                                ON hd.HopDongID = hdct.HopDongFK
                                WHERE hdct.DmSanPhamREF = 144 AND hdct.TK_AdMarket = 'datxanh_mienbac2' AND hdct.DeletedStatus <> 1
                                AND hd.TrangThaiHopDong <> 3 )
delete   FROM ThucChayDaTinhAdmarket WHERE NgayThucHien =  '2015-06-16' AND DmSanPhamREF = 144
AND HopDongChiTietREF IN (SELECT HopDongChiTietID
                                FROM HopDong hd INNER JOIN HopDongChiTiet hdct 
                                ON hd.HopDongID = hdct.HopDongFK
                                WHERE hdct.DmSanPhamREF = 144 AND hdct.TK_AdMarket = 'datxanh_mienbac2' AND hdct.DeletedStatus <> 1
                                AND hd.TrangThaiHopDong <> 3 )                              
*/

--B5. Mơ sp ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_haidh
--Recommend 	--Insert data to ThucChaySelfServingUsers table
		--EXEC dbo.ThucChaySelfServingUsers_Insert_haidh @NgayThucHien, @NgayThucHien 
	--Exec ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_haidh '2015-06-16','2015-06-16'
    	
CREATE PROCEDURE [dbo].[ThucChaySelfServingUsers_Insert_haidh] 
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
		A.NgayThucHien BETWEEN @StartDate AND @EndDate
		AND A.IsNoiBo = 0
		--AND A.username = 'tienganh123';
		
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
		AND A.IsNoiBo = 0
		--AND A.username = 'tienganh123'
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
		
		-- Insert du lieu ThucChayViewPlusForUsers
	INSERT INTO ThucChaySelfServingUsers
	SELECT NEWID()
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
		,1 DmViTriREF
		,'' TenViTri
	FROM ThucChayViewPlusForUsers  A
		WHERE 
			A.NgayThucHien BETWEEN @StartDate AND @EndDate
			AND A.DmSanPhamREF = 628
			AND A.IsNoiBo = 0
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
END

```
