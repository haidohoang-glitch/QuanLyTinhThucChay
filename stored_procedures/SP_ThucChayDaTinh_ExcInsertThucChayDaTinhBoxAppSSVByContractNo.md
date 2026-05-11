# Stored Procedure: `ThucChayDaTinh_ExcInsertThucChayDaTinhBoxAppSSVByContractNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 14:43:10.960000
- **Ngày sửa cuối**: 2017-02-27 18:41:58.377000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
-- EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhBoxAppSSVByContractNo '2014-08-29', '2014-08-29', 'qc1490813'
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhBoxAppSSVByContractNo]
	-- Add the parameters for the stored procedure here
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@SoHopDong	NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @NgayThucHien			DATETIME;
    DECLARE @DmSanPhamREF			INT,
			@DmWebsiteREF			INT,
			@DmHinhThucQuangCaoREF	INT,
			@TenSanPham				NVARCHAR(50),
			@TenWebsite				NVARCHAR(50)
			
    
    -- Xoa du lieu truoc khi insert neu da ton tai
    DELETE FROM ThucChayDaTinh 
    WHERE NgayThucHien BETWEEN @StartDate AND @EndDate 
		AND DmSanPhamREF = 375 AND SoHopDong = @SoHopDong 

    SET @NgayThucHien = @StartDate
    
    WHILE @NgayThucHien <= @EndDate
    BEGIN
    	DECLARE record_cursor CURSOR FOR
    	SELECT A.SoHopDong, A.DmHinhThucQuangCao, A.DmSanPhamREF, A.TenSanPham, A.DmWebsiteREF, A.TenWebsite
    	FROM ThucChayDaTinhBoxAppSSV A    		
    	WHERE A.NgayThucHien = @NgayThucHien
    		AND A.SoHopDong = @SoHopDong
    	
    	OPEN record_cursor
    	
    	FETCH NEXT FROM record_cursor INTO  @SoHopDong, @DmHinhThucQuangCaoREF, @DmSanPhamREF, @TenSanPham, @DmWebsiteREF, @TenWebsite
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
    	
    	SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
    END
END

```
