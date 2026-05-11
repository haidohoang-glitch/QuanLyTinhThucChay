# Stored Procedure: `ThucChay_GetSumFilterCondition_Test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-17 15:38:13.923000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.583000

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
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

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

CREATE PROCEDURE [dbo].[ThucChay_GetSumFilterCondition_Test] 
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
	@TenDangNhap nvarchar(50),
	@DmHinhThucQuangCaoList NVARCHAR(200)
	,@DmBannerREFList NVARCHAR(200)		
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
	
	IF OBJECT_ID('tempdb..#TempTable') IS NOT NULL
		BEGIN
			DROP TABLE #TempTable
		END

	CREATE TABLE #TempTable
		(
			GroupFieldName nvarchar(50),
			GroupFieldID nvarchar(50),
			DonViTinh nvarchar(50),
			SoHopDong NVARCHAR(50),
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
			ThanhTienThucThu float
		)

	SET @PhongID = 0;
	SET @BoPhanID = 0;
	SET @NhomLamViecID = 0;
	SET @ChucDanhID = 0;

	SET @Sql = '		
		SELECT 
			T1.'+ @GroupFieldName+','+@GroupByFildID+'
			T1.DonViTinh,SoHopDong AS SHD,
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
			SUM(T1.ThanhTienThucChayThucThu) AS ThanhTienThucThu
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
												@ChucDanhID,
												@DmHinhThucQuangCaoList,
												@DmBannerREFList) +
		')T1	
	'

	IF (@GroupFieldName = 'SoHopDong')
		SET @Sql += '
		WHERE T1.DangSuDung NOT IN (5001,5002,5003)
		'
	SET @Sql += '
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF
	'

	PRINT @Sql;
	
	INSERT INTO #TempTable
	EXEC (@Sql);

	DECLARE @SqlAdmarket NVARCHAR(MAX),
			@SqlAdmarketSecurityString NVARCHAR(MAX),
			@SqlAdmarketFilterString NVARCHAR(MAX);
				
		SET @SqlAdmarketSecurityString = '(';
		
		SET @SqlAdmarketSecurityString += dbo.GetSecurityDataByTenDangNhap(@StartDate,
																	@EndDate,
																	@TenDangNhap,
																	'NgayThucHien',
																	'TenDangNhap');

		SET @SqlAdmarketSecurityString += ' OR (' + dbo.GetSecurityWebsiteProductAdmarket(@StartDate,
																					@EndDate,@TenDangNhap,
																					'NgayThucHien',
																					'TenDangNhap',
																					'DmSanPhamREF',
																					'DmWebsiteREF') + 
										')';

		SET @SqlAdmarketSecurityString += ')';

		-- Dieu kien tim kiem theo gia tri truyen vao 
		SET @SqlAdmarketFilterString = '';
		SET @SqlAdmarketFilterString += dbo.ThucChayAdmarket_GetCommandFilterString(@GroupFieldName,
																					@DmSanPhamREFList,
																					@DmWebsiteREFList,
																					@SoHopDongList,
																					@DmPhongBanREFList, 
																					@DmBoPhanREFList, 
																					@DmNhomLamViecREFList, 
																					@TenNhanVienList);
	
	IF @GroupFieldName = 'TenNhanVien'
	BEGIN
		
		SET @SqlAdmarket = '
			SELECT
				T.TenDangNhap,
				T.TenNhanVien,
				' + @DauNhay + 'Click' + @DauNhay + ' AS DonViTinh, 
				SUM(T.TongClick) AS TongClick,
				SUM(T.TongTienKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(T.TongTienThucChay) AS ThanhTienThucThu
			FROM 
			(' 
				+ dbo.ThucChayAdmarket_GenCommandForReportBySale(@SqlAdmarketSecurityString, @SqlAdmarketFilterString) + 
			'
			)T
			GROUP BY T.TenDangNhap,T.TenNhanVien
			'
		
		PRINT @SqlAdmarket;
		
		INSERT INTO #TempTable( GroupFieldID, 
								GroupFieldName,
								DonViTinh, 
								SoLuongThucChayThucThu, 
								ThanhTienKhuyenMai, 
								ThanhTienThucThu)
		
		EXEC(@SqlAdmarket);
	END
	ELSE IF @GroupFieldName = 'SoHopDong'
	BEGIN
		SET @SqlAdmarket = '
			SELECT
				SoHopDong AS ID,
				SoHopDong,
				DonViTinh, 
				SUM(TongClick) AS TongClick,
				SUM(TongTienKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(TongTienThucChay) AS ThanhTienThucThu
			FROM 
			(' 
				+ dbo.ThucChayAdmarket_GenCommandForReportByContract(@SqlAdmarketSecurityString, @SqlAdmarketFilterString) + 
			'
			)T
			GROUP BY T.ID,T.SoHopDong,T.DonViTinh
			'
				
		INSERT INTO #TempTable( GroupFieldID, 
								GroupFieldName,
								DonViTinh, 
								SoLuongThucChayThucThu, 
								ThanhTienKhuyenMai, 
								ThanhTienThucThu)
		
		EXEC(@SqlAdmarket);
		PRINT @SqlAdmarket;
				
	END
	
	IF(@GroupFieldName = 'SoHopDong')	
		SELECT 
			T.GroupFieldID AS ID,
			T.GroupFieldID, T.GroupFieldName,
			T.DonViTinh,  
			T.GiaTriThayDoi AS GTTD,
			T.GiaTriThayDoi AS GiaTriThayDoi,
			(T.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo, 
			(T.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai, 
			(T.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
			(T.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo, 
			(T.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai, 
			(T.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
			(T.ThanhTienNoiBo) AS ThanhTienNoiBo, 
			(T.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai, 
			(T.ThanhTienThucThu) AS ThanhTienThucThu
			--,num AS ItemIndex
		FROM
		(
			SELECT 			 
				 T1.GroupFieldID, T1.GroupFieldName,
				 T1.DonViTinh, 
				 SUM(T1.GiaTriThayDoi) AS GiaTriThayDoi,
				 SUM(T1.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
				 SUM(T1.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
				 SUM(T1.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
				 SUM(T1.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo,
				 SUM(T1.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
				 SUM(T1.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
				 SUM(T1.ThanhTienNoiBo) AS ThanhTienNoiBo,
				 SUM(T1.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
				 SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu,
				 ROW_NUMBER() OVER (ORDER BY MAX(T1.NgayKyHopDong) DESC) AS num
			FROM #TempTable T1
			GROUP BY T1.GroupFieldID, T1.GroupFieldName, T1.DonViTinh
		)T
		WHERE T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount;
	ELSE
			SELECT 
			T.GroupFieldID AS ID,
			T.GroupFieldID, T.GroupFieldName,
			T.DonViTinh,  
			T.GiaTriThayDoi AS GTTD,
			T.GiaTriThayDoi AS GiaTriThayDoi,
			(T.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo, 
			(T.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai, 
			(T.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
			(T.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo, 
			(T.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai, 
			(T.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
			(T.ThanhTienNoiBo) AS ThanhTienNoiBo, 
			(T.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai, 
			(T.ThanhTienThucThu) AS ThanhTienThucThu
			--,num AS ItemIndex
		FROM
		(
			SELECT 			 
				 T1.GroupFieldID, T1.GroupFieldName,
				 T1.DonViTinh, 
				 SUM(T1.GiaTriThayDoi) AS GiaTriThayDoi,
				 SUM(T1.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
				 SUM(T1.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
				 SUM(T1.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
				 SUM(T1.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo,
				 SUM(T1.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
				 SUM(T1.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
				 SUM(T1.ThanhTienNoiBo) AS ThanhTienNoiBo,
				 SUM(T1.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
				 SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu,
				 ROW_NUMBER() OVER (ORDER BY (T1.GroupFieldName) ASC) AS num
			FROM #TempTable T1
			GROUP BY T1.GroupFieldID, T1.GroupFieldName, T1.DonViTinh
		)T
		WHERE T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount;
END

```
