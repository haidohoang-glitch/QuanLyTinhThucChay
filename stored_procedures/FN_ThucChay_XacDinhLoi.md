# Function: `ThucChay_XacDinhLoi`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-10-25 13:59:53.907000
- **Ngày sửa cuối**: 2014-10-14 10:39:28.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TongViewDaTinh` | `float(8)` | No |
| `@TongViewKiemTra` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_XacDinhLoi]
(
	-- Add the parameters for the function here
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT,
	@TongViewDaTinh FLOAT,
	@TongViewKiemTra FLOAT		
	
)
RETURNS NVARCHAR(4000)
AS
BEGIN

-- Declare the return variable here
DECLARE @RecordCount INT, @RecordTest INT, @RecordTest1 INT, @Error NVARCHAR(4000)

SET @Error = N'Không có lỗi'
--Haidh comment neu lech nhau khoang 100 view thi hay check
--IF(@TongViewDaTinh <> @TongViewKiemTra) 
IF((@TongViewDaTinh - @TongViewKiemTra >=100) OR (@TongViewDaTinh - @TongViewKiemTra < -100))
BEGIN

	
	SET @RecordCount = (SELECT COUNT(*) FROM dbo.HopDong A
						INNER JOIN dbo.HopDongChiTiet B ON A.HopDongID = B.HopDongFK
						WHERE A.SoHopDong = @SoHopDong AND B.DmSanPhamREF = @DmSanPhamREF
						)
	
	SET @RecordTest = (SELECT COUNT(*) FROM dbo.HopDong A
						INNER JOIN dbo.HopDongChiTiet B ON A.HopDongID = B.HopDongFK
						WHERE A.SoHopDong = @SoHopDong AND B.DmSanPhamREF = @DmSanPhamREF AND B.DonGia <=0	
						)
						
	SET @RecordTest1 = (SELECT COUNT(DISTINCT B.DonGia) FROM dbo.HopDong A
						INNER JOIN dbo.HopDongChiTiet B ON A.HopDongID = B.HopDongFK
						WHERE A.SoHopDong = @SoHopDong AND B.DmSanPhamREF = @DmSanPhamREF
						)
	SET @Error = N''
	
	IF(@RecordCount = @RecordTest AND @RecordCount >0) SET @Error = @Error + N' Toàn bộ phân bổ hợp đồng giá là 0.' 
	
	IF(@RecordTest >0) SET @Error = @Error + N' Có phân bổ hợp đồng giá là 0.' 
	
	IF(@RecordTest1 >1) SET @Error = @Error + N' Cần gắn thực treo do hợp đồng có 2 đơn giá khác nhau.' 
	
	IF(@RecordCount = 0)SET @Error = @Error + N' Khác nhau về sản phẩm giữa hợp đồng và thực chạy.'
	
	SET @RecordCount = (SELECT COUNT(*) FROM dbo.HopDong A
						INNER JOIN dbo.HopDongChiTiet B ON A.HopDongID = B.HopDongFK
						WHERE A.SoHopDong = @SoHopDong AND B.DmSanPhamREF = @DmSanPhamREF AND B.ThoiGian LIKE N'%Gói%'
						)
	
	IF(@RecordCount > 0)SET @Error = @Error + N' Hợp đồng có số lượng tính theo gói.'
	
	IF(@Error = N'') 
	BEGIN		
		SET @Error = N'Không xác định.'			
	END
END
	-- Return the result of the function
	RETURN @Error

END

```
