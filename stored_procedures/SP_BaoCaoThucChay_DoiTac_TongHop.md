# Stored Procedure: `BaoCaoThucChay_DoiTac_TongHop`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:07.317000
- **Ngày sửa cuối**: 2015-04-03 18:36:12.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ColumnSort` | `nvarchar(100)` | No |
| `@OrderBy` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-15
-- Description:	BaoCaoThucChay_DoiTac_TongHop
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_TongHop]
	-- Add the parameters for the stored procedure here
	@PageIndex int,
	@RecordCount int,
	@StartDate Datetime,
	@EndDate Datetime,
	@SoHopDongList NVARCHAR(2000),
	@DmWebsiteREFList nvarchar(2000),
	@TenDangNhap nvarchar(50),
	@ColumnSort nvarchar(50),
	@OrderBy nvarchar(50),
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
    
    SET @DauNhay = ''''
    
  --  SET @FillterString = 'AND CONVERT(DATE, NgayThucHien) BETWEEN ' + @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay + ' AND ' + @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay
  --  IF @DmWebsiteREFList <> ''
		--SET @FillterString += ' AND DmWebsiteREF IN (' + @DmWebsiteREFList + ')'
	
	--SET @FillterString = ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND IsPheDuyet = 1'
	PRINT @TenDangNhap
	SET @FillterString = ' AND IsPheDuyet = 1'

	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	
	IF dbo.ThucChay_CheckPartnerIsViewedHopDongNoiBo(@TenDangNhap) = 0
		SET @FillterString += ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ')'
		
	IF (@DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1')
		SET @FillterString += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')'
		
	IF @DmSanPhamREFList <> '' 
		SET @FillterString += ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')'
	
	PRINT @FillterString
		
	IF @ColumnSort = 'TenSanPham'
		SET @OrderByString = 'TenSanPham'
	ELSE IF @ColumnSort = 'TongTien'
		SET @OrderByString = 'SUM(ThanhTienThucThu)'

	SET @OrderByString = 'TenSanPham'
	
	DECLARE @TempTable AS TABLE (
			DmHinhThucQuangCao	INT,
			TenHinhThucQuangCao	NVARCHAR(50),
			DmSanPhamREF INT,
			TenSanPham NVARCHAR(50),
			ThanhTienThucChayNoiBo FLOAT,
			TongTien FLOAT
	)
    
	SET @Sql = '
		SELECT 
			T.DmHinhThucQuangCao, T.TenHinhThucQuangCao,
			T.DmSanPhamREF, T.TenSanPham, 
			(SUM(T.ThanhTienThucChayNoiBo)) AS ThanhTienThucChayNoiBo,
			(SUM(T.ThanhTienThucChay)) AS TongTien
			 
		FROM
		(
				SELECT
					A.ThucChayDaTinhID,
					A.SoHopDong, A.HopDongChiTietREF, 
					A.DmHinhThucQuangCao,A.TenHinhThucQuangCao,
					A.DmSanPhamREF, A.TenSanPham,
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
						SoHopDong,DmHinhThucQuangCao,TenHinhThucQuangCao,
						HopDongChiTietREF,DmSanPhamREF,TenSanPham,TenWebsite,DmWebsiteREF, 
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
						CASE WHEN (ThanhTienKM = 0) THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
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
					WHERE TrangThaiHopDong <> 3 ' + @FillterString + '
					GROUP BY DmHinhThucQuangCao,TenHinhThucQuangCao, DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),SoHopDong,ThanhTienKM,
						DotChayHopDong,ChietKhau,DonGia,TenWebsite,DmWebsiteREF,ThanhTien,HopDongID,IsPheDuyet
				)A
				WHERE  SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
								OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0
								OR GiaTriThayDoi <> 0
		)T
		GROUP BY T.DmHinhThucQuangCao, T.TenHinhThucQuangCao,T.DmSanPhamREF, T.TenSanPham 
		ORDER BY ' + @OrderByString + ' ' + @OrderBy 		
    
    PRINT @Sql
    
    INSERT INTO @TempTable    
    EXEC(@Sql)
        
    
    DECLARE @SqlAdmarket NVARCHAR(MAX), @FilterStringAdmarket NVARCHAR(MAX);
    DECLARE @ListWebsiteID NVARCHAR(200), @GroupPermission INT;
    
    SET @FilterStringAdmarket = ' AND IsPheDuyet = 1 AND DmWebsiteREF in (134,182,56,137,254,85)'
    
    IF @DmSanPhamREFList <> '' 
		SET @FilterStringAdmarket += ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')'
		
	IF @DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1'
		SET @FilterStringAdmarket += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')';
		
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
			7 as DmHinhThucQuangCao,' + @DauNhay + 'CPC' + @DauNhay + ' as TenHinhThucQuangCao,
			DmSanPhamREF, TenSanPham,
			0 ThanhTienThucChayNoiBo,
			SUM(ttClick*Price/1.1) AS TongTien
		FROM ThucChayAdmarketPublisher A
		WHERE 1 = 1 ' + @FilterStringAdmarket + '
		GROUP BY DmSanPhamREF, TenSanPham
		'
    
    INSERT INTO @TempTable
    EXEC (@SqlAdmarket);
    
    PRINT @SqlAdmarket;
    
    -- SELECT DATA TO SHOW
    SELECT 
		DmHinhThucQuangCao, TenHinhThucQuangCao,
		DmSanPhamREF, TenSanPham,
		dbo.FormatNumber(ThanhTienThucChayNoiBo) AS ThanhTienThucChayNoiBo,
		dbo.FormatNumber(TongTien) AS TongTien
    FROM @TempTable
    ORDER BY TenSanPham
    
END

```
