# Stored Procedure: `ThucChay_TableTotalPageNumber_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-02-25 11:28:21.247000
- **Ngày sửa cuối**: 2014-10-14 10:39:52.593000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
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

--exec [ThucChay_TableTotalPageNumber]
--	@GroupFieldName = N'TenSanPham',
--	@StartDate = '2013-05-28',
--	@EndDate = '2013-05-30',
--	@DmSanPhamREFList = N'',
--	@DmWebsiteREFList = N'',
--	@SoHopDongList = N'',
--	@DmPhongBanREFList = N'',
--	@DmBoPhanREFList = N'',
--	@DmNhomLamViecREFList = N'',
--	@TenNhanVienList = N''
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_TableTotalPageNumber_v1]
	-- Add the parameters for the stored procedure here
	@GroupFieldName nvarchar(50),
	@StartDate datetime,
	@EndDate datetime,
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
	Declare @Sql varchar(8000)
	Declare @DauNhay nvarchar(50)
	Declare @GroupByFildID nvarchar(50)
	Declare @GroupByFild nvarchar(50)
	Declare @FilterString nvarchar(4000)
	DECLARE @IsHaveValue NVARCHAR(4000)
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

	IF @GroupFieldName = 'TenSanPham'
		Begin
			SET @GroupByFild = 'DmSanPhamREF'
			SET @GroupByFildID = 'DmSanPhamREF AS ID,' 
		End
	ELSE IF @GroupFieldName = 'TenWebsite'
		Begin
			SET @GroupByFild = 'DmWebsiteREF'
			SET @GroupByFildID = 'DmWebsiteREF AS ID,' 
		End
	ELSE IF @GroupFieldName = 'TenPhongBan'
		Begin
			SET @GroupByFild = 'DmPhongBanREF'
			SET @GroupByFildID = 'DmPhongBanREF AS ID,' 
		End
	ELSE IF @GroupFieldName = 'TenBoPhan'
		Begin
			SET @GroupByFild = 'DmBoPhanREF'
			SET @GroupByFildID = 'DmBoPhanREF AS ID,' 
		End
	ELSE IF @GroupFieldName = 'TenNhomLamViec'
		Begin
			SET @GroupByFild = 'DmNhomLamViecREF'
			SET @GroupByFildID = 'DmNhomLamViecREF AS ID,' 
		END
	ELSE IF @GroupFieldName = 'SoHopDong'
		Begin
			SET @GroupByFild = 'SoHopDong'
			SET @GroupByFildID = 'SoHopDong AS ID,' 
		END
	ELSE IF @GroupFieldName = 'TenNhanVien'
		Begin
			SET @GroupByFild = 'TenDangNhap'
			SET @GroupByFildID = 'TenDangNhap AS ID,' 
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
		
		SET @Sql = '
			SELECT COUNT(1) AS MaxRecords 
			FROM
			(
				SELECT
					T2.'+ @GroupFieldName+',T2.ID, T2.DonViTinh,
					SUM(T2.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
					SUM(T2.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
					SUM(T2.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
					SUM(T2.SoLuongThucChayNoiBo) SoLuongThucChayNoiBo,
					SUM(T2.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
					SUM(T2.SoLuongThucChayThucThu) SoLuongThucChayThucThu,
					SUM(T2.ThanhTienNoiBo) AS ThanhTienNoiBo,
					SUM(T2.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
					SUM(T2.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
					SUM(T2.ThanhTienThucThu) AS ThanhTienThucThu,
					ROW_NUMBER() OVER (ORDER BY SUM(T2.ThanhTienThucThu) DESC) AS num
				FROM
				(
					SELECT
						T1.'+ @GroupFieldName+','+@GroupByFildID+'T1.DonViTinh,SoHopDong AS SHD,
						SUM(T1.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
						SUM(T1.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
						SUM(T1.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
						SUM(T1.SoLuongThucChayNoiBo) SoLuongThucChayNoiBo,
						SUM(T1.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
						SUM(T1.SoLuongThucChayThucThu) SoLuongThucChayThucThu,
						SUM(T1.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
						SUM(T1.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
						SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
						SUM(T1.ThanhTienThucChayThucThu) AS ThanhTienThucThu,
						ROW_NUMBER() OVER (ORDER BY T1.'+ @GroupFieldName + ') AS num
					FROM
					('
						+ dbo.ThucChay_GenSQLCommandForQuery(@StartDate,
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
					')T1
					GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF
				)T2
				GROUP BY T2.'+ @GroupFieldName+',T2.ID,T2.DonViTinh
			) AS T
			'
	    
		PRINT @Sql;
		EXEC (@Sql);
	END
	ELSE
	BEGIN
		DECLARE  @NhomID int
			
		DECLARE @TableResult TABLE
		(
			GroupFileName nvarchar(50),
			GroupFileID nvarchar(50),
			DonViTinh nvarchar(50),
			SoLuongHopDongNoiBo int,
			SoLuongHopDongKhuyenMai int,
			SoLuongHopDongThucThu int,
			SoLuongThucChayNoiBo int,
			SoLuongThucChayKhuyenMai int,
			SoLuongThucChayThucThu int,
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
	   			SET @NhomID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			SET @TuNgay = (SELECT TuNgay FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			SET @DenNgay = (SELECT DenNgay FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp WHERE NhanSuID = @CurrentID)
	   			
	   			IF @TuNgay < @StartDate
	   				SET @TuNgay = @StartDate
	   				
	   			IF @DenNgay > @EndDate
	   				SET @DenNgay = @EndDate	 
	   			
	   			SET @Sql = '
	   				SELECT
				T2.'+ @GroupFieldName+',T2.ID, T2.DonViTinh,
				SUM(T2.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
				SUM(T2.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
				SUM(T2.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
				SUM(T2.SoLuongThucChayNoiBo) SoLuongThucChayNoiBo,
				SUM(T2.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
				SUM(T2.SoLuongThucChayThucThu) SoLuongThucChayThucThu,
				SUM(T2.ThanhTienNoiBo) AS ThanhTienNoiBo,
				SUM(T2.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(T2.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
				SUM(T2.ThanhTienThucThu) AS ThanhTienThucThu,
				ROW_NUMBER() OVER (ORDER BY SUM(T2.ThanhTienThucThu) DESC) AS num
			FROM
			(
				SELECT
					T1.'+ @GroupFieldName+','+@GroupByFildID+'T1.DonViTinh,SoHopDong AS SHD,
					MAX(T1.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
					MAX(T1.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
					MAX(T1.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
					SUM(T1.SoLuongThucChayNoiBo) SoLuongThucChayNoiBo,
					SUM(T1.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
					SUM(T1.SoLuongThucChayThucThu) SoLuongThucChayThucThu,
					SUM(T1.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
					SUM(T1.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
					SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
					SUM(T1.ThanhTienThucChayThucThu) AS ThanhTienThucThu,
					ROW_NUMBER() OVER (ORDER BY T1.'+ @GroupFieldName + ') AS num
				FROM
				('
					+ dbo.ThucChay_GenSQLCommandForQuery(@TuNgay,
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
														@NhomID,
														@ChucDanhID) +
				')T1
				GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF
			)T2
			GROUP BY T2.'+ @GroupFieldName+',T2.ID,T2.DonViTinh
	   			'
	   			PRINT @Sql
	   			INSERT INTO @TableResult(GroupFileName, 
	   									GroupFileID,
	   									DonViTinh,
	   									SoLuongHopDongNoiBo,
	   									SoLuongHopDongKhuyenMai,
	   									SoLuongHopDongThucThu,
	   									SoLuongThucChayNoiBo,
	   									SoLuongThucChayKhuyenMai,
	   									SoLuongThucChayThucThu,
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
			COUNT(*) AS MaxRecords
		FROM
		(
			SELECT 
				GroupFileName, GroupFileID,DonViTinh,
				SUM(T1.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
				SUM(T1.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
				SUM(T1.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
				SUM(T1.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo,
				SUM(T1.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
				SUM(T1.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
				SUM(T1.ThanhTienNoiBo) AS ThanhTienNoiBo,
				SUM(T1.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
				SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu,
				ROW_NUMBER() OVER (ORDER BY SUM(T1.ThanhTienThucThu) DESC) AS num
			FROM @TableResult T1 
			GROUP BY GroupFileName,GroupFileID,DonViTinh
		)T
		
		
		PRINT @Sql;

    END 

END

```
