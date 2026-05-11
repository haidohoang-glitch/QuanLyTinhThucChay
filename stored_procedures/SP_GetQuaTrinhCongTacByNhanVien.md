# Stored Procedure: `GetQuaTrinhCongTacByNhanVien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-18 09:21:17.800000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.467000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenDanNhap` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC GetQuaTrinhCongTacByNhanVien 'lananhphamthi','2013-06-01','2013-08-30'


CREATE PROCEDURE [dbo].[GetQuaTrinhCongTacByNhanVien]
	-- Add the parameters for the stored procedure here
	@TenDanNhap nvarchar(50),
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN

	DECLARE @MaxDate DATETIME
	
	--DECLARE @StartDate datetime,@EndDate DATETIME, @TenDanNhap nvarchar(50)
	
	--SET @StartDate = '2013-08-01'
	--SET @EndDate = '2013-08-30'
	--SET @TenDanNhap = 'lananhphamthi'
	
	SET @MaxDate = (
					SELECT TOP 1 A.NgayNghiViec FROM NhanSuQuaTrinhCongTac A
					INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
					WHERE 
					A.NgayNghiViec >= @EndDate
					AND B.TenDangNhap = @TenDanNhap
					
					ORDER BY A.NgayNghiViec ASC					
					) 
	
	SELECT 
	A.NhanSuQuaTrinhCongTacID,
	A.DmPhongBanREF,
	A.DmBoPhanREF,
	A.DmNhomLamViecREF,
	A.DmChucDanhREF,
	A.NgayBatDauLamViec,
	A.NgayNghiViec
	
    FROM dbo.NhanSuQuaTrinhCongTac A
	INNER JOIN dbo.AdminPermisionHDCN B ON A.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
	WHERE 
	(
	B.TenDangNhap = @TenDanNhap
	AND @StartDate BETWEEN A.NgayBatDauLamViec AND  A.NgayNghiViec
	)
	
	OR 
	
	(
	@MaxDate BETWEEN A.NgayBatDauLamViec AND  A.NgayNghiViec
	AND B.TenDangNhap = @TenDanNhap
	)
	ORDER BY A.NgayBatDauLamViec ASC	


	
END

```
