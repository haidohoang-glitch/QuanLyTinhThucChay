# Function: `GenSQLCommandGetListNhanVienByChucDanh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-30 08:54:05.043000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@NhanVienID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-30
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.GenSQLCommandGetListNhanVienByChucDanh 
(
	-- Add the parameters for the function here
	@NhanVienID INT
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @ChucDanhID INT
	DECLARE @PhongID INT
	DECLARE @BoPhanID INT
	DECLARE @NhomLamViecID INT
	DECLARE @DauNhay NVARCHAR(50)
	
	SET @DauNhay = ''''
	
	SET @ChucDanhID = (SELECT DmChucDanhREF 
	                   FROM NhanSuQuaTrinhCongTac 
	                   WHERE NhanSuSoYeuLyLichREF = @NhanVienID 
							 AND [Active] = 1);
	
	SET @PhongID = (SELECT DmPhongBanREF 
	                FROM NhanSuQuaTrinhCongTac 
	                WHERE NhanSuSoYeuLyLichREF = @NhanVienID
						  AND [Active] = 1);
	
	SET @BoPhanID = (SELECT DmBoPhanREF 
					 FROM NhanSuQuaTrinhCongTac 
	                 WHERE NhanSuSoYeuLyLichREF = @NhanVienID
							AND [Active] = 1);
	
	SET @NhomLamViecID = (SELECT DmNhomLamViecREF
	                      FROM NhanSuQuaTrinhCongTac 
	                      WHERE NhanSuSoYeuLyLichREF = @NhanVienID
								AND [Active] = 1);

	SET @Sql = '
			SELECT DISTINCT
				A.NhanSuSoYeuLyLichID, A.HoVaTen
			FROM NhanSuSoYeuLyLichFull A
				INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
			WHERE 
				B.DmChucDanhREF IN (8,9,10,26,27,28)
			'
	
	IF (@ChucDanhID = 3 OR @ChucDanhID = 6) -- Trưởng phòng, phó phòng
	BEGIN
		SET @Sql += ' AND B.DmPhongBanREF = ' + CONVERT(NVARCHAR(50), @PhongID)
		SET @Sql += ' OR A.NhanSuSoYeuLyLichID = ' + CONVERT(NVARCHAR(50), @NhanVienID)
	END
	ELSE IF (@ChucDanhID = 7) -- Trưởng bộ phận
	BEGIN
		SET @Sql += ' AND B.DmBophanREF = ' + CONVERT(NVARCHAR(50), @BoPhanID)
		SET @Sql += ' OR A.NhanSuSoYeuLyLichID = ' + CONVERT(NVARCHAR(50), @NhanVienID)
	END
	ELSE IF (@ChucDanhID = 1) -- Trưởng nhóm
	BEGIN
		SET @Sql += ' AND B.DmNhomLamViecREF = ' + CONVERT(NVARCHAR(50), @NhomLamViecID)
		SET @Sql += ' OR A.NhanSuSoYeuLyLichID = ' + CONVERT(NVARCHAR(50), @NhanVienID)
	END
	ELSE
		BEGIN
			SET @Sql += ' AND A.NhanSuSoYeuLyLichID = ' + CONVERT(NVARCHAR(50), @NhanVienID)
		END

	-- Return the result of the function
	RETURN @Sql

END

```
