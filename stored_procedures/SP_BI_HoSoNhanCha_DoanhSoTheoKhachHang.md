# Stored Procedure: `BI_HoSoNhanCha_DoanhSoTheoKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:13.940000
- **Ngày sửa cuối**: 2015-06-25 16:17:13.940000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangChaID` | `int(4)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoTheoKhachHang] 1523,'2014-01-01','2015-01-01'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_DoanhSoTheoKhachHang] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	DECLARE @TongDoanhSoHaiDau BIGINT
	SET @TongDoanhSoHaiDau = 
	(
		SELECT SUM(nh.DoanhSoHaiDau) 
		FROM HoSoNhan_DoanhSoChiTiet nh 
		WHERE nh.NhanHangGocID = @DmNhanHangChaID
	)
	SET @TongDoanhSoHaiDau = ISNULL(@TongDoanhSoHaiDau,1)
	SELECT A.DmKhachHangREF, A.TenKhachHang, A.HinhThucKy
	, A.DoanhSoKyHaiDau
	, A.DoanhSoThucChay
	, Round(Convert(float,A.DoanhSoKyHaiDau)/CONVERT(FLOAT,@TongDoanhSoHaiDau)*100,3,3) Tile_DS2Dau_TongDs
	, round(CONVERT(FLOAT,A.DoanhSoThucChay)/CONVERT(FLOAT,A.DoanhSoKyHaiDau)*100,3,3) Tile_DsTc_Ds2Dau
	, 0 IsDeleted	 
	FROM
		(
			SELECT A.DmKhachHangREF, A.TenKhachHang, A.HinhthucKy
			, SUM(A.DoanhSoHaiDau)DoanhSoKyHaiDau
			, SUM(A.ThucChay)DoanhSoThucChay
			FROM
			(
				SELECT isnull(HD.DmKhachHangREF,0) DmKhachHangREF, isnull(HD.TenKhachHang,'')TenKhachHang
				,(
						CASE WHEN  hd.DmHinhThucKhachHangREF = 3 THEN N'Dai ly'
						ELSE N'Truc tiep'
						END
				) AS HinhThucKy
				, DSN.DoanhSoHaiDau 
				, DSN.ThucChay
				
				FROM HoSoNhan_DoanhSoChiTiet DSN
				LEFT JOIN
				( SELECT hd.HopDongID, hd.DmKhachHangREF, hd.TenKhachHang, khttc.DmHinhThucKhachHangREF
					FROM HopDong hd INNER JOIN 
					KhachHangThongTinChung khttc ON hd.DmKhachHangREF= KHTTC.KhachHangThongTinChungID
				  WHERE hd.TrangThaiHopDong <> 3	
				) HD ON DSN.HopDongREF = HD.HopDongID
				WHERE DSN.NhanHangGocID = @DmNhanHangChaID
			)A
			WHERE (A.DoanhSoHaiDau <>0 OR A.ThucChay <> 0)
			GROUP BY A.DmKhachHangREF, A.TenKhachHang, A.HinhthucKy
	)A
	WHERE (a.DoanhSoKyHaiDau <> 0 OR a.DoanhSoThucChay <> 0)
	ORDER BY A.DoanhSoKyHaiDau DESC
END

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoTheoKhachHang] 4152,'2015-01-01','2014-01-01'

```
