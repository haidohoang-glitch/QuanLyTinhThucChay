# Stored Procedure: `GetDonGiaBySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-10 17:57:20.180000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.693000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetDonGiaBySoHopDong]
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT
AS
BEGIN
	SELECT distinct hd.SoHopDong
	, hdct.DonViTinh
	, hdct.DonGia
	, hdct.ChietKhau 
	,(hdct.ChietKhau/100 * hdct.DonGia) TienCK, 
	CASE 
	WHEN (hdct.DonGia - (hdct.ChietKhau/100 * hdct.DonGia)) = 0 THEN  hdct.DonGia 
	ELSE (hdct.DonGia - (hdct.ChietKhau/100 * hdct.DonGia))
	END DonGiaSauCK	,
	hdct.IsKhuyenMai
	FROM   HopDong hd
		  INNER JOIN HopDongChiTiet hdct
			   ON  hd.HopDongID = hdct.HopDongFK
	WHERE  hd.TrangThaiHopDong <> 3
	and hdct.DmSanPhamREF = @DmSanPhamREF
	AND hd.SoHopDong = @SoHopDong
END

```
