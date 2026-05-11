# Stored Procedure: `AdminUser_UpdateEmail`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-26 15:42:58.720000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.737000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-05-26
-- Description:	Dong Bo du lieu email theo username
-- =============================================
-- EXEC dbo.AdminUser_UpdateEmail
CREATE PROCEDURE [dbo].[AdminUser_UpdateEmail] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @UserName	NVARCHAR(50),
			@Email		NVARCHAR(200),
			@ShortName	NVARCHAR(200),
			@FullName	NVARCHAR(200)
			
	DECLARE user_cursor CURSOR FOR
	SELECT DISTINCT
		A.Username
	FROM AdminUser A
	--WHERE A.Username = 'thucchay'
	
	OPEN user_cursor
	
	FETCH NEXT FROM user_cursor INTO @UserName
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SELECT @Email = isnull(A.Email,''),
			   @FullName = ISNULL(A.HovaTen,@UserName)
		FROM NhanSuSoYeuLyLichFull A
			INNER  JOIN AdminPermisionHDCN B ON B.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichID
		WHERE B.TenDangNhap = 'vuongyenvc' --@UserName
		
		IF(@Email IS NOT NULL AND @FullName IS NOT NULL)
		BEGIN
			PRINT @Email + ' - ' + @FullName
		
			UPDATE AdminUser
			SET Email		= @Email,
				FullName	= @FullName
			WHERE Username  = @UserName
		END
		ELSE
			PRINT 'Not have email '
		
		
		FETCH NEXT FROM user_cursor INTO @UserName
	END
	
	CLOSE user_cursor;
	DEALLOCATE user_cursor;
	
	--SELECT * FROM AdminUser AS au
END

--UPDATE AdminUser
--SET
--	--Email = '', FullName = ''

--SELECT * FROM AdminUser AS au where username = 'thucchay'

--SELECT isnull(A.Email,''),
--			  isnull(A.HovaTen,'dfdfd')
--		FROM NhanSuSoYeuLyLichFull A
--			INNER  JOIN AdminPermisionHDCN B ON B.NhanSuSoYeuLyLichID = A.NhanSuSoYeuLyLichID
--		WHERE B.TenDangNhap = 'vuongyenvc'
		
--SELECT A.NhanSuSoYeuLyLichID Email, COUNT(*) TotalCount
--FROM AdminPermisionHDCN A
--GROUP BY NhanSuSoYeuLyLichID
--HAVING COUNT(*) > 1
--ORDER BY COUNT(*) DESC

--SELECT * FROM AdminPermisionHDCN AS aph WHERE aph.NhanSuSoYeuLyLichID = 1168

```
