# Stored Procedure: `rptThucChay_GetTotalSumBaoCaoChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:52.760000
- **Ngày sửa cuối**: 2015-03-27 17:43:52.760000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Type` | `nvarchar(4)` | No |
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
-- Description:	<Description,,>
-- =============================================

--EXEC [rptThucChay_GetTotalSumBaoCaoChiTiet] '01','TenSanPham','2013-01-01','2013-01-31','','','','','','','','Phuongvtt','','','',-1,0,0,0,'','',''
CREATE PROCEDURE [dbo].[rptThucChay_GetTotalSumBaoCaoChiTiet]
	-- Add the parameters for the stored procedure here
	@Type                   NVARCHAR(2),
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
	@ListWebsiteSecurity    NVARCHAR(512), -- anh nhat chuyen vao
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
	SET @Pamrams = N'
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
	ELSE IF UPPER(@GroupFieldName) = 'TENKHACHHANG'
	Begin
		SET @GroupByFild = 'DmKhachHangREF'
		SET @GroupByFildID = 'DmKhachHang AS ID,' 
	END
	ELSE IF UPPER(@GroupFieldName) = 'TENNHANHANG'
	Begin
		SET @GroupByFild = 'DmNhanHangREF'
		SET @GroupByFildID = 'DmNhanHangREF AS ID,' 
	END
	DECLARE @TableCondition TABLE (
				STT INT,
				sTableName NVARCHAR(50),
				sWhere NVARCHAR(500)
				)
	DECLARE @TempTable TABLE 
	(
			GroupFieldName					nvarchar(50),
			GroupFieldID					nvarchar(50),
			TenDonViTinh					nvarchar(50),
			SoLuongHopDongNoiBo				float,
			SoLuongHopDongKhuyenMai			float,
			SoLuongHopDongThucThu			float,
			ThanhTienThucThu				FLOAT,
			ThanhTienNoiBoThucThu			FLOAT,
			ThanhTienKhuyenMaiThucThu		FLOAT,
			GiaTriThayDoiTC					FLOAT,
			GiaTriThayDoiNB					FLOAT,
			GiaTriThayDoiKM				    FLOAT,
			SoLuongPhatSinhTrongKy				BIGINT,
			SoLuongKhuyenMaiPhatSinhTrongKy     BIGINT,
			SoLuongNoiBoPhatSinhTrongKy         BIGINT,
			SoLuongThayDoiTrongKy				BIGINT,
			SoLuongKhuyenMaiThayDoiTrongKy      BIGINT,
			SoLuongNoiBoThayDoiTrongKy          BIGINT
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
    SET @sGroupBy = 'GROUP BY '+@GroupFieldName+','+@GroupByFild+' , TenDonViTinh'
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
    	 TenDonViTinh,
    	 0 as SoLuongHopDongNoiBo,
    	 0 as SoLuongHopDongKhuyenMai,
    	 0 as SoLuongHopDongThucThu,
    	 SUM(ThucChayPhatSinhTrongKy),
    	 SUM(NoiBoPhatSinhTrongKy),
    	 SUM(KhuyenMaiPhatSinhTrongKy),
    	 SUM(ThucChayThayDoiTrongKy) ,
    	 SUM(NoiBoThayDoiTrongKy),
    	 SUM(KhuyenMaiThayDoiTrongKy),
    	 SUM(SoLuongPhatSinhTrongKy),
    	 SUM(SoLuongKhuyenMaiPhatSinhTrongKy),
    	 SUM(SoLuongNoiBoPhatSinhTrongKy),
    	 SUM(SoLuongThayDoiTrongKy),
    	 SUM(SoLuongKhuyenMaiThayDoiTrongKy),
    	 SUM(SoLuongKhuyenMaiThayDoiTrongKy)
    	 FROM '+@sTableName+' WHERE  '
    	 --PRINT (@Sql)
    	 SET @sWhereChay = (SELECT [dbo].[fn_rptThucChay_GetStringWhereByFilterString](@sWhere, @DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,
															 @PhongBanREFList,@BoPhanREFList,@NhomREFList,@TenNhanVienList,
															 @DmHinhThucQuangCaoList,@DmBannerREFList,@DonViTinhList,@sWhereSecurity)
    	 )
    	 SET @Sql = @Sql + @sWhereChay  + @sGroupBy
    	 PRINT (@Sql)
	     INSERT INTO @TempTable 
	    EXECUTE sys.sp_executesql @Sql, @Pamrams, 
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
			,@IsPheDuyet					INT				= 0
			,@PheDuyetAt					DATETIME
			,@PheDuyetBy					NVARCHAR(50)
			
	SET @TenBaoCao = N'Báo cáo Thực chạy chi tiết theo ' + @GroupFieldName;	
	
	-- Lay So luong theo don vi tinh Click
	SELECT @TongClickThucChayNoiBo		= SUM(A.SoLuongNoiBoPhatSinhTrongKy),
			@TongClickThucChayKhuyenMai = SUM(A.SoLuongKhuyenMaiPhatSinhTrongKy),
			@TongClickThucChay			= SUM(A.SoLuongPhatSinhTrongKy)
	FROM @TempTable A
	WHERE A.TenDonViTinh = 'CLICK';
	
	-- Lay So luong, Thanh tien theo don vi tinh View
	SELECT  @TongViewThucChayNoiBo		= SUM(A.SoLuongNoiBoPhatSinhTrongKy),
			@TongViewThucChayKhuyenMai  = SUM(A.SoLuongKhuyenMaiPhatSinhTrongKy),
			@TongViewThucChay			= SUM(A.SoLuongPhatSinhTrongKy)
	FROM @TempTable A
	WHERE A.TenDonViTinh = N'VIEW';
	
	-- Lay So luong theo don vi tinh Ngay
	SELECT  @TongSoNgayChayNoiBo		= SUM(A.SoLuongNoiBoPhatSinhTrongKy),
			@TongSoNgayChayKhuyenMai = SUM(A.SoLuongKhuyenMaiPhatSinhTrongKy),
			@TongSoNgayChay			= SUM(A.SoLuongPhatSinhTrongKy)
	FROM @TempTable A
	WHERE A.TenDonViTinh = N'NGÀY';
	
	-- Lay So luong theo don vi tinh Bài
	SELECT  @TongSoBaiVietNoiBo		= SUM(A.SoLuongNoiBoPhatSinhTrongKy),
			@TongSoBaiVietKhuyenMai =SUM(A.SoLuongKhuyenMaiPhatSinhTrongKy),
			@TongSoBaiViet			= SUM(A.SoLuongPhatSinhTrongKy)
	FROM @TempTable A
	WHERE A.TenDonViTinh = N'BÀI';
	
	-- Lay Thanh tien thuc chay
	SELECT  
			@TongTienNoiBo				= SUM(A.ThanhTienNoiBoThucThu -A.GiaTriThayDoiNB),
			@TongTienKhuyemMai			= SUM(A.ThanhTienKhuyenMaiThucThu - A.GiaTriThayDoiKM),
			@TongTienThucChaySauCK		= SUM(A.ThanhTienThucThu - A.GiaTriThayDoiTC),
			@TongGiaTriThayDoi			= SUM(A.GiaTriThayDoiTC)
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
		,@PhongBanREFList
		,@BoPhanREFList
		,@NhomREFList
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
		
	-- En Insert action log
    SELECT 
			T1.TenDonViTinh, 
			SUM(T1.GiaTriThayDoiTC) AS GiaTriThayDoi,
			SUM(T1.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
			SUM(T1.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
			SUM(T1.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
			--SUM(T1.SoLuongNoiBoPhatSinhTrongKy - T1.SoLuongThayDoiTrongKy) AS SoLuongThucChayNoiBo,
			--SUM(T1.SoLuongKhuyenMaiPhatSinhTrongKy - T1.SoLuongKhuyenMaiThayDoiTrongKy) AS SoLuongThucChayKhuyenMai,
			--SUM(T1.SoLuongPhatSinhTrongKy - T1.SoLuongNoiBoThayDoiTrongKy) AS SoLuongThucChayThucThu,
			SUM(T1.SoLuongNoiBoPhatSinhTrongKy ) AS SoLuongThucChayNoiBo,
			SUM(T1.SoLuongKhuyenMaiPhatSinhTrongKy ) AS SoLuongThucChayKhuyenMai,
			SUM(T1.SoLuongPhatSinhTrongKy ) AS SoLuongThucChayThucThu,
			SUM(T1.ThanhTienNoiBoThucThu - T1.GiaTriThayDoiNB) AS ThanhTienNoiBo,
			SUM(T1.ThanhTienKhuyenMaiThucThu - T1.GiaTriThayDoiKM) AS ThanhTienKhuyenMai,
			SUM(T1.ThanhTienThucThu - T1.GiaTriThayDoiTC) AS ThanhTienThucThu,
			SUM(T1.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
			SUM(T1.GiaTriThayDoiTC) AS GiaTriThayDoiTC,
			SUM(T1.ThanhTienNoiBoThucThu ) AS ThanhTienThucThuNB,
			SUM(T1.ThanhTienThucThu ) AS ThanhTienThucThuTC,
			ROW_NUMBER() OVER (ORDER BY SUM(T1.ThanhTienThucThu) DESC) AS num
	FROM @TempTable T1
	GROUP BY T1.TenDonViTinh
	ORDER BY T1.TenDonViTinh
END

```
