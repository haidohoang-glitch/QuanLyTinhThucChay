# Stored Procedure: `NhanSu_GetListNhanVienByChucDanh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-28 16:50:07.053000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.683000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanVienID` | `int(4)` | No |
| `@HoVaTenList` | `nvarchar(8000)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-28
-- Description:	Get list nhan vien by vi tri cong tac
-- =============================================

CREATE PROCEDURE [dbo].[NhanSu_GetListNhanVienByChucDanh]
	-- Add the parameters for the stored procedure here
	@NhanVienID INT
	,
	@HoVaTenList NVARCHAR(4000) OUTPUT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @DoubleDauNhay NVARCHAR(50) 
	DECLARE @Table NVARCHAR(4000)
	DECLARE @ChucDanhID INT
	DECLARE @PhongID INT
	DECLARE @BoPhanID INT
	DECLARE @NhomLamViecID INT
	DECLARE @N1DauNhay NVARCHAR(4000) 
	DECLARE @N2DauNhay NVARCHAR(4000) 
	DECLARE @2DauNhay NVARCHAR(4000) 
	DECLARE @Sql1 NVARCHAR(4000)
	--DECLARE @HoVaTenList NVARCHAR(4000)
		
	SET @DauNhay=''''
	SET @DoubleDauNhay=''''''
	SET @N1DauNhay='N'''''''
	SET @N2DauNhay='N'''''''''''
    SET @2DauNhay=''''''''''''''
    
    SET @HoVaTenList='@HoVaTenList'
	
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
								
	SET @Table = '
			SELECT DISTINCT
				A.NhanSuSoYeuLyLichID, A.HoVaTen
			FROM NhanSuSoYeuLyLichFull A
				INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
			WHERE 
				B.DmChucDanhREF IN (8,9,10,26,27,28)
			'
	
	IF (@ChucDanhID = 3 OR @ChucDanhID = 6) -- Trưởng phòng, phó phòng
	BEGIN
		SET @Table += ' AND B.DmPhongBanREF = ' + CONVERT(NVARCHAR(50), @PhongID)
		SET @Table += ' OR A.NhanSuSoYeuLyLichID = ' + CONVERT(NVARCHAR(50), @NhanVienID)
	END
	ELSE IF (@ChucDanhID = 7) -- Trưởng bộ phận
	BEGIN
		SET @Table += ' AND B.DmBophanREF = ' + CONVERT(NVARCHAR(50), @BoPhanID)
		SET @Table += ' OR A.NhanSuSoYeuLyLichID = ' + CONVERT(NVARCHAR(50), @NhanVienID)
	END
	ELSE IF (@ChucDanhID = 1) -- Trưởng nhóm
	BEGIN
		SET @Table += ' AND B.DmNhomLamViecREF = ' + CONVERT(NVARCHAR(50), @NhomLamViecID)
		SET @Table += ' OR A.NhanSuSoYeuLyLichID = ' + CONVERT(NVARCHAR(50), @NhanVienID)
	END
	ELSE
		BEGIN
			SET @Table += ' AND A.NhanSuSoYeuLyLichID = ' + CONVERT(NVARCHAR(50), @NhanVienID)
		END								
	
    SET @Sql = '
    SELECT ' + @HoVaTenList +' =  T.HoVaTen 
    FROM
     (SELECT 
    STUFF(
    (
    SELECT CAST('+@DauNhay+','+@DauNhay+' as VARCHAR(MAX)) +  ' + @DauNhay + @N2DauNhay +' + U.HoVaTen+ '+@2DauNhay+'
    FROM ('+ @Table+') U
    ORDER BY U.HoVaTen
    FOR XML PATH('+@DauNhay+''+@DauNhay+') 
    ), 1, 1, '+@DauNhay+''+@DauNhay+') AS HoVaTen
    )T
    '
	
	--SET @Sql1 = @N1DauNhay+@Sql + @DauNhay
	
	PRINT @Sql;
	EXEC(@Sql);
	
END

--EXEC NhanSu_GetListNhanVienByChucDanh 153
-- EXEC NhanSu_GetListNhanVienByChucDanh 153,@HoTenList = @Result OUTPUT

```
