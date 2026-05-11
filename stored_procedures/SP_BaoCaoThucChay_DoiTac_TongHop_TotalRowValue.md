# Stored Procedure: `BaoCaoThucChay_DoiTac_TongHop_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:07.523000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-16
-- Description:	BaoCaoThucChay_DoiTac_TongHop
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_TongHop_TotalRowValue]
	-- Add the parameters for the stored procedure here
	@StartDate Datetime,
	@EndDate Datetime,
	@SoHopDongList nvarchar(2000),
	@DmWebsiteREFList nvarchar(2000),
	@TenDangNhap nvarchar(50),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmSanPhamREFList NVARCHAR(2000)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Sql nvarchar(4000)
    DECLARE @DauNhay nvarchar(50)
    DECLARE @FillterString nvarchar(4000)
    DECLARE @OrderByString nvarchar(2000)
    
    DECLARE @TempTable AS TABLE (
			TotalRow INT,
			TongThanhTienThucChayNoiBo FLOAT,
			TotalValue FLOAT
    )
    
    SET @DauNhay = ''''
    
	
	SET @FillterString = ' AND IsPheDuyet = 1'
	
	IF (@DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1')
		SET @FillterString += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')'
		
	IF @DmSanPhamREFList <> '' 
		SET @FillterString += ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')'
	
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
    
		
	SET @Sql = '
		SELECT 
			1 AS TotalRow, 
			(SUM(T.ThanhTienThucChayNoiBo)) AS ThanhTienThucChayNoiBo,
			(SUM(T.ThanhTienThucChay)) AS TongTien
			 
		FROM
		(
				SELECT
					A.ThucChayDaTinhID,
					A.SoHopDong, A.HopDongChiTietREF, A.DmSanPhamREF, A.TenSanPham,
					(SoLuongHopDongNoiBo+SoLuongHopDongKhuyenMai+SoLuongHopDongThucThu)AS SoLuongTheoHopDong,
					A.DonViTinh,A.DotChayHopDong,IsPheDuyet, A.TenWebsite,A.DmWebsiteREF, A.DonGia, A.ChietKhau,
					A.ThanhTien AS ThanhTienSauChietKhau,
					A.SoLuongThucChayKhuyenMai AS SoLuongThucChayKM,
					(SoLuongThucChayThucThu + SoLuongThucChayNoiBo) AS SoLuongThucChay,
					(A.ThanhTienThucThu + A.GiaTriThayDoi) AS ThanhTienThucChay,
					A.ThanhTienThucChayNoiBo
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
						SUM(ISNULL(GiaTriThayDoi,0)) AS GiaTriThayDoi,
						CASE WHEN (UPPER(SoHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
							ELSE 0
						END AS SoLuongHopDongNoiBo,
						CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
							ELSE 0
						END AS SoLuongHopDongKhuyenMai,
						CASE WHEN (ThanhTienKM = 0 AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
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
					WHERE TrangThaiHopDong <> 3 AND DangSuDung NOT IN (5001,5002,5003) ' + @FillterString + '
					GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),SoHopDong,ThanhTienKM,
						DotChayHopDong,ChietKhau,DonGia,TenWebsite,DmWebsiteREF,ThanhTien,HopDongID,IsPheDuyet
				)A
				WHERE  SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
								OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0
								OR GiaTriThayDoi <> 0
		)T
	'
    
    PRINT @Sql
    
    INSERT INTO @TempTable
    EXEC(@Sql)
    
    DECLARE @SqlAdmarket NVARCHAR(MAX), @FilterStringAdmarket NVARCHAR(MAX);
    DECLARE @ListWebsiteID NVARCHAR(200), @GroupPermission INT;
    
    IF @DmSanPhamREFList <> '' 
		SET @FilterStringAdmarket += ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')'
		
	IF @DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1'
		SET @FilterStringAdmarket += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')';
    
    SET @FilterStringAdmarket = ' AND IsPheDuyet = 1 AND DmWebsiteREF in (134,182,56,137,254,85)'
    SET @FilterStringAdmarket += ' AND NgayThucHien BETWEEN ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' AND ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay
    SET @ListWebsiteID = dbo.GetListWebsiteByNhanVien(@TenDangNhap)
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    IF(@DmWebsiteREFList <> '')
		SET @FilterStringAdmarket += ' AND DmWebsiteREF in (' + @DmWebsiteREFList + ')'
			
    IF (@GroupPermission <> -1)
    BEGIN
		IF @ListWebsiteID <> ''
			SET @FilterStringAdmarket = @FilterStringAdmarket + ' AND DmWebsiteREF in (' + @ListWebsiteID + ')';
	END
    
    SET @SqlAdmarket = '
		SELECT
			1 AS TotalRow,
			0 ThanhTienThucChayNoiBo,
			ROUND(SUM(ttClick*Price/1.1),0) AS TongTien
		FROM ThucChayAdmarketPublisher A
		WHERE 1 = 1 ' + @FilterStringAdmarket + '
		GROUP BY DmSanPhamREF, TenSanPham
		'
		
    INSERT INTO @TempTable
    EXEC (@SqlAdmarket);
    
    PRINT @SqlAdmarket;
    
    -- Cho Log action nguoi dung
	DECLARE @LogTime						DATETIME
			,@TenBaoCao						NVARCHAR(512)
			,@DmPhongBanREFList				NVARCHAR(2000) = ''
			,@DmBoPhanREFList				NVARCHAR(2000) = ''
			,@DmNhomLamViecREFList			NVARCHAR(2000) = ''
			,@TenNhanVienList				NVARCHAR(2000) = ''
			,@DmBannerREFList				NVARCHAR(2000) = ''
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
			,@IsPheDuyet					INT				= 1
			,@PheDuyetAt					DATETIME
			,@PheDuyetBy					NVARCHAR(50)
			
	SET @TenBaoCao = N'Báo cáo kênh - tổng hợp'
		
	-- Lay So luong theo don vi tinh Click
	SELECT  @TongClickThucChayNoiBo		= 0,
			@TongClickThucChayKhuyenMai = 0,
			@TongClickThucChay			= 0,
			
			@TongViewThucChayNoiBo		= 0,
			@TongViewThucChayKhuyenMai  = 0,
			@TongViewThucChay			= 0,
			
			@TongSoNgayChayNoiBo		= 0,
			@TongSoNgayChayKhuyenMai	= 0,
			@TongSoNgayChay				= 0,
			
			@TongSoBaiVietNoiBo		= 0,
			@TongSoBaiVietKhuyenMai = 0,
			@TongSoBaiViet			= 0
	
	-- Lay Thanh tien thuc chay
	SELECT  
			@TongTienNoiBo				= SUM(A.TongThanhTienThucChayNoiBo),
			@TongTienKhuyemMai			= 0,
			@TongTienThucChaySauCK		= SUM(A.TotalValue),
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
		
	-- End Insert action log
    
    SELECT 
		SUM(TotalRow) AS TotalRow,
		dbo.FormatNumber(SUM(TongThanhTienThucChayNoiBo)) AS TongThanhTienThucChayNoiBo,
		dbo.FormatNumber(SUM(TotalValue)) AS TotalValue
    FROM @TempTable
    
END

```
