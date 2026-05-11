# Stored Procedure: `ThucChayDaTinhAdmarket_CheckThucChayVuotGiaTriHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.233000
- **Ngày sửa cuối**: 2015-04-02 16:14:29.640000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
--	EXEC dbo.ThucChayDaTinhAdmarket_CheckThucChayVuotGiaTriHopDong
--
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_CheckThucChayVuotGiaTriHopDong]
	-- Add the parameters for the stored procedure here
	--@DmSanPhamREF	INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT *
	FROM
	(
		SELECT 
			A.SoHopDong, B.DmSanPhamREF, B.TenSanPham, A.ThanhTienThucChay, B.GiaTriHopDong,
			ROUND((B.GiaTriHopDong - A.ThanhTienThucChay),0) Lech
		FROM
		(
			SELECT 
				SoHopDong, tcdt.DmSanPhamREF, tcdt.TenSanPham,
				SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) ThanhTienThucChay
			FROM ThucChayDaTinhAdmarket tcdt
			WHERE 1=1				
				AND tcdt.DmSanPhamREF IN (144,585)
				AND tcdt.HopDongID > 0
				AND tcdt.SoHopDong <> '' AND tcdt.SoHopDong <> '-'				
			GROUP BY 
				tcdt.SoHopDong, tcdt.DmSanPhamREF, tcdt.TenSanPham
		) A INNER JOIN
		(
			SELECT HD.SoHopDong, HD.DmSanPhamREF, HD.TenSanPham, SUM(HD.GiaTriHopDong) AS GiaTriHopDong FROM
			(
				SELECT 
					hd.SoHopDong, hdct.DmSanPhamREF, hdct.TenSanPham,
					CASE WHEN hd.TrangThaiHopDong = 3 THEN 0 ELSE SUM(hdct.ThanhTien) END GiaTriHopDong
				FROM HopDong AS hd
					INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
				WHERE 1 = 1
					AND hdct.DmSanPhamREF IN (144,585)				
					AND hdct.IsKhuyenMai = 0
					AND hdct.DeletedStatus = 0
					--AND hd.SoHopDong = 'QC620214'
				GROUP BY hd.SoHopDong, hdct.DmSanPhamREF, hdct.TenSanPham, hd.TrangThaiHopDong
			) HD GROUP BY HD.SoHopDong, HD.DmSanPhamREF, HD.TenSanPham
		)B ON B.SoHopDong = A.SoHopDong AND B.DmSanPhamREF=A.DmSanPhamREF
	)T
	WHERE ROUND(T.Lech,0) < 0;
	
	
END

```
