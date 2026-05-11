# Stored Procedure: `ThucChay_GetSyntheticFilterConditionTest`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-25 17:01:12.363000
- **Ngày sửa cuối**: 2014-10-14 10:39:54.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
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

--exec [ThucChay_GetSumFilterCondition]
--@PageIndex = 1,
--	@RecordCount = 10,
--	@GroupFieldName = N'TenSanPham',
--	@StartDate = '2013-01-01',
--	@EndDate = '2013-01-05',
--	@DmSanPhamREFList = N'',
--	@DmWebsiteREFList = N'',
--	@SoHopDongList = N'',
--	@DmPhongBanREFList = N'',
--	@DmBoPhanREFList = N'',
--	@DmNhomLamViecREFList = N'',
--	@TenNhanVienList = N''

-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-09-17
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_GetSyntheticFilterConditionTest] 
    -- Add the parameters for the stored procedure here
    @PageIndex INT = 1,
	@RecordCount INT = 10,
	@GroupFieldName nvarchar(50),
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@TenDangNhap nvarchar(50)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql VARCHAR(MAX);
    DECLARE @DauNhay NVARCHAR(50);
    Declare @GroupByFildID nvarchar(4000);
	Declare @GroupByFild nvarchar(4000);
	Declare @FilterString nvarchar(4000);
	DECLARE @GroupPermission INT;
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
	DECLARE @OrderBy NVARCHAR(50)
	
	IF UPPER(@GroupFieldName) = 'SOHOPDONG'
		SET @OrderBy = ' MAX(T2.NgayKyHopDong) DESC'
	ELSE
		SET @OrderBy = ' MAX(T2.NgayKyHopDong) DESC'
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName
    
    IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild = 'DmSanPhamREF'
		SET @GroupByFildID = 'DmSanPhamREF AS ID,' 
		
		--IF @DmSanPhamREFList=''
		--	SET @DmSanPhamREFList = dbo.GetListSanPhamByNhanVien(@TenDangNhap)
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENWEBSITE'
	Begin
		SET @GroupByFild = 'DmWebsiteREF'
		SET @GroupByFildID = 'DmWebsiteREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENPHONGBAN'
	Begin
		SET @GroupByFild = 'DmPhongBanREF'
		SET @GroupByFildID = 'DmPhongBanREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENBOPHAN'
	Begin
		SET @GroupByFild = 'DmBoPhanREF'
		SET @GroupByFildID = 'DmBoPhanREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC'
	Begin
		SET @GroupByFild = 'DmNhomLamViecREF'
		SET @GroupByFildID = 'DmNhomLamViecREF AS ID,' 
	END
	ELSE IF UPPER(@GroupFieldName) = 'SOHOPDONG'
	Begin
		SET @GroupByFild = 'SoHopDong'
		SET @GroupByFildID = 'SoHopDong AS ID,' 
	END
	ELSE IF UPPER(@GroupFieldName) = 'TENNHANVIEN'
	Begin
		SET @GroupByFild = 'TenDangNhap'
		SET @GroupByFildID = 'TenDangNhap AS ID,' 
		
	END
	
	SET @SqlCommand = dbo.Fn_GetQuaTrinhCongTacByNhanVien(@TenDangNhap,@StartDate,@EndDate)
	PRINT @SqlCommand
	
	INSERT INTO @QuaTrinhCongTacTemp(NhanSuID, PhongBanREF, BoPhanREF, NhomLamViecREF, ChucDanhREF, TuNgay, DenNgay)
	EXEC (@SqlCommand)

	SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp)
	SET @MinDate = (SELECT MIN(TuNgay) FROM @QuaTrinhCongTacTemp)
	SET @MaxDate = (SELECT MIN(DenNgay) FROM @QuaTrinhCongTacTemp)
	
	IF @Count <= 1
	BEGIN	
		SET @PhongID = (SELECT PhongBanREF FROM @QuaTrinhCongTacTemp)
		SET @BoPhanID = (SELECT BoPhanREF FROM @QuaTrinhCongTacTemp)
		SET @NhomLamViecID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp)
		SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp)
		
		SET @Sql = '
			SELECT TOP (' + CONVERT(NVARCHAR,@RecordCount) + ') 
				T.'+ @GroupFieldName+ ',T.ID,
				T.ThanhTienNoiBo AS ThanhTienNoiBo,
				T.ThanhTienKhuyenMai AS ThanhTienKhuyenMai,
				T.ThanhTienThucChaySauChietKhau AS ThanhTienThucChaySauChietKhau,
				T.ThanhTienThucThu AS ThanhTienThucThu
			FROM
			(
				SELECT
					T2.'+ @GroupFieldName+',' + @GroupByFildID + '
					SUM(T2.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
					SUM(T2.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
					SUM(T2.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
					SUM(T2.ThanhTienThucChayThucThu) AS ThanhTienThucThu,
					ROW_NUMBER() OVER (ORDER BY SUM(T2.ThanhTienThucChayThucThu) DESC) AS num
				FROM
				('
						+ dbo.ThucChay_GenSQLCommandForSyntheticQuery(@StartDate,
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
																		@ChucDanhID
																		) +
				')T2
				GROUP BY T2.'+ @GroupFieldName+',T2.' + @GroupByFild + '
			) AS T
			WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount) + '
			ORDER BY T.ThanhTienThucThu DESC'
	    
		PRINT @Sql;
		EXEC (@Sql);
	END
	ELSE
    BEGIN			
		DECLARE @TableResult TABLE
		(
			GroupFileName nvarchar(50),
			GroupFileID nvarchar(50),
			ThanhTienNoiBo float,
			ThanhTienKhuyenMai float,
			ThanhTienThucChaySauChietKhau float,
			ThanhTienThucThu float,
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
	   			
	   			SET @Sql = ''
	   			
	   			SET @Sql = '
	   				SELECT
						T2.'+ @GroupFieldName+',' + @GroupByFildID + '
						SUM(T2.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
						SUM(T2.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
						SUM(T2.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
						SUM(T2.ThanhTienThucChayThucThu) AS ThanhTienThucThu,
						ROW_NUMBER() OVER (ORDER BY SUM(T2.ThanhTienThucChayThucThu) DESC) AS num
					FROM
					('
							+ dbo.ThucChay_GenSQLCommandForSyntheticQuery(@TuNgay,
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
																			@ChucDanhID
																			) +
					')T2
					GROUP BY T2.'+ @GroupFieldName+',T2.' + @GroupByFild + '
	   				'
	   			PRINT @Sql
	   			INSERT INTO @TableResult(GroupFileName, 
	   									GroupFileID,
	   									ThanhTienNoiBo,
	   									ThanhTienKhuyenMai,
	   									ThanhTienThucChaySauChietKhau,
	   									ThanhTienThucThu,
	   									RowNumber)
	   			EXEC (@Sql)
	   						
				FETCH NEXT FROM Data INTO @CurrentID;		  
		   END;	   
		CLOSE Data;
		DEALLOCATE Data;

		SELECT 
			T.GroupFileName,T.GroupFileID,
			T.ThanhTienNoiBo,
			T.ThanhTienKhuyenMai,
			T.ThanhTienThucChaySauChietKhau,
			T.ThanhTienThucThu
		FROM
		(
			SELECT 
				GroupFileName, GroupFileID,
				SUM(T1.ThanhTienNoiBo) AS ThanhTienNoiBo,
				SUM(T1.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
				SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu,
				ROW_NUMBER() OVER (ORDER BY GroupFileName) AS num
			FROM @TableResult T1 
			GROUP BY GroupFileName,GroupFileID
		)T
		WHERE num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
		ORDER BY T.ThanhTienThucThu DESC
		
		PRINT @Sql;
		--EXEC (@SqlResult);
    END
END
```
