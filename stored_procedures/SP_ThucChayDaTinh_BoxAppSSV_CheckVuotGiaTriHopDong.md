# Stored Procedure: `ThucChayDaTinh_BoxAppSSV_CheckVuotGiaTriHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-28 16:24:00.213000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.850000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@MaxNgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC dbo.ThucChayDaTinh_BoxAppSSV_CheckVuotGiaTriHopDong '2014-08-27'
CREATE PROCEDURE [dbo].[ThucChayDaTinh_BoxAppSSV_CheckVuotGiaTriHopDong]
	-- Add the parameters for the stored procedure here	
	@MaxNgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	SELECT T1.HopDongID, T1.SoHopDong, T1.ThanhTienThucChay, T2.GiaTriHopDong, 
		ROUND((T1.ThanhTienThucChay - T2.GiaTriHopDong),0) ChenhLech 
	FROM
	(
		SELECT 
			C.HopDongID,C.SoHopDong,
			SUM(C.ThanhTienThucChay) as ThanhTienThucChay
		FROM
		(
			SELECT 
				A.HopDongID, A.SoHopDong,
				SUM(ISNULL(A.ThanhTienSauTrietKhauThucChay,0) + ISNULL(A.GiaTriThayDoi,0)) ThanhTienThucChay
			FROM ThucChayDaTinh A
			WHERE A.TrangThaiHopDong<> 3
				AND A.HopDongID > 0
				AND A.DmSanPhamREF = 375
				AND A.NgayThucHien <= @MaxNgayThucHien
			GROUP BY 
				A.HopDongID, A.SoHopDong
			UNION ALL
			SELECT 
				B.HopDongID, B.SoHopDong,
				SUM(ISNULL(B.ThanhTienSauTrietKhauThucChay,0) + ISNULL(B.GiaTriThayDoi,0)) ThanhTienThucChay
			FROM ThucChayDaTinhAdmarket B
			WHERE B.TrangThaiHopDong<> 3
				AND B.HopDongID > 0
				AND B.DmSanPhamREF = 375
				AND B.NgayThucHien <= @MaxNgayThucHien
			GROUP BY 
				B.HopDongID, B.SoHopDong
		)C
		GROUP BY
			C.HopDongID, C.SoHopDong
	)T1 INNER JOIN
	(
		SELECT 
			hd.HopDongID, hd.SoHopDong,
			SUM(hdct.ThanhTien) as GiaTriHopDong
		FROM HopDong hd
			INNER JOIN HopDongChiTiet hdct ON hdct.HopDongFK = hd.HopDongID
		WHERE
			hdct.DeletedStatus = 0
			AND hd.TrangThaiHopDong <> 3
			AND hdct.DmSanPhamREF = 375
			AND hdct.IsKhuyenMai <> 1
		GROUP BY
			hd.HopDongID, hd.SoHopDong
	)T2 ON T1.HopDongID = T2.HopDongID
	WHERE 
		T1.ThanhTienThucChay > T2.GiaTriHopDong
	
END

```
