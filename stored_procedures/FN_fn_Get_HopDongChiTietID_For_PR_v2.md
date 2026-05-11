# Function: `fn_Get_HopDongChiTietID_For_PR_v2`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-10 14:17:32.977000
- **Ngày sửa cuối**: 2017-05-15 10:40:29.540000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@HopDongREF` | `int(4)` | No |
| `@ChietKhau` | `int(4)` | No |
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@DonGia` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
select  [dbo].[fn_Get_HopDongChiTietID_For_PR_v2]
(
	@HopDongREF ,
	@ChietKhau ,
	@ThucChayHopDongChiTietPRID ,
	@HopDongChiTietREF ,
	@DmHinhThucQuangCaoREF ,
	@DmSanPhamREF ,
	@DmWebsiteREF ,
	@DonGia 
)

*/
CREATE FUNCTION [dbo].[fn_Get_HopDongChiTietID_For_PR_v2]
(
	@HopDongREF INT,
	@ChietKhau INT,
	@ThucChayHopDongChiTietPRID INT,
	@HopDongChiTietREF INT,
	@DmHinhThucQuangCaoREF INT,
	@DmSanPhamREF INT,
	@DmWebsiteREF INT,
	@DonGia INT
)
RETURNS BIGINT

BEGIN
	DECLARE @out INT, @Count_HopDongChiTietID INT, @v_HopDongChiTietID INT
	SET @out = 0
		IF(@ChietKhau = 100)
		BEGIN
			SET @out =
			(
				SELECT TOP 1 hdct.HopDongChiTietID 
				FROM HopDongChiTiet hdct
				WHERE hdct.HopDongFK = @HopDongREF
				AND hdct.DmSanPhamREF in (141,245,250,637,305) --PR
				AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)--Mua ngoai
				AND hdct.ChietKhau = 100
				AND hdct.DeletedStatus = 0
				AND hdct.DmSanPhamREF = @DmSanPhamREF
				AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
				ORDER BY hdct.HopDongChiTietID DESC
			)
			SET @out = ISNULL(@out,0)
			IF(@out = 0)
			 BEGIN
			 	 SET @out = 
			 	 (
					SELECT TOP 1 A.HopDongChiTietID FROM
						(
							SELECT hdct.HopDongFK,hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.ThanhTien,
							SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))ThanhTienThucChay
							  FROM ThucChayDaTinh tcdt
							  RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
							  AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
							WHERE 1=1
							and hdct.HopDongFK =@HopDongREF
							AND hdct.DmSanPhamREF in (141,245,250,637,305) --PR
							AND hdct.DmSanPhamREF = @DmSanPhamREF
							AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
							AND hdct.DeletedStatus = 0
							AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)--Mua ngoai
							GROUP BY hdct.HopDongFK,hdct.HopDongChiTietID, hdct.DmSanPhamREF,hdct.ThanhTien
						)A
						WHERE 1=1
						ORDER BY A.HopDongChiTietID
				)
			 END
		END	
		ELSE
		BEGIN
				SET @Count_HopDongChiTietID = (
						SELECT COUNT(hdct.HopDongChiTietID)
							  FROM ThucChayDaTinh tcdt
							  RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
							  AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
							WHERE 1=1
							and hdct.HopDongFK =@HopDongREF
							AND hdct.DmSanPhamREF in (141,245,250,637,305) --PR
							AND hdct.DmSanPhamREF = @DmSanPhamREF
							AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
							AND hdct.DeletedStatus = 0
							AND hdct.DmWebsiteREF = @DmWebsiteREF
							AND hdct.DonGia = @DonGia
							AND hdct.ChietKhau = @ChietKhau
							AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)--Mua ngoai
							GROUP BY hdct.HopDongFK, hdct.DmSanPhamREF
				)
				IF(@Count_HopDongChiTietID = 1)
				BEGIN
					SET @out =
					(
						SELECT TOP 1 A.HopDongChiTietID FROM
						(
							SELECT hdct.HopDongChiTietID
							, SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))ThanhTienThucChay
								  FROM ThucChayDaTinh tcdt
								  RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
								  AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
								WHERE 1=1
								and hdct.HopDongFK =@HopDongREF
								AND hdct.DmSanPhamREF in (141,245,250,637,305) --PR
								AND hdct.DmSanPhamREF = @DmSanPhamREF
								AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
								AND hdct.DeletedStatus = 0
								AND hdct.DmWebsiteREF = @DmWebsiteREF
								AND hdct.DonGia = @DonGia
								AND hdct.ChietKhau = @ChietKhau
								AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)--Mua ngoai
								GROUP BY hdct.HopDongFK,hdct.HopDongChiTietID, hdct.DmSanPhamREF
						)A
						ORDER BY A.ThanhTienThucChay
					)
				END
				ELSE
					BEGIN
						SET @out =
						(
							SELECT TOP 1 A.HopDongChiTietID FROM
								(
									SELECT hdct.HopDongFK,hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.ThanhTien,
									SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))ThanhTienThucChay
									  FROM ThucChayDaTinh tcdt
									  RIGHT JOIN HopDongChiTiet hdct ON hdct.HopDongFK = tcdt.HopDongID
									  AND hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
									WHERE 1=1
									and hdct.HopDongFK =@HopDongREF
									AND hdct.DmSanPhamREF in (141,245,250,637,305) --PR
									AND hdct.DmSanPhamREF = @DmSanPhamREF
									AND hdct.DmLoaiREF = @DmHinhThucQuangCaoREF
									AND hdct.DeletedStatus = 0
									AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)--Mua ngoai
									GROUP BY hdct.HopDongFK,hdct.HopDongChiTietID, hdct.DmSanPhamREF,hdct.ThanhTien
								)A
								WHERE (A.ThanhTien - A.ThanhTienThucChay) >0 -- HAIDH CHECK LAI TH NAY NEU CHIET KHAU TANG DAN DEN VIEC CHECK NAY SAI
								ORDER BY A.HopDongChiTietID
						)
					END
			END
	SET @out = ISNULL(@out, 0)
	
	RETURN @out;
END

```
