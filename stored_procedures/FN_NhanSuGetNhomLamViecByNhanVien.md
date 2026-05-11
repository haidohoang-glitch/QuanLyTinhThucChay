# Function: `NhanSuGetNhomLamViecByNhanVien`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-13 15:04:06.900000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.690000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-13
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[NhanSuGetNhomLamViecByNhanVien]
(
	-- Add the parameters for the function here
	@TenDangNhap NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue INT

	SET @ResultValue = (SELECT A.DmNhomLamViecREF
						FROM NhanSuQuaTrinhCongTac A
							INNER JOIN AdminPermisionHDCN B ON B.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichREF
							LEFT JOIN DmChucDanh C ON C.DmChucDanhID = A.DmChucDanhREF
						WHERE A.[Active]=1
							AND B.TenDangNhap = @TenDangNhap)

	-- Return the result of the function
	RETURN @ResultValue

END

```
