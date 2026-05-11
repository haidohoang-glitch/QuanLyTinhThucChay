# Function: `ThucChay_XacDinhMaLoi`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-10-25 13:59:46.500000
- **Ngày sửa cuối**: 2014-10-14 10:39:28.937000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
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
CREATE FUNCTION [dbo].[ThucChay_XacDinhMaLoi]
(
	-- Add the parameters for the function here
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT,
	@TongViewDaTinh FLOAT,
	@TongViewKiemTra FLOAT	
)
RETURNS NVARCHAR(50) 
AS
BEGIN

DECLARE @RecordCount INT, @RecordTest INT, @RecordTest1 INT, @ErrorCode NVARCHAR(50) 

SET @ErrorCode = '-1'

--Haidh comment neu lech nhau khoang 100 view thi hay check
--IF(@TongViewDaTinh <> @TongViewKiemTra) 
IF((@TongViewDaTinh - @TongViewKiemTra >=100) OR (@TongViewDaTinh - @TongViewKiemTra < -100))
BEGIN
	-- Declare the return variable here
	
	
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
	
	
	SET @ErrorCode = '' 
	
		
	IF(@RecordCount = @RecordTest AND @RecordCount >0) SET @ErrorCode = '1' -- N' Toàn bộ phân bổ hợp đồng giá là 0.' 
	
	IF(@RecordTest >0) SET @ErrorCode = @ErrorCode + ',' + '2' --  N' Có phân bổ hợp đồng giá là 0.' 
	
	IF(@RecordTest1 >1) SET @ErrorCode = @ErrorCode + ',' + '3' --  N' Cần gắn thực treo do hợp đồng có 2 đơn giá khác nhau.' 
	
	IF(@RecordCount = 0)SET @ErrorCode = @ErrorCode + ',' + '4' --  N' Khác nhau về sản phẩm giữa hợp đồng và thực chạy.'
	
	SET @RecordCount = (SELECT COUNT(*) FROM dbo.HopDong A
						INNER JOIN dbo.HopDongChiTiet B ON A.HopDongID = B.HopDongFK
						WHERE A.SoHopDong = @SoHopDong AND B.DmSanPhamREF = @DmSanPhamREF AND B.ThoiGian LIKE N'%Gói%'
						)
	
	IF(@RecordCount > 0)SET @ErrorCode = @ErrorCode + ',' + '5' --  N' Hợp đồng có số lượng tính theo gói.'
	
	IF(@ErrorCode = '') SET @ErrorCode = '0' --N'Không xác định lỗi' 
END
-- Return the result of the function
	RETURN @ErrorCode

END

```
