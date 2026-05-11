# Stored Procedure: `ThucChayDaTinh_ExcInsertThucChayDaTinhGG_FB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-04 12:08:12.533000
- **Ngày sửa cuối**: 2015-05-11 15:07:04.580000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@startDate` | `datetime(8)` | No |
| `@endDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
	exec ThucChayDaTinh_ExcInsertThucChayDaTinhGG_FB '2015-05-04','2015-05-04'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhGG_FB]
-- Add the parameters for the stored procedure here
	@startDate DATETIME,
	@endDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @ngayThucHien  DATETIME,
	        @account       NVARCHAR(50),
	        @sanPhamId     INT,
	        @type          NVARCHAR(50)
	
	SET @ngayThucHien = @startDate;
	--Insert Thong tin nhieu tai khoan tren 01 phan bo
	EXEC dbo.HopDongChiTietGoogleFacebook_InsertMultileAccount @endDate
	WHILE @ngayThucHien <= @endDate
	BEGIN
	    --Day thong tin du lieu vao table tam de tinh	
	    EXEC dbo.ThucChayGoogleFacebookByDay_InsertDataByDay @ngayThucHien	
	    DECLARE acc_cursor CURSOR  
	    FOR
	        SELECT DISTINCT
	               A.NgayThucHien,
	               A.TaiKhoan,
	               A.DmSanPhamREF,
	               A.[Type]
	        FROM   ThucChayGoogleFacebookByDay A
	        WHERE  1 = 1
	        --AND A.TaiKhoan IN ('TH True Milk')
	               AND A.NgayThucHien = @ngayThucHien
	            
	    
	    OPEN acc_cursor
	    
	    FETCH NEXT FROM acc_cursor INTO @ngayThucHien, @account, @sanPhamId, @type
	    
	    WHILE @@FETCH_STATUS = 0
	    BEGIN
	        EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhGG_FB 
	             @ngayThucHien,
	             @account,
	             @sanPhamId,
	             @type
	        
	        FETCH NEXT FROM acc_cursor INTO @ngayThucHien, @account, @sanPhamId, @type
	    END
	    
	    CLOSE acc_cursor
	    DEALLOCATE acc_cursor
	    
	    -- Update gia tri thay doi
	    
	    EXEC dbo.ThucChayDaTinh_GG_FB_UpdateGiaTriThayDoi @ngayThucHien
	    
	    -- Tinh du lieu trong bang online
	    EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_Online_By_NgayThucHien @NgayThucHien
	    
	    SET @ngayThucHien = DATEADD(d, 1, @ngayThucHien);
	END
END

```
