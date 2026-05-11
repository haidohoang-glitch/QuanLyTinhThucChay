# Stored Procedure: `prc_QLTC_XuLylaiDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.620000
- **Ngày sửa cuối**: 2023-07-13 11:43:36.477000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@Contract` | `nvarchar(4000)` | No |
| `@Product` | `int(4)` | No |
| `@Table` | `nvarchar(4000)` | No |
| `@HopDongChiTiet` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_QLTC_XuLylaiDuLieu]
	@FromDate Datetime = NULL,
	@ToDate Datetime = NULL,
	@Contract Nvarchar(2000) = '',
	--@Banner Nvarchar(500) = '',
	@Product Int = 0,
	@Table Nvarchar(2000) = '',
	@HopDongChiTiet INT = 0
	--@Id INT = 0
AS
BEGIN
	SET NOCOUNT ON;
	--Declare @HopDongChiTietID INT = 0;
	Declare @NgayGhiNhanThucChay DATE;
	Set @NgayGhiNhanThucChay = CAST(DATEADD(DAY, -1, GETDATE()) AS DATE);
	--Set @HopDongChiTietID = (SELECT top(1) HopDongChiTietREF FROM dbo.ThucChayHopDongChiTiet where DmBannerREF = @Banner order by id desc)

	--Update trạng thái đang chạy
	UPDATE [dbo].[DataLog_QLTC_XuLylaiDuLieu] SET Status = 1 
	WHERE CAST(FromDate AS Date) = CAST(@FromDate AS Date)
			AND CAST(ToDate AS Date) = CAST(@ToDate AS Date)
			AND (ISNULL(@Contract, '') = ''
					OR SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
			AND (ISNULL(@HopDongChiTiet, 0) = 0
					OR HopDongChiTietREF = @HopDongChiTiet)
			AND (ISNULL(@Product, 0) = 0
					OR DmSanPhamREF = @Product)
			AND (Status = 0 OR Status IS NULL)

	If(@Table = N'DataThucChay_test' Or @Table = N'DataThucChay' Or @Table = N'Branding' Or @Table = N'Branding_Test') --Branding
		BEGIN
			DECLARE @donVi INT = 0;

			SELECT DISTINCT * FROM dbo.DmDonViTinh
			SELECT TOP(1) @donVi = DonViTinhREF FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTiet
			IF(@donVi = 10)	--doi tru tinh lai displayads đơn vị GÓI doitrutinhlai
				BEGIN
					EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_V2] @FromDate, --	@StartDate DATETIME, --Ngay BD phat sinh du lieu bang thuc chay
												  @ToDate , --@EndDate DATETIME,
												  @Contract , --@pSoHopDong NVARCHAR(100),
												   @HopDongChiTiet, --@pHopDongChiTietREF INT,
												   @NgayGhiNhanThucChay --	@pNgayGhiNhanThucChay DATETIME
                END
			ELSE IF(EXISTS(SELECT Name FROM dbo.STRING_SPLIT('1,2,28,27') WHERE @donVi = Name))
				BEGIN
					IF(@Product = 342)
						BEGIN
							EXEC [dbo].[ThucChay_DoiTruVaTinhLai_Mobile_Job] @StartDate = @FromDate, -- datetime
																			@EndDate = @ToDate,   -- datetime
																			@pSoHopDong = @Contract,                  -- nvarchar(50)
																			@NgayTinh = @NgayGhiNhanThucChay   -- datetime						 
						END
					ELSE
						BEGIN
							EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Job] @dtStart = @FromDate, --DATETIME
																		  @dtEnd = @ToDate, --DATETIME
																		  @pSoHopDong = @Contract, --NVARCHAR(50)
																		  @pHopDongChiTietID = @HopDongChiTiet, --INT
																		  @NgayTinh = @NgayGhiNhanThucChay --DATETIME
				
						END
				END
		 END
	ELSE If(@Table = N'DataThucchay_Native_Ads_test' Or @Table = N'DataThucchay_Native_Ads') --Native Ads
		Begin
			EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Native_Ads] @pSoHopDong = @Contract, --NVARCHAR(100),
																 @pDmSanPhamREF = @Product, --INT,
																 @pStartDate = @FromDate, --datetime,
																 @pEndDate = @ToDate, --DATETIME,
																 @pNgayGhiNhanThucChay = @NgayGhiNhanThucChay--DATETIME
		End
	Else If(@Table = N'DataThucchay_OnImageAds_test' Or @Table = N'DataThucchay_OnImageAds')--OnImage Ads
		Begin
			EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Native_Ads] @pSoHopDong = @Contract, --NVARCHAR(100),
																 @pDmSanPhamREF = @Product, --INT,
																 @pStartDate = @FromDate, --datetime,
																 @pEndDate = @ToDate, --DATETIME,
																 @pNgayGhiNhanThucChay  = @NgayGhiNhanThucChay --DATETIME
		End
	Else If(@Table = N'DataThucChay_Admatic_v2_test' Or @Table = N'DataThucChay_Admatic_v2')--Admatic
		BEGIN
        PRINT 4
			EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic] @pSoHopDong = @Contract, --NVARCHAR(100)
																	@pHopDongChiTietID = @HopDongChiTiet, --INT
																	@pDmSanPhamREF = @Product, --INT
																	@pStartDate = @FromDate, --datetime
																	@pEndDate = @ToDate, --DATETIME
																	@pNgayGhiNhanThucChay  = @NgayGhiNhanThucChay--DATETIME
			-- Đối với sản phẩm ADX (IN (144,585,628)	) chạy đối trừ thì phải insert thêm vào bảng ThucChayDaTinhAdmarket
			IF(@Product = 585 OR @Product = 144 OR @Product = 628)
				BEGIN
					INSERT INTO ThucChayDaTinhAdmarket 
					SELECT * from dbo.ThucChayDaTinh WHERE SoHopDong = @Contract AND HopDongChiTietREF=@HopDongChiTiet  AND CONVERT(DATE,NgayThucHien) = @NgayGhiNhanThucChay and DmSanPhamREF =@Product
				End
		End
End

```
