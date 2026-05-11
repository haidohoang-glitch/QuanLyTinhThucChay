# Stored Procedure: `ThucChayDaTinh_Admarket_CheckThucChayVuotGiaTriHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-13 16:38:37.563000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.870000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
--	EXEC dbo.ThucChayDaTinh_Admarket_CheckThucChayVuotGiaTriHopDong 144
--
CREATE PROCEDURE [dbo].[ThucChayDaTinh_Admarket_CheckThucChayVuotGiaTriHopDong]
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF	INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT *
	FROM
	(
		SELECT 
			A.SoHopDong, A.ThanhTienThucChay, B.GiaTriHopDong,
			(B.GiaTriHopDong - A.ThanhTienThucChay) Lech
		FROM
		(
			SELECT 
				SoHopDong,
				SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) ThanhTienThucChay
			FROM ThucChayDaTinhAdmarket tcdt
			WHERE 1=1
				--AND tcdt.NgayThucHien >= '2014-01-01'
				AND tcdt.DmSanPhamREF = @DmSanPhamREF
				AND tcdt.SoHopDong <> '' AND tcdt.SoHopDong <> '-'
				--AND tcdt.SoHopDong = 'QC620214'
			GROUP BY 
				tcdt.SoHopDong
		) A INNER JOIN
		(
			SELECT 
				hd.SoHopDong,
				SUM(hdct.ThanhTien) GiaTriHopDong
			FROM HopDong AS hd
				INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
			WHERE 1 = 1
				AND hdct.DmSanPhamREF = @DmSanPhamREF
				AND hd.TrangThaiHopDong <> 3
				AND hdct.IsKhuyenMai = 0
				AND hdct.DeletedStatus = 0
				--AND hd.SoHopDong = 'QC620214'
			GROUP BY hd.SoHopDong
		)B ON B.SoHopDong = A.SoHopDong
	)T
	WHERE T.Lech < 0;
	
	
END

```
