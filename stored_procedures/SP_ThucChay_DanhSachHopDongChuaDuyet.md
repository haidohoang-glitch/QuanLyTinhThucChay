# Stored Procedure: `ThucChay_DanhSachHopDongChuaDuyet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:09.050000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.033000

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
| `@DonViTinh` | `nvarchar(100)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@IsPheDuyet` | `int(4)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_DanhSachHopDongChuaDuyet] 
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
	@DonViTinh NVARCHAR(50),	
	@TenDangNhap NVARCHAR(50),
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
    
    DECLARE @Sql NVARCHAR(MAX);
    DECLARE @DauNhay NVARCHAR(50);
    Declare @GroupByFildID nvarchar(4000);
	Declare @GroupByFild nvarchar(4000);
	Declare @FilterString nvarchar(4000);
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand NVARCHAR(MAX);
	DECLARE @Count int
	DECLARE @ToUserName NVARCHAR(50)
	
	DECLARE @DuyetDuLieuTemp TABLE (
			[ThucChayDaTinhID] [nvarchar](50) NOT NULL,
			[HopDongID] [int] NULL,
			[SoHopDong] [nvarchar](50) NULL,
			[HopDongChiTietREF] [int] NULL,
			[DmSanPhamREF] [int] NULL,
			[TenSanPham] [nvarchar](255) NULL,
			[SoLuongTheoHopDong] [bigint] NULL,
			[DonViTinh] [nvarchar](50) NULL,
			[DmHinhThucQuangCao] [int] NULL,
			[DotChayHopDong] [nvarchar](2000) NULL,
			[IsPheDuyet] [int] NULL,
			[TenWebsite] [nvarchar](255) NULL,
			[DmWebsiteREF] int null,
			[DonGia] [int] NULL,
			[ChietKhau] [int] NULL,
			[ThanhTienSauChietKhau] [float] NULL,
			[SoLuongThucChayKM] [bigint] NOT NULL,
			[SoLuongThucChay] [bigint] NULL,
			[ThanhTienThucThu] [float] NULL
	)
	
	DECLARE @DotChayHopDong NVARCHAR(2000);
	
	DECLARE @Pamrams NVARCHAR(MAX);
	SET @Pamrams = N'@PageIndexParam INT,
					@RecordCountParam INT,
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
					@DonViTinhParam NVARCHAR(50),	
					@TenDangNhapParam NVARCHAR(50),
					@IsPheDuyetParam INT,
					@IsNoiBoParam INT,
					@DmHinhThucQuangCaoListParam NVARCHAR(200),
					@DmBannerREFListParam NVARCHAR(200)'
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
 --   SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	--IF @ToUserName IS NOT NULL
	--	SET @TenDangNhap = @ToUserName

	IF @IsPheDuyet <> -1
		SET @FilterString = ' AND IsPheDuyet = ' + CONVERT(nvarchar(30),@IsPheDuyet) + ' ' 
	ELSE IF @IsPheDuyet = -1 
		SET @FilterString = ''
		
	IF @IsNoiBo = 1
		SET @FilterString =  @FilterString 
	ELSE IF @IsNoiBo = 0
		SET @FilterString = @FilterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'
	
	IF @DmSanPhamREFList <> 144
	BEGIN
		
	SET @FilterString = @FilterString + ' AND DmWebsiteREF IN (134,182,56,137,254,85) AND '	
	
	SET @FilterString = @FilterString + dbo.GetThucChayFilterString(
														@StartDate ,
														@EndDate ,
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
														@DmBannerREFList 
													)
		SET @Sql = '
			SELECT
				A.ThucChayDaTinhID, A.HopDongID,
				A.SoHopDong, 0 as HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham,
				(SoLuongHopDongNoiBo+SoLuongHopDongKhuyenMai+SoLuongHopDongThucThu)AS SoLuongTheoHopDong,
				dbo.FormatText(A.DonViTinh) AS DonViTinh, 
				A.DmHinhThucQuangCao,
				A.DotChayHopDong,IsPheDuyet, A.TenWebsite,A.DmWebsiteREF, A.DonGia, A.ChietKhau,
				A.ThanhTien AS ThanhTienSauChietKhau,
				A.SoLuongThucChayKhuyenMai AS SoLuongThucChayKM,
				(SoLuongThucChayNoiBo+SoLuongThucChayThucThu) AS SoLuongThucChay,
				(ThanhTienThucChayNoiBo + ThanhTienThucThu + GiaTriThayDoi) AS ThanhTienThucThu
			FROM
			(
				SELECT
					MAX(0) AS ThucChayDaTinhID, HopDongID,
					SoHopDong,HopDongChiTietREF,DmSanPhamREF,TenSanPham,TenWebsite,DmWebsiteREF, 
					dbo.FormatDonViTinh(DonViTinh) AS DonViTinh, DmHinhThucQuangCao,
					DotChayHopDong,
					IsPheDuyet,
					CASE WHEN HopDongChiTietREF = 0 THEN
							dbo.ThucChay_GetChietKhauOfPhanBo(HopDongID,DmSanPhamREF) 
						ELSE
							ChietKhau
					END AS ChietKhau,
					DonGia,ThanhTien,
					SUM(ISNULL(GiaTriThayDoi,0)) GiaTriThayDoi,
					CASE WHEN (UPPER(SoHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongNoiBo,
					CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongKhuyenMai,
					CASE WHEN (ThanhTienKM = 0 ) THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongThucThu,
					CASE WHEN (UPPER(SoHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongThucChayNoiBo,
					ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
					CASE WHEN (UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongThucChayThucThu,
					CASE WHEN (UPPER(SoHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
						ELSE 0
					END AS ThanhTienThucChayNoiBo,
					ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
					ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
					CASE WHEN (UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
						ELSE 0
					END AS ThanhTienThucThu
				FROM ThucChayDaTinh
				WHERE TrangThaiHopDong <> 3 ' + @FilterString + '
				GROUP BY DmSanPhamREF,TenSanPham,HopDongID,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),DmHinhThucQuangCao,SoHopDong,ThanhTienKM,
					DotChayHopDong,ChietKhau,DonGia,TenWebsite,DmWebsiteREF,ThanhTien,HopDongID,IsPheDuyet
			)A
			WHERE  (SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
							OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChayNoiBo <> 0 OR GiaTriThayDoi <> 0)
					AND (ThanhTienThucChayNoiBo + ThanhTienThucThu + GiaTriThayDoi) > 1000
			ORDER BY A.SoHopDong, A.DmWebsiteREF 
		'
		
		PRINT @Sql
													
		INSERT INTO @DuyetDuLieuTemp (
							[ThucChayDaTinhID],
							[HopDongID],
							[SoHopDong],
							[HopDongChiTietREF],
							[DmSanPhamREF],
							[TenSanPham],
							[SoLuongTheoHopDong],
							[DonViTinh],
							[DmHinhThucQuangCao],
							[DotChayHopDong],
							[IsPheDuyet],
							[TenWebsite],
							[DmWebsiteREF],
							[DonGia],
							[ChietKhau],
							[ThanhTienSauChietKhau],
							[SoLuongThucChayKM],
							[SoLuongThucChay],
							[ThanhTienThucThu]
		)
		--EXEC(@Sql);
		EXECUTE sp_executesql @Sql, @Pamrams, 
								@PageIndexParam					= @PageIndex,
								@RecordCountParam				= @RecordCount,
								@GroupFieldNameParam			= @GroupFieldName,
								@StartDateParam					= @StartDate,
								@EndDateParam					= @EndDate,
								@DmSanPhamREFListParam			= @DmSanPhamREFList,
								@DmWebsiteREFListParam			= @DmWebsiteREFList,
								@SoHopDongListParam				= @SoHopDongList,
								@DmPhongBanREFListParam			= @DmPhongBanREFList,
								@DmBoPhanREFListParam			= @DmBoPhanREFList,
								@DmNhomLamViecREFListParam		= @DmNhomLamViecREFList,
								@TenNhanVienListParam			= @TenNhanVienList,
								@DonViTinhParam					= @DonViTinh,
								@TenDangNhapParam				= @TenDangNhap,
								@IsPheDuyetParam				= @IsPheDuyet,
								@IsNoiBoParam					= @IsNoiBo,
								@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
								@DmBannerREFListParam			= @DmBannerREFList;												
		
		IF (@DmSanPhamREFList = 140 OR @DmSanPhamREFList = 228 OR @DmSanPhamREFList = 241)
		BEGIN
			SELECT
				T2.ThucChayDaTinhID,
				CASE WHEN T1.SoHopDong = '-' THEN 'MuaOnline'
					 ELSE T1.SoHopDong
				END AS SoHopDong, 
				T2.HopDongChiTietREF, 
				T2.DmSanPhamREF, 
				T2.TenSanPham,
				dbo.FormatNumber(MAX(T2.SoLuongTheoHopDong)) AS SoLuongTheoHopDong, 
				T2.DonViTinh, T2.DotChayHopDong, T2.IsPheDuyet,
				T2.TenWebsite, 
				T2.DmWebsiteREF, 
				--dbo.FormatNumber(MAX(T2.DonGia)) AS DonGia, 
				--dbo.FormatNumber(MAX(T2.ChietKhau)) AS ChietKhau, 
				--dbo.FormatNumber(SUM(T2.ThanhTienSauChietKhau)) AS ThanhTienSauChietKhau,
				(SELECT dbo.FormatNumber(ISNULL(MAX(A.DonGia),0))
				 FROM 	HopDongChiTiet A
					INNER JOIN DmWebsite B ON B.DmWebsiteID = A.DmWebsiteREF
				 WHERE A.HopDongFK = T2.HopDongID
					AND A.IsKhuyenMai = 0
					AND A.DmSanPhamREF = T2.DmSanPhamREF
					AND B.WebsiteLink = T2.TenWebsite				 
				) AS DonGia,
				(SELECT dbo.FormatNumber(ISNULL(SUM(A.ThanhTien),0))
				 FROM 	HopDongChiTiet A
					INNER JOIN DmWebsite B ON B.DmWebsiteID = A.DmWebsiteREF
				 WHERE A.HopDongFK = T2.HopDongID
					AND A.IsKhuyenMai = 0
					AND A.DmSanPhamREF = T2.DmSanPhamREF
					AND B.WebsiteLink = T2.TenWebsite				 
				) AS ChietKhau,
				(SELECT dbo.FormatNumber(ISNULL(SUM(A.ThanhTien),0))
				 FROM 	HopDongChiTiet A
					INNER JOIN DmWebsite B ON B.DmWebsiteID = A.DmWebsiteREF
				 WHERE A.HopDongFK = T2.HopDongID
					AND A.IsKhuyenMai = 0
					AND A.DmSanPhamREF = T2.DmSanPhamREF
					AND B.WebsiteLink = T2.TenWebsite				 
				) ThanhTienSauChietKhau,
				dbo.FormatNumber(SUM(T2.SoLuongThucChayKM)) AS SoLuongThucChayKM,
				dbo.FormatNumber(SUM(T2.SoLuongThucChay)) AS SoLuongThucChay,
				dbo.FormatNumber(SUM(T2.ThanhTienThucThu)) AS ThanhTienThucThu
			FROM
			(
				SELECT 
					T.SoHopDong
				FROM
				(
					SELECT 
						A.SoHopDong,
						ROW_NUMBER() OVER(ORDER BY A.SoHopDong) num
					FROM
					(
						SELECT DISTINCT
							SoHopDong
						FROM @DuyetDuLieuTemp 
					)A 
				)T
				WHERE 
					T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
			)T1 INNER JOIN @DuyetDuLieuTemp T2 ON T1.SoHopDong = T2.SoHopDong
			GROUP BY 
				T2.ThucChayDaTinhID,
				T2.HopDongID,
				T1.SoHopDong, 
				T2.HopDongChiTietREF, 
				T2.DmSanPhamREF, 
				T2.TenSanPham,
				T2.DonViTinh, T2.DotChayHopDong, T2.IsPheDuyet,
				T2.TenWebsite, 
				T2.DmWebsiteREF
		END
		ELSE
		BEGIN
			SELECT
				T2.ThucChayDaTinhID,
				CASE WHEN T1.SoHopDong = '-' THEN 'MuaOnline'
					 ELSE T1.SoHopDong
				END AS SoHopDong, 
				T2.HopDongChiTietREF, 
				T2.DmSanPhamREF, 
				T2.TenSanPham,
				dbo.FormatNumber(MAX(T2.SoLuongTheoHopDong)) AS SoLuongTheoHopDong, 
				T2.DonViTinh, 
				' ' AS DotChayHopDong,
				T2.IsPheDuyet,
				T2.TenWebsite, 
				T2.DmWebsiteREF, 
				--dbo.FormatNumber(MAX(T2.DonGia)) AS DonGia, 
				--dbo.FormatNumber(MAX(T2.ChietKhau)) AS ChietKhau, 
				--dbo.FormatNumber(SUM(T2.ThanhTienSauChietKhau)) AS ThanhTienSauChietKhau,
				(SELECT dbo.FormatNumber(ISNULL(MAX(A.DonGia),0))
				 FROM 	HopDongChiTiet A
					INNER JOIN DmWebsite B ON B.DmWebsiteID = A.DmWebsiteREF
				 WHERE A.HopDongFK = T2.HopDongID
					AND A.IsKhuyenMai = 0
					AND A.DmSanPhamREF = T2.DmSanPhamREF
					AND B.WebsiteLink = T2.TenWebsite				 
				) AS DonGia,
				(SELECT dbo.FormatNumber(ISNULL(SUM(A.ThanhTien),0))
				 FROM 	HopDongChiTiet A
					INNER JOIN DmWebsite B ON B.DmWebsiteID = A.DmWebsiteREF
				 WHERE A.HopDongFK = T2.HopDongID
					AND A.IsKhuyenMai = 0
					AND A.DmSanPhamREF = T2.DmSanPhamREF
					AND B.WebsiteLink = T2.TenWebsite				 
				) AS ChietKhau,
				--dbo.FormatNumber(SUM(T2.ThanhTienSauChietKhau)) AS ThanhTienSauChietKhau,
				(SELECT dbo.FormatNumber(ISNULL(SUM(A.ThanhTien),0))
				 FROM 	HopDongChiTiet A
					INNER JOIN DmWebsite B ON B.DmWebsiteID = A.DmWebsiteREF
				 WHERE A.HopDongFK = T2.HopDongID
					AND A.IsKhuyenMai = 0
					AND A.DmSanPhamREF = T2.DmSanPhamREF
					AND B.WebsiteLink = T2.TenWebsite				 
				) ThanhTienSauChietKhau,
				dbo.FormatNumber(SUM(T2.SoLuongThucChayKM)) AS SoLuongThucChayKM,
				dbo.FormatNumber(SUM(T2.SoLuongThucChay)) AS SoLuongThucChay,
				dbo.FormatNumber(SUM(T2.ThanhTienThucThu)) AS ThanhTienThucThu
			FROM
			(
				SELECT 
					T.SoHopDong
				FROM
				(
					SELECT 
						A.SoHopDong,
						ROW_NUMBER() OVER(ORDER BY A.SoHopDong) num
					FROM
					(
						SELECT DISTINCT
							SoHopDong
						FROM @DuyetDuLieuTemp 
					)A 
				)T
				WHERE 
					T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
			)T1 INNER JOIN @DuyetDuLieuTemp T2 ON T1.SoHopDong = T2.SoHopDong
			GROUP BY 
				T2.ThucChayDaTinhID,
				T2.HopDongID,
				T1.SoHopDong, 
				T2.HopDongChiTietREF, 
				T2.DmSanPhamREF, 
				T2.TenSanPham,
				T2.DonViTinh, 
				T2.IsPheDuyet,
				T2.TenWebsite, 
				T2.DmWebsiteREF
		END
	END
	ELSE
		BEGIN
			DECLARE @SqlAdmarket NVARCHAR(MAX), @FilterStringAdmarket NVARCHAR(MAX)
			
			SET @FilterStringAdmarket = ' AND DmWebsiteREF in (134,182,56,137,254,85)'
			SET @FilterStringAdmarket += ' AND CONVERT(DATE,NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
			IF @IsPheDuyet <> -1
				SET @FilterStringAdmarket += ' AND IsPheDuyet = ' + CONVERT(NVARCHAR(10),@IsPheDuyet)
							
			IF @DmWebsiteREFList <> ''
				SET @FilterStringAdmarket += ' AND DmWebsiteREF IN (' + @DmWebsiteREFList + ')'
			
			IF @SoHopDongList <> ''
				SET @FilterStringAdmarket += ' AND 1 <> 1'
		
			IF (@DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1')
				SET @FilterStringAdmarket += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')'
	
			SET @SqlAdmarket = '
				SELECT 
					0 ThucChayPublisherID, ' +
					@DauNhay + 'MuaOnline'  + @DauNhay + ' as SoHopDong, 0 HopDongChiTiet,
					DmSanPhamREF, 
					TenSanPham, ' + 
					@DauNhay + 'click'  + @DauNhay + ' as DonViTinh,
					0 SoLuongTheoHopDong,' + 
					@DauNhay + ''  + @DauNhay + ' as DotChayHopDong,
					IsPheDuyet,
					TenWebsite,
					DmWebsiteREF,
					ROUND(MAX(Price/1.1),0) AS DonGia, 
					0 AS ChietKhau, 
					0 AS ThanhTienSauChietKhau,
					0 AS SoLuongThucChayKM,
					dbo.FormatNumber(SUM(ttClick)) AS SoLuongThucChay,
					dbo.FormatNumber(SUM(ttClick * Price/1.1)) AS ThanhTienThucThu
				FROM ThucChayAdmarketPublisher
				WHERE 1=1 ' + @FilterStringAdmarket + '
				GROUP BY DmSanPhamREF,TenSanPham,DmWebsiteREF,TenWebsite,IsPheDuyet
				'
		
			PRINT @SqlAdmarket
			
			EXECUTE sp_executesql @SqlAdmarket, @Pamrams, 
								@PageIndexParam					= @PageIndex,
								@RecordCountParam				= @RecordCount,
								@GroupFieldNameParam			= @GroupFieldName,
								@StartDateParam					= @StartDate,
								@EndDateParam					= @EndDate,
								@DmSanPhamREFListParam			= @DmSanPhamREFList,
								@DmWebsiteREFListParam			= @DmWebsiteREFList,
								@SoHopDongListParam				= @SoHopDongList,
								@DmPhongBanREFListParam			= @DmPhongBanREFList,
								@DmBoPhanREFListParam			= @DmBoPhanREFList,
								@DmNhomLamViecREFListParam		= @DmNhomLamViecREFList,
								@TenNhanVienListParam			= @TenNhanVienList,
								@DonViTinhParam					= @DonViTinh,
								@TenDangNhapParam				= @TenDangNhap,
								@IsPheDuyetParam				= @IsPheDuyet,
								@IsNoiBoParam					= @IsNoiBo,
								@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
								@DmBannerREFListParam			= @DmBannerREFList;	
		END
END

```
