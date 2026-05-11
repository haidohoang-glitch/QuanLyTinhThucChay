# Function: `ThucChay_CheckHopDongCoSanPhamLechDonGiaYN`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-17 13:50:56.150000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@TypeProduct` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[ThucChay_CheckHopDongCoSanPhamLechDonGiaYN]
(
	-- Add the parameters for the function here
	@TypeProduct INT,
	@SoHopDong NVARCHAR(50)
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(50)
	DECLARE @Count INT, @DmSanPhamREF int
	SET @Result = 'Y'
	SET @DmSanPhamREF =
	(
		CASE 
			WHEN @TypeProduct=3 THEN 231
			WHEN @TypeProduct=4 THEN 238
			WHEN @TypeProduct=5 THEN 339
			WHEN @TypeProduct=6 THEN 342
			WHEN @TypeProduct=7 THEN 337
			WHEN @TypeProduct=8 THEN 240
			WHEN @TypeProduct=9 THEN 370
			WHEN @TypeProduct=14 THEN 598
			WHEN @TypeProduct=15 THEN 613
		END
	)
    SET @Count = 
    (        
			SELECT COUNT(*) FROM 
			(
				SELECT MAX(HDCT.DonGia) DonGiaMax, MIN(hdct.DonGia)DonGiaMin
				--, MAX(hdct.ChietKhau) CKMax, MIN(hdct.ChietKhau) CKMin   
				FROM HopDong hd
				INNER JOIN HopDongChiTiet hdct ON HD.HopDongID = HDCT.HopDongFK
				WHERE HD.SoHopDong = Upper(@SoHopDong)
				AND HDCT.DmSanPhamREF = @DmSanPhamREF
				AND hdct.DeletedStatus = 0
				AND HDCT.DonGia >0
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 3 --Đơn vị của hình thức CPD 
			)A
			WHERE (A.DonGiaMax >A.DonGiaMin)
			--OR (A.CKMax > A.CKMin)
    )
    IF(@Count = 0)
		SET @Result = 'N'
	-- Return the result of the function
	RETURN @Result

END

--select dbo.ThucChay_CheckHopDongCoSanPhamLechDonGiaYN(9 ,'QC2521013') HDLechGiaYN

```
