# Stored Procedure: `sp_TC_CheckHopDongCoThayDoi_DonViBai_ThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-07 11:38:18.283000
- **Ngày sửa cuối**: 2023-05-29 16:13:35.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
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
--EXEC [sp_TC_CheckHopDongCoThayDoi_TRUEVIEW] 26325,'SH020614',370,59116,'2014-06-12'

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongCoThayDoi_DonViBai_ThucTreo] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(100),
	@DmSanPhamREF INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ChietKhauBF FLOAT, @ChietKhau FLOAT, @DonGiaBF FLOAT, @DonGia FLOAT, @StartDate DATETIME, @EndDate DATETIME
	DECLARE @NgayThayDoiMax DATETIME, @SoLuongHD INT, @SoLuongHDBF INT
	, @ThanhTien FLOAT, @ThanhTienBF FLOAT
	
	DECLARE @SoLuongThucChay FLOAT

	SET @SoLuongHD = 0
	SET @SoLuongHDBF = 0

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
			SELECT Top (1 )
			@DonGia = hdct.DonGia
			, @ChietKhau = hdct.ChietKhau
			, @SoLuongHD = hdct.SoLuong
			, @ThanhTien = hdct.ThanhTien
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
			@DonGia = A.DonGia
			, @ChietKhau = A.ChietKhau
			, @SoLuongHD = A.SoLuong
			, @ThanhTien = A.ThanhTien
			FROM dbo.HopDongChiTietThayDoi A
			INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
			WHERE A.DeletedStatus <> 1 AND B.DeletedStatus <> 1 
			AND a.HopDongChiTietREF <> 0 AND A.HopDongChiTietREF = @HopDongChiTietID 
			AND	convert(date,B.NgayThayDoi) = @NgayThayDoiMax
			Order by A.HopDongChiTietThayDoiID desc

	END
	set @DonGia = ISNULL(@DonGia,0)
	SET @ChietKhau = ISNULL(@ChietKhau,0)
	SET @SoLuongHD = ISNULL(@SoLuongHD,0)
	SET @ThanhTien = ISNULL(@ThanhTien,0)
	--GET DONGIA VA CHIETKHAU TRUOC NGAY HIEN TAI
	SELECT  TOP (1) 
	@ChietKhauBF = ISNULL(tcdt.ChietKhau,0),
	@SoLuongHDBF = ISNULL(tcdt.SoLuong,0) ,
	@ThanhTienBF = ISNULL(tcdt.thanhtien,0)
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) < @NgayThucHien
	AND tcdt.HopDongID = @HopDongREF
	AND tcdt.DmSanPhamREF = tcdt.DmSanPhamREF
	AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
	ORDER BY tcdt.NgayThucHien desc

	SET @ChietKhauBF = ISNULL(@ChietKhauBF,0)
	SET @SoLuongHDBF = ISNULL(@SoLuongHDBF,0)

	--TINH SO LUONG THUC CHAY
	SELECT @SoLuongThucChay = ISNULL(sum(tcdt.SoLuongThucChay),0) + SUM(ISNULL(tcdt.SoLuongThayDoi,0)) ,
	@StartDate = MIN(tcdt.NgayThucHien),
	@EndDate = MAX(tcdt.NgayThucHien)
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien
	AND tcdt.HopDongID = @HopDongREF
	AND tcdt.DmSanPhamREF = @DmSanPhamREF
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	AND tcdt.DotChayHopDong = N'CPM_DonViBai'

	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
	SET @StartDate = ISNULL(@StartDate,@NgayThayDoiMax)
	SET @EndDate = ISNULL(@EndDate,@NgayThayDoiMax)
	
	--TRUONG HOP HD THAY DOI SO LUONG(SOLUONG HIEN TAI NHO HON SO LUONG BAN DAU
	--TRUONG HOP SO LUONG HD HIEN TAI > SO LUONG HD TRUOC DO CHUA LAM DC
	IF(
		((@SoLuongHD <> @SoLuongHDBF)OR (@ChietKhau <> @ChietKhauBF) OR (@ThanhTien <> @ThanhTienBF)) 
		AND (@SoLuongThucChay > 0)
	)
	BEGIN
		--TH CO THAY DOI VE GIA TRI, THUC HIEN DOI TRU DI VA TINH LAI
		EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViBai_ThucTreo] 
		@pSoHopDong = @SoHopDong,
		@pHopDongChiTietREF = @HopDongChiTietID,
		@pDmSanPhamREF = @DmSanPhamREF,
		@pNgayThucHien = @NgayThucHien,
		@pNgayGhiNhanThucChay = @NgayThucHien
	END
	ELSE
	BEGIN
			PRINT 'HD Khong thay doi so luong'
	END
	
	
END

```
