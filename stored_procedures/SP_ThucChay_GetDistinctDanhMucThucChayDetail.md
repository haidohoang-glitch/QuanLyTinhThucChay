# Stored Procedure: `ThucChay_GetDistinctDanhMucThucChayDetail`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-28 11:58:12.600000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.427000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@DmBookingREF` | `nvarchar(4000)` | No |
| `@DmBannerREF` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_GetDistinctDanhMucThucChayDetail]
	-- Add the parameters for the stored procedure here
	@GroupFieldName nvarchar(50),
	@StartDate date,
	@EndDate date,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@DmBookingREF nvarchar(2000),
	@DmBannerREF nvarchar(2000)
AS
BEGIN
	DECLARE @sql NVARCHAR(4000) ='';

	DECLARE @DmSanPhamREFFilter NVARCHAR(4000)='';
	DECLARE @DmWebsiteREFFilter NVARCHAR(4000)='';
	DECLARE @DmSoHopDongFilter NVARCHAR(4000)='';
	DECLARE @DmPhongBanREFFilter NVARCHAR(4000)='';
	DECLARE @DmBoPhanREFFilter NVARCHAR(4000)='';
	DECLARE @DmNhomLamViecREFFilter NVARCHAR(4000)='';
	DECLARE @TenNhanVienFilter NVARCHAR(4000)='';
	DECLARE @TenDangNhap NVARCHAR(50);
	
	Declare @DauNhay nvarchar(50)
	Declare @GroupByFildID nvarchar(50)
	Declare @GroupByFild nvarchar(50)
	
	Declare @FilterString nvarchar(4000);

	set @DauNhay = ''''
	SET @TenDangNhap = 'thucchay'

	set @DmSanPhamREFList =replace(@DmSanPhamREFList,'''','');
	set @DmWebsiteREFList=replace(@DmWebsiteREFList,'''','');
	set @SoHopDongList =replace(@SoHopDongList,'''','');
	set @DmPhongBanREFList =replace(@DmPhongBanREFList,'''','');
	set @DmBoPhanREFList =replace(@DmBoPhanREFList,'''','');
	set @DmNhomLamViecREFList =replace(@DmNhomLamViecREFList,'''','');
	set @TenNhanVienList =replace(@TenNhanVienList,'''','');
	
	
	IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild = 'DmSanPhamREF'
		SET @GroupByFildID = 'DmSanPhamREF AS ID' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENWEBSITE'
		Begin
			SET @GroupByFild = 'DmWebsiteREF'
			SET @GroupByFildID = 'DmWebsiteREF AS ID' 
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENPHONGBAN'
		Begin
			SET @GroupByFild = 'DmPhongBanREF'
			SET @GroupByFildID = 'DmPhongBanREF AS ID' 
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENBOPHAN'
		Begin
			SET @GroupByFild = 'DmBoPhanREF'
			SET @GroupByFildID = 'DmBoPhanREF AS ID' 
		End
	ELSE IF UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC'
		Begin
			SET @GroupByFild = 'DmNhomLamViecREF'
			SET @GroupByFildID = 'DmNhomLamViecREF AS ID' 
		END
	ELSE IF UPPER(@GroupFieldName) = 'SOHOPDONG'
		Begin
			SET @GroupByFild = 'SoHopDong'
			SET @GroupByFildID = 'SoHopDong AS ID' 
		END
	ELSE IF UPPER(@GroupFieldName) = 'TenNhanVien'
		Begin
			SET @GroupByFild = 'TenNhanVien'
			SET @GroupByFildID = 'TenNhanVien AS ID' 
		END
	ELSE IF (@GroupFieldName) = 'DmBannerREF'
	BEGIN
		SET @GroupByFild = 'DmBannerREF'
		SET @GroupByFildID = 'DmBannerREF AS ID' 
	END

		
	
	SET @FilterString = ' AND CONVERT(DATE,A.NgayThucHien) Between ' + @DauNhay + CONVERT(nvarchar(50),@StartDate) + @DauNhay + ' AND '+ @DauNhay + CONVERT(nvarchar(50),@EndDate)+@DauNhay 
	 
	IF @SoHopDongList <> ''
		SET @FilterString += ' AND SoHopDong IN (' + + @SoHopDongList + ')'
	IF @DmSanPhamREFList <> ''
		SET @FilterString += ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')'
	IF @DmWebsiteREFList <> ''
		SET @FilterString += ' AND DmWebsiteREF IN (' + @DmWebsiteREFList + ')'	
	IF @DmBannerREF <> ''
		SET @FilterString += ' AND DmBannerREF IN (' + @DmBannerREF + ')'
	IF @DmBookingREF <> ''
		SET @FilterString += ' AND B.DanhsachDmBookingREF IN (' + @DmBookingREF + ')'
		
	PRINT @GroupFieldName;
	
	IF @GroupFieldName = 'DmBookingREF'
	BEGIN
		EXEC dbo.GetDistinctBookingIDFromThucChaySystem @StartDate,@EndDate,@SoHopDongList,@DmBookingREF,@DmBannerREF
	END
	ELSE
	BEGIN
		IF @GroupFieldName = 'TenSanPham'
		BEGIN
			SET @sql='
			SELECT  DISTINCT
				dbo.ThucChay_RepleaceTenSanPham(TenSanPham)  AS Name,
				DmSanPhamREF AS ID 
			FROM dbo.ThucChay as A 
			 WHERE (1=1) 
			AND dbo.ThucChay_CheckLechTreoHa(NgayThucHien, HopDongChiTietREF, TenSanPham) > 0 
			'
			SET @Sql = @Sql + @FilterString + '
		
			GROUP BY '+ @GroupByFild + ',' + @GroupFieldName +' 
			ORDER BY Name'
		END 
		ELSE IF @GroupFieldName = 'SoHopDong'
		BEGIN
			SET @sql='
			SELECT  
				SoHopDong AS Name,
				SoHopDong AS ID 
			FROM dbo.ThucChay as A 
			 WHERE (1=1) 
			AND dbo.ThucChay_CheckLechTreoHa(NgayThucHien, HopDongChiTietREF, TenSanPham) > 0 
			AND dbo.ThucChay_CheckSoHopDong(SoHopDong) = 1
			'
			SET @Sql = @Sql + @FilterString + '
		
			GROUP BY '+ @GroupByFild + ',' + @GroupFieldName +' 
			ORDER BY SoHopDong'
		END
		ELSE IF @GroupFieldName = 'TenWebsite'
		BEGIN
			SET @sql='	
			SELECT DISTINCT '+@GroupFieldName+' as Name,'+@GroupByFildID+'
			FROM dbo.ThucChay as A 
			 WHERE (1=1) 
			AND dbo.ThucChay_CheckLechTreoHa(NgayThucHien, HopDongChiTietREF, TenSanPham) > 0 
			'
			SET @Sql = @Sql + @FilterString + '
		
			GROUP BY '+ @GroupByFild + ',' + @GroupFieldName +' 
			ORDER BY '+@GroupFieldName +' ASC'
		END
		ELSE IF @GroupFieldName = 'DmBannerREF'
		BEGIN
			SET @sql = '
			SELECT DISTINCT '+@GroupFieldName+' as Name,'+@GroupByFildID+'
			FROM dbo.ThucChay as A 
			 WHERE (1=1)
			'
			SET @sql += @FilterString + '
			GROUP BY '+ @GroupByFild + ',' + @GroupFieldName +' 
			ORDER BY '+@GroupFieldName +' ASC'
		END
		
		--IF @GroupFieldName = 'DmBookingREF'
		--BEGIN
		--	SET @sql = '
		--	SELECT DISTINCT B.DanhsachDmBookingREF AS Name, B.DanhsachDmBookingREF AS ID 
		--	FROM ThucChay A 
		--	INNER JOIN [dbo].[GetThucChayByFullCondition](' + @DauNhay + CONVERT(nvarchar(50),@StartDate) + @DauNhay + ','  + @DauNhay + CONVERT(nvarchar(50),@EndDate) + @DauNhay + ',' + @DauNhay + CONVERT(nvarchar(50),@DmBookingREF) + @DauNhay + ',' + @DauNhay  + CONVERT(nvarchar(50),@DmBannerREF) + @DauNhay + ') B 
		--		ON B.ThucChayID = A.ThucChayID
		--	WHERE 1 = 1
		--		AND B.DanhsachDmBookingREF <> ' + @DauNhay + @DauNhay + '
		--		--AND B.DanhsachDmBookingREF > 0 
		--	'
		--	SET @sql += @FilterString + '
		--	ORDER BY B.DanhsachDmBookingREF ASC'
		--END
		
		
		
		print @sql;
		exec(@sql);
	END
	
END

```
