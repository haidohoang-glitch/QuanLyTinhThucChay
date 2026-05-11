# Function: `Fn_NhanSu_GetListNhanVienByChucDanh1`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-31 12:47:36.877000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.437000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@NhanVienID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-29
-- Description:	GetListNhanVienByChucDanh
-- =============================================
CREATE FUNCTION [dbo].[Fn_NhanSu_GetListNhanVienByChucDanh1] 
(
	@NhanVienID INT
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @ChucDanhID INT
	DECLARE @PhongID INT
	DECLARE @BoPhanID INT
	DECLARE @NhomLamViecID INT
		
	SET @DauNhay=''''
	
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
	
	IF (@ChucDanhID = 3 OR @ChucDanhID = 6) -- Trưởng phòng, phó phòng
	BEGIN
		SET @Sql= (SELECT 
						STUFF((
								SELECT CAST(',' as VARCHAR(MAX)) + CONVERT(NVARCHAR(50),U.NhanSuSoYeuLyLichID) 
								FROM 
								(
    								SELECT DISTINCT
										A.NhanSuSoYeuLyLichID, A.HoVaTen
									FROM NhanSuSoYeuLyLichFull A
										INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
									WHERE 
										B.DmChucDanhREF IN (8,9,10,26,27,28) 
										AND B.DmPhongBanREF = @PhongID
										OR A.NhanSuSoYeuLyLichID = @NhanVienID
								)U
								ORDER BY U.HoVaTen
								FOR XML PATH('') 
								), 1, 1, '') AS HoVaTen
		)
	END
	ELSE IF (@ChucDanhID = 7) -- Trưởng bộ phận
	BEGIN
		SET @Sql= (SELECT 
						STUFF((
								SELECT CAST(',' as VARCHAR(MAX)) + CONVERT(NVARCHAR(50),U.NhanSuSoYeuLyLichID) 
								FROM 
								(
    								SELECT DISTINCT
										A.NhanSuSoYeuLyLichID, A.HoVaTen
									FROM NhanSuSoYeuLyLichFull A
										INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
									WHERE 
										B.DmChucDanhREF IN (8,9,10,26,27,28) 
										AND B.DmBophanREF = @BoPhanID
										OR A.NhanSuSoYeuLyLichID = @NhanVienID
								)U
								ORDER BY U.HoVaTen
								FOR XML PATH('') 
								), 1, 1, '') AS HoVaTen
		)
	END
	ELSE IF (@ChucDanhID = 1) -- Trưởng nhóm
	BEGIN
		SET @Sql= (SELECT 
						STUFF((
								SELECT CAST(',' as VARCHAR(MAX)) + CONVERT(NVARCHAR(50),U.NhanSuSoYeuLyLichID) 
								FROM 
								(
    								SELECT DISTINCT
										A.NhanSuSoYeuLyLichID, A.HoVaTen
									FROM NhanSuSoYeuLyLichFull A
										INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
									WHERE 
										B.DmChucDanhREF IN (8,9,10,26,27,28) 
										AND B.DmNhomLamViecREF = @NhomLamViecID
										OR A.NhanSuSoYeuLyLichID = @NhanVienID
								)U
								ORDER BY U.HoVaTen
								FOR XML PATH('') 
								), 1, 1, '') AS HoVaTen
		)
	END
	ELSE
		BEGIN
			SET @Sql= (SELECT 
						STUFF((
								SELECT CAST(',' as VARCHAR(MAX)) + CONVERT(NVARCHAR(50),U.NhanSuSoYeuLyLichID) 
								FROM 
								(
    								SELECT DISTINCT
										A.NhanSuSoYeuLyLichID, A.HoVaTen
									FROM NhanSuSoYeuLyLichFull A
										INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
									WHERE 
										B.DmChucDanhREF IN (8,9,10,26,27,28) 
										AND A.NhanSuSoYeuLyLichID = @NhanVienID
								)U
								ORDER BY U.HoVaTen
								FOR XML PATH('') 
								), 1, 1, '') AS HoVaTen
		)
		END								
	
     
    
	-- Return the result of the function
	RETURN @Sql

END

--SELECT dbo.Fn_NhanSu_GetListNhanVienByChucDanh1(153)


```
