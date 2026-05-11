# Stored Procedure: `rptThucChay_GetDataBaoCaoTongHop`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:53.230000
- **Ngày sửa cuối**: 2015-03-27 17:43:53.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Type` | `nvarchar(4)` | No |
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@GroupFieldName` | `nvarchar(1024)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(1024)` | No |
| `@DmWebsiteREFList` | `nvarchar(1024)` | No |
| `@SoHopDongList` | `nvarchar(1024)` | No |
| `@PhongBanREFList` | `nvarchar(1024)` | No |
| `@BoPhanREFList` | `nvarchar(1024)` | No |
| `@NhomREFList` | `nvarchar(1024)` | No |
| `@TenNhanVienList` | `nvarchar(1024)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@DonViTinhList` | `nvarchar(1024)` | No |
| `@Security` | `int(4)` | No |
| `@PhongBanSecurity` | `int(4)` | No |
| `@BoPhanSecurity` | `int(4)` | No |
| `@NhomSecurity` | `int(4)` | No |
| `@ListSanPhamSecurity` | `nvarchar(1024)` | No |
| `@ListWebsiteSecurity` | `nvarchar(1024)` | No |
| `@ListKhachHangSecurity` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,> ''qc103','qc91829''
-- =============================================

--EXEC [rptThucChay_GetDataBaoCaoTongHop] '01',1,100,'TenSanPham','2013-01-01','2013-01-31','','','','','','','','Phuongvtt','','','',-1,0,0,0,'','',''
CREATE PROCEDURE [dbo].[rptThucChay_GetDataBaoCaoTongHop]
	-- Add the parameters for the stored procedure here
	@Type                   NVARCHAR(2),
	@PageIndex				INT,
	@RecordCount			INT,
	@GroupFieldName			NVARCHAR(512),
	@StartDate				DATETIME,
	@EndDate				DATETIME,
	@DmSanPhamREFList		NVARCHAR(512),
	@DmWebsiteREFList		NVARCHAR(512),
	@SoHopDongList			NVARCHAR(512),
	@PhongBanREFList		NVARCHAR(512),
	@BoPhanREFList			NVARCHAR(512),
	@NhomREFList			NVARCHAR(512),
	@TenNhanVienList		NVARCHAR(512),
	@TenDangNhap			NVARCHAR(50),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList		NVARCHAR(200),
	@DonViTinhList			NVARCHAR(512),
	@Security				INT,-- anh Nhat chuyen vao
	@PhongBanSecurity		INT,-- anh nhat chuyen vao
	@BoPhanSecurity			INT,-- anh nhat chuyen vao
	@NhomSecurity			INT,-- anh nhat chuyen vao
	@ListSanPhamSecurity    NVARCHAR(512), -- anh nhat chuyen vao
	@ListWebsiteSecurity    NVARCHAR(512),  -- anh nhat chuyen vao
	@ListKhachHangSecurity  NVARCHAR(512)  -- anh nhat chuyen vao
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    DECLARE @Sql				NVARCHAR(MAX)
    DECLARE @DauNhay			NVARCHAR(50)
    Declare @GroupByFildID		NVARCHAR(512)
    Declare @GroupByFild     	NVARCHAR(512)
    DECLARE @StartTableName		NVARCHAR(50)
    DECLARE @ToUserName		    NVARCHAR(50)
    DECLARE @Pamrams		NVARCHAR(MAX);
	SET @Pamrams = N'@PageIndexParam int,
					@RecordCountParam int,
					@GroupFieldNameParam nvarchar(50), 
					@StartDateParam datetime,
					@EndDateParam datetime, 
					@DmSanPhamREFListParam nvarchar(4000), 
					@DmWebsiteREFListParam nvarchar(4000), 
					@SoHopDongListParam nvarchar(4000), 
					@DmPhongBanREFListParam nvarchar(4000), 
					@DmBoPhanREFListParam nvarchar(4000), 
					@DmNhomLamViecREFListParam nvarchar(4000), 
					@TenNhanVienListParam nvarchar(4000),
					@TenDangNhapParam nvarchar(50), 
					@DmHinhThucQuangCaoListParam NVARCHAR(200), 
					@DmBannerREFListParam NVARCHAR(200), 
					@DonViTinhListParam NVARCHAR(200)'
     
 --   SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	--IF @ToUserName IS NOT NULL
	--	SET @TenDangNhap = @ToUserName
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
		SET @GroupByFild = 'PhongBanREF'
		SET @GroupByFildID = 'DmPhongBanREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENBOPHAN'
	Begin
		SET @GroupByFild = 'BoPhanREF'
		SET @GroupByFildID = 'DmBoPhanREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENNHOM' OR UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC'
	Begin
		SET @GroupFieldName = 'TenNhom'
		SET @GroupByFild = 'NhomREF'
		SET @GroupByFildID = 'NhomREF AS ID,' 
	END
	ELSE IF UPPER(@GroupFieldName) = 'SOHOPDONG'
	Begin
		SET @GroupByFild = 'SoHopDong'
		SET @GroupByFildID = 'SoHopDong AS ID,' 
	END
	ELSE IF UPPER(@GroupFieldName) = 'TENNHANVIEN'
	Begin
		SET @GroupByFild = 'UserName'
		SET @GroupByFildID = 'UserName AS ID,' 
	END
	DECLARE @TableCondition TABLE (
				STT INT,
				sTableName NVARCHAR(50),
				sWhere NVARCHAR(500)
				)
	DECLARE @TempTable TABLE 
	(
				GroupFieldName					NVARCHAR(50),
				GroupFileID						NVARCHAR(50),
				NgayThucHien				    DATETIME,
				ThanhTienThucThu				FLOAT,
				ThanhTienNoiBoThucThu			FLOAT,
				ThanhTienKhuyenMaiThucThu		FLOAT,
				GiaTriThayDoiTC					FLOAT,
				GiaTriThayDoiNB					FLOAT,
				GiaTriThayDoiKM				    FLOAT
	)
	
    
    SET @StartTableName = [dbo].[fn_rptThucChay_GetStartTableNameByFilterCondition] (@Type,@TenDangNhap,@GroupFieldName,@SoHopDongList,@DmHinhThucQuangCaoList,@DmSanPhamREFList,@DmWebsiteREFList,@DmBannerREFList,@ListWebsiteSecurity,@ListSanPhamSecurity)
    PRINT(@StartTableName)
    
    INSERT INTO @TableCondition SELECT * FROM dbo.fn_GetListWhereReport(@StartDate,@EndDate,@StartTableName)
    DECLARE @i INT SET @i =1 
    DECLARE @sTableName NVARCHAR(500)
    DECLARE @sWhere NVARCHAR(500)
    DECLARE @sWhereChay NVARCHAR(500)
    DECLARE @sWhereSecurity NVARCHAR(500)
    DECLARE @sGroupBy NVARCHAR(500)
    -- group by
    SET @sGroupBy = 'GROUP BY '+@GroupFieldName+','+@GroupByFild+''
    -- Chuc vu 
    IF @Security = -1 SET @sWhereSecurity = ' AND  1=1 '
    ELSE
    	SET @sWhereSecurity = ' AND ' + [dbo].[fn_getsWhereSecurity](@TenDangNhap,@Security,@PhongBanSecurity,@BoPhanSecurity,@NhomSecurity,@ListSanPhamSecurity,@ListWebsiteSecurity,@ListKhachHangSecurity)
     PRINT(@sGroupBy)
    WHILE @i <= (SELECT MAX(STT) FROM @TableCondition)
    BEGIN
    	 SET @sTableName = (SELECT sTableName FROM @TableCondition WHERE STT = @i)
    	 SET @sWhere = (SELECT sWhere FROM @TableCondition WHERE STT = @i)
    	 print(@sTableName)
    	 SET @Sql =''
    	 SET @Sql = 'SELECT '+@GroupFieldName+','+@GroupByFildID+'
    	 MAX(NgayThucHien) as NgayThucHien,
    	 SUM(ThucChayPhatSinhTrongKy),
    	 SUM(NoiBoPhatSinhTrongKy),
    	 SUM(KhuyenMaiPhatSinhTrongKy),
    	 SUM(ThucChayThayDoiTrongKy) ,
    	 SUM(NoiBoThayDoiTrongKy),
    	 SUM(KhuyenMaiThayDoiTrongKy) FROM '+@sTableName+' WHERE  '
    	 PRINT (@Sql)
    	 SET @sWhereChay = (SELECT [dbo].[fn_rptThucChay_GetStringWhereByFilterString](@sWhere, @DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,
															 @PhongBanREFList,@BoPhanREFList,@NhomREFList,@TenNhanVienList,
															 @DmHinhThucQuangCaoList,@DmBannerREFList,@DonViTinhList,@sWhereSecurity)
    	 )
    	 SET @Sql = @Sql + @sWhereChay  + @sGroupBy
	     INSERT INTO @TempTable 
	    EXECUTE sys.sp_executesql @Sql, @Pamrams, 
		@PageIndexParam					= @PageIndex,
		@RecordCountParam				= @RecordCount,
		@GroupFieldNameParam			= @GroupFieldName,
		@StartDateParam					= @StartDate,
		@EndDateParam					= @EndDate,
		@DmSanPhamREFListParam			= @DmSanPhamREFList,
		@DmWebsiteREFListParam			= @DmWebsiteREFList,
		@SoHopDongListParam				= @SoHopDongList,
		@DmPhongBanREFListParam			= @PhongBanREFList,
		@DmBoPhanREFListParam			= @BoPhanREFList,
		@DmNhomLamViecREFListParam		= @NhomREFList,
		@TenNhanVienListParam			= @TenNhanVienList,
		@TenDangNhapParam				= @TenDangNhap,
		@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
		@DmBannerREFListParam			= @DmBannerREFList,
		@DonViTinhListParam				= @DonViTinhList;		
		 
    	 SET @i += 1
    END
    SELECT 
		T.GroupFieldName,T.GroupFileID,
		T.GiaTriThayDoiTC + T.GiaTriThayDoiNB AS GiaTriThayDoi,
		(T.ThanhTienNoiBo - T.GiaTriThayDoiNB) as ThanhTienNoiBo,
		(T.ThanhTienKhuyenMai - T.GiaTriThayDoiKM) as ThanhTienKhuyenMai,
		T.ThanhTienThucThu + T.ThanhTienNoiBo as ThanhTienThucChaySauChietKhau,
		(T.ThanhTienThucThu - T.GiaTriThayDoiTC) AS ThanhTienThucThu,
		T.GiaTriThayDoiNB,
		T.GiaTriThayDoiTC,
		T.ThanhTienNoiBo AS ThanhTienThucThuNB,
		T.ThanhTienThucThu AS ThanhTienThucThuTC
    FROM
    (
       SELECT 
			GroupFieldName, GroupFileID,
			MAX(T1.NgayThucHien) AS NgayThucHien,				
			SUM(T1.ThanhTienThucThu) ThanhTienThucThu,
			SUM(T1.ThanhTienNoiBoThucThu) AS ThanhTienNoiBo,
			SUM(T1.ThanhTienKhuyenMaiThucThu) AS ThanhTienKhuyenMai,
			SUM(T1.GiaTriThayDoiTC) AS GiaTriThayDoiTC,
			SUM(T1.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
			SUM(T1.GiaTriThayDoiKM) AS GiaTriThayDoiKM,
			ROW_NUMBER() OVER (ORDER BY GroupFieldName) AS num
		FROM @TempTable T1 GROUP BY GroupFieldName,GroupFileID
		)T
		WHERE num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
	ORDER BY 
		T.GroupFieldName
END

```
