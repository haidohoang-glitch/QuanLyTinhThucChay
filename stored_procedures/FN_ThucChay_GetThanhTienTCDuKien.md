# Function: `ThucChay_GetThanhTienTCDuKien`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-26 17:28:53.960000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.770000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPham` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienTCDuKien]
(
	-- Add the parameters for the function here
	@HopDongID INT,
	@DmSanPham INT,
	@StartDate DATETIME,
	@EndDate DATETIME
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChayDK FLOAT
	DECLARE @SoLuongTC INT
	DECLARE @SoLuongHD INT
	DECLARE @DonGia FLOAT
	--TINH CPD (140,228,241)
	IF(@DmSanPham IN (140,228,241))
	BEGIN
		SET @ThanhTienThucChayDK = 
		(
			SELECT SUM(ISNULL(A.thanhtiendukien,0)) thanhtientcdk FROM 
			(
				SELECT (dchdct.soluong * hdct.DongiaKC) thanhtiendukien, hdct.HopDongFK, hdct.HopDongChiTietID
						, hdct.DmSanPhamREF, hdct.TenSanPham
				FROM (
					SELECT ISNULL(sum(DATEDIFF(day, A.ThoiGianBatDauKQ, A.ThoiGianKetThucKQ) + 1),0) soluong ,A.HopDongREF, A.HopDongChiTietREF
					FROM
					( 
						SELECT
						(CASE when CONVERT(DATE,A.ThoiGianBatDau) < '2013-01-01' then '2013-01-01'
							else A.ThoiGianBatDau
						  END
						) as ThoiGianBatDauKQ
						,(CASE when CONVERT(DATE,A.ThoiGianKetThuc) > '2013-12-31' then '2013-12-31'
							else A.ThoiGianKetThuc
						  END
						) as ThoiGianKetThucKQ,
						A.HopDongREF, A.HopDongChiTietREF
						FROM DotChayHopDongChiTiet A
						WHERE NOT ((CONVERT(DATE,A.ThoiGianBatDau) > '2013-12-31') OR (CONVERT(DATE,A.ThoiGianKetThuc) < '2013-01-01'))
						AND A.HopDongREF = @HopDongID
					)A
					GROUP BY A.HopDongREF, A.HopDongChiTietREF
				) dchdct
				INNER JOIN 
				(
					SELECT (ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(A.SoLuong,A.DonViTinh,A.DonGia,'2013-08-08', '2013-08-30', A.HopDongChiTietID),0)*(100 - A.ChietKhau))/100 DongiaKC 
					--(A.ThanhTien/A.SoLuong) DongiaKC
					, A.HopDongFK, a.HopDongChiTietID, A.DmSanPhamREF, a.TenSanPham
					  FROM HopDongChiTiet A
					WHERE A.DmSanPhamREF = @DmSanPham
					AND A.HopDongFK = @HopDongID
				) hdct ON dchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			)A
			GROUP BY A.HopDongFK, A.DmSanPhamREF, A.TenSanPham
		)		
	END 
	/*
	ELSE--TINH CPM(231,238,339,342,337,240,370)
		BEGIN
			IF(@DmSanPham IN(231,238,339,342,337,240,370))
			BEGIN
				SET @SoLuongTC = 
				(
					SELECT SUM(tcdt.SoLuongThucChay) soluongtc
					  FROM ThucChayDaTinh tcdt
					WHERE tcdt.DmSanPhamREF = @DmSanPham
					AND tcdt.HopDongID = @HopDongID 
					AND CONVERT(DATE,tcdt.NgayThucHien) <= '2013-08-25'
					GROUP BY TCDT.HopDongID, TCDT.DmSanPhamREF
				)
				SET @SoLuongHD = 
				(
					SELECT SUM(ISNULL(HDCT.SoLuong,0))*1000 FROM HopDongChiTiet hdct
					WHERE HDCT.HopDongFK = @HopDongID AND HDCT.DmSanPhamREF = @DmSanPham
					GROUP BY HDCT.HopDongFK ,HDCT.DmSanPhamREF
				) 
				SET @DonGia = 
				(
					SELECT MAX(HDCT.ThanhTien/(HDCT.SoLuong*1000)) 
					FROM HopDongChiTiet hdct
					WHERE HDCT.HopDongFK = @HopDongID 
					AND HDCT.DmSanPhamREF = @DmSanPham
					GROUP BY HDCT.HopDongFK ,HDCT.DmSanPhamREF
				)
				SET @ThanhTienThucChayDK =
				(	
					CASE when ISNULL(@SoLuongHD,0) < ISNULL(@SoLuongTC,0) then 0
					else ISNULL((ISNULL(@SoLuongHD,0) - ISNULL(@SoLuongTC,0))*ISNULL(@DonGia,0),0)
					END
				) 
			END
			ELSE--TINH PR(141,245,250)
				BEGIN
					IF(@DmSanPham IN (141,245,250))
					BEGIN
						SET @SoLuongTC = 
						(
							SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay) soluongtc
							  FROM ThucChayDaTinh tcdt
							WHERE tcdt.DmSanPhamREF = 141
							AND tcdt.HopDongID = 18978 
							AND CONVERT(DATE,tcdt.NgayThucHien) <= '2013-08-25'
							GROUP BY TCDT.HopDongID, TCDT.DmSanPhamREF
						)
						SET @SoLuongHD = 
						(
							SELECT SUM(ISNULL(HDCT.ThanhTien,0)) FROM HopDongChiTiet hdct
							WHERE HDCT.HopDongFK = 18978 AND HDCT.DmSanPhamREF = 141
							GROUP BY HDCT.HopDongFK ,HDCT.DmSanPhamREF
						) 
						SET @ThanhTienThucChayDK =
						(	
							CASE when ISNULL(@SoLuongHD,0) < ISNULL(@SoLuongTC,0) then 0
							else ISNULL((ISNULL(@SoLuongHD,0) - ISNULL(@SoLuongTC,0)),0)
							END
						) 
					END
				END
		END
		*/
	IF(@ThanhTienThucChayDK IS NULL)
	BEGIN
		SET @ThanhTienThucChayDK = 0
	END
	RETURN @ThanhTienThucChayDK
END


--SELECT  [dbo].[ThucChay_GetThanhTienTCDuKien](18978,141,'2013-08-26','2013-12-31')


```
