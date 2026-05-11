# Stored Procedure: `ThucChay_GetDistinctDanhMucTest`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-14 08:23:33.167000
- **Ngày sửa cuối**: 2014-10-14 10:39:54.713000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

--EXEC [dbo].[ThucChay_GetDistinctDanhMuc]
--	-- Add the parameters for the stored procedure here
--	@GroupFieldName = 'TenSanPham',
--	@StartDate = '1/1/0001 12:00:00 AM',
--	@EndDate = '1/1/0001 12:00:00 AM',
--	@DmSanPhamREFList ='',
--	@DmWebsiteREFList ='',
--	@SoHopDongList ='',
--	@DmPhongBanREFList ='',
--	@DmBoPhanREFList ='',
--	@DmNhomLamViecREFList ='',
--	@TenNhanVienList =''

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetDistinctDanhMucTest]
	-- Add the parameters for the stored procedure here
	@GroupFieldName nvarchar(50),
	@StartDate date,
	@EndDate date,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000)
	,@TenDangNhap nvarchar(50)
AS
BEGIN
	DECLARE @sql VARCHAR(8000) ='';

	DECLARE @DmSanPhamREFFilter NVARCHAR(4000)='';
	DECLARE @DmWebsiteREFFilter NVARCHAR(4000)='';
	DECLARE @DmSoHopDongFilter NVARCHAR(4000)='';
	DECLARE @DmPhongBanREFFilter NVARCHAR(4000)='';
	DECLARE @DmBoPhanREFFilter NVARCHAR(4000)='';
	DECLARE @DmNhomLamViecREFFilter NVARCHAR(4000)='';
	DECLARE @TenNhanVienFilter NVARCHAR(4000)='';
	
	Declare @DauNhay nvarchar(50)
	Declare @GroupByFildID nvarchar(50)
	Declare @GroupByFild nvarchar(50)
	Declare @FilterString nvarchar(4000);
	DECLARE @GroupPermission INT;
	
	DECLARE @MinDateTime NVARCHAR(200)
	
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand nvarchar(4000)
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
	
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	
	
	IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild = 'DmSanPhamREF'
		SET @GroupByFildID = 'DmSanPhamREF AS ID' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENWEBSITE'
		Begin
			SET @GroupByFild = 'DmWebsiteREF'
			SET @GroupByFildID = 'DmWebsiteREF AS ID' 
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENPHONGBAN'
		Begin
			SET @GroupByFild = 'DmPhongBanREF'
			SET @GroupByFildID = 'DmPhongBanREF AS ID' 			
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENBOPHAN'
		Begin
			SET @GroupByFild = 'DmBoPhanREF'
			SET @GroupByFildID = 'DmBoPhanREF AS ID' 			
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC'
		Begin
			SET @GroupByFild = 'DmNhomLamViecREF'
			SET @GroupByFildID = 'DmNhomLamViecREF AS ID' 			
		END
	ELSE IF UPPER(@GroupFieldName) = 'SOHOPDONG'
		Begin
			SET @GroupByFild = 'SoHopDong'
			SET @GroupByFildID = 'SoHopDong AS ID' 
		END
	ELSE IF UPPER(@GroupFieldName) = 'TenNhanVien'
		Begin
			SET @GroupByFild = 'TenDangNhap'
			SET @GroupByFildID = 'TenDangNhap AS ID' 					
		End		
		
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
		
		SET @sql = 'SELECT DISTINCT '
						+ @GroupFieldName+' as Name,'+@GroupByFildID+'
					FROM
					('
						+ dbo.ThucChay_GenSQLCommandForDistinctListQuery(@StartDate,
															@EndDate,
															@DmSanPhamREFList ,
															@DmWebsiteREFList ,
															@SoHopDongList ,
															@DmPhongBanREFList ,
															@DmBoPhanREFList ,
															@DmNhomLamViecREFList ,
															@TenNhanVienList,
															@TenDangNhap,
															@PhongID,
															@BoPhanID,
															@NhomLamViecID,
															@ChucDanhID) +
					')T
					ORDER BY ' + @GroupFieldName + ' ASC'
					
		print @sql;
		exec(@sql);
	END
	ELSE
	BEGIN			
		DECLARE @TableResult TABLE
		(
			Name nvarchar(50),
			ID nvarchar(50)
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
	   			
	   			SET @Sql = ''
	   			
	   			SET @Sql = 'SELECT DISTINCT '
						+ @GroupFieldName+' as Name,'+@GroupByFildID+'
					FROM
					('
						+ dbo.ThucChay_GenSQLCommandForDistinctListQuery(@TuNgay,
															@DenNgay,
															@DmSanPhamREFList ,
															@DmWebsiteREFList ,
															@SoHopDongList ,
															@DmPhongBanREFList ,
															@DmBoPhanREFList ,
															@DmNhomLamViecREFList ,
															@TenNhanVienList,
															@TenDangNhap,
															@PhongID,
															@BoPhanID,
															@NhomLamViecID,
															@ChucDanhID) +
					')T
					ORDER BY ' + @GroupFieldName + ' ASC'
					
	   			PRINT @Sql
	   			INSERT INTO @TableResult(Name, ID)
	   			EXEC (@Sql)
	   						
				FETCH NEXT FROM Data INTO @CurrentID;		  
		   END;	   
		CLOSE Data;
		DEALLOCATE Data;

		SELECT DISTINCT
			T.Name,T.ID
		FROM @TableResult T
		
		PRINT @Sql;
		--EXEC (@SqlResult);
    END
END

```
