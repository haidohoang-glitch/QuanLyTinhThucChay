# Stored Procedure: `ThucChayDaTinh_ExcInsertThucChayDaTinhBoxAppSSV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 14:26:17.707000
- **Ngày sửa cuối**: 2017-02-27 18:41:50.977000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
-- EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhBoxAppSSV '2014-07-18', '2014-07-20'
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhBoxAppSSV]
	-- Add the parameters for the stored procedure here
	@StartDate	DATETIME,
	@EndDate	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @NgayThucHien			DATETIME;
    DECLARE @DmSanPhamREF			INT,
			@DmWebsiteREF			INT,
			@DmHinhThucQuangCaoREF	INT,
			@SoHopDong				NVARCHAR(50),
			@TenSanPham				NVARCHAR(50),
			@TenWebsite				NVARCHAR(50)
			
    
    -- Xoa du lieu truoc khi insert neu da ton tai
    DELETE FROM ThucChayDaTinh 
    WHERE NgayThucHien BETWEEN @StartDate AND @EndDate 
	AND DmSanPhamREF = 375 ;
	
	DELETE FROM ThucChayBoxAppSSVOnline WHERE NgayThucHien BETWEEN @StartDate AND @EndDate   
    
    SET @NgayThucHien = @StartDate
    
    WHILE @NgayThucHien <= @EndDate
    BEGIN
    	DECLARE record_cursor CURSOR FOR
    	SELECT A.SoHopDong, A.DmHinhThucQuangCao, A.DmSanPhamREF, A.TenSanPham, A.DmWebsiteREF, A.TenWebsite
    	FROM ThucChayDaTinhBoxAppSSV A    		
    	WHERE A.NgayThucHien = @NgayThucHien
    	
    	OPEN record_cursor
    	
    	FETCH NEXT FROM record_cursor INTO @SoHopDong, @DmHinhThucQuangCaoREF, @DmSanPhamREF, @TenSanPham, @DmWebsiteREF, @TenWebsite
    	WHILE @@FETCH_STATUS = 0
    	BEGIN
    		EXEC dbo.ThucChayDaTinhBoxAppSSV_InsertByContractNo 
    			@NgayThucHien, 
    			@SoHopDong, 
    			@DmHinhThucQuangCaoREF,
    			@DmSanPhamREF,
    			@TenSanPham,
    			@DmWebsiteREF,
    			@TenWebsite
    		
    		FETCH NEXT FROM record_cursor INTO @SoHopDong, @DmHinhThucQuangCaoREF, @DmSanPhamREF, @TenSanPham, @DmWebsiteREF, @TenWebsite
    	END
    	CLOSE record_cursor;
    	DEALLOCATE record_cursor;
    	
    	-- insert du lieu khong co hop dong
    	EXEC dbo.ThucChayDaTinhBoxappSSV_InsertNoContract @NgayThucHien
    	
    	SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
    END
    
    -- Update gia tri thay doi
    EXEC ThucChayDaTinh_UpdateGiaTriThayDoi_BoxAppSSV 
		@StartDate
		,@EndDate
		,@DmSanPhamREF
		,@DmHinhThucQuangCaoREF;
END

```
