# Stored Procedure: `ThucChay_DanhSachHopDongChuaDuyet_TotalRow`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:09.250000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.673000

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
| `@DonViTinh` | `nvarchar(100)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@IsPheDuyet` | `int(4)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-17
-- Description:	ThucChay_DanhSachHopDongChuaDuyet_TotalRow
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_DanhSachHopDongChuaDuyet_TotalRow]
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
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName

	--SET @SqlCommand = dbo.Fn_GetQuaTrinhCongTacByNhanVien(@TenDangNhap,@StartDate,@EndDate)
	--PRINT @SqlCommand
	
	--INSERT INTO @QuaTrinhCongTacTemp(NhanSuID, PhongBanREF, BoPhanREF, NhomLamViecREF, ChucDanhREF, TuNgay, DenNgay)
	--EXEC (@SqlCommand)
	
	IF @DmSanPhamREFList <> 144 
	BEGIN

		IF @IsPheDuyet <> -1
			SET @FilterString = ' AND IsPheDuyet = ' + CONVERT(nvarchar(30),@IsPheDuyet) + ' ' 
		ELSE IF @IsPheDuyet = -1 
			SET @FilterString = ''
		
		PRINT 'IsNoiBo: ' + CONVERT(NVARCHAR(50), @IsNoiBo)
		IF @IsNoiBo = 1
			SET @FilterString += '' 
		ELSE IF @IsNoiBo = 0
			SET @FilterString += ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'

		SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp)
	
		IF @IsPheDuyet <> -1
			SET @FilterString += ' AND IsPheDuyet = ' + CONVERT(nvarchar(30),@IsPheDuyet) + ' ' 
		ELSE IF @IsPheDuyet = -1 
			SET @FilterString += ''

		SET @Count = (SELECT COUNT(*) FROM @QuaTrinhCongTacTemp)
	
	
		SET @PhongID = (SELECT PhongBanREF FROM @QuaTrinhCongTacTemp)
		SET @BoPhanID = (SELECT BoPhanREF FROM @QuaTrinhCongTacTemp)
		SET @NhomLamViecID = (SELECT NhomLamViecREF FROM @QuaTrinhCongTacTemp)
		SET @ChucDanhID = (SELECT ChucDanhREF FROM @QuaTrinhCongTacTemp)
	
	
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
				COUNT(DISTINCT T.SoHopDong) AS MaxRecords 
			FROM
			(
					SELECT
							A.ThucChayDaTinhID,
							A.SoHopDong, A.HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham,
							(SoLuongHopDongNoiBo+SoLuongHopDongKhuyenMai+SoLuongHopDongThucThu)AS SoLuongTheoHopDong,
							A.DonViTinh,A.DotChayHopDong,IsPheDuyet, A.TenWebsite,A.DmWebsiteREF, A.DonGia, A.ChietKhau,
							A.ThanhTien AS ThanhTienSauChietKhau,
							A.SoLuongThucChayKhuyenMai AS SoLuongThucChayKM,
							(SoLuongThucChayNoiBo+SoLuongThucChayThucThu) AS SoLuongThucChay,
							(ThanhTienThucChayNoiBo + ThanhTienThucThu + GiaTriThayDoi) AS ThanhTienThucThu
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
								DonGia,ThanhTien,
								SUM(ISNULL(GiaTriThayDoi,0)) GiaTriThayDoi,
								CASE WHEN (UPPER(SoHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
									ELSE 0
								END AS SoLuongHopDongNoiBo,
								CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
									ELSE 0
								END AS SoLuongHopDongKhuyenMai,
								CASE WHEN (ThanhTienKM = 0 AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
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
							GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),SoHopDong,ThanhTienKM,
								DotChayHopDong,ChietKhau,DonGia,TenWebsite,DmWebsiteREF,ThanhTien,HopDongID,IsPheDuyet
						)A
						WHERE  (SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
										OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0 OR GiaTriThayDoi <> 0)
								AND (ThanhTienThucChayNoiBo + ThanhTienThucChaySauChietKhau + GiaTriThayDoi) > 1000
			)T
			'
	    
		PRINT @Sql;
		EXEC (@Sql);
	END
	ELSE
	BEGIN
		SELECT 1 AS MaxRecords
		
		-- DU LIEU ADMARKET TRA VE KHONG CO HOP DONG NEN MAC DINH CHI CO 1.
		--DECLARE @SqlAdmarket NVARCHAR(MAX), @FilterStringAdmarket NVARCHAR(MAX)
		
		--SET @FilterStringAdmarket = ' AND DmWebsiteREF in (134,182,56,137,254,85)'
		--SET @FilterStringAdmarket += ' AND CONVERT(DATE,NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
		--IF @IsPheDuyet <> -1
		--		SET @FilterStringAdmarket += ' AND IsPheDuyet = ' + CONVERT(NVARCHAR(10),@IsPheDuyet)
				
		--	IF @DmWebsiteREFList <> ''
		--		SET @FilterStringAdmarket += ' AND DmWebsiteREF IN (' + @DmWebsiteREFList + ')'
		
		--	IF (@DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1')
		--		SET @FilterStringAdmarket += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')'
	
		--SET @SqlAdmarket = '
		--	SELECT 
		--		COUNT(DmWebsiteREF) MaxRecords
		--	FROM ThucChayAdmarketPublisher
		--	WHERE 1=1 ' + @FilterStringAdmarket + '
			
		--	'
		
		--PRINT @SqlAdmarket
			
		--EXEC(@SqlAdmarket)
	END
	
END

```
