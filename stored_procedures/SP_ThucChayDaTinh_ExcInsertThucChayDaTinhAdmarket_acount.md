# Stored Procedure: `ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_acount`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-19 16:27:53.910000
- **Ngày sửa cuối**: 2015-07-09 11:48:44.520000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@TaiKhoan` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_acount] '2015-06-25','2015-06-25','thegioixedien',628
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_acount]
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@TaiKhoan NVARCHAR(50),
	@DmSanPhamREF int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	--Ngay nap tien gan nhat so voi ngay tinh lai du lieu
    DECLARE @NgayNapTienGanNhat DATETIME
    -- Insert statements for procedure here

    SET @NgayNapTienGanNhat = (SELECT TOP 1 LastDateRecharge
                                 FROM AdmarketUserLastRecharge
                               WHERE UserName = @TaiKhoan
									 --AND DmSanPhamREF = @DmSanPhamREF
									 AND CONVERT(DATE,LastDateRecharge) < @FromDate
                               ORDER BY LastDateRecharge desc)
    UPDATE HopDongAdmarketCanhBao
    SET RecordStatus = 0 WHERE Convert(DATE,NgayThucHien) BETWEEN CONVERT(DATE,@NgayNapTienGanNhat) AND @FromDate
    AND TK_Admarket = @TaiKhoan AND DmSanPhamREF = @DmSanPhamREF
    	
    EXEC dbo.[ThucChaySelfServingUsers_Insert_haidh] @FromDate, @FromDate
    DELETE FROM ThucChaySelfServingUsers WHERE 
												username <> @TaiKhoan 
												AND DmSanPhamREF <> @DmSanPhamREF
	DELETE FROM ThucChayAdmarketOnline WHERE
											TaiKhoan = @TaiKhoan 
											AND CONVERT(DATE,NgayThucHien) >=  @FromDate  
											AND DmSanPhamREF = @DmSanPhamREF

	DELETE  FROM ThucChayDaTinhAdmarket WHERE 
												 CONVERT(DATE,NgayThucHien) >=  @FromDate  
												AND DmSanPhamREF = @DmSanPhamREF
												AND HopDongChiTietREF IN (SELECT HopDongChiTietID
																			FROM HopDong hd INNER JOIN HopDongChiTiet hdct 
																			ON hd.HopDongID = hdct.HopDongFK
																			WHERE DmSanPhamREF = @DmSanPhamREF AND hdct.TK_AdMarket = @TaiKhoan AND hdct.DeletedStatus <> 1
																			AND hd.TrangThaiHopDong <> 3 )                              


	DELETE FROM HopDongAdmarketCanhBao WHERE CONVERT(DATE,NgayThucHien) >=  @FromDate  
	AND TK_Admarket = @TaiKhoan AND DmSanPhamREF = @DmSanPhamREF
	
	EXEC [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_doannv] @FromDate,@FromDate,@TaiKhoan,@DmSanPhamREF
END


```
