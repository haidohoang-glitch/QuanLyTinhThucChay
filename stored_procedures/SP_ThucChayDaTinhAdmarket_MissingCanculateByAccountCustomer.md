# Stored Procedure: `ThucChayDaTinhAdmarket_MissingCanculateByAccountCustomer`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-01 14:36:31.160000
- **Ngày sửa cuối**: 2014-11-19 17:36:21.610000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@Account` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-09-25
-- Description:	List phan bo co ngay thuc chay nho hon ngay tao phan bo
-- =============================================
/*
 *    EXEC dbo.ThucChayDaTinhAdmarket_MissingCanculateByAccountCustomer '2014-08-01', '2014-09-30',
 			'thiepgialong',
 			'2014-09-30'
 */
 
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_MissingCanculateByAccountCustomer]
	-- Add the parameters for the stored procedure here
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@Account	nvarchar(50),
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	DECLARE 
			@SanPhamID	INT,
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
				--AND cast(A.NgayThucHien AS DATE) BETWEEN '2014-01-01' AND  @NgayThucHien
				--AND A.NgayThucHien = @NgayThucHien
				AND B.DmSanPhamREF in (144,299,337)		
				--AND B.DmSanPhamREF = 337		
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
				AND A.DmSanPhamREF in (144,299,337)
				--AND A.DmSanPhamREF = 337
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
		AND (T2.TongTien IS NULL OR T1.TongTien <> T2.TongTien)
		
	OPEN account_cursor
	
	FETCH NEXT FROM account_cursor INTO @account, @SanPhamID, @TenSanPham, @DonViTinh
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		
		--SET @NgayThucHien = '2014-09-29' --CAST((SELECT DATEADD(s,-1,DATEADD(mm, DATEDIFF(m,0,@EndDate)+1,0))) AS DATE);
		
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
			AND A.NgayThucHien BETWEEN @StartDate AND @EndDate
			--AND A.NgayThucHien BETWEEN '2014-09-20' AND '2014-09-26'
			AND A.username = @account
			--AND A.DmSanPhamREF = 337
		GROUP BY
			[username]
			,[DmSanPhamREF]
			,[TenSanPham]
			,[Domain]
			,[IsNoiBo]
		
		-- Tinh
		EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhAdmarket 
    			@NgayThucHien, 
    			@SanPhamID, 
    			@account,
    			@DonViTinh,
    			N'Admarket_Chay_Lai_Du_Lieu'
		
		FETCH NEXT FROM account_cursor INTO @account, @SanPhamID, @TenSanPham, @DonViTinh
	END
	
	CLOSE account_cursor;
	DEALLOCATE account_cursor;
END

```
