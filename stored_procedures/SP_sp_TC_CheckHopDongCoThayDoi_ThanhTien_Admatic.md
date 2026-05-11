# Stored Procedure: `sp_TC_CheckHopDongCoThayDoi_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-06-23 11:48:41.023000
- **Ngày sửa cuối**: 2021-06-22 16:26:48.403000

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
/*
EXEC [dbo].[sp_TC_CheckHopDongCoThayDoi_ThanhTien_Admatic] 
	-- Add the parameters for the stored procedure here
	@HopDongREF = 1032437,
	@SoHopDong = N'QC5440421',
	@DmSanPhamREF = 342,
	@HopDongChiTietID = 618692,
	@NgayThucHien ='2021-05-18'
*/

CREATE  PROCEDURE [dbo].[sp_TC_CheckHopDongCoThayDoi_ThanhTien_Admatic] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(100),
	@DmSanPhamREF INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ChietKhauBF FLOAT, @ChietKhau FLOAT, @DonGiaBF FLOAT, @DonGia FLOAT, @StartDate DATETIME, @EndDate DATETIME,
	@ThanhTienHDBF FLOAT, @ThanhTienHD FLOAT
	DECLARE @NgayThayDoiMax DATETIME, @SoLuongHD INT, @SoLuongHDBF INT
	
	DECLARE @SoLuongThucChay FLOAT

	SET @SoLuongHD = 0
	SET @SoLuongHDBF = 0
	SET @ThanhTienHD = 0
	SET @ThanhTienHDBF = 0

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
			@DonGia = hdct.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
			, @ChietKhau = hdct.ChietKhau
			, @SoLuongHD = hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
			, @ThanhTienHD = hdct.ThanhTien
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
			@DonGia = A.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(A.DonViTinh)
			, @ChietKhau = A.ChietKhau
			, @SoLuongHD = A.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(A.DonViTinh)
			, @ThanhTienHD = A.ThanhTien
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
	SET @ThanhTienHD = ISNULL(@ThanhTienHD,0)

	--GET DONGIA VA CHIETKHAU TRUOC NGAY HIEN TAI
	SELECT  TOP (1) @ChietKhauBF = ISNULL(tcdt.ChietKhau,0),
					@SoLuongHDBF = ISNULL(tcdt.SoLuong,0) ,
					@ThanhTienHDBF = ISNULL(tcdt.ThanhTien,0)
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) < @NgayThucHien
	AND tcdt.HopDongID = @HopDongREF
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID
	ORDER BY tcdt.NgayThucHien desc

	SET @ChietKhauBF = ISNULL(@ChietKhauBF,0)
	SET @SoLuongHDBF = ISNULL(@SoLuongHDBF,0)
	SET @ThanhTienHDBF = ISNULL(@ThanhTienHDBF,0)

	--TINH SO LUONG THUC CHAY
	SELECT @SoLuongThucChay = ISNULL(sum(tcdt.SoLuongThucChay),0) + SUM(ISNULL(tcdt.SoLuongThayDoi,0)) 
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien
	AND tcdt.HopDongID = @HopDongREF
	AND tcdt.HopDongChiTietREF = @HopDongChiTietID

	--lay thong tin max, min
	SELECT 
		@StartDate = MIN(tc.NgayThucHien),
		@EndDate = MAX(tc.NgayThucHien)
	 FROM dbo.ThucChay_ThanhTien_Admatic tc
	WHERE tc.SoHopDong = @SoHopDong
	--AND tc.DmSanPhamREF = @DmSanPhamREF --HAIDH COMMENT 2021-06-22 DO admatic danh so san pham "nhieu san pham "- 733

	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
	SET @StartDate = ISNULL(@StartDate,@NgayThayDoiMax)
	SET @EndDate = ISNULL(@EndDate,@NgayThayDoiMax)
	
	--TRUONG HOP HD THAY DOI SO LUONG(SOLUONG HIEN TAI NHO HON SO LUONG BAN DAU
	--TRUONG HOP SO LUONG HD HIEN TAI > SO LUONG HD TRUOC DO CHUA LAM DC

	IF(
		((@ThanhTienHD <> @ThanhTienHDBF) AND (@ChietKhau <> 100))
		AND (@SoLuongThucChay > 0)
	)
	BEGIN
		--TH CO THAY DOI VE GIA TRI, THUC HIEN DOI TRU DI VA TINH LAI
		
		EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic] 
		@pSoHopDong = @SoHopDong,
		@pHopDongChiTietID = @HopDongChiTietID,
		@pDmSanPhamREF = @DmSanPhamREF,
		@pStartDate = @StartDate,
		@pEndDate = @NgayThucHien,
		@pNgayGhiNhanThucChay = @NgayThucHien
	END
	else
		print 'khong phai lam gi'
	
	
END

```
