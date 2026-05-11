# Stored Procedure: `CheckThucChayVuotHopDong_TableTCDT_DotChayBooking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-10-17 10:55:06.067000
- **Ngày sửa cuối**: 2020-10-17 10:55:17.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


--CheckThucChayVuotHopDong_TableTCDT '2019-12-05'
CREATE PROCEDURE [dbo].[CheckThucChayVuotHopDong_TableTCDT_DotChayBooking] 
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	/*DROP TABLE dbo.KS_ThucChay_TCDT

 CREATE TABLE KS_ThucChay_TCDT_DotChayBooking
(
SoHopDong NVARCHAR(50),
Nam INT,
HopDongID INT,
HopDongChiTietID INT,
NgayThucHien DATETIME,
DmHinhThucQuangCao INT,
DmLoaiBannerREF INT,
DmSanPhamREF INT,
SoLuongThucChay FLOAT,
DonViTinh NVARCHAR(50),
ThanhTienThucChay FLOAT,
ThanhTienThucChayKM FLOAT,
DmChienDichREF int,
DotChayBooking nvarchar(50)
)
Delete from KS_ThucChay_TCDT_DotChayBooking
*/
-------------------Insert dữ liệu--------------------
IF EXISTS (SELECT * FROM KS_ThucChay_TCDT_DotChayBooking WHERE NgayThucHien BETWEEN @FromDate AND @ToDate)
BEGIN
Delete from KS_ThucChay_TCDT_DotChayBooking WHERE NgayThucHien BETWEEN @FromDate AND @ToDate
END

 -------------------ThucChayDaTinh--------------------
INSERT INTO KS_ThucChay_TCDT_DotChayBooking
SELECT SoHopDong,
Nam,
HopDongID,
HopDongChiTietREF,
NgayThucHien,
DmHinhThucQuangCao ,
DmLoaiBannerREF ,
DmSanPhamREF ,
SUM(ISNULL(SoLuongThucChay,0))SoLuongThucChay,
DonViTinh,
SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0)+ISNULL(GiaTriThayDoi,0))ThanhTienThucChay ,
SUM(ISNULL(ThanhTienKM,0)+ISNULL(GiaTriKMThayDoi,0))ThanhTienThucChayKM,
DmChienDichREF,
DotChayBooking
FROM dbo.ThucChayDaTinh WHERE TrangThaiHopDong <> 3
AND NgayThucHien BETWEEN @FromDate AND @ToDate
AND DmSanPhamREF NOT IN (585,144,628,337,299)
AND HopDongID <> 0
AND Nam >=2015
--and DmChienDichREF = 0 -- không lay ggfb
GROUP BY SoHopDong,
Nam,
HopDongID,
HopDongChiTietREF,
NgayThucHien,
DmHinhThucQuangCao ,
DmLoaiBannerREF ,
DmSanPhamREF ,
DonViTinh,
DmChienDichREF,
DotChayBooking
END

```
