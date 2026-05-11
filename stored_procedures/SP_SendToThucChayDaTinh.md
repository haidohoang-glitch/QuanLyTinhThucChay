# Stored Procedure: `SendToThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-12-01 10:26:17.260000
- **Ngày sửa cuối**: 2016-06-16 18:15:11.833000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 01/12/2015
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[SendToThucChayDaTinh] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @NgayThucHien DATETIME 
	SET @NgayThucHien = DATEADD(dd,-1,GETDATE())
	INSERT INTO ThucChayDaTinh
	SELECT * FROM ThucChayDaTinh_ThayDoi 
	WHERE 1=1
	AND convert(date,NgayThucHien) = convert(date,@NgayThucHien)
	AND DmSanPhamREF NOT IN (141,637,305)
	
	UNION ALL
	
	SELECT * FROM ThucChayDaTinh_ThayDoi 
	WHERE 1=1
	AND convert(date,NgayThucHien) = convert(date,@NgayThucHien)
	AND DmSanPhamREF IN (141,637,305)
	AND (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
	
	INSERT INTO ThucChayDaTinhAdmarket
	SELECT * FROM ThucChayDaTinhAdmarket_ThayDoi WHERE convert(date,NgayThucHien) = convert(date,@NgayThucHien)

	--- Update nhan hang bởi thực chạy hd chi tiết
	DECLARE @NhanHangMoi NVARCHAR(500),@HDID INT, @PhanBoID INT 
	DECLARE cursor_hdct CURSOR FOR  
	
	SELECT HopDongREF,HopDongChiTietREF, DmNhanHangREF
	FROM ThucChayHopDongChiTiet 
	WHERE CONVERT(DATE,LastModifiedAt) = CONVERT(DATE,@NgayThucHien)
	AND  HopDongChiTietREF <> 0
	OPEN cursor_hdct   
	FETCH NEXT FROM cursor_hdct INTO @HDID,@PhanBoID,@NhanHangMoi   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   -----
		   UPDATE ThucChayDaTinh
		   SET
		   NhanHang = @NhanHangMoi
		   WHERE hopdongid = @HDID
		   AND HopDongChiTietREF = @PhanBoID
		   AND CONVERT(DATE,NgayThucHien) = CONVERT(DATE,@NgayThucHien)
		   FETCH NEXT FROM cursor_hdct INTO @HDID,@PhanBoID,@NhanHangMoi    
	END   

	CLOSE cursor_hdct   
	DEALLOCATE cursor_hdct

END

```
