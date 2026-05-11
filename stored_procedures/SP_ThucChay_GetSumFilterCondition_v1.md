# Stored Procedure: `ThucChay_GetSumFilterCondition_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-02-25 11:27:28.550000
- **Ngày sửa cuối**: 2014-10-14 10:39:54.177000

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
-- Modified date: 2013-09-02
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_GetSumFilterCondition_v1] 
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
	DECLARE @SqlCommand VARCHAR(MAX);
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
	
	DECLARE @OrderByField NVARCHAR(50)
	DECLARE @Function NVARCHAR(50)
	DECLARE @SortColum nvarchar(50)
	
	IF UPPER(@GroupFieldName) = 'SOHOPDONG'
	BEGIN
		SET @OrderByField = 'NgayKyHopDong'
		SET @Function = 'MAX'
	END
	ELSE
	BEGIN
		SET @OrderByField = 'ThanhTienThucThu'
		SET @Function = 'SUM'
	END
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName   
					
    IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild = 'DmSanPhamREF'
		SET @GroupByFildID = 'DmSanPhamREF AS ID,' 
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

	-- Check neu co quyen xem full du lieu
	IF (@GroupPermission = -1)
	BEGIN
		PRINT 'Full quyen';

		SET @PhongID = 0;
		SET @BoPhanID = 0;
		SET @NhomLamViecID = 0;
		SET @ChucDanhID = 0;

		SET @Sql = '
			SELECT TOP (' + CONVERT(NVARCHAR,@RecordCount) + ') 
				T.'+ @GroupFieldName+' AS GroupFieldName,T.ID,T.DonViTinh,
				T.GiaTriThayDoi,
				T.SoLuongHopDongNoiBo,
				T.SoLuongHopDongKhuyenMai,
				T.SoLuongHopDongThucThu,
				T.SoLuongThucChayNoiBo,
				T.SoLuongThucChayKhuyenMai,
				T.SoLuongThucChayThucThu,
				T.ThanhTienNoiBo AS ThanhTienNoiBo,
				T.ThanhTienKhuyenMai AS ThanhTienKhuyenMai,
				T.ThanhTienThucChaySauChietKhau AS ThanhTienThucChaySauChietKhau,
				T.ThanhTienThucThu AS ThanhTienThucThu
			FROM
			( 
				SELECT
					T2.'+ @GroupFieldName+',T2.ID, T2.DonViTinh,
					SUM(T2.GiaTriThayDoi) GiaTriThayDoi,
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
					ROW_NUMBER() OVER (ORDER BY '+@Function +'(T2.' + @OrderByField + ')DESC) AS num
				FROM
				(
					SELECT
						T1.'+ @GroupFieldName+','+@GroupByFildID+'T1.DonViTinh,SoHopDong AS SHD,
						MAX(T1.NgayKyHopDong) AS NgayKyHopDong,
						SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
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
					GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF
				)T2
				GROUP BY T2.'+ @GroupFieldName+',T2.ID,T2.DonViTinh
			) AS T
			WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount)
	
			PRINT @Sql;
			EXEC (@Sql);
	END
	ELSE
	BEGIN
		SET @SqlCommand = dbo.Fn_GetQuaTrinhCongTacByNhanVien(@TenDangNhap,@StartDate,@EndDate)
		PRINT @SqlCommand
	
		INSERT INTO @QuaTrinhCongTacTemp(NhanSuID, PhongBanREF, BoPhanREF, NhomLamViecREF, ChucDanhREF, TuNgay, DenNgay)
		EXEC (@SqlCommand)

		SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp)
		
		PRINT 'COUNT: ' + convert(nvarchar(50),@Count);
	
		IF @Count <= 1
		BEGIN	
			SET @PhongID = (SELECT PhongBanREF FROM @QuaTrinhCongTacTemp)
			SET @BoPhanID = (SELECT BoPhanREF FROM @QuaTrinhCongTacTemp)
			SET @NhomLamViecID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp)
			SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp)										
																								
    
		SET @Sql = '
			SELECT TOP (' + CONVERT(NVARCHAR,@RecordCount) + ') 
				T.'+ @GroupFieldName+' AS GroupFieldName,T.ID,T.DonViTinh,
				T.GiaTriThayDoi,
				T.SoLuongHopDongNoiBo,
				T.SoLuongHopDongKhuyenMai,
				T.SoLuongHopDongThucThu,
				T.SoLuongThucChayNoiBo,
				T.SoLuongThucChayKhuyenMai,
				T.SoLuongThucChayThucThu,
				T.ThanhTienNoiBo AS ThanhTienNoiBo,
				T.ThanhTienKhuyenMai AS ThanhTienKhuyenMai,
				T.ThanhTienThucChaySauChietKhau AS ThanhTienThucChaySauChietKhau,
				T.ThanhTienThucThu AS ThanhTienThucThu
			FROM
			(
				SELECT
					T2.'+ @GroupFieldName+',T2.ID, T2.DonViTinh,
					SUM(T2.GiaTriThayDoi) GiaTriThayDoi,
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
					ROW_NUMBER() OVER (ORDER BY '+@Function +'(T2.' + @OrderByField + ')DESC) AS num
				FROM
				(
					SELECT
						T1.'+ @GroupFieldName+','+@GroupByFildID+'T1.DonViTinh,SoHopDong AS SHD,
						MAX(T1.NgayKyHopDong) AS NgayKyHopDong,
						SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
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
					GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF
				)T2
				GROUP BY T2.'+ @GroupFieldName+',T2.ID,T2.DonViTinh
			) AS T
			WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount)
	
			PRINT @Sql;
			EXEC (@Sql);
    
		END
		ELSE
		BEGIN
			DECLARE  @NhomID int
			
			DECLARE @TableResult TABLE
			(
				GroupFieldName nvarchar(50),
				GroupFileID nvarchar(50),
				DonViTinh nvarchar(50),
				NgayKyHopDong DATETIME,
				GiaTriThayDoi FLOAT,
				SoLuongHopDongNoiBo float,
				SoLuongHopDongKhuyenMai float,
				SoLuongHopDongThucThu float,
				SoLuongThucChayNoiBo float,
				SoLuongThucChayKhuyenMai float,
				SoLuongThucChayThucThu float,
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
							MAX(T2.NgayKyHopDong) NgayKyHopDong,
							SUM(T2.GiaTriThayDoi) GiaTriThayDoi,
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
							ROW_NUMBER() OVER (ORDER BY '+@Function +'(T2.' + @OrderByField + ')DESC) AS num
						FROM
						(
							SELECT
								T1.'+ @GroupFieldName+','+@GroupByFildID+'T1.DonViTinh,SoHopDong AS SHD,
								MAX(T1.NgayKyHopDong) NgayKyHopDong,
								SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
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
	   				INSERT INTO @TableResult(GroupFieldName, 
	   										GroupFileID,
	   										DonViTinh,
	   										NgayKyHopDong,
	   										GiaTriThayDoi,
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
		
			IF @GroupFieldName = 'SoHopDong'
				SET @SortColum = 'CONVERT(DATETIME,T.NgayKyHopDong)'
			ELSE
				SET @SortColum = 'T.ThanhTienThucThu'
		
			SELECT 
					T.GroupFieldName,T.GroupFileID AS ID,T.DonViTinh,
					T.GiaTriThayDoi,
					T.SoLuongHopDongNoiBo,T.SoLuongHopDongKhuyenMai,T.SoLuongHopDongThucThu,
					T.SoLuongThucChayNoiBo,T.SoLuongThucChayKhuyenMai,T.SoLuongThucChayThucThu,
					T.ThanhTienNoiBo,T.ThanhTienKhuyenMai,T.ThanhTienThucChaySauChietKhau,T.ThanhTienThucThu,
					T.NgayKyHopDong
				FROM
				(
					SELECT 
						GroupFieldName, GroupFileID,DonViTinh,
						MAX(CONVERT(DATETIME,T1.NgayKyHopDong)) AS NgayKyHopDong,
						SUM(T1.GiaTriThayDoi) AS GiaTriThayDoi,
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
					GROUP BY GroupFieldName,GroupFileID,DonViTinh
				)T
				WHERE num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
				ORDER BY 
				
					CASE WHEN GroupFieldName <> 'SoHopDong' THEN CONVERT(varchar(50),T.ThanhTienThucThu)
						ELSE CONVERT(varchar(30), T.NgayKyHopDong, 121)
					END DESC
		END   
	END   
END
```
