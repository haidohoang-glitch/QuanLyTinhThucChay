# Function: `CheckDonViTinhHinhThucCPDAndNotCPD`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-08 18:37:53.910000
- **Ngày sửa cuối**: 2022-10-05 15:26:45.640000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DonViTinhREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD]
(
	-- Add the parameters for the function here
	@DonViTinhREF INT,
	@DonViTinh NVARCHAR(50)
	
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DonViHinhThucTinh INT
	--@DonViHinhThucTinh= 1 => là tính cho hình thức sản phẩm CPD
	--@DonViHinhThucTinh= 2 => là tính cho hình thức sản phẩm là PR (Bài)
	--@DonViHinhThucTinh= 3 => là tính cho hình thức sản phẩm không phải CPD, PR (Bài)
	SET @DonViHinhThucTinh = 1
	set @DonViTinh = dbo.FormatStringUpper(@DonViTinh)
	
	IF((@DonViTinhREF IS NULL) OR (@DonViTinhREF = 0))
		BEGIN
			SET @DonViHinhThucTinh = 
			CASE @DonViTinh
				WHEN N'NGÀY' THEN 1
				WHEN N'TUẦN' THEN 1
				WHEN N'THÁNG' THEN 1
				WHEN N'NĂM' THEN 1
				
				WHEN N'BÀI' THEN 2
				
				WHEN 'CPM' THEN 3
				--WHEN 'CPV' THEN 3
				WHEN 'CPC' THEN 3
				WHEN 'CLICK' THEN 3
				WHEN 'VIEW' THEN 3
				WHEN N'TRUE REACH' THEN 3
				WHEN N'GÓI' THEN 5
			ELSE 4
			END	
		END
	ELSE
		BEGIN
			SET @DonViHinhThucTinh = 
			CASE @DonViTinhREF
				WHEN 3 THEN 1 --Đơn vị tính là ngày
				WHEN 4 THEN 1 --Đơn vị tính là tuần
				WHEN 5 THEN 1 --Đơn vị tính là tháng
				WHEN 6 THEN 1 --Đơn vị tính là năm
				
				WHEN 7 THEN 2 --Đơn vị tính là bài
				
				WHEN 1 THEN 3 --Đơn vị tính là CPM
				WHEN 2 THEN 3 --Đơn vị tính là CPC
				WHEN 31 THEN 3 --Đơn vị tính là TRUE REACH
				--WHEN 22 THEN 3 --Đơn vị tính là CPV
				WHEN 10 THEN 5 --Đơn vị tính là Gói
			ELSE 4
			END
		END
	
	-- Return the result of the function
	RETURN @DonViHinhThucTinh

END

```
