# Function: `fn_ThucChay_CheckHopDongThayDoi_bk20160930`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-09-30 13:34:24.400000
- **Ngày sửa cuối**: 2016-09-30 13:34:24.400000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
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
CREATE FUNCTION [dbo].[fn_ThucChay_CheckHopDongThayDoi_bk20160930]
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
RETURNS INT 
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultVar INT 
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
	  FROM HopDong hd WHERE hd.HopDongID = @HopDongID
	

	set @SoHopDong_old =''
	set @NgayDanhSo_old ='2010-01-01'
	set @DmNhanVienREF_old = 0
	set @TenKhachHang_old =''
	set @DmSanPhamREF_old =0
	set @DsTenNhanHang_old =''
	set @HinhThucQuangCaoREF_old =0
	set @MaSoHopDong_old =0
	SET @TenDangNhap_old = '';
--------------------------------------- Nhan hang thay doi ----------------------------------------------------------------
		DECLARE @out NVARCHAR(2000);

		 SELECT @out = COALESCE(@out + ',', '') + ISNULL(CAST(T.DmNhanHangREF AS VARCHAR(1000)),'')
		 FROM   (
					SELECT DISTINCT DmNhanHangREF FROM dbo.ThucChayHopDongChiTiet
					WHERE  1=1
					AND HopDongChiTietREF = @HopDongChiTietID AND DeletedStatus = 0
				) T         
 
		 SET @out = ISNULL(@out,'');


	IF @DmSanPhamREF_new IN (342,240,339,598,613,370,140,549,228)  
		SET @DsTenNhanHang_new = @out
	ELSE 
		SET @DsTenNhanHang_new = @DsTenNhanHang_new
-------------------------------------------------------------------------------------------------------
	IF (SELECT count(*) FROM ThucChayDaTinh WHERE HopDongChiTietREF = @HopDongChiTietID) > 0
	BEGIN
		SELECT TOP 1 
		@SoHopDong_old = dskcr.SoHopDong,
		@NgayDanhSo_old = dskcr.NgayDanhSoHopDong,
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
		--AND @SoHopDong_new <> dskcr.SoHopDong
		--AND @NgayDanhSo_new <> dskcr.NgayDanhSoHopDong
		--AND @DmNhanVienREF_new <> dskcr.SysNhanVienREF
		--AND @TenKhachHang_new <> dskcr.TenKhachHang
		--AND @DmSanPhamREF_new <> dskcr.DmSanPhamREF
		----AND @DsTenNhanHang_new <> @DsTenNhanHang_old
		--AND @HinhThucQuangCaoREF_new <> dskcr.DmHinhThucQuangCao
		--AND @MaSoHopDong_new <> dskcr.DmMaHopDongREF
		--AND @TenDangNhap_new <> dskcr.TenDangNhap
	ORDER BY dskcr.NgayThucHien DESC
	END
	IF (SELECT count(*) FROM ThucChayDaTinhAdmarket WHERE HopDongChiTietREF = @HopDongChiTietID) > 0
	BEGIN
		SELECT TOP 1 
		@SoHopDong_old = dskcr.SoHopDong,
		@NgayDanhSo_old = dskcr.NgayDanhSoHopDong,
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
	ORDER BY dskcr.NgayThucHien DESC
	END
	-- Return the result of the function
	
	-----Thay doi so hop Dong-----
	IF  @SoHopDong_new <> @SoHopDong_old
		OR @NgayDanhSo_new <> @NgayDanhSo_old
		OR @DmNhanVienREF_new <> @DmNhanVienREF_old
		OR @TenKhachHang_new <> @TenKhachHang_old
		OR @DmSanPhamREF_new <> @DmSanPhamREF_old
		or @DsTenNhanHang_new <> @DsTenNhanHang_old 
		OR @HinhThucQuangCaoREF_new <> @HinhThucQuangCaoREF_old
		OR @MaSoHopDong_new <> @MaSoHopDong_old
		OR @TenDangNhap_new <> @TenDangNhap_old
	Begin SET @ResultVar = 1 END 
	-----Phan bo bi xoa-----
	IF (SELECT COUNT(*) FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = @HopDongChiTietID AND hdct.DeletedStatus =1) > 0
	SET @ResultVar = 2
	--- Thay doi nhan hang
	--IF (@DmSanPhamREF_new IN (375,420,423,624,688)) and (@DsTenNhanHang_new <> @DsTenNhanHang_old)
	IF @DsTenNhanHang_new <> @DsTenNhanHang_old
	SET @ResultVar = 3 
	IF @TrangThaiHopDong = 3
	SET @ResultVar = 4
	
	SET @ResultVar = ISNULL(@ResultVar,0)
	RETURN @ResultVar

END


```
