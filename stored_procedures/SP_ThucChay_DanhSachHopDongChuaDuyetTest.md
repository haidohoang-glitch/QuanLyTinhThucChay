# Stored Procedure: `ThucChay_DanhSachHopDongChuaDuyetTest`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:14.213000
- **Ngày sửa cuối**: 2014-10-14 10:39:55.523000

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

## Definition (Source Code)

```sql
	
CREATE PROCEDURE [dbo].[ThucChay_DanhSachHopDongChuaDuyetTest] 
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
	@IsPheDuyet INT	
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
	
	DECLARE @DuyetDuLieuTemp TABLE (
	[ThucChayDaTinhID] [nvarchar](50) NOT NULL,
	[SoHopDong] [nvarchar](50) NULL,
	[HopDongChiTietREF] [int] NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](255) NULL,
	[SoLuongTheoHopDong] [bigint] NULL,
	[DonViTinh] [nvarchar](50) NULL,
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
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName

	SET @SqlCommand = dbo.Fn_GetQuaTrinhCongTacByNhanVien(@TenDangNhap,@StartDate,@EndDate)
	PRINT @SqlCommand
	
	INSERT INTO @QuaTrinhCongTacTemp(NhanSuID, PhongBanREF, BoPhanREF, NhomLamViecREF, ChucDanhREF, TuNgay, DenNgay)
	EXEC (@SqlCommand)

	IF @IsPheDuyet <> -1
		SET @FilterString = ' AND IsPheDuyet = ' + CONVERT(nvarchar(30),@IsPheDuyet) + ' ' 
	ELSE IF @IsPheDuyet = -1 
		SET @FilterString = ''

	SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp)
	
	IF @Count <= 1
	BEGIN	
		SET @PhongID = (SELECT PhongBanREF FROM @QuaTrinhCongTacTemp)
		SET @BoPhanID = (SELECT BoPhanREF FROM @QuaTrinhCongTacTemp)
		SET @NhomLamViecID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp)
		SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp)
		
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
														@ChucDanhID 
													)
		SET @Sql = '
			SELECT
				A.ThucChayDaTinhID,
				A.SoHopDong, A.HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham,
				(SoLuongHopDongNoiBo+SoLuongHopDongKhuyenMai+SoLuongHopDongThucThu)AS SoLuongTheoHopDong,
				dbo.FormatText(A.DonViTinh) AS DonViTinh,A.DotChayHopDong,IsPheDuyet, A.TenWebsite,A.DmWebsiteREF, A.DonGia, A.ChietKhau,
				A.ThanhTien AS ThanhTienSauChietKhau,
				A.SoLuongThucChayKhuyenMai AS SoLuongThucChayKM,
				(SoLuongThucChayNoiBo+SoLuongThucChayThucThu) AS SoLuongThucChay,
				(ThanhTienThucChayNoiBo + ThanhTienThucThu) AS ThanhTienThucThu
			FROM
			(
				SELECT
					MAX(0) AS ThucChayDaTinhID,
					SoHopDong,HopDongChiTietREF,DmSanPhamREF,TenSanPham,TenWebsite,DmWebsiteREF, 
					dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
					DotChayHopDong,
					IsPheDuyet,
					CASE WHEN HopDongChiTietREF = 0 AND ThanhTienKM = 0 THEN
							dbo.ThucChay_GetChietKhauOfPhanBo(HopDongID,DmSanPhamREF) 
						WHEN HopDongChiTietREF = 0 AND ThanhTienKM > 0 THEN
							100
						ELSE
							ChietKhau
					END AS ChietKhau,
					--DonGia,
					DonGiaTheoDonVi AS DonGia,
					ThanhTien,
					CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongNoiBo,
					CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongKhuyenMai,
					CASE WHEN (ThanhTienKM = 0 AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongHopDongThucThu,
					CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongThucChayNoiBo,
					ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
					CASE WHEN UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
						ELSE 0
					END AS SoLuongThucChayThucThu,
					CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
						ELSE 0
					END AS ThanhTienThucChayNoiBo,
					ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
					ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
					CASE WHEN UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
						ELSE 0
					END AS ThanhTienThucThu
				FROM ThucChayDaTinh
				WHERE TrangThaiHopDong <> 3 ' + @FilterString + '
				GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),TenMaHopDong,ThanhTienKM,
					DotChayHopDong,ChietKhau,DonGia,TenWebsite,DmWebsiteREF,ThanhTien,HopDongID,IsPheDuyet,DonGiaTheoDonVi
			)A
			WHERE  SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
							OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0
		'
		
		PRINT @Sql
													
		INSERT INTO @DuyetDuLieuTemp (
							[ThucChayDaTinhID],
							[SoHopDong],
							[HopDongChiTietREF],
							[DmSanPhamREF],
							[TenSanPham],
							[SoLuongTheoHopDong],
							[DonViTinh],
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
		EXEC (@Sql)	
		
		--SELECT
		--	T2.ThucChayDaTinhID,
		--	T1.SoHopDong, 
		--	T2.HopDongChiTietREF, 
		--	T2.DmSanPhamREF, 
		--	T2.TenSanPham,
		--	dbo.FormatNumber(T2.SoLuongTheoHopDong) AS SoLuongTheoHopDong, 
		--	T2.DonViTinh, T2.DotChayHopDong, T2.IsPheDuyet,
		--	T2.TenWebsite, 
		--	T2.DmWebsiteREF, 
		--	dbo.FormatNumber(T2.DonGia) AS DonGia, 
		--	dbo.FormatNumber(T2.ChietKhau) AS ChietKhau, 
		--	dbo.FormatNumber(T2.ThanhTienSauChietKhau) AS ThanhTienSauChietKhau,
		--	dbo.FormatNumber(T2.SoLuongThucChayKM) AS SoLuongThucChayKM,
		--	dbo.FormatNumber(T2.SoLuongThucChay) AS SoLuongThucChay,
		--	dbo.FormatNumber(T2.ThanhTienThucThu) AS ThanhTienThucThu
		--FROM
		--(
		--	SELECT 
		--		T.SoHopDong
		--	FROM
		--	(
		--		SELECT 
		--			A.SoHopDong,
		--			ROW_NUMBER() OVER(ORDER BY A.SoHopDong) num
		--		FROM
		--		(
		--			SELECT DISTINCT
		--				SoHopDong
		--			FROM @DuyetDuLieuTemp 
		--		)A 
		--	)T
		--	WHERE 
		--		T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
		--)T1 INNER JOIN @DuyetDuLieuTemp T2 ON T1.SoHopDong = T2.SoHopDong
		
		IF (@DmSanPhamREFList = 140 OR @DmSanPhamREFList = 228 OR @DmSanPhamREFList = 241)													
			BEGIN
				PRINT 'IS CPD'
				SELECT
					T2.ThucChayDaTinhID,
					T1.SoHopDong, 
					T2.HopDongChiTietREF, 
					T2.DmSanPhamREF, 
					T2.TenSanPham,
					dbo.FormatNumber(T2.SoLuongTheoHopDong) AS SoLuongTheoHopDong, 
					T2.DonViTinh, T2.DotChayHopDong, T2.IsPheDuyet,
					T2.TenWebsite, 
					T2.DmWebsiteREF, 
					dbo.FormatNumber(T2.DonGia) AS DonGia, 
					dbo.FormatNumber(T2.ChietKhau) AS ChietKhau, 
					dbo.FormatNumber(T2.ThanhTienSauChietKhau) AS ThanhTienSauChietKhau,
					dbo.FormatNumber(T2.SoLuongThucChayKM) AS SoLuongThucChayKM,
					dbo.FormatNumber(T2.SoLuongThucChay) AS SoLuongThucChay,
					dbo.FormatNumber(T2.ThanhTienThucThu) AS ThanhTienThucThu
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
			END
		ELSE
		BEGIN
			PRINT 'NOT CPD'
			SELECT
				T2.ThucChayDaTinhID,
				T1.SoHopDong, 
				T2.HopDongChiTietREF, 
				T2.DmSanPhamREF, 
				T2.TenSanPham,
				dbo.FormatNumber(MAX(T2.SoLuongTheoHopDong)) AS SoLuongTheoHopDong, 
				T2.DonViTinh,
				0 AS DotChayHopDong,
				T2.IsPheDuyet,
				T2.TenWebsite, 
				T2.DmWebsiteREF, 
				dbo.FormatNumber(MAX(T2.DonGia)) AS DonGia, 
				dbo.FormatNumber(T2.ChietKhau) AS ChietKhau, 
				dbo.FormatNumber(SUM(T2.ThanhTienSauChietKhau)) AS ThanhTienSauChietKhau,
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
				T1.SoHopDong, 
				T2.HopDongChiTietREF, 
				T2.DmSanPhamREF, 
				T2.TenSanPham,
				T2.DonViTinh,
				T2.IsPheDuyet,
				T2.TenWebsite, 
				T2.DmWebsiteREF,
				T2.ChietKhau
			ORDER BY T2.DmWebsiteREF 
		END
		
	END
	ELSE
    BEGIN
		DECLARE  @NhomID int
			
		DECLARE @TableResult TABLE
		(
			ThucChayDaTinhID nvarchar(50),
			SoHopDong nvarchar(50),
			HopDongChiTietREF int,
			DmSanPhamREF int,
			TenSanPham nvarchar(50),
			SoLuongTheoHopDong bigint,
			DonViTinh nvarchar(50),
			DotChayHopDong nvarchar(MAX),
			IsPheDuyet int,
			TenWebsite nvarchar(50),
			DmWebsiteREF int,
			DonGia int,
			ChietKhau int,
			ThanhTienSauChietKhau float,
			SoLuongThucChayKM bigint,
			SoLuongThucChay bigint,
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
	   				
	   			SET @FilterString = dbo.GetThucChayFilterString(
														@TuNgay ,
														@DenNgay ,
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
													)
	   			
	   			SET @Sql = '
	   					SELECT
							A.ThucChayDaTinhID,
							A.SoHopDong, A.HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham,
							(SoLuongHopDongNoiBo+SoLuongHopDongKhuyenMai+SoLuongHopDongThucThu)AS SoLuongTheoHopDong,
							A.DonViTinh,A.DotChayHopDong,IsPheDuyet, A.TenWebsite,A.DmWebsiteREF, A.DonGia, A.ChietKhau,
							A.ThanhTien AS ThanhTienSauChietKhau,
							A.SoLuongThucChayKhuyenMai AS SoLuongThucChayKM,
							(SoLuongThucChayNoiBo+SoLuongThucChayThucThu) AS SoLuongThucChay,
							(ThanhTienThucChayNoiBo + ThanhTienThucThu) AS ThanhTienThucThu
						FROM
						(
							SELECT
								MAX(0) AS ThucChayDaTinhID,
								SoHopDong,HopDongChiTietREF,DmSanPhamREF,TenSanPham,TenWebsite,DmWebsiteREF, 
								dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,
								DotChayHopDong,
								IsPheDuyet,
								CASE WHEN HopDongChiTietREF = 0 THEN
										dbo.ThucChay_GetChietKhauOfPhanBo(HopDongID,DmSanPhamREF) 
									ELSE
										ChietKhau
								END AS ChietKhau,
								--DonGia,
								DonGiaTheoDonVi AS DonGia,
								ThanhTien,
								CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
									ELSE 0
								END AS SoLuongHopDongNoiBo,
								CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
									ELSE 0
								END AS SoLuongHopDongKhuyenMai,
								CASE WHEN (ThanhTienKM = 0 AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
									ELSE 0
								END AS SoLuongHopDongThucThu,
								CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
									ELSE 0
								END AS SoLuongThucChayNoiBo,
								ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
								CASE WHEN UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
									ELSE 0
								END AS SoLuongThucChayThucThu,
								CASE WHEN UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
									ELSE 0
								END AS ThanhTienThucChayNoiBo,
								ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
								ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
								CASE WHEN UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
									ELSE 0
								END AS ThanhTienThucThu
							FROM ThucChayDaTinh
							WHERE TrangThaiHopDong <> 3 ' + @FilterString + '
							GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),TenMaHopDong,ThanhTienKM,
								DotChayHopDong,ChietKhau,DonGia,TenWebsite,DmWebsiteREF,ThanhTien,HopDongID,IsPheDuyet,DonGiaTheoDonVi
						)A
						WHERE  SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
										OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0'
				
	   			PRINT @Sql
	   			INSERT INTO @TableResult(ThucChayDaTinhID,
	   									SoHopDong,
										HopDongChiTietREF,
										DmSanPhamREF,
										TenSanPham,
										SoLuongTheoHopDong,
										DonViTinh,
										DotChayHopDong,
										IsPheDuyet,
										TenWebsite,
										DmWebsiteREF,
										DonGia,
										ChietKhau,
										ThanhTienSauChietKhau,
										SoLuongThucChayKM,
										SoLuongThucChay,
										ThanhTienThucThu
										)
	   			EXEC (@Sql)
	   						
				FETCH NEXT FROM Data INTO @CurrentID;		  
		   END;	   
		CLOSE Data;
		DEALLOCATE Data;
		
		INSERT INTO @DuyetDuLieuTemp (
							[ThucChayDaTinhID],
							[SoHopDong],
							[HopDongChiTietREF],
							[DmSanPhamREF],
							[TenSanPham],
							[SoLuongTheoHopDong],
							[DonViTinh],
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
		SELECT 
			MAX(T1.ThucChayDaTinhID) AS ThucChayDaTinhID,
			T1.SoHopDong, T1.HopDongChiTietREF, T1.DmSanPhamREF, T1.TenSanPham,
			SUM(T1.SoLuongTheoHopDong) AS SoLuongTheoHopDong, T1.DonViTinh,
			T1.DotChayHopDong, T1.IsPheDuyet, T1.TenWebsite, DmWebsiteREF, T1.DonGia,
			T1.ChietKhau,
			T1.ThanhTienSauChietKhau AS ThanhTienSauChietKhau,				
			SUM(T1.SoLuongThucChayKM) AS SoLuongThucChayKM,
			SUM(T1.SoLuongThucChay) AS SoLuongThucChay,
			SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu
		FROM @TableResult T1 
		GROUP BY T1.SoHopDong, T1.HopDongChiTietREF, T1.DmSanPhamREF, T1.TenSanPham, T1.DonViTinh,T1.DotChayHopDong, 
				T1.TenWebsite, T1.DonGia, T1.ChietKhau, T1.ThanhTienSauChietKhau, T1.DmWebsiteREF, T1.IsPheDuyet						
		
		IF (@DmSanPhamREFList = 140 OR @DmSanPhamREFList = 228 OR @DmSanPhamREFList = 241)													
			BEGIN
				PRINT 'Is CPD'
				SELECT
					T2.ThucChayDaTinhID,
					T1.SoHopDong, 
					T2.HopDongChiTietREF, 
					T2.DmSanPhamREF, 
					T2.TenSanPham,
					dbo.FormatNumber(T2.SoLuongTheoHopDong) AS SoLuongTheoHopDong, 
					T2.DonViTinh, T2.DotChayHopDong, T2.IsPheDuyet,
					T2.TenWebsite, 
					T2.DmWebsiteREF, 
					dbo.FormatNumber(T2.DonGia) AS DonGia, 
					dbo.FormatNumber(T2.ChietKhau) AS ChietKhau, 
					dbo.FormatNumber(T2.ThanhTienSauChietKhau) AS ThanhTienSauChietKhau,
					dbo.FormatNumber(T2.SoLuongThucChayKM) AS SoLuongThucChayKM,
					dbo.FormatNumber(T2.SoLuongThucChay) AS SoLuongThucChay,
					dbo.FormatNumber(T2.ThanhTienThucThu) AS ThanhTienThucThu
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
			END
		ELSE
		BEGIN
			PRINT 'Not CPD'
			SELECT
				T2.ThucChayDaTinhID,
				T1.SoHopDong, 
				T2.HopDongChiTietREF, 
				T2.DmSanPhamREF, 
				T2.TenSanPham,
				dbo.FormatNumber(MAX(T2.SoLuongTheoHopDong)) AS SoLuongTheoHopDong, 
				T2.DonViTinh,
				T2.IsPheDuyet,
				T2.TenWebsite, 
				T2.DmWebsiteREF, 
				dbo.FormatNumber(MAX(T2.DonGia)) AS DonGia, 
				dbo.FormatNumber(T2.ChietKhau) AS ChietKhau, 
				dbo.FormatNumber(SUM(T2.ThanhTienSauChietKhau)) AS ThanhTienSauChietKhau,
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
				T1.SoHopDong, 
				T2.HopDongChiTietREF, 
				T2.DmSanPhamREF, 
				T2.TenSanPham,
				T2.DonViTinh,
				T2.IsPheDuyet,
				T2.TenWebsite, 
				T2.DmWebsiteREF,
				T2.ChietKhau
			ORDER BY T2.DmWebsiteREF 
		END
		
		--SELECT
		--	T2.ThucChayDaTinhID,
		--	T1.SoHopDong, T2.HopDongChiTietREF, T2.DmSanPhamREF, T2.TenSanPham,
		--	T2.SoLuongTheoHopDong, dbo.FormatText(T2.DonViTinh) AS DonViTinh, T2.DotChayHopDong, T2.IsPheDuyet,
		--	T2.TenWebsite, T2.DmWebsiteREF, T2.DonGia, T2.ChietKhau, 
		--	T2.ThanhTienSauChietKhau,
		--	T2.SoLuongThucChayKM,
		--	T2.SoLuongThucChay,
		--	T2.ThanhTienThucThu
		--FROM
		--(
		--	SELECT 
		--		T.SoHopDong
		--	FROM
		--	(
		--		SELECT 
		--			A.SoHopDong,
		--			ROW_NUMBER() OVER(ORDER BY A.SoHopDong) num
		--		FROM
		--		(
		--			SELECT DISTINCT
		--				SoHopDong
		--			FROM @DuyetDuLieuTemp 
		--		)A 
		--	)T
		--	WHERE 
		--		T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
		--)T1 INNER JOIN @DuyetDuLieuTemp T2 ON T1.SoHopDong = T2.SoHopDong

    END  
END
```
