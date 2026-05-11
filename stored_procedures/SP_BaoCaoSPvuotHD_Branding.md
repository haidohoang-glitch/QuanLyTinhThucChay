# Stored Procedure: `BaoCaoSPvuotHD_Branding`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-02-27 16:36:44.880000
- **Ngày sửa cuối**: 2026-03-02 18:36:47.913000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[BaoCaoSPvuotHD_Branding]

AS
BEGIN
    SET NOCOUNT ON;

    -- Xóa dữ liệu cũ của Branding
    DELETE FROM dbo.BaoCaoSPvuotHD
    WHERE NguonSP = 'Branding';

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
      SELECT 
	CONVERT(DATE,C.CreatedAt) CreatedAt,
	C.SoHopDong,
	HopDongID,
	C.HopDongChiTietID,
	DmLoaiREF,
	TenLoai,
	C.DmSanPhamREF
	,TenSanPham,
	TenLoaiBanner,
	DmViTriREF,
	TenViTri,
	C.SoLuong
	,DonViTinh
	,C.DonGia
	,C.ChietKhau
	,C.ThanhtienHD
	,Soluong_tool
	,C.thanhtien_Tool
	,ROUND(C.thanhtien_Tool,0) - C.ThanhtienHD Lech_SP_ASD
	,Round(CASE 
            WHEN C.ThanhtienHD = 0 THEN 0
            ELSE 
                (ISNULL(C.thanhtien_Tool,0) - C.ThanhtienHD) * 100.0 
                / C.ThanhtienHD
        END,2),
		GETDATE(),
        'Branding'
	FROM (
		SELECT A.SoHopDong,A.DmSanPhamREF,A.HopDongChiTietID,A.SoLuong,A.DonGia,A.ChietKhau,A.ThanhtienHD	
		,SUM(B.Thanhtien_Sp) AS thanhtien_Tool,SUM(B.Soluong_tool) AS Soluong_tool   ,A.CreatedAt, 
		A.HopDongID,A.DmViTriREF,A.TenLoaiBanner,A.TenLoai,A.DmLoaiREF,A.TenViTri,TenSanPham,DonViTinh
		FROM (
			SELECT hd.SoHopDong,hdct.DmSanPhamREF,hdct.HopDongChiTietID,hdct.DonViTinhREF,hdct.DonViTinh,hdct.SoLuong
			,hdct.ChietKhau,hd.CreatedAt, hd.HopDongID,hdct.DmViTriREF,hdct.TenLoaiBanner,hdct.TenLoai,hdct.DmLoaiREF,hdct.TenViTri
			,ROUND( CASE WHEN hdct.ChietKhau = 100 THEN hdct.ChietKhau ELSE (100-hdct.ChietKhau) END,0) AS ChietkhauHD
			,hdct.DonGia,TenSanPham
			,ROUND( CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong * hdct.DonGia ELSE hdct.ThanhTien END,0) AS ThanhtienHD
			FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
			ON hd.HopDongID=hdct.HopDongFK
			WHERE hdct.DmSanPhamREF IN (733,821,5133,339,240,598,342,505,733,5056,5299) 
			AND hdct.DonViTinhREF IN(1,2,10)
			AND NOT hdct.DmLoaiREF = 42
			AND hd.Nam > = 2025 
			AND NOT hdct.DmLoaiNenTangREF = 9
		)A INNER JOIN(	
			SELECT a.HopDongChiTietREF
			,CASE WHEN a.ChietKhau = 100 then (ISNULL(a.Soluong_tool,0) * a.DonGiaTool) ELSE 
				ISNULL(a.Soluong_tool,0) * a.DonGiaTool * (100-a.ChietKhau)/100  end Thanhtien_Sp 
			,Soluong_tool
			FROM(
				SELECT E.HopDongChiTietREF ,E.DonGiaTool,E.ChietKhau
					,  CASE WHEN E.DmDonViTinhREF_Tool = 1 AND E.DmDonViTinhREFHĐ = 10 THEN SUM(F.TongViewThucChay) 
							WHEN E.DmDonViTinhREF_Tool = 2 AND E.DmDonViTinhREFHĐ = 10 THEN SUM(F.TongClickThucChay) 
							WHEN E.DmDonViTinhREFHĐ = 1 THEN SUM(F.TongViewThucChay) 
							WHEN E.DmDonViTinhREFHĐ = 2 THEN SUM(F.TongClickThucChay)
							ELSE 0 END				
					AS Soluong_tool  
				FROM (
					SELECT DISTINCT(tchd.DmBannerREF),tchd.HopDongChiTietREF ,tchd.DmDonViTinhREF DmDonViTinhREF_Tool ,hdct1.DonViTinhREF AS DmDonViTinhREFHĐ 
					,tchd.DonGia,hdct1.ChietKhau
					,CASE when hdct1.DonViTinhREF = 10 AND tchd.DmDonViTinhREF = 1 THEN tchd.DonGia/1000 
						  WHEN hdct1.DonViTinhREF = 10 AND tchd.DmDonViTinhREF = 2 THEN tchd.DonGia 
						  WHEN hdct1.DonViTinhREF = 1 THEN hdct1.DonGia/1000
						  WHEN hdct1.DonViTinhREF = 2 THEN hdct1.DonGia
					ELSE 0 END AS DonGiaTool	
					FROM dbo.ThucChayHopDongChiTiet tchd 
					INNER JOIN dbo.HopDongChiTiet hdct1
					ON tchd.HopDongChiTietREF = hdct1.HopDongChiTietID
					WHERE tchd.DeletedStatus = 0 
					AND hdct1.DeletedStatus = 0
					AND tchd.DmSanPhamREF NOT IN (821,5133)
					--and HopDongChiTietREF ='774058'
					AND NOT LTRIM(RTRIM(tchd.TenBanner)) = N'Sponsor Page'
					AND not ROUND( CASE WHEN tchd.DmDonViTinhREF = 1 THEN  ISNULL(tchd.DonGia,0)/1000 ELSE ISNULL(tchd.DonGia,0) END,3) IS null 
				)E LEFT JOIN (
					SELECT tc.DmBannerREF,SUM(tc.TongViewThucChay) TongViewThucChay	, SUM(tc.TongClickThucChay) TongClickThucChay
					FROM dbo.ThucChay tc				
					WHERE tc.SoHopDong NOT IN ('hd_demo', '', 'HD DEMO', 'hd_king_test2','HD_DEMO_CPM','hd_stick_test','HD_TEST_KING1','DEMO','Khac0010919')	
					AND tc.CreatedBy <> N'From API_Admatic'
					GROUP BY tc.DmBannerREF
				)F 
				ON CONVERT(VARCHAR(50),E.DmBannerREF)  = CONVERT(VARCHAR(50),F.DmBannerREF) 
				AND TRY_CONVERT(INT, E.DmBannerREF) IS NOT NULL
				AND TRY_CONVERT(INT, F.DmBannerREF) IS NOT NULL
				GROUP BY E.HopDongChiTietREF ,E.DmDonViTinhREF_Tool,E.DmDonViTinhREFHĐ,DonGiaTool,E.ChietKhau
			)a 
			UNION(	
				SELECT b.HopDongChiTietREF
				,b.thanhtien_SP ,b.Soluong_tool
				FROM (
					SELECT S.HopDongChiTietREF
					,CASE WHEN S.ChietKhau = 100 THEN ROUND(SUM(X.TTKM_SP),0) ELSE ROUND(SUM(X.TTTC_SP),0) END thanhtien_SP
					,CASE WHEN S.ChietKhau = 100 THEN ROUND(SUM(X.SLKM_SP),0) ELSE ROUND(SUM(X.SLTC_SP),0) END Soluong_tool
					FROM (
						SELECT DISTINCT(tchd.DmBannerREF),tchd.HopDongChiTietREF,hdct3.ChietKhau 
						FROM dbo.ThucChayHopDongChiTiet tchd 
						INNER JOIN dbo.HopDongChiTiet hdct3
						ON tchd.HopDongChiTietREF = hdct3.HopDongChiTietID
						WHERE tchd.DeletedStatus = 0 
						AND tchd.DmSanPhamREF IN (821,5133)				
					)S LEFT JOIN (
						SELECT DmBannerID,SUM(ThanhTienThucChaySauCK) TTTC_SP,SUM(ThanhTienThucChayKM) TTKM_SP
						,SUM(SoLuongThucChay) SLTC_SP,SUM(SoLuongThucChayKM) SLKM_SP
						FROM dbo.ThucChay_Native_Ads tc
						WHERE tc.SoHopDong NOT IN ('hd_demo', '', 'HD DEMO', 'hd_king_test2','HD_DEMO_CPM','hd_stick_test','HD_TEST_KING1','DEMO','Khac0010919')
						GROUP BY DmBannerID
					)X 
					ON CONVERT(VARCHAR(50),S.DmBannerREF)  = CONVERT(VARCHAR(50),X.DmBannerID )
					GROUP BY S.HopDongChiTietREF,S.ChietKhau			
				)b	
			)
		)B
		ON A.HopDongChiTietID=B.HopDongChiTietREF
		GROUP BY A.SoHopDong,A.DmSanPhamREF,A.HopDongChiTietID,A.SoLuong,A.DonGia,A.ThanhtienHD,A.ChietKhau,A.CreatedAt, 
		A.HopDongID,A.DmViTriREF,A.TenLoaiBanner,A.TenLoai,A.DmLoaiREF,A.TenViTri,TenSanPham,DonViTinh
	)C LEFT JOIN(
		SELECT TCDT.HopDongChiTietREF,SUM(TCDT.SoLuongThucChay+TCDT.SoLuongThayDoi) AS SL,SUM(TCDT.ThanhTienSauTrietKhauThucChay+TCDT.GiaTriThayDoi) AS thanhtien
		,SUM(TCDT.SoLuongThucChayKM + TCDT.SoLuongKMThayDoi) AS SLKM,SUM(TCDT.ThanhTienKM +TCDT.GiaTriKMThayDoi) AS thanhtienKM
		FROM dbo.ThucChayDaTinh TCDT
		WHERE TCDT.DmHinhThucQuangCao NOT IN (13,42)
		GROUP BY TCDT.HopDongChiTietREF
	)D
	ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE ROUND(ISNULL(C.thanhtien_Tool,0),0)
          - ROUND(C.ThanhtienHD,0) > 1000

END

```
