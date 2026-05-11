# Stored Procedure: `CheckThucChayThieuBrandingAdmatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-01-29 14:55:28.107000
- **Ngày sửa cuối**: 2025-05-31 10:10:31.090000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		nguyenthihongnhung04
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[CheckThucChayThieuBrandingAdmatic] 	
	
AS
BEGIN
	
	SET NOCOUNT ON;
	--Kiểm tra 1 banner treo 2 đơn vị khác nhau. (bỏ qua Admatic + treo không đơn vị)
	SELECT 'TreoTrungDonVi' TreoTrungDonVi, COUNT(DISTINCT DonViTinh_Id) DonViTinh_Id,Banner_Id  FROM ASDAG2.ThucTreo.dbo.ThucTreo WHERE Deleted_Status = 0  AND Product_Formality_Id<>42 AND DonViTinh_Id IS NOT NULL
	AND Banner_Id<>0 
	GROUP BY Banner_Id,DonViTinh_Id
	HAVING COUNT(DISTINCT DonViTinh_Id)>1

	SELECT N'HĐ hủy còn Tiền TC' HĐ_hủy,* FROM(
		SELECT SoHopDong,GiaTriHopDong,NguoiHuyHopDong FROM dbo.HopDong WHERE Nam > = 2022 AND TrangThaiHopDong = 3
	) A INNER JOIN (
		SELECT SoHopDong, SUM(SoLuongThucChay+SoLuongThayDoi) Sl, ROUND(SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0) tt FROM dbo.ThucChayDaTinh
		GROUP BY SoHopDong 
	)B
	ON A.SoHopDong = B.SoHopDong
	WHERE B.tt > 0

	---TH1: Thiếu thực chạy nhóm Branding
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
					,  CASE WHEN E.DonViTinhREF = 10 AND E.DmDonViTinhREF_Tool = 1 THEN SUM(F.TongViewThucChay) 
							WHEN E.DonViTinhREF = 10 AND E.DmDonViTinhREF_Tool = 2 THEN SUM(F.TongClickThucChay) 
							WHEN E.DmDonViTinhREFHĐ = 1 THEN SUM(F.TongViewThucChay) 
							WHEN E.DmDonViTinhREFHĐ = 2 THEN SUM(F.TongClickThucChay)
							ELSE 0 END				
					AS Soluong_tool  
				FROM (
					SELECT DISTINCT(tchd.DmBannerREF),hdct1.DonViTinhREF,tchd.HopDongChiTietREF ,tchd.DmDonViTinhREF DmDonViTinhREF_Tool ,hdct1.DonViTinhREF AS DmDonViTinhREFHĐ 
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
					--AND tchd.HopDongChiTietREF ='752126'
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
				--WHERE E.HopDongChiTietREF ='752126'
				GROUP BY E.HopDongChiTietREF ,E.DmDonViTinhREF_Tool,E.DmDonViTinhREFHĐ,DonGiaTool,E.ChietKhau,E.DonViTinhREF
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
					--WHERE S.HopDongChiTietREF ='752126'
					GROUP BY S.HopDongChiTietREF,S.ChietKhau			
				)b	
			)
		)B
		ON A.HopDongChiTietID=B.HopDongChiTietREF
		--WHERE A.HopDongChiTietID ='752126'
		GROUP BY A.SoHopDong,A.DmSanPhamREF,A.HopDongChiTietID,A.SoLuong,A.DonGia,A.ThanhtienHD,A.ChietKhau
	)C LEFT JOIN(
		SELECT TCDT.HopDongChiTietREF,SUM(TCDT.SoLuongThucChay+TCDT.SoLuongThayDoi) AS SL,SUM(TCDT.ThanhTienSauTrietKhauThucChay+TCDT.GiaTriThayDoi) AS thanhtien
		,SUM(TCDT.SoLuongThucChayKM + TCDT.SoLuongKMThayDoi) AS SLKM,SUM(TCDT.ThanhTienKM +TCDT.GiaTriKMThayDoi) AS thanhtienKM
		FROM dbo.ThucChayDaTinh TCDT
		WHERE TCDT.DmHinhThucQuangCao NOT IN (13,42)
		GROUP BY TCDT.HopDongChiTietREF
	)D
	ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE 1=1
	--AND C.HopDongChiTietID ='752126'
	--AND C.SoHopDong ='NB0100124'
	AND NOT ( C.ThanhtienHD = ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0)
	OR (ROUND(C.thanhtien_Tool,0) - ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) BETWEEN 0 AND 1 ))
	AND NOT C.SoHopDong IN ('QC4070622') ---HĐ cũ trước ghi nhận = tay
	AND NOT C.HopDongChiTietID IN (654952,665197,685648,664787) --PB khuyến mãi cũ
	ORDER BY C.DmSanPhamREF DESC

	---TH2. Thiếu TC nhóm Admatic
	SELECT 'Admatic' Thiếu_Admatic,  C.SoHopDong,C.DmSanPhamREF,C.HopDongChiTietID,C.DonViTinh,dbo.formatnumber(C.SoluongHD) SLHĐ,C.ChietKhau, C.ThanhtienHD
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN C.SLKM_tool ELSE C.SLTC_tool END,0) AS SoluongTool
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN C.TTKM_tool ELSE C.TTTC_tool END,0) AS ThanhTienTool
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM,0) ELSE ISNULL(D.SL,0) END,0) AS SoluongTC
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) AS ThanhtienTC
	,dbo.FormatNumber((ROUND( CASE WHEN C.ChietKhau = 100 THEN C.TTKM_tool ELSE C.TTTC_tool END,0) - ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0))) LechSP_Tool
    ,dbo.FormatNumber((C.ThanhtienHD - ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0))) LechHD_TC
	FROM (
		SELECT * FROM (
			SELECT hd.SoHopDong,hdct.HopDongChiTietID,hdct.DonViTinh
			,CASE WHEN hdct.DonViTinhREF = 1 THEN hdct.SoLuong*1000 ELSE hdct.SoLuong END AS SoluongHD
			,CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong * hdct.DonGia ELSE hdct.ThanhTien END AS ThanhtienHD
			,hdct.ChietKhau,hdct.DonGia, hdct.ThanhTien,hdct.DmSanPhamREF 
			,(hdct.SoLuong * hdct.DonGia ) ThanhtienKM
			FROM dbo.HopDong hd 
			INNER JOIN dbo.HopDongChiTiet hdct 
			ON hd.HopDongID=hdct.HopDongFK
			WHERE 1=1
			AND hd.Nam >= 2022 
			AND NOT hdct.DmLoaiNenTangREF = 9
			AND hdct.DmLoaiREF = 42
			AND NOT hdct.DmSanPhamREF IN (817,140,549)
			AND NOT hdct.DonViTinhREF IN ( 7,84) 
			--AND hd.SoHopDong ='QC6060822'
		)A INNER JOIN(
		SELECT E.HopDongChiTietREF,SUM(F.SLTC) SLTC_tool,SUM(F.TTTC) TTTC_tool,SUM(F.SLKM) SLKM_tool, SUM(F.TTKM) TTKM_tool
		FROM (
			SELECT DISTINCT(tchdct.DmBannerREF),dbo.GetSoHopDongByID(tchdct.HopDongREF) Sohopdong,tchdct.HopDongChiTietREF	,tchdct.DmSanPhamREF	
			FROM  dbo.ThucChayHopDongChiTiet tchdct
			WHERE tchdct.DeletedStatus = 0
			--And tchdct.HopDongChiTietREF ='752576'
			) E left JOIN (
				SELECT tc.SoHopDong,tc.DmBannerID,tc.DmSanPhamREF, SUM(tc.SoLuongThucChay) SLTC, SUM(tc.ThanhTienThucChaySauCK_ChuaVAT) TTTC, SUM(tc.SoLuongThucChayKM) SLKM, SUM(tc.ThanhTienThucChayKM) TTKM
				FROM ThucChay_ThanhTien_Admatic tc
				WHERE NOT tc.SoHopDong ='HD DEMO' 
				--AND tc.DmBannerID IN ('89276','89277') 
				GROUP BY tc.DmBannerID,tc.SoHopDong,tc.DmSanPhamREF
			) F 
			ON CONVERT(NVARCHAR(500),E.DmBannerREF) = CONVERT(NVARCHAR(500),F.DmBannerID) AND E.Sohopdong = f.SoHopDong AND E.DmSanPhamREF = F.DmBannerID
			--WHERE E.HopDongChiTietREF ='752576'
			GROUP BY E.HopDongChiTietREF
		)B
		ON A.HopDongChiTietID=B.HopDongChiTietREF

	)C LEFT JOIN(
		SELECT HopDongChiTietREF,SUM(SoLuongThucChay+SoLuongThayDoi) AS SL,SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) AS thanhtien
		,SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SLKM,SUM(ThanhTienKM +GiaTriKMThayDoi) AS thanhtienKM
		FROM dbo.ThucChayDaTinh tcdt
		WHERE DmHinhThucQuangCao = 42
		GROUP BY HopDongChiTietREF
	)D
	ON C.HopDongChiTietREF = D.HopDongChiTietREF
	WHERE 1=1 
	--AND C.HopDongChiTietID ='752576'
	--AND C.SoHopDong IN ('QC1770125') -- Do đã thanh lý năm 2022
	AND NOT ROUND(C.ThanhtienHD,0)  = ROUND ( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0)
	AND NOT ROUND( CASE WHEN C.ChietKhau = 100 THEN C.TTKM_tool ELSE C.TTTC_tool END,0)  = ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0)
	ORDER BY C.DmSanPhamREF,C.ChietKhau DESC

	SELECT 'Inventory' Thiếu_Inventory, C.SoHopDong,C.DmSanPhamREF,C.HopDongChiTietID,C.DonViTinh,dbo.formatnumber(C.SoluongHD) SLHĐ,C.ChietKhau,C.DonGia
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END,0) AS ThanhtienHD
	,ROUND( CASE WHEN C.DonViTinhREF = 1 THEN C.TongViewThucChay ELSE C.TongClickThucChay END,0) AS SoluongTool
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM,0) ELSE ISNULL(D.SL,0) END,0) AS SoluongTC
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) AS ThanhtienTC
	, ROUND( CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END,0) - ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) ThanhtienHD_TC
	FROM (
		SELECT * FROM (
			SELECT hd.SoHopDong,hdct.HopDongChiTietID,hdct.DonViTinhREF,hdct.DonViTinh
			,CASE WHEN hdct.DonViTinhREF = 1 THEN hdct.SoLuong*1000 ELSE hdct.SoLuong END AS SoluongHD
			,hdct.ChietKhau, hdct.ThanhTien,hdct.DmSanPhamREF ,hdct.DonGia,(hdct.SoLuong * hdct.DonGia ) ThanhtienKM
			FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
			ON hd.HopDongID=hdct.HopDongFK
			WHERE 1=1 AND hdct.DmLoaiNenTangREF = 9 AND hd.Nam >= 2022 AND NOT hdct.DmSanPhamREF IN (817,253)
			--AND hd.SoHopDong ='NB0190722'
		)A INNER JOIN(
			SELECT E.HopDongChiTietREF,SUM(TongViewThucChay) TongViewThucChay, SUM(TongClickThucChay) TongClickThucChay FROM (
			SELECT DISTINCT(DmBannerREF),HopDongChiTietREF FROM dbo.ThucChayHopDongChiTiet WHERE DeletedStatus = 0
			)E INNER JOIN (
			SELECT tc.DmBannerREF,SUM(tc.TongViewThucChay) TongViewThucChay	, SUM(tc.TongClickThucChay) TongClickThucChay
			FROM dbo.ThucChay tc
			GROUP BY tc.DmBannerREF
			)F 
			ON CONVERT(NVARCHAR(1000),E.DmBannerREF) = CONVERT(NVARCHAR(1000),F.DmBannerREF)
			GROUP BY E.HopDongChiTietREF
		)B
		ON A.HopDongChiTietID =  B.HopDongChiTietREF
	)C LEFT JOIN(
		SELECT TCDT.HopDongChiTietREF,SUM(TCDT.SoLuongThucChay+TCDT.SoLuongThayDoi) AS SL,SUM(TCDT.ThanhTienSauTrietKhauThucChay+TCDT.GiaTriThayDoi) AS thanhtien
		,SUM(TCDT.SoLuongThucChayKM + TCDT.SoLuongKMThayDoi) AS SLKM,SUM(TCDT.ThanhTienKM +TCDT.GiaTriKMThayDoi) AS thanhtienKM
		FROM dbo.ThucChayDaTinh TCDT
		WHERE 1=1 AND NOT DmSanPhamREF IN (817,253)
		--AND TCDT.SoHopDong ='NB0190722'
		--AND YEAR(TCDT.NgayThucHien)= 2022
		GROUP BY TCDT.HopDongChiTietREF

	)D
	ON C.HopDongChiTietREF = D.HopDongChiTietREF
	WHERE 1=1
	AND NOT ROUND( CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END,0) - ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) = 0
	AND NOT C.DmSanPhamREF IN (817,253)
	ORDER BY C.DmSanPhamREF,C.ChietKhau DESC


	---Th3: True view
	SELECT 'True_View' Thiếu_True_View, C.SoHopDong,C.DmSanPhamREF,C.HopDongChiTietID,dbo.formatnumber(C.SoluongHD) SLHĐ,C.ChietKhau,C.DonGia DonGiaHĐ
	,dbo.FormatNumber( CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END) AS ThanhtienHD
	--,ROUND(C.TongTrue_ViewThucChay,0) AS SoluongTool
	,dbo.FormatNumber(CASE WHEN C.ChietKhau = 100 THEN ROUND(C.TongTrue_ViewThucChay * C.DonGia,0) ELSE ROUND(C.TongTrue_ViewThucChay * C.DonGia * (100-C.ChietKhau)/100,0) END) Thanhtien_tool
	--,ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM,0) ELSE ISNULL(D.SL,0) END,0) AS SoluongTC
	,dbo.FormatNumber( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END) AS ThanhtienTC
	,ROUND(CASE WHEN C.ChietKhau = 100 THEN ROUND(C.TongTrue_ViewThucChay * C.DonGia,0) ELSE ROUND(C.TongTrue_ViewThucChay * C.DonGia * (100-C.ChietKhau)/100,0) END,0) - ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) Lech_SP_ASD
	,ROUND(CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END,0) - ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) Lech_HĐ_ASD
	FROM (
		SELECT * FROM (
			SELECT hd.SoHopDong,hdct.HopDongChiTietID,hdct.DonViTinhREF,hdct.DonViTinh
			,CASE WHEN hdct.DonViTinhREF = 1 THEN hdct.SoLuong*1000 ELSE hdct.SoLuong END AS SoluongHD
			,hdct.ChietKhau, hdct.ThanhTien,hdct.DmSanPhamREF ,hdct.DonGia,(hdct.SoLuong * hdct.DonGia ) ThanhtienKM
			FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
			ON hd.HopDongID=hdct.HopDongFK
			WHERE hdct.DmSanPhamREF IN (339,240,598,342,505,733,5056,5299) 
			AND hdct.DonViTinhREF = 32
			AND hd.Nam >=2022 AND NOT hdct.DmLoaiNenTangREF = 9
			AND NOT hdct.DmLoaiREF = 42
			--AND hd.SoHopDong ='QC0580122'
		)A INNER JOIN(
			SELECT E.HopDongChiTietREF,SUM(TongTrue_ViewThucChay) TongTrue_ViewThucChay FROM (
			SELECT DISTINCT(DmBannerREF),HopDongChiTietREF FROM dbo.ThucChayHopDongChiTiet WHERE DeletedStatus = 0
			)E INNER JOIN (
			SELECT tc.bannerid,SUM(tc.True_View) TongTrue_ViewThucChay
			FROM dbo.ThucChayTrueView tc
			--WHERE tc.SoHopDong ='QC1960422'
			GROUP BY tc.bannerid
			)F 
			ON CONVERT(NVARCHAR(1000), E.DmBannerREF) = CONVERT(NVARCHAR(1000),F.bannerid)
			GROUP BY E.HopDongChiTietREF
		)B
		ON A.HopDongChiTietID=B.HopDongChiTietREF

	)C LEFT JOIN(
		SELECT TCDT.HopDongChiTietREF,SUM(TCDT.SoLuongThucChay+TCDT.SoLuongThayDoi) AS SL,SUM(TCDT.ThanhTienSauTrietKhauThucChay+TCDT.GiaTriThayDoi) AS thanhtien
		,SUM(TCDT.SoLuongThucChayKM + TCDT.SoLuongKMThayDoi) AS SLKM,SUM(TCDT.ThanhTienKM +TCDT.GiaTriKMThayDoi) AS thanhtienKM	
		FROM dbo.ThucChayDaTinh TCDT
		WHERE TCDT.DmHinhThucQuangCao NOT IN (13,42)
		AND TCDT.DmSanPhamREF IN (339,240,598,342,505,733,821,5133,5056)
		--AND YEAR(TCDT.NgayThucHien)= 2022
		GROUP BY TCDT.HopDongChiTietREF
	)D
	ON C.HopDongChiTietREF = D.HopDongChiTietREF
	WHERE 1=1
	AND NOT ROUND( CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END,0) = ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0)
	AND NOT ROUND(C.TongTrue_ViewThucChay,0) = ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM,0) ELSE ISNULL(D.SL,0) END,0)
	ORDER BY C.DmSanPhamREF


	--TH4: HĐ ký bài
	SELECT 'Bài' Thiếu_Bài, C.SoHopDong,C.DmSanPhamREF,C.HopDongChiTietID,C.DonViTinh,dbo.formatnumber(C.SoluongHD) SLHĐ,C.ChietKhau,C.DonGia
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END,0) AS ThanhtienHD
	,C.LinkTreo,C.DonGiaTreo
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN (C.LinkTreo* C.DonGiaTreo)  ELSE (C.LinkTreo* C.DonGiaTreo * (100-C.ChietKhau)/100)  END,0) AS ThanhtienTreo
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM,0) ELSE ISNULL(D.SL,0) END,0) AS SoluongTC
	,ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) AS ThanhtienTC
	FROM (
		SELECT A.SoHopDong,A.HopDongChiTietID,A.DmSanPhamREF,A.DonViTinhREF,A.DonViTinh,A.SoluongHD,A.DonGia,A.ChietKhau,A.ThanhTien,A.ThanhtienKM,SUM(B.Link) LinkTreo,B.DonGiaTreo
		FROM (
			SELECT hd.SoHopDong,hdct.HopDongChiTietID,hdct.DonViTinhREF,hdct.DonViTinh
			,CASE WHEN hdct.DonViTinhREF = 1 THEN hdct.SoLuong*1000 ELSE hdct.SoLuong END AS SoluongHD
			,hdct.ChietKhau, hdct.ThanhTien,hdct.DmSanPhamREF ,hdct.DonGia,(hdct.SoLuong * hdct.DonGia ) ThanhtienKM
			FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
			ON hd.HopDongID=hdct.HopDongFK
			WHERE hdct.DmSanPhamREF IN (339,240,598,342,505,733,5056,5299) 
			AND hdct.DonViTinhREF = 7
			AND hd.Nam >= 2022 AND NOT hdct.DmLoaiNenTangREF = 9
			AND NOT hdct.DmLoaiREF = 42
			--AND hd.SoHopDong ='QC0220422'
		)A INNER JOIN(		
			SELECT HopDongChiTietREF, COUNT(DISTINCT(Link)) Link,DonGia AS DonGiaTreo
			FROM dbo.ThucChayHopDongChiTiet
			WHERE DeletedStatus = 0
			GROUP BY DmBannerREF,DonGia,HopDongChiTietREF 		
		)B
		ON A.HopDongChiTietID=B.HopDongChiTietREF
		GROUP BY A.SoHopDong,A.HopDongChiTietID,A.DmSanPhamREF,A.DonViTinhREF,A.DonViTinh,A.SoluongHD,A.DonGia,A.ChietKhau,A.ThanhTien,A.ThanhtienKM,B.DonGiaTreo
	)C LEFT JOIN(
		SELECT TCDT.HopDongChiTietREF,SUM(TCDT.SoLuongThucChay+TCDT.SoLuongThayDoi) AS SL,SUM(TCDT.ThanhTienSauTrietKhauThucChay+TCDT.GiaTriThayDoi) AS thanhtien
		,SUM(TCDT.SoLuongThucChayKM + TCDT.SoLuongKMThayDoi) AS SLKM,SUM(TCDT.ThanhTienKM +TCDT.GiaTriKMThayDoi) AS thanhtienKM	
		FROM dbo.ThucChayDaTinh TCDT
		WHERE TCDT.DmHinhThucQuangCao NOT IN (13,42)
		AND TCDT.DmSanPhamREF IN (339,240,598,342,505,733,821,5133,5056)
		--AND YEAR(TCDT.NgayThucHien)= 2022
		GROUP BY TCDT.HopDongChiTietREF
	)D
	ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE 1=1
	AND C.LinkTreo <> ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM,0) ELSE ISNULL(D.SL,0) END,0) 
	AND C.LinkTreo <= C.SoluongHD 
	AND NOT C.SoHopDong IN ('QC3990922','QC2180822') -- HĐ trước view đã đối trừ = 0
	ORDER BY C.DmSanPhamREF,C.ChietKhau DESC

	---Th5 : HĐ ký đơn vị ngày
	SELECT 'DonViNgay' Thieu_Branding_Ngay,C.SoHopDong,C.HopDongChiTietID,C.SoLuongHĐ,ROUND(C.DonGia, 0) DonGia,C.ChietKhau,
	CASE WHEN C.ChietKhau = 100 THEN ROUND(C.ThanhtienKM, 0) ELSE C.ThanhtienHD END thanhtienHĐ,C.SoLuongTreo,
	CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongKM, 0) ELSE ISNULL(D.SoluongTC, 0) END SoluongTC,
	CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0) ELSE ISNULL(D.thanhtienTC, 0) END thanhtienTC
	FROM (	
		SELECT A.SoHopDong,A.HopDongChiTietID,DonGia, A.ChietKhau,ROUND(A.ThanhTien, 0) ThanhtienHD,SUM(B.SoLuongTreo) SoLuongTreo,A.ThanhtienKM, SUM(A.SoLuongDC) AS SoLuongHĐ
		FROM(
			SELECT DISTINCT (dchdct.BookingREF),hd.SoHopDong, hdct.HopDongChiTietID, hdct.SoLuong, hdct.ChietKhau, hdct.DonGia,hdct.ThanhTien,(hdct.SoLuong * hdct.DonGia) AS ThanhtienKM,     DATEDIFF(DAY, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1 AS SoLuongDC
			FROM dbo.HopDongChiTiet hdct
			INNER JOIN dbo.HopDong hd    ON hd.HopDongID = hdct.HopDongFK
			LEFT JOIN DotChayHopDongChiTiet dchdct  ON (  hdct.HopDongChiTietID = dchdct.HopDongChiTietREF  AND dchdct.DeletedStatus <> 1)
			WHERE hdct.DmSanPhamREF NOT IN ( 140, 228, 549, 385, 564, 5007, 5005, 736, 5082, 252, 5006 ) --sp không phải CPD 
			AND hd.Nam >= 2022 
			AND hdct.DonViTinhREF IN (3,4) -- đơn vị ngày, tuần	
		) A
		LEFT JOIN
		(
		SELECT DISTINCT (tchdct.BookingREF),                tchdct.ThoiGianBatDau,                tchdct.ThoiGianKetThuc,                tchdct.HopDongChiTietREF,
		CASE WHEN CONVERT(DATE, tchdct.ThoiGianKetThuc) > GETDATE() - 1 THEN DATEDIFF(DAY, tchdct.ThoiGianBatDau, GETDATE() - 1) + 1
		ELSE DATEDIFF(DAY, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc) + 1
		END AS SoLuongTreo
		--,DATEDIFF(DAY,tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc)+1 AS SoLuongTreo  
		FROM ThucChayHopDongChiTiet tchdct
		WHERE tchdct.DeletedStatus = 0 --AND tchdct.HopDongChiTietREF  = '691701'
		AND NOT (CONVERT(DATE, tchdct.CreatedAt) > GETDATE() - 1 OR CONVERT(DATE, tchdct.LastModifiedAt) > GETDATE() - 1)
		) B
		ON A.HopDongChiTietID = B.HopDongChiTietREF
		AND A.BookingREF = B.BookingREF 
		WHERE B.SoLuongTreo > 0 GROUP BY A.SoHopDong,A.HopDongChiTietID,A.DonGia,A.ChietKhau,A.ThanhTien,A.ThanhtienKM
	) C LEFT JOIN (
		SELECT HopDongChiTietREF,
		SUM(SoLuongThucChay + SoLuongThayDoi) SoluongTC,
		SUM(SoLuongThucChayKM + SoLuongKMThayDoi) SoluongKM,
		ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) thanhtienTC,
		ROUND(SUM(ThanhTienKM + GiaTriKMThayDoi), 0) thanhtienKM
		FROM ThucChayDaTinh 
		GROUP BY HopDongChiTietREF
	) D
	ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE 1 = 1 
	AND (ABS( CASE WHEN C.ChietKhau = 100 THEN ROUND(C.ThanhtienKM, 0) ELSE C.ThanhtienHD END- CASE  WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0) ELSE ISNULL(D.thanhtienTC, 0) END)> 1000)
	ORDER BY C.SoHopDong;

	---Th6 : Check phan bo Admatic - Adpage - donvi BAI co tinh KHONG DUNG Thuc chay
	SELECT 'Admatic' Admatic_Bai_URL,C.SoHopDong,C.HopDongID,C.HopDongChiTietID,C.DonViTinh,C.SoLuong,dbo.FormatNumber(C.DonGia) ĐonGiaHĐ,C.ChietKhau
	,dbo.FormatNumber(CASE WHEN C.ChietKhau = 100 THEN C.SoLuong*C.DonGia ELSE C.ThanhTien END) ThanhTienHĐ
	,ISNULL(C.Soluongtreo,0) Soluongtreo
	,dbo.FormatNumber(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM,0) ELSE ISNULL(D.SoluongTC,0) END ) SoluongTC_ASD
	,dbo.FormatNumber(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhtienTCKM,0) ELSE ISNULL(D.ThanhtienTC,0) END) ThanhtienTC_ASD
	FROM(
		SELECT A.*,B.Soluongtreo FROM(
			SELECT hd.HopDongID,hd.SoHopDong,hdct.HopDongChiTietID,hdct.DonViTinh,hdct.SoLuong,hdct.DonGia,hdct.ChietKhau,hdct.ThanhTien FROM dbo.HopDongChiTiet hdct
			INNER JOIN dbo.HopDong hd
			ON hd.HopDongID = hdct.HopDongFK
			WHERE 1=1 --hdct.DmSanPhamREF IN ( 305,5312,598) 
			AND hdct.DonViTinhREF IN ( 7,84)
			AND hdct.DmLoaiREF = 42
			AND hd.DeletedStatus = 0
			AND hdct.DeletedStatus = 0
			AND hd.TrangThaiHopDong NOT IN (0,3)
		)A LEFT JOIN (
			SELECT COUNT(*) Soluongtreo,tt.HopDongChiTietREF
			FROM dbo.ThucChayHopDongChiTiet tt
			WHERE tt.DeletedStatus =0
			GROUP BY tt.HopDongChiTietREF
		)B ON A.HopDongChiTietID = B.HopDongChiTietREF
	)C LEFT JOIN (
		SELECT tcdt.HopDongChiTietREF
		,SUM(tcdt.SoLuongThucChay+tcdt.SoLuongThayDoi) SoluongTC
		,SUM(tcdt.SoLuongThucChayKM+tcdt.SoLuongKMThayDoi) SoluongTCKM
		,SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi) ThanhtienTC
		,SUM(tcdt.ThanhTienKM+tcdt.GiaTriKMThayDoi) ThanhtienTCKM
		FROM dbo.ThucChayDaTinh tcdt
		GROUP BY tcdt.HopDongChiTietREF
	)D ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE ISNULL(C.Soluongtreo,0) <> C.SoLuong
		AND ISNULL(C.Soluongtreo,0) <> CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM,0) ELSE ISNULL(D.SoluongTC,0) END 
		AND CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM,0) ELSE ISNULL(D.SoluongTC,0) END <> C.SoLuong
		AND NOT C.SoHopDong IN ('QC10331221','QC8240322','TR0010921')
	ORDER BY C.HopDongID

	END

```
