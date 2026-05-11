# Stored Procedure: `sp_TC_CheckHopDongCoThayDoi_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 16:31:46.070000
- **Ngày sửa cuối**: 2024-09-26 15:18:32.520000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_CheckHopDongCoThayDoi_CPM] 26325,'SH020614',370,59116,'2014-06-12'

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongCoThayDoi_CPM] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ChietKhauBF FLOAT, @ChietKhau FLOAT, @DonGia FLOAT, @HopDongChiTietThayDoiGia INT, @HopDongChiTietThayDoiCK INT
	DECLARE @NgayThayDoiMax DATETIME, @SoLuongHD INT, @SoLuongHDBF INT

	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500)
	DECLARE @DonGiaLienKeTruoc FLOAT, @SoLuongThucChay FLOAT
	DECLARE @count_HDCT INT
	

	SET @CONTENT_LOG = CONVERT(NVARCHAR(20),@HopDongChiTietID) + ': ' 
	SET @NGUON_LOG = N'sp_TC_CheckHopDongCoThayDoi_CPM :'
	SET @HopDongChiTietThayDoiGia = 0
	SET @HopDongChiTietThayDoiCK = 0
	SET @SoLuongHD = 0
	SET @SoLuongHDBF = 0
	
	--GET DONGIA VA CHIETKHAU HIEN TAI
	SET @NgayThayDoiMax = 
	(
		SELECT convert(date,MAX(B.NgayThayDoi))
		FROM dbo.HopDongChiTietThayDoi A
		INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
		WHERE 
		A.DeletedStatus <> 1 AND 
		B.DeletedStatus <> 1 AND
		A.HopDongChiTietREF = @HopDongChiTietID
	)
	SET @NgayThayDoiMax = ISNULL(@NgayThayDoiMax,@NgayThucHien)
	IF(@NgayThucHien >= @NgayThayDoiMax)
	BEGIN
			SELECT Top (1)
			@DonGia = hdct.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
			, @ChietKhau = hdct.ChietKhau
			, @SoLuongHD = hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
			FROM dbo.HopDongChiTiet hdct
			WHERE hdct.DeletedStatus <> 1 AND 
			hdct.HopDongChiTietID = @HopDongChiTietID 
			ORDER BY hdct.HopDongChiTietID
	END
	ELSE
	BEGIN
		SET @NgayThayDoiMax = 
		(
			SELECT Top (1) Convert(date,b.NgayThayDoi)
			FROM dbo.HopDongChiTietThayDoi A
			INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
			WHERE 
			A.DeletedStatus <> 1 AND B.DeletedStatus <> 1 AND
			A.HopDongChiTietREF = @HopDongChiTietID AND	convert(date,B.NgayThayDoi) >=  @NgayThucHien
			Order by B.NgayThayDoi asc
		)	
		
		SELECT TOP (1) 
			@DonGia = A.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(A.DonViTinh), @ChietKhau = A.ChietKhau, @SoLuongHD = A.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(A.DonViTinh)
			FROM dbo.HopDongChiTietThayDoi A
			INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
			WHERE 
			A.DeletedStatus <> 1 AND B.DeletedStatus <> 1 
			AND a.HopDongChiTietREF <> 0 AND A.HopDongChiTietREF = @HopDongChiTietID 
			AND	convert(date,B.NgayThayDoi) = @NgayThayDoiMax
			Order by A.HopDongChiTietThayDoiID desc

	END
	set @DonGia = ISNULL(@DonGia,0)
	SET @ChietKhau = ISNULL(@ChietKhau,0)
	SET @SoLuongHD = ISNULL(@SoLuongHD,0)

	--GET DONGIA VA CHIETKHAU TRUOC NGAY HIEN TAI
	SELECT  TOP (1) 
	@DonGiaLienKeTruoc  = ISNULL(tcdt.DonGiaTheoDonVi,0),
	@ChietKhauBF = ISNULL(tcdt.ChietKhau,0),
	@SoLuongHDBF = ISNULL(tcdt.SoLuong,0) 
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) < @NgayThucHien
	AND tcdt.HopDongID = @HopDongREF
	AND tcdt.DmSanPhamREF = tcdt.DmSanPhamREF
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	ORDER BY tcdt.NgayThucHien desc

	SET @DonGiaLienKeTruoc = ISNULL(@DonGiaLienKeTruoc,0)
	SET @ChietKhauBF = ISNULL(@ChietKhauBF,0)
	SET @SoLuongHDBF = ISNULL(@SoLuongHDBF,0)
	--TINH SO LUONG THUC CHAY
	SET @SoLuongThucChay = 	(	
		SELECT ISNULL(sum(tcdt.SoLuongThucChay),0) + SUM(ISNULL(tcdt.SoLuongThayDoi,0)) 
		FROM dbo.ThucChayDaTinh tcdt
		WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien
		AND tcdt.HopDongID = @HopDongREF
		AND tcdt.DmSanPhamREF = tcdt.DmSanPhamREF
		AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	)
	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
	--NEU CO THAY DOI VE GIA
	IF(@DonGia <> @DonGiaLienKeTruoc)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi giá:' + CONVERT(NVARCHAR(30),@DonGiaLienKeTruoc) + '->' + CONVERT(NVARCHAR(30),@DonGia) + ');'
		--SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi:'	+ CONVERT(NVARCHAR(50),@HopDongChiTietThayDoiGia)	
	END
	--NEU CO THAY DOI VE CHIET KHAU
	IF(@ChietKhau <> @ChietKhauBF)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi chiết khấu:' + CONVERT(NVARCHAR(30),@ChietKhauBF) + '->' + CONVERT(NVARCHAR(30),@ChietKhau) + ');'
		--SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi: ' + CONVERT(NVARCHAR(30),@HopDongChiTietThayDoiCK)
	END
	--TRUONG HOP HD THAY DOI SO LUONG(SOLUONG HIEN TAI NHO HON SO LUONG BAN DAU
	--TRUONG HOP SO LUONG HD HIEN TAI > SO LUONG HD TRUOC DO CHUA LAM DC

	IF(
		((@SoLuongHD <> @SoLuongHDBF)OR (@ChietKhau <> @ChietKhauBF) OR (@DonGia <> @DonGiaLienKeTruoc)) 
		AND (@SoLuongThucChay > 0)
	)
	BEGIN
		SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi số lượng:' + CONVERT(NVARCHAR(30),@SoLuongHDBF) + '->' + CONVERT(NVARCHAR(30),@SoLuongHD) + ');'
		--HAIDH COMMENT 2024-08-21 THUC HIEN TINH GIA TRI THAY DOI CHO CPM
		EXEC dbo.[sp_TC_UpdateGiaTriTDTCCPMThucTreoByNgayLog] @NgayThucHien ,@HopDongREF ,	@DmSanPhamREF ,	@HopDongChiTietID, @CONTENT_LOG	
	END

	
END

```
