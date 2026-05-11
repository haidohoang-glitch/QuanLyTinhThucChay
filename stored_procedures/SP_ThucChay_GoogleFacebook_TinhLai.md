# Stored Procedure: `ThucChay_GoogleFacebook_TinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-04 13:46:33.613000
- **Ngày sửa cuối**: 2017-10-07 09:36:26.637000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pNgayThucHien` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChay_GoogleFacebook_TinhLai] '2016-03-18'
CREATE PROCEDURE [dbo].[ThucChay_GoogleFacebook_TinhLai]
	-- Add the parameters for the stored procedure here
	@pNgayThucHien DATETIME,
	@pSoHopDong NVARCHAR(50)
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @check INT 
	DECLARE @SoHopDong NVARCHAR(50),@DmSanPhamREF NVARCHAR(50),@SoLuongThucChay INT, @ThanhTienThucChay FLOAT, @DonViTinh NVARCHAR(50), @DmLoaiBannerREF  INT ,@NhanHopDong NVARCHAR(500), @NgayThucHien DATETIME
    -- Insert statements for procedure here
	DECLARE db_cursor CURSOR FOR  
	SELECT DISTINCT A.SoHopDong,
				A.DmSanPhamREF,
				A.DonViTinh,
				A.SoLuongThucChay,
				A.ThanhTienThucChay,
				A.DmLoaiBannerREF,
				A.NhanHopDong ,
				A.NgayThucHien
	FROM dbo.ThucChayGGFBInput A
		INNER JOIN (
		SELECT MAX(NgayThucHien) NgayThucHien, SoHopDong FROM dbo.ThucChayGGFBInput
		GROUP BY SoHopDong) B ON A.NgayThucHien = B.NgayThucHien AND A.SoHopDong = B.SoHopDong
		WHERE A.SoHopDong = @pSoHopDong

	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @SoHopDong,@DmSanPhamREF,@DonViTinh,@SoLuongThucChay,@ThanhTienThucChay   ,@DmLoaiBannerREF,@NhanHopDong, @NgayThucHien

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
	PRINT (@SoHopDong)
	PRINT(@DmSanPhamREF)
	PRINT(@DonViTinh)
	PRINT(@DmLoaiBannerREF)
	SET @check = (SELECT dbo.fn_CheckTienGoogleFacebook_Doannv(@SoHopDong,@DmSanPhamREF,@NgayThucHien,@DmLoaiBannerREF,@DonViTinh))	  
	PRINT (@SoHopDong)
	PRINT(@DmSanPhamREF)
	PRINT(@DonViTinh)
	PRINT(@DmLoaiBannerREF)
	PRINT(@check)
	IF(@check = 1)
	    EXEC [dbo].[ThucChay_GoogleFacebookInsert_TinhLai] @pNgayThucHien,@SoHopDong,@DmSanPhamREF, @SoLuongThucChay, @ThanhTienThucChay,@DonViTinh,@DmLoaiBannerREF,@NhanHopDong
	IF(@check = 2)
		EXEC [dbo].[ThucChay_GoogleFacebookInsertGTTD_TinhLai] @pNgayThucHien,@SoHopDong,@DmSanPhamREF, @SoLuongThucChay, @ThanhTienThucChay,@DonViTinh,@DmLoaiBannerREF,@NhanHopDong
	IF(@check = 3)
		EXEC [dbo].[ThucChay_GoogleFacebookInsertGTTD3_TinhLai] @pNgayThucHien,@SoHopDong,@DmSanPhamREF, @SoLuongThucChay, @ThanhTienThucChay,@DonViTinh,@DmLoaiBannerREF,@NhanHopDong
	IF(@check = 4)
		EXEC [dbo].[ThucChay_GoogleFacebookInsertGTTD4_TinhLai] @pNgayThucHien,@SoHopDong,@DmSanPhamREF, @SoLuongThucChay, @ThanhTienThucChay,@DonViTinh,@DmLoaiBannerREF,@NhanHopDong
	FETCH NEXT FROM db_cursor INTO @SoHopDong,@DmSanPhamREF,@DonViTinh,@SoLuongThucChay,@ThanhTienThucChay  ,@DmLoaiBannerREF  ,@NhanHopDong, @NgayThucHien
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
END


--SELECT * FROM HopDongChiTiet hdct WHERE hdct.HopDongFK= 34882

```
