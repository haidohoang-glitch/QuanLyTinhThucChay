# Stored Procedure: `BaoCaoSPvuotHD_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-03 16:52:23.580000
- **Ngày sửa cuối**: 2026-03-03 16:55:04.023000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[BaoCaoSPvuotHD_PR]

AS
BEGIN
    SET NOCOUNT ON;

    -- Xóa dữ liệu cũ của PR
    DELETE FROM dbo.BaoCaoSPvuotHD
    WHERE NguonSP = 'PR';

INSERT INTO dbo.BaoCaoSPvuotHD
(
    NgayDanhso,
    SoHopDong,
    HopDongID,
    HopDongChiTietID,
    DmLoaiREF,
    htqc,
    DmSanPhamREF,
    TenSanPham,
    TenLoaiBanner,
    DmViTriREF,
    TenViTri,
    SoLuong,
    DonViTinh,
    DonGia,
    ChietKhau,
    ThanhTien,
    SoLuong_SP,
    ThucChayBanSP,
    Lech,
    TyLeVuot,
    CreatedDate,
    NguonSP
)
SELECT CONVERT(DATE,A.CreatedAt) CreatedAt
,A.SoHopDong
,A.HopDongID
,A.HopDongChiTietID
,A.DmLoaiREF
,A.TenLoai
,A.DmSanPhamREF
,A.TenSanPham
,A.TenLoaiBanner
,A.DmViTriREF
,A.TenViTri
,A.SoLuong
,A.DonViTinh
,A.DonGia
,A.ChietKhau
,A.Thanhtien_HD
,B.SoLuong_treo
,B.Thanhtientreo
,round((isnull(Thanhtientreo,0) - Thanhtien_HD),0) as TreoVuotHD
,Round(CASE 
            WHEN Thanhtien_HD = 0 THEN 0
            ELSE 
                (ISNULL(Thanhtientreo,0) - Thanhtien_HD) * 100.0 
                / Thanhtien_HD
        END,2),
		GETDATE(),
        'PR'
from(
	SELECT hd.CreatedAt,
		hd.SoHopDong, hd.HopDongID, hdct.HopDongChiTietID,DmLoaiREF,TenLoai,
		hdct.TenSanPham, hdct.SoLuong, hdct.DonViTinhREF, hdct.DonViTinh,DmSanPhamREF,
		hdct.DonGia, hdct.ChietKhau,TenLoaiBanner,DmViTriREF,TenViTri,
		CAST(CASE WHEN hdct.ChietKhau = 100
				  THEN hdct.SoLuong * hdct.DonGia
				  ELSE hdct.ThanhTien END AS decimal(18,2)) AS Thanhtien_HD
	FROM dbo.HopDongChiTiet hdct
	JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
	WHERE hdct.DmSanPhamREF IN (141, 637, 305)
	  AND hd.TrangThaiHopDong NOT IN (0, 3)
	  AND hdct.DeletedStatus = 0
	  AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
	  AND hd.Nam >= 2025
	  --AND hdct.ChietKhau <> 100
)A left join (
	SELECT
		tt.HopDongChiTietREF,
		Sum(tt.SoLuong) SoLuong_treo,
		Sum(CASE WHEN tt.ChietKhau = 100
			 THEN  (tt.GiaTien * tt.SoLuong) 
			 ELSE (tt.GiaTien *  tt.SoLuong * (100 -  tt.ChietKhau) / 100.0) END) AS Thanhtientreo
	FROM dbo.ThucChayHopDongChiTietPR tt	
	WHERE tt.DeletedStatus = 0
	--and tt.HopDongChiTietREF ='763184'
	group by tt.HopDongChiTietREF
)B on a.HopDongChiTietID = B.HopDongChiTietREF
where round((isnull(Thanhtientreo,0) - Thanhtien_HD),0) > 1000

END
```
