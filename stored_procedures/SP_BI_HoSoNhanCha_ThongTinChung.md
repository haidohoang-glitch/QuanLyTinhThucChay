# Stored Procedure: `BI_HoSoNhanCha_ThongTinChung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:14.897000
- **Ngày sửa cuối**: 2015-06-25 16:17:14.897000

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

--EXEC [dbo].[BI_HoSoNhanCha_ThongTinChung] 42556,'2014-01-01','2015-01-01'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_ThongTinChung] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	DECLARE @tableDoanhSoNhan TABLE(Rowid INT
	, DmNhanHangID INT
	, TenNhanHang NVARCHAR(MAX)
	, DmNganhHangREF NVARCHAR(MAX)
	, NhanHangChaREF INT
	, levels INT
	, DmNhanHangGocID INT )
	
	;WITH cte
		 AS
		 (
		  SELECT dnh.DmNhanHangID, TenNhanHang, dnh.NhanHangCha, ISNULL(dnh.DmNghanhHangREF,'')DmNghanhHangREF,levels = 0, DmNhanHangGocID = dnh.DmNhanHangID ,
					RIGHT('000' + CONVERT(VARCHAR(MAX), DmNhanHangID), 3) AS Lvl
		  FROM DmNhanHang dnh
		  WHERE dnh.DmNhanHangID = @DmNhanHangChaID
		  AND dnh.DeletedStatus <> 1
			 UNION ALL
		     
			 SELECT s.DmNhanHangID,
					s.TenNhanHang,
					s.NhanHangCha,
					ISNULL(s.DmNghanhHangREF,'')DmNghanhHangREF,
					levels = c.levels + 1,
					DmNhanHangGocID,
					c.lvl + RIGHT('000' + CONVERT(VARCHAR(MAX), s.DmNhanHangID), 3) AS  lvl
			 FROM   cte c
					INNER JOIN DmNhanHang s
						 ON  c.DmNhanHangID = s.NhanHangCha
			 WHERE s.DeletedStatus <> 1
		 )
		 
		 INSERT INTO @tableDoanhSoNhan
		 SELECT ROW_NUMBER() OVER ( ORDER BY lvl) AS rowid,
				DmNhanHangID,
				LEFT(REPLICATE('|- ', cte.levels) + cte.TenNhanHang, 50) AS TenNhanHang,
				DmNghanhHangREF,
				ISNULL(NhanHangCha,'')NhanHangCha,
				levels,
				DmNhanHangGocID
		 FROM   cte
	
	--SELECT * FROM dbo.HoSoNhan_DoanhSoChiTiet
	
	--XOA THONG TIN DU LIEU TABLE TAM
	DELETE FROM dbo.HoSoNhan_DoanhSoChiTiet 
	WHERE NhanHangGocID = @DmNhanHangChaID
	--TAO DOANH SO CHO TABLE HoSoNhan_DoanhSoChiTiet
	
	INSERT INTO dbo.HoSoNhan_DoanhSoChiTiet
	SELECT tb.Rowid,
	 tb.DmNhanHangID
	 ,tb.TenNhanHang
	 , tb.DmNganhHangREF
	 , isnull(ds.TenNganhHang,'')TenNganhHang
	 , tb.NhanHangChaREF
	 , tb.DmNhanHangGocID
	 , tb.levels
	 , isnull(DS.SoHopDong,'')SoHopDong
	 , isnull(ds.HopDongREF,0)HopDongREF
	 , isnull(ds.TenNhanVien,'')TenNhanVien
	 , ISNULL(ds.TenBoPhan,'')TenBoPhan
	 , isnull(ds.TenKhachHang,'')TenKhachHang
	 , isnull(ds.DoanhSoKyHaiDau,0)*1.1 DoanhSoKyHaiDau
	 , isnull(TC.ThucChay,0)*1.1 ThucChay
	 , ISNULL(ds.DmSanPhamREF,0)DmSanPhamREF
	 , ISNULL(ds.TenSanPham,'')TenSanPham
	 , '' CreatedBy
	 , GETDATE() CreatedAt
	FROM @tableDoanhSoNhan tb
	LEFT JOIN 
	(
		SELECT rnhttct.DmNhanHangREF, rnhttct.TenNhanHang, rnhttct.TenNganhHang, rnhttct.SoHopDong, rnhttct.HopDongREF
		, hd.TenNhanVien, hd.TenKhachHang, hd.TenBoPhan
		, rnhttct.TenSanPham, rnhttct.DmSanPhamREF
		, SUM(rnhttct.DoanhSoKyHaiDau)DoanhSoKyHaiDau 
		FROM RptNhanHangThongTinChiTiet rnhttct
		INNER JOIN HopDong hd ON hd.HopDongID = rnhttct.HopDongREF
		--INNER JOIN HopDongChiTiet hdct ON rnhttct.HopDongREF = hdct.HopDongFK
		WHERE 1=1
		AND CONVERT(DATE,rnhttct.NgayThucHien) BETWEEN @FromDate AND @ToDate
		GROUP BY rnhttct.DmNhanHangREF, rnhttct.TenNhanHang, rnhttct.TenNganhHang, rnhttct.SoHopDong, rnhttct.HopDongREF
		, hd.TenNhanVien, hd.TenKhachHang, hd.TenBoPhan
		, rnhttct.TenSanPham, rnhttct.DmSanPhamREF
		--,hdct.ChietKhau, hdct.TiLeTuVan
	) DS ON tb.DmNhanHangID = DS.DmNhanHangREF
	LEFT JOIN
	(
		SELECT rnhtcf.DmNhanHangREF, rnhtcf.TenNhanHang, rnhtcf.HopDongREF,rnhtcf.DmSanPhamREF
		, SUM(rnhtcf.DoanhSoThucChay) ThucChay 
		FROM RptNhanHangThucChayFull rnhtcf
		WHERE 1=1 
		AND	CONVERT(DATE,rnhtcf.NgayThucHien) BETWEEN @FromDate AND @ToDate
		GROUP BY rnhtcf.DmNhanHangREF, rnhtcf.TenNhanHang, rnhtcf.HopDongREF,rnhtcf.DmSanPhamREF
	)TC ON DS.DmNhanHangREF = tc.DmNhanHangREF AND ds.HopDongREF = tc.HopDongREF AND ds.DmSanPhamREF = tc.DmSanPhamREF 
	WHERE 1=1 
	ORDER BY tb.Rowid
	
	SELECT dnh.DmNhanHangID, dnh.TenNhanHang,N'Đang chạy' TinhTrangNhanHang
	, isnull(khttc.KhachHangThongTinChungID,0)KhachHangSoHuuREF
	, ISNULL(khttc.TenKhachHang,'')TenKhachHangSoHuu
	, ISNULL(khttc.MaSoThue,'')MaSoThue
	, ISNULL(khttc.DiaChiKhachHang,'')DiaChiKhachHang
	, ISNULL(khttc.SoDienThoai,'')SoDienThoai
	 FROM DmNhanHang dnh 
	LEFT JOIN KhachHangThongTinChung khttc ON dnh.DmKhachhangSohuuREF = khttc.KhachHangThongTinChungID
	WHERE dnh.DmNhanHangID = @DmNhanHangChaID 
END

--EXEC [BI_HoSoNhanCha_ThongTinChung] 4152,'2015-01-01','2014-01-01'

```
