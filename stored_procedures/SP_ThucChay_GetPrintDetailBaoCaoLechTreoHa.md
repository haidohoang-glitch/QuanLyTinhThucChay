# Stored Procedure: `ThucChay_GetPrintDetailBaoCaoLechTreoHa`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-13 09:11:42.247000
- **Ngày sửa cuối**: 2014-11-19 12:17:55.057000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@ListDmSanPhamREF` | `nvarchar(400)` | No |
| `@ListSoHopDong` | `nvarchar(4000)` | No |
| `@ListTenNhanVien` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetPrintDetailBaoCaoLechTreoHa] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@ListDmSanPhamREF NVARCHAR(200),
	@ListSoHopDong NVARCHAR(2000),
	@ListTenNhanVien NVARCHAR(2000),
	@TenDangNhap NVARCHAR(50)
AS
BEGIN
	DECLARE @Sql VARCHAR(8000)
	DECLARE @DauNhay NVARCHAR(50)
	
	
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand varchar(8000)
	DECLARE @Count int
	DECLARE @QuaTrinhCongTacTemp TABLE
	(
	  NhanSuID int, 
	  PhongBanREF INT,
	  BoPhanREF INT,
	  NhomLamViecREF INT,
	  ChucDanhREF INT,
	  TuNgay DATETIME,
	  DenNgay DATETIME
	)
	DECLARE @ToUserName NVARCHAR(50)
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName 

	-- Check neu co quyen xem full du lieu
	IF (@GroupPermission = -1)
	BEGIN
		PRINT 'Full quyen';

		SET @PhongID = 0;
		SET @BoPhanID = 0;
		SET @NhomLamViecID = 0;
		SET @ChucDanhID = 0;

		SET @Sql = '
			SELECT 
					T1.TenSanPham,T1.SoHopDong, T1.TenNhanVien
					,MAX(T1.TongViewHopDong) AS TongViewHopDong
					,SUM(T1.TongViewThucChay) AS TongViewThucChay
					,SUM(T1.TongViewLechTreoHa) AS TongViewLechTreoHa
					,ROUND(SUM(T1.ThanhTienThucChay),0) AS ThanhTienThucChay
					,ROUND(SUM(T1.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
				FROM
				('
					+ dbo.ThucChay_GenSQLCommandBaoCaoLechTreoHa(@StartDate,
																 @EndDate,
																 @ListDmSanPhamREF,
																 @ListSoHopDong,
																 @ListTenNhanVien,
																 @TenDangNhap,
																 @PhongID,
																 @BoPhanID,
																 @NhomLamViecID,
																 @ChucDanhID
																) + 
				')T1
				GROUP BY T1.SoHopDong,T1.TenNhanVien,T1.TenSanPham 
				ORDER BY MAX(T1.NgayKyHopDong) DESC'
			
		PRINT @Sql
		EXEC (@Sql)
	END
	ELSE
	BEGIN
		SET @SqlCommand = dbo.Fn_GetQuaTrinhCongTacByNhanVien(@TenDangNhap,@StartDate,@EndDate)
		PRINT @SqlCommand
	
		INSERT INTO @QuaTrinhCongTacTemp(NhanSuID, PhongBanREF, BoPhanREF, NhomLamViecREF, ChucDanhREF, TuNgay, DenNgay)
		EXEC (@SqlCommand)

		SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp)
	
		IF @Count <= 1
		BEGIN
			SET @PhongID = (SELECT PhongBanREF FROM @QuaTrinhCongTacTemp)
			SET @BoPhanID = (SELECT BoPhanREF FROM @QuaTrinhCongTacTemp)
			SET @NhomLamViecID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp)
			SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp)
	
			SET @Sql = '
				SELECT 
						T1.TenSanPham,T1.SoHopDong, T1.TenNhanVien
						,MAX(T1.TongViewHopDong) AS TongViewHopDong
						,SUM(T1.TongViewThucChay) AS TongViewThucChay
						,SUM(T1.TongViewLechTreoHa) AS TongViewLechTreoHa
						,ROUND(SUM(T1.ThanhTienThucChay),0) AS ThanhTienThucChay
						,ROUND(SUM(T1.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
					FROM
					('
						+ dbo.ThucChay_GenSQLCommandBaoCaoLechTreoHa(@StartDate,
																	 @EndDate,
																	 @ListDmSanPhamREF,
																	 @ListSoHopDong,
																	 @ListTenNhanVien,
																	 @TenDangNhap,
																	 @PhongID,
																	 @BoPhanID,
																	 @NhomLamViecID,
																	 @ChucDanhID
																	) + 
					')T1
					GROUP BY T1.SoHopDong,T1.TenNhanVien,T1.TenSanPham 
					ORDER BY MAX(T1.NgayKyHopDong) DESC'
			
			PRINT @Sql
			EXEC (@Sql)
		END
		ELSE
		BEGIN
			DECLARE  @NhomID int
			
			DECLARE @TableResult TABLE
			(
				TenSanPham nvarchar(50),
				SoHopDong nvarchar(50),
				TenNhanVien nvarchar(50),
				NgayKyHopDong datetime,
				TongViewHopDong BIGINT,
				TongViewThucChay BIGINT,
				TongViewLechTreoHa BIGINT,
				ThanhTienThucChay FLOAT,
				ThanhTienLechTreoHa FLOAT,
				RowNumber int
			)
		
			DECLARE Data CURSOR FOR		
				SELECT NhanSuID FROM @QuaTrinhCongTacTemp
			
			OPEN Data;
			DECLARE @CurrentID INT		
			FETCH NEXT FROM Data INTO @CurrentID;
			WHILE @@FETCH_STATUS = 0
			   BEGIN
	   				--SELECT * FROM @TableTemp WHERE ID = @CurrentID   		   			
	   				--PRINT 'CurrentID: ' + CONVERT(nvarchar(50), @CurrentID)	
	   				SET @PhongID = (SELECT PhongBanREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   				SET @BoPhanID = (SELECT BoPhanREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   				SET @NhomLamViecID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   				SET @TuNgay = (SELECT TuNgay FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   				SET @DenNgay = (SELECT DenNgay FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   				SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			
	   				IF @TuNgay < @StartDate
	   					SET @TuNgay = @StartDate
	   				
	   				IF @DenNgay > @EndDate
	   					SET @DenNgay = @EndDate	 
	   			
	   				SET @Sql = '
	   					SELECT 
							T1.TenSanPham,T1.SoHopDong, T1.TenNhanVien
							,MAX(T1.NgayKyHopDong) AS NgayKyHopDong
							,MAX(T1.TongViewHopDong) AS TongViewHopDong
							,SUM(T1.TongViewThucChay) AS TongViewThucChay
							,SUM(T1.TongViewLechTreoHa) AS TongViewLechTreoHa
							,ROUND(SUM(T1.ThanhTienThucChay),0) AS ThanhTienThucChay
							,ROUND(SUM(T1.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
							,ROW_NUMBER() OVER (ORDER BY MAX(T1.NgayKyHopDong) DESC) AS num
						FROM
						('
							+ dbo.ThucChay_GenSQLCommandBaoCaoLechTreoHa(@TuNgay,
																		 @DenNgay,
																		 @ListDmSanPhamREF,
																		 @ListSoHopDong,
																		 @ListTenNhanVien,
																		 @TenDangNhap,
																		 @PhongID,
																		 @BoPhanID,
																		 @NhomLamViecID,
																		 @ChucDanhID
																		) + 
						')T1
						GROUP BY T1.TenSanPham,T1.SoHopDong, T1.TenNhanVien
	   				'
	   				PRINT @Sql
	   				INSERT INTO @TableResult(TenSanPham,
	   										SoHopDong,
	   										TenNhanVien,
	   										NgayKyHopDong,
	   										TongViewHopDong,
	   										TongViewThucChay ,
	   										TongViewLechTreoHa,
	   										ThanhTienThucChay,
	   										ThanhTienLechTreoHa,
	   										RowNumber)
	   				EXEC (@Sql)
	   						
					FETCH NEXT FROM Data INTO @CurrentID;		  
			   END;	   
			CLOSE Data;
			DEALLOCATE Data;
		
			SELECT 
				T.TenSanPham,T.SoHopDong, T.TenNhanVien,
				T.TongViewHopDong,T.TongViewThucChay,T.TongViewLechTreoHa,
				T.ThanhTienThucChay,T.ThanhTienLechTreoHa
			FROM
			(
				SELECT 
					T1.TenSanPham,T1.SoHopDong, T1.TenNhanVien,
					MAX(T1.NgayKyHopDong) AS NgayKyHopDong,
					SUM(T1.TongViewHopDong) AS TongViewHopDong,
					SUM(T1.TongViewThucChay) AS TongViewThucChay,
					SUM(T1.TongViewLechTreoHa) AS TongViewLechTreoHa,
					SUM(T1.ThanhTienThucChay) AS ThanhTienThucChay,
					SUM(T1.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa,
					ROW_NUMBER() OVER (ORDER BY MAX(T1.NgayKyHopDong) DESC) AS num
				FROM @TableResult T1 
				GROUP BY T1.TenSanPham,T1.SoHopDong, T1.TenNhanVien
			)T
			ORDER BY T.NgayKyHopDong DESC
		
			PRINT @Sql;

		END
	END
END

```
