# Stored Procedure: `sp_TC_CheckHopDongCoThayDoi_DonViGoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-04-08 10:03:31.630000
- **Ngày sửa cuối**: 2021-06-14 15:43:07.363000

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

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongCoThayDoi_DonViGoi] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(100),
	@DmSanPhamREF INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ChietKhauBF FLOAT, @ChietKhau FLOAT, @ThanhTienBF FLOAT, @ThanhTien FLOAT, @StartDate DATETIME, @EndDate DATETIME
	DECLARE @NgayThayDoiMax DATETIME
		
	DECLARE @SoLuongThucChay FLOAT

	SET @ThanhTienBF = 0
	SET @ThanhTien = 0

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
			@Thanhtien = hdct.ThanhTien
			, @ChietKhau = hdct.ChietKhau
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
			@ThanhTien = A.ThanhTien
			, @ChietKhau = A.ChietKhau
			FROM dbo.HopDongChiTietThayDoi A
			INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
			WHERE A.DeletedStatus <> 1 AND B.DeletedStatus <> 1 
			AND a.HopDongChiTietREF <> 0 AND A.HopDongChiTietREF = @HopDongChiTietID 
			AND	convert(date,B.NgayThayDoi) = @NgayThayDoiMax
			Order by A.HopDongChiTietThayDoiID desc

	END

	set @ThanhTien = ISNULL(@ThanhTien,0)
	SET @ChietKhau = ISNULL(@ChietKhau,0)

	--GET DONGIA VA CHIETKHAU TRUOC NGAY HIEN TAI
	SELECT  TOP (1) 
	@ChietKhauBF = ISNULL(tcdt.ChietKhau,0),
	@ThanhTienBf = ISNULL(tcdt.ThanhTien,0) 
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) < @NgayThucHien
	AND tcdt.HopDongID = @HopDongREF
	AND tcdt.DmSanPhamREF = tcdt.DmSanPhamREF
	AND dbo.FormatString(TCDT.HopDongChiTietREF) = @HopDongChiTietID
	ORDER BY tcdt.NgayThucHien desc

	SET @ChietKhauBF = ISNULL(@ChietKhauBF,0)
	SET @ThanhTienBf = ISNULL(@ThanhTienBf,0)

	--TINH SO LUONG THUC CHAY
	SELECT @SoLuongThucChay = ISNULL(sum(tcdt.SoLuongThucChay),0) + SUM(ISNULL(tcdt.SoLuongThayDoi,0)) 
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien
	AND tcdt.HopDongID = @HopDongREF
	AND tcdt.DmSanPhamREF = @DmSanPhamREF
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	AND tcdt.DotChayHopDong = N'CPM_DonViGoi'

	SELECT @StartDate = MIN(tc.NgayThucHien),
	@EndDate = MAX(tc.NgayThucHien) 
	FROM dbo.ThucChay tc
	where  tc.SoHopDong = @SoHopDong
	AND tc.DmSanPhamREF = @DmSanPhamReF

	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
	SET @StartDate = ISNULL(@StartDate,@NgayThayDoiMax)
	SET @EndDate = ISNULL(@EndDate,@NgayThayDoiMax)
	

	IF(
		((@ThanhTien <> @ThanhTienBf)OR (@ChietKhau <> @ChietKhauBF)) 
		AND (@SoLuongThucChay > 0)
	)
	BEGIN
		--TH CO THAY DOI VE GIA TRI, THUC HIEN DOI TRU DI VA TINH LAI
		EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi] 
		@StartDate = @StartDate,
		@EndDate = @NgayThucHien,
		@pSoHopDong = @SoHopDong,
		@pHopDongChiTietREF = @HopDongChiTietID,
		@pDmSanPhamREF = @DmSanPhamREF,
		@pNgayGhiNhanThucChay = @NgayThucHien
	END
	ELSE
	BEGIN
			PRINT 'HD Khong thay doi Chiet khau hoac ThanhTien'
	END
	
	
END

```
