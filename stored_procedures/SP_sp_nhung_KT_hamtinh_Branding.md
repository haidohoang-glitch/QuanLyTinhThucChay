# Stored Procedure: `sp_nhung_KT_hamtinh_Branding`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-19 17:36:07.617000
- **Ngày sửa cuối**: 2026-03-19 17:40:12.243000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Branding
AS
BEGIN
    SET NOCOUNT ON;

	SELECT CASE WHEN C.DmSanPhamREF = 733 THEN N'Gói'
		  WHEN C.DmSanPhamREF IN ( 821,5133) THEN N'Native Ads/ On images'
		  WHEN C.DmSanPhamREF IN ( 342) THEN N'Mobile'
		  WHEN C.DmSanPhamREF NOT IN ( 821,5133,733,342) THEN N'CPC / CPM'
	ELSE N'Chưa xác định' END Thiếu_Branding,
	C.SoHopDong,C.DmSanPhamREF,C.HopDongChiTietID,dbo.formatnumber(C.SoLuong) SLHĐ,C.ChietKhau,C.DonGia
	,dbo.FormatNumber(C.ThanhtienHD) AS ThanhtienHD
	,dbo.FormatNumber(C.thanhtien_Tool) AS thanhtien_Tool
	,dbo.FormatNumber( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END) AS ThanhtienTC
	,dbo.FormatNumber(ROUND(C.thanhtien_Tool,0) - ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) ) Lech_SP_ASD
	,dbo.FormatNumber(C.ThanhtienHD - CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END ) Lech_HĐ_ASD
	FROM (
		SELECT A.SoHopDong,A.DmSanPhamREF,A.HopDongChiTietID,A.SoLuong,A.DonGia,A.ChietKhau,A.ThanhtienHD	
		,SUM(B.Thanhtien_Sp) AS thanhtien_Tool 
		FROM (
			SELECT hd.SoHopDong,hdct.DmSanPhamREF,hdct.HopDongChiTietID,hdct.DonViTinhREF,hdct.DonViTinh,hdct.SoLuong
			,hdct.ChietKhau
			,ROUND( CASE WHEN hdct.ChietKhau = 100 THEN hdct.ChietKhau ELSE (100-hdct.ChietKhau) END,0) AS ChietkhauHD
			,hdct.DonGia
			,ROUND( CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong * hdct.DonGia ELSE hdct.ThanhTien END,0) AS ThanhtienHD
			FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
			ON hd.HopDongID=hdct.HopDongFK
			WHERE hdct.DmSanPhamREF IN (733,821,5133,339,240,598,342,505,733,5056,5299) 
			AND hdct.DonViTinhREF IN(1,2,10)
			AND NOT hdct.DmLoaiREF = 42
			AND hd.Nam > = 2022 AND NOT hdct.DmLoaiNenTangREF = 9
		)A INNER JOIN(	
			SELECT a.HopDongChiTietREF
			,CASE WHEN a.ChietKhau = 100 then (ISNULL(a.Soluong_tool,0) * a.DonGiaTool) ELSE 
				ISNULL(a.Soluong_tool,0) * a.DonGiaTool * (100-a.ChietKhau)/100  end Thanhtien_Sp FROM(
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
					--AND CONVERT(NVARCHAR(50),tchd.DmBannerREF) > 0
					AND tchd.DmSanPhamREF NOT IN (821,5133)
					AND NOT LTRIM(RTRIM(tchd.TenBanner)) = N'Sponsor Page'
					--AND tchd.HopDongChiTietREF ='664555'
					AND not ROUND( CASE WHEN tchd.DmDonViTinhREF = 1 THEN  ISNULL(tchd.DonGia,0)/1000 ELSE ISNULL(tchd.DonGia,0) END,3) IS null 
				)E LEFT JOIN (
					SELECT tc.DmBannerREF,SUM(tc.TongViewThucChay) TongViewThucChay	, SUM(tc.TongClickThucChay) TongClickThucChay
					FROM dbo.ThucChay tc				
					WHERE tc.SoHopDong NOT IN ('hd_demo', '', 'HD DEMO', 'hd_king_test2','HD_DEMO_CPM','hd_stick_test','HD_TEST_KING1','DEMO','Khac0010919')	
					--AND CONVERT(NVARCHAR(50),tc.DmBannerREF) > 0
					AND tc.CreatedBy <> N'From API_Admatic'
					GROUP BY tc.DmBannerREF
				)F 
				ON CONVERT(VARCHAR(50),E.DmBannerREF)  = CONVERT(VARCHAR(50),F.DmBannerREF) AND CONVERT(VARCHAR(50),E.DmBannerREF) > 0 AND CONVERT(VARCHAR(50),F.DmBannerREF) > 0
				--WHERE E.HopDongChiTietREF ='678192'
				GROUP BY E.HopDongChiTietREF ,E.DmDonViTinhREF_Tool,E.DmDonViTinhREFHĐ,DonGiaTool,E.ChietKhau
			)a 
			UNION(	
				SELECT b.HopDongChiTietREF,b.thanhtien_SP FROM (
					SELECT S.HopDongChiTietREF
					,CASE WHEN S.ChietKhau = 100 THEN ROUND(SUM(X.TTKM_SP),0) ELSE ROUND(SUM(X.TTTC_SP),0) END thanhtien_SP
					FROM (
						SELECT DISTINCT(tchd.DmBannerREF),tchd.HopDongChiTietREF,hdct3.ChietKhau 
						FROM dbo.ThucChayHopDongChiTiet tchd 
						INNER JOIN dbo.HopDongChiTiet hdct3
						ON tchd.HopDongChiTietREF = hdct3.HopDongChiTietID
						WHERE tchd.DeletedStatus = 0 
						--AND CONVERT(FLOAT,tchd.DmBannerREF) > 0
						AND tchd.DmSanPhamREF IN (821,5133)				
					)S LEFT JOIN (
						SELECT DmBannerID,SUM(ThanhTienThucChaySauCK) TTTC_SP,SUM(ThanhTienThucChayKM) TTKM_SP
						FROM dbo.ThucChay_Native_Ads tc
						WHERE tc.SoHopDong NOT IN ('hd_demo', '', 'HD DEMO', 'hd_king_test2','HD_DEMO_CPM','hd_stick_test','HD_TEST_KING1','DEMO','Khac0010919')
						GROUP BY DmBannerID
					)X 
					ON CONVERT(VARCHAR(50),S.DmBannerREF)  = CONVERT(VARCHAR(50),X.DmBannerID )
					--WHERE S.HopDongChiTietREF ='715194'
					GROUP BY S.HopDongChiTietREF,S.ChietKhau			
				)b	
			)
		)B
		ON A.HopDongChiTietID=B.HopDongChiTietREF
		--WHERE A.HopDongChiTietID ='715194'
		GROUP BY A.SoHopDong,A.DmSanPhamREF,A.HopDongChiTietID,A.SoLuong,A.DonGia,A.ThanhtienHD,A.ChietKhau
	)C LEFT JOIN(
		SELECT TCDT.HopDongChiTietREF,SUM(TCDT.SoLuongThucChay+TCDT.SoLuongThayDoi) AS SL,SUM(TCDT.ThanhTienSauTrietKhauThucChay+TCDT.GiaTriThayDoi) AS thanhtien
		,SUM(TCDT.SoLuongThucChayKM + TCDT.SoLuongKMThayDoi) AS SLKM,SUM(TCDT.ThanhTienKM +TCDT.GiaTriKMThayDoi) AS thanhtienKM
		FROM dbo.ThucChayDaTinh TCDT
		WHERE TCDT.DmHinhThucQuangCao NOT IN (13,42)
		--AND NOT CONVERT(DATE,TCDT.NgayThucHien) = '2025-05-14' 
		GROUP BY TCDT.HopDongChiTietREF
	)D
	ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE 1=1
	--AND C.HopDongChiTietID ='697826'
	--AND C.SoHopDong ='QC3790524'
	AND NOT (
		(
			C.ThanhtienHD = ROUND(ISNULL(CASE WHEN C.ChietKhau = 100 THEN D.thanhtienKM ELSE D.thanhtien END, 0), 0)
			AND ROUND(C.thanhtien_Tool, 0) > ROUND(ISNULL(CASE WHEN C.ChietKhau = 100 THEN D.thanhtienKM ELSE D.thanhtien END, 0), 0)
		)
		OR 
		(
			ROUND(ISNULL(CASE WHEN C.ChietKhau = 100 THEN D.thanhtienKM ELSE D.thanhtien END, 0), 0) = ROUND(C.thanhtien_Tool, 0)
			AND ROUND(C.thanhtien_Tool, 0) <= C.ThanhtienHD
		)
	)
	AND NOT (
		(ROUND(ROUND(C.thanhtien_Tool,0) - ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0),0) BETWEEN -1000 AND 1000)
		
	)
	--OR (ROUND(C.thanhtien_Tool,0) - ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) BETWEEN 0 AND 1 ))
	-- Loại các phân bổ khuyến mãi cũ nếu KHÔNG có thay đổi hôm nay
	AND NOT (
		C.HopDongChiTietID IN ('664787','685648','720617','665197','659710','734608','751064','703545','662786','654952','657746','659709','668540','664844','667905','686779')
		AND NOT EXISTS (
			SELECT 1 
			FROM dbo.ThucChayDaTinh t 
			WHERE 
				t.HopDongChiTietREF = C.HopDongChiTietID
				AND CAST(t.NgayThucHien AS DATE) = CAST(GETDATE() AS DATE) -- thay đổi hôm nay
		)
	)
	ORDER BY C.DmSanPhamREF DESC


	    
END


```
