# Stored Procedure: `ThucChay_DuLieuChuaDuyetFilterCondition_TotalValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:12.350000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.407000

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
| `@IsPheDuyet` | `int(4)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-11-05
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_DuLieuChuaDuyetFilterCondition_TotalValue] 
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
	
	DECLARE @TempTable AS TABLE (
			DonViTinh NVARCHAR(50),
			SoLuongThucChayKhuyenMai BIGINT,
			SoLuongThucChayThucThu BIGINT,
			ThanhTienThucThu FLOAT
	)
	
	SET @Sql = '
		SELECT
			T1.DonViTinh,
			ROUND(SUM(T1.SoLuongThucChayKhuyenMai),0) SoLuongThucChayKhuyenMai,
			ROUND((SUM(T1.SoLuongThucChayThucThu) + SUM(SoLuongThucChayNoiBo)),0) SoLuongThucChayThucThu,
			ROUND((SUM(T1.ThanhTienThucChayNoiBo) + SUM(T1.ThanhTienThucChayThucThu)),0) AS ThanhTienThucThu
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
		SET @FilterStringAdmarket += ' AND 1 <> 1'
	
	IF @IsPheDuyet <> -1
		SET @FilterStringAdmarket += ' AND IsPheDuyet = ' + CONVERT(NVARCHAR(10),@IsPheDuyet)
		
	IF (@DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1')
		SET @FilterStringAdmarket += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')' 
	
	SET @SqlAdmarket = '
		SELECT ' +
			@DauNhay + 'click'  + @DauNhay + ' as DonViTinh,
			0 as SoLuongThucChayKhuyenMai,
			CAST(SUM(ttClick) AS BIGINT) SoLuongThucChayThucThu,
			SUM(ttClick * Price/1.1) ThanhTienThucThu
		FROM ThucChayAdmarketPublisher
		WHERE 1=1 ' + @FilterStringAdmarket + '
		GROUP BY DmSanPhamREF,TenSanPham
		'
		
	PRINT @SqlAdmarket
	
	INSERT INTO @TempTable
	EXEC(@SqlAdmarket);
	
	-- Cho Log action nguoi dung
	DECLARE @LogTime						DATETIME
			,@TenBaoCao						NVARCHAR(512)
			,@KhachHangREF					NVARCHAR(512)  = ''
			,@NhanHang						NVARCHAR(4000) = ''
			,@DmNhomNganhREF				NVARCHAR(2000) = ''
			,@TongViewThucChayNoiBo			BIGINT
			,@TongClickThucChayNoiBo		BIGINT
			,@TongSoBaiVietNoiBo			BIGINT
			,@TongSoNgayChayNoiBo			BIGINT
			,@TongViewThucChayKhuyenMai		BIGINT
			,@TongClickThucChayKhuyenMai	BIGINT
			,@TongSoBaiVietKhuyenMai		BIGINT
			,@TongSoNgayChayKhuyenMai		BIGINT
			,@TongViewThucChay				BIGINT
			,@TongClickThucChay				BIGINT
			,@TongSoBaiViet					BIGINT
			,@TongSoNgayChay				BIGINT
			,@TongTienKhuyemMai				FLOAT
			,@TongTienNoiBo					FLOAT
			,@TongTienThucChaySauCK			FLOAT
			,@TongGiaTriThayDoi				FLOAT
			,@PheDuyetAt					DATETIME
			,@PheDuyetBy					NVARCHAR(50)
			
	SET @TenBaoCao = N'Dữ liệu chưa duyệt theo sản phẩm';
		
	-- Lay So luong theo don vi tinh Click
	SELECT  @TongClickThucChayNoiBo		= 0,
			@TongClickThucChayKhuyenMai = SUM(A.SoLuongThucChayKhuyenMai),
			@TongClickThucChay			= SUM(A.SoLuongThucChayThucThu)
	FROM @TempTable A
	WHERE A.DonViTinh = N'CLICK'
	
	SELECT 		
			@TongViewThucChayNoiBo		= 0,
			@TongViewThucChayKhuyenMai  = SUM(A.SoLuongThucChayKhuyenMai),
			@TongViewThucChay			= SUM(A.SoLuongThucChayThucThu)
	FROM @TempTable A
	WHERE A.DonViTinh = N'VIEW'
	
	SELECT		
			@TongSoNgayChayNoiBo		= 0,
			@TongSoNgayChayKhuyenMai	= SUM(A.SoLuongThucChayKhuyenMai),
			@TongSoNgayChay				= SUM(A.SoLuongThucChayThucThu)
	FROM @TempTable A
	WHERE A.DonViTinh = N'NGÀY'
	
	SELECT		
			@TongSoBaiVietNoiBo		= 0,
			@TongSoBaiVietKhuyenMai = SUM(A.SoLuongThucChayKhuyenMai),
			@TongSoBaiViet			= SUM(A.SoLuongThucChayThucThu)
	FROM @TempTable A
	WHERE A.DonViTinh = N'BÀI';
	
	-- Lay Thanh tien thuc chay
	SELECT  
			@TongTienNoiBo				= 0,
			@TongTienKhuyemMai			= 0,
			@TongTienThucChaySauCK		= SUM(A.ThanhTienThucThu),
			@TongGiaTriThayDoi			= 0
	FROM @TempTable A;
	
	SET @LogTime = GETDATE();
	
	-- Insert action log
	EXEC dbo.LogUserActionFromThucChay_InsertActionLog
		@TenDangNhap
		,@LogTime
		,@TenBaoCao
		,@StartDate
		,@EndDate
		,@SoHopDongList
		,@DmPhongBanREFList
		,@DmBoPhanREFList
		,@DmNhomLamViecREFList
		,@TenNhanVienList
		,@KhachHangREF
		,@NhanHang
		,@DmNhomNganhREF
		,@DmHinhThucQuangCaoList
		,@DmSanPhamREFList
		,@DmBannerREFList
		,@DmWebsiteREFList
		,@TongViewThucChayNoiBo
		,@TongClickThucChayNoiBo
		,@TongSoBaiVietNoiBo
		,@TongSoNgayChayNoiBo
		,@TongViewThucChayKhuyenMai
		,@TongClickThucChayKhuyenMai
		,@TongSoBaiVietKhuyenMai
		,@TongSoNgayChayKhuyenMai
		,@TongViewThucChay
		,@TongClickThucChay
		,@TongSoBaiViet
		,@TongSoNgayChay
		,@TongTienKhuyemMai
		,@TongTienNoiBo
		,@TongTienThucChaySauCK
		,@TongGiaTriThayDoi
		,@IsPheDuyet
		,@PheDuyetAt
		,@PheDuyetBy
	
	SELECT 
		LOWER(T.DonViTinh) AS DonViTinh,
		SUM(T.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
		SUM(T.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
		SUM(T.ThanhTienThucThu) AS ThanhTienThucThu
	FROM @TempTable T
	GROUP BY T.DonViTinh
		
END

```
