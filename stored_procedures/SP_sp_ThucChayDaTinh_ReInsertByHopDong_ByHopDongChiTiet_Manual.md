# Stored Procedure: `sp_ThucChayDaTinh_ReInsertByHopDong_ByHopDongChiTiet_Manual`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-07 10:18:30.140000
- **Ngày sửa cuối**: 2017-01-07 10:45:30.937000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@i_HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_ByHopDongChiTiet_Manual] '2016-12-31',12345
CREATE PROCEDURE [dbo].[sp_ThucChayDaTinh_ReInsertByHopDong_ByHopDongChiTiet_Manual]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME	, 
	@i_HopDongChiTietID INT

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    declare 
	@HopDongID INT,
	@HopDongChiTietID INT,
	@SoHopDong_new NVARCHAR(50),
	@NgayDanhSo_new DATETIME,
	@DmNhanVienREF_new INT,
	@DmKhachHangREF_new NVARCHAR(200),
	@DmSanPhamREF_new INT,
	@DsNhanHangREF_new NVARCHAR(200),
	@HinhThucQuangCaoREF_new INT, @TenDangNhap_new NVARCHAR(50),
	@MaSoHopDong_new INT , @Note NVARCHAR(50), @IsThayDoi INT,@GiaTriThucChay FLOAT,@GiaTriThucChayAd FLOAT, @IsExistData INT ,@IsExistData1 INT  ;
	DECLARE @out NVARCHAR(2000);

    DECLARE db_cursor CURSOR FOR  
	SELECT DISTINCT
		hd.HopDongID,
		hdct.HopDongChiTietID,
		hd.SoHopDong,
		hd.NgayDanhSoHopDong,
		hd.SysNhanVienREF, 
		hd.TenKhachHang,
		hdct.DmSanPhamREF,
		hdct.DanhSachNhanHangREF,
		hdct.DmLoaiREF,
		hd.DmMaHopDongREF,
		hd.TenDangNhap
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
	WHERE 1=1
	AND hdct.HopDongChiTietID = @i_HopDongChiTietID
	
	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @HopDongID,
	@HopDongChiTietID ,
	@SoHopDong_new ,
	@NgayDanhSo_new ,
	@DmNhanVienREF_new ,
	@DmKhachHangREF_new ,
	@DmSanPhamREF_new ,
	@DsNhanHangREF_new ,
	@HinhThucQuangCaoREF_new ,
	@MaSoHopDong_new ,
	@TenDangNhap_new

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		

		SELECT @GiaTriThucChay = SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID AND tcdt.NgayThucHien < @NgayThucHien

		SET @GiaTriThucChay = isnull(ROUND(@GiaTriThucChay,0),0)
		SET @GiaTriThucChayAd = isnull(ROUND(@GiaTriThucChayAd,0),0)
		SET @IsThayDoi = 3
		if @IsThayDoi = 3 SET @Note = 'TDNH_2016 THAY DOI DANH SACH NHAN HANG'

		EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Manual]
				-- Add the parameters for the stored procedure here
				@NgayThucHien ,
				@HopDongID ,
				@HopDongChiTietID ,
				@SoHopDong_new ,
				@NgayDanhSo_new ,
				@DmNhanVienREF_new ,
				@DmKhachHangREF_new ,
				@DmSanPhamREF_new ,
				@DsNhanHangREF_new ,
				@HinhThucQuangCaoREF_new , 
				@TenDangNhap_new ,
				@MaSoHopDong_new  , 
				@Note , 
				@IsThayDoi ,
				@GiaTriThucChay ,
				@GiaTriThucChayAd ,
				@IsExistData  ,
				@IsExistData1   
		

	FETCH NEXT FROM db_cursor INTO @HopDongID,
	@HopDongChiTietID ,
	@SoHopDong_new ,
	@NgayDanhSo_new ,
	@DmNhanVienREF_new ,
	@DmKhachHangREF_new ,
	@DmSanPhamREF_new ,
	@DsNhanHangREF_new ,
	@HinhThucQuangCaoREF_new ,
	@MaSoHopDong_new  ,
	@TenDangNhap_new  
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
	
END



```
