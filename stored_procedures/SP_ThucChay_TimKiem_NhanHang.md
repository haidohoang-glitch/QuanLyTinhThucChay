# Stored Procedure: `ThucChay_TimKiem_NhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-23 09:17:32.747000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.620000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Keyword` | `nvarchar(8000)` | No |
| `@NhanSuSoYeuLyLichREF` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
-- [Rpt_NhanHang_TimKiem_Nhan_Test] 'omo', '23'

CREATE proc [dbo].[ThucChay_TimKiem_NhanHang]	
	@Keyword				NVARCHAR(4000),
	@NhanSuSoYeuLyLichREF	NVARCHAR(256)
AS
BEGIN
	DECLARE @SQL		NVARCHAR(MAX)
	DECLARE @Filter		NVARCHAR(4000)
	DECLARE @IsAdmin	INT
	 
	SET @Filter  = ''		
	SET @Keyword = replace(@Keyword,'''', '''''')
	
	IF (@Keyword <> '')
		SET @Filter = 'TenNhanHang COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%'+ @Keyword +'%''';				
	
	-- Kiểm tra Admin trong bảng AdminGroup
	-- 2, 34			Admin Thực chạy
	-- 103 ,151 ,152	Quản lý nhãn
	SET @IsAdmin = (SELECT COUNT(au.OxUserREF) 
	                FROM AdminGroupUser agu JOIN AdminUser au
					ON agu.AdminUserId = au.AdminUserId
					WHERE agu.AdminGroupID IN (2, 34, 103 ,151 ,152) AND au.OxUserREF = CONVERT(INT, @NhanSuSoYeuLyLichREF))					
					
	--PRINT '@IsAdmin: ' + CONVERT(NVARCHAR(10), @IsAdmin);
	
	IF (@IsAdmin = 0)
		BEGIN
			SET @SQL = 'SELECT TOP 50 A.DmNhanHangId AS ID , A.TenNhanHang AS Name FROM DmNhanHang A
						INNER JOIN PhanQuyenNhanHang AS B 
						ON A.DmNhanHangId = B.DmNhanHangREF						
						WHERE ' + @Filter + ' AND OxUserREF = ' + @NhanSuSoYeuLyLichREF + ' AND A.RecordStatus = 1 AND A.DeletedStatus <> 1				
						ORDER BY A.TenNhanHang ASC'					
		END		
	ELSE
		BEGIN			
			SET @SQL = 'SELECT TOP 50 A.DmNhanHangId AS ID, A.TenNhanHang AS Name FROM DmNhanHang A
						WHERE ' + @Filter + ' AND A.RecordStatus = 1 AND A.DeletedStatus <> 1
						ORDER BY A.TenNhanHang ASC'	
		END
						
	PRINT @SQL;
	
	EXEC sp_executesql @SQL;		
END

```
