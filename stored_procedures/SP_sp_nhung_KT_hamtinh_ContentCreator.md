# Stored Procedure: `sp_nhung_KT_hamtinh_ContentCreator`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 09:12:29.497000
- **Ngày sửa cuối**: 2026-03-20 09:12:29.497000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_ContentCreator
AS
BEGIN
    SET NOCOUNT ON;

    SELECT C.SoHopDong,C.HopDongChiTietID,C.DmSanPhamREF,C.TenSanPham,C.DmLoaiBannerREF, C.SoLuong,dbo.FormatNumber(C.DonGia) DonGia,C.ChietKhau,dbo.FormatNumber(C.ThanhTien) ThanhTienHĐ
	,dbo.FormatNumber(C.PbThanhTien_SP) PbThanhTien_SP,dbo.FormatNumber(C.ThanhTien_ChiPhi ) ThanhTien_ChiPhi
	,dbo.FormatNumber(C.ThanhTien_MuaNgoai) ThanhTien_MuaNgoai
	,dbo.FormatNumber(D.Thanhtien_TC) Thanhtien_TC
	,CASE WHEN ROUND(ISNULL(C.ThanhTien_ChiPhi,0),0) <= ROUND(ISNULL(C.ThanhTien,0),0) AND ROUND(ISNULL(D.Thanhtien_TC,0),0) <> ROUND(ISNULL(C.ThanhTien_ChiPhi,0),0) 
	THEN CONCAT(N'Thực chạy ghi nhận thiếu với treo:',dbo.FormatNumber(ROUND(ISNULL(C.ThanhTien_ChiPhi,0) - ISNULL(D.Thanhtien_TC,0),0) )) 
	ELSE N'' END Ghi_chu
	FROM(
		SELECT * FROM(
			SELECT hd.SoHopDong,hdct.HopDongChiTietID,hdct.DmSanPhamREF,hdct.TenSanPham,hdct.SoLuong,hdct.DonGia,hdct.ChietKhau,hdct.ThanhTien,hdct.DmLoaiBannerREF  FROM dbo.HopDong hd
			LEFT JOIN dbo.HopDongChiTiet hdct
			ON hdct.HopDongFK = hd.HopDongID
			WHERE hdct.DeletedStatus = 0
			AND hd.TrangThaiHopDong <> 3
			AND hd.Nam > = 2023
			AND hdct.DmSanPhamREF ='5184'
		)A LEFT JOIN (
			SELECT H.HopDongChiTietREF,H.ThanhTien_ChiPhi,H.PbThanhTien_SP,I.ThanhTien_MuaNgoai,H.PhanBoRef,I.HopDongChiTietREF2 FROM(
				SELECT * FROM(
					SELECT tt_SP.HopDongChiTietREF,SUM(tt_SP.ThanhTien) ThanhTien_ChiPhi FROM dbo.ThucChayHopDongChiTiet tt_SP
					WHERE tt_SP.DeletedStatus = 0
					GROUP BY tt_SP.HopDongChiTietREF			
				)E Full JOIN(			
					SELECT PhanBoRef,ROUND(SUM(PbThanhTien),0) PbThanhTien_SP FROM dbo.AppKetQuaVanHanh_CreatorContent 
					WHERE IsDeleted = 0
					AND TrangThai = 6
					GROUP BY PhanBoRef
				)F ON ISNULL(F.PhanBoRef,0) = ISNULL(E.HopDongChiTietREF,0)
			) H FULL JOIN (
				SELECT HopDongChiTietREF HopDongChiTietREF2, SUM(ThanhTienThucChayBanSauCK) ThanhTien_MuaNgoai  FROM  dbo.ThucChayMuaNgoaiChiTiet
				WHERE DeletedStatus = 0
				GROUP BY HopDongChiTietREF
			)I ON H.HopDongChiTietREF = ISNULL(I.HopDongChiTietREF2,0)
		)B ON A.HopDongChiTietID = ISNULL(B.HopDongChiTietREF,0) OR A.HopDongChiTietID = ISNULL(B.PhanBoRef,0) OR A.HopDongChiTietID = ISNULL(B.HopDongChiTietREF2,0)
	)C LEFT JOIN (
		SELECT tcdt.HopDongChiTietREF,SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi) Thanhtien_TC FROM dbo.ThucChayDaTinh tcdt	
		GROUP BY tcdt.HopDongChiTietREF	
	)D ON C.HopDongChiTietID = ISNULL(D.HopDongChiTietREF,0)
	WHERE ROUND(D.Thanhtien_TC - C.ThanhTien,0) <> 0
	And ROUND(ISNULL(D.Thanhtien_TC,0) - CASE WHEN C.ThanhTien_ChiPhi IS NULL THEN C.ThanhTien_MuaNgoai ELSE C.ThanhTien_ChiPhi END,0) <> 0

END;
```
