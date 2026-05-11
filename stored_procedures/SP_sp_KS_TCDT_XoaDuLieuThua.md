# Stored Procedure: `sp_KS_TCDT_XoaDuLieuThua`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-08 17:03:01.710000
- **Ngày sửa cuối**: 2021-06-08 17:03:08.873000

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
CREATE PROCEDURE sp_KS_TCDT_XoaDuLieuThua 
	-- Add the parameters for the stored procedure here
	@FromDate datetime,
	@ToDate datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	delete from 
		ThucChayDaTinh where 1=1
		AND NgayThucHien between @FromDate and @ToDate
		and dmsanphamref not in (140,549) and ChietKhau <> 100
		AND TiLeTuVan = 0	
		AND ChiPhiTuVan = 0 
		AND TongViewThucChay = 0
		AND TongClickThucChay = 0	
		AND TongSoBaiViet	 = 0
		AND SoLuongThucChay		 = 0
		AND GiaTriThayDoi	 = 0
		AND ThanhTienThucChayTruocTrietKhau	 = 0
		AND GiaTriTrietKhauThucChay	 = 0
		AND ThanhTienSauTrietKhauThucChay	 = 0
		AND GiaTriHoaHongThucChay	 = 0
		AND ThanhTienThucThu	 = 0
		AND ThanhTienKM	 = 0
		AND SoLuongThucChayKM	 = 0
		AND SoLuongThucChayLechTreoHa	 = 0
		AND ThanhTienLechTreoHa	 = 0
		AND SoLuongThayDoi	 = 0
		AND SoLuongKMThayDoi	 = 0
		AND GiaTriKMThayDoi = 0
END

```
