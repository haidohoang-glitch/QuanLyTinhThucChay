# Stored Procedure: `sp_nhung_KT_hamtinh_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 09:14:17.213000
- **Ngày sửa cuối**: 2026-03-20 09:14:17.213000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_GGFB
AS
BEGIN
    SET NOCOUNT ON;

    SELECT C.SoHopDong,C.HopDongID,C.HopDongChiTietID,C.DmSanPhamREF,C.TenSanPham,C.SoLuong,C.DonGia,C.ChietKhau,C.ThanhTien
,dbo.FormatNumber(D.tcmm) tcmm,dbo.FormatNumber(ISNULL(D.TCDT,0)) TCDT
,ROUND(ISNULL(D.tcmm,0) - ISNULL(D.TCDT,0), 0) Lệch
FROM (
	SELECT hd.SoHopDong,hd.HopDongID,hdct.HopDongChiTietID,hdct.DmSanPhamREF,hdct.TenSanPham,
	hdct.SoLuong,hdct.DonGia,hdct.ChietKhau,hdct.ThanhTien
	FROM dbo.HopDongChiTiet hdct 
	INNER JOIN dbo.HopDong hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE 1=1
	AND hdct.DmLoaiREF <> 42 
	AND hdct.DmLoaiNenTangREF <> 9
	AND hd.DeletedStatus = 0
	AND hdct.DeletedStatus = 0
	AND hd.TrangThaiHopDong NOT IN (0,3)
	AND hd.Nam >= 2021
	and (hdct.DmSanPhamREF IN ( 306, 423, 5188 )  OR hdct.DmViTriREF IN ( 100093, 100478, 100774 ))
)C LEFT JOIN (	
	SELECT A.Contract_Detail_Id, SUM((CASE WHEN A.ThucChayBan > A.Money_Turnover THEN A.Money_Turnover ELSE A.ThucChayBan END)) tcmm, SUM(B.tcdt ) TCDT
	FROM (	
		SELECT  o.Contract_Number,o.Contract_Id,o.Contract_Detail_Id,															
			SUM(r.Total_Money_VND)TongTienMua, SUM(m.Result)SoLuongThucChay															
			,SUM(m.Sell_Money_VND)ThucChayBan 															
			,SUM(r.Sell_Money_VND)Sell_Money_VND															
			,o.Money_Turnover, o.Id order_id
			FROM [ADS_Operating_Result_Map_Order] m															
			INNER JOIN ADS_Operating_Order o ON o.Id = m.Operating_Order_Id															
			LEFT JOIN ADS_Operating_Result r ON m.operating_Result_Id = r.Id															
			WHERE m.IsDeleted = 0														
			AND m.Sell_Money_VND <> 0		
			--AND o.Contract_Detail_Id ='752755'
			AND NOT ( CONVERT(DATE,m.CreationTime) = CAST(GETDATE() AS DATE) OR  CONVERT(DATE,m.LastModificationTime) = CAST(GETDATE() AS DATE))
			--CAST(@FromDate AS DATE)
			GROUP BY o.Contract_Number,o.Contract_Id,o.Contract_Detail_Id,o.Money_Turnover,o.Id	
		UNION ALL															
			SELECT  o.Contract_Number,o.Contract_Id,o.Contract_Detail_Id,-- m.[LastModificationTime] ,															
			SUM(r.Total_Money_VND)TongTienMua, - 1 SoLuongThucChay															
			,q.TotalMoney ThucChayBan --tương đương r.Sell_Money_VND															
			,SUM(r.Sell_Money_VND)Sell_Money_VND															
			,o.Money_Turnover, o.Id order_id						
			FROM ADS_Operating_Order o															
			INNER JOIN ADS_Operating_Result_Quantity q ON o.Id = q.Operating_Order_Id															
			LEFT JOIN ADS_Operating_Result r ON o.Id = r.Operating_Order_Id															
			WHERE q.IsDeleted = 0				
		GROUP BY o.Contract_Number,o.Contract_Id,o.Contract_Detail_Id,o.Money_Turnover,o.Id,q.TotalMoney	
	) A LEFT JOIN (															
		SELECT HopDongChiTietREF, DmChienDichREF, ROUND(SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0)tcdt															
		FROM ThucChayDaTinh 
		WHERE 1 = 1 												
		AND DmChienDichREF <> 0															
		GROUP BY HopDongChiTietREF, DmChienDichREF															
	)B															
		ON A.Contract_Detail_Id= B.HopDongChiTietREF															
		AND A.order_id = B.DmChienDichREF	
	GROUP BY A.Contract_Detail_Id
)D ON C.HopDongChiTietID = D.Contract_Detail_Id
WHERE ROUND(ISNULL(D.tcmm,0) - ISNULL(D.TCDT,0), 0) NOT IN (-1,0,1) 
AND ROUND(C.ThanhTien - ISNULL(D.TCDT,0),0) > 0
ORDER BY C.HopDongID DESC

END;
```
