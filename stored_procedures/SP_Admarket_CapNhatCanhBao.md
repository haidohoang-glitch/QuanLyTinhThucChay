# Stored Procedure: `Admarket_CapNhatCanhBao`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-14 15:05:56.860000
- **Ngày sửa cuối**: 2016-03-14 15:05:56.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@User` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Admarket_CapNhatCanhBao]
	-- Add the parameters for the stored procedure here
	@User NVARCHAR(50),
	@DmSanPhamREF INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @NapTienHomNay INT  
	 select @NapTienHomNay = COUNT(*)  from dbo.AdmarketUserLastRecharge WHERE UserName = @User 
    AND DmSanPhamREF = @DmSanPhamREF
    AND CONVERT(DATE,LastDateRecharge) = CONVERT(DATE,@NgayThucHien)
   -- cập nhật cảnh báo khi có nạp tiền
    IF @NapTienHomNay > 0
    BEGIN
    	UPDATE HopDongAdmarketCanhBao_NhanHang SET DeletedStatus = 1 WHERE TK_Admarket = @User
    	AND DmSanphamREF = @DmSanPhamREF
    END
END

```
