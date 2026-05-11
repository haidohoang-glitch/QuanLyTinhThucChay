# Stored Procedure: `ThucChay_DuLieuChuaDuyetFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:08.607000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.423000

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
| `@IsPheDuyet` | `int(4)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-10-16
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_DuLieuChuaDuyetFilterCondition] 
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
	@IsPheDuyet INT,
	@IsNoiBo INT,
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList NVARCHAR(200)
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
	
	--SET @SqlCommand = dbo.Fn_GetQuaTrinhCongTacByNhanVien(@TenDangNhap,@StartDate,@EndDate)
	----PRINT @SqlCommand
	
	--INSERT INTO @QuaTrinhCongTacTemp(NhanSuID, PhongBanREF, BoPhanREF, NhomLamViecREF, ChucDanhREF, TuNgay, DenNgay)
	--EXEC (@SqlCommand)

	SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp)
	
	SET @PhongID = (SELECT PhongBanREF FROM @QuaTrinhCongTacTemp)
		SET @BoPhanID = (SELECT BoPhanREF FROM @QuaTrinhCongTacTemp)
		SET @NhomLamViecID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp)
		SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp)										
			
	DECLARE @TempTable AS TABLE (
			GroupFieldName NVARCHAR(50),
			GroupFieldID NVARCHAR(50),
			DonViTinh NVARCHAR(50),
			SoLuongThucChayKhuyenMai BIGINT,
			SoLuongThucChayThucThu BIGINT,
			ThanhTienThucThu FLOAT
	)	
	
	SET @Sql = '
		SELECT
			T1.'+ @GroupFieldName+','+@GroupByFildID+'T1.DonViTinh,					
			SUM(T1.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
			(SUM(T1.SoLuongThucChayThucThu) + SUM(SoLuongThucChayNoiBo)) SoLuongThucChayThucThu,
			(SUM(T1.ThanhTienThucChayNoiBo) + SUM(T1.ThanhTienThucChayThucThu)) AS ThanhTienThucThu
		FROM
		('
			+ dbo.ThucChay_GenSQLCommandForDataDuyetDuLieuQuery(@StartDate,
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
												@IsPheDuyet,
												@IsNoiBo,
												@DmHinhThucQuangCaoList,
												@DmBannerREFList) +
		')T1
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh
	'		
	
	PRINT @Sql
	
	INSERT INTO @TempTable
	EXEC(@Sql);
	
	DECLARE @SqlAdmarket NVARCHAR(MAX), @FilterStringAdmarket NVARCHAR(MAX)
	
	SET @FilterStringAdmarket = ' AND DmWebsiteREF in (134,182,56,137,254,85)'
	SET @FilterStringAdmarket += ' AND CONVERT(DATE,NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
	IF @DmWebsiteREFList <> ''
		SET @FilterStringAdmarket += ' AND DmWebsiteREF IN (' + @DmWebsiteREFList + ')'
		
	IF @DmSanPhamREFList <> ''
		SET @FilterStringAdmarket += ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')'
		
	IF @SoHopDongList <> ''
		SET @FilterStringAdmarket += ' AND 1 <> 1 '
		
	IF @IsPheDuyet <> -1
		SET @FilterStringAdmarket += ' AND IsPheDuyet = ' + CONVERT(NVARCHAR(10),@IsPheDuyet)
	
	IF (@DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1')
		SET @FilterStringAdmarket += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')' 
	
	SET @SqlAdmarket = '
		SELECT 
			TenSanPham, 
			DmSanPhamREF, ' + 
			@DauNhay + 'click'  + @DauNhay + ' as DonViTinh,
			0 as SoLuongThucChayKhuyenMai,
			SUM(ttClick) SoLuongThucChayThucThu,
			SUM(ttClick * Price/1.1) ThanhTienThucThu
		FROM ThucChayAdmarketPublisher
		WHERE 1=1 ' + @FilterStringAdmarket + '
		GROUP BY DmSanPhamREF,TenSanPham
		'
		
	PRINT @SqlAdmarket
	
	INSERT INTO @TempTable
	EXEC(@SqlAdmarket);
	
	SELECT 
		T1.TenSanPham, T1.ID, T1.DonViTinh,
		T1.SoLuongThucChayKhuyenMai,
		T1.SoLuongThucChayThucThu,
		T1.ThanhTienThucThu,
		T1.STT
	FROM
	(
	SELECT 
		T.GroupFieldName AS TenSanPham, T.GroupFieldID AS ID,
		LOWER(T.DonViTinh) AS DonViTinh,
		dbo.FormatNumber(T.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
		dbo.FormatNumber(T.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
		dbo.FormatNumber(T.ThanhTienThucThu) AS ThanhTienThucThu,
		ROW_NUMBER() OVER (ORDER BY T.GroupFieldName) AS STT
	FROM @TempTable T
	)T1	
	WHERE 	
		T1.STT BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount														
    
    
END

```
