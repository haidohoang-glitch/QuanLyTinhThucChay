# Stored Procedure: `ThucChayDaTinhAdmarket_MissingCanculateByProduct`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-04 08:32:20.873000
- **Ngày sửa cuối**: 2014-11-19 17:36:32.410000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@Account` | `nvarchar(100)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SanPhamID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-09-25
-- Description:	List phan bo co ngay thuc chay nho hon ngay tao phan bo
-- =============================================
/*
 *    EXEC dbo.ThucChayDaTinhAdmarket_MissingCanculateByProduct '2014-01-01', '2014-10-03',
 			'windsorplazahotel',
 			'2014-08-17 00:00:00.000', 
 			'2014-09-11 16:06:04.000',
 			'2014-10-03',
 			585
 */
 
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_MissingCanculateByProduct]
	-- Add the parameters for the stored procedure here
	@StartDate		DATETIME,
	@EndDate		DATETIME,
	@Account		NVARCHAR(50),
	@FromDate		DATETIME,
	@ToDate			DATETIME,
	@NgayThucHien	DATETIME,
	@SanPhamID		INT	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	DECLARE 
			@TenSanPham	NVARCHAR(50),
			@DonViTinh	NVARCHAR(50),
			@NgayGioiHanTinh	DATETIME
			
	DECLARE @MinDate	DATETIME,
			@MaxDate	DATETIME,
			@GhiChu		NVARCHAR(255) = 'Admarket_Chay_Lai_Du_Lieu'
			
	SET @NgayGioiHanTinh = '2013-01-01';
	
	PRINT 'ABC';
	
	DECLARE account_cursor CURSOR FOR
    SELECT 
		T1.username, T1.DmSanPhamREF, T1.TenSanPham, T1.DonViTinh
	FROM
	(
		SELECT 
			T.DmSanPhamREF, T.TenSanPham,
			T.username, T.DonViTinh,
			SUM(T.ThanhTienThucChay) AS ThanhTienThucChay,
			SUM(T.ThanhTienKM) AS ThanhTienKM,
			ROUND(SUM(T.ThanhTienThucChay + T.ThanhTienKM),0) AS TongTien
		FROM
		(
			SELECT  distinct
				A.DmSanPhamREF, A.TenSanPham, A.username, 
				case when A.DmSanPhamREF = 337 THEN 'VIEW' ELSE 'CLICK' end DonViTinh,
				A.ttv, A.ttc,
				CASE WHEN A.DmSanPhamREF = 337 THEN A.ttv
					 ELSE A.ttc
				END SoLuong,
				CASE A.IsNoiBo
					WHEN 1 THEN (A.[money] + A.pro)/1.1
					ELSE A.[money]/1.1
				END ThanhTienThucChay,
				CASE A.IsNoiBo
					WHEN 1 THEN 0
					ELSE A.pro/1.1
				END ThanhTienKM,
				A.NgayThucHien
			FROM ThucChayAdmarketUsers A
				INNER JOIN HopDongChiTiet B ON B.TK_AdMarket = A.username AND A.DmSanPhamREF = B.DmSanPhamREF
				INNER JOIN HopDong C ON C.HopDongID = B.HopDongFK
			WHERE 1=1 
				AND A.username = @Account 
				AND cast(A.NgayThucHien AS DATE) BETWEEN @StartDate AND  @EndDate
				AND C.TrangThaiHopDong <> 3
				AND B.DeletedStatus = 0
				AND B.DmSanPhamREF in (144,299,337)		
				AND B.DmSanPhamREF = @SanPhamID	
			UNION
			SELECT  distinct
				A.DmSanPhamREF, A.TenSanPham, A.username, 
				case when A.DonViTinh = 'CPC' THEN 'CLICK' 
					 WHEN A.DonViTinh = 'CLICK' THEN 'CLICK'
					 ELSE 'VIEW' 
				end DonViTinh,
				A.ttv, A.ttc,
				A.ttc SoLuong,
				CASE A.IsNoiBo
					WHEN 1 THEN (A.[money] + A.pro)/1.1
					ELSE A.[money]/1.1
				END ThanhTienThucChay,
				CASE A.IsNoiBo
					WHEN 1 THEN 0
					ELSE A.pro/1.1
				END ThanhTienKM,
				A.NgayThucHien
			FROM ThucChayAdXForUsers A
				INNER JOIN HopDongChiTiet B ON B.TK_AdMarket = A.username AND A.DmSanPhamREF = B.DmSanPhamREF
				INNER JOIN HopDong C ON C.HopDongID = B.HopDongFK
			WHERE 1=1 
				AND A.username = @Account 
				AND cast(A.NgayThucHien AS DATE) BETWEEN @StartDate AND  @EndDate
				AND C.TrangThaiHopDong <> 3
				AND B.DeletedStatus = 0	
				AND B.DmSanPhamREF = @SanPhamID		
		)T
		GROUP BY T.DmSanPhamREF, T.TenSanPham
		, T.username, T.DonViTinh
	)T1 LEFT JOIN 
	(
		SELECT T.username, T.DmSanPhamREF, T.TenSanPham, T.DonViTinh,
			SUM(T.ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
			SUM(T.ThanhTienKM) AS ThanhTienKM,
			SUM(T.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa, 
			ROUND(SUM(T.ThanhTienSauTrietKhauThucChay + ThanhTienKM + T.ThanhTienLechTreoHa),0) TongTien
		FROM
		(
			SELECT 
				A.DmSanPhamREF, A.TenSanPham, A.DonViTinh,
				--A.HopDongChiTietREF,
				(SELECT hdct.TK_AdMarket
				   FROM HopDongChiTiet AS hdct WHERE hdct.HopDongChiTietID = A.HopDongChiTietREF) username,
				ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay + GiaTriThayDoi),0) ThanhTienSauTrietKhauThucChay,
				ISNULL(SUM(A.ThanhTienKM),0) AS ThanhTienKM,
				ISNULL(SUM(A.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
			FROM ThucChayDaTinhAdmarket A
			WHERE 1=1
				--and A.NgayThucHien = @NgayThucHien
				AND A.NgayThucHien BETWEEN @StartDate AND  @EndDate
				--AND A.DmSanPhamREF in (144,299,337,585)
				AND A.DmSanPhamREF = @SanPhamID
			GROUP BY
				A.DmSanPhamREF, A.TenSanPham
				, A.HopDongChiTietREF, A.DonViTinh
		)T
		WHERE T.username = @Account
		GROUP BY T.username, T.DmSanPhamREF, T.TenSanPham, T.DonViTinh
	)T2 ON T1.username = T2.username AND T1.DmSanPhamREF = T2.DmSanPhamREF AND T1.DonViTinh = T2.DonViTinh
	WHERE 1 = 1
		--AND T1.DonViTinh = 'VIEW'
		AND T1.TongTien > 0 
		AND T1.TongTien <> T2.TongTien
		
	OPEN account_cursor
	
	FETCH NEXT FROM account_cursor INTO @account, @SanPhamID, @TenSanPham, @DonViTinh
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT 'CDF'
		IF @SanPhamID = '585'
		BEGIN
			PRINT 'SanPhamID: ' + CAST(@SanPhamID AS NVARCHAR(50));
			SELECT 
				@MinDate = MIN(tcau.NgayThucHien)
				, @MaxDate = DATEADD(d,-1,MIN(cast(hdct.CreatedAt AS DATE)))
			FROM ThucChayAdXForUsers AS tcau
				INNER JOIN [ABM_Data].dbo.HopDongChiTiet AS hdct ON hdct.TK_AdMarket = tcau.username
			WHERE 1 = 1
				AND hdct.DeletedStatus = 0
				AND tcau.username = @account
				AND tcau.NgayThucHien >= @StartDate
				AND CAST(hdct.CreatedAt AS DATE) <= @EndDate
				AND hdct.CreatedAt >= @StartDate
				AND hdct.DmSanPhamREF IN (144,299,337,585)
				AND tcau.NgayThucHien >= CAST(@FromDate AS DATE)
				AND tcau.NgayThucHien < CAST(@ToDate AS DATE)
				AND tcau.DmSanPhamREF = @SanPhamID
				and hdct.DmSanPhamREF = @SanPhamID
				--AND hdct.CreatedAt >= @NgayGioiHanTinh
		END
		ELSE
		BEGIN
			PRINT 'SanPhamID: ' + CAST(@SanPhamID AS NVARCHAR(50));
			SELECT 
				@MinDate = MIN(tcau.NgayThucHien)
				, @MaxDate = DATEADD(d,-1,MIN(cast(hdct.CreatedAt AS DATE)))
			FROM ThucChayAdmarketUsers AS tcau
				INNER JOIN [ABM_Data].dbo.HopDongChiTiet AS hdct ON hdct.TK_AdMarket = tcau.username
			WHERE 1 = 1
				AND hdct.DeletedStatus = 0
				AND tcau.username = @account
				AND tcau.NgayThucHien >= @StartDate
				AND CAST(hdct.CreatedAt AS DATE) <= @EndDate
				AND hdct.CreatedAt >= @StartDate
				AND hdct.DmSanPhamREF IN (144,299,337)
				AND tcau.NgayThucHien >= CAST(@FromDate AS DATE)
				AND tcau.NgayThucHien < CAST(@ToDate AS DATE)
				AND tcau.DmSanPhamREF = @SanPhamID
				and hdct.DmSanPhamREF = @SanPhamID
				--AND hdct.CreatedAt >= @NgayGioiHanTinh
		END	
			
		--SET @NgayThucHien = CAST((SELECT DATEADD(s,-1,DATEADD(mm, DATEDIFF(m,0,@MaxDate)+1,0))) AS DATE);
		
		PRINT '@MinDate: ' + CAST(@MinDate AS NVARCHAR(50));
		PRINT '@MaxDate: ' + CAST(@MaxDate AS NVARCHAR(50));
		
		PRINT 'NgayThucHien: ' + CAST(@NgayThucHien AS NVARCHAR(50));
		PRINT 'account: ' + CAST(@account AS NVARCHAR(50));
		
		DELETE FROM ThucChaySelfServingUsers;
		
		INSERT INTO ThucChaySelfServingUsers
		SELECT 
			NEWID()
			,[username]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[Domain]
			,SUM([ttc]) AS [ttc] 
			,SUM([ttv]) AS [ttv]
			,SUM([money]) AS [money]
			,SUM([pro]) AS [pro]
			,[IsNoiBo]
			,@NgayThucHien  AS [NgayThucHien]
			,GETDATE() AS [CreatedAt]
			,'asd' AS [CreatedBy]
			,GETDATE() AS [LastModifedAt]
			,'asd' AS [LastModifiedBy]
			,0 [userid]
			,CASE A.DmSanPhamREF
				WHEN 337 THEN N'VIEW'
				ELSE N'CLICK'
			END AS DonViTinh
		FROM ThucChayAdmarketUsers A
		WHERE 1 = 1 
			AND A.NgayThucHien BETWEEN @MinDate AND @MaxDate
			--AND A.NgayThucHien BETWEEN '2014-09-20' AND '2014-09-26'
			AND A.username = @account
			--AND A.DmSanPhamREF = 337
		GROUP BY
			[username]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[Domain]
			,[IsNoiBo]
			
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
			,@NgayThucHien [NgayThucHien]
			,GETDATE() [CreatedAt]
			,[CreatedBy]
			,GETDATE() [LastModifedAt]
			,[LastModifiedBy]
			,[userid]
			,CASE A.DonViTinh
				WHEN 'View' THEN N'VIEW'
				WHEN 'CPC' THEN N'CLICK'
			END AS DonViTinh
		FROM ThucChayAdXForUsers A
		WHERE 
			A.NgayThucHien BETWEEN @MinDate AND @MaxDate
			AND A.DmSanPhamREF = 585
			AND A.username = @Account
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
		
		-- Tinh
		EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhAdmarket 
    			@NgayThucHien, 
    			@SanPhamID, 
    			@account,
    			@DonViTinh,
    			N'AdX_Chay_Lai_Du_Lieu'
		
		FETCH NEXT FROM account_cursor INTO @account, @SanPhamID, @TenSanPham, @DonViTinh
	END
	
	CLOSE account_cursor;
	DEALLOCATE account_cursor;
END

```
