# Stored Procedure: `Admarket_ThucChayDaTinhAdmarket_NhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-11 15:35:57.077000
- **Ngày sửa cuối**: 2016-03-31 11:49:34.063000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANV
-- Create date: 2016-03-11
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[Admarket_ThucChayDaTinhAdmarket_NhanHang] '2016-03-28','2016-03-28'
CREATE PROCEDURE [dbo].[Admarket_ThucChayDaTinhAdmarket_NhanHang]
	-- Add the parameters for the stored procedure here
	-- Luôn nhập là một ngày
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    DELETE FROM ThucChayDaTinhAdmarket WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
    DELETE FROM HopDongAdmarketCanhBao_NhanHang WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
    DELETE FROM ThucChayAdmarketUser_NhanHang_Online WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
    -- Insert statements for procedure here
	DECLARE @NgayThucHien		DATETIME,
			@NgayGioiHanTinh	DATETIME
    DECLARE @DmSanPhamREF INT,
			@TenSanPham		NVARCHAR(50),
			@UserName		NVARCHAR(50),
			@DonViTinh		NVARCHAR(50),
			@GhiChu			NVARCHAR(255),
			@DmViTriREF		INT,
			@TenViTri		NVARCHAR(50),
			@DmNhanHanREF	INT
			
	SET @GhiChu = '';
			
	SET @NgayGioiHanTinh = '2013-01-01'
			
    SET @NgayThucHien = @StartDate
    WHILE @NgayThucHien <= @EndDate
		BEGIN
			-- insert dl vào bảng tính thực chạy admar hàng ngày
			EXEC dbo.ThucChaySelfServingUsers_Insert_haidh @NgayThucHien, @NgayThucHien 
			EXEC dbo.Admarket_ThucChaySelfServingUsers_NhanHang_Insert @NgayThucHien, @NgayThucHien 
	    	
	    	DECLARE db_cursorAdmar CURSOR FOR  
			SELECT DISTINCT
    		tcau.DmSanPhamREF, tcau.username, tcau.DonViTinh, tcau.DmViTriREF,tcau.DmNhanHangREF
    		FROM ThucChaySelfServingUsers_NhanHang tcau
    		INNER JOIN
    		(	
    			SELECT distinct hdct.TK_AdMarket FROM HopDong hd
    			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
    			WHERE 1=1
    			AND hd.DeletedStatus = 0
    			AND hdct.DeletedStatus = 0
    			AND hd.TrangThaiHopDong <> 3
    			AND hdct.CreatedAt >= @NgayGioiHanTinh
    			AND CONVERT(DATE, hdct.CreatedAt) <= @NgayThucHien
    		)hd ON tcau.username = hd.TK_AdMarket --AND tcau.DmSanPhamREF = tcau.DmSanPhamREF
    		WHERE tcau.NgayThucHien = @NgayThucHien
   			AND tcau.[money] > 0

			OPEN db_cursorAdmar   
			FETCH NEXT FROM db_cursorAdmar INTO @DmSanPhamREF, @UserName, @DonViTinh, @DmViTriREF,@DmNhanHanREF   

			WHILE @@FETCH_STATUS = 0   
			BEGIN   
				   -- Insert thực chạy admarket
				   EXEC [dbo].[Admarket_InsertThucChayDaTinhAdMarket]
				    @NgayThucHien,
					@DmSanPhamREF,
					@UserName,
					'insert admarket',
					@DmViTriREF,
					@DmNhanHanREF
					
				   FETCH NEXT FROM db_cursorAdmar INTO @DmSanPhamREF, @UserName, @DonViTinh, @DmViTriREF,@DmNhanHanREF  
			END   

			CLOSE db_cursorAdmar   
			DEALLOCATE db_cursorAdmar
			-- cân chiều domain và chiều user
			EXEC [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract] @NgayThucHien
			-- Tính ngày tiếp theo
	    	SET @NgayThucHien = dateadd(dd,1,@NgayThucHien) 
		END
	-- xóa thực chay admarket mà có giá trị tiền = 0
	DELETE FROM ThucChayDaTinhAdmarket WHERE NgayThucHien BETWEEN @StartDate AND @EndDate AND GiaTriThayDoi + ThanhTienSauTrietKhauThucChay = 0
    -- Can khi phan bo update gia tri giam
    EXEC [dbo].[Admarket_ThucChayAdmarketCanPhanBoUpdateGiamGiaTri] @StartDate
END



```
