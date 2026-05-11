# Stored Procedure: `ThucChay_UpdateTenDangNhap`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-10 18:25:13.487000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.527000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-03
-- Description:	Update TenDangNhap if is null
-- =============================================

-- exec dbo.ThucChay_UpdateTenDangNhap 
CREATE PROCEDURE [dbo].[ThucChay_UpdateTenDangNhap] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	DECLARE @TableTemp TABLE
		(
			TenDangNhap nvarchar(50),
			NhanVienREF INT,
			TenNhanVien nvarchar(50)
		)
		
	INSERT INTO @TableTemp(TenDangNhap, NhanVienREF, TenNhanVien)
	SELECT DISTINCT ('NV_' + CONVERT(nvarchar(50),A.SysNhanVienREF) + '_blank_username') AS TenDangNhap1,
					A.SysNhanVienREF, A.TenNhanVien
	FROM ThucChayDaTinh A
	WHERE A.TenDangNhap = ''
	
	--SELECT * FROM @TableTemp
	
	DECLARE Data CURSOR FOR		
	SELECT NhanVienREF FROM @TableTemp
			
	OPEN Data;
	DECLARE @CurrentNhanVienID INT	
	DECLARE @TenDangNhapNew NVARCHAR(50)	
	FETCH NEXT FROM Data INTO @CurrentNhanVienID;
	WHILE @@FETCH_STATUS = 0
	   BEGIN
	   		SET @TenDangNhapNew = (SELECT TenDangNhap FROM @TableTemp WHERE NhanVienREF = @CurrentNhanVienID)
	   		
			UPDATE ThucChayDaTinh
			SET TenDangNhap = @TenDangNhapNew
			WHERE SysNhanVienREF = @CurrentNhanVienID
				AND (TenDangNhap = '' OR TenDangNhap IS NULL) 
				--AND SysNhanVienREF = 596
			
						
			FETCH NEXT FROM Data INTO @CurrentNhanVienID;		  
	   END;	   
	CLOSE Data;
	DEALLOCATE Data;
	
	SELECT DISTINCT SysNhanVienREF, TenDangNhap, tcdt.TenNhanVien
	FROM ThucChayDaTinh tcdt WHERE tcdt.TenDangNhap = '' OR tcdt.TenDangNhap IS NULL
END

```
