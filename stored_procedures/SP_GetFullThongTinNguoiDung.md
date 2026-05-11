# Stored Procedure: `GetFullThongTinNguoiDung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-10 07:55:08.083000
- **Ngày sửa cuối**: 2015-04-16 09:20:54.073000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

-- EXEC GetFullThongTinNguoiDung 'giadinhnet'

CREATE PROCEDURE [dbo].[GetFullThongTinNguoiDung]
	-- Add the parameters for the stored procedure here
	@TenDangNhap NVARCHAR(50)
AS
BEGIN

DECLARE 
	@FullName NVARCHAR(50), 
	@TenChucVu NVARCHAR(50),
	@TenPhongBan NVARCHAR(50),
	@TenBoPhan NVARCHAR(50),
	@TenNhomLamViec NVARCHAR(50),
	@Email NVARCHAR(50),
	@MaNhanSu NVARCHAR(50),
	@DoiTac	NVARCHAR(50) -- 1: doi tac kenh, 0: Doi tac noi bo; -1: all
	
DECLARE Record_Cursor CURSOR FOR 
	SELECT 		
		B.HoVaTen,
		B.Email,
		B.MaNhanSu,
		G.TenChucDanh,
		D.TenPhongBan,
		E.TenBoPhan,
		F.TenNhom as TenNhomLamViec

	FROM dbo.AdminPermisionHDCN A
	INNER JOIN dbo.NhanSuSoYeuLyLich B ON A.NhanSuSoYeuLyLichID = B.NhanSuSoYeuLyLichID
	INNER JOIN dbo.NhanSuQuaTrinhCongTac C ON C.NhanSuSoYeuLyLichREF = B.NhanSuSoYeuLyLichID
	LEFT JOIN dbo.DmPhongBan D ON C.DmPhongBanREF = D.DmPhongBanID
	LEFT JOIN dbo.DmBoPhan E ON E.DmBoPhanID = C.DmBoPhanREF
	LEFT JOIN dbo.DmNhom F ON F.DmNhomID = C.DmNhomLamViecREF
	LEFT JOIN dbo.DmChucDanh G ON G.DmChucDanhID = C.DmChucDanhREF	
	WHERE 
	UPPER(A.TenDangNhap) = UPPER(@TenDangNhap)
	AND C.[Active]=1

OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor INTO	
	@FullName, 
	@Email,
	@MaNhanSu,
	@TenChucVu,
	@TenPhongBan,
	@TenBoPhan,
	@TenNhomLamViec 

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

IF @DoiTac IS NOT NULL
	SET @DoiTac = N'Đối tác: ' + CONVERT(nvarchar(10),@DoiTac) + ';'	
ELSE
	SET @DoiTac = ''
	
IF(@FullName IS NOT NULL)
	SET @FullName = N'Họ và tên: ' + @FullName + ';'
ELSE
	SET @FullName = ''

IF(@Email IS NOT NULL)
	SET @Email = N'Email: ' + @Email + ';'
ELSE
	SET @Email = ''
	
IF(@MaNhanSu IS NOT NULL)
	SET @MaNhanSu = N'Mã nhân sự: ' + CONVERT(NVARCHAR(50), @MaNhanSu) + ';'
ELSE
	SET @MaNhanSu = ''
	
IF(@TenChucVu IS NOT NULL)
	SET @TenChucVu = N'Chức vụ: ' + @TenChucVu + ';'
ELSE
	SET @TenChucVu = ''

DECLARE @FullPhongBan NVARCHAR(150)

SET @FullPhongBan = ''

IF(@TenNhomLamViec IS NOT NULL)
	SET @FullPhongBan = @TenNhomLamViec  + '/'

IF(@TenBoPhan IS NOT NULL)
	SET @FullPhongBan = @FullPhongBan + @TenBoPhan + '/'

IF(@TenPhongBan IS NOT NULL)
	SET @FullPhongBan =  @FullPhongBan + @TenPhongBan 

IF(@FullPhongBan <> '') 
	SET @FullPhongBan = N'Phòng ban: ' + @FullPhongBan
	
SET @DoiTac = (SELECT PartnerValue FROM AdminUser AS au WHERE au.Username = @TenDangNhap)

IF @DoiTac IS NOT NULL 
	SET @DoiTac = N'Đối tác: ' + @DoiTac + ';';
ELSE
	SET @DoiTac = '';

SELECT 
	@DoiTac + 
	@MaNhanSu + 
	@FullName + 
	@Email + 
	@TenChucVu + 
	@FullPhongBan
	

END

```
