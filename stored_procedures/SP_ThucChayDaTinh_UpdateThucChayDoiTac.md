# Stored Procedure: `ThucChayDaTinh_UpdateThucChayDoiTac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-21 16:27:23.860000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.373000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-05-20
-- Description:	<Description,,>
-- =============================================
-- EXEC dbo.ThucChayDaTinh_UpdateThucChayDoiTac 549, 137

CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateThucChayDoiTac]
	-- Add the parameters for the stored procedure here
	@StartDate		DATETIME,
	@EndDate		DATETIME,
	@DmSanPhamREF	INT,
	@DmWebsiteREF	INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Delta	FLOAT = 0,
			@TyLe	FLOAT = 0,
			@Count	INT	  = 0
			
	DECLARE @ThucChayDaTinhID				NVARCHAR(50),
			@ThanhTienSauTrietKhauThucChay	FLOAT = 0,
			@GiaTriThayDoi					FLOAT = 0,
			@TongGiaTriThucChay				FLOAT = 0,
			@ThanhTienThucChayNew			FLOAT = 0
	
	SET @Delta = 213510000.9
	
	SELECT @TongGiaTriThucChay = SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) 
	FROM ThucChayDaTinh tcdt
	WHERE 
		tcdt.DmSanPhamREF = @DmSanPhamREF
		AND tcdt.DmWebsiteREF = @DmWebsiteREF
		AND tcdt.NgayThucHien BETWEEN @StartDate AND @EndDate
		AND tcdt.SoHopDong = 'QC1611112'
		
		
	DECLARE tc_cursor CURSOR FOR
	SELECT 
		A.ThucChayDaTinhID, A.ThanhTienSauTrietKhauThucChay, A.GiaTriThayDoi
	FROM ThucChayDaTinh A
	WHERE
		A.DmSanPhamREF = @DmSanPhamREF
		AND A.DmWebsiteREF = @DmWebsiteREF
		AND A.NgayThucHien BETWEEN @StartDate AND @EndDate
		AND A.SoHopDong = 'QC1611112'
		
	OPEN tc_cursor
	FETCH NEXT FROM tc_cursor INTO @ThucChayDaTinhID, @ThanhTienSauTrietKhauThucChay, @GiaTriThayDoi
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @TyLe = @ThanhTienSauTrietKhauThucChay/@TongGiaTriThucChay
		SET @ThanhTienThucChayNew = @ThanhTienSauTrietKhauThucChay - (@TyLe*@Delta)-- - @GiaTriThayDoi
		
		PRINT 'ThucChayNew: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChayNew);

		UPDATE ThucChayDaTinh
			SET ThanhTienSauTrietKhauThucChay = @ThanhTienThucChayNew
		WHERE ThucChayDaTinhID = @ThucChayDaTinhID
		
		FETCH NEXT FROM tc_cursor INTO @ThucChayDaTinhID, @ThanhTienSauTrietKhauThucChay, @GiaTriThayDoi
	END
	
	CLOSE tc_cursor
	DEALLOCATE tc_cursor
END

```
