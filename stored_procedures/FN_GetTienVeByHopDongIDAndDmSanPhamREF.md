# Function: `GetTienVeByHopDongIDAndDmSanPhamREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-26 11:34:11.893000
- **Ngày sửa cuối**: 2015-04-14 15:31:31.337000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[GetTienVeByHopDongIDAndDmSanPhamREF]
(
	@HopDongID INT, 
	@DmSanPhamREF int
)
RETURNS FLOAT
AS
BEGIN	
	-- Declare the return variable here
	DECLARE @TienVe FLOAT
	SET @TienVe = (	
	SELECT 
		(X.GiaTriTienVe * HD.Tyle)/100 AS TienVe
	FROM
	(
		SELECT hd.HopDongID, hd.SoHopDong,hd.GiaTriHopDong, hdct.TenSanPham
			, SUM(hdct.ThanhTien) AS ThanhTien
			, CASE WHEN hd.GiaTriHopDong <> 0 THEN SUM(hdct.ThanhTien)*110/hd.GiaTriHopDong
				ELSE 100
			  END Tyle
		FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.TrangThaiHopDong <> 3 
		AND hdct.DmSanPhamREF = @DmSanPhamREF		
		AND hdct.ChietKhau <> 100		
		AND hdct.DeletedStatus = 0	
		AND hd.HopDongID = @HopDongID
		GROUP BY hd.HopDongID, hd.SoHopDong,hd.GiaTriHopDong, hdct.TenSanPham
	)HD
	LEFT JOIN
	(
		SELECT tthd.HopDongREF, ROUND(SUM(tthd.GiaTri)/1.1,0) AS GiaTriTienVe  
		FROM ThongTinTienVe tthd	
		WHERE tthd.DeletedStatus = 0 AND tthd.HopDongREF = @HopDongID	
		GROUP BY tthd.HopDongREF
	) X ON HD.HopDongID = X.HopDongREF	
	) 	
	--SELECT @TienVe
	RETURN @TienVe 
END

```
