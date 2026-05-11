# Stored Procedure: `sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ThanhTien_Admatic_ByPhanBoID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-07-29 16:50:44.353000
- **Ngày sửa cuối**: 2020-07-29 16:55:51.613000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE  PROCEDURE [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_ThanhTien_Admatic_ByPhanBoID] 
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(100),
	@HopDongID INT,
	@HopDongChiTietID INT, 
    @NgayThucHien DATETIME
AS
    BEGIN
        DECLARE @count_HDCT INT , @SoLuongThucChayBF INT  , @DmSanPhamREF INT  , @StartDate DATETIME, @EndDate DATETIME
		DECLARE @NgayDanhSoGioiHan DATETIME 
		SET @NgayDanhSoGioiHan = '2020-07-20'     

		SELECT TOP (1) @DmSanPhamREF =  hdct.DmSanPhamREF FROM dbo.HopDongDongChiTiet hdct
		WHERE hdct.HopDongChiTietID = @HopDongChiTietID
		ORDER BY hdct.HopDongChiTietID

		SELECT @SoLuongThucChayBF  = SUM(tcdt.SoLuongThucChay),
				@StartDate = MIN(tcdt.NgayThucHien),
				@EndDate = MAX(tcdt.NgayThucHien)
		FROM     dbo.ThucChayDaTinh tcdt
		WHERE    CONVERT(DATE, tcdt.NgayThucHien) < @NgayThucHien
				AND tcdt.HopDongID = @HopDongID
				AND tcdt.HopDongChiTietREF = @HopDongChiTietID
				AND tcdt.DmHinhThucQuangCao = 42
				--AND DmSanPhamREF = @DmSanPhamREF --CHO NAY CAN XEM LAI VI NEU ADMATIC CHAY SAN PHAM NHIEU SAN PHAM
				AND NOT ( tcdt.DmLoaiBannerREF IN (17, 18)OR tcdt.DmHinhThucQuangCao IN (13))
				AND tcdt.DotChayHopDong <> N'NGAY'
										
		SET @count_HDCT = ( SELECT  COUNT(hdct.HopDongChiTietID)
							FROM    dbo.HopDongChiTiet hdct
							WHERE   hdct.HopDongChiTietID = @HopDongChiTietID
									AND hdct.DeletedStatus = 0
									AND hdct.DmLoaiREF = 42
									AND NOT ( hdct.DmLoaiREF IN ( 13) OR hdct.DmLoaiBannerREF = 18 )--Khong update gia tri thay doi cho HTQC Mua Ngoai 
							)	
		IF ( @SoLuongThucChayBF > 0 )
		BEGIN
			IF ( @count_HDCT > 0 )
				--TH CO THAY DOI VE GIA TRI, THUC HIEN DOI TRU DI VA TINH LAI
				EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic] 
				@pSoHopDong = @SoHopDong,
				@pHopDongChiTietID = @HopDongChiTietID,
				@pDmSanPhamREF = @DmSanPhamREF,
				@pStartDate = @StartDate,
				@pEndDate = @EndDate,
				@pNgayGhiNhanThucChay = @NgayThucHien

		
		END
END

```
