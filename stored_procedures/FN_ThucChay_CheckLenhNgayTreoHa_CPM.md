# Function: `ThucChay_CheckLenhNgayTreoHa_CPM`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-27 17:10:06.263000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.943000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DanhSachDmBookingREF` | `nvarchar(200)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@Soluong` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_CheckLenhNgayTreoHa_CPM]
(
	-- Add the parameters for the function here
	@DanhSachDmBookingREF NVARCHAR(100), 
	@NgayThucHien DATETIME,
	@Soluong INT,
	@DonGia FLOAT,
	@DonViTinh NVARCHAR(50),
	@HopDongChiTietID INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienLechTreoHa FLOAT
	DECLARE @TongViewThucChay BigINT
	DECLARE @TongViewHopDong BigINT
	--DECLARE @TongViewKhuyenMai BigINT
	SET @DanhSachDmBookingREF = '123'
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	
	SET @ThanhTienLechTreoHa = 0			
	IF((DATALENGTH(@DanhSachDmBookingREF) >0) AND (@DonViTinh = 'CPM'))
	--1. Get so luong thuc chay cua HopDongChiTietID.
	BEGIN
		SET @TongViewThucChay = (
				SELECT SUM(TongViewThucChay) FROM ThucChayDaTinh
				WHERE HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien <= @NgayThucHien
		)
		
	--2. Get so tong so luong View cua HopDong ChiTiet.
		SET @TongViewHopDong = @Soluong
		IF(@TongViewHopDong >= @TongViewThucChay)
			BEGIN
				SET @ThanhTienLechTreoHa = 0
			END
		ELSE
			BEGIN
	--3. Get so luong cua khuyen mai neu co. 			
	--4. Tinh Thanh tien lech treo ha.
				SET @ThanhTienLechTreoHa = (@DonGia/1000)*(@TongViewThucChay - @TongViewHopDong)
			END
	END
	RETURN @ThanhTienLechTreoHa;

END

```
