# Function: `fn_ThucChay_CheckHopDongThayDoi_noidungthaydoi`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-11-03 11:50:38.133000
- **Ngày sửa cuối**: 2022-07-20 10:04:11.217000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@SoHopDong_new` | `nvarchar(100)` | No |
| `@NgayDanhSo_new` | `datetime(8)` | No |
| `@DmNhanVienREF_new` | `int(4)` | No |
| `@TenKhachHang_new` | `nvarchar(400)` | No |
| `@DmSanPhamREF_new` | `int(4)` | No |
| `@DsTenNhanHang_new` | `nvarchar(400)` | No |
| `@HinhThucQuangCaoREF_new` | `int(4)` | No |
| `@MaSoHopDong_new` | `int(4)` | No |
| `@TenDangNhap_new` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[fn_ThucChay_CheckHopDongThayDoi_noidungthaydoi]
(
	-- Add the parameters for the function here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT,
	@SoHopDong_new NVARCHAR(50),
	@NgayDanhSo_new DATETIME,
	@DmNhanVienREF_new INT,
	@TenKhachHang_new NVARCHAR(200),
	@DmSanPhamREF_new INT,
	@DsTenNhanHang_new NVARCHAR(200),
	@HinhThucQuangCaoREF_new INT,
	@MaSoHopDong_new INT,
	@TenDangNhap_new NVARCHAR(50)
)
RETURNS NVARCHAR(MAX) 
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultVar NVARCHAR(max) , @DmLoaiBannerREFNew INT, @NoiDungThayDoi NVARCHAR(max) = ''
	-- declare loai banner 
	--DECLARE DmLoaiBannerREF
	-- Add the T-SQL statements to compute the return value here
	declare @SoHopDong_old NVARCHAR(50),
	@NgayDanhSo_old DATETIME,
	@DmNhanVienREF_old INT,
	@TenKhachHang_old NVARCHAR(200),
	@DmSanPhamREF_old INT,
	@DsTenNhanHang_old NVARCHAR(200),
	@HinhThucQuangCaoREF_old INT,
	@MaSoHopDong_old INT,
	@TenDangNhap_old NVARCHAR(50),
	@TrangThaiHopDong INT 
	SELECT  @TrangThaiHopDong = hd.TrangThaiHopDong
	  FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID
	

	SET @DmLoaiBannerREFNew =
	ISNULL((
	SELECT 
		hdct.DmLoaiBannerREF
	FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	),0)

	set @SoHopDong_old =''
	set @NgayDanhSo_old ='2010-01-01'
	set @DmNhanVienREF_old = 0
	set @TenKhachHang_old =''
	set @DmSanPhamREF_old =0
	set @DsTenNhanHang_old =''
	set @HinhThucQuangCaoREF_old =0
	set @MaSoHopDong_old =0
	SET @TenDangNhap_old = '';

-------------------------------------------------------------------------------------------------------
	IF (EXISTS(SELECT TOP (1) HopDongChiTietREF FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF = @HopDongChiTietID ORDER BY HopDongChiTietREF) )
	BEGIN
		SELECT TOP 1 
		@SoHopDong_old = dskcr.SoHopDong,
		--@NgayDanhSo_old = dskcr.NgayDanhSoHopDong,
		@TenKhachHang_old = dskcr.TenKhachHang,
		@DmNhanVienREF_old = dskcr.SysNhanVienREF,
		@DmSanPhamREF_old = dskcr.DmSanPhamREF,
		@HinhThucQuangCaoREF_old = dskcr.DmHinhThucQuangCao,
		@MaSoHopDong_old = dskcr.DmMaHopDongREF,
		@DsTenNhanHang_old = dskcr.NhanHang,
		@TenDangNhap_old = dskcr.TenDangNhap
		FROM dbo.ThucChayDaTinh dskcr 
		WHERE dskcr.NgayThucHien < @NgayThucHien
		AND dskcr.HopDongID = @HopDongID
		AND dskcr.HopDongChiTietREF = @HopDongChiTietID

	ORDER BY dskcr.NgayThucHien DESC, dskcr.LastModifiedAt DESC
	END
	IF (EXISTS(SELECT TOP (1) HopDongChiTietREF FROM ThucChayDaTinhAdmarket WHERE HopDongChiTietREF = @HopDongChiTietID ORDER BY HopDongChiTietREF))
	BEGIN
		SELECT TOP 1 
		@SoHopDong_old = dskcr.SoHopDong,
		--@NgayDanhSo_old = dskcr.NgayDanhSoHopDong,
		@TenKhachHang_old = dskcr.TenKhachHang,
		@DmNhanVienREF_old = dskcr.SysNhanVienREF,
		@DmSanPhamREF_old = dskcr.DmSanPhamREF,
		@HinhThucQuangCaoREF_old = dskcr.DmHinhThucQuangCao,
		@MaSoHopDong_old = dskcr.DmMaHopDongREF,
		@DsTenNhanHang_old = dskcr.NhanHang,
		@TenDangNhap_old = dskcr.TenDangNhap
		FROM dbo.ThucChayDaTinhAdmarket dskcr 
		WHERE dskcr.NgayThucHien < @NgayThucHien
		AND dskcr.HopDongID = @HopDongID
		AND dskcr.HopDongChiTietREF = @HopDongChiTietID
	ORDER BY dskcr.NgayThucHien DESC, dskcr.LastModifiedAt DESC
	END
	-- Return the result of the function
	
	-----Thay doi so hop Dong-----
	SET @NoiDungThayDoi =
	(
	CASE WHEN @SoHopDong_new <> @SoHopDong_old 
				THEN  @NoiDungThayDoi + ' SoHopDong: ' + @SoHopDong_old + ' -> ' + @SoHopDong_new
			--WHEN @NgayDanhSo_new <> @NgayDanhSo_old 
			--	THEN  @NoiDungThayDoi +' NgayDanhSo: ' + CONVERT(nvarchar(50),@NgayDanhSo_old,120) + ' -> ' + CONVERT(nvarchar(50),@NgayDanhSo_new,120)
			WHEN @DmNhanVienREF_new <> @DmNhanVienREF_old 
				THEN @NoiDungThayDoi + ' DmNhanVienREF: ' + CONVERT(nvarchar(50),@DmNhanVienREF_old) + ' -> ' + CONVERT(nvarchar(50),@DmNhanVienREF_new)
			--WHEN @TenKhachHang_new <> @TenKhachHang_old 
			--	THEN  @NoiDungThayDoi + ' TenKhachHang: ' + @TenKhachHang_old + ' -> ' + @TenKhachHang_new
			WHEN ((@DmSanPhamREF_new <> @DmSanPhamREF_old) AND (@DmSanPhamREF_new <> 733 AND @DmSanPhamREF_old <> 733))--Haidh comment 20/07/2022 loai sp nhieu san pham
				THEN  @NoiDungThayDoi + ' DmSanPhamREF: ' + CONVERT(nvarchar(50),@DmSanPhamREF_old) + ' -> ' + CONVERT(nvarchar(50),@DmSanPhamREF_new)
			WHEN @HinhThucQuangCaoREF_new <> @HinhThucQuangCaoREF_old 
				THEN  @NoiDungThayDoi + ' HinhThucQuangCao: ' + CONVERT(nvarchar(50),@HinhThucQuangCaoREF_old) + ' -> ' + CONVERT(nvarchar(50),@HinhThucQuangCaoREF_new)
			WHEN @MaSoHopDong_new <> @MaSoHopDong_old 
				THEN  @NoiDungThayDoi +' MaSoHopDong: ' + CONVERT(nvarchar(50),@MaSoHopDong_old) + ' -> ' + CONVERT(nvarchar(50),@MaSoHopDong_new)
			WHEN @TenDangNhap_new <> @TenDangNhap_old 
				THEN  @NoiDungThayDoi +' TenDangNhap: ' + @TenDangNhap_old+ ' -> ' + @TenDangNhap_new
		ELSE ''
	END
	)

	IF  @SoHopDong_new <> @SoHopDong_old
		--OR @NgayDanhSo_new <> @NgayDanhSo_old
		OR @DmNhanVienREF_new <> @DmNhanVienREF_old
		--OR @TenKhachHang_new <> @TenKhachHang_old
		OR ((@DmSanPhamREF_new <> @DmSanPhamREF_old) AND (@DmSanPhamREF_new <> 733 AND @DmSanPhamREF_old <> 733))
		--or @DsTenNhanHang_new <> @DsTenNhanHang_old 
		OR @HinhThucQuangCaoREF_new <> @HinhThucQuangCaoREF_old
		OR @MaSoHopDong_new <> @MaSoHopDong_old
		OR @TenDangNhap_new <> @TenDangNhap_old

	Begin SET @ResultVar = 1 END 
	-----Phan bo bi xoa-----
	IF (EXISTS(SELECT TOP (1) HopDongChiTietID FROM dbo.HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID AND hdct.DeletedStatus =1 Order by HopDongChiTietID))
	SET @NoiDungThayDoi= 'HopDongChiTietID: ' + CONVERT(NVARCHAR(50),@HopDongChiTietID) + ' Bi xoa'
	--- Thay doi nhan hang voi nhung san pham lay thong tin thuc chay tren hop dong
	IF ((@DmSanPhamREF_new IN (375,420,423,624,688)) OR(@HinhThucQuangCaoREF_new = 13 OR @DmLoaiBannerREFNew = 18)) and (@DsTenNhanHang_new <> @DsTenNhanHang_old)
		SET @NoiDungThayDoi= ' NhanHang: ' + @DsTenNhanHang_old + ' -> ' + @DsTenNhanHang_new
	IF @TrangThaiHopDong = 3
		SET @NoiDungThayDoi= ' HopDong: ' + CONVERT(NVARCHAR(50),@HopDongID) + ' Bi huy'
	
	SET @ResultVar = ISNULL(@NoiDungThayDoi,'')
	RETURN @ResultVar

END


```
