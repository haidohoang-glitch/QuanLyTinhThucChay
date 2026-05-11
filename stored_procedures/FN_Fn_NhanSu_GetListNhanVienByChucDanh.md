# Function: `Fn_NhanSu_GetListNhanVienByChucDanh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-29 18:04:17.593000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.463000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-29
-- Description:	GetListNhanVienByChucDanh
-- =============================================
CREATE FUNCTION [dbo].[Fn_NhanSu_GetListNhanVienByChucDanh] 
(
	@TenDangNhap NVARCHAR(50)
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
	
	SET @ChucDanhID = (SELECT A.DmChucDanhREF 
	                   FROM NhanSuQuaTrinhCongTac A
						INNER JOIN AdminPermisionHDCN B ON B.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichREF
	                   WHERE B.TenDangNhap = @TenDangNhap 
							 AND [Active] = 1);
	
	SET @PhongID = (SELECT A.DmPhongBanREF 
	                FROM NhanSuQuaTrinhCongTac A
						INNER JOIN AdminPermisionHDCN B ON B.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichREF
	                   WHERE B.TenDangNhap = @TenDangNhap 
							 AND [Active] = 1);
	
	SET @BoPhanID = (SELECT A.DmBoPhanREF 
					 FROM NhanSuQuaTrinhCongTac A
						INNER JOIN AdminPermisionHDCN B ON B.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichREF
	                   WHERE B.TenDangNhap = @TenDangNhap 
							 AND [Active] = 1);
	
	SET @NhomLamViecID = (SELECT A.DmNhomLamViecREF
	                      FROM NhanSuQuaTrinhCongTac A
							INNER JOIN AdminPermisionHDCN B ON B.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichREF
						   WHERE B.TenDangNhap = @TenDangNhap 
								 AND [Active] = 1);
	
	IF (@ChucDanhID = 3 OR @ChucDanhID = 6) -- Trưởng phòng, phó phòng
	BEGIN
		SET @Sql= (SELECT 
						STUFF((
								SELECT ','+ '''' + CONVERT(NVARCHAR(50),U.TenDangNhap) + ''''
								FROM 
								(
    								SELECT DISTINCT
										A.NhanSuSoYeuLyLichID, A.HoVaTen, C.TenDangNhap
									FROM NhanSuSoYeuLyLichFull A 
										INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
										INNER JOIN AdminPermisionHDCN C ON C.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichID
									WHERE 
										--B.DmChucDanhREF IN (8,9,10,26,27,28) 
										--AND 
										B.DmPhongBanREF = @PhongID
										OR C.TenDangNhap = @TenDangNhap
								)U
								ORDER BY U.TenDangNhap
								FOR XML PATH('') 
								), 1, 1, '') AS TenDangNhap
		)
	END
	ELSE IF (@ChucDanhID = 7) -- Trưởng bộ phận
	BEGIN
		SET @Sql= (SELECT 
						STUFF((
								SELECT ','+ '''' + CONVERT(NVARCHAR(50),U.TenDangNhap) + '''' 
								FROM 
								(
    								SELECT DISTINCT
										A.NhanSuSoYeuLyLichID, A.HoVaTen, C.TenDangNhap
									FROM NhanSuSoYeuLyLichFull A
										INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
										INNER JOIN AdminPermisionHDCN C ON C.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichID
									WHERE 
										--B.DmChucDanhREF IN (8,9,10,26,27,28) 
										--AND 
										B.DmPhongBanREF = @PhongID
										AND B.DmBophanREF = @BoPhanID
										OR C.TenDangNhap = @TenDangNhap
								)U
								ORDER BY U.TenDangNhap
								FOR XML PATH('') 
								), 1, 1, '') AS TenDangNhap
		)
	END
	ELSE IF (@ChucDanhID = 1) -- Trưởng nhóm
	BEGIN
		SET @Sql= (SELECT 
						STUFF((
								SELECT ','+ '''' + CONVERT(NVARCHAR(50),U.TenDangNhap) + '''' 
								FROM 
								(
    								SELECT DISTINCT
										A.NhanSuSoYeuLyLichID, A.HoVaTen, C.TenDangNhap
									FROM NhanSuSoYeuLyLichFull A
										INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
										INNER JOIN AdminPermisionHDCN C ON C.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichID
									WHERE 
										--B.DmChucDanhREF IN (8,9,10,26,27,28) 
										--AND 
										B.DmPhongBanREF = @PhongID
										AND B.DmBophanREF = @BoPhanID
										AND B.DmNhomLamViecREF = @NhomLamViecID
										OR C.TenDangNhap = @TenDangNhap
								)U
								ORDER BY U.TenDangNhap
								FOR XML PATH('') 
								), 1, 1, '') AS HoVaTen
		)
	END
	ELSE
		BEGIN
			SET @Sql= (SELECT 
						STUFF((
								SELECT ','+ '''' + CONVERT(NVARCHAR(50),U.TenDangNhap) + '''' 
								FROM 
								(
    								SELECT DISTINCT
										A.NhanSuSoYeuLyLichID, A.HoVaTen, C.TenDangNhap
									FROM NhanSuSoYeuLyLichFull A
										INNER JOIN NhanSuQuaTrinhCongTac B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichREF AND B.[Active] = 1
										INNER JOIN AdminPermisionHDCN C ON C.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichID
									WHERE 
										C.TenDangNhap = @TenDangNhap
										--AND B.DmChucDanhREF IN (8,9,10,26,27,28) 
										
								)U
								ORDER BY U.TenDangNhap
								FOR XML PATH('') 
								), 1, 1, '') AS TenDangNhap
		)
		END								
	
     
    
	-- Return the result of the function
	RETURN @Sql

END


```
