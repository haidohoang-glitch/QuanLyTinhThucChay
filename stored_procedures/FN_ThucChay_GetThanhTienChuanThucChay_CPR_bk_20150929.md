# Function: `ThucChay_GetThanhTienChuanThucChay_CPR_bk_20150929`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-09-29 13:54:47.340000
- **Ngày sửa cuối**: 2015-09-29 13:54:51.273000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DonViTinhREF` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |
| `@UV` | `int(4)` | No |
| `@View_user` | `int(4)` | No |
| `@UVThucChay` | `int(4)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_CPR_bk_20150929]
(
	-- Add the parameters for the function here
	@DonViTinhREF INT, 
	@DonGia FLOAT,
	@UV	INT,
	@View_user INT,
	@UVThucChay INT,
	@TongViewThucChay FLOAT,
	@HopDongChiTietID INT,
	@SoHopDong NVARCHAR(100),
	@TypeProduct INT	
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT
	,@TongVewInNgay INT = 0
	,@TongViewGoiMua BIGINT = 0
	,@ThucChayInNgay FLOAT = 0
	
	IF(@DonViTinhREF = 10)
	BEGIN
		SET @TongVewInNgay =
		(
			SELECT SUM(A.TongViewThucChay) 
			FROM
			(
				select 
				A.NgayThucHien,
				round(SUM((A.TongViewThucChay*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongViewThucChay,
				round(SUM((A.TongClickThucChay*B.TiLeThucChayHDCTSoVoiBanner)/100),0) TongClickThucChay,
				SUM(ISNULL(A.TongSoBaiViet,0)) TongSoBaiViet,
				B.HopDongChiTietREF,
				A.TypeProduct
				from ThucChayTemp A				
				INNER JOIN  
				(
					SELECT distinct b.DmBannerID, b.HopDongChiTietREF, b.HopDongREF, b.TiLeThucChayHDCTSoVoiBanner,
					b.DeletedStatus, b.DaThucHienUpdateTiLe
				   from dbo.ThucChayHopDongChiTietAndBanner b
				) B on B.DmBannerID = Convert(nvarchar(50),A.DmBannerREF)
				WHERE a.SoHopDong = @SoHopDong AND a.TypeProduct = @TypeProduct 
				AND B.DeletedStatus = 0				
				GROUP BY A.NgayThucHien, B.HopDongChiTietREF, A.TypeProduct	
			)A
			WHERE 1=1
			AND A.HopDongChiTietREF = @HopDongChiTietID
		)
		SET @TongVewInNgay = ISNULL(@TongVewInNgay,0)
		
		IF(@UV*@View_user = 0 OR @UV = 0 OR @TongVewInNgay = 0)
		BEGIN
			set @ThanhTienThucChay = 0
		END
		ELSE
		BEGIN
				SET @TongViewGoiMua = @UV*@View_user
				SET @ThucChayInNgay = (Convert(float,@TongVewInNgay)/Convert(float,@TongViewGoiMua)) 
										*(Convert(float,@UVThucChay)/Convert(float,@UV))*@DonGia
				SET @ThanhTienThucChay = @ThucChayInNgay*(Convert(float,@TongViewThucChay)/Convert(float,@TongVewInNgay))
		END
	END
	
	SET @ThanhTienThucChay = ISNULL(@ThanhTienThucChay,0)
	RETURN @ThanhTienThucChay

END

```
