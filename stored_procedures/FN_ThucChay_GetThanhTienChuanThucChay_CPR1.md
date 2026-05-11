# Function: `ThucChay_GetThanhTienChuanThucChay_CPR1`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-09-15 12:03:24.147000
- **Ngày sửa cuối**: 2015-09-15 12:03:46.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DonViTinhREF` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |
| `@UV` | `float(8)` | No |
| `@View_user` | `float(8)` | No |
| `@UVThucChay` | `float(8)` | No |
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

--select dbo.ThucChay_GetThanhTienChuanThucChay_CPR1 (10,60000000,500000,500000,71343,72580,82323,'QC040915',16)
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_CPR1]
(
	-- Add the parameters for the function here
	@DonViTinhREF INT, 
	@DonGia FLOAT,
	@UV	FLOAT,
	@View_user FLOAT,
	@UVThucChay FLOAT,
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
